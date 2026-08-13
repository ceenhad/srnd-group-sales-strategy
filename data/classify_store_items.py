#!/usr/bin/env python3
"""Recover product categories for `SRND Store Sales` rows from their item descriptions.

Why this exists: the Shopify integration posts every store order to a single nominal
account, `SRND Store Sales`, so 416 rows and just over half of SRND Group's revenue
arrive with no product category. The item description survives, in the form
"<Contact> - <Item>", so the category is recoverable by rule.

This is a DERIVED, REVIEWABLE classification — assigned by keyword rule here, not by
the business. It is written to a separate `category` column; the account-derived
`product_line` is never overwritten. Anything unmatched is labelled `Unclassified`
rather than guessed, so the gap stays visible.

Outputs:
  data/derived/srnd-account-transactions.csv        rewritten with 3 added columns
  data/derived/srnd-store-item-categories.csv       item -> category, for review

Usage:
    python data/classify_store_items.py
"""
import csv, re, collections, openpyxl, datetime

SRC = 'data/source/SRND Group - Account Transactions.xlsx'
CSV = 'data/derived/srnd-account-transactions.csv'
REVIEW = 'data/derived/srnd-store-item-categories.csv'
STORE_ACCOUNT = 'SRND Store Sales'

# Ordered rules: FIRST match wins, so the specific must precede the general.
# e.g. "Fabric Walls Tool" is a tool, not a fabric wall; an Ultrasuede *sample* is a
# sample, not fabric revenue; a Leyard *services* line is a service, not an LED wall.
RULES = [
    # --- adjustments and logistics first: they mention products but are not product sales
    (r'\bshipping\b|\bdhl\b|incoterms|shipping from', 'Shipping'),
    (r'refund discrepancy|payment received|payment for order|downpayment|prepaid', 'Payments & adjustments'),
    (r'rush fee|urgent delivery|additional charges|additional charge|second visit|extra for the', 'Surcharges'),

    # --- services
    (r'design package|design service|design project|project discovery|project drawings|'
     r'build guide|technical architecture|design optimised|design,|\bredesign\b|'
     r'calibration|commissioning support|installation support|labour and travel|'
     r'annual service|professional services|gold tier|software configuration|'
     r'pixel layout|\bbom\b|isolation details', 'Services — design, commissioning & support'),

    # --- tools and samples
    (r'fabric walls tool', 'Tools'),
    (r'\bsample\b|large sample', 'Fabric samples'),

    # --- LED
    (r'komodo|led video wall', 'LED video walls'),
    (r'pixlite|advatek|\bpsu\b|meanwell|vlight interface|lwlm|perpetual license|'
     r'media server|micro media server|\bpoet\b', 'LED control, power & software'),
    (r'led tape|rgbw', 'LED tape'),
    (r'led profile|surface mount profile|surface mount 35mm|led profiles|'
     r'illumination stair|opal diffuser', 'LED profile'),

    # --- projection
    (r'port hole|porthole|\bphg-\b|optical clear glass|optical glass|custom sized glass|'
     r'glass only|glass panel', 'Port holes & glass'),
    (r'hush box|\bhb\b|dt-hb|dt-ent-hb|dt-hbo', 'Hush boxes'),
    (r'mirror mount|mirror unit|mirror drop|vmm|custom mirror|ceiling mount|'
     r'linear actuator|dt-cm|acoustic isolator for dt', 'Mounts & mirrors'),
    (r'tension band|masking motor|dynamic commander|actuator v3 controller', 'Screen accessories'),
    (r'image surface|dt-is-|atstudio screen surface|black backing|black backing for', 'Image surfaces'),
    # DYN4XL / DYN-2S etc: match the model prefix, not a bare word — "DYN4XL" has no \b after DYN
    (r'masking screen|\bdyn[\d-]|dt-dyn|dynamic 2|dynamic 4|\bmask 2|dt-mask', 'Masking screens'),
    (r'frontier|contempo|dt-frnt|dt-cntp|fixed projection screen|outline fixed', 'Fixed & specialist screens'),
    (r'projector\b|heimdall|balder|i600|zoom lens|lens option|bar-fldx|\ben6\d\b|\bild6\b',
     'Projectors & lenses'),
    (r'screen wall|dt-sw-led|modular screen wall|acusti cubes', 'Screen walls'),

    # --- fabric walls
    (r'fabric track', 'Fabric track'),
    (r'fw frame|aluminium fabric frame|aluminium frame system|fabric frame|'
     r'silicon edge fabric|supply of fabric|extra fabric|wrapped aluminium|wrapped profiles',
     'Fabric wall frames & panels'),
    (r'ultrasuede|showtex|aura flex|diffusion fabric', 'Fabrics'),

    # --- acoustics
    (r'sylomer|barite|\bmp5a\b|isolation bracket|isolation mount|isolation back box|'
     r'channel clip|sound isolation', 'Sound isolation'),
    (r'control panel|foam panel|foam sheet|acoustic foam|acoustic panels|'
     r'acoustic materials|front wall panels|acoustic treatment', 'Acoustic treatment'),

    # --- audio
    (r'amplifier|pf-a-|dp4000|\btdc-\b', 'Amplifiers'),
    (r'theatron|magt-|\bmag\b|flyte|phasetech|\bci\d|\bpt-diw\b|soundbar|subwoofer|wall mount',
     'Speakers'),

    # --- other
    (r'madvr|mad vr|video processor', 'Video processors'),
    (r'mistral|inline fan|fan controller', 'Airflow'),
    (r'sylvox|cinema pro 75', 'Displays'),
    # a named-room interior supply, distinct from the design packages caught by the
    # services rule above ("Enhanced Cinema Interior Design Package" matches there first)
    (r'cinema interior', 'Cinema interiors'),
    (r'stereo camera|\bzed 2i\b', 'Sensors'),
    (r'colour matching|\bral\b|custom colour|powder coat', 'Finishes & colour'),
]

COMPILED = [(re.compile(p, re.I), c) for p, c in RULES]

# The rule names above and Xero's own account names collide on case and synonyms, which
# would show the same category twice in any aggregate. Harmonise onto the account name —
# the company's own vocabulary — for these unambiguous pairs only.
#
# NOT harmonised, deliberately: masking screens, fixed & specialist screens, image
# surfaces, screen accessories, port holes, hush boxes and fabric wall frames are all
# FINER than the account set (which lumps them into "Projection Screens" or has no line
# at all). Recovering that detail is the point of this exercise, so it is kept.
CANONICAL = {
    'Acoustic treatment': 'Acoustic Treatment',
    'LED video walls': 'LED Video Walls',
    'LED tape': 'LED Tape',
    'LED profile': 'LED Profile',
    'LED control, power & software': 'LED Control and Power',
    'Video processors': 'Video Processors',
    'Sound isolation': 'Sound Isolation',
    'Screen walls': 'Screen Walls',
    'Projectors & lenses': 'Projectors',
    'Mounts & mirrors': 'Projector Mounts',
    'Amplifiers': 'Audio Amplifiers',
    # the Xero account is spelled "Audio Amplfiers" — corrected here and worth fixing at source
    'Audio Amplfiers': 'Audio Amplifiers',
}


def classify(item: str) -> str:
    for rx, cat in COMPILED:
        if rx.search(item):
            return cat
    return 'Unclassified'


def strip_contact(desc: str, contact: str) -> str:
    if contact and desc.lower().startswith(contact.lower()):
        return desc[len(contact):].lstrip(' -').strip()
    if ' - ' in desc:
        return desc.split(' - ', 1)[1].strip()
    return desc


def read_source():
    """(date, reference, account, description, contact) per transaction row, in file order."""
    ws = openpyxl.load_workbook(SRC, read_only=True, data_only=True)['Account Transactions']
    current = ''
    for r in [list(x) for x in ws.iter_rows(values_only=True)][5:]:
        head = r[0]
        if isinstance(head, datetime.datetime):
            yield dict(date=head.date().isoformat(), ref=(r[3] or '').strip(),
                       account=(r[9] or '').strip(), desc=(r[2] or '').strip(),
                       contact=current)
        elif isinstance(head, str) and head.strip():
            s = head.strip()
            current = '' if (s.lower() == 'total' or s.lower().startswith('total ')) else s


def main():
    rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
    source = list(read_source())
    if len(rows) != len(source):
        raise SystemExit(f'row mismatch: {len(rows)} in csv vs {len(source)} in source — '
                         'regenerate with normalise.py first')

    review = collections.defaultdict(lambda: [0, 0.0, ''])
    for row, src in zip(rows, source):
        # sanity: the two files must be describing the same transaction
        assert row['invoice_date'] == src['date'] and row['account_raw'] == src['account']
        item = strip_contact(src['desc'], src['contact'])
        row['description'] = src['desc']
        row['item_description'] = item
        if src['account'] == STORE_ACCOUNT:
            cat = classify(item)
            row['category'] = CANONICAL.get(cat, cat)
            row['category_source'] = 'description-rule' if cat != 'Unclassified' else 'unclassified'
            r = review[item]
            r[0] += 1
            r[1] += float(row['net'] or 0)
            r[2] = row['category']
        else:
            row['category'] = CANONICAL.get(row['product_line'], row['product_line'])
            row['category_source'] = 'account'

    fields = list(rows[0].keys())
    with open(CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with open(REVIEW, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['item_description', 'assigned_category', 'rows', 'net'])
        for item, (n, net, cat) in sorted(review.items(), key=lambda x: -x[1][1]):
            w.writerow([item, cat, n, round(net, 2)])

    store = [r for r in rows if r['account_raw'] == STORE_ACCOUNT]
    total = sum(float(r['net'] or 0) for r in store)
    uncl = [r for r in store if r['category'] == 'Unclassified']
    print(f'{len(store)} store rows, {len(review)} distinct items, GBP {round(total):,}')
    print(f'unclassified: {len(uncl)} rows, GBP {round(sum(float(r["net"] or 0) for r in uncl)):,} '
          f'({100*sum(float(r["net"] or 0) for r in uncl)/total:.1f}% of store value)')
    by = collections.defaultdict(float)
    for r in store:
        by[r['category']] += float(r['net'] or 0)
    print('\ncategory                                        net      % of store')
    for c, v in sorted(by.items(), key=lambda x: -x[1]):
        print(f'  {c:<44} {round(v):>10,}   {100*v/total:5.1f}%')


if __name__ == '__main__':
    main()

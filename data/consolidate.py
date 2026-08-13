#!/usr/bin/env python3
"""Join every per-entity extract into one analysis table: data/derived/all-transactions.csv

Why: five workbooks became five CSVs with three different notions of "product line" —
GTUK's are third-party BRAND names, DT's and SRND's are product CATEGORIES, C-ATS's and
Light Walls' are internal lines. Any group-level question needed a bespoke script. This
produces one table where every row carries a harmonised `category`, a `supply` class
(own-made / carried / services), and the `carried_brand` where there is one.

Nothing is discarded: the source's own wording stays in `account_raw` and `product_line`,
and the added columns sit alongside. Unmappable lines are labelled `Unclassified` and
listed in data/derived/consolidation-review.csv rather than guessed at.

Run after normalise.py (all sources) and classify_store_items.py:
    python data/consolidate.py
"""
import csv, os, re, collections

DERIVED = 'data/derived'
OUT = os.path.join(DERIVED, 'all-transactions.csv')
REVIEW = os.path.join(DERIVED, 'consolidation-review.csv')

SOURCES = [
    ('gtuk-invoice-lines.csv',            'GTUK / Apex Tech Scotland Ltd', 'UK distribution'),
    ('dt-invoice-lines.csv',              'Display Technologies',          'own-brand manufacturer'),
    ('cats-account-transactions.csv',     'C-ATS',                         'own-brand manufacturer'),
    ('lightwalls-account-transactions.csv','Light Walls',                  'own-brand manufacturer'),
    ('srnd-account-transactions.csv',     'SRND Group Ltd',                'hybrid distributor/manufacturer'),
]

COLUMNS = ['source_file','entity','entity_role','invoice_number','invoice_date','year',
           'item_code','quantity','contact_raw','contact_canonical','status',
           'account_raw','product_line','category','category_source','carried_brand','supply',
           'net','is_product_revenue','is_intra_group','description','item_description']

# ---------------------------------------------------------------- GTUK brand lines
# (category, carried_brand, supply). Brand identifications are from the account name only.
# Lines whose product category is genuinely unknown are left None and reported for review —
# NOT guessed. Together the unknowns are material, so read the review file before using
# `category` on GTUK rows.
GTUK = {
    'BARCO':            ('Projectors',            'Barco',            'carried'),
    'STEALTH':          ('Speakers',              'Stealth Acoustics','carried'),
    'DT SCREENS':       ('Projection screens',    None,               'own-made'),
    'LEON':             ('Speakers',              'Leon Speakers',    'carried'),
    'ADA':              ('Amplifiers',            'ADA',              'carried'),
    'DPI':              ('Projectors',            'Digital Projection','carried'),
    'madVR':            ('Video processors',      'madVR',            'carried'),
    'DATASAT':          ('Audio processing',      'Datasat',          'carried'),
    'CINEMATECH':       ('Seating',               'CinemaTech',       'carried'),
    'WISDOM':           ('Speakers',              'Wisdom Audio',     'carried'),
    'KALEIDESCAPE':     ('Media servers',         'Kaleidescape',     'carried'),
    'ACURUS':           ('Amplifiers',            'Acurus',           'carried'),
    'STEWART':          ('Projection screens',    'Stewart',          'carried'),
    'CATS':             ('Acoustic treatment',    None,               'own-made'),
    'PHASE TECHNOLOGY': ('Speakers',              'Phase Technology', 'carried'),
    'SOLID DRIVE':      ('Speakers',              'SolidDrive',       'carried'),
    'CINEVERSUM':       ('Projectors',            'CineVersum',       'carried'),
    'BARRISOL COUTURE': ('Fabric wall frames',    'Barrisol',         'carried'),
    'DNP':              ('Projection screens',    'DNP',              'carried'),
    'LUMAGEN':          ('Video processors',      'Lumagen',          'carried'),
    'AERIAL':           ('Speakers',              'Aerial',           'carried'),
    'STRAIGHTWIRE':     ('Cables & distribution', 'Straight Wire',    'carried'),
    'PRISMASONIC':      ('Lenses & optics',       'Prismasonic',      'carried'),
    'STORM AUDIO':      ('Audio processing',      'StormAudio',       'carried'),
    'VIVADI':           ('Media servers',         'Vivadi',           'carried'),
    'XPAND':            ('Other',                 'XPAND',            'carried'),
    'QUESTED':          ('Speakers',              'Quested',          'carried'),
    'INTEGRA':          ('Amplifiers',            'Integra',          'carried'),
    'KEY DIGITAL':      ('Cables & distribution', 'Key Digital',      'carried'),
    'ARAGON':           ('Amplifiers',            'Aragon',           'carried'),
    'SEATING':          ('Seating',               None,               'carried'),
    'SERVICES':         ('Services',              None,               'services'),
    'CINEMA PARTNERS SERVICES': ('Services',       None,              'services'),
    'CINEMA PARTNERS MATERIALS':(None,             None,              'carried'),
    # --- identified by Neil, 2026-08-13
    'NEXTGENTECH':      ('Audio over IP',         'NextGen Tech',     'carried'),
    'PRO AUDIO':        ('Speakers & amplifiers', 'Pro Audio',        'carried'),
    'AGATH':            ('Mirror TVs',            'Agath',            'carried'),
    'TPI Cinema':       ('Speakers & amplifiers', 'TPI',              'carried'),
    'IMAGE':            ('Projection screens',    'Image',            'carried'),
    'LEAF':             ('Cables & distribution', 'Leaf',             'carried'),
    # High Tech Couture — Simon's operation under Neil, fabric-wall work. Marked own-made
    # on that basis; Barrisol stays carried because the underlying product is Barrisol's.
    'HTC':              ('Fabric wall frames',    None,               'own-made'),
    # still unidentified — see review file
    'OTHERS': (None, None, None),
}

# `Speakers & amplifiers` exists because two carried lines — Pro Audio and TPI — are each
# "speakers and amps" (Neil) and cannot be split. It rolls into audio alongside Speakers,
# Amplifiers, Audio processing and Audio over IP; treat it as audio, never as speakers alone.
AUDIO_CATEGORIES = {'Speakers', 'Amplifiers', 'Audio processing',
                    'Speakers & amplifiers', 'Audio over IP'}

# ---------------------------------------------------------------- DT SKU prefixes
# DT's store blob (372 rows, GBP 905k) carries structured SKUs on 257 of them.
DT_SKU = [
    (r'^DT-DYN|^DT-ES-MASK|^DT-MASK', 'Masking screens'),
    (r'^DT-VMM|^DT-MMD|^DT-M-C|^DT-M\d|^DT-CM',  'Mounts & mirrors'),
    (r'^DT-HB|^DT-ENT-HB|^DT-HBO',    'Hush boxes'),
    (r'^DT-PHG|^DT-PH',               'Port holes & glass'),
    (r'^DT-FRNT|^DT-CNTP',            'Fixed & specialist screens'),
    (r'^DT-IS|^DT-S-TENSION',         'Image surfaces'),
    (r'^DT-SW',                       'Screen walls'),
    (r'^DT-ISO',                      'Sound isolation'),
]
DT_SKU = [(re.compile(p, re.I), c) for p, c in DT_SKU]

# DT's own account names -> canonical categories
DT_ACCOUNT = {
    'Motorised On Wall Screens': 'Masking screens',
    'Non Motorised On Wall Screens': 'Projection screens',
    'Port Hole Glass': 'Port holes & glass',
    'Non Motorised Mount Solutions': 'Mounts & mirrors',
    'Motorised Mount Solutions': 'Mounts & mirrors',
    'Image Surfaces': 'Image surfaces',
    'Other Screens': 'Projection screens',
    'Bespoke Solutions': 'Bespoke',
    'Hush Boxes': 'Hush boxes',
    'Mechanics': 'Screen accessories',
    'Mistral': 'Airflow',
    'Others': None,
}
CATS_ACCOUNT = {
    'C-ATS Reflection': 'Acoustic treatment', 'C-ATS Reverberation': 'Acoustic treatment',
    'C-ATS Resonance': 'Acoustic treatment', 'CATS Packs': 'Acoustic treatment',
    'CATS Complete': 'Acoustic treatment', 'Design Services': 'Services',
}
LW_ACCOUNT = {'Light Walls': 'LED lighting systems', 'Protopixel': 'LED control & software',
              'Sales': None}
# SRND: `category` is already harmonised by classify_store_items.py; map its names on.
SRND_CATEGORY = {
    'LED Video Walls': ('LED video walls', 'Leyard', 'carried'),
    'Projectors': ('Projectors', None, 'carried'),
    'Video Processors': ('Video processors', None, 'carried'),
    'Speakers': ('Speakers', None, 'carried'),
    'Audio Amplifiers': ('Amplifiers', None, 'carried'),
    'Displays': ('Displays', None, 'carried'),
    'Sensors': ('Sensors', None, 'carried'),
    'LED Control and Power': ('LED control & software', None, 'carried'),
    'Fabrics': ('Fabrics', None, 'carried'),
    'Fabric samples': ('Fabrics', None, 'carried'),
    'Metal Fabric Track': ('Fabric track', None, 'own-made'),
    'Plastic Fabric Track': ('Fabric track', None, 'own-made'),
    'Fabric track': ('Fabric track', None, 'own-made'),
    'Fabric wall frames & panels': ('Fabric wall frames', None, 'own-made'),
    'Masking screens': ('Masking screens', None, 'own-made'),
    'Projection Screens': ('Projection screens', None, 'own-made'),
    'Fixed & specialist screens': ('Fixed & specialist screens', None, 'own-made'),
    'Image surfaces': ('Image surfaces', None, 'own-made'),
    'Screen accessories': ('Screen accessories', None, 'own-made'),
    'Port holes & glass': ('Port holes & glass', None, 'own-made'),
    'Hush boxes': ('Hush boxes', None, 'own-made'),
    'Projector Mounts': ('Mounts & mirrors', None, 'own-made'),
    'Mounts & mirrors': ('Mounts & mirrors', None, 'own-made'),
    'Screen Walls': ('Screen walls', None, 'own-made'),
    'Acoustic Treatment': ('Acoustic treatment', None, 'own-made'),
    'Sound Isolation': ('Sound isolation', None, 'own-made'),
    'LED Tape': ('LED tape', None, 'own-made'),
    'LED Profile': ('LED profile', None, 'own-made'),
    'Airflow': ('Airflow', None, 'own-made'),
    'Cinema interiors': ('Cinema interiors', None, 'own-made'),
    'Tools': ('Tools', None, 'own-made'),
    'Finishes & colour': ('Finishes & colour', None, 'own-made'),
    'Services — design, commissioning & support': ('Services', None, 'services'),
    'Project Design': ('Services', None, 'services'),
    'On Site Services': ('Services', None, 'services'),
    'Project Services': ('Services', None, 'services'),
    'Product Design': ('Services', None, 'services'),
    'Shipping': ('Shipping', None, 'other'),
    'Surcharges': ('Surcharges', None, 'other'),
    'Payments & adjustments': ('Payments & adjustments', None, 'other'),
    'Sales': (None, None, None),
}


def classify(row, entity):
    """-> (category, category_source, carried_brand, supply)"""
    line = row.get('product_line') or ''
    if entity.startswith('GTUK'):
        cat, brand, supply = GTUK.get(line, (None, None, None))
        return cat, 'brand-map' if cat else 'unclassified', brand, supply
    if entity == 'Display Technologies':
        if line == 'DT Store Sales':
            code = row.get('item_code') or ''
            for rx, cat in DT_SKU:
                if rx.search(code):
                    return cat, 'sku-prefix', None, 'own-made'
            return None, 'unclassified', None, 'own-made'
        cat = DT_ACCOUNT.get(line)
        return cat, 'account' if cat else 'unclassified', None, 'own-made'
    if entity == 'C-ATS':
        cat = CATS_ACCOUNT.get(line)
        supply = 'services' if cat == 'Services' else 'own-made'
        return cat, 'account' if cat else 'unclassified', None, supply
    if entity == 'Light Walls':
        cat = LW_ACCOUNT.get(line)
        supply = 'carried' if line == 'Protopixel' else 'own-made'
        brand = 'ProtoPixel' if line == 'Protopixel' else None
        return cat, 'account' if cat else 'unclassified', brand, supply
    if entity == 'SRND Group Ltd':
        cat, brand, supply = SRND_CATEGORY.get(row.get('category') or '', (None, None, None))
        src = row.get('category_source') or 'account'
        return cat, src if cat else 'unclassified', brand, supply
    return None, 'unclassified', None, None


def main():
    out, review = [], collections.defaultdict(lambda: [0, 0.0])
    for fn, entity, role in SOURCES:
        for row in csv.DictReader(open(os.path.join(DERIVED, fn), encoding='utf-8')):
            cat, src, brand, supply = classify(row, entity)
            rec = {c: row.get(c, '') for c in COLUMNS}
            rec.update(source_file=fn, entity=entity, entity_role=role,
                       category=cat or 'Unclassified', category_source=src,
                       carried_brand=brand or '', supply=supply or 'unknown')
            out.append(rec)
            if not cat and row['is_product_revenue'] == '1':
                k = (entity, row.get('product_line') or '(blank)')
                review[k][0] += 1
                review[k][1] += float(row['net'] or 0)

    with open(OUT, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(out)
    with open(REVIEW, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['entity', 'product_line', 'rows', 'net', 'note'])
        for (e, l), (n, v) in sorted(review.items(), key=lambda x: -abs(x[1][1])):
            w.writerow([e, l, n, round(v, 2), 'category unidentified — needs a human'])

    rev = [r for r in out if r['is_product_revenue'] == '1']
    tot = sum(float(r['net'] or 0) for r in rev)
    unc = sum(float(r['net'] or 0) for r in rev if r['category'] == 'Unclassified')
    print(f'{OUT}: {len(out)} rows from {len(SOURCES)} sources')
    print(f'  product revenue GBP {round(tot):,} | unclassified GBP {round(unc):,} '
          f'({100*unc/tot:.1f}%) across {len(review)} lines -> {REVIEW}')


if __name__ == '__main__':
    main()

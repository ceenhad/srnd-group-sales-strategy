#!/usr/bin/env python3
"""Flatten a Monday.com board export into CSV.

Monday exports are grouped boards, which means the sheet is not a table:

    row 1        board title
    row 2        board description / help text
    row 4        GROUP NAME          <- e.g. "Closed Lost"
    row 5        column headers      <- repeated for every group
    rows 6..n    items
    ...          GROUP NAME again, headers again, items again

**The group name carries meaning and must be kept** — on the Deals board the groups are
the outcome (Active Deals / Closed Won / Closed Lost / Complete), which is the only
win/loss signal in the export. It is written to a `board_group` column.

The Deals board additionally interleaves SUBITEM blocks: a `Subitems` header row followed
by sub-deal rows, sitting between parent deal rows. Those have a different shape and are
written to a separate file, tagged with the parent deal they sit under.

Usage:
    python data/normalise_monday.py
"""
import csv, os, openpyxl

SRC = 'data/source'
OUT = 'data/derived'

BOARDS = [
    ('Monday - SRND Deals.xlsx',    'monday-deals.csv',    'deals'),
    ('Monday - SRND Accounts.xlsx', 'monday-accounts.csv', 'accounts'),
    ('Monday - Leads.xlsx',         'monday-leads.csv',    'leads'),
    ('Monday - SRND Contacts.xlsx', 'monday-contacts.csv', 'contacts'),
]


def dedupe(headers):
    """Monday allows duplicate column names (Leads has 'Role' twice). Suffix repeats."""
    seen, out = {}, []
    for h in headers:
        h = (str(h).strip() if h is not None else '')
        if not h:
            h = 'col'
        if h in seen:
            seen[h] += 1
            h = f'{h}_{seen[h]}'
        else:
            seen[h] = 1
        out.append(h)
    return out


def parse(path):
    """-> (items, item_fields, subitems, subitem_fields)

    Row kinds are decided per row, never by a latching mode — on the Deals board a subitem
    block sits BETWEEN parent rows, so a mode flag swallows every parent after the first
    block (it produced 6 deals instead of 451). **Column A is the discriminator:** a parent
    item populates it; a subitem leaves it blank and starts at column B.
    """
    ws = openpyxl.load_workbook(path, data_only=True).worksheets[0]
    rows = list(ws.iter_rows(values_only=True))

    def cell(v):
        return '' if v is None else str(v).strip()

    # A group row is a single populated cell in column A immediately followed by a header
    # row. Testing the follower avoids mistaking a sparse item for a group.
    group_rows = set()
    for i, row in enumerate(rows):
        populated = [c for c in row if c is not None and str(c).strip() != '']
        if (len(populated) == 1 and cell(row[0]) and i + 1 < len(rows)
                and cell(rows[i + 1][0]) in ('Name', 'Subitems')):
            group_rows.add(i)

    items, subitems = [], []
    item_fields, subitem_fields = [], []
    item_hdr, sub_hdr = [], []
    group, last_parent = '', ''

    for i, row in enumerate(rows):
        first = cell(row[0])
        populated = [c for c in row if c is not None and str(c).strip() != '']

        if i in group_rows:
            group = first
            continue
        if first == 'Name':
            item_hdr = dedupe(row)
            if not item_fields:
                item_fields = [h for h in item_hdr if h]
            continue
        if first == 'Subitems':
            sub_hdr = dedupe(row)
            if not subitem_fields:
                subitem_fields = [h for h in sub_hdr if h]
            continue
        if not populated:
            continue

        def build(hdr):
            rec = {}
            for h, v in zip(hdr, row):
                if h:
                    rec[h] = '' if v is None else (
                        v.isoformat() if hasattr(v, 'isoformat') else str(v))
            return rec

        if first and item_hdr:                      # parent item
            rec = build(item_hdr)
            rec['board_group'] = group
            last_parent = rec.get('Name', '')
            items.append(rec)
        elif not first and sub_hdr:                 # subitem, indented one column
            rec = build(sub_hdr)
            rec['board_group'] = group
            rec['parent_item'] = last_parent
            subitems.append(rec)

    return items, item_fields, subitems, subitem_fields


def write(path, fields, records):
    fields = list(fields)
    for extra in ('board_group', 'parent_item'):
        if any(extra in r for r in records) and extra not in fields:
            fields.append(extra)
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in records:
            w.writerow(r)
    return len(records)


def main():
    for fn, out, kind in BOARDS:
        items, ifields, subs, sfields = parse(os.path.join(SRC, fn))
        n = write(os.path.join(OUT, out), ifields, items)
        groups = {}
        for r in items:
            groups[r['board_group']] = groups.get(r['board_group'], 0) + 1
        print(f'{out}: {n} items, {len(ifields)} columns')
        print('   groups: ' + ', '.join(f'{k or "(none)"}={v}' for k, v in groups.items()))
        if subs:
            sn = write(os.path.join(OUT, 'monday-deal-subitems.csv'), sfields, subs)
            print(f'   monday-deal-subitems.csv: {sn} sub-items, {len(sfields)} columns')


if __name__ == '__main__':
    main()

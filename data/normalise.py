#!/usr/bin/env python3
"""Normalise a Xero sales export into the shared column contract in data/README.md.

Two report types are handled:

  sales-analysis      the Sales Analysis Report — a `Raw Data` sheet, one row per
                      invoice line, with `Contact` and `Net` as columns.
  account-txns        the Account Transactions report — contact appears as a group
                      HEADER ROW rather than a column, and amounts arrive as
                      Debit (GBP) / Credit (GBP), so net = credit - debit.

Usage:
    python data/normalise.py sales-analysis "data/source/DT - ....xlsx" data/derived/dt.csv "Display Technologies"
    python data/normalise.py account-txns   "data/source/C-ATS - ....xlsx" data/derived/cats.csv

For account-txns the entity name is read from the sheet, so the 4th argument is optional.
Every source row is written out; cleaning decisions are carried as the columns
is_product_revenue and is_intra_group, never applied as deletions.
"""
import sys, csv, datetime, openpyxl

COLUMNS = ['entity','invoice_number','invoice_date','year','item_code','quantity',
           'contact_raw','contact_canonical','status','account_raw','product_line',
           'net','is_product_revenue','is_intra_group']

# Settled 2026-08-13. Everything not listed here is external — in particular the two
# Genesis Technologies AG companies and Genesis Home Technologies SL are third parties,
# despite "Genesis Technologies Ltd" appearing as a DESCRIPTION on group invoices.
INTRA_GROUP = {
    'apex tech scotland ltd',
    'apex tech scotland ltd / apex-tech uk',      # Light Walls spelling
    'apex tech international ltd',
    'apex technologies international',
    'srnd group ltd',
    'dzyn ltd',
    'display technologies ltd',
    'display technologies limited',               # Light Walls spelling
    'light walls ltd',
    'cinema acoustic treatment systems limited',
}

# [?] UNRESOLVED — 'Complete-ATS' appears as a Light Walls counterparty. "Complete ATS" is
# the C-ATS vendor name on the store (group/store-split-worklist.md), which suggests a group
# entity, but the C-ATS company is "Cinema Acoustic Treatment Systems Limited". Left EXTERNAL
# pending confirmation; see archive-findings.md. Add it above if it is ours.
UNRESOLVED_ENTITIES = {'complete-ats'}

# Accounts that are not product revenue. Matched as a prefix on the raw account name.
NON_REVENUE_PREFIXES = (
    'Shipping Out','Freight','Warehousing','Wages','VAT','Accounts Receivable',
    'Cost of Sales','Motor Vehicle','Advertising','Postage','Inter Company',
    'Inter-Company','Other Revenue','General Expenses','Bank Fees','Travel',
    'Rounding','Suspense',
    'Sales - Inter Company',    # Light Walls posts group trade to its own sales account
)

# Xero source types that are not a sale to a customer.
NON_SALE_SOURCES = {'payable invoice','spend money','bill','payable credit note'}


def canon(contact: str) -> str:
    """Collapse account names that are the same counterparty."""
    c = contact.strip()
    if c.lower().startswith('apex technologies us'):
        return 'Apex Technologies USA'   # "USA" and "USA LLC" are one entity (Neil)
    if c.lower().startswith('apex tech scotland'):
        return 'Apex Tech Scotland Ltd'  # collapses ".../ Apex-Tech UK"
    if c.lower() == 'display technologies limited':
        return 'Display Technologies Ltd'
    if c.lower() == 'apex tech international ltd':
        return 'Apex Tech International Ltd'   # normalises the lower-case 'apex' spelling
    return c


def is_revenue_account(account) -> bool:
    if account is None:
        return True                      # unattributed, but still revenue
    return not str(account).startswith(NON_REVENUE_PREFIXES)


def product_line(account) -> str:
    if not account:
        return ''
    s = str(account)
    for prefix in ('Sales - Materials - ', 'Sales - Services - ', 'Sales - '):
        if s.startswith(prefix):
            return s[len(prefix):]
    return s


def read_sales_analysis(path, entity):
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)['Raw Data']
    for r in ws.iter_rows(min_row=2, values_only=True):
        inv, date, item, qty, unit, vat, gross, invtot, contact, status, acct, net = r
        d = date.date().isoformat() if isinstance(date, datetime.datetime) else ''
        contact = (contact or '').strip()
        usable = (is_revenue_account(acct) and status not in ('Deleted', 'Draft')
                  and net is not None and bool(d) and bool(contact))
        yield dict(entity=entity, invoice_number=inv or '', invoice_date=d,
                   year=date.year if d else '', item_code=item or '',
                   quantity='' if qty is None else qty,
                   contact_raw=contact, contact_canonical=canon(contact) if contact else '',
                   status=status or '', account_raw=acct or '',
                   product_line=product_line(acct),
                   net='' if net is None else round(float(net), 2),
                   is_product_revenue='1' if usable else '0',
                   is_intra_group='1' if contact.lower() in INTRA_GROUP else '0')


def read_account_txns(path, entity=None):
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)['Account Transactions']
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    entity = entity or (rows[1][0] or '').strip()
    current = ''
    for r in rows[5:]:
        head = r[0]
        if isinstance(head, datetime.datetime):
            source = (r[1] or '').strip()
            acct = (r[9] or '').strip()
            net = round(float(r[8] or 0) - float(r[7] or 0), 2)   # credit - debit
            usable = (is_revenue_account(acct) and bool(current)
                      and source.lower() not in NON_SALE_SOURCES)
            yield dict(entity=entity, invoice_number=(r[3] or '').strip(),
                       invoice_date=head.date().isoformat(), year=head.year,
                       item_code='', quantity='',
                       contact_raw=current, contact_canonical=canon(current) if current else '',
                       status=source, account_raw=acct, product_line=product_line(acct),
                       net=net,
                       is_product_revenue='1' if usable else '0',
                       is_intra_group='1' if current.lower() in INTRA_GROUP else '0')
        elif isinstance(head, str) and head.strip():
            s = head.strip()
            # a "Total <contact>" row closes the group; a bare name opens one
            current = '' if (s.lower() == 'total' or s.lower().startswith('total ')) else s


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    kind, src, dest = sys.argv[1], sys.argv[2], sys.argv[3]
    entity = sys.argv[4] if len(sys.argv) > 4 else None
    if kind == 'sales-analysis':
        if not entity:
            sys.exit('sales-analysis needs an entity name as the 4th argument')
        records = list(read_sales_analysis(src, entity))
    elif kind == 'account-txns':
        records = list(read_account_txns(src, entity))
    else:
        sys.exit('kind must be sales-analysis or account-txns')

    with open(dest, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(records)

    revenue = [r for r in records if r['is_product_revenue'] == '1']
    total = sum(float(r['net']) for r in revenue if r['net'] != '')
    intra = sum(float(r['net']) for r in revenue if r['is_intra_group'] == '1' and r['net'] != '')
    print(f'{dest}: {len(records)} rows, {len(revenue)} product-revenue')
    print(f'  total GBP {round(total):,} = external {round(total-intra):,} + intra-group {round(intra):,}')


if __name__ == '__main__':
    main()

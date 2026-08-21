#!/usr/bin/env python3
"""Mechanical invariants for this repo. Run it before committing.

Every check here exists because it failed on 2026-08-20 and cost a whole session.
It catches only what a machine can catch — the judgement failures are in method.md.
"""
import re, sys, glob, collections

FAIL = []
WARN = []

def md_files():
    return sorted(f for f in glob.glob('**/*.md', recursive=True) if '.git' not in f)

# 1 — no strikethrough. Corrections delete the wrong version (CLAUDE.md).
def check_strikethrough():
    for f in md_files():
        n = open(f).read().count('~~')
        if n:
            FAIL.append(f'{f}: {n} strikethrough markers — a correction deletes the wrong version, it does not strike it')

# 2 — duplicate IDs in a register. A citation must resolve to one row.
def check_duplicate_ids():
    for f in ['registers/backlog.md', 'registers/questions.md']:
        try: s = open(f).read()
        except FileNotFoundError: continue
        ids = re.findall(r'^\| \*?\*?([A-Z]+-[0-9a-z-]+|Q\d+)\b', s, re.M)
        dupes = {k: v for k, v in collections.Counter(ids).items() if v > 1}
        if dupes:
            FAIL.append(f'{f}: duplicate IDs {dupes} — a citation cannot resolve to two rows')

# 3 — table column counts must be uniform per table.
def check_tables():
    strip_code = lambda t: re.sub(r'`[^`]*`', '', t)   # a pipe inside `code` is not a separator
    for f in md_files():
        rows, tbl = [], 0
        for line in open(f).read().split('\n'):
            if line.startswith('|'):
                bare = strip_code(line)
                if re.match(r'^\|[^|]+\|+\s*$', bare):   # a spanning label row: '| Heading ||||'
                    continue
                rows.append(bare.count('|'))
            elif rows:
                if len(set(rows)) > 1:
                    tbl += 1
                rows = []
        if tbl:
            FAIL.append(f'{f}: {tbl} table(s) with ragged column counts')

# 4 — a clarification is never a question for an owner (CLAUDE.md, the bar).
def check_bar():
    try: s = open('registers/backlog.md').read()
    except FileNotFoundError: return
    for line in s.split('\n'):
        m = re.match(r'^\| \*?\*?([A-Z]+-[0-9a-z-]+)\s*\|\s*Ask\s*\|\s*clarification\s*\|', line)
        if m:
            FAIL.append(f'backlog {m.group(1)}: typed Ask with weight clarification — it fails the bar, so it is Do')

# 5 — no Decide type. A decision is a question, asked and answered.
def check_no_decide():
    try: s = open('registers/backlog.md').read()
    except FileNotFoundError: return
    n = len(re.findall(r'^\| \*?\*?[A-Z]+-[0-9a-z-]+\s*\|\s*Decide\s*\|', s, re.M))
    if n:
        FAIL.append(f'backlog: {n} rows typed Decide — that type does not exist; it is Ask (a question) or Do (work)')

# 6 — emphasis density. Above ~8 marks per 100 words nothing reads as emphasised.
def check_emphasis():
    for f in md_files():
        s = open(f).read(); w = len(s.split())
        if w < 300: continue
        d = len(re.findall(r'\*\*|\*', s)) * 100 / w
        if d > 12:
            WARN.append(f'{f}: {d:.0f} emphasis marks per 100 words — nothing reads as emphasised above ~8')

# 7 — register size. open-items.md reached 838 lines because nothing said stop.
def check_size():
    for f in glob.glob('registers/*.md') + ['NEXT.md']:
        n = len(open(f).read().split('\n'))
        if n > 450:
            WARN.append(f'{f}: {n} lines — a register over ~450 lines is becoming a diary; cut it')

# 8 — process narration. The registers are not a session diary.
def check_narration():
    pats = [r'\bI (wrote|had|offered|first|turned|assumed)\b', r'\bmy (error|misreading|own reading)\b',
            r'\b(second|third|fourth|fifth|sixth) (instance|time) (of|this)\b']
    for f in md_files():
        if f in ('method.md',): continue          # method.md is where lessons legitimately live
        s = open(f).read()
        hits = sum(len(re.findall(p, s, re.I)) for p in pats)
        if hits:
            WARN.append(f'{f}: {hits} passage(s) narrating a session\'s own process — keep the finding, drop the diary')

for fn in [check_strikethrough, check_duplicate_ids, check_tables, check_bar,
           check_no_decide, check_emphasis, check_size, check_narration]:
    fn()

for x in FAIL: print('FAIL ', x)
for x in WARN: print('warn ', x)
print(f'\n{len(FAIL)} failures, {len(WARN)} warnings')
sys.exit(1 if FAIL else 0)

"""The ADR index for the group strategy repo, generated from the ADRs themselves.

ADR 0001 makes an ADR a versioned document with a permanent number: a decision
that changes is rewritten in place, `version` and `revised` move, and the number
every citation depends on stays still. Two things have to hold for that to work,
and this script is both of them.

**The catalogue is generated.** `decisions/CATALOGUE.md` is built from the front
matter of every ADR, grouped by functional area. A hand-maintained index rots —
the platform's did, to 41 of 70 in three months with nine rows disagreeing with
their own files.

**The rules are asserted.** `check()` returns one string per breach and the
script exits non-zero if there are any, so it can gate a commit.

    python scripts/adr_catalogue.py            # print the summary and any breaches
    python scripts/adr_catalogue.py --write    # regenerate the tracked catalogue
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECISIONS = ROOT / "decisions"
CATALOGUE = DECISIONS / "CATALOGUE.md"

STATUSES = {"proposed", "accepted", "superseded", "rejected"}

# Area order is the reading order of the catalogue. An unknown area is a breach,
# so adding one is a deliberate act rather than a typo.
AREAS = [
    ("governance", "How this repo decides"),
    ("commercial", "Commercial model, pricing and territory"),
    ("motion", "The sales motion and content"),
    ("record", "The product record"),
    ("partner", "The partner programme"),
    ("brand", "Brands and alignment"),
    ("market", "Markets and events"),
]

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse(path: Path) -> dict:
    """Read one ADR's front matter. Returns a dict with `_path` and `_breaches`."""
    text = path.read_text(encoding="utf-8")
    m = FM.match(text)
    if not m:
        return {"_path": path, "_breaches": [f"{path.name}: no front matter"]}
    data: dict = {"_path": path, "_breaches": [], "_body": text[m.end():]}
    for line in m.group(1).split("\n"):
        if not line.strip() or line.startswith("#"):
            continue
        key, _, raw = line.partition(":")
        val = raw.strip().strip('"')
        key = key.strip()
        if key in {"id", "version"}:
            data[key] = int(val) if val.isdigit() else val
        elif key == "supersedes":
            data[key] = [int(n) for n in re.findall(r"\d+", val)]
        elif key == "superseded_by":
            data[key] = None if val in {"null", ""} else int(val)
        else:
            data[key] = val
    return data


def load() -> list[dict]:
    if not DECISIONS.is_dir():
        return []
    return [parse(p) for p in sorted(DECISIONS.glob("[0-9]*.md"))]


def check(adrs: list[dict]) -> list[str]:
    """One string per rule breach. Empty list means the set is sound."""
    out: list[str] = []
    seen_ids: dict[int, str] = {}
    known_areas = {a for a, _ in AREAS}
    for a in adrs:
        out.extend(a.get("_breaches", []))
        name = a["_path"].name
        for field in ("id", "slug", "title", "status", "version", "revised", "area"):
            if field not in a:
                out.append(f"{name}: missing `{field}`")
        if a.get("status") not in STATUSES:
            out.append(f"{name}: status {a.get('status')!r} not one of {sorted(STATUSES)}")
        if a.get("area") not in known_areas:
            out.append(f"{name}: area {a.get('area')!r} is not a known area — add it to AREAS deliberately")
        i = a.get("id")
        if isinstance(i, int):
            if i in seen_ids:
                out.append(f"{name}: id {i} already used by {seen_ids[i]}")
            seen_ids[i] = name
            if not name.startswith(f"{i:04d}-"):
                out.append(f"{name}: filename does not start with its zero-padded id {i:04d}")
            # the H1 must restate id and title, so a grep of the top of the file is truthful
            body = a.get("_body", "")
            h1 = next((l for l in body.split("\n") if l.startswith("# ")), "")
            if f"{i:04d}" not in h1 and f"ADR {i}" not in h1:
                out.append(f"{name}: H1 does not restate the id")
        if a.get("status") == "superseded" and not a.get("superseded_by"):
            out.append(f"{name}: superseded with no `superseded_by`")
        if a.get("superseded_by") and a.get("status") != "superseded":
            out.append(f"{name}: has `superseded_by` but status is {a.get('status')!r}")
    ids = set(seen_ids)
    for a in adrs:
        for ref in a.get("supersedes", []) or []:
            if ref not in ids:
                out.append(f"{a['_path'].name}: supersedes {ref}, which does not exist")
        sb = a.get("superseded_by")
        if sb and sb not in ids:
            out.append(f"{a['_path'].name}: superseded_by {sb}, which does not exist")
    if ids and sorted(ids) != list(range(1, max(ids) + 1)):
        missing = sorted(set(range(1, max(ids) + 1)) - ids)
        out.append(f"id sequence has holes: {missing}")
    return out


def render(adrs: list[dict]) -> str:
    live = [a for a in adrs if a.get("status") != "superseded"]
    counts = Counter(a.get("status") for a in adrs)
    by_area: dict[str, list[dict]] = defaultdict(list)
    for a in live:
        by_area[a.get("area", "?")].append(a)

    L = ["# ADR catalogue — SRND group strategy", ""]
    L.append("<!-- GENERATED by scripts/adr_catalogue.py — do not hand-edit.")
    L.append("     Run `python scripts/adr_catalogue.py --write`. -->")
    L.append("")
    L.append("A number is permanent and its content is versioned (ADR 0001), so a citation of `ADR 0007` "
             "resolves for the life of the repo.")
    L.append("")
    L.append("| | ADRs |")
    L.append("|---|---:|")
    for s in ("proposed", "accepted", "superseded", "rejected"):
        if counts.get(s):
            L.append(f"| {s.capitalize()} | {counts[s]} |")
    L.append("")
    if counts.get("proposed"):
        n = counts['proposed']
        L.append(f"> **{n} ADR{'' if n == 1 else 's'} {'is' if n == 1 else 'are'} `proposed` and bind{'s' if n == 1 else ''} nothing.** Only Neil moves an ADR to "
                 "`accepted` (ADR 0001 decision 3). A proposed ADR may not be cited as settled.")
        L.append("")
    for area, heading in AREAS:
        rows = sorted(by_area.get(area, []), key=lambda a: a.get("id", 0))
        if not rows:
            continue
        L.append(f"## {heading}")
        L.append("")
        L.append("| ADR | Decision | Status | Ver | Revised |")
        L.append("|---|---|---|---:|---|")
        for a in rows:
            i = a.get("id", 0)
            L.append(f"| {i:04d} | [{a.get('title','')}]({a['_path'].name}) | {a.get('status','')} "
                     f"| {a.get('version','')} | {a.get('revised','')} |")
        L.append("")
    sup = sorted((a for a in adrs if a.get("status") == "superseded"), key=lambda a: a.get("id", 0))
    if sup:
        L.append("## Superseded")
        L.append("")
        L.append("| ADR | Decision | Superseded by |")
        L.append("|---|---|---|")
        for a in sup:
            L.append(f"| {a.get('id',0):04d} | [{a.get('title','')}]({a['_path'].name}) "
                     f"| {a.get('superseded_by')} |")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true", help="regenerate decisions/CATALOGUE.md")
    args = ap.parse_args()

    adrs = load()
    if not adrs:
        print("no ADRs found in decisions/")
        return 0
    breaches = check(adrs)
    if args.write:
        DECISIONS.mkdir(exist_ok=True)
        CATALOGUE.write_text(render(adrs), encoding="utf-8")
        print(f"wrote {CATALOGUE.relative_to(ROOT)} — {len(adrs)} ADRs")
    else:
        counts = Counter(a.get("status") for a in adrs)
        print(f"{len(adrs)} ADRs: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
    for b in breaches:
        print(f"  BREACH: {b}", file=sys.stderr)
    return 1 if breaches else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Cut the C-ATS segments from the consolidated ledger.

Reads data/derived/all-transactions.csv; writes data/derived/cats-segments.csv
(one row per external account) and prints the counts the brand's segments.md
quotes. Numbers only — what they mean lives in brands/c-ats/segments.md.

Account identity: contact_canonical collapses only the Apex USA/LLC pair
(data/README.md), so a further legal-suffix normalisation is applied here.
Without it the same dealer appears two or three times and lands in opposite
segments -- Meridian Audio Ltd bought C-ATS, "Meridian Audio Limited" did not.
The chosen display name is the longest variant seen.

    python data/cats_segments.py
"""

import csv
import re
from collections import defaultdict

LEDGER = "data/derived/all-transactions.csv"
OUT = "data/derived/cats-segments.csv"
CATEGORY = "Acoustic treatment"

# Legal-form words dropped when testing whether two account names are one dealer.
SUFFIXES = r"\b(ltd|limited|inc|llc|bv|b\.v|gmbh|ag|sl|sagl|pty|dmcc|eirl|nv|co|corp|t/a|ta)\b"


def account_key(name):
    s = re.sub(SUFFIXES, "", name.lower())
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


def panel(row):
    """Which of the 3 Rs a line names, where the source says."""
    blob = (row["product_line"] + " " + (row.get("item_description") or row.get("description") or "")).lower()
    for word, name in (("reflection", "Reflection"), ("ref-cp", "Reflection"),
                       ("reverberation", "Reverberation"), ("rev-cp", "Reverberation"),
                       ("resonance", "Resonance"), ("res-cp", "Resonance")):
        if word in blob:
            return name
    if "pack" in blob:
        return "Packs (legacy)"
    if "complete" in blob:
        return "Complete (legacy)"
    return "unattributed"


def segment(last_cats, last_any):
    """Recency against the ledger's own last year, not against today."""
    if not last_cats:
        return "never bought C-ATS — active" if last_any >= 2024 else "never bought C-ATS — inactive"
    if last_cats >= 2025:
        return "C-ATS active"
    if last_cats == 2024:
        return "C-ATS recent"
    if last_cats >= 2020:
        return "C-ATS lapsed"
    return "C-ATS dormant"


def main():
    rows = [r for r in csv.DictReader(open(LEDGER, encoding="utf-8"))
            if r["is_product_revenue"] == "1" and r["is_intra_group"] == "0"]

    acc = defaultdict(lambda: {"names": set(), "cats": 0.0, "other": 0.0, "cats_rows": 0,
                               "last_cats": 0, "first_cats": 9999, "last_any": 0,
                               "cats_years": set(), "categories": set(), "panels": defaultdict(float)})
    for r in rows:
        a = acc[account_key(r["contact_canonical"] or r["contact_raw"])]
        a["names"].add(r["contact_canonical"] or r["contact_raw"])
        year, net = int(r["year"]), float(r["net"])
        a["last_any"] = max(a["last_any"], year)
        if r["category"] == CATEGORY:
            a["cats"] += net
            a["cats_rows"] += 1
            a["cats_years"].add(year)
            a["last_cats"] = max(a["last_cats"], year)
            a["first_cats"] = min(a["first_cats"], year)
            a["panels"][panel(r)] += net
        else:
            a["other"] += net
            a["categories"].add(r["category"])

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["account", "name_variants", "segment", "cats_net", "cats_rows", "cats_years",
                    "first_cats_year", "last_cats_year", "other_net", "other_categories",
                    "last_any_year", "top_panel"])
        for a in sorted(acc.values(), key=lambda a: -a["cats"]):
            w.writerow([max(a["names"], key=len), len(a["names"]),
                        segment(a["last_cats"], a["last_any"]),
                        round(a["cats"], 2), a["cats_rows"], len(a["cats_years"]),
                        a["first_cats"] or "", a["last_cats"] or "", round(a["other"], 2),
                        len(a["categories"]), a["last_any"],
                        max(a["panels"], key=a["panels"].get) if a["panels"] else ""])

    buyers = [a for a in acc.values() if a["last_cats"]]
    active_never = [a for a in acc.values() if not a["last_cats"] and a["last_any"] >= 2024]
    print(f"external accounts (suffix-normalised): {len(acc)}")
    print(f"  ever bought C-ATS: {len(buyers)} ({len(buyers)/len(acc):.1%}), "
          f"GBP {sum(a['cats'] for a in buyers):,.0f}")
    print(f"  of those, bought in more than one year: {sum(1 for a in buyers if len(a['cats_years']) > 1)}")
    print(f"  of those, also bought another category: {sum(1 for a in buyers if a['other'])}")
    print(f"  active 2024-26 and never bought C-ATS: {len(active_never)}, "
          f"GBP {sum(a['other'] for a in active_never):,.0f} spent elsewhere")
    print()
    for seg in ["C-ATS active", "C-ATS recent", "C-ATS lapsed", "C-ATS dormant"]:
        s = [a for a in acc.values() if segment(a["last_cats"], a["last_any"]) == seg]
        print(f"  {seg:16s} {len(s):4d} accounts  GBP {sum(a['cats'] for a in s):>10,.0f}")
    print()
    panels = defaultdict(float)
    for a in acc.values():
        for p, v in a["panels"].items():
            panels[p] += v
    for p, v in sorted(panels.items(), key=lambda x: -x[1]):
        print(f"  {p:20s} GBP {v:>10,.0f}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()

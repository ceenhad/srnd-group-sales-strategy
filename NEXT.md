# What happens next — rev 2

*Rev 2, set 2026-08-17. Replaces rev 1 (2026-08-04) wholesale; git history holds the old text. Rewritten on
Neil's instruction because too much had moved for a patch: engagement is priority one, the six functional
areas replaced the old structure, SRND OS is the source of record, the roles are filled, and the LWCP,
services and sensing positions all changed. Rev 1's completed work lives in `evidence/` and the registers,
not here. Amend this file; do not re-argue it.*

## The constraint

Two founders, a business that has to keep running, no marketing department. Everything below rides on work
already happening, or is named as the exception. The size of the business this plan is for: £19.4m external
revenue over fifteen years, £1.44m in 2025, 2026 annualising near £1.7m — rebuilding on a narrower base,
with own-brand share roughly tripled since the distribution era (`evidence/archive-findings.md` finding 14).

## Priority one: engagement

*"Engagement is terrible. Increasing and maintaining engagement is priority one. We can only sell to
engaged partners."* (Neil, `registers/questions.md` G1.) Engaged means they contact us — inbound only (G2).
Breadth is the symptom; engagement is the cause.

**The two drumbeats** (Neil, 2026-08-17, Q48):

- **Marketing: every brand communicates something through our channels at least once a day.**
- **Sales: real conversations with people, as often as possible.**

Neither is measurable today. Inbound lands in mailboxes, calls and heads; sends are at zero; the best
campaign ever sent was the last one sent, four months ago.

## The order of work

1. **Fix the fault: `MON-13`.** Forty approved dealers hold no engine account and cannot see a price.
   Today's work, not a project.
2. **Build the engagement machinery.** The inbound log in engine (one field on a screen already in use —
   it also feeds the recurring-question list and the spec-conversation capture). Segment the mail list by
   brand and restart the cadence (`MON-15`/`MON-16`/`MON-17` — reach exists, targeting does not). The
   one-tap deal-status email (`operations/engine-as-hub.md` §1 Q4 — the first use of engine-owned mail).
3. **State the group direction (`GRP-1`).** The data is loaded and queryable; what is needed is a reading
   Neil recognises, built from the measured findings only. Precedes all brand work.
4. **Run the per-brand question sweep (`GRP-2`).** One question series, swept through every brand in turn —
   the sibling of `registers/questions.md`. No bespoke brand sessions.
5. **Keep filling the record — it is the content feed.** In this repo's files; **this repo never works
   directly into engine** (Neil, Q47) — engine-side implementation is the platform's job. C-ATS is the
   worked standard; Fabric Walls is the second pass candidate; DT goes by mechanism, twelve scopes drafted.
   With the roles held by Neil and Simon alone, the record, the block library and the production line are
   load-bearing — they are what carries producer work when there is no producer
   (`registers/open-items.md` § "The roles are filled").
6. **Work the sessions list** — `registers/open-items.md` § "Sessions needed". The service offer (`XS-5`)
   is first: the offer is in Neil's head and the session is extraction; it gates the proposal build, the
   incentive policy and the partner-programme value question. The store architecture session gates `C1` on
   every DT record.

**Running beside, not instead:** the consolidation programme (`operations/engine-as-hub.md` §3 — no
third-party operations software, replacements inheriting the old system's baselines). The finding-30
warning binds: building must not absorb the hours while 189 signed partners receive no brand proposition.

## How to tell it is moving

The KPI framework is agreed and lives in `operations/engine-as-hub.md` §1 — funnel spine, signal matrix,
account types, the six questions. The numbers to say out loud:

- **Communications per brand per day** against the once-a-day standard, and **real conversations per
  period** — the two drumbeats, directly.
- **Inbound contacts per period**, once the log exists. The priority-one metric.
- **Accounts created per period → first-order conversion.** The gate is passed 348 times and converts 104;
  that gap is the sales problem in one line.
- **Active dealers per year.** The asset the strategy accumulates; a rising revenue line on a falling
  dealer count is the failure this catches, and DT 2026 showed exactly that.

## Deliberately not now

- **The training programme** — waits on the manuals, which are its raw material.
- **Non-cinema channels** — LWCP opens them properly (commercial fit-out, hospitality, the specifier
  route); until then lane work stays cinema-shaped. LWCP is settled and Neil's; the physical layer waits
  on fab. **Sensing** is a potential giant market and a session (`registers/open-items.md` sessions list),
  not a guess.
- **The group identity line** — drafted after the beyond-cinema position has evidence.
- **Deploying anything** — still the last step, still deliberate.

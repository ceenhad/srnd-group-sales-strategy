# Direct sales and carried lines

*What can be bought without us, what must go through the channel, and what role `cinema-store.com`
plays. Internal.*

## The problem this solves

A steady stream of enquiries asks for pricing on things we can happily sell but which are not really
channel business — a fabric tool, a few rolls of pixel tape, a sample, an accessory. Each one currently
consumes a quote, a reply and someone's attention, for an order worth very little. Meanwhile there are
lines that are genuinely consumer products — DT's Enthusiast range, Ultrasuede — which we have never
promoted as such, so they sell far below their potential.

Both problems have the same answer: somewhere to send people. `cinema-store.com` exists for that. It is
**live but currently a test**, and mid-clean-up — a large number of carried brands have already been
removed — so its present contents are a snapshot, not a specification.

## The test that sorts everything: does the purchase need a relationship?

The dividing line is not B2C versus B2B, and it is not margin. It is whether the buyer needs us involved
to buy correctly.

**If it can be bought without advice, a quote, a design conversation or commissioning — it is
non-channel.** Publish the price, let them buy it, and stop quoting it.

**If it requires specification, design, commissioning or an ongoing relationship — it is channel.** It
belongs to SRND and the trade route, and it should not appear on the consumer site at all.

Applied, that gives:

| | Non-channel — buy it directly | Channel — through SRND |
|---|---|---|
| **Examples** | fabric tools, short runs of pixel tape and profile, samples, small accessories and consumables, Ultrasuede, DT **Enthusiast** screens | own-brand treatment, fabric interiors and room kits, DT's premium **Dynamic** range and Screen Wall, Pro-Fi systems, Leyard, design and commissioning services |
| **Pricing** | public, RRP | registered-partner-only, fully gated |
| **What the buyer needs** | nothing from us but delivery | specification, design, support, relationship |

Two refinements matter.

**The same product can fall either side, depending on the transaction.** A few metres of LED tape is
non-channel; a project's worth of the same tape, specified as part of a lighting scheme, is channel. The
test applies to the purchase, not the product code.

**This resolves the apparent conflict with the gated-pricing policy.** `07-portal-and-pricing.md` bars
public pricing — and it means *channel* products, where a published price would undercut partners and
commoditise the specification work. Non-channel items are a different economic object: publishing their
price is the whole point, because the alternative is quoting them one at a time forever. The two
policies are consistent once the categories are separated.

## Keep the consumer site genuinely consumer

`cinema-store.com` should not become a second trade property. B2B on a real B2C site serves neither
audience: the consumer meets prices and products that make no sense without a designer, and the trade
sees their pricing in public. So the discipline is simple — anything that needs a relationship comes
off, however tempting it is to list it.

That has one immediate consequence worth stating plainly: **large project equipment does not belong
there.** DCI-scale LED walls, commissioning packages and complete room systems are channel business
whatever site they happen to be listed on today.

## The lines we carry, and why

Carried and adjacent products divide by the job they do, not by the margin they return.

- **Distributed lines with real margin** — Leyard is the clear case: a genuine distribution business,
  and per `17-on-ramp.md` potentially our lowest-trust door, because a dealer can try SRND without
  betting on SRND's own engineering.
- **Necessary adjacencies with little or no margin by nature** — pixel controllers, fabric track,
  tools. These are not profit lines and should not be judged as such. They exist for **completeness**:
  one source for the whole job, so a dealer never has to shop elsewhere, and every trip elsewhere is an
  opportunity for someone else to start a relationship. Their strategic role is retention. The
  discipline that follows: make them easy to find and effortless to reorder, and never spend sales
  effort or campaign budget on them.
- **Genuinely consumer lines** — DT's **Enthusiast** range and Ultrasuede. These have real demand that
  goes unrealised because we have never addressed the consumer directly. Note the strict boundary:
  Enthusiast only, never the premium Dynamic range, which is trade business
  (`brands/display-technologies/positioning.md`).

## Where the properties now stand

Adding to the architecture in `09-brand-portfolio.md`:

- **`srnd.store`** — the trade purchasing destination. Gated pricing, registered partners, the real
  business including Leyard.
- **`cinema-store.com`** — the direct, non-channel destination. Public prices, no relationship required,
  no account needed. Its two jobs: absorb the small ad-hoc purchases that currently arrive as quote
  requests, and finally sell the consumer lines properly.

Keeping those two jobs distinct is what makes both work.

## What still has to be decided

- **Confirm the carried-brand roster.** The clean-up is in progress, and the live listings do not yet
  reflect the intended roster. Settle which third-party relationships are actually live, and reconcile
  `srnd.store`, `cinema-store.com` and `09-brand-portfolio.md` to the same answer — the portfolio doc
  currently states Leyard is the only third-party line.
- **Third-party audio versus Pro-Fi.** Carried cinema speaker and amplifier lines sit in Pro-Fi's
  territory. That is defensible while Pro-Fi's range is largely design-intent and Pantheon is
  pre-release, but it needs to be a decision with an end state rather than a drift, or it will compete
  with Pro-Fi exactly when Pro-Fi needs the channel's attention.
- **How Cinema Store is promoted, if at all.** A consumer property implies a consumer voice and consumer
  channels, which is not work the group does today. It may be right to leave it as a destination we
  point people to rather than a brand we market. That is a real choice, not an oversight.
- **Whether Cinema Store has any on-ramp role.** A low-value public purchase is the lowest-trust first
  contact imaginable, and enthusiasts are where some professionals come from — but a consumer buying a
  tool is not a dealer, so don't overstate it. Worth a look, not a plan.
- **Two brand-truth fixes on the live site:** the C-ATS vendor name currently reads "Complete ATS",
  hard-coding an expansion that is deliberately unresolved (use **C-ATS**); and the acoustic design
  service appears as two price tiers when the settled range has a single design service.

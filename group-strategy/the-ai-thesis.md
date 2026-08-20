# The AI thesis — Neil's own frame for the plan, 2026-08-14

*Lifted out of `../registers/open-items.md` on 2026-08-20, where it had been filed among to-do items. **It is not a
to-do: it is the frame the rest of the plan sits inside**, in the owner's own words, with the measured evidence for
it and the honest reservations against it.*

*"The transformation in our business is being driven from the bottom and the top by leveraging AI. It literally
changes the way that you need to think about how to do things. For example, we use Shopify right now but in the new
world it really gives us nothing compared to a Claude-powered combo of Cloudflare and Supabase. All the old glue apps
that you used to get are going to be dead in 12 months because an MCP makes them irrelevant. We are not a complex
business really and we are ambitious and smart enough to use you to let us own and optimise every single thing that
goes through our company."*

**Recorded as a strategic position, with the evidence for it and the honest reservations against it. It is not
this repo's to accept or reject — but it is now the frame the plan sits inside, so it should be written down rather
than carried in someone's head.**

#### What the measured data supports

- **"We are not a complex business" is true and countable.** £1.44m in 2025, roughly 150 trading dealers, 165 live
  products in 12 families, **10,360 transaction lines across fifteen years and five entities.** Engine already models
  the whole operation. **This is a business that genuinely fits inside one system** — the claim is not bravado.
- **The margin ladder applies to software exactly as it applies to product** (finding 23). Each step of the chain you
  hold is a margin you keep. **Shopify, Mailchimp and Monday each hold a step**, and today measured what one of them
  costs: **Shopify's integration posts every store order to a single nominal account, so £1,385,960 — over half of
  SRND Group's revenue — arrived with no product category**, and had to be reconstructed from item descriptions by
  keyword rule (`data/classify_store_items.py`). **That is a third party's design decision costing the group its own
  sales analysis.** Neil's own argument, one rung up.
- **The glue-app claim was demonstrated rather than asserted this week.** The failure that stops the 189 being sold
  to is Monday's per-brand flags never reaching Mailchimp — **precisely the job Zapier-class tooling exists to do,
  and precisely what it did not do.** Meanwhile the whole Mailchimp pull is one ~120-line file
  (`data/fetch_mailchimp.py`) written in minutes, and the engine audit was an MCP connection and a series of
  questions. **The economics of integration have already changed for a business this size.**
- **And this session is the proof of concept.** Six sources loaded and reconciled, a 200-table platform audited, one
  consolidated table, thirty findings and a plan amended throughout — **in two days, by the method being proposed.**

#### Where the reservations sit, stated plainly

- **Shopify is not only a storefront, and the replaceable parts are not the risky parts.** Catalogue, pricing tiers
  and product data **already live in engine** — that half is genuinely low-risk to take back. **Payments, PCI scope,
  multi-territory tax, fraud, and B2B company accounts are the hard half**, and the group uses the last of those:
  `customer_shopify_company_refs` holds **338 mappings**. The honest framing is **storefront cheap, checkout
  expensive** — and the sequencing should follow that, not the enthusiasm.
- **"Dead in 12 months" is right about capability and optimistic about everyone else.** It does not need to be true
  of the market to be true here: **what matters is whether *this* group can do it, and it can, because it is small
  and already owns its data.** Worth holding the claim in the narrow form, since the wide form invites an argument
  nobody needs to win.
- **The real risk is not technical, and this week named it.** Finding 30: **the group's measured failure mode is
  building things and never saying them.** A platform programme is a *building* activity — the mode the group is
  already strongest in — and it could absorb every available hour while **189 signed partners still receive no brand
  proposition and 40 still cannot see a price.** *The architecture is right; it must not become the ninth entry in
  finding 30's table.*
- **And the selling half still needs an owner.** Engine is thorough where it was authored — operations — and empty
  where it was not (`evidence/engine-audit.md` §0). **Making engine the hub for marketing and selling does not by itself
  create the selling content**; group 04 of the record remains homeless whichever system holds it.

#### The one thing that follows for sequencing

**Consolidation and the audience work are not competitors, and the plan should say so explicitly.** One is building,
the other is selling; they draw on different hours and different people. **The test this page already applies settles
it** — *does this ride on something already happening?* **Mailing the 189 does. Rebuilding checkout does not.** So the
audience work starts now at whatever rate it can, and the platform programme runs behind it on its own timetable,
**with `MON-13` treated as neither — a fault to fix today, because forty partners cannot buy.**


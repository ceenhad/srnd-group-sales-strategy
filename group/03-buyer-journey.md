# The buyer journey

**Defined at group level; run end to end.** This is the whole arc of a trade relationship — from a
dealer who has never heard of us to one who orders across the group, repeatedly. It was first worked
out for a single brand (C-ATS); read here it's the group case, because that's how it actually runs:
**a dealer relationship is won through a brand but held by the group, and a real project spans
brands.** A home cinema needs a screen (Display Technologies), acoustics (CATS), fabric walls
(Fabric Walls), lighting (Light Walls) and audio (Pro-Fi) — one room, one dealer, one client. So the
journey is not one brand selling one product; it's the group earning and compounding a relationship
through whichever brand opens the door.

Each brand runs its own version — same stages, same handoffs — over a largely shared dealer base.
What changes per brand is the *content* at each stage (`brands/<brand>/content.md`). The web
properties do specific jobs along the way: `srnd.group` opens the funnel (stages 1–2), brand sites
do the functional/proof work (stages 2–3), and the store takes the order (stage 4). See the web
architecture in `09-brand-portfolio.md`.

## The end-to-end case (one arc)

A dealer meets the group at the top of the funnel — a search, a referral, a trade event, or another
SRND brand they already buy — and lands on **srnd.group**, which introduces the company and points
them at the brand that fits the need in front of them. On that **brand site** they get the
functional case: does this solve my problem, can I spec and install it, will it hold up in front of
my client. Convinced, they register as a trade partner (handled by engine) and buy through
**srnd.store** — one account that already covers every other brand. The first job goes in; we make
it succeed, and it becomes a reference. Then the relationship compounds: the same room needs the
next system, the next project needs a different brand, and reordering is one action on an account
that spans the group. A satisfied dealer refers a peer, and the arc begins again — now with the
group, not just the brand that opened the door.

The rest of this document is that arc as six stages, with the mechanics each one needs.

## The stages

1. **Unaware → get in front of them.** The relationship can start at any brand, or at the group
   itself. Warmest of all is a dealer who *already buys another SRND brand* — the group's own base
   is a standing entry point. The top of funnel is deliberately **wide**: many entry points, and
   many valid places to land a given piece across the group's properties. Use that flexibility to
   route entry and **spread contact load** rather than funnelling everyone through one door — it's
   one of the two oversaturation levers in `02-commercial-model.md`.
   *Touchpoints: trade press, trade events, social, inbound search/AI, peer referral, existing
   dealers of other brands. Destination: `srnd.group` opens the funnel and routes onward. Content:
   the hook — the core problem the relevant brand solves, stated boldly.*
2. **Name lands, means nothing → land the proposition.** One system, a real problem they have, made
   easy. They're now on a **brand site**, which stays functional and focused — but they're meeting a
   brand backed by a group that covers the whole room, which is itself part of the proposition.
   *Touchpoints: brand site, social, email, a short video. Content: the range/possibility layer.*
3. **"Could this work for me?" → prove it.** It works, it's easy to spec and install, it won't
   embarrass them in front of their client. This is the brand site's real job, backed by the shared
   proof assets.
   *Touchpoints: KB how-to content, virtual demo/webinar, sample kit, the Experience Centre
   (`06-content-production.md`), a Zoom, the measured data. Content: the how-it-works layer.*
4. **Wants to buy → register, then buy.** Pricing is registered-partner-only by design
   (`07-portal-and-pricing.md`), so **partner registration *is* the stage-4 gate** — it turns an
   interested dealer into one who can see pricing and transact. Registration and gating are run by
   engine; the purchase happens at **srnd.store**. Crucially, this is **one account across every
   brand** — register once, buy the whole room.
   *Touchpoints: the store (`srnd.store`), engine-run registration and partner pricing, spec help,
   the design service.*
5. **First order, job on site → make the first job succeed.** Install support, verification, make
   the dealer look good. Because the project is often multi-brand, "the job" may already span more
   than one brand — support what they actually bought, across brands. → a satisfied dealer *and* a
   public-safe reference asset.
   *Touchpoints: install content, verification services, Zoom support.*
6. **The next order — the hardest stage, and the group's payoff.** Process, not hope:
   - **reorder ease** — saved details, one action to restock, on the group-wide account;
   - **new reasons** — a new element, or a new range when it ships (never before it ships);
   - **cross-brand expansion** — the same room needs the next system, and the dealer's next project
     may need a *different brand entirely*. This is where "one relationship, six brands" pays off and
     the group compounds beyond any single brand (`01-dealer-as-asset.md`);
   - **persistent presence and low friction** — we can't manufacture the dealer's next project; it
     lands on *their client's* clock, not ours. So the approach isn't a push, it's being recalled
     the moment it lands and being effortless to act on. A satisfied dealer then refers a peer →
     back to stage 1.

## Why this is a group document, not a brand one

- **The cross-brand steps at 5–6 are group-owned.** A single brand's version of the journey can't
  own the step that hands to *another* brand — that coordination is why the buyer journey is defined
  at group level.
- **The compounding is only visible at group level.** "One account across brands" (store + engine)
  is what makes reorder and cross-brand expansion frictionless; a brand looking at its own orders
  can't see, or engineer, the whole relationship.

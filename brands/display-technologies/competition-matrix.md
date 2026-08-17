# Display Technologies — Commander competition matrix

Why DT's control outclasses competitor control, dimension by dimension. The DT column is real,
drawn from `ceenhad/dt-platform`; the competitor column is a framework to fill with **verified**
research on named competitors (see open items) — not guessed specifics.

## The magnitude

"~400×" is deliberate hyperbole — shorthand for *the Commander is in a different league from
competitor control*, not a metric to compute or a figure to publish. This matrix exists to make that
felt through concrete capability differences a professional recognises. Lead with the differences,
not the number.

## The competitors (named)

Who DT is measured against, grouped by where they overlap. Capabilities to be filled from verified
research — don't guess specs.

- **Screens & masking** (vs DT screens and the Dynamic Screen):
  - **Stewart Filmscreen** — premium projection screens and masking.
  - **Screen Research** — premium screens (incl. acoustically transparent) and masking.
  - **Screen Excellence** — acoustically transparent screens and masking.
- **Motion / automation** (vs DT mounts, the MMD and the Actuator Commander):
  - **Future Automation** — motorised mounts, lifts and motion. *Internal view: rated as derivative
    and overpriced — a positioning cue (DT competes on real sophistication and value), not language
    for public copy.*
- **Whole cinema build** (overlaps DT and other SRND brands — Fabric Walls, C-ATS):
  - **Cinema Build Systems** — cinema construction/interiors and integrated systems; competes at the
    room level, so relevant group-wide, not to DT alone.

Several of these are group-level competitors, not DT-only — researched (what each does well) in the
group competitor study `../../group-strategy/competitors.md`. This matrix stays DT/Commander-specific.

## The matrix

DT column = real (from the platform repo). Competitor column = *typical* control among the named
competitors above (Stewart, Screen Research, Screen Excellence, Future Automation, Cinema Build
Systems), **to validate per competitor before use in copy.**

| Dimension | DT Commander V5 | Typical competitor control (verify) | Why it matters to the pro |
|---|---|---|---|
| Architecture | Distributed system — network Bridge + Controller + per-unit Peripherals; closed-loop control local to each motor | Single relay/driver box; open-loop | Precision + reliability without network latency |
| Masking axes | Up to **5 independently-positioned** mask edges (L/R/T/B/Art) coordinated for aspect ratio | 2-way (verified: Future Automation LUMA-SHIFT) up to ~4-way (Screen Research) | True aspect matching, no grey bars, no manual fiddling |
| Motion control | Closed-loop position/speed/current; soft-start/decel; quiet by design | Open-loop, limit-switch | Quiet, exact, ends where it should |
| Network / AV integration | Ethernet+PoE, browser WebUI (no desktop app), mDNS/SDDP discovery, OpenAPI, TCP line protocol, WebSocket; native Crestron/Control4/Savant | RS232 / contact-closure; maybe a basic IP relay | Drops onto the AV network and integrates with far less effort |
| Presets & sequencing | Factory-curated presets bundling parameters **and** safety limits; one-tap aspect recall; coordinated multi-device sequences (JSON→bytecode) | A few stored positions | Complex choreography without bespoke programming |
| Diagnostics | Built-in self-test (structured JSON over USB/RS232/network); real-time move-trace charts; wire-protocol console; activity log | Status LEDs, or nothing | Commission and fault-find without extra tooling |
| Safety | Per-device safety limits in presets; current + thermal-fault monitoring; closed-loop overrun protection | Limit switches, fuses | Motion safety is engineered in, not bolted on |
| Security | Sealed-at-provisioning (PBKDF2), three-tier access, on-device audit log, per-assembly-serial identity | Open serial console, no auth | Safe on a client's network |
| Remote support | Time-boxed **physical Request Support button** — remote help, no standing backdoor | Vendor backdoor, or truck roll | Support without a site visit *or* a permanent security hole |
| Traceability / manufacturing | Per-PCB assembly serials, bench provisioning, persistent fault/cycle history | None | Returned units carry their history; repeatable at volume |
| Platform / roadmap | One platform + shared WebUI across products (Dynamic, Actuator, Video, cooling to come) | Point product | Learn once; integration work carries product to product |

## How to use it

- The pro's decision is *easier and safer to deliver* (`dt-commander-v5.md`); this matrix is the
  evidence for **why DT can deliver that and others can't** — each row is a concrete reason.
- Lead with the rows that matter most to the specific buyer/channel; don't dump the whole grid.
- **On the masking row:** DT's 5th (Art) edge is a capability, not a selling point — art masking is
  a niche, compromise-laden solution in the field (Screen Research offer it too;
  `../../group-strategy/competitors.md`). Lead on coordinated primary-edge masking done well + the control
  behind it, not "we do Art."
- Keep the DT column honest to the repo (and to the status caveats — some V5 boards are designed,
  not yet built).

## Open items

- **Fill the competitor column with verified research** on the named set. First-pass public research
  (what each does well) is captured in `../../group-strategy/competitors.md`; the per-capability cells here
  still need the specific control-vs-control detail, from closer research + Neil's knowledge — no
  guessed specs.

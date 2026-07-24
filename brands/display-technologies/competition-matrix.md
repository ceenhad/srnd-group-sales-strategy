# Display Technologies — Commander competition matrix

Why DT's control outclasses competitor control, dimension by dimension. The DT column is real,
drawn from `ceenhad/dt-platform`; the competitor column is a framework to fill with **verified**
research on named competitors (see open items) — not guessed specifics.

## The magnitude (framing, not a claim)

Neil's assessment: the Commander is **orders of magnitude** more powerful and sophisticated than any
competitor's control — put at roughly **~400×**. Treat that as the internal sense of the gap, not a
published spec. **Express it through this matrix** — concrete, checkable capability differences —
rather than a bare multiple. (Group `CLAUDE.md`: don't publish figures we can't substantiate; a
number a specifier can't verify weakens credibility rather than building it.)

## The matrix

DT column = real (from the platform repo). Competitor column = *typical* control in this segment,
**to validate against named competitors before use in copy.**

| Dimension | DT Commander V5 | Typical competitor control (verify) | Why it matters to the pro |
|---|---|---|---|
| Architecture | Distributed system — network Bridge + Controller + per-unit Peripherals; closed-loop control local to each motor | Single relay/driver box; open-loop | Precision + reliability without network latency |
| Masking axes | Up to **5 independently-positioned** mask edges (L/R/T/B/Art) coordinated for aspect ratio | 2–4-way masking, often fixed endpoints | True aspect matching, no grey bars, no manual fiddling |
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
- Keep the DT column honest to the repo (and to the status caveats — some V5 boards are designed,
  not yet built).

## Open items

- **Fill the competitor column with verified research** on the real named competitors DT is measured
  against (masking-screen and motion-control makers) — no guessed specs.
- **Decide how to express the magnitude** — the matrix (recommended), a chosen headline, or both;
  and whether any single number is defensible enough to publish.

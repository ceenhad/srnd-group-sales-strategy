# Display Technologies — DT Commander V5 platform (new developments)

Captured from the **`ceenhad/dt-platform`** repo (sales/dt-commander-v5-summary.md, 2026-05-26; plus
the system/ and products/ docs), 2026-07-23. Raw input for messaging — and a strong candidate for
what DT leads with. **Status caveats at the end: not all of this is shipping — do not overclaim.**

## What it is

**DT Commander V5** is a shared, network-grade control platform underneath DT's motorised/dynamic
products. Two products run on it today — **Actuator Commander** and **Dynamic Commander** —
re-architected onto one shared chassis, WebUI and integration surface. It's a step-change, not a
refresh. More products are planned on the same platform (projector cooling is stated as next; a
video/TV Commander also exists in the repo).

## Architecture (the enabling change)

- Was: a single-board controller reached over serial, configured via a Windows desktop app
  (MegunoLink). Now: a **two-board architecture — a network Bridge + a control Controller** (plus
  per-mask **Peripherals** on the Dynamic Screen). The Bridge faces the customer network; the
  Controller/Peripherals sit on a private in-product CAN bus and never touch the customer LAN.
- **A real network product:** wired Ethernet + PoE by default (WiFi available); browser **WebUI**
  from any phone/laptop (no desktop software); **TCP integration port 20108** for line-protocol
  clients (Crestron, Control4, Savant); **mDNS** (`_dt-commander._tcp`) auto-discovery; **SDDP**
  responder; **OpenAPI 3.1** REST spec; **WebSocket** live state to multiple clients.

## The standout differentiator: the physical "Request Support" button

The category's usual trade-off is a permanent remote-support backdoor (convenient, but a standing
risk) *or* no remote access (every fix is a truck roll). **V5 resolves it in hardware:**

- Only a **physical button on the device** puts it into support mode — no remote command or login can.
- The session is **time-boxed**; when it expires the device re-seals automatically.
- So: **the customer is in absolute control** of who reaches in and when; distributors keep remote
  support (no truck roll); **DT itself has no path into a deployed unit** without on-site
  authorisation; a leaked admin password is non-fatal (still needs the button).
- The pitch shifts from "we promise we won't…" to **"we can't — and here's why."** For
  privacy-conscious high-end residential and luxury commercial cinema clients — exactly DT's market
  — this is genuinely category-leading, and enforced by hardware behaviour, not policy.

## Security & field-service model

Sealed-at-provisioning (factory generates a random 16-char admin password, PBKDF2-HMAC-SHA256, the
literal "admin" default then stops working); three-tier access (operator / admin / factory);
on-device audit log; per-assembly-serial identity written once at the factory (faulted units are
replaced and re-provisioned, not field-migrated).

## Shared WebUI & DT brand identity

One shared component kit across products — same buttons, cards, vocabulary. **DT brand cues:
Vibrant Blue accent, Titillium Web type, JetBrains Mono for data.** Self-hosted fonts (works on
isolated networks, no CDN call); System/Light/**Dark-by-default** (cinema rooms never flash white);
Operator (phone, homeowner-simple: Home/Install/Closed/Stop) / Admin (dense, config-grade) / Factory
tiers. (Full brand guidelines exist: `dt-platform/branding/`.)

## Diagnostics

Built-in **self-test** (one command/button → structured JSON-line results over USB, RS232 and
network — paste straight into a ticket); **real-time move-trace charts** (position/speed/current vs
time); **wire-protocol console** in the admin WebUI; **activity log** on the operator screen
("Recall Preset 1 · 14:32").

## The two products

- **Actuator Commander V5** — for **opening mechanisms** (hatches, lifts, vents, table-tops). Drives
  third-party Electromen EM-PLI motor controllers (EM-339/337/348) over RS-485 Modbus RTU (no
  DT-built peripheral firmware); factory-curated presets bundle parameters + per-device safety
  limits; multi-device **coordinated opening sequences** (authored as JSON, compiled to bytecode,
  run on the Controller). *Note: this extends DT beyond screens/mounts into motion/opening control.*
- **Dynamic Commander V5** — the **DT Dynamic Screen (DYN-4-AM)** masking system. Up to **five
  independently-positioned mask edges** (Left/Right/Top/Bottom/Art) coordinate to set aspect ratio,
  blacking off outside the picture against absolute black. Solves the real problem: source arrives
  in many/arbitrary aspect ratios; a fixed screen shows grey bars, a manual mask needs constant
  attention — this automates it, **quietly, precisely, reliably** (per-mask closed-loop control kept
  local to the motor). CAN-FD-capable hardware; aspect presets (1.33/1.78/1.85/2.35/2.40/custom),
  one-tap recall. This is the engine behind DT's masking-screen / "Mask Position Logic" story.

## Why it matters commercially

- A **sellable privacy story** no competitor in the segment matches (the support button).
- **One pitch, one integration, one look across products** — and reusable Crestron/Control4 work
  (same TCP port, wire grammar, mDNS type).
- **Lower support burden** (self-explaining WebUI, audit log, self-test, remote-support-without-truck-roll).
- **Manufacturing scaling baked in** (per-PCB serials, bench provisioning, documented re-flash).

## Status — do NOT overclaim (from the repo's own "in flight" note)

- Dynamic Commander V5 **Controller and Peripheral PCBs are designed, not yet manufactured**;
  firmware is built and **bench-validated**, boards to follow on schedule.
- Some deeper admin/factory flows are functionally complete on the bench, pending final visual polish.
- Full on-hardware soak testing runs after bench bring-up with real motors — **currently mid-Stage 0**.

So: treat V5 as an **in-development platform with a validated firmware/architecture story**, not a
shipping product line. Marketing must not present unbuilt boards as available (group `CLAUDE.md`:
don't write up in-development products as shipping).

## Messaging note (to agree)

The **Request Support button / "we can't reach in" privacy guarantee** is the strongest single
differentiator surfaced for any brand so far and squarely fits DT's high-end/luxury-cinema buyer.
Strong candidate to lead DT's story — pending the status caveats above and sign-off on what's
claimable now vs on-ship.

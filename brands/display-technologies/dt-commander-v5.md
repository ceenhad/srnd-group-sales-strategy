# Display Technologies — the Commanders (DT Commander V5)

Captured from **`ceenhad/dt-platform`** (system/, products/, sales/dt-commander-v5-summary.md,
2026-05-26), 2026-07-23. Raw input for DT's messaging.

## The point: the Commanders are what control DT's products

DT's differentiated products aren't just screens and mounts — they're **motion and masking systems**,
and each one is only as good as the control that drives it. **The Commanders are that control.**
This control layer — coordinated multi-edge masking, closed-loop motion, factory-tuned safety and
sequencing — is **what DT can do that others can't**. Competitors sell the hardware; DT builds the
brains as well.

| Product | Controlled by | What it is |
|---|---|---|
| **DT Dynamic Screen** (DYN-4-AM) | **Dynamic Commander** (`dt.screen.dynamic_commander`) | Aspect-ratio masking — up to 5 independently-positioned mask edges (L/R/T/B/Art) reshape the picture, quietly and precisely |
| MMD (motorised mirror drop) & general motion | **Actuator Commander** (`dt.motion.actuator_commander`) | Lifts, drops and opening mechanisms (hatches, vents, table-tops) driven via Electromen EM-PLI Modbus controllers, with coordinated sequences |
| AV device control (investigation) | **Video Commander** (`dt.av.video_commander`) | Inline HDMI/EDID appliance translating IP → USB-HID/CEC/RS232/IR *(firmware not yet scaffolded)* |
| Projector cooling (future) | hushbox-commander | Cinema projector cooling — likely next on the platform |

("Commander" = the complete assembled system — Bridge + Controller + Peripherals — running one
coordinated function.) **V5 is the new, fully-updated version of this control.**

## Why V5 matters: easier and safer for the professional

Our customer is the professional installer/integrator. Everything V5 changed reduces their **effort**
and their **risk** in delivering advanced motion/masking systems.

**Easier for the pro:**
- **On the AV network in minutes.** Was: a single-board device reached over serial, configured with
  a Windows desktop app (MegunoLink). Now: drop a Cat5 (PoE), and it's on the network — **browser
  WebUI from any phone or laptop, no desktop software.**
- **It just appears and integrates.** mDNS/SDDP auto-discovery, native Crestron/Control4/Savant, a
  published OpenAPI spec and a TCP line-protocol port — far less integration work, and work done for
  one Commander largely carries to the next (shared platform, shared WebUI).
- **Presets do the hard parts.** Factory-curated product presets bundle the right parameters *and*
  the safety limits in one apply; aspect-ratio presets recall in one tap; multi-device choreography
  is authored simply and run coordinated.
- **Commissioning and support are self-serve.** One-command **self-test** emits structured results to
  paste into a ticket; **move-trace charts** (position/speed/current) and a wire-protocol console
  make calibration and fault-finding need no extra tooling; the activity log shows what just
  happened. When a callout is needed, the **Request Support button** lets a distributor help
  remotely — no truck roll.

**Safer for the pro and the client:**
- **Motion safety is built in** — per-device safety limits travel inside the presets; closed-loop
  control lives *local to each motor* (precise, quiet, ends at the right position, won't overrun);
  thermal-fault thresholds tuned to the climate-controlled cinema environment.
- **The device is secure by default** — sealed-at-provisioning (random admin password,
  PBKDF2-hashed; the "admin" default stops working after commissioning), three-tier access
  (operator / admin / factory), an on-device audit log, and per-assembly-serial identity.
- **Safe on the client's network** — the **physical, time-boxed Request Support button** means no
  standing remote backdoor: nobody (not even DT) can reach a deployed unit without someone pressing
  the button on site. For a professional carrying liability for the networks they build, that removes
  a real risk — a supporting proof point, not the headline.

## Status — do NOT overclaim (from the repo's own "in flight" note)

- Dynamic Commander V5 **Controller and Peripheral PCBs are designed, not yet manufactured**;
  firmware is built and **bench-validated**, boards to follow on schedule.
- Some deeper admin/factory flows are complete on the bench, pending final visual polish.
- Full on-hardware soak testing runs after bench bring-up with real motors — **currently mid-Stage 0**.
- Video Commander is at investigation stage (firmware not scaffolded); hushbox/cooling is a future
  product. Treat V5 as an in-development control platform with a validated firmware story — don't
  present unbuilt boards as shipping (group `CLAUDE.md`).

## Messaging note (to agree)

DT's story here, for the professional customer: **DT builds the control that powers advanced
motion and masking — not just the hardware — and V5 makes delivering it dramatically easier and
safer to install, commission and support.** That's the differentiation ("what we can do that others
can't"), and it speaks directly to the pro. The privacy/Request-Support feature supports the "safer"
half; it doesn't lead. Exact lead and claimable-now scope to confirm against the status caveats.

**The scale of the gap.** The Commander is in a different league from competitor control — "~400×"
is the hyperbole for it. Make it felt through the concrete capability differences in
`competition-matrix.md` (vs Stewart, Screen Research, Screen Excellence, Future Automation, Cinema
Build Systems), not a headline number.

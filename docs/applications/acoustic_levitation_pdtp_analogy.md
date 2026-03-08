# Acoustic Standing Wave Levitation — PDTP Analogy

**Status:** SPECULATION — visual concept only. No Sudoku check, no formal Part number yet.
This document maps the known physics of acoustic levitation to the PDTP decoupling goal.
The math will be done properly in a future Part once the framework is ready.

---

## How Acoustic Levitation Works (Known Physics)

In acoustic levitation, a transducer generates a sound wave that bounces off a reflector
above it. The two waves (upward + reflected downward) interfere to create a **standing wave**:
fixed nodes (zero pressure) and antinodes (maximum pressure oscillation).

A small object placed near a pressure node experiences:
- Upward acoustic radiation pressure from below
- Downward acoustic radiation pressure from above
- Net force: zero at the node → object is trapped

![How acoustic levitation works — transducer, reflector, node/antinode diagram](../../assets/images/acoustic%20standing%20waves%20levitation%20H19fQ==.jpg)

The object does **not** need to touch anything. It floats in mid-air, held purely by
the wave pattern. No propellant. No contact force. No exhaust.

![Real acoustic levitation — multiple objects trapped at nodes along the standing wave column](../../assets/images/acoustic%20standing%20waves%20levitation%20472926_1_En_2_Fig1_HTML.png)

Key parameters:
- Wave frequency: typically 20–100 kHz (ultrasound)
- Wavelength: a few mm (sets node spacing)
- Object size: must be smaller than half-wavelength
- Power: a few watts for gram-scale objects

**Source:** Andrade et al. (2018), "Acoustic levitation of small disks" — standard acoustic physics

---

## The PDTP Inversion

Standard acoustic levitation has one critical feature: **the object is passive**.
The transducer generates the standing wave. The object just sits there and gets trapped.

PDTP Goal 2 flips this completely:

| | Standard Acoustic Levitation | PDTP Decoupling (Goal 2) |
|---|---|---|
| Wave source | External transducer | The craft/object itself |
| Medium | Air (pressure waves) | Spacetime condensate (phase waves in φ) |
| What is trapped | Small object at node | Craft at node in gravitational condensate |
| Coupling | Acoustic radiation pressure | Phase-locking α = cos(ψ − φ) |
| At node | Acoustic force = 0 | Gravitational coupling α = 0 (decoupled) |
| What escapes | Nothing — object trapped | Gravity — craft is free of spacetime |

**The key insight:** If the craft can generate a standing wave pattern in the
gravitational condensate field φ, it creates its own node — a region where
ψ − φ = π/2 and the phase-locking coupling α = cos(π/2) = 0.

At that node, the craft is **gravitationally decoupled** from the surrounding spacetime.
Not shielded (shielding would require blocking the field from outside).
Not repelled (repulsion would require α = −1).
Simply: **unlocked** — the phase difference is 90°, the coupling vanishes.

---

## The Phase Sequence Analogy

Three-phase electrical current (120° spacing) is the simplest way to create a
rotating phase gradient in space. Each phase pushes the field pattern around in a
smooth, continuous rotation — no dead spots.

![Three-phase sequence (3-2-1 rotating field)](../../assets/images/phase%20sequesnce%2002182.png)

The PDTP analog: a ring of coils, each driven at a different phase offset, creates
a **traveling phase wave** that propagates through and around the ring. This is the
mechanism that would drive oscillation in the φ field.

![Phase gradient coil array — toroidal ring, independently phase-controlled](../../assets/images/phase_gradient_coil_schematic.png)

The three-amplifier 120° geometry matches the claimed configuration of the Lazar craft.
The toroidal coil array is the transducer. The craft body is the "object at the node."

![PDTP analog simulation concepts — EM levitation, eddy current inertia reduction, contained field](../../assets/images/pdtp_analog_simulation.png)

---

## Why the Saucer Shape

In acoustic levitation, the node geometry is determined by the wave source shape:
- A flat transducer creates flat horizontal node planes → objects levitate in horizontal bands
- A curved transducer creates a focal node → one strong trapping point

For a toroidal (ring-shaped) wave source:
- The field is strongest inside and above/below the ring equator
- The natural node plane is **flat and horizontal** — the equatorial plane of the torus
- A disk-shaped craft centered on this plane maximizes the area sitting at the node

This is why the saucer shape is optimal — not aerodynamics, not aesthetics.
It is the shape that best fits the standing wave geometry of a toroidal condensate oscillator.

---

## What PDTP Needs to Compute (Future Part)

The acoustic analogy is clear visually. To make it rigorous, PDTP needs to answer:

**1. Wave equation for φ with an oscillating matter source:**

Standard PDTP field equation:
```
□φ = Σᵢ gᵢ sin(ψᵢ − φ)
```

If matter oscillates (ψᵢ driven at frequency ω), the right-hand side becomes a
time-varying source. This generates outgoing φ waves — the "transducer" effect.
A reflective boundary (the craft structure?) would create standing waves.

**2. Coupling constant EM → φ:**

The coil array drives EM fields, not φ directly. The coupling between EM phase
and gravitational condensate phase is unknown. The Tajmar (2006) result suggests
it exists at the ~10⁻⁷ level. What PDTP predicts is unknown — this is the key
missing number.

**3. Resonance frequency:**

The condensate has a characteristic oscillation frequency ω_gap = m_cond c²/ħ.
This is the frequency the "transducer" needs to operate near to efficiently drive
the φ field. m_cond is currently unknown (the central open problem, Part 29).

**4. Node stability:**

In acoustic levitation, nodes are stable equilibria (restoring force pushes object
back if displaced). Is the gravitational condensate node also stable? Or does the
condensate restore the phase lock too quickly? The restoring force scale is g (the
coupling constant from the Lagrangian) — the same ~10 kW/ton decoupling energy
estimated in Part 29.

**5. Partial decoupling:**

Full decoupling (α = 0) requires ψ − φ = π/2 everywhere in the craft.
Partial decoupling (α reduced, not zero) reduces effective gravitational mass.
Even 10% decoupling would be measurable. Even 1% would be a publishable anomaly.

---

## Experimental Ladder (No Exotic Materials)

Three levels, each buildable with current technology:

### Level 1 — Classical analog (today, ~£200)
Build the acoustic levitation rig with ultrasound transducers.
Observe objects trapped at nodes. Understand the wave geometry experimentally.
This is purely acoustic — no PDTP connection yet, but builds physical intuition.

### Level 2 — EM phase array with superconductor (~£500, liquid nitrogen)
Build the toroidal coil array (copper wire, STM32 controller, fiberglass former).
Place a YBCO superconducting ring inside (liquid nitrogen cooling, 77K).
Sweep phase rotation frequency. Measure weight of assembly on precision scale.
This tests the Tajmar coupling — whether a rotating EM phase pattern produces
any anomalous gravitational effect through the superconductor.

### Level 3 — Full PDTP experiment (requires knowing m_cond)
Once m_cond is measured (via breathing mode detection, Strategy A),
calculate the required φ oscillation frequency.
Build a resonant structure at that frequency.
Measure gravitational coupling change (α shift) in the assembly.

Level 3 is the real experiment. Levels 1 and 2 are preparation and calibration.

---

## Summary

Acoustic standing wave levitation demonstrates that **wave interference can suspend
matter with no contact and no propellant** — purely through standing wave geometry.

The PDTP extension of this idea is:
- Replace acoustic pressure waves with phase waves in the spacetime condensate φ
- Replace the external transducer with the craft's own oscillating reactor/coil array
- Replace acoustic node (zero pressure) with condensate node (zero phase coupling, α = 0)
- Result: a craft that is gravitationally decoupled at its own standing wave node

The physics is analogous. The math is not yet done. The experiment is buildable in stages.
This document records the concept for when PDTP is ready to compute the numbers.

---

## References

- Andrade et al. (2018) — acoustic levitation review
- Tajmar et al. (2006), Phys.Rev.Lett. — anomalous gravitomagnetic field from spinning superconductor
- PDTP Part 29 — decoupling energy estimate ~10 kW/ton
- PDTP Part 27/28 — breathing mode and condensate oscillation
- PDTP Goal 2 (CLAUDE.md) — phase decoupling engineering goal
- Lazar (1989) — three gravity amplifiers at 120° spacing, saucer geometry
- **Images:** assets/images/acoustic standing waves levitation H19fQ==.jpg (HowStuffWorks diagram)
- **Images:** assets/images/acoustic standing waves levitation 472926_1_En_2_Fig1_HTML.png (real experiment)
- **Images:** assets/images/phase sequesnce 02182.png (three-phase rotating field)
- **Images:** assets/images/phase_gradient_coil_schematic.png (toroidal coil array design)
- **Images:** assets/images/pdtp_analog_simulation.png (EM levitation analog concepts)

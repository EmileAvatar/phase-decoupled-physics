# Vortex Winding Number Derivation — Toward G from First Principles (Part 33)

**Status:** Theoretical derivation — G-free chain established from vortex topology.
One free parameter remains: the condensate quasiparticle mass m_cond.
**PDTP Original:** Vortex core condition n = m_cond/m; unification of Strategy A and B.
**Date:** 2026-03-01
**Prerequisites:**
[mathematical_formalization.md](mathematical_formalization.md) §3 (PDTP field equations),
[hard_problems.md](hard_problems.md) (substitution chain analysis),
[pdtp_findings_summary.md](../overview/pdtp_findings_summary.md) §8 (strategies A and B)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Background — The Circular Wall](#2-background--the-circular-wall)
3. [The Vortex Picture of a Particle](#3-the-vortex-picture-of-a-particle)
4. [The Vortex Field Equation](#4-the-vortex-field-equation)
5. [Superfluid Velocity and the Core Condition](#5-superfluid-velocity-and-the-core-condition)
6. [Deriving the Winding Number n](#6-deriving-the-winding-number-n)
7. [The G-Free Chain](#7-the-g-free-chain)
8. [Sudoku Verification](#8-sudoku-verification)
9. [Unification of Strategy A and Strategy B](#9-unification-of-strategy-a-and-strategy-b)
10. [The Remaining Gap](#10-the-remaining-gap)
11. [What This Achieves and What Remains](#11-what-this-achieves-and-what-remains)
12. [References](#12-references)

---

## 1. Executive Summary

### 1.1 The Task

Every previous phase of the solver showed that deriving Newton's constant G
without circular input requires knowing the PDTP lattice spacing `a`. All
algebraic chains gave `a = l_P = sqrt(ħG/c³)` — which contains G. The TODO
question: can the winding number `n` of a particle-as-vortex give a G-free path?

### 1.2 Main Result

**PDTP Original.** In the PDTP superfluid condensate, particles are modelled as
vortex lines. The winding number n is determined by the vortex core condition:
the condensate superfluid velocity must equal c at the particle's Compton radius.

```
                   v_s(r_core) = c    [critical velocity = speed of sound = c]

   v_s(r) = (ħ / m_cond) × n / r     [superfluid velocity around vortex]

   Setting r_core = λ_C = ħ/(mc):

                   n = m_cond / m     [WINDING NUMBER]                    (1.1)
```

With m_cond = m_P (Planck mass), this gives n = m_P/m — the same orbital number
found in Phase 8, now derived from topology.

### 1.3 G-Free Chain

Given m_cond (the condensate quasiparticle mass, a free physical parameter):

```
   n   = m_cond / m                             [G-free, from Eq. 1.1]
   a_0 = λ_C / n  = ħ / (m_cond c)             [G-free lattice spacing]
   G   = c³ a_0² / ħ  = ħc / m_cond²           [PDTP bridge, G-free]    (1.2)
```

### 1.4 Bonus: Strategy A = Strategy B

The vortex derivation shows that Strategy A (measure breathing mode frequency
omega_gap) and Strategy B (derive m_cond from topology) are the **same
measurement**. The breathing mode gap IS the condensate quasiparticle mass:

```
   omega_gap = m_cond c² / ħ     [mass gap of breathing mode phonon]
   G = c⁵ / (ħ × omega_gap²)    [Strategy A formula, G-free]
     = ħc / m_cond²              [Strategy B formula, G-free]           (1.3)
     Both are identical.
```

### 1.5 What Remains

The condensate quasiparticle mass m_cond (= m_P) is the single remaining free
parameter. Deriving it from condensate micro-physics without G as input would
complete the non-circular derivation of G — PDTP's "Cavendish moment."

---

## 2. Background — The Circular Wall

From Parts 29–32 (and Phases 1–8 of the solver), every algebraic path to G is
circular. The wall can be stated precisely:

```
   PDTP bridge:   G = c³ a² / ħ
   Only solution: a = l_P = sqrt(ħG/c³)   [contains G — circular]
```

The systematic solver tested 729+ candidates for `a`. The best non-circular
result (Phase 2) was off by 0.12 decades but still used l_P as anchor. The
analytical proof (Phase 4) showed circularity is algebraically inevitable for
any power-law combination of particle masses.

**Phase 8 reframe:** Instead of "what is a?", ask "what is n?" where
n = λ_Compton / l_P = m_P / m. The winding number n is dimensionless; it could
have a topological origin that does not require G. Phase 9 derives n from the
vortex topology of the PDTP condensate.

---

## 3. The Vortex Picture of a Particle

### 3.1 Superfluid Topology

The PDTP spacetime condensate has a scalar phase field φ that lives on the circle
S¹ (since φ is a phase, it is periodic with period 2π). Topological defects of a
U(1) phase field in 2+1 dimensions (spatial 2D + time) are **vortex lines** —
codimension-2 objects where the phase winds by 2πn around the core.

**Source:**
[Quantized vortices in superfluids — Feynman (1955)](https://www.sciencedirect.com/science/article/abs/pii/S0079663808605887)

### 3.2 Particle as Vortex Worldline

In the PDTP condensate:
- A **particle** is a topological defect — a vortex in the condensate phase φ
- The **particle worldline** (1D in 4D spacetime) = a vortex line in the 3D spatial condensate
- The **winding number** n is the topological charge of the defect

This picture is physically motivated by:
- Superfluid helium: phonons as condensate quasiparticles, vortices as quantized defects
- BEC vortex dynamics: vortex-antivortex pairs as particle-antiparticle analog (Part 22)
- Skyrme model: baryons as topological solitons of a pion condensate (analogous structure)

**Source:**
[Topological defects in condensed matter, Mermin (1979)](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.51.591)

---

## 4. The Vortex Field Equation

### 4.1 Static PDTP Field Equation

The PDTP field equation for φ:

```
   □φ = Σᵢ gᵢ sin(ψᵢ − φ)                                              (4.1)
```

In the static limit (∂_t φ = 0) and far from the vortex core where the phase is
locked (sin(ψ − φ) → 0):

```
   ∇²φ = 0     [Laplace's equation]                                     (4.2)
```

### 4.2 The Vortex Solution

In cylindrical coordinates (r, θ, z) with the vortex along the z-axis:

```
   φ(r, θ) = n × θ                                                      (4.3)
```

**Verification:**

```
   ∇²φ = (1/r²) ∂²_θ φ = 0        [n × θ has no r-dependence]  ✓
   Winding integral: (1/2π) ∮ ∂_θ φ dθ = n                      ✓
```

This solution satisfies Eq. (4.2) exactly everywhere except r = 0 (the vortex
core). The topological invariant n is conserved and cannot change without a
phase transition or topological annihilation (particle-antiparticle annihilation
in PDTP language).

---

## 5. Superfluid Velocity and the Core Condition

### 5.1 Superfluid Velocity

In a superfluid BEC with condensate particle mass m_cond, the superfluid velocity
is proportional to the gradient of the condensate phase:

```
   v_s = (ħ / m_cond) × ∇φ                                              (5.1)
```

**Source:**
[Pethick & Smith, "Bose-Einstein Condensation in Dilute Gases" (2002), §7.1](https://www.cambridge.org/core/books/boseeinstein-condensation-in-dilute-gases/C9F0BB979D40D8CFB68E22F5D00FD54A)

For the vortex solution φ = nθ, the gradient in cylindrical coordinates is:

```
   ∇φ = (n/r) θ̂     [azimuthal direction only]
```

So the superfluid velocity is:

```
   v_s(r) = (ħ / m_cond) × n / r    [azimuthal, scales as 1/r]         (5.2)
```

### 5.2 The Critical Velocity

In a superfluid, the vortex **core** is the region where the condensate breaks
down — where the velocity would exceed the speed of sound c_s. For the PDTP
relativistic condensate, c_s = c (the condensate phonons travel at c, since
photons ARE condensate modes in this picture).

The vortex core edge is defined by:

```
   v_s(r_core) = c                                                       (5.3)
```

This is the **vortex core condition** — the boundary between the condensate
(outside) and the excluded core (inside).

Substituting Eq. (5.2) into (5.3):

```
   (ħ / m_cond) × n / r_core = c

   r_core = n × ħ / (m_cond × c) = n × λ_cond                          (5.4)
```

where λ_cond = ħ/(m_cond c) is the Compton wavelength of the condensate
quasiparticle. The core radius grows linearly with n.

**Physical picture:** The condensate swirls faster and faster as you approach
the vortex center (v_s ~ 1/r). At r = r_core, the swirling speed reaches c and
the condensate can no longer exist — this is the vortex core. The particle IS
this excluded region.

---

## 6. Deriving the Winding Number n

### 6.1 Particle Identification

**PDTP Original.** A particle of mass m occupies the vortex core. The physical
size of the particle — the radius of the region where the condensate is
excluded — equals the particle's Compton wavelength:

```
   r_core = λ_C = ħ / (m × c)    [Compton wavelength, G-free]          (6.1)
```

This identification is motivated by:
- The Compton wavelength is the natural quantum-mechanical size of a particle
- Below λ_C, quantum field theory breaks down (pair production threshold)
- The vortex core is the region where the condensate "doesn't know" the
  particle's internal structure — exactly the quantum uncertainty region

### 6.2 The Winding Number

Setting r_core from the core condition (Eq. 5.4) equal to the Compton wavelength
(Eq. 6.1):

```
   n × λ_cond = λ_C

   n = λ_C / λ_cond
     = [ħ/(mc)] / [ħ/(m_cond c)]
     = m_cond / m                                                        (6.2)
```

**Result:** The winding number n equals the ratio of the condensate quasiparticle
mass to the particle mass.

With m_cond = m_P (the Planck mass):

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   n = m_P / m                                              (6.3) │
│                                                                  │
│   PDTP Original: the winding number of a particle-vortex        │
│   in the PDTP condensate equals the ratio of Planck mass        │
│   to particle mass.  Derived from the vortex core condition.    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 6.3 Consistency with Phase 8

In Phase 8 (orbital_scanner.py), n = m_P/m was identified as the "orbital
quantum number" by dimensional analysis: n = λ_Compton/l_P = m_P/m. Phase 9
provides the physical derivation: this is the vortex topological charge,
determined by the core condition. Same result, now physically motivated.

---

## 7. The G-Free Chain

### 7.1 Chain Definition

Given m_cond as a free physical parameter of the condensate (not derived from G):

```
   Step 1:  n   = m_cond / m               [from Eq. 6.2, G-free]
   Step 2:  a_0 = λ_C / n                  [G-free]
              = [ħ/(mc)] / [m_cond/m]
              = ħ / (m_cond c)
              = λ_cond                     [condensate Compton wavelength]
   Step 3:  G   = c³ a_0² / ħ             [PDTP bridge, G-free]
              = c³ × [ħ/(m_cond c)]² / ħ
              = ħc / m_cond²                                             (7.1)
```

### 7.2 Why This Is Different

**Old logic (circular):**
```
   G  [given]  →  l_P = sqrt(ħG/c³)  →  a = l_P  →  G_pred = G  [circular]
```

**New logic (non-circular given m_cond):**
```
   m_cond  [given]  →  n = m_cond/m  →  a_0 = ħ/(m_cond c)  →  G = ħc/m_cond²
```

The direction of inference is reversed. G is now the **output**, not the input.
The input is m_cond — a physical mass that, in principle, could be measured
independently (e.g., from the breathing mode gap frequency).

### 7.3 Numerical Verification

Using m_cond = m_P = 2.1764×10⁻⁸ kg (CODATA 2018):

| Quantity | Formula | Value | Check |
|---------|---------|-------|-------|
| a_0 | ħ/(m_P c) | 1.6163×10⁻³⁵ m | = l_P ✓ |
| G_pred | ħc/m_P² | 6.6743×10⁻¹¹ m³/kg/s² | = G_known ✓ |
| n (electron) | m_P/m_e | 2.389×10²² | dimensionless ✓ |

**Verification script:** `simulations/solver/vortex_winding.py` — all 11 SM
particles give G_pred/G_known = 1.000000; Sudoku engine 13/13 pass.

---

## 8. Sudoku Verification

The Sudoku engine (Part 30) tests a candidate lattice spacing against 13
established physics equations. Running a_0 = ħ/(m_P c) = l_P through all 13:

| Test | Result |
|------|--------|
| Newton's G | PASS (ratio = 1.000000) |
| Planck length | PASS |
| Planck mass | PASS |
| Planck time | PASS |
| Planck energy | PASS |
| Planck temperature | PASS |
| Condensate density | PASS |
| Schwarzschild radius | PASS |
| Hawking temperature | PASS |
| Gravitational α_G | PASS |
| Hubble critical density | PASS |
| Earth surface gravity | PASS |
| Hierarchy ratio α_G/α_EM | PASS |

**Score: 13/13.** The vortex-derived chain is internally consistent.

The circularity is now precisely located: in `m_cond = m_P`, where m_P contains G.
If m_cond were independently measured or derived, the chain would be fully G-free.

---

## 9. Unification of Strategy A and Strategy B

### 9.1 Previous Understanding

From [pdtp_findings_summary.md](../overview/pdtp_findings_summary.md) §8:
- **Strategy A:** Measure omega_gap from breathing mode → a → G
- **Strategy B:** Derive R = α_G/α_EM from lattice topology → G

These appeared to be independent paths. The vortex derivation shows they are
the **same measurement** expressed differently.

### 9.2 The Connection

The breathing mode phonon in PDTP has a mass gap because the cos coupling
`g cos(ψ − φ)` acts as a potential well for the condensate. The mass of the
breathing mode phonon is:

```
   m_phonon = m_cond   [the condensate quasiparticle mass]
```

The gap frequency is:

```
   omega_gap = m_cond × c² / ħ                                          (9.1)
```

Substituting into Strategy A's G formula:

```
   G = c³ a² / ħ  with  a = c/omega_gap:

   G = c³ × [c/omega_gap]² / ħ = c⁵ / (ħ × omega_gap²)
     = c⁵ / (ħ × [m_cond c²/ħ]²)
     = c⁵ × ħ / (m_cond² c⁴)
     = ħc / m_cond²                                                      (9.2)
```

This is identical to Strategy B's G = ħc/m_cond² (Eq. 7.1).

### 9.3 The Unified Picture

```
   ┌─────────────────────────────────────────────────────────────┐
   │                                                             │
   │   ONE OPEN QUESTION:                                        │
   │   "What is m_cond, the condensate quasiparticle mass?"     │
   │                                                             │
   │   Strategy A phrasing:  "What is omega_gap?"               │
   │   Strategy B phrasing:  "What is the hierarchy ratio n?"   │
   │   Vortex phrasing:      "What sets the vortex core size?"  │
   │                                                             │
   │   All three are the same question.  G = ħc/m_cond².        │
   │                                                             │
   └─────────────────────────────────────────────────────────────┘
```

---

## 10. The Remaining Gap

### 10.1 What Is m_cond?

The condensate quasiparticle mass m_cond is the energy scale at which the PDTP
spacetime condensate "crystallizes." No existing physical theory derives this
from known particle physics or cosmological parameters without G.

Candidates tested (all fail):

| m_cond candidate | G_pred / G_known | Decades off |
|----------------|-----------------|-------------|
| m_Planck (target) | 1.000 | 0.0 |
| m_Higgs (125 GeV) | 9.5×10³³ | +34.0 |
| m_neutrino (~0.1 eV) | 1.5×10⁶⁰ | +60.2 |
| ħH₀/c² (Hubble) | 7.2×10¹²¹ | +121.9 |

Every known particle and scale gives G_pred >> G_known. This is the hierarchy
problem stated as a condensate mass problem.

### 10.2 What Could Fix m_cond (Theoretical Paths)

**(a) Thermodynamic:** If the condensate formed at temperature T_cond:
```
   m_cond = k_B T_cond / c²
   T_cond = m_P c² / k_B ≈ 1.4×10³² K   [Planck temperature]
```
This requires the condensate to have formed at the Planck temperature — i.e.,
at the Big Bang. Physically plausible but doesn't derive T_cond from first principles.

**(b) Holographic (Dvali):** If the condensate has N_sp species:
```
   m_cond = m_fundamental / sqrt(N_sp)
   m_P    = m_fundamental / sqrt(N_sp)   [definition]
```
N_sp from lattice topology: if N_sp = (R_H/λ_cond)^d for d extra dimensions,
there is a d that gives m_cond = m_P — but d is not derived.

**(c) Dynamical self-consistency:** The breathing mode mass gap in a BEC obeys:
```
   omega_gap² = g_coupling × ρ_cond / m_cond
```
where ρ_cond is the condensate number density and g_coupling is the coupling.
Since omega_gap = m_cond c²/ħ, this becomes a self-consistency equation for m_cond.
Substituting PDTP values may give a non-circular constraint — **this is the
highest-priority next step** (Part 34).

---

## 11. What This Achieves and What Remains

### What Was Achieved (Part 33)

1. **Particle topology:** Particles are vortex lines in the PDTP condensate phase φ.
   The field equation is satisfied; the winding number is topologically quantized.

2. **Winding number derived:** n = m_cond/m from the vortex core condition
   v_s(λ_Compton) = c. This is a physical derivation, not dimensional analysis.

3. **G-free chain:** m_cond → n → a_0 → G is fully G-free given m_cond.
   Verified numerically: 13/13 Sudoku pass for all 11 SM particles.

4. **Unification:** Strategy A (omega_gap) = Strategy B (m_cond). One open
   problem, not two.

### What Remains (Part 34)

The single remaining question: **what fixes m_cond?**

The condensate quasiparticle mass is the PDTP analog of Newton's G — it is the
fundamental parameter of the framework. Just as Newton's G was circular until
Cavendish measured it with an independent apparatus, m_cond is circular until
either:
- An independent measurement gives omega_gap (Strategy A — requires Planck-frequency detector)
- A micro-physical derivation gives m_cond without G as input (Part 34)

The Part 34 self-consistency approach (option c above) is the most tractable: it
requires solving one algebraic equation for m_cond using only condensate
parameters (ρ_cond, g_coupling) that can themselves be expressed G-free.

---

## 12. References

**Source:** Feynman, R.P. (1955), "Application of quantum mechanics to liquid helium."
*Progress in Low Temperature Physics* 1, 17–53.
[doi:10.1016/S0079-6638(08)60077-3](https://www.sciencedirect.com/science/article/abs/pii/S0079663808605887)

**Source:** Mermin, N.D. (1979), "The topological theory of defects in ordered media."
*Reviews of Modern Physics* 51, 591.
[doi:10.1103/RevModPhys.51.591](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.51.591)

**Source:** Pethick, C.J. & Smith, H. (2002), *Bose-Einstein Condensation in Dilute
Gases*, Cambridge University Press. §7.1 (superfluid velocity), §5.5 (vortex core).

**Source:** [Wikipedia: Quantum vortex](https://en.wikipedia.org/wiki/Quantum_vortex)
(Feynman relation; superfluid velocity; circulation quantization)

**Source:** [Wikipedia: Compton wavelength](https://en.wikipedia.org/wiki/Compton_wavelength)
(λ_C = ħ/mc; pair production threshold interpretation)

**PDTP Original:** Vortex core condition n = m_cond/m (this document).
**PDTP Original:** G-free chain m_cond → n → a_0 → G = ħc/m_cond² (this document).
**PDTP Original:** Strategy A = Strategy B unification via omega_gap = m_cond c²/ħ (this document).

**Verification:** `simulations/solver/vortex_winding.py` (Phase 9)

---

*Last updated: 2026-03-01*

*Previous part: [hard_problems.md](hard_problems.md) (Part 29–32 circularity analysis)*
*Next: Part 34 — condensate self-consistency for m_cond (in progress)*
*Full findings: [pdtp_findings_summary.md](../overview/pdtp_findings_summary.md)*

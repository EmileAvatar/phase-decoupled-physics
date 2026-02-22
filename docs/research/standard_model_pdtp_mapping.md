# Standard Model and PDTP: Particle-Force Mapping (Part 20)

**Status:** Systematic comparison — established physics + PDTP interpretation
**Date:** 2026-02-22
**Prerequisites:** Parts 1–5, 12, 14;
[advanced_formalization.md](advanced_formalization.md) §3,
[koide_derivation.md](koide_derivation.md),
[fine_structure_derivation.md](fine_structure_derivation.md),
[condensate_microphysics.md](condensate_microphysics.md)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Standard Model — Established Physics](#2-the-standard-model--established-physics)
3. [PDTP Interpretation of Particles](#3-pdtp-interpretation-of-particles)
4. [PDTP Interpretation of Forces](#4-pdtp-interpretation-of-forces)
5. [The Combined Lagrangian — Full Picture](#5-the-combined-lagrangian--full-picture)
6. [Mass Hierarchy — SM Problem, PDTP Perspective](#6-mass-hierarchy--sm-problem-pdtp-perspective)
7. [What PDTP Explains That the SM Cannot](#7-what-pdtp-explains-that-the-sm-cannot)
8. [What the SM Explains That PDTP Cannot (Yet)](#8-what-the-sm-explains-that-pdtp-cannot-yet)
9. [Honest Assessment](#9-honest-assessment)
10. [References](#10-references)

---

## 1. Executive Summary

This document provides a systematic side-by-side mapping of every Standard Model
particle and force to its PDTP interpretation.

**Key finding:** PDTP does **not** replace the Standard Model. It **adds** a
gravitational mechanism — phase-locking between matter-wave phases ψᵢ and the
spacetime condensate phase φ — while preserving the entire SM gauge structure,
particle content, and interaction rules.

What PDTP changes:
- Gravity: from geometric curvature (GR) to phase synchronization
- Mass interpretation: from "Higgs gives mass" to "Higgs gives mass AND mass
  determines gravitational coupling strength"
- Dark energy: from cosmological constant to phase drift

What PDTP preserves:
- All 17 SM particles and their properties
- All gauge symmetries: SU(3)_C × SU(2)_L × U(1)_Y
- All SM forces: electromagnetic, strong, weak
- The Higgs mechanism for electroweak symmetry breaking

---

## 2. The Standard Model — Established Physics

### 2.1 Particle Content

The Standard Model contains 17 fundamental particles organized into fermions
(matter) and bosons (force carriers).

**Source:** [Standard Model — Wikipedia](https://en.wikipedia.org/wiki/Standard_Model)
**Source:** Particle Data Group, R.L. Workman et al. (2024), Phys. Rev. D 110,
030001. [PDG](https://pdg.lbl.gov/)

#### Quarks (spin-½ fermions, feel all four forces)

| Particle | Symbol | Mass (MeV/c²) | Charge | Color | Generation |
|----------|--------|---------------|--------|-------|------------|
| Up | u | 2.16 ± 0.07 | +2/3 | RGB | 1st |
| Down | d | 4.70 ± 0.07 | −1/3 | RGB | 1st |
| Charm | c | 1,270 ± 20 | +2/3 | RGB | 2nd |
| Strange | s | 93.5 ± 0.8 | −1/3 | RGB | 2nd |
| Top | t | 172,570 ± 290 | +2/3 | RGB | 3rd |
| Bottom | b | 4,180 ± 20 | −1/3 | RGB | 3rd |

**Source:** [Quark — Wikipedia](https://en.wikipedia.org/wiki/Quark);
PDG 2024 quark mass review

#### Leptons (spin-½ fermions, no color charge)

| Particle | Symbol | Mass (MeV/c²) | Charge | Generation |
|----------|--------|---------------|--------|------------|
| Electron | e⁻ | 0.511 | −1 | 1st |
| Electron neutrino | ν_e | < 0.0000008 | 0 | 1st |
| Muon | μ⁻ | 105.658 | −1 | 2nd |
| Muon neutrino | ν_μ | < 0.17 | 0 | 2nd |
| Tau | τ⁻ | 1,776.86 | −1 | 3rd |
| Tau neutrino | ν_τ | < 18.2 | 0 | 3rd |

**Source:** [Lepton — Wikipedia](https://en.wikipedia.org/wiki/Lepton); PDG 2024

Note: Neutrino mass eigenstates have nonzero masses (established by oscillation
experiments), with Σm_ν < 0.12 eV from cosmological bounds.

**Source:** [Neutrino oscillation — Wikipedia](https://en.wikipedia.org/wiki/Neutrino_oscillation)

#### Gauge Bosons (spin-1, force carriers)

| Particle | Symbol | Mass (GeV/c²) | Charge | Force mediated |
|----------|--------|---------------|--------|----------------|
| Photon | γ | 0 (exact) | 0 | Electromagnetic |
| Gluon (×8) | g | 0 (exact) | 0 | Strong |
| W boson | W± | 80.3692 ± 0.0133 | ±1 | Weak |
| Z boson | Z⁰ | 91.1880 ± 0.0020 | 0 | Weak |

**Source:** [Gauge boson — Wikipedia](https://en.wikipedia.org/wiki/Gauge_boson);
PDG 2024

#### Scalar Boson (spin-0)

| Particle | Symbol | Mass (GeV/c²) | Charge | Role |
|----------|--------|---------------|--------|------|
| Higgs boson | H | 125.20 ± 0.11 | 0 | Electroweak symmetry breaking |

**Source:** [Higgs boson — Wikipedia](https://en.wikipedia.org/wiki/Higgs_boson);
PDG 2024

### 2.2 The Four Fundamental Forces

#### Gravity (described by General Relativity, not part of the SM)

Einstein's field equation:

```
G_μν + Λg_μν = (8πG/c⁴) T_μν                                          ... (2.1)
```

- Mediator: graviton (hypothetical, spin-2, massless)
- Range: infinite (1/r² law)
- Coupling strength: G ≈ 6.674 × 10⁻¹¹ m³/(kg·s²)
- Relative strength: ~10⁻³⁹ (weakest)

**Source:** [General relativity — Wikipedia](https://en.wikipedia.org/wiki/General_relativity)

#### Electromagnetism

Maxwell's equations in covariant form:

```
∂_μ F^μν = μ₀ J^ν                                                      ... (2.2)
F_μν = ∂_μ A_ν − ∂_ν A_μ                                               ... (2.3)
```

- Gauge group: U(1)_EM
- Mediator: photon (γ)
- Coupling constant: α = e²/(4πε₀ℏc) ≈ 1/137.036
- Range: infinite
- Relative strength: ~10⁻²

**Source:** [Electromagnetic field — Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_field)

#### Strong Force

QCD Lagrangian density:

```
ℒ_QCD = −¼ G^a_μν G^a_μν + Σ_q q̄ᵢ(iγ^μ(D_μ)ᵢⱼ − m_q δᵢⱼ) qⱼ       ... (2.4)
```

where G^a_μν = ∂_μ A^a_ν − ∂_ν A^a_μ + g_s f^{abc} A^b_μ A^c_ν is the
gluon field strength tensor and D_μ = ∂_μ − ig_s T^a A^a_μ is the covariant
derivative.

- Gauge group: SU(3)_C
- Mediator: 8 gluons
- Coupling constant: α_s ≈ 0.118 at M_Z scale (runs with energy)
- Range: ~1 fm (confinement)
- Λ_QCD ≈ 200 MeV (confinement scale)
- Relative strength: 1 (reference)

**Source:** [Quantum chromodynamics — Wikipedia](https://en.wikipedia.org/wiki/Quantum_chromodynamics)

#### Weak Force

Electroweak Lagrangian (before symmetry breaking):

```
ℒ_EW = −¼ W^a_μν W^a_μν − ¼ B_μν B^μν + ψ̄_L iγ^μ D_μ ψ_L + ψ̄_R iγ^μ D_μ ψ_R
                                                                        ... (2.5)
```

where W^a_μν (a = 1,2,3) is the SU(2)_L field strength and B_μν is the U(1)_Y
field strength.

- Gauge group: SU(2)_L × U(1)_Y → U(1)_EM (after Higgs mechanism)
- Mediators: W±, Z⁰ (massive after symmetry breaking)
- Coupling: G_F = 1.1664 × 10⁻⁵ GeV⁻² (Fermi constant)
- Range: ~10⁻¹⁸ m (limited by W/Z mass)
- Relative strength: ~10⁻⁵

**Source:** [Electroweak interaction — Wikipedia](https://en.wikipedia.org/wiki/Electroweak_interaction)

### 2.3 Key SM Equations Summary

The complete SM Lagrangian:

```
ℒ_SM = ℒ_gauge + ℒ_fermion + ℒ_Higgs + ℒ_Yukawa                       ... (2.6)
```

where:

```
ℒ_gauge   = −¼ G^a_μν G^a_μν − ¼ W^a_μν W^a_μν − ¼ B_μν B^μν         ... (2.7)
ℒ_fermion = Σ_f ψ̄_f iγ^μ D_μ ψ_f                                      ... (2.8)
ℒ_Higgs   = |D_μ H|² − V(H),  V(H) = −μ² |H|² + λ|H|⁴               ... (2.9)
ℒ_Yukawa  = −y_f ψ̄_L H ψ_R + h.c.                                     ... (2.10)
```

**Source:** [Standard Model (mathematical formulation) — Wikipedia](https://en.wikipedia.org/wiki/Mathematical_formulation_of_the_Standard_Model)

### 2.4 How Mass Arises — The Higgs Mechanism

The Higgs field H is an SU(2) doublet with hypercharge Y = 1:

```
H = (H⁺, H⁰)ᵀ
```

In the vacuum state, H acquires a vacuum expectation value (VEV):

```
⟨H⟩ = (0, v/√2)ᵀ,    v = (√2 G_F)^{−1/2} ≈ 246 GeV                  ... (2.11)
```

This breaks SU(2)_L × U(1)_Y → U(1)_EM, generating masses:

**Gauge boson masses:**

```
M_W = gv/2 ≈ 80.4 GeV                                                 ... (2.12)
M_Z = M_W / cos θ_W ≈ 91.2 GeV                                        ... (2.13)
```

where g is the SU(2)_L coupling and θ_W ≈ 28.7° is the Weinberg angle.

**Fermion masses (Yukawa coupling):**

```
m_f = y_f v / √2                                                       ... (2.14)
```

where y_f is the Yukawa coupling constant for fermion f.

**Source:** [Higgs mechanism — Wikipedia](https://en.wikipedia.org/wiki/Higgs_mechanism)

**Key point:** The Yukawa couplings y_f are **free parameters** of the SM. The
Higgs mechanism explains HOW particles get mass, not WHY specific values occur.

### 2.5 What the Standard Model Does NOT Explain

Despite extraordinary precision (predictions verified to 10+ decimal places in
some cases), the SM has fundamental gaps:

1. **Gravity** — not included in the SM framework
2. **Dark matter** — no SM particle candidate
3. **Dark energy** — no mechanism for cosmic acceleration
4. **Mass hierarchy** — why m_top/m_electron ≈ 340,000 (Yukawa couplings unexplained)
5. **Matter-antimatter asymmetry** — SM CP violation insufficient
6. **Neutrino masses** — require BSM extension (Dirac or Majorana)
7. **19+ free parameters** — masses, mixing angles, coupling constants are inputs
8. **Strong CP problem** — why θ_QCD ≈ 0 (no explanation)
9. **Quantum gravity** — incompatible with GR at Planck scale

**Source:** [Physics beyond the Standard Model — Wikipedia](https://en.wikipedia.org/wiki/Physics_beyond_the_Standard_Model)

---

## 3. PDTP Interpretation of Particles

### 3.1 The PDTP Particle Picture

**PDTP Original.** In PDTP, all matter consists of standing-wave patterns in
phase fields ψᵢ(x,t), coupled to the spacetime condensate phase φ(x,t) via:

```
ℒ_coupling = Σᵢ gᵢ cos(ψᵢ − φ)                                        ... (3.1)
```

The key interpretive mappings:

| SM Concept | PDTP Interpretation |
|-----------|-------------------|
| Particle | Stable standing-wave pattern in phase field ψ |
| Mass | Phase-locking strength to spacetime condensate: m ∝ gᵢ |
| Quantum numbers | Topological invariants of the phase configuration |
| Particle identity | Specific mode of the standing wave (frequency, topology) |
| Antiparticle | Same mode with conjugate phase: ψ → −ψ |

**Critical point:** PDTP does not change WHAT the particles are or HOW they
interact with each other (SM forces). It adds a new layer: how each particle
gravitationally couples to spacetime through phase-locking.

### 3.2 Quarks in PDTP

**PDTP Original.** Quarks are confined phase modes — standing waves that cannot
exist as isolated, free-propagating waves.

| SM Property | PDTP Interpretation |
|------------|-------------------|
| Confinement | Phase modes below confinement scale (~1 fm) cannot decouple from the strong-interaction phase field |
| Color charge | Internal SU(3) phase degrees of freedom — **preserved exactly** |
| Quark mass (current) | Yukawa coupling to Higgs: m_q = y_q v/√2 — **unchanged** |
| Constituent mass | Effective mass from QCD binding — in PDTP, this is the dominant contribution to gravitational coupling |

**PDTP does not replace QCD.** The SU(3) gauge structure, confinement, and
asymptotic freedom are all preserved. PDTP adds only: the quark's gravitational
coupling to φ is through its total effective mass (current mass + QCD binding).

Example — the proton:

```
m_proton = 938.3 MeV/c²
m_u + m_u + m_d = 2.16 + 2.16 + 4.70 ≈ 9.0 MeV/c² (only ~1% of proton mass)
m_QCD_binding ≈ 929 MeV/c² (~99% from gluon field energy and quark kinetic energy)
```

**Source:** [Proton — Wikipedia](https://en.wikipedia.org/wiki/Proton)

In PDTP: the proton's gravitational coupling is g_proton ∝ 938.3 MeV, NOT
∝ 9.0 MeV. The full mass-energy couples to φ. This is consistent with the
equivalence principle: all forms of energy gravitate.

### 3.3 Leptons in PDTP

**PDTP Original.** Leptons are free-propagating phase modes — standing waves
that can exist independently without confinement.

#### Charged Leptons

| Particle | Mass (MeV/c²) | PDTP coupling gᵢ | Phase-lock strength |
|----------|---------------|-------------------|-------------------|
| Electron | 0.511 | g_e ∝ 0.511 MeV | Weakest charged lepton lock |
| Muon | 105.658 | g_μ ∝ 105.658 MeV | ~207× electron |
| Tau | 1,776.86 | g_τ ∝ 1,776.86 MeV | ~3,477× electron |

The mass hierarchy among charged leptons follows the Koide formula:

```
Q ≡ (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3                  ... (3.2)
```

This is a Z₃ phase harmonic structure: √mᵢ = μ(1 + δ cos(θ₀ + 2πi/3)) with
δ = √2.

**Source:** Koide formula — see [koide_derivation.md](koide_derivation.md) (Part 4)

**PDTP interpretation:** The three charged lepton masses arise from a Z₃
symmetric phase structure — three modes equally spaced in phase angle, with a
specific amplitude ratio δ = √2 from equal partition of symmetric and
symmetry-breaking energy.

#### Neutrinos

| Particle | Mass bound | PDTP interpretation |
|----------|-----------|-------------------|
| ν_e | < 0.8 eV | Extremely weak phase-lock |
| ν_μ | < 0.17 MeV | Very weak phase-lock |
| ν_τ | < 18.2 MeV | Weak phase-lock |

Neutrino masses are at least 6 orders of magnitude smaller than the electron
mass. In PDTP: neutrinos are the most weakly phase-locked particles, barely
coupling to the spacetime condensate.

**Neutrino oscillations:** In the SM, neutrino flavour states are superpositions
of mass eigenstates, leading to oscillations with probability:

```
P(ν_α → ν_β) = sin²(2θ) sin²(Δm² L / (4E))                           ... (3.3)
```

**Source:** [Neutrino oscillation — Wikipedia](https://en.wikipedia.org/wiki/Neutrino_oscillation)

**PDTP interpretation:** Neutrino oscillations are phase interference between
mass eigenstates, each with a slightly different phase-locking frequency to φ.
The oscillation arises because the different mass eigenstates accumulate phase
at different rates — precisely the PDTP picture of phase evolution. PDTP does
not modify the oscillation formula; it provides a natural language for it.

### 3.4 Gauge Bosons in PDTP

**PDTP Original.** PDTP preserves the SM gauge structure completely. The gauge
bosons continue to mediate forces exactly as in the SM. PDTP only adds their
gravitational coupling to φ.

#### Photon (γ)

- Mass: 0 (exact, by U(1)_EM gauge invariance)
- In PDTP: couples to φ **indirectly** via acoustic metric geodesics
- Photon propagates on null geodesics of the effective spacetime metric
- The photon's EM stress-energy tensor is traceless: T^μ_μ = 0
- Therefore: photons do NOT source the scalar field □φ at classical level
- But: photon energy gravitates via the tensor sector (Part 12)

**Source:** See [hard_problems.md](hard_problems.md) §4,
[photon_gravity_analysis.md](photon_gravity_analysis.md)

#### Gluons (g, ×8)

- Mass: 0 (exact, by SU(3)_C gauge invariance)
- In PDTP: like photons, gluons have traceless stress-energy
- Cannot directly source □φ
- But: gluon field energy is ~99% of proton mass — it gravitates via
  composite particle binding energy
- This is the dominant gravitational coupling for all hadrons

#### W± and Z⁰ Bosons

- Mass: M_W ≈ 80.4 GeV, M_Z ≈ 91.2 GeV (massive)
- In PDTP: massive bosons have de Broglie phases → direct cos(ψ − φ) coupling
- Their coupling strength: g_W ∝ 80.4 GeV, g_Z ∝ 91.2 GeV
- But: W/Z are virtual in most processes (real W/Z only at high-energy colliders)
- Their gravitational effect is through the mass-energy they contribute to processes

### 3.5 Higgs Boson in PDTP

**PDTP Original.** The Higgs field and the PDTP condensate field φ are both
scalar order parameters that break symmetry. This parallel is structurally
significant.

| Property | Higgs Field H | PDTP Condensate Φ |
|----------|--------------|-------------------|
| Type | Complex SU(2) doublet | Complex scalar singlet Φ = √ρ₀ e^{iφ} |
| Symmetry broken | SU(2)_L × U(1)_Y → U(1)_EM | Lorentz group (via tetrad) |
| VEV | v ≈ 246 GeV | ρ₀ (condensate density, unknown) |
| Excitation | Higgs boson (125.2 GeV) | Breathing mode (massive scalar) |
| What it gives | Fermion and gauge boson masses | Gravitational coupling strength |
| Goldstone modes | 3 (eaten by W±, Z⁰) | Phonon = graviton (eaten by metric) |

**Structural parallel:** Just as the Higgs boson is the radial excitation of the
Higgs condensate, the breathing mode (Part 3, §1) is the radial excitation of
the PDTP spacetime condensate. The Higgs mechanism gives particles their
inertial mass; the PDTP mechanism gives particles their gravitational coupling.

**Speculative connection:** The Higgs VEV v = 246 GeV sets the electroweak scale.
The PDTP condensate density ρ₀ sets the gravitational scale. The hierarchy between
them (the gauge hierarchy problem) might be related to the phase stiffness κ of
the condensate. This requires condensate microphysics to investigate (Part 21).

### 3.6 Complete Particle Table — SM vs PDTP

**PDTP Original.** The coupling constant gᵢ is proportional to mass (from
G_derivation.md): gᵢ = (4πG/c⁴) × mᵢc² for a point-particle approximation.
Since G/c⁴ ≈ 8.26 × 10⁻⁴⁵ s²/(kg·m), the coupling values are extremely small.

| Particle | Mass | SM mass source | PDTP: coupling gᵢ (s⁻²) | PDTP: interpretation |
|----------|------|---------------|--------------------------|---------------------|
| u quark | 2.16 MeV | Yukawa | ~3.2 × 10⁻⁵⁸ | Confined phase mode |
| d quark | 4.70 MeV | Yukawa | ~7.0 × 10⁻⁵⁸ | Confined phase mode |
| c quark | 1.27 GeV | Yukawa | ~1.9 × 10⁻⁵⁵ | Confined phase mode |
| s quark | 93.5 MeV | Yukawa | ~1.4 × 10⁻⁵⁶ | Confined phase mode |
| t quark | 172.6 GeV | Yukawa | ~2.6 × 10⁻⁵³ | Strongest quark lock |
| b quark | 4.18 GeV | Yukawa | ~6.2 × 10⁻⁵⁵ | Confined phase mode |
| Electron | 0.511 MeV | Yukawa | ~7.6 × 10⁻⁵⁹ | Free phase mode |
| Muon | 105.7 MeV | Yukawa | ~1.6 × 10⁻⁵⁶ | Free phase mode |
| Tau | 1.777 GeV | Yukawa | ~2.6 × 10⁻⁵⁵ | Free phase mode |
| ν_e | < 0.8 eV | BSM | < 1.2 × 10⁻⁶⁴ | Barely locked |
| ν_μ | < 0.17 MeV | BSM | < 2.5 × 10⁻⁵⁹ | Barely locked |
| ν_τ | < 18.2 MeV | BSM | < 2.7 × 10⁻⁵⁷ | Barely locked |
| Photon | 0 | Gauge sym. | 0 | Indirect (acoustic) |
| Gluon | 0 | Gauge sym. | 0 | Indirect (binding) |
| W± | 80.4 GeV | Higgs | ~1.2 × 10⁻⁵³ | Massive boson lock |
| Z⁰ | 91.2 GeV | Higgs | ~1.4 × 10⁻⁵³ | Massive boson lock |
| Higgs | 125.2 GeV | Self-coupling | ~1.9 × 10⁻⁵³ | Scalar condensate excitation |

Note: gᵢ values are order-of-magnitude estimates using gᵢ ~ Gmᵢ/(ℏc) in
natural units. The exact relationship depends on condensate microphysics
(see Part 14).

---

## 4. PDTP Interpretation of Forces

### 4.1 Gravity — The PDTP Force

**This is the one force PDTP reinterprets.**

#### In General Relativity (standard):

```
G_μν = (8πG/c⁴) T_μν                                                   ... (4.1)
```

Gravity = curvature of spacetime caused by stress-energy.

#### In PDTP:

```
ℒ_gravity = Σᵢ gᵢ cos(ψᵢ − φ)                                         ... (4.2)

Field equations:
  □φ = Σᵢ gᵢ sin(ψᵢ − φ)                                              ... (4.3)
  □ψⱼ = −gⱼ sin(ψⱼ − φ)                                               ... (4.4)
```

**Source:** [mathematical_formalization.md](mathematical_formalization.md) §2–3

Gravity = phase synchronization tendency between matter-wave phases and the
spacetime condensate phase.

**Why gravity is different from other forces in PDTP:**

| Property | SM gauge forces | PDTP gravity |
|----------|----------------|-------------|
| Mechanism | Gauge boson exchange | Phase synchronization |
| Mediator | Spin-1 particles | No mediator (collective effect) |
| Symmetry | Local gauge invariance | Global U(1) phase symmetry |
| Universality | Force-specific (charge-dependent) | Universal (all mass-energy) |
| Renormalizability | Yes (SM forces) | Not applicable (emergent) |
| Strength | Strong (α_s ~ 0.1) | Extremely weak (G ~ 10⁻¹¹) |

**Newtonian limit recovery:**

In the weak-field, non-relativistic limit:

```
∇²φ = 4πG ρ                                                            ... (4.5)
```

This is the Poisson equation for Newtonian gravity, recovered from eq. (4.3)
with the linearization sin(ψ − φ) ≈ ψ − φ.

**Source:** [mathematical_formalization.md](mathematical_formalization.md) §7

**Full GR recovery (tensor sector):**

The tetrad extension (Part 12) recovers the Einstein equation:

```
G_μν = 8πG T_μν                                                        ... (4.6)
```

as the field equation for the tetrad sector, with the scalar sector providing
the phase-locking mechanism.

**Source:** [tetrad_extension.md](tetrad_extension.md) §4

### 4.2 Electromagnetism — Unchanged

#### SM description:

- Gauge group: U(1)_EM
- Coupling: α = e²/(4πε₀ℏc) ≈ 1/137.036
- Lagrangian: ℒ_EM = −¼F_μν F^μν + ψ̄(iγ^μ D_μ − m)ψ

```
Maxwell's equations:
  ∂_μ F^μν = J^ν    (inhomogeneous)                                    ... (4.7)
  ∂_{[μ} F_{νρ]} = 0  (homogeneous, Bianchi identity)                  ... (4.8)
```

**Source:** [Quantum electrodynamics — Wikipedia](https://en.wikipedia.org/wiki/Quantum_electrodynamics)

#### PDTP addition:

PDTP does **not** modify electromagnetism. The only addition:

1. **Photons follow acoustic metric geodesics** — the effective spacetime
   metric felt by light is determined by the condensate flow (Part 3b §4).
   This reproduces gravitational lensing with the correct factor of 2.

2. **Fine-structure constant interpretation:** α = Z₀/(2R_K) — the ratio of
   electromagnetic impedance to quantum impedance — interpreted as coupling
   efficiency between EM and matter-wave phase media (Part 5).

**Source:** [fine_structure_derivation.md](fine_structure_derivation.md)

### 4.3 Strong Force — Unchanged

#### SM description:

- Gauge group: SU(3)_C
- Coupling: α_s ≈ 0.118 at M_Z (runs with energy)
- Asymptotic freedom: α_s → 0 at high energy

```
QCD β-function (1-loop):
  β(g_s) = −(11N_c − 2N_f)/(48π²) g_s³                                ... (4.9)
```

With N_c = 3 colors and N_f = 6 flavors: β < 0 → asymptotic freedom.

**Source:** [Asymptotic freedom — Wikipedia](https://en.wikipedia.org/wiki/Asymptotic_freedom)

- Confinement: quarks and gluons are bound into color-neutral hadrons
- Confinement scale: Λ_QCD ≈ 200 MeV (energy below which coupling becomes strong)

#### PDTP addition:

PDTP does **not** modify QCD. The only connection:

**QCD binding energy contributes to gravitational mass.** In PDTP, the coupling
gᵢ of a composite hadron to the spacetime condensate is proportional to its
total mass-energy — which is ~99% QCD binding energy for nucleons.

```
g_proton ∝ m_proton c² = 938.3 MeV    (not 9.0 MeV from quark masses alone)
```

This is simply the equivalence principle: all forms of energy gravitate equally.
PDTP provides a mechanism (phase-locking strength proportional to total mass),
but the numerical result is the same as GR.

### 4.4 Weak Force — Unchanged

#### SM description:

- Gauge group: SU(2)_L × U(1)_Y, broken to U(1)_EM by Higgs mechanism
- Fermi constant: G_F = 1.1664 × 10⁻⁵ GeV⁻²
- Range: ~10⁻¹⁸ m (limited by M_W, M_Z)

Key processes:
- Beta decay: n → p + e⁻ + ν̄_e (via W⁻)
- Neutrino scattering: ν_e + e⁻ → ν_e + e⁻ (via Z⁰)
- Quark mixing: described by CKM matrix

```
CKM matrix:
V_CKM = | V_ud  V_us  V_ub |     (3×3 unitary matrix)                 ... (4.10)
        | V_cd  V_cs  V_cb |
        | V_td  V_ts  V_tb |
```

**Source:** [Weak interaction — Wikipedia](https://en.wikipedia.org/wiki/Weak_interaction);
[CKM matrix — Wikipedia](https://en.wikipedia.org/wiki/Cabibbo%E2%80%93Kobayashi%E2%80%93Maskawa_matrix)

#### PDTP addition:

PDTP does **not** modify the weak force. The interpretive connection:

- **Weak decay = phase reconfiguration.** When a neutron decays to a proton,
  the quark phase configuration transforms: d → u + W⁻. In PDTP language,
  this is a transition between two different standing-wave modes of the phase
  field.

- **Neutrino oscillations** fit naturally into PDTP's phase language: different
  mass eigenstates evolve at different phase rates, producing interference.

- **CKM mixing** is preserved exactly — PDTP adds nothing to the mixing angles
  or CP violation parameters.

### 4.5 Force Comparison Table

| Force | Gauge group | Mediator | Range | SM coupling | PDTP changes? | PDTP interpretation |
|-------|-----------|---------|-------|------------|--------------|-------------------|
| Gravity | — (GR) | graviton? | ∞ | G | **YES** | Phase synchronization cos(ψ−φ) |
| EM | U(1)_EM | γ | ∞ | α ≈ 1/137 | No | Impedance matching (Part 5) |
| Strong | SU(3)_C | g (×8) | ~1 fm | α_s ≈ 0.118 | No | Binding energy → gravitational mass |
| Weak | SU(2)_L×U(1)_Y | W±, Z⁰ | ~10⁻¹⁸ m | G_F | No | Phase reconfiguration |

**Bottom line:** PDTP modifies ONE force (gravity) and preserves THREE (EM,
strong, weak) exactly as they are in the Standard Model.

---

## 5. The Combined Lagrangian — Full Picture

### 5.1 The Complete Lagrangian

**PDTP Original (structure from [advanced_formalization.md](advanced_formalization.md) §3.2).**

```
ℒ_total = ℒ_spacetime + ℒ_SM + ℒ_PDTP_gravity                         ... (5.1)
```

where:

```
ℒ_spacetime = ½(∂_μ φ)(∂^μ φ)                                          ... (5.2)
   [Spacetime condensate phase — kinetic term]

ℒ_SM = −¼G^a_μν G^a_μν − ¼W^a_μν W^a_μν − ¼B_μν B^μν
     + Σ_f ψ̄_f iγ^μ D_μ ψ_f
     + |D_μ H|² − V(H) − y_f ψ̄_L H ψ_R + h.c.                       ... (5.3)
   [Standard Model: gauge fields + fermions + Higgs + Yukawa]

ℒ_PDTP_gravity = Σᵢ gᵢ cos(ψᵢ − φ)                                    ... (5.4)
   [Phase-locking gravitational coupling]
```

### 5.2 What PDTP Adds vs What It Preserves

**Adds:**
- The spacetime condensate phase field φ(x,t) — eq. (5.2)
- The gravitational phase coupling cos(ψᵢ − φ) — eq. (5.4)
- The tensor sector: tetrad e^a_μ in the extended order parameter (Part 12)

**Preserves (entirely unchanged):**
- All SM gauge symmetries: SU(3)_C × SU(2)_L × U(1)_Y
- All 17 SM particles and their quantum numbers
- All SM force laws, coupling constants, and interactions
- The Higgs mechanism for electroweak symmetry breaking
- All SM predictions (anomalous magnetic moments, cross sections, etc.)

**Replaces:**
- GR's geometric gravity with phase-locking gravity
- But: the tensor sector (Part 12) recovers the Einstein equation as a
  limiting case, so GR is the large-scale, weak-field limit of PDTP

---

## 6. Mass Hierarchy — SM Problem, PDTP Perspective

### 6.1 The Mass Hierarchy Problem

**Source:** [Hierarchy problem — Wikipedia](https://en.wikipedia.org/wiki/Hierarchy_problem)

The SM has a severe mass hierarchy:

```
Lightest: ν₁ ≈ 0.001 eV (estimated)
Heaviest: t = 172,570 MeV

Ratio: m_t/m_ν ≈ 10¹⁴
```

Even among charged fermions:

```
m_t/m_e ≈ 172,570/0.511 ≈ 337,710
```

In the SM, this hierarchy comes from Yukawa couplings y_f that span many
orders of magnitude. These couplings are free parameters — the SM provides
no explanation for their values.

### 6.2 PDTP Perspective

**PDTP Original.** In PDTP, the mass hierarchy becomes a **coupling hierarchy**:
the vast range of particle masses maps to a vast range of phase-locking
strengths gᵢ to the spacetime condensate.

```
g_top ≈ 2.6 × 10⁻⁵³ s⁻²     (strongest fermion coupling)
g_ν   < 10⁻⁶⁴ s⁻²            (weakest coupling)

Ratio: g_top/g_ν > 10¹¹
```

**The Koide formula** (Part 4) provides a structural hint: for charged leptons,
the mass hierarchy follows a Z₃ phase harmonic pattern with δ = √2. This
suggests the coupling hierarchy may have a geometric/symmetry origin.

**Does PDTP solve the hierarchy problem?** No. It reframes it:

| SM framing | PDTP framing |
|-----------|-------------|
| Why are Yukawa couplings so different? | Why are phase-locking strengths so different? |
| Why is m_t/m_e ≈ 340,000? | Why is g_t/g_e ≈ 340,000? |
| Free parameters y_f | Free parameters gᵢ |

The hierarchy is traded from one set of unexplained constants to another.
However, PDTP offers a potential path forward: if the condensate microphysics
determines gᵢ through a symmetry-breaking mechanism (see Part 21), the
hierarchy might emerge from the condensate dynamics.

---

## 7. What PDTP Explains That the SM Cannot

### 7.1 Why Gravity Exists

The SM has no explanation for gravity. It simply doesn't include it. GR is a
separate theory that must be grafted on.

**PDTP:** Gravity exists because all matter has de Broglie phases, and the
spacetime vacuum is a phase-coherent condensate. Phase-locking between matter
and spacetime is inevitable when both have oscillatory character. Gravity is
not a separate force — it is the universal synchronization tendency.

### 7.2 Why Gravity Is Universal

In GR, the equivalence principle (all masses fall the same way) is postulated.

**PDTP:** Gravity is universal because ALL matter has a de Broglie phase.
Every particle with mass m has a phase ψ evolving as ψ̇ = mc²/ℏ. This phase
necessarily couples to the condensate φ. There is no "gravitational charge" —
the coupling is to mass-energy itself, which all particles possess.

### 7.3 Why Gravity Is So Weak

The gauge hierarchy problem: why is G so small compared to other coupling
constants?

**PDTP:** Gravity is weak because it is an emergent, collective phenomenon
rather than a fundamental gauge interaction. The gravitational coupling
gᵢ ~ Gm/c² involves Newton's constant G, which in PDTP relates to the
phase stiffness of the condensate:

```
G = 1/(4πκ)    (from oscillator model, see ChatGPT derivation)
```

A very stiff condensate (large κ) means very weak gravity. The condensate
IS very stiff — its excitations propagate at c.

### 7.4 Dark Energy

The SM has no mechanism for cosmic acceleration.

**PDTP:** Dark energy = phase drift of the spacetime condensate at scales
beyond the coherence length ξ. This produces an effective Langevin equation
for the drift (Part 19) with qualitative predictions matching DESI DR2
observations (w₀ > −1, w_a < 0).

### 7.5 Gravitational Wave Breathing Mode

GR predicts exactly 2 tensor polarizations for gravitational waves. The SM
says nothing about GW polarization.

**PDTP:** In addition to the 2 tensor modes (recovered from the tetrad sector,
Part 12), PDTP predicts a third breathing (scalar) mode from the condensate
density oscillation. This mode is massive (suppressed below detection threshold)
but is a genuine new prediction.

**Source:** [hard_problems.md](hard_problems.md) §1

---

## 8. What the SM Explains That PDTP Cannot (Yet)

### 8.1 Specific Particle Masses

The SM, given Yukawa couplings as inputs, predicts exact particle masses. PDTP
has no mass formula — gᵢ ∝ mᵢ is a definition, not a prediction. Computing
particle masses from first principles requires knowing the condensate ground
state and the allowed standing-wave modes.

### 8.2 Running Coupling Constants

The SM predicts how coupling constants change with energy scale (renormalization
group flow). PDTP does not modify this — the RG equations for α, α_s, and the
weak coupling are unchanged.

### 8.3 CKM and PMNS Mixing Matrices

The SM accommodates (but does not predict) the quark and neutrino mixing
matrices. PDTP adds nothing to these — the mixing angles and CP phases remain
free parameters.

### 8.4 Confinement and Hadron Spectrum

QCD explains why quarks are confined and predicts the hadron mass spectrum
(lattice QCD). PDTP does not touch this — the strong force dynamics are
entirely within the SM.

### 8.5 Condensate Microphysics

**The deepest gap.** PDTP cannot derive:
- The condensate density ρ₀
- The phase stiffness κ
- The coupling constants gᵢ from first principles
- Why the condensate exists at all

This is the subject of Part 21 (Energy-Frequency-Vibration approach to
microphysics) and remains the keystone open problem.

---

## 9. Honest Assessment

### 9.1 What This Mapping Achieves

1. **Clarifies PDTP's scope:** PDTP modifies gravity only. The SM is preserved
   intact. This eliminates misconceptions about PDTP "replacing" established
   physics.

2. **Shows structural parallels:** The Higgs condensate ↔ PDTP condensate
   parallel is genuine and suggestive.

3. **Identifies the one change:** cos(ψ − φ) coupling added to L_SM gives
   gravity as phase synchronization.

4. **Demonstrates consistency:** PDTP + SM is a well-defined Lagrangian system
   (eq. 5.1–5.4) that preserves all gauge symmetries.

### 9.2 What This Mapping Does NOT Achieve

1. **No new particle physics predictions.** PDTP does not predict any new
   particle, any new decay channel, or any new cross section.

2. **No mass values derived.** The particle table (§3.6) is interpretive, not
   predictive.

3. **No resolution of SM problems.** The mass hierarchy, strong CP problem,
   and matter-antimatter asymmetry are not addressed.

4. **The coupling constants gᵢ are not independent.** They are defined as
   proportional to mass, which is already known from experiment.

### 9.3 Strategic Assessment (informed by external review)

ChatGPT's strategic review recommended:

> Stop expanding cosmology. Focus exclusively on:
> Microphysics → symmetry breaking → derive κ → derive G.
> That's the keystone. Everything else becomes secondary.

This Part 20 confirms that assessment: the SM mapping is **interpretive, not
generative**. PDTP's real potential lies in its microphysics — if the condensate
ground state can be derived, the coupling constants, G, and potentially Λ all
follow. This is the focus of Part 21.

---

## 10. References

### Established Physics Sources

1. **Standard Model** — [Wikipedia](https://en.wikipedia.org/wiki/Standard_Model)
2. **Quark** — [Wikipedia](https://en.wikipedia.org/wiki/Quark)
3. **Lepton** — [Wikipedia](https://en.wikipedia.org/wiki/Lepton)
4. **Gauge boson** — [Wikipedia](https://en.wikipedia.org/wiki/Gauge_boson)
5. **Higgs boson** — [Wikipedia](https://en.wikipedia.org/wiki/Higgs_boson)
6. **General relativity** — [Wikipedia](https://en.wikipedia.org/wiki/General_relativity)
7. **Electromagnetic field** — [Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_field)
8. **Quantum chromodynamics** — [Wikipedia](https://en.wikipedia.org/wiki/Quantum_chromodynamics)
9. **Electroweak interaction** — [Wikipedia](https://en.wikipedia.org/wiki/Electroweak_interaction)
10. **Higgs mechanism** — [Wikipedia](https://en.wikipedia.org/wiki/Higgs_mechanism)
11. **Mathematical formulation of the Standard Model** — [Wikipedia](https://en.wikipedia.org/wiki/Mathematical_formulation_of_the_Standard_Model)
12. **Quantum electrodynamics** — [Wikipedia](https://en.wikipedia.org/wiki/Quantum_electrodynamics)
13. **Asymptotic freedom** — [Wikipedia](https://en.wikipedia.org/wiki/Asymptotic_freedom)
14. **Weak interaction** — [Wikipedia](https://en.wikipedia.org/wiki/Weak_interaction)
15. **CKM matrix** — [Wikipedia](https://en.wikipedia.org/wiki/Cabibbo%E2%80%93Kobayashi%E2%80%93Maskawa_matrix)
16. **Neutrino oscillation** — [Wikipedia](https://en.wikipedia.org/wiki/Neutrino_oscillation)
17. **Proton** — [Wikipedia](https://en.wikipedia.org/wiki/Proton)
18. **Hierarchy problem** — [Wikipedia](https://en.wikipedia.org/wiki/Hierarchy_problem)
19. **Physics beyond the Standard Model** — [Wikipedia](https://en.wikipedia.org/wiki/Physics_beyond_the_Standard_Model)

### Papers

20. Particle Data Group, R.L. Workman et al. (2024), "Review of Particle
    Physics," Phys. Rev. D 110, 030001.
    [PDG](https://pdg.lbl.gov/)

### PDTP Cross-References

21. [mathematical_formalization.md](mathematical_formalization.md) — Parts 1–2
22. [advanced_formalization.md](advanced_formalization.md) — Part 2, §3 (SM integration)
23. [hard_problems.md](hard_problems.md) — Part 3 (GW polarization, PPN, photon coupling)
24. [koide_derivation.md](koide_derivation.md) — Part 4 (mass hierarchy)
25. [fine_structure_derivation.md](fine_structure_derivation.md) — Part 5 (α)
26. [tetrad_extension.md](tetrad_extension.md) — Part 12 (tensor sector, Einstein recovery)
27. [condensate_microphysics.md](condensate_microphysics.md) — Part 14 (microphysics)
28. [photon_gravity_analysis.md](photon_gravity_analysis.md) — Part 7 (photon coupling)
29. [phase_drift_mechanism.md](phase_drift_mechanism.md) — Part 19 (dark energy)

### PDTP Original Results in This Document

| # | Result | Section |
|---|--------|---------|
| 1 | Phase-locking interpretation of all SM particle categories | §3.1 |
| 2 | Quarks as confined phase modes with QCD binding → gravitational coupling | §3.2 |
| 3 | Lepton mass hierarchy as Z₃ phase harmonics (cross-ref Part 4) | §3.3 |
| 4 | Neutrino oscillations as phase interference in PDTP language | §3.3 |
| 5 | Photon indirect coupling via acoustic metric | §3.4 |
| 6 | Higgs ↔ PDTP condensate structural parallel table | §3.5 |
| 7 | Complete SM particle table with PDTP coupling estimates | §3.6 |
| 8 | Gravity as synchronization vs gauge exchange comparison | §4.1 |
| 9 | Force comparison table (what PDTP changes vs preserves) | §4.5 |
| 10 | Combined Lagrangian L_total = L_spacetime + L_SM + L_PDTP (extended) | §5.1 |
| 11 | Mass hierarchy reframing as coupling hierarchy | §6.2 |
| 12 | Five things PDTP explains that SM cannot | §7 |

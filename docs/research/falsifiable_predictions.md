# PDTP Falsifiable Predictions

## Purpose

This document lists every prediction that PDTP makes which **differs from
standard General Relativity (GR)**. Each prediction includes:

1. What PDTP predicts
2. What GR predicts (for comparison)
3. How to test it
4. What result would **confirm** PDTP
5. What result would **kill** PDTP
6. Current experimental status

A theory that can't be proven wrong isn't science. This is how PDTP can be
proven wrong.

**Conceptual framework — not experimentally validated.**

---

## The Central Claim

**PDTP claims:** Gravity is not the curvature of a smooth spacetime manifold.
Instead, spacetime is a condensate (a wave medium with phase field φ), matter
is a wave (with phase field ψ), and gravity is the phase-locking between them:

```
L_coupling = g cos(ψ − φ)                                      (PDTP Lagrangian)
α = cos(ψ − φ)                                                  (coupling parameter)
```

When α = 1 (phases aligned): normal gravity.
When α = 0 (phases orthogonal): no gravitational interaction.

**Source:** PDTP Lagrangian from mathematical_formalization.md (Part 1).

**GR says:** Spacetime is a smooth manifold with metric g_μν. Matter tells
spacetime how to curve (Einstein equation), curvature tells matter how to
move (geodesic equation). There is no phase, no condensate, no possibility
of "decoupling."

To confirm PDTP over GR, we need to find something PDTP predicts that GR
does not, and observe it. Or find something GR forbids that PDTP allows, and
observe it. Here are the candidates:

---

## Prediction 1: Massive Scalar Breathing Mode

### What PDTP predicts

The spacetime lattice has three wave branches (Part 28):
- Two **transverse** (tensor) modes: massless, propagate at c → these are
  the gravitational waves LIGO detects (h₊ and h×)
- One **longitudinal** (scalar) mode: **massive** — has a frequency gap
  ω_gap from the cos(ψ − φ) coupling

Below ω_gap: the breathing mode is evanescent (exponentially decaying,
doesn't propagate). Above ω_gap: the breathing mode propagates freely.

```
Dispersion relation (breathing mode):

ω² = c²k² + ω²_gap                                            (Eq. F.1)

where ω_gap = √(g/I)  (from Part 21, Eq. 21.4.12)
```

**Source:** Part 28, tensor_gw_lattice.md §5.5; Part 21, efv_microphysics.md §4.

### What GR predicts

GR has **only** two tensor modes (h₊, h×). No scalar breathing mode at
any frequency. Period.

**Source:** [Gravitational wave — Wikipedia](https://en.wikipedia.org/wiki/Gravitational_wave)

### How to test

**Detector requirements:**
- Must be sensitive to **scalar** (breathing) GW polarization — LIGO's
  differential arms are nearly blind to isotropic modes (Part 28b)
- Must operate at frequencies **above** ω_gap

**Suitable experiments:**

| Experiment | Frequency range | Scalar sensitivity | Status |
|-----------|----------------|-------------------|--------|
| LIGO/Virgo/KAGRA network | 10–10⁴ Hz | Partial (null stream method with 3+ detectors) | Running — no scalar signal in O1-O4 |
| LISA (space interferometer) | 10⁻⁴–10⁻¹ Hz | Better (triangular geometry) | Launch ~2035 |
| Einstein Telescope | 2–10⁴ Hz | Better (triangular, underground) | Construction ~2030s |
| Superconducting magnet detectors | 10³–10⁷ Hz | Yes (resonant) | R&D phase |
| Resonant bar detectors | ~10³ Hz | Yes (responds to all modes) | Some operational |

**Source:** [LIGO — Wikipedia](https://en.wikipedia.org/wiki/LIGO);
Isi & Weinstein (2017), [LIGO-P1700276](https://dcc.ligo.org/public/0145/P1700276/005/maxisi_cbcpols.pdf);
[Phys.org — superconducting magnet GW detectors](https://phys.org/news/2025-06-powerful-magnets-high-frequency-gravitational.html)

### What confirms PDTP

Detection of a scalar GW mode that:
- Appears only above a threshold frequency (the gap)
- Has isotropic strain pattern (breathing, not quadrupole)
- Is consistent with the dispersion relation ω² = c²k² + ω²_gap

### What kills PDTP

If high-frequency detectors (well above any reasonable ω_gap) find
**zero** scalar modes with sufficient sensitivity to rule out the PDTP
coupling strength, the massive breathing mode doesn't exist.

**Current status:** LIGO O1-O4 null stream analysis finds no evidence
for scalar or vector GW modes. But LIGO is nearly blind to breathing
modes (geometric suppression), and the gap frequency ω_gap is not yet
determined — it could be above LIGO's band.

**Source:** Abbott et al. (2018), "A Search for Tensor, Vector, and Scalar
Polarizations in the Stochastic Gravitational-Wave Background,"
[arXiv:1802.10194](https://arxiv.org/abs/1802.10194)

### PDTP gap: what we still need

The gap frequency ω_gap = √(g/I) depends on the coupling constant g
and the lattice inertia I — neither is determined from first principles
yet. **Part 29 (substitution chain analysis) aims to fix these constants.**
Without knowing ω_gap, we can't tell experimentalists where to look.

---

## Prediction 2: Gravitational Birefringence

### What PDTP predicts

Different GW polarizations travel at different speeds through the
spacetime lattice:

```
c²_T = μ/ρ                     (transverse/tensor mode speed)
c²_L = (λ + 2μ)/ρ              (longitudinal/breathing mode speed)
```

If λ ≠ 0 (which is generally the case), then c_L ≠ c_T. The spacetime
condensate is **birefringent** for gravitational waves — just as calcite
is birefringent for light.

**Source:** Part 28, tensor_gw_lattice.md §4.7; Part 28b,
polarization_analogy.md §5.3.

### What GR predicts

All gravitational radiation travels at exactly c. GR has no scalar mode,
so there's nothing to have a different speed. No birefringence.

### How to test

**Multi-messenger astronomy:** if a source emits both tensor GWs and
(hypothetical) scalar GWs simultaneously, the arrival time difference is:

```
ΔT = d × |1/c_L − 1/c_T|                                     (Eq. F.2)

where d = distance to source
```

For GW170817 (d ≈ 40 Mpc ≈ 1.3 × 10²⁶ m):

```
ΔT = 1.3 × 10²⁶ × |1/c_L − 1/c_T|                            (Eq. F.3)
```

Even a tiny speed difference (10⁻¹⁵) would give ΔT ~ 0.1 seconds —
detectable.

### What confirms PDTP

Detection of a time delay between different GW polarization modes from
the same astrophysical event.

### What kills PDTP

If tensor and scalar GW modes from the same event arrive simultaneously
(ΔT < detector resolution), then c_L = c_T and the Cauchy relation
holds exactly (λ = 0), which constrains the lattice structure.

**Note:** This test requires first detecting scalar modes (Prediction 1).

### Current status

GW170817 constrains |c_tensor − c_light|/c < 10⁻¹⁵. No scalar mode
detected yet, so birefringence between tensor and scalar not testable yet.

**Source:** Abbott et al. (2017), "Gravitational Waves and Gamma-Rays
from a Binary Neutron Star Merger," *ApJL* 848(2), L13.

---

## Prediction 3: Phase-Dependent Gravitational Coupling

### What PDTP predicts

Gravity depends on the phase relationship between matter and spacetime:
α = cos(ψ − φ). If the matter phase ψ can be controlled (e.g., in a
coherent quantum system like a Bose-Einstein condensate), the
gravitational coupling should vary.

Specifically: a BEC in a definite quantum phase state should have a
**slightly different** gravitational response than thermal (incoherent)
matter of the same mass.

```
Coherent matter (BEC):    all atoms in same phase ψ₀
                          → coupling: α = cos(ψ₀ − φ)
                          → single definite value

Thermal matter:           atoms in random phases ψᵢ
                          → coupling: ⟨α⟩ = ⟨cos(ψᵢ − φ)⟩ = 0
                          ... but wait, this would mean zero gravity!
```

### The subtlety

The naive prediction (thermal matter has zero average coupling) is clearly
wrong — hot objects still fall. This means either:

**(a)** The phase ψ in PDTP is NOT the quantum mechanical phase, but
something else (a deeper, always-locked condensate phase), or

**(b)** The averaging works differently: each atom individually locks to
spacetime (α_i = 1 for each), and the "phase" is always driven to
alignment by the coupling itself (like a compass needle always points
north regardless of where you start it).

**PDTP Original:** Option (b) is more consistent with the framework.
The cos(ψ − φ) coupling acts as a **restoring force** that pulls ψ
toward φ. Individual atoms phase-lock independently. The relevant
question is not "does thermal matter decouple?" (it doesn't) but
"can you prevent phase-locking by actively driving ψ away from φ?"

### What GR predicts

Gravitational coupling depends only on mass-energy (equivalence principle).
The quantum phase of matter is irrelevant to gravity. A BEC and thermal gas
of equal mass fall identically.

**Source:** [Equivalence principle — Wikipedia](https://en.wikipedia.org/wiki/Equivalence_principle)

### How to test

**Atom interferometry with BECs:**

Existing experiments already measure gravitational acceleration of cold atoms
and BECs with extreme precision:

| Experiment | Precision | What it measures |
|-----------|-----------|-----------------|
| Stanford atom interferometer | Δg/g ~ 10⁻⁹ | Free-fall of cesium atoms |
| MICROSCOPE satellite | Δη ~ 10⁻¹⁵ | Equivalence principle violation |
| AION/MAGIS | Planned Δg/g ~ 10⁻¹³ | Atom interferometry over 100m baseline |

**Source:** [Atom-interferometry constraints on dark energy — Science](https://www.science.org/doi/abs/10.1126/science.aaa8883);
[Testing sub-gravitational forces — Nature Physics](https://www.nature.com/articles/nphys4189)

The specific PDTP test: compare gravitational response of:
- Same atoms, same mass, same temperature
- One sample in a coherent BEC state, one in a thermal state
- Look for any difference in free-fall acceleration

### What confirms PDTP

Any measurable difference in gravitational acceleration between coherent
(BEC) and incoherent (thermal) matter of the same species and mass.

### What kills PDTP

If BEC and thermal matter fall identically to the precision of the
experiment, PDTP's phase-coupling picture must be modified. Specifically,
it means the "phase" in α = cos(ψ − φ) cannot be the quantum mechanical
phase of the matter wave.

**Important caveat:** option (b) above (automatic phase-locking) predicts
that both BEC and thermal matter phase-lock independently, giving α ≈ 1
for both. In this case, the test would show **no difference** — which
doesn't kill PDTP, it just confirms automatic locking. This makes
Prediction 3 harder to falsify than Predictions 1 and 2.

### Current status

No experiment has specifically compared BEC vs thermal gravitational
response. Equivalence principle tests (MICROSCOPE) find no violation
at 10⁻¹⁵ level, but these compare different materials, not different
quantum states of the same material.

---

## Prediction 4: Screened Fifth Force from Phase Coupling

### What PDTP predicts

If spacetime is a condensate with phase stiffness κ, there should be a
**scalar force** mediated by the phase field φ — in addition to the
tensor gravitational force from the metric.

This scalar force has a characteristic range determined by the mass of
the breathing mode:

```
Range: λ_scalar = ℏ / (m_breathing × c)                        (Eq. F.4)
       = 2πc / ω_gap

Force: F_scalar ∝ (1/r²) × exp(−r/λ_scalar)                   (Eq. F.5)
```

**Source:** [Fifth force — Wikipedia](https://en.wikipedia.org/wiki/Fifth_force);
Yukawa potential for massive mediator.

At distances r ≪ λ_scalar: the scalar force adds to gravity (effective
G is larger). At distances r ≫ λ_scalar: the scalar force is screened
(exponentially suppressed), and only tensor gravity remains.

### What GR predicts

No fifth force. Gravity is purely tensor (spin-2). Newton's G is the same
at all distances (no distance-dependent correction).

### How to test

**Short-range gravity experiments:**

| Experiment | Range tested | Current limit on extra force |
|-----------|-------------|----------------------------|
| Eöt-Wash torsion balance | > 50 μm | |α_5th| < 10⁻² at 100 μm |
| Casimir force experiments | 0.1–10 μm | Constraints on Yukawa coupling |
| Atom interferometry | Atomic scale | Best constraints on chameleon/symmetron |
| Neutron interferometry | Nuclear scale | Constraints on short-range forces |

**Source:** [Searching for screened scalar forces with atom interferometers](https://arxiv.org/html/2511.09750);
[Testing screened scalar-tensor theories with atomic clocks](https://arxiv.org/html/2410.17292)

### What confirms PDTP

Detection of a distance-dependent deviation from 1/r² gravity at short
range, consistent with a Yukawa profile (exponential cutoff at range
λ_scalar).

### What kills PDTP

If gravity is exactly 1/r² down to arbitrarily short distances (with no
Yukawa correction), the breathing mode either has zero coupling to matter
or infinite mass (no propagation range). This doesn't kill all of PDTP
but severely constrains the scalar sector.

### Current status

No fifth force detected. Current experiments constrain any Yukawa-type
force to be weaker than ~1% of gravity at distances > 50 μm. This is
consistent with PDTP if λ_scalar < 50 μm (which means the breathing
mode mass is > ~4 meV).

---

## Prediction 5: Dark Energy Equation of State w(z)

### What PDTP predicts

Dark energy arises from slow phase drift between matter and spacetime
condensate (Part 25). The equation of state parameter follows the CPL
parametrization:

```
w(z) = w₀ + w_a × z/(1+z)                                     (Eq. F.6)

where:
w₀ = (ε₀ − 1)/(ε₀ + 1)
w_a = −(1 − w₀²)/2 × (m + 3Ω_m)
ε₀ = g_eff(today) / (9H₀²)
```

**Source:** Part 25, dark_energy_phase_drift.md

The self-consistency condition (Part 26) gives m = 6ε ≈ 0.57, predicting:

```
w₀ ≈ −0.92    (with ε₀ ≈ 0.05)
w_a ≈ −0.02
```

And a **consistency line** (falsifiable relation between w₀ and w_a):

```
w_a = −(1 − w₀²)/2 × R        where R = m + 3Ω_m              (Eq. F.7)
```

### What GR + Λ predicts

Cosmological constant: w = −1 exactly, at all redshifts. w_a = 0.

### How to test

**Current and upcoming surveys:**

| Survey | Measures | Status |
|--------|---------|--------|
| DESI (Dark Energy Spectroscopic Instrument) | w₀, w_a from BAO | DR2 released — hints w₀ > −1 |
| Euclid | w(z) from weak lensing + BAO | Operating, first results 2025 |
| Rubin Observatory (LSST) | w(z) from Type Ia supernovae | First light 2025 |
| Roman Space Telescope | w(z) from multiple probes | Launch ~2027 |

### What confirms PDTP

If w₀ > −1 (as DESI DR2 hints) and w_a follows the PDTP consistency line
R = m + 3Ω_m with the predicted m ≈ 0.57.

### What kills PDTP

If w = −1.000 exactly (cosmological constant), with w_a = 0 to high
precision. This would mean dark energy has no dynamics — inconsistent
with PDTP's phase-drift picture.

Also killed if: w < −1 (phantom dark energy). PDTP's canonical scalar
field gives a **hard bound** w ≥ −1.

### Current status

DESI DR2 data show mild preference for w₀ > −1 (about 2-3σ), consistent
with PDTP. Not yet conclusive. More data from DESI, Euclid, and Rubin
will tighten constraints over the next 2-5 years.

---

## Prediction 6: Lattice Spacing at Planck Scale

### What PDTP predicts

If spacetime is a lattice with spacing a, then:
- Below the Planck length (a ~ ℓ_P ≈ 1.6 × 10⁻³⁵ m), the concept of
  "continuous space" breaks down
- There should be a maximum energy for gravitons/GWs (the lattice cutoff):
  E_max = ℏc/a ~ E_Planck ≈ 1.2 × 10¹⁹ GeV

```
Maximum GW frequency: f_max = c/a ~ c/ℓ_P ≈ 1.9 × 10⁴³ Hz    (Eq. F.8)
```

More practically: the GW dispersion relation should deviate from ω = ck
at very high frequencies (near the lattice cutoff), showing the sinusoidal
dispersion of a lattice:

```
ω = (2c/a) sin(ka/2)                                           (Eq. F.9)
```

instead of the linear ω = ck expected from GR.

**Source:** [Dispersion relation — Wikipedia](https://en.wikipedia.org/wiki/Dispersion_relation)
(lattice dispersion); Part 28, tensor_gw_lattice.md §6.1.

### What GR predicts

Spacetime is continuous down to arbitrarily small scales. No lattice
cutoff, no modified dispersion relation.

### How to test

**Gamma-ray burst dispersion:** if photons (or gravitons) at different
energies travel at slightly different speeds due to lattice dispersion,
high-energy photons from distant gamma-ray bursts should arrive at
slightly different times than low-energy photons.

**Source:** Fermi-LAT observations of GRB 090510 already constrain
Planck-scale dispersion: |ΔE/E| × (E/E_Planck) < 1 for first-order
corrections.

### What confirms PDTP

Energy-dependent arrival times consistent with lattice dispersion
relation ω = (2c/a)sin(ka/2).

### What kills PDTP

If spacetime is provably continuous below the Planck scale (no energy-
dependent dispersion seen to arbitrary precision). However, the lattice
spacing could be smaller than ℓ_P, pushing the signal below current
sensitivity.

### Current status

No Planck-scale dispersion detected. Current constraints are consistent
with a lattice spacing a ≤ ℓ_P but don't rule it out.

---

## Summary: Predictions Ranked by Testability

| # | Prediction | Differs from GR? | Testable now? | Strongest test |
|---|-----------|-------------------|---------------|---------------|
| 5 | w(z) ≠ −1 (dark energy dynamics) | Yes | **Yes** | DESI, Euclid, Rubin (2025-2030) |
| 4 | Screened fifth force | Yes | **Yes** | Atom interferometry, torsion balances |
| 1 | Massive breathing mode GW | Yes | **Partially** | LIGO null stream; future: ET, LISA |
| 3 | Phase-dependent gravity (BEC test) | Yes | **In principle** | BEC vs thermal free-fall comparison |
| 2 | GW birefringence | Yes | **Not yet** | Requires scalar mode detection first |
| 6 | Planck-scale dispersion | Yes | **Barely** | Gamma-ray burst timing |

### The critical path

The most important near-term result for PDTP:

```
1. DESI/Euclid confirm w₀ > −1          → PDTP's dark energy picture survives
2. Determine ω_gap from Part 29          → tells experimentalists WHERE to look
3. High-frequency GW detector finds      → smoking gun for condensate spacetime
   scalar breathing mode above ω_gap
```

If all three happen, PDTP goes from "speculative framework" to "viable
candidate theory." If any of the "kills PDTP" results occur instead,
specific parts of the framework must be abandoned or revised.

---

## What PDTP Still Needs to Calculate

Before experimentalists can fully test these predictions, PDTP must
provide **specific numbers:**

| Quantity | Symbol | Needed for | Status |
|---------|--------|-----------|--------|
| Breathing mode mass | m_b = ℏω_gap/c² | Predictions 1, 2, 4 | Unknown — depends on coupling g and lattice inertia I |
| Lattice coupling constant | K | All predictions | Part 29 (substitution chains) aims to determine this |
| Phase stiffness | κ = c²/(4πG) | Known: ≈ 1.07 × 10²⁶ Pa | Determined |
| Scalar-tensor coupling | g_scalar/g_tensor | Prediction 4 (fifth force range) | Not yet determined |
| Dark energy parameters | w₀, w_a | Prediction 5 | Depends on ε₀ (currently free parameter) |

**The single most important calculation is Part 29:** deriving the lattice
constant K from known physics. Once K is known, ω_gap, m_b, and
λ_scalar all follow — and every prediction gets a specific number.

---

*This document will be updated as new calculations are completed and
new experimental results become available.*

**Conceptual framework — not experimentally validated.**

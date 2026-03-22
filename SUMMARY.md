# PDTP Framework Summary

*Phase-Decoupled Transport Physics — Status as of Parts 1-76*

---

## What Is Gravity?

**Gravity is phase-locking.**

Everything vibrates. Matter is a standing wave with a phase ψ. Spacetime itself
has a phase field φ. These two phases want to synchronize — exactly like pendulum
clocks on the same wall, or fireflies blinking in unison.

The coupling energy is V = +g cos(ψ − φ). When ψ = φ (phases aligned), energy
is minimized. That falling-into-alignment **is** gravity.

---

## Three Lagrangians

PDTP has been developed through three levels of symmetry:

### U(1) — Gravitational Condensate (Parts 1-32)

```
L = ½(∂μφ)(∂^μφ) + Σᵢ ½(∂μψᵢ)(∂^μψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)
```

The single-phase model. φ is a real scalar (one angle). Recovers Newtonian gravity,
PPN parameters (γ=β=1), Hawking temperature, GW propagation at c.

### Two-Phase — Gravity + Surface Tension (Parts 61-63)

```
L = +g cos(ψ − φ_b) − g cos(ψ − φ_s)
```

φ_b = bulk phase (+cos, gravity); φ_s = surface phase (−cos, surface tension).
Product coupling: 2g sin(ψ−φ_+) sin(φ_-). Derives Newton's 3rd law exactly
(ψ̈ = −2φ̈_+), Jeans instability, biharmonic gravity, and a reversed Higgs
mechanism (φ_- massless in vacuum, massive near matter). **16/16 re-derivation
tests PASS** — all single-phase results reproduced.

### SU(3) — QCD Condensate (Parts 37-41, 75-76)

```
L = K Tr[(∂μU†)(∂^μU)] + Σᵢ Kᵢ Tr[(∂μΨᵢ†)(∂^μΨᵢ)] + Σᵢ gᵢ Re[Tr(Ψᵢ†U)] / 3
```

U(x) ∈ SU(3) — spacetime condensate field. Produces 8 gluons (N²−1), Z₃ vortices
(quarks), and an emergent metric g_μν = Tr(∂U†∂U) with exactly 2 transverse-traceless
gravitational wave polarizations — matching GR.

---

## What Has Been Achieved (76 Parts)

### GR Recovery (Parts 72-76) — The Central Achievement

The SU(3) emergent metric g_μν = Tr(∂U†∂U) is **NOT pure gauge** (rank 4, vs rank ≤ 2
for gauge artifacts). It produces:

- **2 TT tensor modes** (+ and × GW polarizations) — matching GR
- **Auto-Lorenz gauge** d^μh = (1/2)d_νh — DERIVED, not imposed (unique to PDTP)
- **Fierz-Pauli structure** — the unique ghost-free massless spin-2 action
- **Isaacson stress-energy** — GW modes carry energy (not gauge artifacts)
- **Bianchi identity** — conservation laws automatic (3 independent proofs)
- **Einstein equation** — via Sakharov 1-loop induced gravity

Status: Einstein equation structure PASS; coefficient has N_eff gap (G_ind = 2.36×G
with 8 gluon fields; need N_eff = 6π ≈ 18.85 for exact match). This is a shared
limitation with ALL induced gravity approaches.

### QCD (Parts 37-41)

- String tension σ = 0.173 GeV² — **4% off QCD's 0.18** (from first principles)
- κ_GL = √2 (Type II superconductor) — Abrikosov flux tubes = confinement
- Wilson action Monte Carlo verified in 2D and 4D

### Particle Physics (Parts 20-53)

- Koide formula Q = 2/3 from Z₃ geometry; δ = √2 from equal partition
- Chirality = Z₂ vortex winding; maximal parity violation automatic
- 3 generations = 3 radial vortex modes (n_r = 0, 1, 2)
- Ξ_cc⁺ baryon mass: 3621 MeV (0.02% off LHCb measurement)

### Black Holes (Parts 45-47)

- Singularity replaced by vortex core (ξ = l_P/√2)
- Information protected by topology (winding number W)
- Complete evaporation; no remnant

---

## What Has NOT Been Achieved (Honest Limitations)

| Problem | Status | Parts |
|---------|--------|-------|
| m_cond (= m_P) not derived | FREE PARAMETER (like Λ in GR) | 29-35 |
| α_EM = 1/137 not derived | Free parameter (structure yes, value no) | 52 |
| N_eff = 6π not identified | Coefficient gap in Sakharov formula | 75b, 76a |
| Strong-field metrics | 2-DOF deficit (8 fields < 10 metric components) | 76e |
| Full nonlinear Einstein eq | Sakharov gives 1-loop only; beyond is open | 76g |
| Hubble tension | Both mechanisms ~9 orders too small | 16 |
| CP violation | Lagrangian is C,P,T invariant; gap for baryogenesis | 22 |

---

## Falsifiable Predictions (12 ranked)

1. w(z) ≠ −1 — testable now with DESI/Euclid (hints at 2-3σ)
2. Screened fifth force — atom interferometry, torsion balances
3. QCD string tension from K_NAT = 1/(4π) — lattice comparison
4. Hollow shell test: φ_- massive inside — distinguishes from chameleon
5. Massive breathing mode GW — LIGO null stream; ET, LISA
6. Phase-dependent gravity — BEC interferometry
7-12. See [falsifiable_predictions.md](docs/research/falsifiable_predictions.md)

---

## Free Parameters

| Parameter | Controls | Status |
|-----------|----------|--------|
| m_cond (= m_P) | G = ℏc/m_cond² | Free — all perturbative paths exhausted |
| Λ | Cosmological constant | Free — second parameter alongside G |
| α_EM | EM coupling | Free — structure derived, value not |
| sin²θ_W | Weak mixing angle | Free — ratio of condensate stiffnesses |
| v_EW = 246 GeV | EW condensate scale | Free — 3rd condensate mass |
| θ₀ = 2/9 | Koide angular parameter | Free — no SU(3) derivation |

The Standard Model also cannot derive these values. PDTP explains their *structure*
(why they exist, what form they take) but not their *values*.

---

## One Sentence

Gravity is not a force pulling objects together — it is the tendency of
matter-waves and spacetime-waves to synchronize their phases, and the
Einstein equation emerges from this synchronization via the SU(3) condensate.

---

For the full framework: [Introduction](INTRODUCTION.md)
For mathematical foundations: [Mathematical Formalization](docs/research/mathematical_formalization.md)
For complete findings: [Findings Summary](docs/overview/pdtp_findings_summary.md)
For all equations: [Equation Reference](docs/research/equation_reference.md)
For the active roadmap: [TODO_02.md](TODO_02.md)

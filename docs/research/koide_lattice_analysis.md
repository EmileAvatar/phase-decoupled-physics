# Part 32: Koide-Lattice Analysis

**PDTP Research Document — Part 32: Bottom-Up Derivation of K and G**

Attempt to derive the PDTP lattice spring constant K and gravitational constant G
using only particle masses (Koide/Brannen parameterization) — no G as input.

**Status:** Analysis complete. The Koide formula alone cannot break the circularity.
Results confirm the hierarchy problem from a new angle. Clear path forward identified.

**Simulation:** [koide_lattice_analysis.py](../../simulations/koide_lattice_analysis.py)
**Output:** [koide_lattice_output.md](../../simulations/koide_lattice_output.md)

---

## Table of Contents

1. [Motivation: The Maxwell Analogy](#1-motivation-the-maxwell-analogy)
2. [The Koide Formula as a Lattice Constraint](#2-the-koide-formula-as-a-lattice-constraint)
3. [Brannen Parameterization](#3-brannen-parameterization)
4. [The 3×3 Circulant Mass Matrix](#4-the-3x3-circulant-mass-matrix)
5. [Systematic Maxwell-Term Search](#5-systematic-maxwell-term-search)
6. [Hierarchy Wall Analysis](#6-hierarchy-wall-analysis)
7. [Quark Sector Analysis](#7-quark-sector-analysis)
8. [The Missing Maxwell Term](#8-the-missing-maxwell-term)
9. [Summary and Scorecard](#9-summary-and-scorecard)
10. [Conclusions](#10-conclusions)

[References](#references)

---

## 1. Motivation: The Maxwell Analogy

### 1.1 The Idea

In 1861, Maxwell added a single term — the displacement current ∂E/∂t — to Ampère's
law to make it consistent with charge conservation. As a by-product of that one
consistency requirement, he obtained:

```
  c = 1 / sqrt(epsilon_0 * mu_0)
```

for free, from purely electromagnetic measurements. No optical measurements needed.

**The PDTP question (Part 32):** Can we do the same for gravity?

Specifically: particle masses are known to extraordinary precision. If PDTP is correct
and particles are emergent phase waves in the spacetime condensate, then the mass
spectrum should encode the lattice parameters K (spring constant) and a (spacing).
Feeding those back in should give G without using G as input.

### 1.2 The Strategy

**Bottom-up:** treat measured particle masses as the OUTPUT of the lattice, not the input.
Then reverse-engineer the lattice.

The PDTP G formula (from Part 29, G-free formulation):

```
  K = hbar / (4*pi*c)              [G-free spring constant, units: kg*m]
  G = c^2 a^2 / (4*pi*K) = c^3 a^2 / hbar
```

**Source:** [simulations/substitution_chains.py](../../simulations/substitution_chains.py)

So everything hinges on: **what is the lattice spacing a?**

The Koide/Brannen parameterization of lepton masses extracts a mass scale M₀ = μ²
from the mass spectrum. The Compton wavelength of M₀ gives a candidate length:

```
  a_candidate = hbar / (M_0 * c)
```

We test this and eight other candidates systematically.

---

## 2. The Koide Formula as a Lattice Constraint

### 2.1 The Formula

**Source:** Y. Koide, *Lett. Nuovo Cimento* **34**, 201 (1982)

```
           m_e + m_mu + m_tau
  Q  =  ─────────────────────────  =  2/3
         (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2
```

Verified numerically (PDG 2024 masses):

| Quantity | Value |
|----------|-------|
| Q measured | 0.66666051 |
| 2/3 exact  | 0.66666667 |
| \|Q − 2/3\| | 6.2 × 10⁻⁶ |

The relation holds to 1 part in 10⁵ despite masses spanning a factor of 3,477.

### 2.2 The Scale-Invariance Problem

The Koide formula is **dimensionless and scale-invariant**. Multiplying all three masses
by any constant λ leaves Q unchanged:

```
  Q(lambda*m_e, lambda*m_mu, lambda*m_tau) = Q(m_e, m_mu, m_tau)
```

**Consequence:** The Koide formula constrains mass RATIOS, not absolute masses.
It cannot determine M₀ = μ² independently — μ is fixed only after one mass is measured.
There is no way to extract a length scale 'a' from Q alone.

---

## 3. Brannen Parameterization

**Source:** C.A. Brannen, "The Lepton Masses" (2006)

### 3.1 The Ansatz

```
  sqrt(m_i) = mu * (1 + delta * cos(theta_0 + 2*pi*i/3))    for i = 0, 1, 2
```

where:
- μ > 0 is the overall scale (MeV^{1/2})
- δ = √2 exactly (Koide condition: Q = 2/3 iff δ = √2)
- θ₀ ≈ 2/9 radians is the phase offset (Brannen convention: i=0 is the heaviest)

**Source:** See full derivation in [koide_derivation.md](koide_derivation.md) §§2–3.

### 3.2 Fitted Parameters (Charged Leptons)

| Parameter | Value | Notes |
|-----------|-------|-------|
| μ | 17.7156 MeV^{1/2} | Overall amplitude scale |
| M₀ = μ² | **313.84 MeV** | Koide base mass scale |
| δ | 1.41420 | cf. √2 = 1.41421 ✓ |
| θ₀ | 0.22223 rad | cf. 2/9 = 0.22222 rad ✓ |

### 3.3 Fit Quality

| Lepton | √m measured | √m predicted | Error |
|--------|------------|--------------|-------|
| τ (i=0) | 42.1528 MeV^{1/2} | 42.1530 MeV^{1/2} | 0.0005% |
| e (i=1) | 0.7148 MeV^{1/2} | 0.7147 MeV^{1/2} | 0.022% |
| μ (i=2) | 10.2790 MeV^{1/2} | 10.2790 MeV^{1/2} | 0.0007% |

Excellent fit across four orders of magnitude.

### 3.4 The Koide Base Mass M₀ = 313.84 MeV

This scale is notable:

```
  M_0 = mu^2 = 313.84 MeV

  Compare:
    m_proton / 3  = 938.27 / 3 = 312.76 MeV   (constituent quark mass!)
    Ratio: M_0 / (m_p/3) = 1.003   (less than 0.3% difference)
```

**PDTP Original observation:** The Koide base mass M₀ coincides with the
constituent quark mass (≈ m_proton/3) to within 0.3%. Whether this is a
coincidence or a hint of lepton-quark unification via a common lattice mode
requires further investigation.

---

## 4. The 3×3 Circulant Mass Matrix

### 4.1 The Tight-Binding Picture

**PDTP Original**

The Brannen ansatz is identical to the eigenspectrum of a 3-site ring lattice
(tight-binding model). Define the mass-amplitude matrix:

```
  M_circ = mu * I + (mu/sqrt(2)) * C
```

where C is the adjacency matrix of a triangular ring (all-to-all coupling):

```
        ⎛ 0  1  1 ⎞
  C  =  ⎜ 1  0  1 ⎟       (3-site ring)
        ⎝ 1  1  0 ⎠
```

Eigenvalues of C: {2, −1, −1}

Eigenvalues of M_circ (θ₀ = 0, symmetric):
```
  lambda_0 = mu * (1 + sqrt(2)) = 42.77 MeV^{1/2}   (tau-like)
  lambda_1 = mu * (1 - 1/sqrt(2)) = 5.19 MeV^{1/2}  (degenerate)
  lambda_2 = 5.19 MeV^{1/2}                          (degenerate)
```

With θ₀ = 2/9 (the Hermitian circulant, complex off-diagonals):
the degeneracy breaks and the three eigenvalues reproduce exactly the
measured lepton masses.

### 4.2 Lattice Interpretation of Matrix Elements

| Element | Value | PDTP interpretation |
|---------|-------|---------------------|
| Diagonal μ | 17.7156 MeV^{1/2} | Onsite amplitude (shared generation mode) |
| Off-diagonal t = μ/√2 | 12.527 MeV^{1/2} | Inter-generation hopping amplitude |
| M₀ = μ² | 313.84 MeV | Shared generation mass scale |
| t² = μ²/2 = M₀/2 | 156.92 MeV | Hopping energy (inter-generation coupling) |

### 4.3 Connection to PDTP Spring Constant

In a standard 1D harmonic lattice with spring constant K_spring [N/m] and
mass per site m₀, the wave speed is c² = K_spring a² / m₀.

In the circulant mass matrix, the off-diagonal element t² = M₀/2 plays the
role of the hopping energy. Interpreting t² as an energy scale and using the
Compton wavelength:

```
  a_hop = hbar / (t^2 * c / c^2) = hbar c / (t^2 c^2) = hbar / (M_hop * c)
        = 1.257e-15 m   (about 1.3 fm, nuclear scale)
```

This gives (from PDTP G formula):
```
  G_pred(a_hop) = c^3 a_hop^2 / hbar = 4.04e+29 m^3/(kg*s^2)
  G_pred / G_known = 6.05e+39
```

**Result:** 39 orders of magnitude off. FAIL.

The structural lesson: the mass matrix encodes generation STRUCTURE beautifully,
but connecting its energy scale to the lattice spacing a requires the hierarchy
ratio between particle masses and the Planck scale — which is exactly what we
are trying to derive.

---

## 5. Systematic Maxwell-Term Search

We test 10 candidates for the lattice spacing a using:
```
  G_pred = c^3 * a^2 / hbar
```

| # | Candidate | a (m) | G_pred | Ratio | Score |
|---|-----------|-------|--------|-------|-------|
| 0 | a = l_Planck (CIRCULAR — control) | 1.62e−35 | 6.67e−11 | 1.00 | **PASS** |
| 1 | a = λ_C(electron) | 3.86e−13 | 3.81e+34 | 5.71e+44 | FAIL |
| 2 | a = r_e = α × λ_C(e) | 2.82e−15 | 2.03e+30 | 3.04e+40 | FAIL |
| 3 | a = λ_C(M₀) — Koide base mass | 6.29e−16 | 1.01e+29 | 1.51e+39 | FAIL |
| 4 | a = λ_C(M_geom) — geometric mean | 4.31e−15 | 4.75e+30 | 7.11e+40 | FAIL |
| 5 | a = λ_C(M_hop) — circulant hopping | 1.26e−15 | 4.04e+29 | 6.05e+39 | FAIL |
| 6 | a = λ_C(proton) | 2.10e−16 | 1.13e+28 | 1.69e+38 | FAIL |
| 7 | a = α × λ_C(M₀) — EM-scaled Koide | 4.59e−18 | 5.38e+24 | 8.06e+34 | FAIL |
| 8 | a = λ_C(m_e/θ₀²) — phase-angle scale | 1.91e−14 | 9.29e+31 | 1.39e+42 | FAIL |
| 9 | a = λ_C(m_Planck) (same as #0, circular) | 1.62e−35 | 6.67e−11 | 1.00 | **PASS** |

**SUDOKU SCORECARD: 2 PASS, 8 FAIL — both passes are circular (use G).**

---

## 6. Hierarchy Wall Analysis

Every candidate can be written as:

```
  G_pred / G_known  =  (m_Pl / m_x)^N
```

| Candidate | G_pred/G_known | N (m_Pl/m_e)^N | Physical meaning |
|-----------|---------------|----------------|------------------|
| 0 (control) | 1.00 | 0 | Trivially circular |
| 1 (electron Compton) | 5.71 × 10⁴⁴ | **N = 2.00** | (m_Pl/m_e)² exactly |
| 2 (classical e radius) | 3.04 × 10⁴⁰ | N = 1.81 | α² × (m_Pl/m_e)² |
| 3 (Koide base M₀) | 1.51 × 10³⁹ | N = 1.75 | (m_Pl/M₀)² |
| 4 (geometric mean) | 7.11 × 10⁴⁰ | N = 1.83 | (m_Pl/M_geom)² |
| 5 (hopping M₀/2) | 6.05 × 10³⁹ | N = 1.78 | (m_Pl/(M₀/2))² |
| 6 (proton) | 1.69 × 10³⁸ | N = 1.71 | (m_Pl/m_p)² |
| 7 (α × Koide) | 8.06 × 10³⁴ | N = 1.56 | α² × (m_Pl/M₀)² |
| 8 (phase angle) | 1.39 × 10⁴² | N = 1.88 | (m_Pl/(m_e/θ₀²))² |

**Key observation:**

Candidate 1 (electron Compton wavelength) gives N = **exactly 2.00** — this is
the hierarchy problem stated with perfect clarity:

```
  G_pred(a = lambda_C(e)) / G_known = (m_Pl / m_e)^2 = 5.71e44
```

The electron's gravitational self-coupling is:

```
  alpha_G(e) = G m_e^2 / (hbar c) = (m_e / m_Pl)^2 = 1.75e-45
```

So using a = λ_C(e) gives G_pred = (m_Pl/m_e)² × G_known — exactly the inverse
of the gravitational hierarchy. The particle physics gives a lattice spacing that is
(m_Pl/m_e) = 2.39 × 10²² times too large, requiring G to be 5.71 × 10⁴⁴ times
too strong.

Every other candidate also has this form, with different particle masses or
dimensionless combinations. The Koide formula shifts the mass scale from m_e to
M₀ ≈ 614 m_e, reducing the exponent from 2.00 to 1.75 — but cannot close the gap.

---

## 7. Quark Sector Analysis

Applying the same Brannen analysis to quark triplets:

| Triplet | Q | δ (implied) | M₀ (MeV) | M₀ / M₀(leptons) |
|---------|---|-------------|----------|------------------|
| (e, μ, τ) charged leptons | **0.6667** | **√2 = 1.414** | **313.84** | 1.00 |
| (c, b, t) heavy quarks | 0.6694 | 1.420 | 29,550 | 94.2 |
| (d, s, b) down-type | 0.7312 | 1.545 | 650 | 2.07 |
| (u, c, t) up-type | 0.8489 | 1.759 | 22,753 | 72.5 |

**Key finding:** Each quark triplet gives a *different* M₀, and none matches the
lepton M₀ exactly. The Koide relation (Q = 2/3) is exact only for charged leptons.

Interpretations:

1. **QCD corrections:** Quark masses run strongly with energy scale (asymptotic
   freedom). The Koide relation may be exact at a high unification scale but
   distorted at low energies by QCD radiative corrections.

2. **Different lattice sectors:** Quarks and leptons may occupy different phase
   sectors of the condensate with different lattice parameters a_quark ≠ a_lepton.
   This would explain why the lepton Koide relation is exact but the quark relations
   are approximate.

3. **Waterfall structure:** The near-Koide (c, b, t) tuple (Q = 0.669) and
   signed (s, c, b) tuple suggest an overlapping generational ladder rather than
   clean independent triplets.

---

## 8. The Missing Maxwell Term

### 8.1 What Would Be Needed

Maxwell's displacement current was derived by requiring Ampère's law to be
consistent with the continuity equation ∂ρ/∂t + ∇·J = 0 — a *different*
physical principle, independent of Faraday's law. The displacement current
term then gave c = 1/√(ε₀μ₀) for free.

The PDTP analogue would require: *a physical equation, independent of G,
that fixes the ratio M₀/m_Planck*.

The required lattice spacing is:
```
  a_required = l_Planck = 1.616e-35 m
  Mass that gives this Compton wavelength: m_* = hbar/(l_Pl * c) = m_Planck
  Ratio: m_Planck / M_0 = 3.89e19   (19 orders of magnitude)
```

The Koide formula cannot generate this ratio because it is dimensionless.

### 8.2 Viable Paths to the Maxwell Term

Three concrete options remain:

**Option A: Breathing mode detection (Strategy A, Part 29)**

```
  Measure omega_gap (breathing mode frequency of spacetime)
  -> a = pi*c / omega_gap
  -> G = c^3 a^2 / hbar  (G as output, not input)
```

This IS the Maxwell-term analog: an independent measurement (gravitational
wave interferometry at high frequency) feeds into the lattice structure and
gives G as a derived quantity. The LIGO/ET/LISA path at ultra-high frequencies.

**Option B: Hierarchy ratio from lattice topology (Strategy B, Part 29)**

```
  R = alpha_G / alpha_EM = G m_e^2 / (e^2/(4*pi*eps_0)) ~ 10^-37
```

If R can be derived from the lattice topology (how many dimensions, what
symmetry group, what filling fraction), then G = R × e²/(4πε₀ m_e²).
This requires a first-principles lattice theory, not just the mass spectrum.

**Option C: Dvali species counting**

```
  G = hbar*c / (N_s * Lambda_s^2)
```

If the PDTP lattice has N_s ~ 10³² modes per Planck volume (Dvali's number),
gravity is weak because spacetime has many degrees of freedom. This is an
entirely different direction: not from the particle mass spectrum but from
counting the spacetime lattice's degrees of freedom.

### 8.3 What the Koide Analysis Rules Out

Part 32 establishes rigorously that **the mass spectrum of the Standard Model
cannot by itself break the circularity in G**. More precisely:

- The Koide formula encodes Z₃ symmetry and mass RATIOS only
- No combination of lepton (or quark) masses, α_EM, θ₀, or integer exponents
  generates the Planck scale without G as input
- The exponent N in G_pred/G_known = (m_Pl/m_x)^N ranges from 1.56 to 2.00
  depending on the mass scale used — always less than or equal to 2
- N = 2 exactly (candidate 1) is the purest statement of the hierarchy problem

---

## 9. Summary and Scorecard

### 9.1 Numerical Results

| Scale | Value |
|-------|-------|
| Koide ratio Q | 0.66666051 (exact = 2/3 to 10⁻⁵) |
| Brannen μ | 17.7156 MeV^{1/2} |
| Koide base mass M₀ = μ² | **313.84 MeV** |
| M₀ vs proton/3 | 313.84 vs 312.76 MeV (0.3% match) |
| Required a for G_known | 1.616 × 10⁻³⁵ m (Planck length) |
| Best candidate a (Koide) | 6.29 × 10⁻¹⁶ m (nuclear scale) |
| Gap: a_required / a_Koide | 3.89 × 10¹⁹ (Planck/M₀ ratio) |

### 9.2 Sudoku Scorecard

| Test | Result | Notes |
|------|--------|-------|
| Koide Q = 2/3 for leptons | **PASS** (6.2×10⁻⁶ error) | |
| Brannen δ = √2 | **PASS** (error < 10⁻⁵) | |
| θ₀ = 2/9 | **PASS** (error 7.4×10⁻⁶) | |
| G_pred from electron Compton | FAIL (off by 10⁴⁴·⁷) | |
| G_pred from Koide base M₀ | FAIL (off by 10³⁹·²) | |
| G_pred from geometric mean | FAIL (off by 10⁴⁰·⁸) | |
| G_pred from hopping term | FAIL (off by 10³⁹·⁸) | |
| G_pred from classical e radius | FAIL (off by 10⁴⁰·⁵) | |
| G_pred from proton Compton | FAIL (off by 10³⁸·²) | |
| G_pred from EM-scaled Koide | FAIL (off by 10³⁴·⁹) | |
| G_pred from phase-angle scale | FAIL (off by 10⁴²·¹) | |
| **Overall for G derivation** | **0/8 PASS** (2 passes are circular) | |

### 9.3 PDTP Original Results

| Result | Type | Status |
|--------|------|--------|
| M₀ = 313.84 MeV ≈ m_p/3 (constituent quark mass) | PDTP Observation | Suggestive coincidence |
| Circulant 3×3 mass matrix reproduces Brannen eigenspectrum | PDTP Original | Exact (mathematical) |
| Hopping energy t² = M₀/2 ~ meson scale | PDTP Original | Numerically interesting |
| All G_pred = (m_Pl/m_x)^N × G_known with N ≤ 2 | PDTP Original | **Key result** |
| N = 2.00 for electron Compton = hierarchy problem in purest form | PDTP Original | **Key result** |
| Koide formula is STRUCTURE theorem, not SCALE theorem | PDTP Original | **Key result** |

---

## 10. Conclusions

### 10.1 What the Analysis Shows

**1. The Koide formula is exact and well-described by the Brannen parameterization.**
The three charged leptons satisfy Q = 2/3 to 6 × 10⁻⁶, and the circulant
mass matrix picture gives a clean lattice interpretation.

**2. The Koide base mass M₀ = 313.84 MeV coincides with the constituent quark mass
(m_proton/3 = 312.76 MeV) to within 0.3%.** This is a non-trivial coincidence
that may hint at a connection between lepton and quark sectors through a
shared lattice mode.

**3. The Koide formula cannot break the circularity in G.**
It encodes mass RATIOS (a structure theorem) but not the absolute mass scale.
No candidate lattice spacing derived from particle masses reproduces G_known.

**4. The hierarchy wall sits at exactly N = 2 for the electron.**
Using a = λ_C(e) gives G_pred/G_known = (m_Pl/m_e)² = 5.71 × 10⁴⁴.
This is the hierarchy problem stated with maximum clarity.
The Koide formula shifts the exponent slightly (N ≈ 1.75 for M₀) but
cannot close the 22-orders-of-magnitude gap.

**5. The "Maxwell term" for gravity requires an independent measurement
that directly accesses the Planck scale.** Three concrete options:
- Breathing mode detection (omega_gap → a → G)
- Hierarchy ratio R from lattice topology
- Dvali species counting (N_s → G)

### 10.2 What This Changes

- **The bottom-up strategy is valid in principle** — particles as emergent lattice
  modes is a coherent framework. The failure is not conceptual but computational:
  we lack the Maxwell-term analog.

- **M₀ ≈ m_p/3 is worth tracking.** If this is not a coincidence, it suggests
  the lepton mass scale is set by QCD confinement, which would connect
  electroweak symmetry breaking to the lattice through a different channel.

- **The quark sector requires separate treatment.** QCD corrections likely
  distort quark masses from their "bare" Koide values. Evaluating quark masses
  at a common high-energy scale (lattice QCD) might reveal a cleaner Koide
  structure.

### 10.3 What Remains Open

| Question | Status |
|----------|--------|
| Derive θ₀ = 2/9 from lattice geometry | Open — purely empirical |
| Is M₀ ≈ m_p/3 a lattice coincidence or constraint? | Open — needs QCD connection |
| Quark Koide at high energy scale | Open — needs lattice QCD |
| Breathing mode frequency (omega_gap) | Open — requires future experiments |
| Hierarchy ratio R from topology | Open — requires lattice first-principles |

**Next steps:** Strategy A (breathing mode → omega_gap → a → G) remains the
clearest path. Strategy B (hierarchy ratio R from lattice topology) remains
the most theoretically appealing.

---

## References

| # | Citation | Used In |
|---|----------|---------|
| 1 | Y. Koide, "A Fermion-Boson Composite Model of Quarks and Leptons," *Lett. Nuovo Cimento* **34**, 201 (1982) | §2.1 |
| 2 | [Koide formula — Wikipedia](https://en.wikipedia.org/wiki/Koide_formula) | §2.1 |
| 3 | [Particle Data Group (2024)](https://pdg.lbl.gov/) | §2.1, §3.2 |
| 4 | C.A. Brannen, "The Lepton Masses" (2006), [brannenworks.com/MASSES2.pdf](https://brannenworks.com/MASSES2.pdf) | §3 |
| 5 | W. Rodejohann & H. Zhang, "Extended Empirical Fermion Mass Relation," [arXiv:1101.5525](https://arxiv.org/abs/1101.5525) (2011) | §7 |
| 6 | A. Rivero, "A new Koide tuple: strange-charm-bottom," [arXiv:1111.7232](https://arxiv.org/abs/1111.7232) (2011) | §7 |
| 7 | PDTP Part 29: Substitution chain analysis — circularity proven | §5 |
| 8 | PDTP Part 30: External G derivations — Sakharov, string, Dvali | §8 |
| 9 | G. Dvali, "Black Holes and Large N Species Solution to the Hierarchy Problem," [arXiv:0706.1075](https://arxiv.org/abs/0706.1075) (2007) | §8.2 |
| 10 | [docs/research/koide_derivation.md](koide_derivation.md) — Z₃ phase derivation of Koide formula | §4 |

---

End of Document

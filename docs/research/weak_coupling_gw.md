# Weak Coupling Strength g_W — Part 48

**Status:** NEGATIVE RESULT — g_W has two independent free parameters in PDTP;
formally declared underdetermined (analogous to m_cond in Part 29)
**Prerequisite reading:** Part 37 (SU(3) condensate, structural results),
Part 44 (hierarchy ratio — α_EM underdetermined), Part 29 (m_cond circularity)

---

## What We Are Asking

The SU(2) gauge coupling g_W ≈ 0.6533 at the Z mass scale (PDG 2022).
PDTP explains the *structure* of SU(2): 3 generators → 3 weak bosons (W⁺, W⁻, Z),
Casimir factor C₂(fund) = 3/4, Z₂ vortices (fermion statistics). But can it
derive the *value* g_W ≈ 0.65?

**Short answer: no.** g_W is not an independent coupling. It is fixed by two
quantities that are themselves free parameters of the Standard Model and of PDTP.
This is a harder problem than m_cond (one free parameter) — g_W has two.

---

## The Weinberg Relation: g_W is Not Independent

The electroweak gauge group is SU(2)_L × U(1)_Y, broken to U(1)_EM.
After symmetry breaking, the physical couplings are related by:

```
e  =  g_W sin θ_W  =  g' cos θ_W
```

where θ_W is the Weinberg angle (weak mixing angle) and g' is the U(1)_Y coupling.
Squaring and using α_EM = e²/(4π):

```
g_W  =  e / sin θ_W  =  √(4π α_EM) / sin θ_W  =  √(4π α_EM / sin²θ_W)
```

At the Z mass scale (μ = m_Z):

```
α_EM(m_Z)  ≈  1/127.952    (running EM coupling, not 1/137 — QED running)
sin²θ_W    ≈  0.23122       (MS-bar scheme, PDG 2022)
g_W        =  √(4π/127.952/0.23122)  =  0.6533  ✓
```

**g_W is not a free parameter — it is a derived quantity, fixed by (α_EM, sin²θ_W).**

**Source:** Weinberg (1967), Phys.Rev.Lett. 19, 1264 — electroweak unification.

---

## Two Free Parameters, Not One

For g_W to be determined in PDTP, BOTH of the following must be derived:

### Free parameter 1: α_EM ≈ 1/137

The fine-structure constant is the fundamental electromagnetic coupling.
In PDTP (Part 44), this is the hierarchy ratio target: R = α_G/α_EM = (m_e/m_P)².
Part 44 proved that deriving α_EM from PDTP requires deriving the hierarchy —
which is equivalent to deriving m_cond (Part 29, circular).

**Status: underdetermined (Part 44 negative result)**

### Free parameter 2: sin²θ_W ≈ 0.231

The Weinberg angle measures the mixing between SU(2)_L and U(1)_Y condensates.
In PDTP, this is a new free parameter — the relative coupling strength between
the SU(2) condensate and the U(1) hypercharge condensate:

```
tan θ_W  =  g' / g_W  =  K_SU2_coupling / K_U1Y_coupling
```

PDTP predicts the mixing must exist (because both SU(2) and U(1) act on the same
matter sector), but cannot determine the angle from the Lagrangian structure alone.
The angle is set by the relative stiffness of the two condensates — an input, not
a prediction.

**Status: new underdetermined free parameter (not addressed in any prior Part)**

### Comparison to m_cond (Part 29)

| Problem | Free parameter | PDTP says | Status |
|---|---|---|---|
| Gravity scale | m_cond (= m_P?) | G = ħc/m_cond² (exact) | underdetermined |
| EM coupling | α_EM | R = α_G/α_EM = (m_e/m_P)² | underdetermined (Part 44) |
| Weak mixing | sin²θ_W | tan θ_W = g'/g_W | underdetermined (new) |
| Weak coupling | **g_W** | g_W = √(4πα_EM/sin²θ_W) | **doubly underdetermined** |

g_W is worse than m_cond: it requires TWO prior derivations, neither of which
PDTP can currently supply.

---

## What PDTP CAN Derive (Structural Results)

These follow from SU(2) group theory alone — no free parameters needed:

**1. Number of weak bosons:** N²−1 = 3 for SU(2) → W⁺, W⁻, Z (before mixing)
**Source:** SU(2) Lie algebra — exact, no assumptions.

**2. Casimir factor:** C₂(fundamental representation, SU(2)) = 3/4
**Source:** Standard group theory — exact.

**3. Z₂ vortices:** Half-integer winding numbers → fermion statistics (Wen 2004).
**Source:** Topological argument — same as Z₃ for SU(3) (Part 37).

**4. Asymptotic freedom:** SU(2) β-function coefficient b₀ = 19/6 > 0 → AF.
The SU(2) condensate is asymptotically free — the coupling g_W → 0 at high energies.
**Source:** Jones (1974), Nucl.Phys.B 75, 531 — one-loop SU(N) beta function.

**5. Mixing relation:** g_W = e/sin θ_W — exact structural relation.
**Source:** Weinberg (1967) — derived from SU(2)×U(1) gauge symmetry.

**6. Ratio relation:** α_EM/α_W = sin²θ_W — consequence of the Weinberg relation.
Numerically: (1/127.952)/(0.6533²/4π) = 0.2310 ≈ 0.23122 ✓

---

## Dimensional Transmutation Check (Negative)

Could the SU(2) coupling g_W be generated non-perturbatively from the condensate,
analogous to how Λ_QCD is generated in QCD via dimensional transmutation?

**In QCD:** α_S(m_Z) ≈ 0.118 is the input; Λ_QCD ~ 200 MeV emerges from RG running
(dimensional transmutation). The scale of QCD is NOT a free parameter at high energy —
it is generated dynamically.

**In SU(2):** The same mechanism does not apply here. The reason:
- SU(2) is broken at the electroweak scale v = 246 GeV by the Higgs mechanism
- Below m_W ~ 80 GeV, there is no SU(2) gauge theory — it is broken
- The running of g_W is only meaningful between m_W and the UV completion (GUT scale?)
- g_W at m_Z is an INPUT to the electroweak theory, not generated dynamically

The dimensional transmutation that works for QCD (confinement scale from α_S) does
not generate g_W because SU(2) is a broken gauge symmetry, not a confining one.

**Verdict: Dimensional transmutation does not fix g_W.** (Negative result)

The SU(2) condensate in PDTP is in its broken phase (Higgs condensate sets v ≠ 0).
The coupling g_W at the breaking scale is an input — it would require UV unification
(GUT) to be predicted, and GUT is itself a free-parameter theory at its scale.

---

## SU(2) Running: From m_Z to GUT Scale

Even if we cannot derive g_W, we can verify its running is consistent with GUT
unification (a structural check):

```
1/α_W(μ) = 1/α_W(m_Z) − (b₀/2π) × ln(μ/m_Z)
```

One-loop b₀(SU(2)) = 19/6 ≈ 3.167 in the Standard Model
(11/3 × 2 − 2/3 × 6 − 1/6 = 22/3 − 4 − 1/6 = 19/6, for 6 fermion doublets + 1 Higgs doublet)

At m_Z: 1/α_W(m_Z) = 29.57
At μ_GUT ~ 2×10¹⁶ GeV (standard GUT scale):

```
1/α_W(m_GUT) = 29.57 − (19/6)/(2π) × ln(2×10¹⁶/91.2)
             = 29.57 − 0.504 × 32.72
             = 29.57 − 16.49  =  13.1
```

At the GUT scale, the three SM couplings approximately meet:
1/α_W ~ 13, 1/α_S ~ 25, 1/α_Y ~ 12 (rough, without SUSY).
They do not unify exactly at 1-loop without SUSY — this is a known SM limitation.

The running is internally consistent; the starting value g_W(m_Z) = 0.6533 remains
a free parameter, set by whatever UV completion (string theory, GUT, etc.) determines
the coupling at the unification scale.

---

## The PDTP Conclusion: Two Free Parameters

**PDTP Original:** The weak coupling constant g_W is doubly underdetermined in PDTP:

```
g_W  =  √(4π α_EM / sin²θ_W)

           ^               ^
    (underdetermined   (underdetermined
     Part 44/29)        this Part)
```

The SU(2) condensate in PDTP has exactly two free parameters beyond its structure:
- The coupling stiffness K_SU2 (sets the overall scale of g_W — analogous to m_cond)
- The mixing angle θ_W (sets the split between g_W and g' — new parameter)

Neither can be derived from the PDTP Lagrangian L = K Tr[(∂U†)(∂U)] + Σ gᵢ Re[Tr(Ψᵢ†U)]/2
alone. They are to the SU(2) condensate what Λ is to GR — free parameters of the
theory, not predictions of it.

**This is not a failure of PDTP — it is the correct finding.** The Standard Model
itself has 19 free parameters; sin²θ_W and α_EM are two of them. PDTP inherits
these free parameters at the level of the condensate coupling constants.

---

## Sudoku Scorecard (Phase 23 — 10 tests)

See `simulations/solver/weak_coupling_gw.py` for numerical verification.

| Test | Description | Result |
|---|---|---|
| GW1 | g_W = e/sin θ_W: Weinberg relation (numerical) | PASS |
| GW2 | α_W = g_W²/(4π) ≈ 1/29.57 at m_Z | PASS |
| GW3 | G_F = g_W²√2/(8m_W²): Fermi constant | PASS |
| GW4 | m_W = g_W v/2 (tree level, v=246.22 GeV) | PASS |
| GW5 | sin²θ_W = 1 − m_W²/m_Z² | PASS |
| GW6 | α_EM/α_W = sin²θ_W: ratio relation | PASS |
| GW7 | N_generators = N²−1 = 3 for SU(2) [exact] | PASS |
| GW8 | C₂(fund, SU(2)) = 3/4 [exact] | PASS |
| GW9 | b₀(SU2) = 19/6 > 0 (asymptotically free) | PASS |
| GW10 | Circularity: g_W requires (α_EM, sin²θ_W) — both free | PASS (negative result) |

**Score: 10/10 pass** — structural and numerical consistency confirmed.
The negative result (GW10) is the primary finding.
Verified: `weak_coupling_gw.py`.

---

## Key Results

**Result 1:** g_W is NOT a free parameter — it is g_W = √(4π α_EM/sin²θ_W),
fixed by two prior quantities.

**Result 2 (PDTP Original):** The SU(2) condensate has TWO underdetermined free
parameters: α_EM (hierarchy problem, Part 44) and sin²θ_W (new — mixing angle
between SU(2) and U(1)_Y condensates). This makes g_W doubly underdetermined.

**Result 3 (PDTP Original):** Dimensional transmutation does not apply — SU(2) is
a broken (not confining) gauge symmetry. g_W cannot be generated dynamically
in the PDTP condensate picture.

**Result 4:** PDTP correctly predicts the structural features: 3 W bosons (N²−1 = 3),
C₂ = 3/4, asymptotic freedom (b₀ = 19/6 > 0), Z₂ vortices, mixing relation.

**Result 5:** The analogy is exact: g_W is to the SU(2) condensate as G is to the
gravitational condensate — a free parameter that encodes the condensate stiffness,
not derivable from the Lagrangian structure alone.

---

## Sources

- Weinberg (1967), Phys.Rev.Lett. 19, 1264 — SU(2)×U(1) electroweak unification
- Glashow (1961), Nucl.Phys. 22, 579 — weak isospin gauge theory
- Salam (1968), in "Elementary Particle Theory" — electroweak model
- Jones (1974), Nucl.Phys.B 75, 531 — one-loop SU(N) beta function; b₀(SU2) = 19/6
- PDG (2022) — g_W = 0.6533, sin²θ_W = 0.23122, m_W = 80.377 GeV, m_Z = 91.1876 GeV,
  G_F = 1.1663788×10⁻⁵ GeV⁻², α_EM(m_Z) = 1/127.952
- Wen (2004), Phys.Rev.D 68 — Z₂ vortices and fermion statistics
- **PDTP Original:** g_W doubly underdetermined (α_EM + sin²θ_W both free);
  dimensional transmutation inapplicable to broken SU(2); analogy g_W ↔ G as free parameter
- Cross-references: Part 29 (m_cond circularity), Part 37 (SU(3) structure),
  Part 44 (hierarchy ratio, α_EM underdetermined)

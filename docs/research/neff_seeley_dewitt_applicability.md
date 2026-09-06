# N_eff via Spin-Weighted Seeley-DeWitt Coefficient — Applicability Check (Part 140)

**Script:** `simulations/solver/t70_neff_seeley_dewitt.py`
**Status:** DONE — CONSTRUCTIVE NEGATIVE (10/10 Sudoku PASS)
**Output log:** `simulations/solver/outputs/t70_neff_seeley_dewitt_20260906.txt`
**Closes:** TODO_04.md T70
**Prerequisites:** Part 83 (`neff_sakharov.md`, the N_eff = 6π gap), Part 114
(`su3_nonlinear_vertex.md`, the exact SU(3) vertex + Weinberg anchor), Part 37
(`su3_condensate_extension.md`, the SU(3) Lagrangian), Part 40 (`su3_fermion.md`,
Wilson fermions as lattice scaffolding), Part 129 (T12, the M=0 negative result).

---

## Plain English Summary

An external AI review (qwen3.7) suggested closing Part 83's "gravity is 2.4x
too strong" gap with a fancier counting tool: instead of counting each field
as worth exactly 1 unit, weight vectors, fermions, and scalars differently
(vectors count fully, fermions count 5.5x, scalars count 1/6), because that's
supposedly how a rigorous quantum-gravity calculation (the "Seeley-DeWitt heat
kernel") actually works. **Two independent checks kill this before it ever
gets applied.** First: a real literature search could not find this specific
formula attributed to any paper — it may be a garbled memory of something
real, or it may not exist at all; either way it fails the project's own
citation bar. Second, and more decisive: **the formula needs actual vector
particles (like photons) and actual fermion particles (like electrons) to
plug numbers into — and PDTP's own Lagrangian has neither.** PDTP's "8
gluons" and "quarks" are just names borrowed from QCD for what is
mathematically a completely different kind of object: a field of numbers
(technically, a 3×3 matrix of angles) with an ordinary wave equation, the
same mathematical family as the pion field in nuclear physics — not a force-
carrying particle with the twisting, self-referential structure of a real
gauge field, and not a spin-1/2 particle either. We checked this by re-
reading every version of the PDTP Lagrangian (single-phase, SU(3), two-
phase) line by line, and by confirming that the one place actual fermions
*do* show up in the project (Part 40) is explicitly borrowed, standard
lattice-QCD machinery used as a numerical tool for one specific side-
calculation — not a description of PDTP's own matter field. So the
suggested formula's more sophisticated parts (the vector and fermion
weights) have nothing to attach to. We even computed what the numbers
would be if you plugged them in anyway (treating PDTP's gluons and quarks
as if they were literally the QCD versions) — it makes the gap far worse,
not better. **Part 83's original, plainer scalar-only counting was already
the right tool for the job; nothing about the gap's characterization
changes.**

---

## 1. The Question (T70, filed after external review)

Does replacing Part 83's crude DOF-counting tools (a scalar-only Visser
formula, and a naive signed helicity sum that gives the nonsensical
N_eff(SM) = −62) with a more sophisticated spin-weighted formula close, or
meaningfully tighten, the N_eff = 6π gap in PDTP's Sakharov induced-gravity
calculation?

**The suggested tool** [UNVERIFIED — see Section 2]:

```
N_eff = N_v + (11/2)*N_f + (1/6)*N_s                              (140.1)
```

with N_v = vector bosons, N_f = Dirac fermions, N_s = real scalars, applied
to PDTP's field content: 8 SU(3) "gluons" (as N_v), matter "quarks"/leptons
(as N_f), and the two-phase φ₊/φ₋ scalars (as N_s).

---

## 2. Step 1 — Source Verification [NEGATIVE, per CODING_STANDARDS]

CODING_STANDARDS requires every established formula to cite its source.
Eq. 140.1 was supplied by the external review without one. Two targeted
literature searches were run:

1. "induced gravity Sakharov effective number of degrees of freedom heat
   kernel '11/2' fermion vector scalar coefficient"
2. "Seeley-DeWitt a2 coefficient induced Newton constant N_eff vector
   fermion scalar weight Visser Frolov Fursaev"

Both searches returned genuine heat-kernel and induced-gravity literature
(Vassilevich 2003's heat-kernel review, Visser's own "Sakharov's induced
gravity: a modern perspective", Frolov & Fursaev 1998 — all already cited
in Part 83) but **no source stating the specific combination N_v + (11/2)N_f
+ (1/6)N_s could be located.** This does not prove no such paper exists —
search coverage is not exhaustive — but per the project's own citation
standard, an unsourced formula cannot be accepted as "established physics"
and used as-is. [Consistent with the T71 finding on the same review's
Suggestion 4 (the CKN "factor 12" claim) — that one search succeeded and
the number turned out to be real (Part 54); this one did not succeed. Both
outcomes are reported plainly, not selectively.]

**This alone would be enough to pause the exercise** — but Step 2 shows the
formula would not apply to PDTP even if a source were found.

---

## 3. Step 2 — Field-Content Audit: Does PDTP Have Vectors or Fermions?

Eq. 140.1 requires literal vector fields (N_v) and literal Dirac fermion
fields (N_f) in the theory being quantized. This section re-reads every
version of the PDTP Lagrangian that exists in the project to check whether
either is actually present.

### 3.1 U(1) Lagrangian (the base theory)

```
L = (1/2)(d_mu phi)(d^mu phi) + Sum_i (1/2)(d_mu psi_i)(d^mu psi_i)
    + Sum_i g_i cos(psi_i - phi)                                  (140.2)
```

**Source:** CLAUDE.md, "Key Equations". Both φ and every ψᵢ are declared
`φ ∈ ℝ` — real scalar phase angles. No vector index, no spinor index,
anywhere in this expression. [CONFIRMED, inspection]

### 3.2 SU(3) Lagrangian (Part 37)

```
L = K Tr[(d_mu U-dag)(d^mu U)] + Sum_i K_i Tr[(d_mu Psi_i-dag)(d^mu Psi_i)]
    + Sum_i g_i Re[Tr(Psi_i-dag U)] / 3                            (140.3)
```

**Source:** `su3_condensate_extension.md` Section 3.1 (Part 37), also
CLAUDE.md. U(x) and every Ψᵢ(x) are declared `∈ SU(3)` — 3×3 unitary
**matrix-valued fields**, with an ordinary two-derivative kinetic term
Tr[(∂U†)(∂U)]. This is the **nonlinear sigma model** kinetic term (the same
mathematical family as the pion Lagrangian in chiral perturbation theory,
Scherer 2003) — not the Yang-Mills kinetic term Tr[F_μν F^μν] that a real
gauge field requires, where F_μν = ∂_μA_ν − ∂_νA_μ + i[A_μ,A_ν] is built
from a **gauge connection** A_μ via a covariant derivative D_μ = ∂_μ + igA_μ.
**Neither a gauge connection nor a covariant derivative appears anywhere in
Eq. 140.3.** [CONFIRMED, inspection — no D_μ, no F_μν, in the cited source]

Ψᵢ(x) is likewise declared matrix-valued with the *same* kinetic-term
structure as U(x) — no spinor index, no γ^μ, no Dirac operator. [CONFIRMED]

### 3.3 Independent confirmation from Part 114

Part 114 (`su3_nonlinear_vertex.md`) performed the actual expansion of Eq.
140.3 to fourth order in the fluctuation field χ (U = e^{iεχ}) and:

- explicitly classifies the 8 real fields χ^a as **"8 real massless
  scalars"** (Part 83 Section 4(a), reused verbatim in Part 114's setup) —
  not vectors;
- verifies the resulting quartic vertex, when reduced to SU(2), reproduces
  **Weinberg's 1966 pion-scattering vertex exactly** (Eq. 114.7, residual
  0) — an experimentally-anchored result for **pions**, which are scalars/
  pseudoscalars, not vector gauge bosons;
- proves a **Trace Theorem** (Eq. 114.6): the tree-level action built from
  Eq. 140.3 is an algebraic functional of Tr(g_μν) alone, containing no
  Yang-Mills-type field-strength dynamics at any order in ε.

Three independent lines (the Lagrangian's own kinetic-term structure, the
absence of any gauge-covariant derivative, and Part 114's SU(2) ChPT anchor)
all agree: **PDTP's "gluons" are spin-0 sigma-model fluctuations, not spin-1
gauge bosons.** [DERIVED, cross-confirmed]

### 3.4 Two-phase Lagrangian (Part 61)

```
L = +g cos(psi - phi_b) - g cos(psi - phi_s)                       (140.4)
```

**Source:** CLAUDE.md, "Two-Phase Lagrangian". φ_b, φ_s (and the derived
φ₊, φ₋) are all real scalar phases — the same U(1) structure as Eq. 140.2,
just split into two terms. No vector or spinor promotion anywhere in
Parts 61–63. [CONFIRMED, inspection]

### 3.5 The one place fermions DO appear: Part 40 — and why it doesn't count here

`su3_fermion.md` (Part 40) introduces genuine 4-component Dirac spinors
ψ(x) with Euclidean γ^μ matrices satisfying the Clifford algebra
{γ_μ,γ_ν} = 2δ_μν — real fermionic structure, unambiguously. **But this is
the standard Wilson-fermion action from conventional lattice QCD** (Wilson
1975; DeGrand & DeTar 2006), borrowed wholesale as a **numerical scaffold**
to test one specific question: does including dynamical sea-quark loops
improve the SU(3) lattice string-tension match from Part 39? This is
exactly the "Wilson's Lattice QCD — Scaffolding as Numerical Tool" pattern
already catalogued in `Methodology.md` ("The lattice is not physical — it
is scaffolding that lets you extract real numbers... The lattice is the
tool, not the theory"). Part 40's own conclusion reinforces this: sea
quarks *widened* the string-tension gap, and the doc attributes the
original 4% mismatch to "an artifact of truncating the strong coupling
expansion... not from missing quark matter fields" — i.e., Part 40 itself
does not treat these borrowed fermions as a successful description of
PDTP's own matter content. PDTP's own continuum matter field remains Ψᵢ(x)
∈ SU(3) (Eq. 140.3), never redefined as a Dirac spinor anywhere in the
project. [CONFIRMED — distinguishing borrowed numerical tool from PDTP's
own fundamental field content]

A related check: `chirality_parity_violation.md` maps PDTP's Z₂ vortex-
winding topology onto the Standard Model's Dirac chirality classification
(γ⁵ eigenvalues) as an **external comparison target**, citing Peskin &
Schroeder's Dirac algebra as the thing being compared *against* — it does
not claim PDTP's own Lagrangian fields are Dirac spinors either.
[CONFIRMED, same pattern as Part 40]

### 3.6 Conclusion of the Audit

**Across every version of PDTP's own continuum Lagrangian (U(1), SU(3),
two-phase), N_v = 0 and N_f = 0 identically. Only N_s is ever nonzero.**
[DERIVED, from Sections 3.1–3.5]

---

## 4. Step 3 — What the Formula Gives, Computed Both Ways

Even though Section 3 shows the QCD-analogy reading (N_v=8, N_f=18-24) is
not justified by PDTP's own Lagrangian, the numbers were computed anyway
for completeness (`t70_neff_seeley_dewitt.py`), since a suggestion should
be checked on its own terms before being set aside:

| Scenario | N_v | N_f | N_s | N_eff (Eq 140.1) | G_ind/G |
|---|---:|---:|---:|---:|---:|
| Minimal (8 gluons as vectors) | 8 | 0 | 0 | 8.00 | 2.356 |
| +two-phase | 8 | 0 | 2 | 8.33 | 2.262 |
| +matter, quarks only (18 as Dirac) | 8 | 18 | 2 | 107.33 | 0.176 |
| +matter, full 24 species (as Dirac) | 8 | 24 | 2 | 140.33 | 0.134 |

[COMPUTED] Including any matter as Dirac fermions massively **overshoots**
N_eff (the (11/2) weight dominates) — G_ind/G collapses to 0.13–0.18, far
worse than Part 83's own already-tabulated range [0.554, 2.356]. The
QCD-analogy reading does not help even taken at face value.

The structurally-justified reading (N_v=0, N_f=0, only Eq. 140.1's (1/6)
scalar weight applied to Part 83's own scalar counts) also does not help:

| N_s (Part 83's own count) | N_eff, Eq 140.1 weighted | G_ind/G | Part 83's own (1-per-scalar) G_ind/G |
|---:|---:|---:|---:|
| 8 | 1.33 | 14.14 | 2.356 |
| 10 | 1.67 | 11.31 | 1.885 |
| 34 | 5.67 | 3.33 | 0.554 |

[COMPUTED] A literal (1/6) weight per scalar makes every scenario worse
(further from G_ind/G = 1) than Part 83's own unweighted counting — which
strongly suggests Eq. 140.1's normalization convention is not the same one
Part 83's Visser-based N_s already uses (Visser's formula likely already
bakes in an equivalent weight internally), rather than being a genuine
correction to it. Reconciling the two conventions would require the Step-1
source this exercise could not locate.

---

## 5. Cross-Check Against T12/Part 129

Part 129 (T12) established a *different* negative: n_PDTP cannot modify the
Sakharov cutoff because the calculation lives entirely at M=0, where
n_PDTP ≡ 1 identically. This Part's negative is structurally independent —
it concerns *which fields exist* to be counted, not whether a refractive
index can rescale the cutoff once fields are chosen. The two negatives are
compatible and non-overlapping: Part 129 closed one proposed modification
mechanism; this Part closes a different proposed counting refinement.
Neither reopens the other. [VERIFIED, no contradiction]

---

## 6. What This Changes (and Doesn't) for Part 83

**Does not change:** Part 83's own characterization of the N_eff gap —
range [8, 34], target 6π ≈ 18.85, the 1%-off Casimir-enhancement near-miss
(18.67) — stands exactly as derived. Part 83 already used a scalar-only
tool (the Visser formula for N_s real scalars); Section 3 above confirms
that was always the *correct* category of tool to use, not merely the
simplest available one.

**Does change:** the project's understanding of *why* a more sophisticated
spin-weighted tool doesn't trivially help — it's not that Part 83's method
was too crude, it's that PDTP's own field content has nothing for the
extra sophistication (vector and fermion weights) to act on. This is a
useful thing to have on record given PDTP borrows QCD's vocabulary
("gluons", "quarks", "color") for objects that are mathematically a
different species (sigma-model scalars, not gauge bosons and spinors) —
a distinction worth stating plainly so it isn't rediscovered by confusion
later, the same service Part 136 (T66) performed for "Cosserat" and
elastic-universe.org's own mislabeled code.

---

## 7. Sudoku Scorecard — 10/10 PASS

| # | Check | Verdict |
|---|-------|---------|
| S1 | Eq 140.1 not found in 2 targeted literature searches | PASS (negative search recorded) |
| S2 | U(1) Lagrangian: phi, psi_i declared real scalar (in R) | PASS |
| S3 | SU(3) Lagrangian: U(x), Psi_i(x) declared matrix-valued, kinetic term Tr[(dU-dag)(dU)] (sigma-model form) | PASS |
| S4 | No covariant derivative D_mu or field-strength F_mu_nu appears in Eq 140.3 | PASS |
| S5 | Part 114 independently classifies chi^a as "8 real massless scalars" | PASS |
| S6 | Part 114's SU(2) reduction matches Weinberg's scalar/pseudoscalar pion vertex exactly (residual 0) | PASS |
| S7 | Two-phase Lagrangian (Part 61): phi_b, phi_s, phi_+, phi_- all real scalar phases | PASS |
| S8 | Part 40's Dirac fermions are the standard lattice-QCD Wilson action (Wilson 1975), a borrowed numerical scaffold -- not a redefinition of Psi_i | PASS |
| S9 | QCD-analogy reading (N_v=8,N_f=18-24) gives G_ind/G in [0.134,0.176], worse than Part 83's existing [0.554,2.356] range | PASS (computed) |
| S10 | Structurally-justified reading (N_v=N_f=0) with Eq 140.1's 1/6 scalar weight gives G_ind/G in [3.33,14.14], worse than Part 83's own unweighted scalar counting | PASS (computed) |

All scorecard values are read from computed step outputs or direct
inspection of cited primary sources (RECHECK rule).

---

## 8. References

- **Source:** Wilson, K. (1975), *Phys. Rev. D* 10, 2445 — Wilson fermion action (Part 40's borrowed tool)
- **Source:** DeGrand, T. & DeTar, C. (2006), *Lattice Methods for Quantum Chromodynamics*, Ch. 6
- **Source:** Scherer, S. (2003), "Introduction to Chiral Perturbation Theory", Adv. Nucl. Phys. 27, 277 (arXiv: hep-ph/0210398) — nonlinear sigma model kinetic-term family
- **Source:** Weinberg, S. (1966), *Phys. Rev. Lett.* 17, 616 — pion vertex, reused as Part 114's anchor
- **Source:** Peskin, M. & Schroeder, D. (1995), *Introduction to QFT* — Dirac algebra, chirality projectors (external comparison target in `chirality_parity_violation.md`)
- Part 37 — `su3_condensate_extension.md` (the SU(3) Lagrangian audited here)
- Part 40 — `su3_fermion.md` (Wilson fermions as lattice scaffolding)
- Part 61 — `two_phase_lagrangian.md` (two-phase Lagrangian)
- Part 83 — `neff_sakharov.md` (the N_eff gap this Part leaves unchanged)
- Part 114 — `su3_nonlinear_vertex.md` (independent scalar classification + ChPT anchor)
- Part 129 — `neff_sakharov.md` Section 10 (T12, the M=0 negative — cross-checked, non-overlapping)
- `docs/misc/qwen3.7. pdtp. suggest.md` — the external suggestion this Part evaluates
- **PDTP Original:** the field-content audit (Section 3), the applicability
  computation (Section 4), and the category-mismatch finding (Section 6) are
  new to this Part.

---

*Part 140 (T70). Previous: Part 139 (T69 sub-points 2-3).*
*Equations to add to `equation_reference.md`: Eq 140.1 (external formula, unverified).*

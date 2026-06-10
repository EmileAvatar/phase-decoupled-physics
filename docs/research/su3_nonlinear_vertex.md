# Part 114 — The O(ε⁴) Nonlinear Vertex: SU(3) Sigma Model vs Einstein–Hilbert

**Phase:** 82 — `simulations/solver/su3_nonlinear_vertex.py`
**Date:** 2026-06-10
**Status:** DONE — CONSTRUCTIVE NEGATIVE + PRODUCTIVE (14/14 Sudoku PASS)
**Output log:** `simulations/solver/outputs/su3_nonlinear_vertex_20260610_165300.txt`
**Closes:** Part 76g OPEN item ("full nonlinear equivalence remains OPEN")

---

## 1. The Question

Parts 75–76 established that the SU(3) emergent metric

```
g_μν = Tr(∂_μU† ∂_νU),   U(x) ∈ SU(3)                       (75.0)
```

reproduces **linearized vacuum GR**: 2 TT modes, Fierz–Pauli structure
(via Sakharov), automatic Lorenz gauge, □h = 0. Part 76g then asked: does
the theory also reproduce GR's **nonlinear** structure (the h∂h∂h graviton
self-interaction)? 76g found, *by inspection*, a derivative-order mismatch
and left the item OPEN with only the schematic estimate

```
h⁽⁴⁾_μν ~ f^{abe} f^{cde} χ^b χ^d (∂χ^c)(∂χ^e)              (76g.1)
```

Part 114 replaces inspection with exact computation. Four questions:

1. What is the **exact** O(ε⁴) term of the emergent metric? (closes 76g.1)
2. Can it be identified with any GR structure at the same order?
3. If not — does that *break* the GR recovery of Parts 75–76?
4. Is the computation **externally checkable** against established physics?

**Plain English:** Einstein's gravity is "nonlinear" — gravity itself
gravitates. We check whether our spacetime-condensate model has the same
self-feeding behaviour built in at the classical level, or something else.

---

## 2. Setup and Conventions

- Generators: T^a = λ^a/2 (Gell-Mann), Tr(T^aT^b) = δ^{ab}/2. [ESTABLISHED]
- Structure constants: [T^a,T^b] = i f^{abc} T^c, computed in the script as
  f^{abc} = −2i Tr([T^a,T^b]T^c) — not table lookup. f^{123} = 1.
- Condensate field: U = exp(iεχ), χ = χ^a(x) T^a, ε the expansion parameter.
- Pointwise representation: χ, ∂_μχ, ∂_νχ are treated as three independent
  Lie-algebra elements A, B, C with free real coefficients (a_a, b_a, c_a).
  This is valid at any single spacetime point and makes every identity below
  a *polynomial* identity that SymPy verifies by exact subtraction.
- Background: expansion around U = I; the flat background η_μν comes from
  background gradients ∂π̄ as in Part 76d. The quartic vertex computed here
  is insensitive to that split at leading order. [NOTED LIMITATION]

---

## 3. Derivation D1 — Expansion of the Metric to O(ε⁴)

### 3.1 Maurer–Cartan form

Every step below is also verified independently by the script via the
direct product-rule series (Eq. 114.D5), so no step relies on memory.

**Step 1.** For U = e^{iεχ}, the left-invariant Maurer–Cartan form is the
standard derivative-of-exponential formula (Weinberg 1996, QFT II, Ch. 15):

```
L_μ ≡ U†∂_μU = iε ∂_μχ − (iε)²/2 [χ, ∂_μχ] + (iε)³/6 [χ,[χ,∂_μχ]] + O(ε⁴)
                                                              (114.D1)
```

**Step 2.** Since U†U = I, differentiating gives ∂_μU† = −L_μU†, hence

```
∂_μU† ∂_νU = −L_μ U† U L_ν = −L_μ L_ν
g_μν = −Tr(L_μ L_ν)                                           (114.D2)
```

**Step 3.** Write A = χ, B = ∂_μχ, C = ∂_νχ and collect powers of ε.

**O(ε²):** −Tr( (iB)(iC) ) = Tr(BC) = ½ Σ_a b_a c_a.
This is exactly Eq. 75.1. **SymPy: residual = 0.**

```
g⁽²⁾_μν = ε² Tr(∂_μχ ∂_νχ) = (ε²/2) Σ_a (∂_μχ^a)(∂_νχ^a)     (114.1) [VERIFIED]
```

**O(ε³):** the cross terms L⁽¹⁾L⁽²⁾ + L⁽²⁾L⁽¹⁾ give

```
−Tr( iεB · ε²/2 [A,C] ) − Tr( ε²/2 [A,B] · iεC )
  = −(iε³/2) [ Tr(B[A,C]) + Tr([A,B]C) ]
```

By cyclicity of the trace, Tr([A,B]C) = Tr(ABC) − Tr(BAC) and
Tr(B[A,C]) = Tr(BAC) − Tr(BCA) = Tr(BAC) − Tr(ABC) = −Tr([A,B]C).
The bracket vanishes **identically**:

```
g⁽³⁾_μν = 0                                                   (114.2) [DERIVED]
```

**SymPy: g⁽³⁾ = 0 exactly** (NV-S2). There is no cubic term at all — the
metric expansion has only even orders (consistent with U(ε,χ) = U(−ε,−χ)
symmetry of the exponential).

**O(ε⁴):** three contributions:

```
(1,3):  −Tr( iεB · (iε)³/6 [A,[A,C]] )  = −(ε⁴/6) Tr(B[A,[A,C]])
(3,1):  −(ε⁴/6) Tr([A,[A,B]] C)
(2,2):  −Tr( (ε²/2)[A,B] · (ε²/2)[A,C] ) = −(ε⁴/4) Tr([A,B][A,C])
```

Using the adjoint-operator identity Tr(B[A,[A,C]]) = −Tr([A,B][A,C])
(integration by parts in the Lie algebra; follows from cyclicity), with
X ≡ Tr([A,B][A,C]):

```
g⁽⁴⁾ = ε⁴ [ −(1/6)(−X) − (1/6)(−X) − (1/4)X ] = ε⁴ (1/3 − 1/4) X = (ε⁴/12) X
```

```
g⁽⁴⁾_μν = (ε⁴/12) Tr( [χ, ∂_μχ] [χ, ∂_νχ] )                  (114.3) [DERIVED]
```

**SymPy: coefficient solved from the computed expansion = 1/12,
full polynomial residual = 0** (232 monomials; NV-S3).

### 3.2 Structure-constant form

**Step 4.** Substitute [χ, ∂_μχ] = i f^{abe} χ^a (∂_μχ^b) T^e and use
Tr(T^eT^{e'}) = δ^{ee'}/2:

```
Tr([χ,∂_μχ][χ,∂_νχ]) = (i)(i) f^{abe} f^{cde} χ^a ∂_μχ^b χ^c ∂_νχ^d · (1/2)
                     = −(1/2) f^{abe} f^{cde} χ^a ∂_μχ^b χ^c ∂_νχ^d
```

```
g⁽⁴⁾_μν = −(ε⁴/24) f^{abe} f^{cde} χ^a (∂_μχ^b) χ^c (∂_νχ^d)  (114.4) [DERIVED]
```

**SymPy: coefficient = −1/24 exactly, residual = 0** (NV-S4). This
upgrades Eq. 76g.1 from a schematic "~" to an exact equation (and fixes
its index placement: the χ's carry the *first* index of each f, the
gradients the second, contracted on the third).

Checks attached to (114.4), all computed:
- g⁽⁴⁾ symmetric under μ↔ν (NV-S5): residual 0.
- Casimir contraction Σ_{ab} f^{abe}f^{abd} = 3δ^{ed} = C₂(adj) δ
  (Weinberg 1996, Eq. 15.4.17) recomputed from the f's: PASS (NV-S6).

**Plain English:** the condensate's "extra" self-interaction at fourth
order is now an exact formula, not a sketch. Its strength is fixed —
coefficient 1/24 — with no freedom left.

---

## 4. Derivation D2 — The Trace Theorem (tree level has no graviton dynamics)

**Step 1.** The tree-level Lagrangian and the emergent metric are built
from the *same* object:

```
L_tree = K Tr(∂_μU† ∂^μU) = K η^{μν} Tr(∂_μU† ∂_νU) = K η^{μν} g_μν[U]
                                                              (114.5) [DERIVED]
```

This is definitional — but its consequence was never stated in Parts 74–76:

**Theorem (114.6).** *The tree-level action is an algebraic functional of
the emergent metric (its η-trace). It contains no derivatives of g_μν,
hence no (∂h)² kinetic term, no curvature, and no h∂h∂h vertex — at any
order in ε.* [DERIVED]

**Step 2.** Therefore the Sakharov one-loop term (Part 74b) is not one
route among several: it is the **unique** source of graviton dynamics in
PDTP. The question "does the tree-level σ-model vertex equal GR's
nonlinear vertex?" has answer **no by structure** — the tree action does
not contain *any* metric dynamics, linear or nonlinear.

**SymPy content:** the Lorentz-diagonal quartic density (C→B) equals
(1/12)Tr([A,B]²), residual 0 (NV-S7); its probe value is negative,
consistent with Tr([A,B]²) = −‖[A,B]‖² (commutators are anti-Hermitian).

**Plain English:** the condensate's own action only *defines* the shape of
spacetime; it does not make spacetime wiggle. The wiggling (gravitons,
Einstein's equations) comes entirely from quantum fluctuations of the
condensate — the Sakharov mechanism. We previously treated that as one
possible route; it is now proven to be the only one.

---

## 5. Derivation D3 — External Anchor: Weinberg's Pion Vertex (1966)

The strongest possible check: the same expansion, for SU(2), must
reproduce chiral perturbation theory — established, experimentally
verified physics.

**Step 1.** ChPT conventions: U = exp(i π·τ/F), L = (F²/4)Tr(∂_μU†∂^μU),
with τ = 2T the Pauli matrices and F the pion decay constant.
**Source:** Scherer (2003), "Introduction to Chiral Perturbation Theory",
Adv. Nucl. Phys. 27, 277 (arXiv: hep-ph/0210398).

**Step 2.** Map to our variables: iεχ·T... = iπ·τ/F ⇒ εχ^a = 2π^a/F,
K = F²/4. The SU(2) expansion is **re-derived from scratch** with Pauli
generators in the script (not reused from SU(3)): coefficient = −1/24
again — the coefficient is group-independent (NV-S8).

**Step 3.** Insert into (114.4), Lorentz-contracted, with SU(2) structure
constants f^{abc} = ε^{abc} and the identity
ε^{abe}ε^{cde} = δ^{ac}δ^{bd} − δ^{ad}δ^{bc}:

```
L₄ = K ε⁴ · (−1/24) ε^{abe}ε^{cde} π^a ∂π^b π^c ∂π^d
   = (F²/4)(2/F)⁴(−1/24) [ π²(∂π·∂π) − (π·∂π)² ]
   = (1/(6F²)) [ (π·∂_μπ)(π·∂^μπ) − π²(∂_μπ·∂^μπ) ]           (114.7) [VERIFIED]
```

This is **exactly** the Weinberg ππ-scattering vertex (Weinberg 1966,
Phys. Rev. Lett. 17, 616; Scherer 2003, Eq. 4.21). **SymPy: residual = 0**
(NV-S9), computed with abstract contraction symbols u_qs = ∂π^q·∂π^s.

**Plain English:** to make sure our gravity formula isn't a calculation
error, we ran the identical machinery on pions (where the answer has been
known and measured for 60 years). It lands on Weinberg's famous formula
exactly. The SU(3) coefficient −1/24 is therefore trustworthy.

---

## 6. Derivation D4 — U(1) Limit

For U = e^{iεφ} with a single phase, scalars commute, so

```
∂_μU† ∂_νU = (−iε∂_μφ)(iε∂_νφ) U†U = ε² (∂_μφ)(∂_νφ)          (114.8) [DERIVED]
```

**exactly, to all orders.** The script verifies the truncated series:
ε³ and ε⁴ coefficients vanish identically (NV-S10).

Consequences:
- The quartic vertex is a genuinely **non-Abelian** effect (∝ f^{abc}).
- The single-phase U(1) PDTP theory, and therefore the **two-phase
  Lagrangian of Part 61** (which lives entirely in the Abelian sector:
  φ_b, φ_s are U(1) phases), is untouched: Newton's 3rd law
  (ψ̈ = −2φ̈₊), the biharmonic equation (∇⁴ + 4g²), and the Jeans
  eigenvalue (+2√2 g) are all unaffected by Part 114. [Sudoku rule 4 ✓]
- Newton's laws check (Sudoku rule 5): the vertex does not modify the
  U(1) phase-locking sector from which Newton's laws were derived. ✓

---

## 7. Derivation D5 — No-Go: Derivative Grading Forbids an EH Identification

**Step 1.** Under χ(x) → χ(λx), a local Lorentz-invariant term with D
derivatives scales as λ^D. The grading D is preserved by integration by
parts (each ∂ stays a ∂) and by the on-shell condition □χ = 0 (which
removes terms but never changes D of the survivors).

**Step 2.** Count D at O(ε⁴) (four χ fields in every candidate):

| Term | Structure | D |
|------|-----------|---|
| NLSM quartic vertex (114.4) | f f χ(∂χ)χ(∂χ) | **2** [COMPUTED: NV-S11] |
| graviton–matter coupling h^{μν}T_μν with h ~ ∂χ∂χ | (∂χ∂χ)(∂χ∂χ) | 4 |
| Fierz–Pauli kinetic L_EH⁽²⁾[h] (Weinberg 1972, Ch. 10) | (∂h)² ~ (∂∂χ∂χ)² | 6 |

The script verifies the NLSM vertex is exactly homogeneous of degree 2
in derivatives: g⁽⁴⁾(λb, λc) − λ²g⁽⁴⁾ = 0.

**Theorem (114.9).** *No identification of the NLSM quartic vertex with
either GR structure is possible, on-shell or off-shell: a λ²-graded term
cannot equal a λ⁴- or λ⁶-graded term unless both vanish.*
[DERIVED, NEGATIVE]

This converts Part 76g's observation ("derivative order differs") into a
proof, and closes the question in the negative — *at tree level*. Combined
with the Trace Theorem (114.6), the negative is not a failure of GR
recovery: tree level was never where GR lives in PDTP.

---

## 8. Derivation D6 — Scale of the Non-GR Contact Term

The vertex (114.4) is a real, additional interaction that GR does not
have. Does it spoil the GR recovery at observable energies?

**Step 1.** Canonical normalization χ_c^a = √K ε χ^a turns the Lagrangian
into

```
L = ½(∂χ_c)² + (1/(24K)) f^{abe}f^{cde} χ_c^a ∂χ_c^b χ_c^c ∂χ_c^d
```

so the 4-point contact amplitude scales as **A_NLSM ~ E²/(24K)** at
center-of-mass energy E.

**Step 2.** Identification of K (Parts 29/35): K = K_NAT·m_cond² with
K_NAT = 1/(4π), m_cond = m_P (Part 33). [ASSUMED — same status as in
Parts 74–76; this is the one input carried over.]

**Step 3.** Computed numbers (NV-S13, NV-S14):

```
λ₄ = 1/(24K) = 4π/24 = π/6 ≈ 0.524 / m_P²
8πG = 8π / m_P² ≈ 25.13 / m_P²
λ₄ / (8πG) = 1/48  (exact)                                    (114.10) [PDTP Original]

E_break = √(24K) = √(6/π) m_P ≈ 1.382 m_P ≈ 1.69×10¹⁹ GeV
contact-term size at E = 10 TeV: ≈ 3.5×10⁻³¹
```

**Result (114.10):** the non-GR contact interaction is Planck-suppressed —
a factor **1/48 below** the graviton self-coupling at any given energy. It
becomes O(1) only at E ≈ 1.38 m_P, the same scale where the condensate
EFT itself dissolves (healing length). GR recovery at first nonlinear
order therefore **survives at all accessible energies**.

**Plain English:** yes, PDTP's spacetime has an extra self-interaction
Einstein's theory doesn't have — but it is 48 times weaker than gravity's
own nonlinearity and only matters at the Planck scale. At LHC energies its
effect is ~10⁻³¹: forty-eight times weaker than something already
unmeasurably small. Einstein's equations survive intact everywhere we can
ever measure.

---

## 9. Sudoku Scorecard — 14/14 PASS

| # | Check | Computed | Expected | Pass |
|---|-------|----------|----------|------|
| NV-S1 | g⁽²⁾ recovers Eq. 75.1 | residual 0 | 0 | PASS |
| NV-S2 | g⁽³⁾ vanishes identically | 0 | 0 | PASS |
| NV-S3 | g⁽⁴⁾ = (1/12)Tr([A,B][A,C]) | 1/12, res 0 | 1/12 | PASS |
| NV-S4 | g⁽⁴⁾ = −(1/24) f f χ∂χχ∂χ | −1/24, res 0 | −1/24 | PASS |
| NV-S5 | g⁽⁴⁾ symmetric μ↔ν | sym | sym | PASS |
| NV-S6 | Casimir Σff = 3δ | 3 | 3 | PASS |
| NV-S7 | Lagrangian quartic = (1/12)Tr([A,B]²) | match | match | PASS |
| NV-S8 | SU(2) coefficient = −1/24 (group-indep.) | −1/24 | −1/24 | PASS |
| NV-S9 | SU(2) vertex = Weinberg L₄π (anchor) | residual 0 | match | PASS |
| NV-S10 | U(1) limit: ε⁴ vertex = 0 | 0 | 0 | PASS |
| NV-S11 | vertex derivative degree D = 2 | 2 | 2 | PASS |
| NV-S12 | D mismatch vs EH (2 vs 4,6) → no-go | 2 vs 4,6 | 2 vs 4,6 | PASS |
| NV-S13 | λ₄/(8πG) = 1/48 | 0.02083 | 0.02083 | PASS |
| NV-S14 | E_break = √(6/π) m_P | 1.3820 | 1.3820 | PASS |

All scorecard values are read from computed step outputs (RECHECK rule);
the closed-form coefficients are *solved for* from one probe monomial and
then *verified* by full polynomial subtraction (residual = 0).

---

## 10. Verdict and Status Changes

**Part 76g OPEN item ("full nonlinear equivalence") — RESOLVED:**
CONSTRUCTIVE NEGATIVE + PRODUCTIVE.

1. **(114.4) [DERIVED]** exact quartic vertex, coefficient −1/24
   (upgrades 76g.1).
2. **(114.2) [DERIVED]** no cubic term — metric expansion is even in ε.
3. **(114.6) [DERIVED]** Trace Theorem: tree level carries no graviton
   dynamics; Sakharov 1-loop is the *unique* source — Part 74/75's route
   is forced, not chosen.
4. **(114.7) [VERIFIED]** external anchor: SU(2) reduction = Weinberg's
   1966 ππ vertex, exactly.
5. **(114.9) [DERIVED, NEGATIVE]** no-go: the tree vertex can never be
   the EH vertex (derivative grading 2 vs 4/6).
6. **(114.10) [PDTP Original]** the non-GR contact term is
   Planck-suppressed (1/48 of graviton self-coupling); GR recovery at
   first nonlinear order survives below m_P. In-principle falsifiable
   distinction from GR, but only at Planckian energies — same class as
   the PSD constraint (75.6).

**Independence argument (Sudoku rules 3–5):** the vertex vanishes in the
U(1) limit, so the Standard-Model-facing and two-phase results (Parts
61–63: Newton's 3rd law, biharmonic equation, Jeans instability) and all
Newton's-law derivations are provably unaffected. The SU(3) sector
results (Parts 37–41, 75–76) acquire one new exact equation and no
contradictions.

**What remains open (unchanged by Part 114):** N_eff = 6π in the Sakharov
coefficient; the 2-DOF deficit (8 fields vs 10 metric components);
m_cond underdetermined (κ = c²/(4πG) remains a free parameter — Part 29
through 78 verdict stands).

---

## 11. Sources

- **Source:** Weinberg (1966), "Pion scattering lengths", Phys. Rev. Lett. 17, 616
- **Source:** Scherer (2003), "Introduction to Chiral Perturbation Theory", Adv. Nucl. Phys. 27, 277 (arXiv: hep-ph/0210398)
- **Source:** Weinberg (1972), *Gravitation and Cosmology*, Ch. 10 (linearized GR)
- **Source:** Weinberg (1996), *The Quantum Theory of Fields*, Vol. II, Eq. 15.4.17 (Casimir identity)
- **Source:** DeWitt (1967), "Quantum theory of gravity II", Phys. Rev. 162, 1239 (graviton vertices)
- **Source:** Sakharov (1968), "Vacuum quantum fluctuations in curved space and the theory of gravitation", Sov. Phys. Dokl. 12, 1040
- **PDTP Original:** Eqs. 114.4 (exact vertex), 114.6 (trace theorem), 114.9 (no-go), 114.10 (Planck suppression ratio 1/48)

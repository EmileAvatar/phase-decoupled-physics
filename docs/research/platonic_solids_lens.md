# Platonic Solids Lens — Discrete Symmetry Constraints on PDTP

**Part:** 105 (Phase 73, TODO_04 T22)
**Script:** `simulations/solver/t22_platonic_lens.py`
**Status:** PARTIAL — 1 DERIVED (textbook), 3 NEGATIVE, 1 CATALOG
**SymPy:** 8/8 PASS | **Sudoku:** 10/10 PASS
**Date:** 2026-04-15

---

## Plain English Summary

We looked at the 5 Platonic solids (tetrahedron, cube, octahedron, dodecahedron,
icosahedron) and asked: does their discrete symmetry pin down any of the open
numbers in PDTP?

Four PDTP numbers we hoped to constrain:

| # | Number | What it is | Platonic lens result |
|---|---|---|---|
| 1 | `N_c = 3` | Number of colours (quarks per baryon) | **Derivable** (Z_3 center of SU(3); textbook) |
| 2 | `N_gen = 3` | Number of fermion generations | **NOT derivable** — no Platonic arithmetic gives 3 |
| 3 | `K_0 = 1/(4π)` | PDTP dimensionless coupling | **NOT from coordination number** — 4π is irrational, Z is integer |
| 4 | `Λ/M_P^4 ~ 10⁻¹²²` | Cosmological constant | **NOT from golden ratio** — off by >19 decades |

The most useful thing that came out of this: the lens **clearly separates two
questions that are often confused**. "Why are there 3 colours?" has an answer
(the Z_3 center of SU(3)). "Why are there 3 fermion generations?" does NOT have
an answer from discrete symmetry. They are different problems. Saying "well,
both are 3, so it's the same mechanism" is wrong — they have different origins.

The "re-examine negatives" checklist item (Methodology section 8) can close this
off: T22 was explicitly speculative going in, and four of its four new claims
failed. The lens confirms existing results (Part 37's N_c=3, Part 54's Λ as a
free parameter) but introduces no new free-parameter fixes.

---

## 1. Platonic Solid Inventory [Eq 105.1, DERIVED]

The five Platonic solids, verified to satisfy the Euler formula `V - E + F = 2`:

| Solid | V | E | F | Schläfli {p,q} | G_rot | ǀG_rotǀ | ǀG_fullǀ |
|---|---|---|---|---|---|---|---|
| Tetrahedron | 4 | 6 | 4 | {3,3} | A_4 | 12 | 24 |
| Cube | 8 | 12 | 6 | {4,3} | S_4 | 24 | 48 |
| Octahedron | 6 | 12 | 8 | {3,4} | S_4 | 24 | 48 |
| Dodecahedron | 20 | 30 | 12 | {5,3} | A_5 | 60 | 120 |
| Icosahedron | 12 | 30 | 20 | {3,5} | A_5 | 60 | 120 |

**Source:** Coxeter (1973), "Regular Polytopes" (Dover), Ch. 1.

Cube↔Octahedron and Dodecahedron↔Icosahedron are dual pairs (sharing groups).
So there are only **three distinct non-cyclic/non-dihedral finite subgroups of
SO(3)**: tetrahedral (A_4), octahedral (S_4), icosahedral (A_5).

**Plain English:** Five solids, but only three kinds of rotation groups. This
"3" will reappear.

---

## 2. McKay Correspondence [Eq 105.2, CATALOG]

Finite subgroups of SU(2) (the double cover of SO(3)) correspond one-to-one to
Dynkin diagrams of simply-laced Lie algebras (the ADE classification):

| SU(2) subgroup | Image in SO(3) | ǀGǀ | ADE Dynkin | Lie algebra dim |
|---|---|---|---|---|
| Z_n (cyclic) | n-gon (degen.) | n | A_{n-1} | n−1 |
| Dic_n (binary dihedral) | n-antiprism | 4n | D_{n+2} | n+2 |
| **2T** (binary tetrahedral) | Tetrahedron | 24 | **E_6** | 78 |
| **2O** (binary octahedral) | Cube/Octahedron | 48 | **E_7** | 133 |
| **2I** (binary icosahedral) | Dodec./Icosahedron | 120 | **E_8** | 248 |

**Source:** McKay, J. (1980), "Graphs, singularities, and finite groups,"
Proc. Symp. Pure Math. 37, 183–186.

The **three exceptional Lie algebras** (E_6, E_7, E_8) are in bijection with
the three non-cyclic/non-dihedral Platonic groups. This is the mathematical
content of McKay's theorem.

**Plain English:** There are exactly three "exceptional" Lie algebras in all of
mathematics — not a choice, but a theorem. Their existence is tied to the fact
that there are exactly three special kinds of rotation groups in 3D (tetrahedral,
octahedral, icosahedral).

---

## 3. Why N_c = 3: Z_3 Center of SU(3) [Eq 105.3, DERIVED]

The center of SU(N) — the elements commuting with everything — is `Z_N`:

$$
Z(\text{SU}(3)) = \{I, \omega I, \omega^2 I\},\qquad \omega = e^{2\pi i/3}
$$

**Step-by-step derivation of "3 quarks per baryon":**

1. A quark transforms in the fundamental 3-dim rep: `ψ → U ψ` with `U ∈ SU(3)`.
2. Under a Z_3 element `ω I`, a single quark picks up `ψ → ω ψ`.
3. A baryon is a Z_3-invariant 3-quark composite:
   $$
   B = \epsilon^{abc} \psi_a \psi_b \psi_c
   $$
   Under `ω I`: `B → ω³ B = B` (because `ω³ = 1`).
4. Mesons are quark-antiquark: `ψ̄ ψ → ω⁻¹ ω ψ̄ψ = ψ̄ψ`.
5. Both baryons and mesons are Z_3-invariant. Confinement requires Z_3-neutral
   composites, so baryons have exactly **N_c = 3** quarks.

**SymPy verification:** `omega³ = 1` exact (S2).

**Source:** Wilson, K.G. (1974), "Confinement of quarks," Phys. Rev. D 10, 2445;
Slansky, R. (1981), Phys. Rep. 79, 1–128.

**Plain English:** The only way for three copies of the same quark to cancel
out the Z_3 phase is if there are exactly three of them. That's why there are
three quarks in every baryon.

---

## 4. Y-Junction Energy: n=3 from Z_N, Not from Geometry [Eq 105.4, DERIVED]

Part 37 describes a Y-junction: 3 vortices meeting at 120° in a plane. **Does
the `n=3` come from force balance, or from the Z_3 center?**

**Setup:** n vortices of equal magnitude meeting at a point, lying in a plane
(cross-section of 1D vortex lines). Force balance:

$$
\sum_{k=0}^{n-1} \hat e_k = 0,\qquad \hat e_k = (\cos(2\pi k/n),\, \sin(2\pi k/n))
$$

This holds for **any n ≥ 3** (SymPy S4 verified for n=3,4,5,6,12). So planar
force balance does NOT select n=3.

**Energy per junction** (schematic, with total winding 1):

$$
E(n) = n \cdot w^2,\qquad w = \tfrac{1}{n} \ \Rightarrow\ E(n) = \tfrac{1}{n}
$$

| n | winding w | E(n) = n·w² |
|---|---|---|
| 2 | 0.500 | 0.500 |
| 3 | 0.333 | 0.333 |
| 4 | 0.250 | 0.250 |
| 5 | 0.200 | 0.200 |
| 12 | 0.083 | 0.083 |

Energy **monotonically decreases** with n. If only energy mattered, `n → ∞`
(continuous flux) would be preferred. So energy minimisation does NOT select
n=3 either.

**What actually selects n=3:** the topology of `SU(3)/Z_3`:

$$
\pi_1(\text{SU}(3)/Z_3) = Z_3
$$

Allowed vortex windings are quantized in units of `1/3`. For a Z_3-neutral
Y-junction with total winding `1`, we need exactly 3 vortices of winding `1/3`.

**Conclusion:** `n=3` is selected by the **group-theoretic Z_3 center**, not by
geometric force balance or energy. Platonic geometry plays **no causal role**
for this result.

- **Hypothesis ELIMINATED:** "n=3 from Platonic/geometric force balance"
- **Hypothesis CONFIRMED:** "n=3 from Z_3 center of SU(3)"

**Source:** Zinn-Justin, J. (2002) "Quantum Field Theory and Critical Phenomena,"
4th ed., Ch. 25 (homotopy and defects in gauge theories).

---

## 5. N_generations vs N_colors — REFRAME [Eq 105.7, NEGATIVE for N_gen]

The Standard Model has **3 fermion generations**: (e, ν_e, u, d), (μ, ν_μ, c, s),
(τ, ν_τ, t, b). Why 3?

**Existing arguments (all fail to uniquely fix 3):**

1. **Anomaly cancellation** — works for any N_gen ≥ 1.
2. **String compactification** — depends on Calabi-Yau Euler number; not unique.
3. **E_6 GUT 27 rep** — contains 3 copies of (15,1)+(6,2)+(1,3), but this is
   an assumption, not a derivation.
4. **Koide relation** — empirical fit; works for 3 but doesn't fix the number.

**Platonic-lens test:** does any arithmetic combination of Platonic group orders
give `3` exactly?

| Orders | Ratio | = 3? |
|---|---|---|
| ǀS_4ǀ / ǀA_4ǀ | 24/12 = 2 | No |
| ǀA_5ǀ / ǀA_4ǀ | 60/12 = 5 | No |
| ǀA_5ǀ / ǀS_4ǀ | 60/24 = 2.5 | No |
| ǀ2Iǀ / ǀA_5ǀ | 120/60 = 2 | No |

**No ratio of Platonic group orders equals 3.** The "3" of generations is not
encoded in the Platonic group data.

**Reframe (the useful part):**

| Quantity | Value | Origin |
|---|---|---|
| N_colors | 3 | **Z_3 center of SU(3)** [DERIVED] |
| N_generations | 3 | **Empirical** [OPEN] |
| # exceptional E groups | 3 | Math fact (E_6,E_7,E_8) |
| # non-cyclic Platonic groups | 3 | Math fact |

The four "3"s above are **NOT all the same 3**. N_c=3 has a derivation; N_gen=3
does not. The Platonic lens makes this distinction clean.

**Plain English:** People often say "there are 3 of everything — colours,
generations, spatial dimensions — so there must be a deep reason." But 3 colours
is a theorem, 3 generations is an observation, 3 exceptional Lie algebras is a
different theorem, and 3 spatial dimensions is something else entirely. The
Platonic lens shows these are unrelated.

---

## 6. Coordination Number → K_0 = 1/(4π)? [Eq 105.5, NEGATIVE]

Part 35 established `K_0 = 1/(4π) ≈ 0.0796` as the dimensionless PDTP coupling.
Does it have a geometric origin in a lattice coordination number `Z`?

| Lattice | Z | Z / (4π) | gap |
|---|---|---|---|
| Simple cubic | 6 | 0.47746 | 52.25% |
| Body-centered cubic | 8 | 0.63662 | 36.34% |
| **Face-centered cubic** | **12** | **0.95493** | **4.51%** |
| Hexagonal close-packed | 12 | 0.95493 | 4.51% |
| Diamond | 4 | 0.31831 | 68.17% |
| Icosahedral (quasi) | 12 | 0.95493 | 4.51% |

Best match: FCC/HCP/icosahedral at `Z=12`, gap 4.51%.

**Why this is fundamentally NEGATIVE:**

- `4π` is **irrational** (Lindemann 1882: π is transcendental).
- `Z` is **integer** (for any crystalline lattice).
- An irrational number cannot equal an integer. **Exact match is impossible.**

**What 4π actually is:** the solid angle of the unit sphere, a feature of 3D
isotropy, not of any specific lattice. `K_0 = 1/(4π)` comes from the Green's
function of the 3D Laplacian, not from a nearest-neighbor count.

**Source:** Ashcroft & Mermin (1976), "Solid State Physics," Ch. 4.

**Plain English:** We hoped that counting nearest neighbours on some lattice
would give `4π`. But `4π ≈ 12.566` is not an integer, and no crystal has 12.566
neighbours. The factor comes from the geometry of 3D space (the surface area of
a sphere), not from any lattice structure.

---

## 7. Icosahedral Z_5 → Cosmological Constant? [Eq 105.6, NEGATIVE]

Icosahedral `A_5` contains a `Z_5` cyclic subgroup (pentagonal rotations).
Penrose tilings and quasicrystals (Shechtman 1984) use 5-fold symmetry and the
golden ratio `φ = (1+√5)/2`. **Can `φ^n` for some natural n reproduce the
cosmological constant ratio?**

$$
\frac{\rho_\Lambda}{\rho_\text{Planck}} \approx 1.4 \times 10^{-123}
\quad\Leftrightarrow\quad \ln(\rho_\Lambda/\rho_\text{Planck}) \approx -283
$$

With `ln(φ) ≈ 0.4812`, the required exponent is `n ≈ -588` — clearly not a
standard integer from Platonic/ADE data.

**Test candidate n values from Platonic/ADE data:**

| Candidate | n | `ln(φ^-n)` | gap (decades) |
|---|---|---|---|
| V+E+F (icosa) | 62 | −29.8 | 110 |
| ǀA_5ǀ | 60 | −28.9 | 110 |
| ǀ2Iǀ | 120 | −57.8 | 98 |
| dim(E_6) | 78 | −37.5 | 107 |
| dim(E_7) | 133 | −64.0 | 95 |
| dim(E_8) | 248 | −119.3 | 71 |
| 2·dim(E_8) | 496 | −238.7 | **19** |
| ǀ2Iǀ²/24 | 600 | −288.7 | 2.5 |

**Best natural candidate** (`2·dim(E_8) = 496`) is still ~19 decades off.
The ad-hoc `ǀ2Iǀ²/24 = 600` fits to 2.5 decades but isn't a natural
group-theoretic number.

**Conclusion:** `Λ/M_P^4` is NOT a natural power of `φ`. The Z_5/Penrose
hypothesis does NOT resolve the cosmological constant problem. Λ remains a
free parameter (consistent with Part 54).

**Source:** Penrose, R. (1974), "The role of aesthetics in pure and applied
mathematics" (Penrose tilings); Shechtman et al. (1984), Phys. Rev. Lett. 53,
1951 (quasicrystals).

**Plain English:** If dark energy came from pentagonal quasicrystal structure,
we'd expect its tiny value to be `(golden ratio)^n` for some n we could
recognize. It isn't. Natural candidates fail by tens of decades.

---

## SymPy Verification (8/8 PASS)

| # | Check | Result |
|---|---|---|
| S1 | V − E + F = 2 for all 5 solids | PASS |
| S2 | ω³ = 1 for ω = exp(2πi/3) | PASS (= 1) |
| S3 | Σ ê_k = 0 at 120° (Part 37) | PASS (= (0,0)) |
| S4 | Σ ê_k = 0 for n=3,4,5,6,12 | PASS |
| S5 | φ² = φ + 1 (golden ratio) | PASS (residual 0) |
| S6 | Tet. bond angle cos = −1/3 (109.47°) | PASS |
| S7 | ǀ2Iǀ = 2·ǀA_5ǀ = 120 (SU(2) double cover) | PASS |
| S8 | 3 exceptional E groups (E_6, E_7, E_8) | PASS |

---

## Sudoku Consistency Check (10/10 PASS)

All 10 checks pass; details in script output
`outputs/t22_platonic_lens_*.txt`.

Highlights:
- S1–S2: Euler formula for tetrahedron and icosahedron (both = 2)
- S3: ǀ2Iǀ/ǀA_5ǀ = 2 (double-cover factor)
- S5: Y-junction energy E(n=3) = 1/3 (matches step 4)
- S6: ǀω³ − 1ǀ = 0 (Z_3 cube root)
- S7: Tetrahedral bond angle 109.4712° (matches arccos(−1/3))
- S8: Best Z/(4π) ≠ 1 (no exact match; FCC is 0.9949, 4.5% off)
- S10: log(Λ/M_P⁴)/log(φ) non-integer (|Δn| = 0.148, confirms NEGATIVE)

---

## Final Verdict

| Claim | Result | Tag |
|---|---|---|
| V − E + F = 2 | Verified for 5 solids | [DERIVED] |
| McKay ADE correspondence | Cataloged | [CATALOG] |
| N_c = 3 from Z_3 center | Derived (textbook) | [DERIVED] |
| Y-junction n=3 from Z_3 (not geometry) | Derived | [DERIVED] |
| N_gen = 3 from Platonic arithmetic | Fails (no ratio = 3) | [NEGATIVE] |
| K_0 = 1/(4π) from coordination Z | Fails (4π irrational) | [NEGATIVE] |
| Λ/M_P⁴ = φⁿ for natural n | Fails (>19 decades off) | [NEGATIVE] |

**Score:** 3 NEGATIVE, 2 DERIVED (textbook), 1 CATALOG.

**Outcome:** The Platonic lens confirms existing results (Part 37 N_c=3 via Z_3,
Part 54 Λ as free parameter) but fixes no new free parameter. The most useful
contribution is the **reframe**: N_c=3 and N_gen=3 are **different questions
with different answers**.

**Status:** PARTIAL. Expected going in (T22 was rated "most speculative" in the
T22-T24 priority table).

**What is NOT closed:**
- N_gen = 3 (open; needs non-discrete-symmetry input)
- Dimensional reasoning behind `4π` in `K_0` (geometry of 3D, not lattice)

---

## Open Questions / Further Work

1. **Non-discrete approaches to N_gen:** Since Platonic lens fails, what could
   fix N_gen = 3? Candidates:
   - Anomaly cancellation with hidden constraints (needs UV completion)
   - Topology of compactified extra dimensions (string-theoretic)
   - Koide-relation generalisation to baryons
2. **Λ from Part 61 two-phase dynamics:** Part 54 left Λ as a free parameter.
   The two-phase Lagrangian (Part 61) introduces `phi_-` which has different
   vacuum structure. Could `phi_-` condensate give the Λ scale? (Separate
   investigation; T23 Part 104 already touched this.)
3. **Revisit if SU(3) is enhanced:** if PDTP needs SU(5) or higher (GUT-like
   unification), its center `Z_5` would bring pentagonal/icosahedral symmetry
   back into play naturally.

---

## References

1. Coxeter, H.S.M. (1973), "Regular Polytopes," 3rd ed., Dover.
2. McKay, J. (1980), "Graphs, singularities, and finite groups," Proc. Symp.
   Pure Math. 37, 183–186.
3. **Part 37:** [SU(3) condensate extension](su3_condensate_extension.md).
4. **Part 35:** [Dimensional transmutation](dimensional_transmutation.md).
5. **Part 54:** [Cosmological constant FCC](cosmological_constant_fcc.md).
6. Slansky, R. (1981), "Group theory for unified model building," Phys. Rep.
   79, 1–128.
7. Penrose, R. (1974), "The role of aesthetics in pure and applied mathematics,"
   Bull. Inst. Math. Appl. 10, 266.
8. Shechtman, D. et al. (1984), Phys. Rev. Lett. 53, 1951 (quasicrystals).
9. Wilson, K.G. (1974), "Confinement of quarks," Phys. Rev. D 10, 2445.
10. Ashcroft, N.W. & Mermin, N.D. (1976), "Solid State Physics."
11. Zinn-Justin, J. (2002), "Quantum Field Theory and Critical Phenomena,"
    4th ed., Ch. 25.

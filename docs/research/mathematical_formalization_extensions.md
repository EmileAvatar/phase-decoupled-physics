# Mathematical Formalization — Structural Extensions

**Companion to:** [`mathematical_formalization.md`](mathematical_formalization.md)
(the foundations document — read that first; this file assumes its §§1–9).
**Purpose:** this file holds the two largest structural extensions to the
single-phase U(1) Lagrangian — the SU(3) extension (Part 37) and the
two-phase Lagrangian (Part 61) — kept in their own file per the project's
file-size convention (large additions go in a companion file with a link
back, not inline into the main doc) rather than bloating the main
document toward ~2000 lines. Closes TODO_04.md T65.
**Added:** 2026-09-26, Part 150.

Same standard as the main document throughout: every established result
is cited, every new result is marked **PDTP Original**, every derivation
is shown step by step, tagged `[ASSUMED]` / `[DERIVED]` / `[VERIFIED]` /
`[PDTP Original]`.

**Scope note:** this file stays at "foundations" depth — the two
structural extensions themselves, shown end-to-end. Results built *on
top of* these extensions (DM winding selection, Lambda-locking, CP
violation, the induced EDE quartic, the Koide-Z₃/tan mass relations, the
T80 gauging attempt, the T23 sin² term, the SU(3) emergent metric of
Parts 75–76) are cross-referenced at the end of each section, not
re-derived here — they already have their own complete research docs,
and duplicating them here would just re-create `equation_reference.md`
with different formatting (per CLAUDE.md's own rule for this document
family: the trigger for a new section is structural, not per-Part).

---

## Table of Contents

1. [SU(3) Extension (Part 37)](#1-su3-extension-part-37)
   - 1.1 [Motivation: From U(1) to SU(3)](#11-motivation-from-u1-to-su3)
   - 1.2 [The SU(3)-Extended Lagrangian](#12-the-su3-extended-lagrangian)
   - 1.3 [U(1) Limit Recovery](#13-u1-limit-recovery)
   - 1.4 [The Z₃ Center and Fractional Vortices](#14-the-z-center-and-fractional-vortices)
   - 1.5 [The 8 Gluons from Linearization](#15-the-8-gluons-from-linearization)
   - 1.6 [String Tension and the Casimir Factor](#16-string-tension-and-the-casimir-factor)
   - 1.7 [Baryon Y-Junction Energy](#17-baryon-y-junction-energy)
   - 1.8 [Summary and Cross-References](#18-summary-and-cross-references)
2. [Two-Phase Lagrangian (Part 61)](#2-two-phase-lagrangian-part-61)
   - 2.1 [Motivation: Adding Surface Tension](#21-motivation-adding-surface-tension)
   - 2.2 [The Lagrangian and the φ₊/φ₋ Change of Variables](#22-the-lagrangian-and-the-φφ-change-of-variables)
   - 2.3 [The Product-Coupling Trig Identity](#23-the-product-coupling-trig-identity)
   - 2.4 [Field Equations and Newton's 3rd Law](#24-field-equations-and-newtons-3rd-law)
   - 2.5 [Biharmonic Gravity](#25-biharmonic-gravity)
   - 2.6 [The φ₋ Mode: Reversed-Higgs Behavior](#26-the-φ-mode-reversed-higgs-behavior)
   - 2.7 [The 16/16 Re-derivation (Part 63)](#27-the-1616-re-derivation-part-63)
   - 2.8 [Summary and Cross-References](#28-summary-and-cross-references)
3. [References](#3-references)

---

## 1. SU(3) Extension (Part 37)

### 1.1 Motivation: From U(1) to SU(3)

The single-phase Lagrangian (main document §2) uses φ ∈ ℝ, a single real
phase angle — U(1) symmetry. This supports only *integer*-winding
vortices. But quarks require *fractional* winding (±1/3, Z₃ topology),
and QCD requires 8 independent gluon fields, matching the 8 generators
of SU(3). Neither can come from a U(1) scalar.

**Question:** can the PDTP Lagrangian be generalized from U(1) to SU(3)
so that quarks, gluons, and QCD's color structure emerge the same way
gravity emerged from the U(1) case — as phase-locking, not postulated?

**Source:** Griffiths, D. (2008), *Introduction to Elementary Particles*,
2nd ed., Wiley-VCH, Ch. 4 — SU(3) color symmetry, Gell-Mann matrices.

### 1.2 The SU(3)-Extended Lagrangian

**PDTP Original.** Replace the real scalar φ with a 3×3 SU(3) matrix
field U(x) — a unitary matrix (`U†U=1`) with `det(U)=1` (the "special"
in Special Unitary). Replace each real matter phase ψᵢ with a matrix
field Ψᵢ(x), also SU(3)-valued:

```
Single-phase (U(1)):
  L = (1/2)(d_mu phi)(d^mu phi) + Sum_i (1/2)(d_mu psi_i)(d^mu psi_i)
      + Sum_i g_i cos(psi_i - phi)
  phi in R                                          [ASSUMED, main doc S2]

SU(3) extension:
  L = K Tr[(d_mu U^dag)(d^mu U)] + Sum_i K_i Tr[(d_mu Psi_i^dag)(d^mu Psi_i)]
      + Sum_i g_i Re[Tr(Psi_i^dag U)] / 3
  U(x) in SU(3)     (spacetime condensate field, 3x3 unitary, det=1)
  Psi_i(x) in SU(3) (matter field for particle i)
                                            [PDTP Original, Part 37]
```

The physical idea is unchanged — phase locking between matter and
spacetime — only the phase is now a matrix rather than a number.

**The coupling is the Wilson loop action.** `Re[Tr(Ψ†U)]/N` is exactly
the fundamental action of lattice gauge theory (the Wilson plaquette
action `S_W = Re[Tr(U_plaquette)]/N`) — not a coincidence: PDTP's
"minimize phase mismatch between matter and condensate" principle, in
the matrix-valued case, produces the same form Wilson postulated
directly as the gauge action.

**Source:** Wilson, K.G. (1974), "Confinement of quarks," *Physical
Review D* 10, 2445 — Wilson action, Eq. (2.10).

### 1.3 U(1) Limit Recovery

**PDTP Original, DERIVED.** The extended Lagrangian must reduce to the
single-phase form exactly at `N=1`. Setting `U(x)=e^{iφ(x)}` (a 1×1
"matrix" — a plain complex number of unit modulus) and
`Ψ(x)=e^{iψ(x)}`:

```
Psi^dag * U = e^{-i*psi} * e^{i*phi} = e^{i*(phi-psi)}
Tr(Psi^dag U) = e^{i*(phi-psi)}                 [trace of a 1x1 matrix = itself]
Re[Tr(Psi^dag U)] / 1 = cos(phi - psi) = cos(psi - phi)          (150.1)
                                        [DERIVED, exact -- SymPy S3, su3_condensate.py]
```

**Numerically verified** at four test angles (θ=0, 0.7, π/2, π): exact
match at machine precision in every case (`su3_condensate_extension.md`
§4.2). **This confirms the SU(3) Lagrangian is a genuine generalization**
of the single-phase Lagrangian, not a different theory that happens to
resemble it — every single-phase result derived in the main document
survives unchanged in the `N=1` sector.

### 1.4 The Z₃ Center and Fractional Vortices

**The center of SU(3)** is the set of elements commuting with every
group element:

```
Z_3 = { I, omega*I, omega^2*I },   omega = e^{2*pi*i/3}          [KNOWN]
```

— the only scalar multiples of the identity in SU(3) (`det(ωI)=ω³=1`
confirms these are legitimate SU(3) elements), three elements at 0°,
120°, 240°.

**Source:** Ramond, P. (2010), *Group Theory*, Cambridge, Ch. 10;
Greensite, J. (2011), *An Introduction to the Confinement Problem*,
Springer, Ch. 4 & 6 — Z₃ center symmetry, center vortices.

**A vortex where `U(x)` winds once around the Z₃ center** carries
fractional topological charge **1/3** — this is the Z₃ vortex, PDTP's
candidate for the quark. Unlike an ordinary U(1) vortex (integer
winding, can unwind continuously to nothing), a Z₃ vortex is
topologically protected: `Z₃` is discrete, so no smooth deformation of
`U(x)` changes the winding number — it can only be removed by an
anti-vortex of winding `−1/3`. **Three Z₃ vortices sum to integer
winding 1** (stable); one alone cannot unwind but also cannot exist as
an isolated stable integer-winding object — exactly matching QCD's
observation that isolated quarks are never seen, only groups of three
(baryons) or quark-antiquark pairs (mesons).

**Vortex energy [PDTP Original, DERIVED]:** using the line-energy
formula from the U(1) vortex case (`E/L = 2πK ln(R/ξ)`, main document's
vortex-winding prerequisite) with winding `1/N`:

```
E_Z3 / L = 2*pi*K*(1/N)^2 * ln(R/xi)                                (150.2)
For N=3:  E_Z3/L = 2*pi*K*(1/9)*ln(R/xi) = E_U1/9        [DERIVED]
Three Z3 vortices together: 3 * E_Z3/L = E_U1/3                     (150.3)
```

Three Z₃ vortices together carry **1/3 the energy of a single U(1)
vortex** — energetically preferred *and* topologically required to
group in threes. This is PDTP's proposed microscopic origin of the
three-quark baryon structure: not imposed, but forced by the Z₃
topology of the extended Lagrangian.

> **Correction — Part 158 (T83e, CLAUDE OPUS 5.5, 2026-10-17).** Three
> statements above do not hold, and Eq. 150.2–150.3 are withdrawn:
> 1. **No protected Z₃ vortices in this Lagrangian.** π₁(SU(3)) = 0. A
>    Z₃ vortex needs the target SU(3)/Z₃ (π₁ = Z₃), i.e. U and ωU must be
>    physically identical. The coupling Re Tr(Ψ†U) changes under U → ωU,
>    so they are not.
> 2. **The energy is 2/9, not 1/9** (conditional on a Z₃-invariant
>    target). Winding "1/N" of one overall phase, e^{iθ/3}I, has
>    det = e^{iθ} ≠ 1. The cheapest SU(3) path to ωI is
>    X = diag(1/3, 1/3, −2/3) with Tr Q² = 2/3, and E/L = 2πK Tr(Q²) ln(R/ξ).
> 3. **Three Z₃ units fuse to the trivial class** (1+1+1 ≡ 0 mod 3), not
>    "integer winding 1". This *permits* the baryon Y-junction (§1.7),
>    whose 120° force balance stands.
>
> ```
> E_Z3/L = 2*pi*K*Tr(X_min^2)*ln(R/xi),  Tr(X_min^2) = 2/3
> E_Z3/E_ref(Tr=3) = 2/9   [DERIVED, CONDITIONAL on SU(3)/Z_3 target]   (158.7)
> ```
>
> $$
> \frac{E_{Z_3}}{E_{\rm ref}} = \frac{2}{9} \quad \text{(conditional on an } SU(3)/\mathbb{Z}_3 \text{ target)}
> $$
>
> Three alternative postulates that would supply the Z₃-invariant target
> (B adjoint coupling, which loses the U(1) limit; C co-rotating matter
> as a discrete gauge redundancy; D U(3) target, which adds an extra
> massless mode) are kept open as TODO_05 T85. See
> [su3_z3_target_audit.md](su3_z3_target_audit.md).

### 1.5 The 8 Gluons from Linearization

In the ordered ground state, `U=I` (the identity matrix) everywhere.
Small fluctuations are parameterized by 8 small real fields `δAᵃ(x)`:

```
U(x) ~ I + i * Sum_a delta_A^a(x) * T^a           (small delta_A^a)     (150.4)
```

where `Tᵃ` (`a=1,...,8`) are the **8 Gell-Mann matrices** — the
generators of SU(3), satisfying `Tr(TᵃTᵇ)=δᵃᵇ/2`.

**Source:** Gell-Mann, M. (1962), "Symmetries of Baryons and Mesons,"
*Physical Review* 125, 1067.

**[DERIVED]** Substituting into the kinetic term at linear order:

```
K*Tr[(d_mu U^dag)(d^mu U)] ~ K * Sum_a (d_mu delta_A^a)(d^mu delta_A^a)   (150.5)
                                              [using Tr(T^a T^b)=delta^ab/2]
```

The 8 fields `δAᵃ` are canonically normalized, massless, and propagate
at speed `c` — **exactly the 8 gluons, not put in by hand but falling
out automatically from the 8 generators of SU(3)**. In the U(1) case
the phase field `φ` does not self-interact; here, because Gell-Mann
matrices don't commute (`[Tᵃ,Tᵇ]≠0`), the `δAᵃ` fields interact with
each other — the origin, in this construction, of QCD's 3-gluon and
4-gluon vertices.

**Source:** Creutz, M. (1983), *Quarks, Gluons, and Lattices*,
Cambridge, Ch. 3.

### 1.6 String Tension and the Casimir Factor

**[DERIVED, PDTP Original]** In SU(N) gauge theory the string tension
between fundamental-representation sources (quarks) scales with the
**fundamental Casimir invariant** `C₂(fund) = (N²−1)/(2N)`:

```
sigma_SU(N) = C_2(fund) * sigma_reference                             (150.6)
For SU(3): C_2(fund) = 8/6 = 4/3                                      (150.7)
```

**Source:** Greensite (2011), Ch. 5 — Casimir scaling of string tensions.

Applied to PDTP's earlier U(1) dimensional estimate
(`σ_U1 ≈ Λ_QCD² = 0.04 GeV²`, from the vortex-winding prerequisite
material):

```
sigma_SU3 = (4/3) * 0.04 GeV^2 = 0.053 GeV^2                          (150.8)
vs measured sigma_QCD = 0.18 GeV^2 (PDG)  ->  factor 3.4 off          [PDTP Original]
```

An improvement over the plain U(1) estimate's factor-4.5 mismatch, but
not a full match — the remaining gap needs the non-Abelian gluon
self-coupling (3- and 4-gluon vertices, §1.5), which is exactly why
lattice QCD, not perturbation theory, is required for the Standard
Model's own exact string tension. **Inverting this relation** to infer
`m_cond` for the QCD sector from the *measured* string tension (no free
parameter adjustment):

```
m_cond_SU3 = sqrt(sigma_measured / C_2(fund)) = sqrt(0.18/(4/3))
           = sqrt(0.135) = 0.367 GeV = 367 MeV                        (150.9)
vs Lambda_QCD = 200 MeV  ->  factor 1.8                    [PDTP Original]
```

Within a factor of 2 of the QCD scale, with no adjustable parameter —
an honest order-of-magnitude success, not an exact match.

### 1.7 Baryon Y-Junction Energy

A baryon (three quarks = three Z₃ vortices) meets at a central junction,
each vortex pulling with string tension `σ` along its own axis.

**Source:** Cornwall, J.M. (1996), *Physical Review D* 54, 6527;
Takahashi, T.T. et al. (2002), *Physical Review D* 65, 114509 — Y-type
baryon flux tube, predicted then confirmed on the lattice.

**[DERIVED]** Force balance at the junction requires:

```
sigma * (e_1_hat + e_2_hat + e_3_hat) = 0                             (150.10)
```

With all three tensions equal, the unique symmetric solution places the
three unit vectors at **120° from each other**:

```
e_1 = (1,0),  e_2 = (-1/2, sqrt(3)/2),  e_3 = (-1/2, -sqrt(3)/2)
e_1 + e_2 + e_3 = (0,0)                                     [VERIFIED, exact]
```

This is the classical **Steiner (Fermat/Torricelli) point** of a
triangle. **The 120° angle is not assumed — it is the unique
equilibrium**, following from force balance among three *equal*
tensions, which in turn follows from all three flux tubes being made of
the same Z₃-vortex stuff. Chain of consequence, none individually
imposed: Z₃ topology → fractional winding (§1.4) → three-fold grouping
required for integer winding → equal tensions → 120° junction.

**Source:** Steiner, J. (1837) — the geometric statement.

### 1.8 Summary and Cross-References

| Result | Tag | Eq. |
|---|---|---|
| Extended Lagrangian, matrix field U(x) ∈ SU(3) | [PDTP Original] | §1.2 |
| U(1) limit recovery, exact | [DERIVED] | 150.1 |
| ~~Z₃ vortex energy = 1/9 of U(1) per quark~~ | WITHDRAWN (Part 158): no protected Z₃ vortex in this Lagrangian; 2/9 if the target is made Z₃-invariant | 150.2–150.3 → 158.7 |
| 8 gluons from 8 Gell-Mann generators | [DERIVED] | 150.4–150.5 |
| String tension via Casimir factor, 3.4× off measured | [PDTP Original] | 150.6–150.8 |
| m_cond(QCD) = 367 MeV, 1.8× off Λ_QCD | [PDTP Original] | 150.9 |
| Y-junction 120°, unique force-balance equilibrium | [DERIVED] | 150.10 |

**Cross-references, not re-derived here:** the SU(3) emergent metric
(`g_μν = Tr[(∂_μU†)(∂_νU)]`, Parts 75–76, `su3_tensor_metric.md`) — a
separate structural extension building on this one, candidate for a
future §3 of this file if wanted; the Trace Theorem (Part 114,
`su3_nonlinear_vertex.md`) proving Sakharov 1-loop is gravity's unique
dynamical source; the NLSM classification of the 8 gluon-analog fields
as scalars, not gauge bosons (T70/Part 140); the T80 gauging attempt
that independently confirmed no vector gauge field exists in PDTP's own
Lagrangian (`em_from_geometry_gauging.md`); the Koide-Z₃ lepton mass
relation built on this same center symmetry (Part 53,
`koide_z3_derivation.md`, and its master-formula generalization Part
122, `koide_tan.md`).

---

## 2. Two-Phase Lagrangian (Part 61)

### 2.1 Motivation: Adding Surface Tension

The single-phase Lagrangian has one matter-spacetime coupling: `+g·cos`,
attractive (gravity). **Question:** does adding a *second*, oppositely-
signed coupling — a `−cos` term, representing surface tension — reveal
new structure, the way adding surface tension to a soap film changes its
equilibrium shape without changing the underlying fluid mechanics?

**PDTP Original.** Split the single spacetime phase φ into a **bulk**
phase `φ_b` (couples with `+cos`, gravity-like) and a **surface** phase
`φ_s` (couples with `−cos`, surface-tension-like):

```
L = (1/2)(d_mu phi_b)^2 + (1/2)(d_mu phi_s)^2 + (1/2)(d_mu psi)^2
    + g*cos(psi - phi_b) - g*cos(psi - phi_s)          [PDTP Original, Part 61]
```

### 2.2 The Lagrangian and the φ₊/φ₋ Change of Variables

**[DERIVED]** Define the sum and difference modes:

```
phi_+ = (phi_b + phi_s) / 2      (gravity mode)                     (150.11)
phi_- = (phi_b - phi_s) / 2      (surface mode)                     (150.12)
```

so that `φ_b = φ₊+φ₋`, `φ_s = φ₊−φ₋`. `φ₊` behaves like the original
single-phase field; `φ₋` is genuinely new — it did not exist in the
single-phase Lagrangian at all.

### 2.3 The Product-Coupling Trig Identity

**[DERIVED, SymPy-verified]** Rewrite the coupling difference using the
standard sum-to-product identity:

```
cos(A) - cos(B) = -2*sin((A+B)/2)*sin((A-B)/2)          [KNOWN identity]
```

**Source:** Abramowitz, M. and Stegun, I.A. (1964), *Handbook of
Mathematical Functions*, eq. 4.3.37.

Applied with `A = ψ−φ_b`, `B = ψ−φ_s`:

```
(A+B)/2 = psi - (phi_b+phi_s)/2 = psi - phi_+
(A-B)/2 = -(phi_b-phi_s)/2 = -phi_-
```

so:

```
cos(psi-phi_b) - cos(psi-phi_s) = -2*sin(psi-phi_+)*sin(-phi_-)
                                 = 2*sin(psi-phi_+)*sin(phi_-)         (150.13)
                                                              [DERIVED, exact]
```

**Result:** the two-phase Lagrangian's coupling term is exactly a
**product** of two sines — one carrying the gravity-like dynamics
(`sin(ψ−φ₊)`), one carrying the new surface mode (`sin(φ₋)`). This
product structure is the source of everything new in this section: when
`φ₋` sits at its own equilibrium, it acts as a *multiplicative*
modulator of the gravity coupling — not an additive correction.

### 2.4 Field Equations and Newton's 3rd Law

**[DERIVED, SymPy-verified, Part 61 §Eq. 2f / Part 63 S3]** Euler-Lagrange
applied to the spatially-uniform (particle-mechanics) limit gives
coupled equations for `ψ`, `φ₊`, `φ₋`; extracting the `ψ`/`φ₊` pair (the
gravitationally relevant sector):

```
psi_ddot = -2 * phi_+_ddot                                            (150.14)
                                  [DERIVED, PDTP Original, Part 61 -- CORRECTED
                                   in Part 63: an earlier draft had factor 1]
```

**Plain English:** this is PDTP's own derivation of Newton's third law —
matter's phase acceleration and spacetime's phase acceleration are
exactly opposite, not by assumption but as a consequence of the
Lagrangian's own symmetry. **The factor is 2, not 1** — a real,
SymPy-caught correction from the original Part 61 draft. (**Corrected
Part 156:** this factor reflects defining φ₊ as the *average* of φ_b and
φ_s — it is 1 for Σ = φ_b + φ_s — and is *not* the origin of
`G_eff = 2·G_bare`, which comes from the coherent 2g coupling divided by
φ₊'s stiffness 2; see `geff_factor_audit.md`.)

> **CORRECTED 2026-09-28 (Part 154, TODO_04 T83b — CLAUDE OPUS 5.5):** the Jeans
> eigenvalue is **±√3·g**, not ±2√2·g. The old value used forces as
> accelerations for φ₊/φ₋, whose inertia is 2 (kinetic term φ̇₊² + φ̇₋²);
> consistent inertias give M = [[0, 3g], [g, 0]]. Sign (instability) unchanged;
> magnitude × √6/4 ≈ 0.612, k_J × 0.7825. Values below are the corrected ones.
> Full derivation: [jeans_eigenvalue_correction.md](jeans_eigenvalue_correction.md).

**Jeans instability [DERIVED]:** in the spatially-uniform (k=0) limit,
the coupled `(Φ,φ₋)` system has the matrix form:

```
d^2/dt^2 [Phi; phi_-] = M [Phi; phi_-],   M = [[0, 3g],[g, 0]]        (150.15)
Characteristic equation: lambda^2 - 3*g^2 = 0
Eigenvalues: lambda = +/- sqrt(3)*g                                  (150.16)
```

`λ₁=+√3g>0`: an unstable (exponentially growing) mode — gravitational
collapse, falling directly out of the Lagrangian rather than assumed.
`λ₂=−√3g<0`: an oscillatory mode at `ω=√(√3g)` — this is the
**breathing mode**, and it is `φ₋` itself (§2.6).

### 2.5 Biharmonic Gravity

**[DERIVED, Part 61]** Promoting the `(Φ,φ₋)` system from the
spatially-uniform ODE (Eq. 150.15) to the full field PDE and eliminating
`φ₋` between the two coupled equations gives a single fourth-order
equation for the gravitational potential:

```
nabla^4(phi_+) - g^2*phi_+ = -g^2*psi                                 (150.17)
                   [DERIVED, PDTP Original, Part 61; corrected Part 155]
```

> **CORRECTED 2026-09-28 (Part 155, TODO_04 T83c — CLAUDE OPUS 5.5):** the
> two-phase static equation is **∇⁴φ₊ − g²φ₊ = −g²ψ**, not ∇⁴Φ + 4g²Φ = source
> (three slips: inertia 1 instead of 2 for φ₊/φ₋, static sign, and an algebra
> sign error in the final rearrangement). Its Green's function
> (cos(κr) − e^{−κr})/(8πκ²r), κ = √g = 1/a₀, has **no 1/r term at any range**
> (constant − r/8π inside a₀; cos(r/a₀)/r ripple outside). It does not reduce to
> Poisson/Newton at short range. Scale a₀/√2 → a₀. Full derivation:
> [biharmonic_rederivation.md](biharmonic_rederivation.md).

— fourth order in spatial derivatives, not the ordinary second-order
Poisson equation. **The full field-elimination steps are not reproduced
here** (this document's scope is the structural result and its role in
the framework, not a re-typing of `two_phase_lagrangian.py`'s own
algebra) — see that script and `equation_reference.md` §2e for the
complete derivation; the coupled system (Eq. 150.15) and its consistent
`ω²=c²k²±√3g` dispersion relation (main-doc-adjacent result, Part 61)
are the load-bearing pieces reproduced here as directly-verifiable
supporting structure.

**Consequence, already explored elsewhere and cross-referenced, not
re-derived here:** the biharmonic Green's function has a dramatically
different short-range behavior than `1/r` — this is exactly the
mechanism T77/Part 145 and T81/Part 146 (this project's most recent
MOND-related work) tested and found insufficient at galactic scale by
~54 orders of magnitude (`dark_matter_energy.md` §2.5, corrected
2026-09-14).

### 2.6 The φ₋ Mode: Reversed-Higgs Behavior

**[DERIVED, Part 62]** Solving for `φ₋`'s own mass near a matter source
(density coupled through `Φ`):

```
m_phi_minus^2 = g*Phi                    (near matter)              (150.18)
m_phi_minus^2 = 0                          (in vacuum, Phi=0)         (150.19)
                                    [DERIVED, PDTP Original, Part 62]
```

**Plain English — why "reversed Higgs":** the ordinary Standard Model
Higgs field is massive essentially everywhere in the physical vacuum
(that mass, ~125 GeV, is what makes it a genuine particle) and would
only become massless at the unstable, symmetric point of its potential.
`φ₋` is the **opposite pattern**: massless in the true vacuum (`Φ=0`,
far from any matter), and only acquires mass *near* matter sources. This
naming is a **structural analogy about the mass-generation pattern**,
not a claim that `φ₋` is a candidate for the Standard Model's actual
electroweak Higgs field — `Φ` here is PDTP's own Newtonian gravitational
potential, and `φ₋` is a mode of the gravity-sector two-phase Lagrangian,
with no connection to `SU(2)×U(1)` electroweak symmetry breaking. (This
distinction was independently re-confirmed and stated explicitly during
T79 Phase 2's audit of the "theory of everything" master equation, Part
149, precisely to prevent this natural naming-driven misreading.)

### 2.7 The 16/16 Re-derivation (Part 63)

**[VERIFIED]** Part 63 (`two_phase_rederivation.md`) systematically
re-derived all 16 previously-established single-phase results inside the
two-phase framework, to confirm the extension doesn't silently break
anything already proven. **The key mechanism enabling this:** at the
equilibrium point `φ₋=π/2`, defining `χ=φ₊+π/2`, the field equation for
`χ` becomes *identical in form* to the original single-phase equation
`φ̈=g·sin(ψ−φ)` — the equilibrium shift is a relabeling of the origin,
not new physics, and every single-phase result (Newton's 1st/2nd law,
the `1/r` potential, `G=ℏc/m_cond²`, `n=m_cond/m`, PPN `γ=β=1`, Hawking
temperature, the double-pulsar test, tensor GW propagation, the SU(3)
Wilson action, string tension, Koide `Q=2/3`, dark-energy `w(z)`) maps
through this substitution and passes unchanged.

**Score: 16/16 PASS** (`two_phase_rederivation.md` §"Scorecard").

### 2.8 Summary and Cross-References

| Result | Tag | Eq. |
|---|---|---|
| Two-phase Lagrangian, φ_b/φ_s split | [PDTP Original] | §2.1 |
| φ₊/φ₋ change of variables | [DERIVED] | 150.11–150.12 |
| Product-coupling identity `2·sin(ψ−φ₊)·sin(φ₋)` | [DERIVED] | 150.13 |
| Newton's 3rd law, factor 2 (corrected) | [DERIVED] | 150.14 |
| Jeans instability eigenvalues `±√3g` | [DERIVED] | 150.15–150.16 |
| Biharmonic `∇⁴φ₊−g²φ₊=−g²ψ` (corrected Part 155) | [DERIVED] | 150.17 |
| φ₋ reversed-Higgs mass, `2gΦ` near matter / `0` in vacuum | [DERIVED] | 150.18–150.19 |
| 16/16 single-phase results re-derived | [VERIFIED] | §2.7 |

**Cross-references, not re-derived here:** the induced EDE quartic at
partial lock (Part 117, `phi_minus_quartic.py`); DM winding selection
via the `n=1` vortex (Part 116, `dm_winding_selection.md`); Λ as a
locking fossil / causal-sync coefficient (Parts 119, 123); the sin²
second-harmonic extension explored and explicitly shelved (T23/Part 104,
`sin2_hilbert_term.md`); the Koide-tan master formula built on the same
Z₃ machinery as §1.4 (Part 122, `koide_tan.md`); T81's kinematic
phase-coherence MOND retry, which explicitly operates on the
single-body-summed source term and does not touch the φ₊/φ₋ structure
here (`kinematic_coherence_mond_retry.md`).

---

## 3. References

**Source:** Griffiths, D. (2008), *Introduction to Elementary Particles*,
2nd ed., Wiley-VCH, Ch. 4.
**Source:** Wilson, K.G. (1974), "Confinement of quarks," *Physical
Review D* 10, 2445.
**Source:** Ramond, P. (2010), *Group Theory*, Cambridge, Ch. 10.
**Source:** Greensite, J. (2011), *An Introduction to the Confinement
Problem*, Springer, Ch. 4–6.
**Source:** Gell-Mann, M. (1962), "Symmetries of Baryons and Mesons,"
*Physical Review* 125, 1067.
**Source:** Creutz, M. (1983), *Quarks, Gluons, and Lattices*, Cambridge, Ch. 3.
**Source:** Cornwall, J.M. (1996), *Physical Review D* 54, 6527.
**Source:** Takahashi, T.T. et al. (2002), *Physical Review D* 65, 114509.
**Source:** Steiner, J. (1837) — Steiner/Fermat point.
**Source:** Abramowitz, M. and Stegun, I.A. (1964), *Handbook of
Mathematical Functions*, eq. 4.3.37.
**Source:** Particle Data Group (2022), "Review of Particle Physics,"
*Progress of Theoretical and Experimental Physics* 2022, 083C01.

**PDTP Originals in this document:** the extended Lagrangian (§1.2), the
Z₃ vortex energy result (§1.6, Eq. 150.2–150.3; withdrawn by Part 158), the Casimir-corrected
string tension and inferred `m_cond` (§1.6, Eq. 150.6–150.9), the
two-phase Lagrangian and its φ₊/φ₋ split (§2.1–2.2), Newton's 3rd law
correction (§2.4, Eq. 150.14), biharmonic gravity (§2.5, Eq. 150.17),
and the φ₋ reversed-Higgs mass formula (§2.6, Eq. 150.18–150.19) — all
reused from their original Parts (37, 61–63), not re-derived from
scratch; this document's own new contribution is the narrative,
step-by-step presentation connecting them, matching the main document's
existing pedagogical standard.

---

*This document is part of the PDTP research series — companion to
[`mathematical_formalization.md`](mathematical_formalization.md). See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*

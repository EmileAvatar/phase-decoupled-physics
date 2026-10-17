# SU(3) Z₃ Target-Space Audit (Part 158)

**TODO:** TODO_04.md T83, sub-task **83e**. Worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-10-17.
**Script:** `simulations/solver/t83e_z3_target.py`
**Log:** `simulations/solver/outputs/t83e_z3_target_<timestamp>.txt`
**Scorecard:** 15 matches, 5 contradictions out of 20 tests. The
contradictions are exactly the four Part 37 claims that fail, plus the one
cost of alternative B.
**Status:** DOWNGRADED (option A, user-approved 2026-10-17). As written,
the Part 37 SU(3) Lagrangian **does not support topologically stable Z₃
vortices**. The "1/9 per vortex" energy is **wrong even if that is fixed**
(the correct conditional value is 2/9). "Three Z₃ vortices = winding 1"
is **wrong group arithmetic**: they fuse to the trivial class, and that
is what *permits* the Y-junction. Three ways to supply a Z₃-invariant
target are kept as **alternative postulates B, C, D** (§3), each with its
gains and costs, for future work (TODO_05 T85).

---

## Plain-English Summary

**What a "topological" vortex needs.** A vortex is a whirlpool in a
field. It is *topologically protected* (it can't simply untwist and
vanish) only if the field's possible values contain a loop that can't
be shrunk to a point, like a rubber band around a pole. Mathematicians
count such loops with π₁ (the "fundamental group").

**The problem.** In Part 37's SU(3) extension, the condensate U is an
SU(3) matrix, and SU(3) has **no** unshrinkable loops (π₁(SU(3)) = 0).
The ⅓-twist "quark" vortices would need the three special "center"
matrices 1, ω·1, ω²·1 (ω = e^{2πi/3}) to count as *the same physical
state*. Then a path from 1 to ω·1 would be a closed loop. That holds
only if nothing in the Lagrangian can tell 1 and ω·1 apart. But the
locking term Re Tr(Ψ†U) **can** tell them apart: it changes when U → ωU.
So the quark vortices are not protected. They are not stable solutions
of the Lagrangian as written.

**Two more slips found.**
1. **The "1/9 of the energy" figure** used the twist e^{iθ/3}·1. That is
   not an SU(3) matrix (its determinant isn't 1). The cheapest legal ⅓-twist
   costs **2/9**, twice as much.
2. **"⅓ + ⅓ + ⅓ = 1, a stable integer"** is the wrong arithmetic. Z₃
   charges add like a clock with 3 hours, so 1 + 1 + 1 = 3 = **0**. Three
   quark vortices together carry *no* net twist. That is actually good
   news: zero net charge is precisely what lets three flux tubes meet at a
   point. **The Y-junction baryon survives, for the right reason.**

**What this means physically.** This mirrors real QCD. Real quarks also
break the "center symmetry", and that is why a QCD flux tube can **snap**
when you pull too hard (a quark–antiquark pair pops out: "string
breaking"). Part 37's coupling behaves like quarks are already present.

**What is not affected.** The lattice runs of Parts 38–41
(σ = 0.173 GeV²) use a genuine *gauge* theory (link variables and
plaquettes), where center vortices are legitimate. That is a different
model from the Part 37 Lagrangian (wording is 83f). The 120° Y-junction,
the U(1) → cos(ψ−φ) limit and the 8 modes (spin-0, per T70) all stand.

**Kept for the future, not discarded (user's instruction).** Three
alternative postulates would make the Z₃ vortices genuine (§3):
B (adjoint coupling), C (matter and condensate co-rotate), D (U(3) target).
Each buys something and costs something.

---

## 1. Setup [ASSUMED]

Part 37 SU(3) Lagrangian (CLAUDE.md) [ASSUMED]:

```
L_3 = K Tr[(d_mu U^dag)(d^mu U)] + sum_i K_i Tr[(d_mu Psi_i^dag)(d^mu Psi_i)]
      + sum_i (g_i/3) Re Tr(Psi_i^dag U),        U, Psi_i in SU(3)      (158.1)
```

$$
\mathcal{L}_3 = K\,\mathrm{Tr}\!\left[(\partial_\mu U^\dagger)(\partial^\mu U)\right] + \sum_i K_i\,\mathrm{Tr}\!\left[(\partial_\mu \Psi_i^\dagger)(\partial^\mu \Psi_i)\right] + \sum_i \frac{g_i}{3}\,\mathrm{Re}\,\mathrm{Tr}(\Psi_i^\dagger U)
$$

Center of SU(3) [ASSUMED, standard]:

```
Z_3 = { 1, w*1, w^2*1 },   w = exp(2 pi i / 3),   w^3 = 1              (158.2)
```

**Source:** [Special unitary group — Wikipedia](https://en.wikipedia.org/wiki/Special_unitary_group)

Fundamental groups [ASSUMED, cited mathematics, not computed]:

```
pi_1(SU(3)) = 0,   pi_1(SU(3)/Z_3) = pi_1(PSU(3)) = Z_3,   pi_1(U(3)) = Z  (158.3)
```

**Source:** [Projective unitary group — Wikipedia](https://en.wikipedia.org/wiki/Projective_unitary_group);
[Unitary group — Wikipedia](https://en.wikipedia.org/wiki/Unitary_group)
(π₁(U(n)) ≅ ℤ via the determinant); Mermin (1979), *Rev. Mod. Phys.* 51, 591.

**Plain English:** a *line defect* (vortex/string) in a field valued in a
space X is protected exactly when π₁(X) ≠ 0. SU(3) itself has nothing to
offer. SU(3)/Z₃ (SU(3) with the three center matrices identified) offers
three classes, and U(3) offers the integers.

---

## 2. Derivations [DERIVED, VERIFIED]

### 2.1 The coupling breaks the Z₃ center

Write t = Tr(Ψ†U) = x + i y. Under U → ωU, linearity of the trace gives
Tr(Ψ†·ωU) = ω t. With ω = −1/2 + i√3/2:

```
Step 1: w t = (-1/2 + i sqrt3/2)(x + i y)
            = (-x/2 - sqrt3 y/2) + i (sqrt3 x/2 - y/2)
Step 2: Re(w t) - Re(t) = -x/2 - sqrt3 y/2 - x
                        = -3x/2 - sqrt3 y/2                             (158.4)
```

$$
\mathrm{Re}(\omega t) - \mathrm{Re}(t) = -\tfrac{3}{2}x - \tfrac{\sqrt{3}}{2}y
$$

This is not identically zero, so the coupling distinguishes U from ωU
[DERIVED; VERIFIED: S1, SymPy residual −3x/2 − √3y/2; S19, max change
3.43 over 200 random SU(3) pairs]. **The field space of (158.1) is
therefore SU(3), not SU(3)/Z₃. By (158.3) it supports no topologically
stable vortex lines.** [DERIVED]

The kinetic terms are center-invariant (|ω| = 1), so the coupling is the
only obstruction.

### 2.2 Vortex energy for a matrix field

Take a straight vortex along z with azimuth θ, and U(θ) = exp(iθX),
X Hermitian and diagonal with eigenvalues q₁, q₂, q₃. (X is the *vortex
generator*. It is written X, not Q, because Q already denotes the Koide
parameter, Q = 2/3 (Part 53), which coincidentally equals Tr X_min² in
(158.6). The two are unrelated. See `term_glossary.md`.)

```
Step 1: dU/dtheta = i X U
Step 2: (dU/dtheta)^dag (dU/dtheta) = U^dag X X U      (X Hermitian)
Step 3: Tr[...] = Tr(U^dag X^2 U) = Tr(X^2)            (cyclic trace)
Step 4: |grad theta|^2 = 1/r^2, so the energy density is K Tr(X^2)/r^2
Step 5: E/L = integral 2 pi r dr K Tr(X^2)/r^2
            = 2 pi K Tr(X^2) ln(R/xi)                                   (158.5)
```

$$
\frac{E}{L} = 2\pi K\,\mathrm{Tr}(X^2)\,\ln\frac{R}{\xi}
$$

For N = 1 and X = n this is the standard 2πKn² ln(R/ξ) used by Part 37
Step 6 (Kosterlitz & Thouless 1973) [DERIVED; VERIFIED: S6, SymPy
Tr[(∂U†)(∂U)] = q₁² + q₂² + q₃², residual 0]. Core energies are not
compared (assumption A1).

### 2.3 The cheapest Z₃ twist inside SU(3)

*If* the target were SU(3)/Z₃, the minimal vortex is the shortest path in
SU(3) from 1 to ω·1:

```
Condition 1: exp(2 pi i X) = w * 1  =>  each q_j in 1/3 + Z
Condition 2: U in SU(3)             =>  Tr X = q_1 + q_2 + q_3 = 0
Minimise Tr(X^2) = q_1^2 + q_2^2 + q_3^2 subject to both:
  (1/3, 1/3, -2/3):  1/9 + 1/9 + 4/9 = 2/3   <- minimum
  (4/3, -2/3, -2/3): 16/9 + 4/9 + 4/9 = 8/3
  ...
Result: X_min = diag(1/3, 1/3, -2/3),  Tr(X_min^2) = 2/3                (158.6)
```

$$
X_{\min} = \mathrm{diag}\!\left(\tfrac13,\tfrac13,-\tfrac23\right), \qquad \mathrm{Tr}(X_{\min}^2) = \tfrac23
$$

Check: exp(2πi·diag(1/3, 1/3, −2/3)) = diag(ω, ω, ω⁻²) = ω·1, since
ω⁻² = ω [VERIFIED: S7 exact residual 0; S8 independent float search
gives 0.666…; S9 the antivortex (ω²) has the same minimum, 2/3].

Using the same reference as Part 37 (assumption A2: the "U(1) vortex"
e^{iθ}·1₃, Tr Q² = 3):

```
E_Z3 / E_ref = (2/3) / 3 = 2/9      [conditional on an SU(3)/Z_3 target] (158.7)
```

$$
\frac{E_{Z_3}}{E_{\rm ref}} = \frac{2/3}{3} = \frac{2}{9}
$$

Against the 1×1 U(1) normalisation (Tr = 1) the ratio is 2/3. **The ratio
depends on the reference. The absolute statement (158.6) does not.**
[DERIVED]

### 2.4 Why Part 37 got 1/9

Part 37 Step 6 inserted winding n = 1/3 of one overall phase, i.e. the
path U(θ) = e^{iθ/3}·1₃:

```
Step 1: X = (1/3) * 1_3,  Tr(X^2) = 3 * 1/9 = 1/3
Step 2: ratio to reference: (1/3)/3 = 1/9      <- Part 37's number (S12)
Step 3: det U(theta) = (e^{i theta/3})^3 = e^{i theta}                  (158.8)
Step 4: det U(pi) = -1 != 1
```

$$
\det\!\left(e^{i\theta/3}\mathbb{1}_3\right) = e^{i\theta} \neq 1
$$

The path ends correctly at ω·1 but leaves SU(3) along the way, so it is
not an allowed configuration [DERIVED; VERIFIED: S10]. Tracelessness
forces one eigenvalue to −2/3, which costs more. **Eq 150.2–150.3 and
Part 37 S7 (1/9 per vortex, 1/3 for three) are withdrawn** [NEGATIVE].

### 2.5 Z₃ fusion and the Y-junction

Z₃ charges add mod 3, and as matrices (ω·1)³ = ω³·1 = 1:

```
1 + 1 + 1 = 3 = 0  (mod 3)                                              (158.9)
```

$$
(\omega\,\mathbb{1})^3 = \mathbb{1} \quad\Longleftrightarrow\quad 1+1+1 \equiv 0 \pmod 3
$$

Three unit Z₃ vortices fuse to the **trivial** class, not to "winding 1"
[DERIVED; VERIFIED: S13 contradiction with Part 37, S14 match]. A node
where three flux lines meet must conserve Z₃ charge. Total 0 means three
unit lines *can* meet at a point and end there, so the baryon Y-junction
is topologically allowed. Two units fuse to one anti-unit (1 + 1 = −1
mod 3), which is the Z₃ statement that "a diquark looks like an
antiquark".

The 120° angle is force balance between three equal tensions,
ê₁ + ê₂ + ê₃ = 0, independent of topology [VERIFIED: S18]. It stands.

### 2.6 What survives

| Claim | Status after 83e |
|---|---|
| U(1) limit Re Tr(Ψ†U)/1 = cos(ψ−φ) | **Stands** (S4) |
| 8 modes from N² − 1 | Stands, as spin-0 modes (T70/Part 140; wording is 83f) |
| Topologically stable Z₃ vortices in (158.1) | **Withdrawn**: target is SU(3), π₁ = 0 |
| E_Z₃/E_U₁ = 1/9 (Eq 150.2, Part 37 S7) | **Withdrawn**: 2/9, conditional (158.7) |
| "3 × ⅓ = winding 1, stable" | **Corrected**: fuses to 0 mod 3 (158.9) |
| Y-junction 120° | **Stands** (force balance) |
| Y-junction allowed topologically | **Stands, conditionally**: needs a Z₃-invariant target |
| Lattice σ = 0.173 GeV² (Parts 38–41) | **Unaffected**: Wilson link gauge theory, a different model |
| Part 105 N_c = 3 from the Z₃ center | Stands as group theory (the center of SU(3) *is* Z₃); its "topology selects" reading becomes conditional |

---

## 3. Alternative Postulates B, C, D [SPECULATIVE — OPEN, kept for future work]

These are **not adopted**. Each would make the Z₃ vortices genuine. Each
is a structural change (a new term or a new postulate), so adopting any
of them needs its own plan, user approval and a
`mathematical_formalization_extensions.md` update. Tracked as TODO_05
**T85**. Recorded in full because a cost here may turn out to be a
feature elsewhere (user's instruction, 2026-10-17).

### Alternative B: adjoint (center-blind) coupling

```
L_int^B = sum_i (g_i/9) |Tr(Psi_i^dag U)|^2                              (158.10)
```

$$
\mathcal{L}_{\rm int}^{B} = \sum_i \frac{g_i}{9}\,\bigl|\mathrm{Tr}(\Psi_i^\dagger U)\bigr|^2
$$

- **Gains:** invariant under U → ωU alone (|ω t|² = |t|², VERIFIED S3,
  S20). The target becomes SU(3)/Z₃ and Z₃ vortices are genuinely
  protected, with minimal energy (158.6).
- **Costs:** (1) **The exact U(1) limit is lost.** For N = 1,
  |e^{i(φ−ψ)}|² = 1 is constant, so no cos(ψ−φ) locking survives
  (VERIFIED S5). The CLAUDE.md headline "SU(3) reduces to the U(1)
  Lagrangian" would have to go. (2) Three degenerate locked vacua: the
  maximum |Tr|² = 9 is reached at Ψ†U = 1, ω·1 and ω²·1 (VERIFIED S16).
  That implies Z₃ domain walls between regions locked to different
  center elements.
- **Why keep it:** Z₃ domain walls and three degenerate vacua are an
  active topic in QCD (center domains at high temperature). The vacuum
  triplet could connect to the existing "three" threads in PDTP (Koide
  Z₃ partition, Part 53; N_c = 3, Part 105) without any extra input.
  Untested.

### Alternative C: co-rotating matter (joint Z₃ as a discrete gauge redundancy)

Postulate: the physical configuration space is

```
(U, Psi) ~ (w U, w Psi)   =>  target (SU(3) x SU(3)) / Z_3^diag          (158.11)
```

$$
(U,\Psi) \sim (\omega U, \omega\Psi) \quad\Rightarrow\quad \bigl(SU(3)\times SU(3)\bigr)/\mathbb{Z}_3^{\rm diag}
$$

- **Gains:** the coupling Re Tr(Ψ†U) is untouched (joint invariance,
  VERIFIED S2, S20), so **the U(1) limit is kept exactly**. π₁ of the
  quotient is Z₃, so Z₃ vortices exist. The minimal one is a joint twist
  U = Ψ = exp(iθX_min) that keeps perfect locking, Re Tr(Ψ†U)/3 = 1 along
  the whole loop (VERIFIED S15).
- **Costs:** (1) a **new postulate**: a discrete gauge symmetry acting on
  matter and condensate together; (2) the quark vortex is then a
  **composite** twist of matter *and* condensate, with energy
  2π(K + K_i)·(2/3)·ln(R/ξ), not a pure condensate defect.
- **Why keep it:** it is the smallest change that keeps every existing
  CLAUDE.md equation. "Quarks are joint matter–spacetime windings" fits
  PDTP's core picture (matter locked to the condensate). Untested.

### Alternative D: U(3) target (drop det U = 1)

```
U in U(3) = (U(1) x SU(3)) / Z_3,   minimal loop U = diag(e^{i theta}, 1, 1)   (158.12)
```

$$
U \in U(3) = \bigl(U(1)\times SU(3)\bigr)/\mathbb{Z}_3, \qquad U_{\min}(\theta) = \mathrm{diag}\!\left(e^{i\theta},1,1\right)
$$

- **Gains:** π₁(U(3)) = ℤ (det winds once, VERIFIED S17). The minimal
  loop is ⅓ of the overall U(1) winding combined with a Z₃ center element,
  i.e. a genuinely fractional vortex with Tr Q² = 1, so 1/3 of the scalar
  vortex (Tr = 3). These are the "semi-superfluid" strings known in
  color-flavor-locked dense QCD (Balachandran, Digal & Matsuura 2006). The
  N = 1 limit is still U(1), so the cos(ψ−φ) limit is kept.
- **Costs:** an **extra massless U(1) mode** (a 9th Goldstone mode), which
  conflicts with the Standard Model's particle content unless it is
  removed (gauged or given a mass). See §5.
- **Why keep it:** it is the only option with direct precedent in
  established dense-QCD physics. The extra U(1) could be identified with
  baryon number, as it is in the CFL phase. Untested.

| | U(1) limit kept | New ingredient | Main cost |
|---|---|---|---|
| A (adopted) | yes | none | no protected Z₃ vortices in (158.1) |
| B | **no** | adjoint coupling term | U(1) limit lost; Z₃ domain walls |
| C | yes | discrete gauge postulate | quark vortex = matter + condensate composite |
| D | yes | U(1) factor (det ≠ 1) | extra massless mode (SM tension) |

---

## 4. Sudoku Scorecard

Run: `python simulations/solver/t83e_z3_target.py` (every entry reads a
computed value from the step return dicts).

| ID | Test | Computed | Expected | Result |
|---|---|---|---|---|
| S1 | Part 37 needs Re Tr(Ψ†U) Z₃-invariant | −3x/2 − √3y/2 | 0 | CONTRADICTION |
| S2 | Joint (ωU, ωΨ) invariant (C) | 0 | 0 | MATCH |
| S3 | Adjoint \|Tr\|² invariant (B) | 0 | 0 | MATCH |
| S4 | U(1) limit Re Tr → cos(ψ−φ) | 0 | 0 | MATCH |
| S5 | U(1) limit of adjoint = cos(ψ−φ)? (B) | −cos(a−b) | 0 | CONTRADICTION |
| S6 | Kinetic density = Tr(Q²)(∂θ)² | 0 | 0 | MATCH |
| S7 | exp(2πiX_min) = ω·1 | true | true | MATCH |
| S8 | min Tr Q²: exact = float search | 2/3 | 0.6667 | MATCH |
| S9 | Antivortex minimum = vortex minimum | 2/3 | 2/3 | MATCH |
| S10 | Part 37 path in SU(3)? det at θ = π | −1 | 1 | CONTRADICTION |
| S11 | E_Z₃/E_U₁ = 1/9 (Part 37 S7) | 2/9 | 1/9 | CONTRADICTION |
| S12 | 1/9 reproduced from Part 37's own path | 1/9 | 1/9 | MATCH |
| S13 | Three Z₃ units nontrivial ("winding 1") | 0 | 1 | CONTRADICTION |
| S14 | (ω·1)³ = 1 (junction allowed) | true | true | MATCH |
| S15 | C: joint vortex keeps locking | 1 | 1 | MATCH |
| S16 | B: three degenerate maxima | [9, 9, 9] | 9 | MATCH |
| S17 | D: U(3) loop det winding | 1 | 1 | MATCH |
| S18 | Y-junction vectors sum to 0 | [0, 0] | [0, 0] | MATCH |
| S19 | Numeric: max \|ΔRe Tr\| > 0 (200 pairs) | 3.43 | > 0 | MATCH |
| S20 | Numeric: adjoint, joint changes < 1e−10 | 2.7e−15, 6.8e−16 | < 1e−10 | MATCH |

**15 matches, 5 contradictions out of 20 tests.** Sub-group analysis:
S1, S10, S11 and S13 are the four Part 37 claims. They share one
assumption: that the Z₃ "⅓-winding" can be treated as an abelian
fraction of a single overall phase. In SU(3) it cannot (det = 1 forces
an unequal twist, and charges add mod 3). S5 is the stated cost of
alternative B, not a defect of A.

Also fixed under the RECHECK rule: `su3_condensate.py` S7 was circular
(`ratio_S7 = 1/9` compared with 1/9). It now computes 2/9 and reports
FAIL. S3 and S8 there printed literals and are now computed (both still
pass). `homotopy_classification.py` S6 was circular in the same way. It
now computes 2/9 and FAILs, and its docstring marks the
"Strong | SU(3)/Z₃" row conditional.

---

## 5. Standard Model Compatibility

- **Gauge invariance:** unchanged. Option A adds nothing. Note that
  (158.1) has a *global* SU(3) only (T70/Part 140). Real QCD's center
  symmetry is a property of the pure *gauge* theory, which is why the
  lattice Parts 38–41 (link variables) have it and (158.1) does not.
- **Fundamental matter breaks the center, as in QCD.** In real QCD,
  dynamical quarks in the fundamental representation break Z₃ center
  symmetry explicitly. Flux tubes are then not topologically protected
  and break by pair creation ("string breaking", seen on the lattice).
  The coupling Re Tr(Ψ†U) is a fundamental-type coupling with the same
  effect, so the 83e finding is **consistent with** QCD with quarks, not
  in tension with it. Confinement of *color* in QCD is not a statement
  about protected vortices in a matter field, so nothing in the SM is
  contradicted.
- **Particle content:** A, B and C add no fields. D adds a massless U(1)
  mode, which is a **TENSION** if adopted (no such massless scalar is
  observed; it would need gauging or a mass).
- **Conservation laws:** unaffected. The Z₃ "triality" of hadrons
  (baryons and mesons have total Z₃ charge 0) agrees with (158.9).
- **Higgs, masses, couplings:** not touched by this sub-task.

## 6. Two-Phase Check

**Not applicable.** The SU(3) sector of (158.1) has no φ₋ / two-phase
structure. Part 61's two-phase construction is defined only for the U(1)
gravitational sector, and none of its results (Newton's 3rd law
ψ̈ = −2φ̈₊, the √3·g Jeans eigenvalue from Part 154, the corrected
biharmonic from Part 155) involve the SU(3) center. The U(1) limit that
links the two sectors (S4) is unchanged.

---

## 7. Impact (files changed in this pass)

| File | Change |
|---|---|
| `su3_condensate_extension.md` | Erratum banner; §1.2, §5.1–5.3, §8.3, §10 (S7 now FAIL, 6/10 exact), §14.1, Originals list |
| `mathematical_formalization_extensions.md` | §1.4 correction block (Eq 150.2–150.3 withdrawn → 158.7); results table |
| `equation_reference.md` | §3d note; Part 158 block; changelog |
| `simulations/solver/su3_condensate.py` | S7 circular check replaced (computes 2/9 → FAIL); S3, S8 literals replaced by computed values; Step 6 erratum print; conclusion text |
| `simulations/solver/homotopy_classification.py` | S6 circular check replaced (2/9 → FAIL); "Strong \| SU(3)/Z₃" row marked conditional in the docstring |
| `term_glossary.md`, `Methodology.md`, `framework_hierarchy.md`, `wave_effects_extension.md`, `mathematical_formalization.md`, `koide_z3_derivation.md`, `koide_theta0.md`, `magic_number_topology.md`, `glueball_x2370_test.md`, `platonic_solids_lens.md`, `su3_gauge_structure.md`, `two_phase_rederivation.md`, `pdtp_lagrangian4.md`, `condensate_layer_optics.md`, `rip_square_emergent_phenomena.md` | One-line "conditional, Part 158" tags (or a corrected sentence) |
| `TODO_04.md` T83 / `TODO_05.md` T85 | 83e DONE; alternatives B/C/D filed |
| CLAUDE.md (root + repo) | **Not edited.** Left for 83h, per the CLAUDE.md rule |

**Unaffected (checked):** Koide Q = 2/3 and N_gen = |Z₃| (Parts 53, 93) use
the Z₃ *center group*, not vortex topology. The Part 106 Hopf link uses the
Z₃-symmetric 120° geometry, not vortex protection or the 1/9. The lattice
Parts 38–41 use a gauge theory.

## 8. Status

- **DONE (option A):** Z₃ vortices downgraded from "topologically stable
  in the PDTP SU(3) Lagrangian" to **conditional on a Z₃-invariant
  target**. Energy corrected 1/9 → 2/9 (conditional). Fusion arithmetic
  corrected. Y-junction kept, now for the right reason.
- **OPEN (TODO_05 T85):** alternative postulates B, C, D. The natural
  first test for each is a Sudoku check of whether it keeps the 10
  Part 37 scorecard items and the U(1) limit, plus a Standard Model
  particle-content check (decisive for D).
- **Hand-off to 83f:** the "8 gluons", "Wilson loop action" and κ_GL
  wording (finding 8), and the observation that the lattice Parts 38–41
  simulate a *different* model (gauge links) from (158.1) (site field).

---

## Sources

- [Special unitary group — Wikipedia](https://en.wikipedia.org/wiki/Special_unitary_group) — center Z_N, simple connectivity
- [Projective unitary group — Wikipedia](https://en.wikipedia.org/wiki/Projective_unitary_group) — PSU(n) = SU(n)/Z_n, π₁ = Z_n
- [Unitary group — Wikipedia](https://en.wikipedia.org/wiki/Unitary_group) — π₁(U(n)) ≅ ℤ via det
- Mermin, N.D. (1979), "The topological theory of defects in ordered media", *Rev. Mod. Phys.* 51, 591 — π₁ classifies line defects
- Kosterlitz, J.M. & Thouless, D.J. (1973), *J. Phys. C* 6, 1181 — vortex line energy 2πKn² ln(R/ξ)
- Balachandran, A.P., Digal, S. & Matsuura, T. (2006), "Semi-superfluid strings in high density QCD", *Phys. Rev. D* 73, 074009, [arXiv:hep-ph/0509276](https://arxiv.org/abs/hep-ph/0509276) — U(3)-type fractional strings (alternative D)
- Greensite, J. (2011), *An Introduction to the Confinement Problem*, Springer — center symmetry, center vortices, string breaking with fundamental matter
- 't Hooft, G. (1978), *Nucl. Phys. B* 138, 1 — center vortices in gauge theory

**PDTP Original in this document:** (158.4) the center-breaking residual of
the Part 37 coupling; (158.6)–(158.7) the corrected minimal Z₃ vortex
energy for the PDTP matrix field; the comparison of alternatives B/C/D
against the PDTP U(1) limit.

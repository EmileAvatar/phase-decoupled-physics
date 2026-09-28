# Newtonian Source Audit — What Actually Sources the 1/r Field? (Part 153)

**TODO:** TODO_04.md T83, sub-task **83a** — worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-09-28.
**Script:** `simulations/solver/t83a_newtonian_source.py`
**Log:** `simulations/solver/outputs/t83a_newtonian_source_<timestamp>.txt`
**Scorecard:** 9 matches, 5 contradictions out of 14 tests (the
contradictions are the finding — see Section 6).
**Status:** CONSTRUCTIVE NEGATIVE. The 1/r *shape* of Newtonian gravity is
correctly recovered; the Part 63 S4 derivation of it is invalid and is
replaced here; and the *strength* of the 1/r field (what Newton calls
"mass") is **not** produced by the Lagrangian as written — it vanishes for
any matter sitting in its lowest-energy (locked) state.

---

## Plain-English Summary

Think of every piece of matter as a clock (ψ) and spacetime as another
clock (φ). PDTP says gravity is the two clocks pulling each other into sync.

1. **The shape of gravity is fine.** Outside a planet there is nothing for
   spacetime's clock to lock to, so its field spreads out freely — and a
   freely spreading field in 3D falls off exactly as 1/r. That is Newton's
   law. ✓
2. **Part 63's proof of that was wrong, though.** It used an equation of the
   form "curvature of Φ ∝ Φ". That equation does *not* give 1/r; it gives a
   force that either dies off exponentially (like the short-range nuclear
   force) or wobbles with distance. The correct argument is point 1: the
   1/r comes from the region *outside* matter, where the coupling is zero.
3. **The real problem is the strength.** How hard a planet pulls is set by
   how far matter's clock is *out of sync* with spacetime's clock inside it.
   But the two clocks are allowed to adjust to each other — and when they
   do, they settle into perfect sync. A perfectly synced planet pulls with
   **zero** force. So a planet at rest in its lowest-energy state is,
   according to these Lagrangians, gravitationally invisible.
4. **Why that happens (the deep reason).** The Lagrangian only cares about
   the *difference* ψ − φ. Shifting both clocks together costs nothing. A
   rule like that (a "symmetry") comes with a bookkeeping law (a
   "conservation law", via Noether's theorem): whatever "push" matter gives
   spacetime, spacetime gives back to matter, and for anything sitting still
   the totals cancel exactly. This is the same reason the massless partners
   of such symmetries ("Goldstone bosons") are known not to produce ordinary
   1/r forces between objects at rest.
5. **What the older derivation did.** The textbook-style recovery in
   `mathematical_formalization.md` §7 quietly *held* matter's clock at a
   fixed offset from spacetime's clock. With that offset imposed by hand,
   you get Newton. Without it, you get nothing. So the offset — not the
   Lagrangian — is doing the work of "mass".

**So what?** This does not kill PDTP, but it pinpoints exactly what is
missing: some ingredient that keeps matter's clock slightly out of step
with spacetime's clock, in proportion to how much matter there is. Finding
(or adding) that ingredient is now the central open question for Goal 1.

---

## 1. Setup and Assumptions

**Starting Lagrangians** [ASSUMED — CLAUDE.md, Parts 1 and 61]:

```
L_1 = 1/2 (d_mu phi)(d^mu phi) + 1/2 (d_mu psi)(d^mu psi) + g(x) cos(psi - phi)      (153.1)
```

$$
\mathcal{L}_1 = \tfrac12(\partial_\mu\phi)(\partial^\mu\phi) + \tfrac12(\partial_\mu\psi)(\partial^\mu\psi) + g(x)\cos(\psi-\phi)
$$

```
L_2 = 1/2[(d psi)^2 + (d phi_b)^2 + (d phi_s)^2] + g cos(psi - phi_b) - g cos(psi - phi_s)   (153.2)
```

$$
\mathcal{L}_2 = \tfrac12\left[(\partial\psi)^2 + (\partial\phi_b)^2 + (\partial\phi_s)^2\right] + g\cos(\psi-\phi_b) - g\cos(\psi-\phi_s)
$$

**Sign conventions:** metric (+,−,−,−); L = T − V; +cos coupling (stable at
ψ = φ); Euler–Lagrange: ∂_μ(∂L/∂(∂_μ q)) − ∂L/∂q = 0.

**Assumptions:**
- [A1] Static, spherically symmetric matter ball of radius R (same setup as
  `mathematical_formalization.md` §7.1).
- [A2] The coupling lives only where matter is: g(x) = g for r < R, 0 for
  r > R (same as §7.2, "outside the mass … no matter sources").
- [A3] Linearisation sin Δ ≈ Δ for the analytic results; the full nonlinear
  equation is solved numerically as a check (Section 5).
- [A4] g is the bare Lagrangian coupling, SI units 1/length² (m⁻²), per
  `term_glossary.md` §4 (corrected by TODO_05 T68). So k_Δ = √(2g) is a
  wavenumber (m⁻¹). Dimensional check of (153.7): [∇²Δ] = m⁻²,
  [2gΔ] = m⁻² ✓; of (153.10): [C] = [Δ_∞]·m ✓ (Δ dimensionless).

**Symbols** (checked against `docs/term_glossary.md`): Δ = ψ − φ (phase
gap, existing); **k_Δ** (new: screening wavenumber of Δ, m⁻¹; numerically
the same value as the existing k̄² = 2g of Part 117, but defined here for
the single-phase gap mode, so named separately); **Δ_∞**
(new: phase gap imposed at infinity, dimensionless); **C** (exterior
monopole coefficient, same meaning as §7.3 of the formalization doc, units
of φ × length).

**Static field equation** [ASSUMED — Euler–Lagrange, Goldstein §13.3]. For
a field q with unit kinetic term, q_tt − ∇²q = ∂L_int/∂q; with q_tt = 0:

```
-nabla^2 q = dL_int/dq                                                    (153.3)
```

$$
-\nabla^2 q = \frac{\partial \mathcal{L}_\text{int}}{\partial q}
$$

---

## 2. The Part 63 S4 Step Is Invalid [NEGATIVE]

`two_phase_rederivation.md` S4 reached `nabla^2(phi_+) ≈ -(g/c^2)*delta`
with δ ∝ Φ, and concluded "∇²Φ ∝ Φ → same 1/r potential". Test this
directly with the radial Laplacian.

**Source:** [Laplace operator — Wikipedia](https://en.wikipedia.org/wiki/Laplace_operator)
(spherical coordinates):

```
nabla^2 f(r) = (1/r^2) d/dr ( r^2 df/dr )                                  (153.4)
```

$$
\nabla^2 f(r) = \frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{df}{dr}\right)
$$

**Step 1 — f = 1/r.** df/dr = −1/r²; r² df/dr = −1; d/dr(−1) = 0. So
∇²(1/r) = 0 away from the origin. [VERIFIED: S4, residual 0]

**Step 2 — f = e^{−mr}/r.** df/dr = −e^{−mr}(mr + 1)/r²;
r² df/dr = −e^{−mr}(mr + 1); d/dr of that = e^{−mr}(m²r); divide by r²:
∇²f = m² e^{−mr}/r = +m² f. [VERIFIED: S5, ratio = m²]

**Step 3 — f = cos(mr)/r.** Same steps give ∇²f = −m² f.
[VERIFIED: log `oscill_ratio = -m**2`]

**Result** [NEGATIVE, VERIFIED]: an equation of the form ∇²Φ = ±m²Φ has
Yukawa (e^{−mr}/r, **Source:** [Yukawa potential — Wikipedia](https://en.wikipedia.org/wiki/Yukawa_potential))
or oscillating (cos(mr)/r) solutions, **never** a pure 1/r. Poisson's
equation needs a source that is *independent* of Φ:

```
nabla^2 Phi = 4 pi G rho      (rho = matter density, not a function of Phi)  (153.5)
```

$$
\nabla^2\Phi = 4\pi G\rho
$$

**Source:** [Poisson's equation — Wikipedia](https://en.wikipedia.org/wiki/Poisson%27s_equation#Newtonian_gravity).

The same applies to the biharmonic form ∇⁴Φ + 4g²Φ: its Fourier-space
Green's function 1/(k⁴ + 4g²) is finite at k → 0, so it has no 1/r tail;
and the Green's function of ∇⁴ alone grows like r (∇²r = 2/r, ∇²(2/r) = 0,
log `lap_r`, `lap_lap_r`). (Sub-task 83c / Part 155 has since corrected the
equation itself to ∇⁴φ₊ − g²φ₊ = −g²ψ — still no 1/r term at any range; see
[biharmonic_rederivation.md](biharmonic_rederivation.md).)

**Plain English:** S4 confused "the field's curvature is proportional to
the field" (a screened, short-range force) with "the field's curvature is
proportional to the amount of matter" (Newton). Only the second gives 1/r.

---

## 3. Where 1/r Really Comes From: the Massless Mode

### 3.1 The joint-shift symmetry [DERIVED, VERIFIED]

**Step 1.** L_int = g cos(ψ − φ).
**Step 2.** ∂L_int/∂ψ = −g sin(ψ − φ); ∂L_int/∂φ = +g sin(ψ − φ) (chain
rule, d/dφ of (ψ − φ) = −1).
**Step 3.** Sum = 0. So L is unchanged under ψ → ψ + a, φ → φ + a.

```
dL_int/dpsi + dL_int/dphi = 0                                              (153.6)
```

$$
\frac{\partial\mathcal{L}_\text{int}}{\partial\psi} + \frac{\partial\mathcal{L}_\text{int}}{\partial\phi} = 0
$$

[VERIFIED: S1, SymPy residual 0.] By Noether's theorem
(**Source:** [Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem))
the current J_μ = ∂_μφ + ∂_μψ is conserved: □(φ + ψ) = 0 exactly (add the
two field equations; the sin terms cancel).

**Two-phase** [VERIFIED: S2]: L_int = g cos(ψ − φ_b) − g cos(ψ − φ_s) is
invariant under the joint shift of all three fields (residual 0), so
□(ψ + φ_b + φ_s) = □(ψ + 2φ₊) = 0. The φ₋ direction (φ_b + a, φ_s − a) is
**not** a symmetry: its derivative is −g[sin(φ_b − ψ) + sin(φ_s − ψ)] ≠ 0
[VERIFIED: S3]. This is also exactly Newton's 3rd law of Part 61:
with inertias 1 (ψ) and 2 (φ₊, since ½φ̇_b² + ½φ̇_s² = φ̇₊² + φ̇₋²),
ψ̈ + 2φ̈₊ = F_ψ + F₊ = 0 [VERIFIED: S13, residual 0].

### 3.2 Linear static modes (U(1)) [DERIVED, VERIFIED]

Apply (153.3) with Δ = ψ − φ, sin Δ ≈ Δ:

**Step 1.** −∇²φ = ∂L_int/∂φ = g sin Δ ≈ gΔ  ⇒  ∇²φ = −gΔ.
**Step 2.** −∇²ψ = ∂L_int/∂ψ = −g sin Δ ≈ −gΔ  ⇒  ∇²ψ = +gΔ.
**Step 3.** Subtract: ∇²Δ = ∇²ψ − ∇²φ = 2gΔ.
**Step 4.** Add: ∇²(φ + ψ) = 0.

```
nabla^2 Delta = k_Delta^2 Delta,   k_Delta^2 = 2 g;     nabla^2 (phi + psi) = 0   (153.7)
```

$$
\nabla^2\Delta = k_\Delta^2\,\Delta,\quad k_\Delta^2 = 2g;\qquad \nabla^2(\phi+\psi) = 0
$$

[VERIFIED: log `lap_Delta = 2*Delta*g`, `lap_S = 0`, `k_Delta_sq = 2*g`.]

**Plain English:** there are two kinds of disturbance. The *gap* Δ between
the clocks is stiff (screened over a length 1/k_Δ). The *common* motion
φ + ψ is completely free — it is the only candidate carrier of a
long-range 1/r force. But being free also means nothing in L pushes on it:
it only gets a 1/r tail if a boundary condition or a flux forces one.

---

## 4. The Strength of the 1/r Field: Two Models of a Matter Ball

### 4.1 Model E — ψ extends everywhere, coupling only inside [DERIVED, VERIFIED]

**Step 1 (interior, r < R).** Write u = rΔ. For a radial function,
∇²Δ = u''/r (from 153.4), so (153.7) becomes u'' = k_Δ² u, with solutions
sinh(k_Δ r) and cosh(k_Δ r). Regularity at r = 0 (Δ finite) excludes
cosh(k_Δ r)/r, leaving

```
Delta_in(r) = A sinh(k_Delta r) / r                                        (153.8)
```

$$
\Delta_\text{in}(r) = A\,\frac{\sinh(k_\Delta r)}{r}
$$

**Step 2 (exterior, r > R).** g = 0, so ∇²Δ = 0 and by Section 2 Step 1

```
Delta_out(r) = Delta_inf - C / r                                           (153.9)
```

$$
\Delta_\text{out}(r) = \Delta_\infty - \frac{C}{r}
$$

**Step 3 (match value at R).** A sinh(k_ΔR)/R = Δ_∞ − C/R.
**Step 4 (match slope at R).** d/dr[sinh(kr)/r] = [kr cosh(kr) − sinh(kr)]/r²,
so A[k_ΔR cosh(k_ΔR) − sinh(k_ΔR)]/R² = C/R², i.e.
C = A[k_ΔR cosh(k_ΔR) − sinh(k_ΔR)].
**Step 5 (solve).** Substitute Step 4 into Step 3 multiplied by R:
A sinh = Δ_∞R − A k_ΔR cosh + A sinh ⇒ A = Δ_∞ /(k_Δ cosh(k_ΔR)). Then

```
C = Delta_inf * ( R - tanh(k_Delta R) / k_Delta )                          (153.10)
```

$$
C = \Delta_\infty\left(R - \frac{\tanh(k_\Delta R)}{k_\Delta}\right)
$$

[VERIFIED: S6 — A and C substituted back into the interior ODE and both
matching conditions, all three residuals = 0.]

**Step 6 (the φ field).** φ + ψ is harmonic on all of space (153.7) and
bounded, so it is constant: φ + ψ = S_∞ (a bounded harmonic function on R³
is constant — **Source:** [Harmonic function — Liouville's theorem, Wikipedia](https://en.wikipedia.org/wiki/Harmonic_function#Liouville's_theorem)). Hence
φ = (S_∞ − Δ)/2 and outside:

```
phi_out(r) = (S_inf - Delta_inf)/2 + C / (2 r)                              (153.11)
```

$$
\phi_\text{out}(r) = \frac{S_\infty - \Delta_\infty}{2} + \frac{C}{2r}
$$

A genuine 1/r tail, with coefficient C/2.

**Step 7 (limits).** Using tanh x = x − x³/3 + O(x⁵):
- **Weak coupling, k_ΔR ≪ 1:** C ≈ Δ_∞ k_Δ² R³/3 = (2g/3) Δ_∞ R³
  [VERIFIED: log `C_weak`]. Scales with **volume** — Newton-like. Numerically
  C(2R)/C(R) = 7.9990 vs Newton's 8 [S7 MATCH].
- **Strong coupling, k_ΔR ≫ 1:** C → Δ_∞ R [VERIFIED: log
  `C_over_R_strong = Delta_inf`]. Scales with **radius**, like the charge on
  a conducting sphere at fixed voltage. C(2R)/C(R) = 2.0101 vs 8
  [S8 CONTRADICTION].
- **No imposed offset, Δ_∞ = 0:** C = 0 exactly [S9 CONTRADICTION].

**Plain English:** in this model the ball does make a 1/r field — but only
if something far away holds matter's clock out of step with spacetime's by
Δ_∞. The strength is set by that far-away offset, not by how much matter
there is; and for strongly coupled (big or dense) bodies it grows with
size, not mass. Model E is also physically odd: it gives the matter field ψ
itself a 1/r tail far outside the matter.

### 4.2 Model K — ψ confined to the ball (the physical case) [DERIVED, VERIFIED]

Matter's phase field exists only where matter is, so no ψ flux leaves the
ball: ∂ψ/∂r = 0 at r = R (Neumann condition).

**Exact nonlinear theorem (no linearisation).**
**Step 1.** Integrate the static ψ equation (153.3), −∇²ψ = −g sin Δ, over
the ball: −∫∇²ψ d³x = −∫ g sin Δ d³x.
**Step 2.** Divergence theorem
(**Source:** [Divergence theorem — Wikipedia](https://en.wikipedia.org/wiki/Divergence_theorem)):
∫∇²ψ d³x = ∮ ∇ψ·dA = 0 by the Neumann condition.
**Step 3.** Therefore ∫ g sin Δ d³x = 0.
**Step 4.** The φ equation is ∇²φ = −g sin Δ, so ∮∇φ·dA = −∫ g sin Δ d³x = 0.
**Step 5.** With φ_out = φ_∞ − C/r, the flux is 4πC. Hence

```
C = 0     for every static configuration with confined psi                  (153.12)
```

$$
C = 0
$$

[DERIVED — exact. VERIFIED in the linear case: S10, SymPy gives the
Neumann-compatible amplitude A = 0 and C = 0; flux identity
φ'(r) + ψ'(r) = 0 inside, residual 0.]

**Time-dependent version** [DERIVED; integral identity, SymPy not needed —
it is Steps 1–2 with ψ_tt kept]: integrating ψ_tt − ∇²ψ = −g sin Δ over
the ball gives

```
Q(t) := integral g sin(Delta) d^3x = - d^2/dt^2 [ integral psi d^3x ]       (153.13)
```

$$
Q(t) \equiv \int g\sin\Delta\, d^3x = -\frac{d^2}{dt^2}\int \psi\, d^3x
$$

Q is the net source of φ. A steady, nonzero source requires matter's total
phase to keep **accelerating** — its clock frequency drifting without limit.

**Plain English:** if matter's clock can't leak out of the matter, then
every tug the matter gives spacetime is balanced by an equal tug spacetime
gives the matter, and for a body at rest the net "gravitational charge" is
exactly zero. That is Newton's 3rd law (Part 61) working *against* Newton's
law of gravity.

---

## 5. Two-Phase Lagrangian and Nonlinear Check

### 5.1 The two-phase vacuum sources nothing [DERIVED, VERIFIED]

**Step 1.** Product identity (A&S 4.3.37, cos A − cos B =
−2 sin((A+B)/2) sin((A−B)/2), with A = ψ − φ_b, B = ψ − φ_s, so
(A+B)/2 = ψ − φ₊ and (A−B)/2 = −φ₋):
L_int = 2g sin(ψ − φ₊) sin(φ₋). [VERIFIED: log `product identity residual = 0`]
**Step 2.** V = −L_int = −2g sin Θ sin φ₋, with Θ = ψ − φ₊.
**Step 3.** ∂V/∂Θ = −2g cos Θ sin φ₋; ∂V/∂φ₋ = −2g sin Θ cos φ₋. At the
Part 119 vacuum Θ = π/2, φ₋ = π/2 both vanish (cos(π/2) = 0).
**Step 4.** Hessian there: ∂²V/∂Θ² = 2g sin Θ sin φ₋ = 2g;
∂²V/∂φ₋² = 2g; mixed = −2g cos Θ cos φ₋ = 0. Eigenvalues 2g, 2g > 0.

```
grad V = 0,  Hessian eigenvalues = {2g, 2g}  at  Theta = phi_- = pi/2        (153.14)
```

$$
\nabla V = 0,\qquad \operatorname{eig}(\partial^2 V) = \{2g,\,2g\}\ \text{at}\ \Theta=\phi_-=\tfrac{\pi}{2}
$$

[VERIFIED: log.] So matter sitting uniformly in the two-phase vacuum is an
exact static solution in which every source term is zero: no exterior field
at all [S12 CONTRADICTION with Newton].

**Step 5 (confinement argument carries over).** Because of the joint-shift
symmetry (S2), the Model K theorem applies to ψ + φ_b + φ_s: with confined
ψ, the monopole of φ_b + φ_s = 2φ₊ (the "gravity mode") is exactly zero.
**The only unprotected channel is φ₋** (S3: not a symmetry direction) —
its source 2g sin Θ cos φ₋ is zero at the vacuum but not identically.

### 5.2 Nonlinear numerical check [VERIFIED]

The full equation Δ'' + (2/r)Δ' = 2g(r) sin Δ (Model E) was solved with
`scipy.integrate.solve_bvp` (g = 0.5 so k_Δ = 1, R = 2, Δ_∞ = 10⁻³,
smoothed step width 0.01, Robin condition Δ + rΔ' = Δ_∞ at r_max = 200).
Result C = 1.03605 × 10⁻³ vs (153.10): Δ_∞(2 − tanh 2) = 1.03597 × 10⁻³;
ratio 1.00008 [S11 MATCH]. The linear analysis is not an artifact.

### 5.3 Jeans sign (two-phase compatibility check)

With the correct inertias (1, 2, 2) the linearised Jeans matrix on
(Θ, φ₋) is M = [[0, 3g], [g, 0]], eigenvalues ±√3·g: a positive (unstable)
eigenvalue exists [S14 MATCH]. The magnitude correction from 2√2·g is
sub-task 83b.

---

## 6. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|----|------|----------|----------|--------|
| S1 | U(1) joint-shift Noether residual | 0 | 0 | MATCH |
| S2 | Two-phase joint-shift residual | 0 | 0 | MATCH |
| S3 | φ₋ direction not a symmetry | −g[sin(φ_b−ψ)+sin(φ_s−ψ)] | ≠ 0 | MATCH |
| S4 | ∇²(1/r) (Newton exterior) | 0 | 0 | MATCH |
| S5 | Part 63 S4: ∇²Φ ∝ Φ gives 1/r? | ∇²f/f = m² | 0 | **CONTRADICTION** |
| S6 | Model E solution checks | residuals 0,0,0 | 0 | MATCH |
| S7 | Weak coupling C(2R)/C(R) | 7.9990 | 8 | MATCH |
| S8 | Strong coupling C(2R)/C(R) | 2.0101 | 8 | **CONTRADICTION** |
| S9 | Model E, Δ_∞ = 0: C | 0 | ≠ 0 | **CONTRADICTION** |
| S10 | Model K (confined ψ): C | 0 | ≠ 0 | **CONTRADICTION** |
| S11 | Nonlinear / linear C | 1.00008 | 1 | MATCH |
| S12 | Two-phase vacuum sources a field? | ∇V = 0, eig 2g > 0 | source ≠ 0 | **CONTRADICTION** |
| S13 | Newton 3rd law ψ̈ + 2φ̈₊ | 0 | 0 | MATCH |
| S14 | Jeans positive eigenvalue exists | ±√3·g | > 0 exists | MATCH |

**Score: 9 matches, 5 contradictions out of 14 tests.**

**Sub-group analysis (what the contradictions share):**
- **Group A — screening (S5, S8).** Any term proportional to the field
  itself screens the force. Shared assumption: using the *interior*
  (coupled) equation to describe the field. Fix: the 1/r comes from the
  exterior region where g = 0 (Section 3–4).
- **Group B — no source at rest (S9, S10, S12).** Shared assumption: ψ is
  a fully dynamical field and the coupling depends only on ψ − φ. Together
  these guarantee (Noether) that stationary, ground-state matter carries
  zero net gravitational charge. The single-phase §7 derivation avoided
  this only by holding ψ − φ fixed by hand.

Matches S7 and S11 show that *if* a uniform offset is supplied, Newton's
volume scaling and the linear treatment both hold — so the missing piece is
specifically the offset, nothing else.

**Standard Model compatibility:** no new field or term is introduced here;
the result is a statement about the existing Lagrangians. No gauge,
particle-content, or conservation-law tension is created. (Any future term
that supplies the offset must be run through this check.)

---

## 7. Analysis [SPECULATIVE]

**7.1 This is a known pattern (Goldstone modes).** The free mode φ + ψ is
the Goldstone mode of the joint-shift symmetry
(**Source:** [Goldstone boson — Wikipedia](https://en.wikipedia.org/wiki/Goldstone_boson)).
In particle physics it is well established that a shift-symmetric
(derivatively coupled) massless scalar does **not** produce a
monopole–monopole 1/r force between static sources; such a force appears
only when the shift symmetry is explicitly broken.
**Source:** Moody, J. E. and Wilczek, F. (1984), "New macroscopic
forces?", *Phys. Rev. D* 30, 130 — [DOI](https://doi.org/10.1103/PhysRevD.30.130)
(for the axion, the monopole coupling requires CP violation; the
shift-symmetric coupling alone gives only spin-dependent forces).
Model K is the PDTP version of that statement. The zero mode itself was
already found in Part 133 (Eq 133.2: "cos-difference Lagrangians always
have a center-of-mass zero mode"); what is new here is its consequence
for the Newtonian source.

**7.2 Candidate ingredients that could supply the offset** (each would be
a new term or assumption, so each needs a plan and user approval under the
Problem-Solving Protocol — filed as sub-task 83i, not pursued here):

1. **An intrinsic matter frequency.** If each matter field carried its own
   natural frequency (e.g. the Compton frequency ω_C = mc²/ħ) that the
   coupling had to pull against, a locked state would settle at a nonzero
   offset. In the classic theory of injection locking, the offset of a
   locked oscillator obeys sin Δ = Δω/(locking strength)
   (**Source:** Adler, R. (1946), "A study of locking phenomena in
   oscillators", *Proc. IRE* 34, 351). If Δω scales with mass, so would the
   gravitational charge — exactly what Newton needs. This connects directly
   to T78's finding that PDTP currently *imports* the Compton oscillation
   rather than deriving it, and to T49's Kuramoto framing. It requires an
   explicit shift-symmetry-breaking term for ψ, which the current
   Lagrangians do not have.
2. **A cosmological offset (Δ_∞ as a boundary condition).** Model E with a
   universal Δ_∞ set by cosmology (cf. the Λ-locking fossil, Part 119).
   Weakness: C ∝ Δ_∞ is not proportional to mass in the strong-coupling
   regime (S8), and it gives ψ a tail outside matter.
3. **The φ₋ channel.** The only direction not protected by the joint-shift
   symmetry (Section 5.1 Step 5). Its source vanishes at the vacuum but a
   matter-induced shift away from φ₋ = π/2 (Part 62's m² = 2gΦ) could
   source it. Needs its own calculation.

**7.3 What this does NOT say.** It does not say PDTP cannot produce
gravity. It says the Lagrangians as currently written do not, by
themselves, turn "amount of matter" into "strength of the 1/r field"; an
ingredient doing that job is currently supplied by assumption (§7.5 of
`mathematical_formalization.md`: ρ_phase = Σgᵢ(ψᵢ − φ) with ψᵢ − φ held
fixed). The G = ħc/m_cond² chain (Part 33, vortex winding) was **not**
re-audited here and should be checked against this result.

---

## 8. Impact on Existing Documents

| Document | Status after Part 153 |
|----------|-----------------------|
| `two_phase_rederivation.md` S4 (Part 63) | S4 derivation INVALID (Section 2); erratum note added pointing here; verdict re-scored: 1/r shape PASS via exterior-region argument, strength OPEN |
| `mathematical_formalization.md` §7 | Shape (7.1–7.3) correct; §7.4–7.5 strength requires ψ − φ held fixed [ASSUMED]; caveat note added |
| Part 63 "16/16" | Becomes 15/16 PASS + 1 corrected (S4 conclusion survives via a different argument; its stated derivation does not) |
| Jeans eigenvalue 2√2·g | Wrong magnitude (√3·g), sign survives — sub-task 83b |
| Biharmonic ∇⁴Φ + 4g²Φ | No 1/r tail in any case; coefficient audit — sub-task 83c |

---

## 9. Status and Predictions

- **Status:** 83a DONE — CONSTRUCTIVE NEGATIVE. S4 corrected; 1/r shape
  re-derived correctly; source-strength gap identified and localised to
  one missing ingredient (a maintained ψ − φ offset). New sub-task 83i
  filed for choosing that ingredient.
- **Falsifiable predictions:** none added (no new testable number yet).
  If option 7.2(1) is later adopted, "gravitational charge ∝ detuning"
  would be a candidate prediction — to be planned with the user first.

**Equations added** (to `equation_reference.md`): 153.7 (screening
wavenumber k_Δ² = 2g), 153.10 (Model E monopole), 153.12 (confined-ψ
zero-monopole theorem), 153.13 (time-dependent source identity), 153.14
(two-phase vacuum is a sourceless minimum).

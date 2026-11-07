# Turing Morphogenesis (Reaction–Diffusion) and PDTP — Exploratory Note

**Status:** PRELIMINARY. Recorded for future investigation. NOT a PDTP Part:
no Sudoku scorecard. The linear-stability algebra in §2 and §4 was checked
with SymPy in a scratch script (residuals and thresholds reproduced), but no
repository script exists yet.
**Date:** 2026-11-07 (from a conversation with the user, prompted by a
Jim Al-Khalili video on Turing; written by CLAUDE OPUS 5.5)
**Tracked in:** TODO_05.md **T87**
**Related PDTP results:** Part 154 [jeans_eigenvalue_correction.md](jeans_eigenvalue_correction.md)
(two-phase Jeans instability √3·g), Part 153 (joint-shift Goldstone mode),
TODO_04 T83i (intrinsic matter frequency / offset mechanism), TODO_05 T52
(Kuramoto expanding-lattice simulation)

---

## 1. Plain English Summary

**Turing's idea (1952).** Two chemicals, an *activator* that makes more of
itself and an *inhibitor* that suppresses it, can turn a perfectly uniform
mixture into regular spots or stripes, **if the inhibitor spreads faster than
the activator**. No blueprint is needed. Simple local rules plus tiny random
fluctuations make the pattern, with a spacing set by the reaction and
spreading rates. This is now known to help shape zebrafish stripes, hair
follicles and the spacing of fingers.

**The user's framing for PDTP (2026-11-07).** Treat **spacetime (φ)** as one
"substance" and **matter/atoms (ψ)** as the other. Each is cos-coupled to
*itself* (neighbouring cells of the same substance) and to the *other*
(phase locking). Their interplay is what gives the universe its structure.

**What the math says (first pass):**
1. **PDTP has exactly Turing's structure.** Its self-coupling between
   neighbouring cells *is* its "spreading" term, and its cross-coupling
   g·cos(ψ − φ) is its "reaction" term (§3).
2. **But plain PDTP cannot make a Turing pattern.** Everything in PDTP comes
   from a single energy function (a Lagrangian). That forces the interaction
   to be *symmetric*: φ pulls ψ exactly as ψ pulls φ. Turing patterns need an
   *asymmetric*, activator-versus-inhibitor interaction. A symmetric system
   just relaxes or oscillates (§4, a short theorem).
3. **PDTP's two-phase version does have an instability** (Jeans, Part 154),
   but it grows fastest at the *largest* scales. That gives clumping with
   no preferred spacing, unlike Turing's regular spots (§5).
4. **To get a true Turing pattern**, PDTP would need an ingredient that is not
   from a single energy function. The obvious candidates are already open
   PDTP questions: matter's own intrinsic frequency (T83i, Kuramoto), and
   cosmic-expansion friction (§6). That is the investigation filed as T87.

---

## 2. Turing's Mathematics `[EXTERNAL; algebra SymPy-checked]`

**Source:** Turing, A.M. (1952), "The Chemical Basis of Morphogenesis",
*Phil. Trans. R. Soc. B* 237, 37–72, [doi:10.1098/rstb.1952.0012](https://doi.org/10.1098/rstb.1952.0012);
[Reaction–diffusion system — Wikipedia](https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system);
[Turing pattern — Wikipedia](https://en.wikipedia.org/wiki/Turing_pattern).

### 2.1 The equations

Two concentrations u (activator) and v (inhibitor):

```
du/dt = f(u, v) + D_u lap(u)
dv/dt = g(u, v) + D_v lap(v)                                          (T.1)
```

$$
\partial_t u = f(u,v) + D_u\nabla^2 u,\qquad \partial_t v = g(u,v) + D_v\nabla^2 v
$$

f, g are the **reactions** (local production/destruction). D_u, D_v are the
**diffusion** constants (how fast each spreads).

### 2.2 Linear stability

Take a uniform steady state (u₀, v₀) with f = g = 0. Add a small ripple of
wavenumber k (wavelength 2π/k):

```
(u, v) = (u0, v0) + (U, V) exp(lambda t + i k x)                      (T.2)
```

Linearising (T.1) gives

```
lambda (U, V)^T = J_k (U, V)^T,
J_k = J - k^2 D,   J = [[f_u, f_v], [g_u, g_v]],   D = diag(D_u, D_v)   (T.3)
```

$$
\lambda\begin{pmatrix}U\\V\end{pmatrix} = \left(J - k^2 D\right)\begin{pmatrix}U\\V\end{pmatrix},\qquad J = \begin{pmatrix} f_u & f_v\\ g_u & g_v\end{pmatrix}
$$

J is the Jacobian of the reactions (f_u = ∂f/∂u, etc.). The ripple grows if
some eigenvalue λ has a positive real part. For a 2×2 matrix that happens iff
**tr J_k > 0** or **det J_k < 0**.

### 2.3 Turing's conditions

1. **Stable without diffusion** (k = 0): tr J = f_u + g_v < 0 and
   det J = f_u g_v − f_v g_u > 0.
2. **Unstable with diffusion** for some k > 0. Since tr J_k = tr J − k²(D_u + D_v)
   stays negative, instability must come from det J_k < 0:

```
h(k^2) = D_u D_v k^4 - (D_v f_u + D_u g_v) k^2 + det J < 0           (T.4)
```

$$
h(k^2) = D_uD_v\,k^4 - \left(D_v f_u + D_u g_v\right)k^2 + \det J
$$

h is a parabola in k², with its minimum at

```
k_c^2 = (D_v f_u + D_u g_v) / (2 D_u D_v)                              (T.5)
```

$$
k_c^2 = \frac{D_v f_u + D_u g_v}{2D_uD_v}
$$

Instability requires h(k_c²) < 0, i.e.

```
(D_v f_u + D_u g_v)^2 > 4 D_u D_v det J,   with  D_v f_u + D_u g_v > 0   (T.6)
```

**Reading the conditions:** f_u > 0 (the activator self-enhances) but
f_u + g_v < 0, so g_v must be strongly negative (the inhibitor self-limits).
D_v f_u + D_u g_v > 0 then forces **D_v > D_u: the inhibitor must spread
faster.** The **pattern spacing** is λ_pattern ≈ 2π/k_c, fixed by the rates,
not by the size of the dish.

### 2.4 Worked example (SymPy-checked)

Take f_u = 1, f_v = −1, g_u = 2, g_v = −3/2, D_u = 1, D_v = d.

- tr J = −1/2 < 0 and det J = 1/2 > 0: stable without diffusion ✓
- det J_k = d k⁴ − (d − 3/2) k² + 1/2
- k_c² = (2d − 3)/(4d). Threshold: **d_c = 9/2**. The inhibitor must diffuse
  4.5× faster than the activator.
- At d = 6: k_c² = 3/8, min det J_k = −11/32 < 0, so a band of wavelengths
  around 2π/√(3/8) ≈ 10.3 units grows. **That is the pattern.**

The signs matter: here f_v < 0 (inhibitor suppresses activator) and g_u > 0
(activator produces inhibitor). **The cross-terms have opposite signs.** This
asymmetry is the heart of the mechanism (§4).

### 2.5 Checked against Turing's own paper

Primary source read 2026-11-07 (PDF supplied by the user:
`assets/pdfs/rstb.1952.0012.pdf`). The text extraction is OCR-like and
garbles some formulas, so the equation numbers below are Turing's, read from
the extracted text.

- **Same equations, his notation.** Turing's eq. (7.1) for a continuous ring
  of tissue is dX/dt = a(X−h) + b(Y−k) + μ′∇²X,
  dY/dt = c(X−h) + d(Y−k) + ν′∇²Y. His "marginal reaction rates"
  a, b, c, d are this note's f_u, f_v, g_u, g_v; his diffusibilities μ′, ν′
  are D_u, D_v.
- **Six kinds of instability** (§8): stationary or oscillatory, each with
  extreme-long, extreme-short or finite wavelength. The pattern-forming one
  is **case (d), "stationary waves of finite wave-length"**, and it requires
  **bc < 0** (eq. 9.4). That is exactly the opposite-sign cross-coupling
  condition of §2.4 and §4.
- **His "chemical wave-length"** (§8) is the wavelength of maximum
  instability, independent of the size of the ring. That is our
  2π/k_c (T.5).
- **Where PDTP sits in Turing's scheme.** PDTP's linearised coupling has
  a = d = −g and b = c = +g, so bc = g² > 0 and case (d) is excluded. It
  falls under Turing's case (a), "stationary waves of extreme long
  wave-length", which is unstable only if bc > ad. For PDTP,
  ad = (−g)(−g) = g² = bc **exactly**. PDTP sits precisely on Turing's
  instability boundary, and that marginal mode is the joint-shift Goldstone
  mode (Part 153) [DERIVED from Turing's conditions].

---

## 3. PDTP as a Two-Substance System (user's framing) `[DERIVED, standard steps]`

### 3.1 Self-coupling = the "spreading" term

On a lattice of spacetime cells j with spacing a, cos-coupling each cell to
its neighbour (Kuramoto / XY-model form):

```
V_self = K sum_j [1 - cos(phi_{j+1} - phi_j)]
       ~ K sum_j (phi_{j+1} - phi_j)^2 / 2          (small differences)
       -> (K a^2 / 2) integral (d phi/dx)^2 dx/a                        (T.7)
```

$$
K\sum_j\left[1-\cos(\phi_{j+1}-\phi_j)\right] \;\to\; \frac{K a}{2}\int(\partial_x\phi)^2\,dx
$$

So **the cos-coupling of spacetime to itself is PDTP's gradient
(stiffness) term ½(∂φ)²**, the role diffusion plays in Turing. The same holds
for matter ψ with its own stiffness. (This is how the continuum PDTP Lagrangian
arises from the phase lattice; stiffness K = ℏ/(4πc), term_glossary.md.)

### 3.2 Cross-coupling = the "reaction" term

```
V_cross = - g cos(psi - phi)       (phase locking; +cos is stable, CLAUDE.md)   (T.8)
```

### 3.3 The resulting equations

```
phi_tt = c^2   lap(phi) + g sin(psi - phi)
psi_tt = c_p^2 lap(psi) - g sin(psi - phi)                              (T.9)
```

$$
\ddot\phi = c^2\nabla^2\phi + g\sin(\psi-\phi),\qquad \ddot\psi = c_\psi^2\nabla^2\psi - g\sin(\psi-\phi)
$$

This is Turing's structure (T.1), **"reaction + spreading"**, with one
difference: PDTP has **second time derivatives (waves)**, Turing has first
derivatives (diffusion). The two coincide in an overdamped limit (§6).

---

## 4. Linear Stability of PDTP: No Turing Pattern `[DERIVED; SymPy-checked]`

Linearise (T.9) about the locked state ψ = φ (sin x ≈ x). With modes
∝ exp(λt + ikx):

```
lambda^2 (Phi, Psi)^T = M_k (Phi, Psi)^T,
M_k = [[ -c^2 k^2 - g,   g          ],
       [  g,          -c_p^2 k^2 - g ]]                                  (T.10)
```

$$
\lambda^2\begin{pmatrix}\Phi\\\Psi\end{pmatrix} = \begin{pmatrix}-c^2k^2-g & g\\ g & -c_\psi^2k^2-g\end{pmatrix}\begin{pmatrix}\Phi\\\Psi\end{pmatrix}
$$

Growth needs an eigenvalue μ = λ² > 0. SymPy:

```
tr M_k  = -(c^2 + c_p^2) k^2 - 2g            < 0
det M_k = k^2 [ c^2 c_p^2 k^2 + g (c^2 + c_p^2) ]   >= 0                (T.11)
eigenvalues at k = 0:  { -2g, 0 }
```

$$
\det M_k = k^2\left[c^2c_\psi^2k^2 + g\,(c^2+c_\psi^2)\right] \ge 0
$$

Negative trace and non-negative determinant mean **both μ ≤ 0 at every k**.
Every ripple just oscillates. The single μ = 0 at k = 0 is the joint-shift
Goldstone mode (Part 153). **Different spreading speeds (c ≠ c_ψ) do not
help.** [DERIVED]

**Why: a short theorem.** M_k is *symmetric* (the off-diagonal entries are
both +g). That is automatic whenever all forces come from one potential
energy (a Lagrangian): the "Jacobian" is a Hessian, and Hessians are
symmetric. For any symmetric reaction matrix S = [[a, b], [b, e]] that is
stable at k = 0 (a < 0, e < 0, ae − b² > 0), SymPy gives

```
det(S - q D) = D_u D_v q^2 - (D_u e + D_v a) q + (a e - b^2)          (T.12)
```

Every term is positive for q = k² > 0, so det(S − qD) > 0 always. **No Turing
instability is possible.** Turing needs the cross-terms to have **opposite
signs** (f_v < 0 < g_u, as in §2.4), which a potential can never produce.

> **Plain English:** in PDTP as written, spacetime and matter pull on each
> other *equally and oppositely*, like two balls joined by a spring. A spring
> system can wobble, but it can't spontaneously organise into regular spots.
> Turing's chemicals are different: one *encourages* the other while the
> other *discourages* it back. That one-sidedness is what makes patterns.

---

## 5. The Two-Phase Jeans Instability Is Not a Turing Instability

Part 154 found an unstable branch in the two-phase system:

```
omega^2 = c^2 k^2 - sqrt(3) g    ->   growth rate^2 = sqrt(3) g - c^2 k^2   (T.13)
```

$$
\lambda^2 = \sqrt3\,g - c^2k^2
$$

It is unstable for k < k_J, with the **fastest growth at k → 0**. That is a
*long-wave* instability (gravitational clumping at all large scales), with no
preferred spacing. Turing's instability is a *band* bounded away from k = 0,
whose maximum at k_c ≠ 0 sets a regular spacing. **Different class.**
(The two-phase +cos/−cos sign structure does supply opposite-sign couplings,
which is why it can be unstable at all. See §6, item 3.)

---

## 6. What Could Give PDTP a Turing Band `[SPECULATIVE — to investigate, T87]`

Each item below breaks the "single potential" condition of §4, which is the
precondition for a Turing band:

1. **Matter's intrinsic frequency (non-variational drive).** If matter phases
   rotate at their own frequency ω_m (Compton-type, Adler locking
   sin Δ = Δω/g), the system becomes a driven Kuramoto lattice. That is not a
   gradient system, and phase-oscillator lattices with frequency mismatch are
   known to form travelling waves, spirals and stationary patterns. **Overlaps
   T83i candidate 1 and TODO_05 T52 (Kuramoto expanding lattice).**
2. **Expansion friction (overdamping).** The cosmological equation is
   φ̈ + 3Hφ̇ = c²∇²φ/a² + ... When 3H dominates, φ̈ drops out and

```
3H phi_t ~ (c^2/a^2) lap(phi) + g sin(psi - phi)   ->  D_eff = c^2/(3 H a^2)   (T.14)
```

$$
3H\,\dot\phi \simeq \frac{c^2}{a^2}\nabla^2\phi + g\sin(\psi-\phi)\quad\Rightarrow\quad D_{\rm eff} = \frac{c^2}{3Ha^2}
$$

   That is genuine diffusion form, Turing's (T.1), but still from a potential,
   so it is still not enough on its own (§4). It would need to combine with
   item 1 or 3. If matter and spacetime are damped differently, D_ψ/D_φ ≠ 1
   arises naturally.
3. **Two-phase sign structure.** +g cos(ψ − φ_b) − g cos(ψ − φ_s) gives
   couplings of opposite sign, the ingredient §2.4 needs. Combined with 1
   and/or 2, check whether the unstable set becomes a finite-k band.
4. **Observational target (only if 1–3 give a band).** A Turing mechanism
   predicts a *preferred spacing* λ = 2π/k_c. The obvious large-scale spacing
   in the universe, the BAO scale (~150 Mpc), is already explained by sound
   waves in the early plasma, so it is not a Turing signature. Any PDTP band
   would need a different, so far unexplained, preferred scale. None is known.

---

## 6b. Candidate "Ticking" Frequencies: Planck, Λ and Others `[SPECULATIVE — dimensional]`

*User suggestion (2026-11-07): the Planck constant and the cosmological
constant "almost sound like the ticking frequency". Script:
`simulations/solver/t87_turing_scales.py` (12/12 checks; log in `outputs/`).*

**The Planck constant turns energies into ticking rates** (E = ℏω). Every
mass-energy scale is therefore a frequency, and so a candidate reaction rate
for a PDTP Turing mechanism. The two extremes are:

```
omega_P  = m_P c^2 / hbar   = 1.855e43 s^-1   (Planck; = PDTP omega_gap)
H_Lambda = c sqrt(Lambda/3) = 1.81e-18 s^-1   (cosmological constant)
```

**Identity [DERIVED, SymPy residual 0]:** the dark-energy energy scale is
exactly the geometric mean of these two ticking rates:

```
E_Lambda = (rho_Lambda (hbar c)^3)^(1/4) = hbar sqrt(omega_P H_Lambda) (3/8pi)^(1/4)
         = 2.25 meV      ->   l_Lambda = hbar c / E_Lambda = 88 um      (T.15)
```

$$
E_\Lambda = \hbar\sqrt{\omega_P\,H_\Lambda}\,\left(\frac{3}{8\pi}\right)^{1/4} \approx 2.25\ \mathrm{meV},\qquad \ell_\Lambda = \frac{\hbar c}{E_\Lambda}\approx 88\ \mu\mathrm{m}
$$

This is the well-known statement that the dark-energy scale is the geometric
mean of the Planck and Hubble scales. In PDTP language it is the same fact as
Part 123's Λ ~ (H₀/ω_gap)² (Λ/m_P⁴ = ratio of the two ticking rates, squared).

**Turing spacing for each candidate rate.** If a Turing band existed (it does
not in plain PDTP, §4) with expansion overdamping D_eff = c²/(3H₀) (§6 item 2)
and reaction rate ω, its spacing would be ℓ_T = √(D_eff/ω) (Turing's
"chemical wave-length", up to O(1) factors):

| Reaction rate ω | ω [s⁻¹] | ℓ_T = √(D_eff/ω) |
|---|---|---|
| Planck ω_P (= ω_gap) | 1.86 × 10⁴³ | **27 μm** |
| QCD condensate (367 MeV, Part 37) | 5.6 × 10²³ | 157 km |
| proton Compton | 1.4 × 10²⁴ | 98 km |
| electron Compton | 7.8 × 10²⁰ | 4,200 km |
| dark-energy E_Λ/ℏ | 3.4 × 10¹² | 6 × 10¹⁰ m (0.4 AU) |
| Hubble H₀ / cosmological H_Λ | ~2 × 10⁻¹⁸ | ~10²⁶ m (Hubble radius) |

**The striking row is the first.** With the Planck rate:

```
l_T(omega_P) = sqrt(l_P R_H / 3) = 27 um     [DERIVED, SymPy residual 0]   (T.16)
```

$$
\ell_T(\omega_P) = \sqrt{\tfrac13\,\ell_P\,R_H} \approx 27\ \mu\mathrm{m}
$$

That is **within a factor ~3 of the dark-energy length ℓ_Λ = 88 μm**. It is
also right at the frontier of laboratory gravity tests: the Eöt-Wash torsion
balance has tested Newton's 1/r² law down to **52 μm** separations (Lee et al.
2020), and its predecessor experiment was explicitly a test "below the
dark-energy length scale" (Kapner et al. 2007).

**Honest reading:**
- **This is dimensional, not dynamical.** Planck × Hubble geometric means
  *always* land at ~10–100 μm. (T.16) and (T.15) are the same combination,
  so their agreement is guaranteed up to O(1). It is not evidence for a PDTP
  Turing mechanism.
- **What it does say:** *if* T87's investigation finds a genuine Turing band
  with Planck-rate reactions and Hubble-rate damping, its pattern spacing
  would fall in exactly the range where (i) dark energy's natural length sits
  and (ii) sub-millimetre gravity experiments are currently probing. That
  would make it testable, and it gives T87 a concrete target number.
- **Matter's own ticking rate** (Compton frequency, T83i) gives
  ~100–4000 km. No known structure there, which also makes it a useful
  discriminator.

---

## 7. Next Steps (not started)

1. Linearise PDTP + intrinsic frequency ω_m (item 1) about the
   frequency-locked state; compute the dispersion relation λ(k); look for
   Re λ > 0 at finite k only.
2. Repeat in the overdamped limit (item 2) with separate damping for φ and ψ.
3. Two-phase version (item 3).
4. If a band appears: compute k_c, compare its physical scale with cosmic
   structure, run the Sudoku and two-phase checks, and decide whether it is
   a Part. An honest negative ("PDTP's structure is gradient-like; no
   Turing patterns") is an acceptable outcome.

---

## 8. References

- Turing, A.M. (1952), "The Chemical Basis of Morphogenesis", *Phil. Trans. R.
  Soc. B* 237, 37–72, [doi:10.1098/rstb.1952.0012](https://doi.org/10.1098/rstb.1952.0012)
  (DOI resolves to the Royal Society page; the publisher blocks automated checks.
  Local copy supplied by the user: `assets/pdfs/rstb.1952.0012.pdf`; key
  passages §7–§9 read 2026-11-07)
  - Publisher page (reached via the DOI redirect, verified 2026-11-07):
    [royalsocietypublishing.org — The chemical basis of morphogenesis](https://royalsocietypublishing.org/rstb/article/237/641/37/112910/The-chemical-basis-of-morphogenesis)
  - PDF in this repo: [assets/pdfs/rstb.1952.0012.pdf](https://raw.githubusercontent.com/EmileAvatar/phase-decoupled-physics/main/assets/pdfs/rstb.1952.0012.pdf)
- Lee, J.G., Adelberger, E.G., Cook, T.S., Fleischer, S.M. & Heckel, B.R. (2020),
  "New Test of the Gravitational 1/r² Law at Separations down to 52 μm",
  *Phys. Rev. Lett.* 124, 101101, [arXiv:2002.11761](https://arxiv.org/abs/2002.11761)
- Kapner, D.J. et al. (2007), "Tests of the Gravitational Inverse-Square Law
  below the Dark-Energy Length Scale", *Phys. Rev. Lett.* 98, 021101,
  [arXiv:hep-ph/0611184](https://arxiv.org/abs/hep-ph/0611184)
- Planck Collaboration (2020), "Planck 2018 results. VI. Cosmological
  parameters", *A&A* 641, A6, [arXiv:1807.06209](https://arxiv.org/abs/1807.06209)
  (Λ = 1.1056×10⁻⁵² m⁻² corresponds to the TT,TE,EE+lowE+lensing+BAO set
  H₀ = 67.66, Ω_Λ = 0.6889)
- Sheth, R. et al. (2012), "Hox genes regulate digit patterning by controlling
  the wavelength of a Turing-type mechanism", *Science* 338, 1476 (verified by search)
- [The Chemical Basis of Morphogenesis — Wikipedia](https://en.wikipedia.org/wiki/The_Chemical_Basis_of_Morphogenesis)
- [Turing pattern — Wikipedia](https://en.wikipedia.org/wiki/Turing_pattern)
- [Reaction–diffusion system — Wikipedia](https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system)
- [Morphogenesis — Wikipedia](https://en.wikipedia.org/wiki/Morphogenesis)
- [Kuramoto model — Wikipedia](https://en.wikipedia.org/wiki/Kuramoto_model)

All Wikipedia links were checked on 2026-11-07 to open the intended article.

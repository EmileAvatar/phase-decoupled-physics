# Primordial Magnetic Fields from PDTP? — Scoping (Part 159)

**TODO:** TODO_05.md **T84**. Worked by **CLAUDE OPUS 5.5** (`claude-opus-5-5`),
2026-11-07. A TODO_05 item, done ahead of the queue at the user's request.
**Script:** `simulations/solver/t84_pmf_scoping.py`
**Log:** `simulations/solver/outputs/t84_pmf_scoping_<timestamp>.txt`
**Scorecard:** 11 matches, 5 contradictions out of 16 tests. The
contradictions are the NO-GO findings.
**Verdict:** **NO-GO** for PDTP making the 5–10 pG fields of Jedamzik,
Pogosian & Abel (2025), with the field content PDTP has today. The one
symmetry-allowed coupling (axion-type φ·E·B) is safe from every bound but
far too weak at PDTP's natural winding. As a by-product, the same
calculation gives a clean statement about **CMB cosmic birefringence**
(§7). This is a scoping note only: no coupling is adopted.

---

## Plain-English Summary

**The question.** A 2025 paper finds weak primordial magnetic fields (about a
trillionth of a fridge magnet) that partly ease the Hubble tension, but nobody
knows where they came from. Could PDTP's spacetime phase φ have made them?

**Step 1: as written, no.** Nothing in the PDTP Lagrangian connects φ to light
(the electromagnetic field). Maxwell's equations are linear, so with no source
they make **zero** magnetic field. Any mechanism needs a new connecting term.

**Step 2: three possible connecting terms, two ruled out.**
- **(a) Make φ electrically charged.** This turns spacetime into a
  superconductor and gives the photon a mass about 10²⁷ eV. Experiments say
  the photon mass is below roughly 10⁻¹⁴ eV, so this fails by **41 orders of
  magnitude**. Ruled out.
- **(b) Let φ change the strength of electromagnetism** (a "dilaton" coupling,
  the kind used in inflation models). This breaks PDTP's basic symmetry
  (shifting φ by a constant changes nothing). A version built from the
  *locking offset* ψ − φ keeps the symmetry, but it can only vary the strength
  by a bounded amount, which is far too little to amplify fields. It would also
  make gravity act differently on different materials, which MICROSCOPE rules
  out at the 10⁻¹⁵ level. Ruled out as a field generator.
- **(c) An "axion-like" coupling** (φ·E·B). This keeps the symmetry exactly,
  and at PDTP's natural (Planck) strength it is a hundred billion times below
  every experimental limit. **It survives.**

**Step 3: the survivor is far too weak.** A changing φ can amplify one twist
direction of magnetic field exponentially. The math gives a strikingly simple
answer: the amount of amplification (in e-folds) is

```
N = (alpha / 4 pi) * (total phase change of phi, in radians)
```

That's **independent of how strong the coupling is or how fast φ turns**. To
get even one e-fold (the bare minimum for a real field), φ must wind through
about **1,700 radians (274 full turns)** in one consistent direction. PDTP's
early-universe phase transition gives about **one turn** per patch, in random
directions. That gives N ≈ 0.004. **NO-GO.**

**Step 4: the bonus result.** The *same* formula gives how much the coupling
would rotate the polarization of the CMB ("cosmic birefringence"). There is a
real 3.6σ hint of a 0.34° rotation in Planck + WMAP data. PDTP's vacuum phase
sits still once it is locked, so with this coupling PDTP predicts **zero**
rotation. If the 0.34° hint becomes a firm detection, it cannot come from PDTP
through this coupling unless φ unwound by about 10 radians after recombination.
And if PDTP's vacuum phase were spinning at the condensate frequency (as in a
laboratory BEC), the rotation would be about 10⁵⁷ radians. So **PDTP's vacuum
phase cannot be spinning** if any such coupling exists.

---

## 1. Setup [ASSUMED]

PDTP (CLAUDE.md) as written:

```
L_PDTP = 1/2 (d phi)^2 + sum_i 1/2 (d psi_i)^2 + sum_i g_i cos(psi_i - phi)   (159.1)
```

$$
\mathcal{L}_{\rm PDTP} = \tfrac12(\partial\phi)^2 + \sum_i \tfrac12(\partial\psi_i)^2 + \sum_i g_i\cos(\psi_i-\phi)
$$

It contains no electromagnetic field A_μ. Maxwell's equations ∂_μF^{μν} = J^ν
with J = 0 from PDTP are linear and sourceless, so PDTP generates **B = 0**
[DERIVED, by inspection].

PDTP's symmetry: L is invariant under the joint shift ψᵢ → ψᵢ + c, φ → φ + c
(Parts 133/153). In vacuum (no ψ), φ → φ + c alone is a symmetry, so φ is a
Goldstone mode. Any new coupling must keep this, or PDTP loses its zero mode.

Natural decay constant [ASSUMED, term_glossary.md K]: the stiffness
K₀ = 1/(4π) per Planck cell gives

```
f_phi = sqrt(2 K_0) m_P = 0.399 m_P = 4.87e18 GeV                    (159.2)
```

$$
f_\phi = \sqrt{2K_0}\,m_P \approx 0.399\,m_P = 4.87\times10^{18}\ \mathrm{GeV}
$$

(§3.4 shows the final answer does not depend on f_φ.)

---

## 2. Coupling (a): charged φ [NEGATIVE]

Make φ the phase of a charged field Φ = v e^{iφ} with
L = ½|(∂_μ − ieA_μ)Φ|²:

```
Step 1: D_mu Phi = (i d_mu phi - i e A_mu) v e^{i phi}
Step 2: |D Phi|^2 = v^2 (d_mu phi - e A_mu)^2
Step 3: L = 1/2 v^2 (d phi)^2 - e v^2 A.d phi + 1/2 e^2 v^2 A^2
Step 4: photon mass m_A^2 = e^2 v^2                                      (159.3)
```

$$
m_A = e\,v
$$

[DERIVED; VERIFIED: S1, SymPy residual 0]. This is the Higgs mechanism: φ is
"eaten" by the photon. With v = f_φ and e = √(4πα) = 0.303:

```
m_A = 0.303 * 4.87e18 GeV = 1.47e27 eV  vs  bound ~2.2e-14 eV  ->  x 6.7e40
```

**NO-GO** by about 41 orders of magnitude (S2), even against the most lenient
bound in the PDG photon listings. Worse, the gauging would remove φ as an
independent mode, i.e. remove PDTP's gravity mode itself.

---

## 3. Couplings (b) and (c)

### 3.1 (b) Dilaton-type −¼ f(φ) F² [NEGATIVE]

Under φ → φ + c: f(φ + c) − f(φ) ≠ 0 for any non-constant f (S3,
residual −f(φ) + f(c + φ)). This breaks PDTP's shift symmetry. [NEGATIVE]

**(b′) the locking-offset version −¼ f(ψ − φ) F²** is joint-shift invariant
(S4, residual 0) but:
1. f takes values only over one period of ψ − φ, so f_max/f_min is a fixed
   finite number. Ratra-type magnetogenesis needs f to change by many
   e-folds. **Bounded variation means no exponential amplification.**
2. It makes α depend on the local locking offset, i.e. on the environment.
   That gives composition-dependent free fall, which MICROSCOPE bounds at
   η ~ 10⁻¹⁵. Not quantified here.

[NEGATIVE as a field generator; recorded, not adopted.]

### 3.2 (c) Axion-type: the shift symmetry is kept exactly [DERIVED]

```
L_c = 1/2 (E^2 - B^2) + g_pg a E.B,    a = f_phi phi                    (159.4)
```

$$
\mathcal{L}_c = \tfrac12(E^2-B^2) + g_{\phi\gamma}\,a\,\mathbf{E}\cdot\mathbf{B},\qquad a = f_\phi\,\phi
$$

E·B ∝ ε^{μνρσ}F_μνF_ρσ, and

```
eps^{mnrs} F_mn F_rs = 4 d_m ( eps^{mnrs} A_n d_r A_s )                  (159.5)
```

$$
\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = 4\,\partial_\mu\!\left(\epsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma\right)
$$

[VERIFIED: S5, SymPy for arbitrary A_μ(x⁰…x³), residual 0]. So under
φ → φ + c the change in L is a total derivative and the equations of motion
are unchanged. **The PDTP shift symmetry survives exactly.** It is the only
one of the three couplings that does.

Natural strength [ASSUMED, standard axion normalisation, C = O(1)]:

```
g_pg = alpha C / (2 pi f_phi) = 2.38e-22 GeV^-1   (C = 1)               (159.6)
```

$$
g_{\phi\gamma} = \frac{\alpha C}{2\pi f_\phi} \approx 2.4\times10^{-22}\ \mathrm{GeV^{-1}}
$$

That is 3.6 × 10⁻¹² of the CAST limit 0.66 × 10⁻¹⁰ GeV⁻¹ (S12). **Allowed.**

### 3.3 Mode equation, growth and rotation [DERIVED, VERIFIED]

Radiation gauge A₀ = 0, E = −∂ₜA, B = ∇×A, homogeneous a(t), waves along z.
The Euler–Lagrange equations of (159.4) (SymPy `euler_equations`), with the
helical ansatz A = u(t)(cos kz, ∓ sin kz, 0) (so ∇×A = ±kA), give

```
u'' + (k^2 -/+ s k) u = 0,     s = g_pg * da/dt                         (159.7)
```

$$
\ddot u_\pm + \left(k^2 \mp s\,k\right)u_\pm = 0,\qquad s = g_{\phi\gamma}\,\dot a
$$

[VERIFIED: S6, both helicities, residual 0; S7, s → 0 gives ω = k].

**Growth.** For 0 < k < s, the + helicity is tachyonic with rate
Γ(k) = √(sk − k²). Maximising, dΓ²/dk = s − 2k = 0:

```
k* = s/2,     Gamma_max = s/2                                          (159.8)
```

[VERIFIED: S8]

**Rotation.** For k ≫ s: ω± = √(k² ∓ sk) ≈ k ∓ s/2, so the polarization plane
rotates at (ω₋ − ω₊)/2 → s/2 [VERIFIED: S9, SymPy limit k → ∞].

**The growth rate and the rotation rate are the same number, s/2.**

### 3.4 The key formula [DERIVED, VERIFIED]

Integrating over the time φ moves:

```
N = integral Gamma_max dt = (g_pg/2) Delta a = (g_pg f_phi/2) Delta phi
  = (alpha C / 4 pi) * Delta phi                                       (159.9)

theta_CB = (alpha C / 4 pi) * Delta phi   (same formula)                (159.10)
```

$$
N = \theta_{\rm CB} = \frac{\alpha C}{4\pi}\,\Delta\phi
$$

[VERIFIED: S10, ∂N/∂f_φ = 0; S11, residual 0]. **f_φ cancels.** The answer
depends only on how many radians φ turns, not on the coupling scale and not on
how fast it turns. (The rotation formula agrees with Harari & Sikivie 1992 for a
Nambu–Goldstone boson.) Consequences:

- The T83 inertia-2 normalisation family cannot affect this result. For φ₊
  (inertia 2, f₊ = √2 f), N is unchanged (S14).
- N ≥ 1, the bare minimum for any classical field (assumption A2; necessary,
  not sufficient), needs

```
Delta phi >= 4 pi / alpha = 1722 rad = 274 turns, coherent              (159.11)
```

---

## 4. Results (Data)

| Quantity | Value | Source |
|---|---|---|
| f_φ | 4.87 × 10¹⁸ GeV | (159.2) |
| g_φγ (C = 1) | 2.38 × 10⁻²² GeV⁻¹ (3.6 × 10⁻¹² of CAST) | (159.6) |
| (a) photon mass | 1.47 × 10²⁷ eV (6.7 × 10⁴⁰ × lenient bound) | (159.3) |
| N needed ≥ 1 | Δφ ≥ 1722 rad (274 turns) | (159.11) |
| N from Kibble–Zurek (Δφ ≈ 2π, Part 116) | **0.0036** | (159.9) |
| θ_CB, static locked vacuum | **0** | (159.10) |
| θ_CB, vacuum phase rotating at ω_gap = 1.85 × 10⁴³ s⁻¹ for 13.8 Gyr | **4.7 × 10⁵⁷ rad** | (159.10) |
| Δφ needed for the 0.342° hint | 10.3 rad (after recombination) | (159.10) |
| ρ_B/ρ_γ needed at recombination (b_rec = 0.0545–0.104 nG) | 2.8 × 10⁻¹⁰ – 1.0 × 10⁻⁹ | Jedamzik+ Table IV |

The last row is a benchmark for any future mechanism: about one part in a
billion of the radiation energy must sit in kpc-coherent magnetic fields at
recombination.

---

## 5. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|---|---|---|---|---|
| S1 | (a) m_A² = e²v² | 0 | 0 | MATCH |
| S2 | (a) photon mass ≤ 2.2 × 10⁻¹⁴ eV | 1.47 × 10²⁷ eV | ≤ bound | CONTRADICTION |
| S3 | (b) f(φ)F² shift-invariant | −f(φ)+f(c+φ) | 0 | CONTRADICTION |
| S4 | (b′) f(ψ−φ)F² joint-shift invariant | 0 | 0 | MATCH |
| S5 | (c) εFF is a total derivative | 0 | 0 | MATCH |
| S6 | (c) mode equation, both helicities | (0, 0) | (0, 0) | MATCH |
| S7 | s → 0: ω = k | 0 | 0 | MATCH |
| S8 | Γ_max = s/2 at k = s/2 | (s/2, s/2) | (s/2, s/2) | MATCH |
| S9 | growth rate = rotation rate | 0 | 0 | MATCH |
| S10 | f_φ cancels | 0 | 0 | MATCH |
| S11 | N = αCΔφ/(4π) | 0 | 0 | MATCH |
| S12 | g_φγ below CAST | 2.38 × 10⁻²² | < 6.6 × 10⁻¹¹ | MATCH |
| S13 | KZ winding gives N ≥ 1 | 3.65 × 10⁻³ | ≥ 1 | CONTRADICTION |
| S14 | two-phase φ₊: N unchanged | 3.649 × 10⁻³ | 3.649 × 10⁻³ | MATCH |
| S15 | rotating vacuum: θ_CB ≤ obs + 3σ | 4.7 × 10⁵⁷ rad | ≤ 0.0107 rad | CONTRADICTION |
| S16 | static vacuum θ_CB vs 0.342° hint | 0° | 0.342 ± 0.09° | CONTRADICTION |

**11 matches, 5 contradictions out of 16.** Sub-groups: S2 and S3 kill
couplings (a) and (b). S13 kills (c) as a field generator at PDTP's natural
winding. S15 excludes a spinning PDTP vacuum if (c) exists. S16 is a 3.6σ
*tension with a hint*, not a refutation (§7).

---

## 6. Two-Phase and Standard Model Checks

**Two-phase.** In the two-phase theory the axion coupling could sit on
φ₊ = (φ_b + φ_s)/2 or on φ₋.
- **φ₊:** inertia 2 rescales f, which cancels in (159.9) (S14). Same answer.
- **φ₋:** it sits at its vacuum π/2 with present displacement ~10⁻⁷⁰ rad
  (Part 87), so Δφ₋ ≈ 0, giving N ≈ 0 and θ_CB ≈ 0.

None of the two-phase results (ψ̈ = −2φ̈₊, Jeans √3·g, biharmonic) involve
A_μ, so they are untouched.

**Standard Model.**
- (a) **breaks** gauge structure (Higgs-like photon mass): TENSION, rejected.
- (b), (b′) keep gauge invariance; (b′) changes α with environment (EP tests).
- (c) keeps gauge invariance and adds no particles beyond φ itself (already
  massless in PDTP). It is CP-odd, like the QCD axion term. Compatible.

---

## 7. Cosmic Birefringence [SPECULATIVE — conditional on coupling (c)]

If PDTP's φ couples to photons as in (159.4), then (159.10) gives the
isotropic CMB polarization rotation from φ's change since recombination:

- **PDTP's locked vacuum is static.** The homogeneous mode obeys
  φ̈ + 3Hφ̇ = Σgᵢ sin(ψᵢ − φ). With locking (sin = 0), any φ̇ decays as a⁻³.
  So θ_CB ≈ 0.
- **The current hint:** θ_CB = 0.342° ± 0.09° (Planck + WMAP; 3.6σ;
  Eskilt & Komatsu 2022). If it is confirmed, PDTP-with-(c) can produce it
  only if φ (or φ₊) unwound by about **10 radians after recombination**, which
  PDTP does not currently give.
- **A spinning vacuum is excluded.** A BEC-like vacuum rotating at ω_gap
  would give θ_CB ~ 10⁵⁷ rad. So *if* (c) exists, PDTP's vacuum phase must
  not rotate. This is consistent with the Lagrangian's own static solution,
  and it constrains any future "phase drift" reinterpretation of expansion.

**The window any PDTP magnetogenesis scenario would need:**

```
Delta phi (before recombination) >= ~1700 rad,  coherent      (N >= 1)
Delta phi (after recombination)  <= ~30 rad                    (theta_CB <= ~1 deg)
```

**Prediction (ADDED to falsifiable_predictions.md as Prediction 17, Eq. F.29–F.30,
with user approval 2026-11-07):** "If PDTP's phase couples to photons at all, it does so
through φ·E·B, and the static locked vacuum predicts zero isotropic cosmic
birefringence (θ_CB = 0). A ≥ 5σ confirmation of θ_CB ≈ 0.34° would require
post-recombination winding Δφ ≈ 10 rad, absent in current PDTP." Test: LiteBIRD,
Simons Observatory and CMB-S4 polarization-angle measurements. Distinguishes
from: axion-like early-dark-energy and quintessence models, which can produce
θ_CB ≠ 0.

---

## 8. Status

- **T84 DONE (scoping): NO-GO** with current field content. (a) and (b)
  rejected; (b′) bounded; (c) allowed but N = 0.0036 ≪ 1 at the KZ winding.
- **Open, not filed as a new item:** a PDTP epoch with coherent winding of
  ≳ 1700 rad before recombination (none is known); quantitative MHD evolution
  (only needed if such an epoch appears); the helical-vs-non-helical point
  (moot while N ≪ 1).
- **Birefringence statement:** added as Prediction 17 in
  `falsifiable_predictions.md` (user-approved 2026-11-07).

---

## Sources

- Jedamzik, K., Pogosian, L. & Abel, T. (2025), *Nature Astronomy*,
  [arXiv:2503.09599](https://arxiv.org/abs/2503.09599) (5–10 pG; Table IV b_rec)
- Harari, D. & Sikivie, P. (1992), "Effects of a Nambu-Goldstone boson on the
  polarization of radio galaxies and the cosmic microwave background",
  *Phys. Lett. B* 289, 67
- Carroll, S.M., Field, G.B. & Jackiw, R. (1990), "Limits on a Lorentz- and
  parity-violating modification of electrodynamics", *Phys. Rev. D* 41, 1231
- Eskilt, J.R. & Komatsu, E. (2022), "Improved constraints on cosmic
  birefringence from the WMAP and Planck CMB polarization data",
  [arXiv:2205.13962](https://arxiv.org/abs/2205.13962) (θ = 0.342° ± 0.09°, 3.6σ)
- CAST Collaboration (2017), "New CAST limit on the axion–photon interaction",
  *Nature Physics* 13, 584, [arXiv:1705.02290](https://arxiv.org/abs/1705.02290)
  (g < 0.66 × 10⁻¹⁰ GeV⁻¹)
- MICROSCOPE Collaboration (2022), *Phys. Rev. Lett.* 129, 121102,
  [arXiv:2209.15487](https://arxiv.org/abs/2209.15487) (η ~ 10⁻¹⁵)
- Particle Data Group, photon listings (photon mass bounds 10⁻¹⁹–10⁻¹⁴ eV
  depending on method), e.g. [PDG 2021](https://pdg.lbl.gov/2021/listings/rpp2021-list-photon.pdf)
- Ratra, B. (1992), "Cosmological 'seed' magnetic field from inflation",
  *ApJ* 391, L1
- Vachaspati, T. (1991), *Phys. Lett. B* 265, 258
- [Higgs mechanism — Wikipedia](https://en.wikipedia.org/wiki/Higgs_mechanism) ·
  [Axion — Wikipedia](https://en.wikipedia.org/wiki/Axion)

**PDTP Original:** (159.9)–(159.11) applied to PDTP: amplification exponent
equals birefringence angle, both αΔφ/4π, independent of f_φ; the KZ estimate
N ≈ 0.004; the static-vacuum θ_CB = 0 statement; the spinning-vacuum exclusion.

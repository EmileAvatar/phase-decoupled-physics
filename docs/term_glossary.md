# PDTP Term and Symbol Glossary

**Purpose:** Complete reference of every symbol, variable, and named concept used
in PDTP research docs, scripts, and TODO files. Written so a new reader — or a
returning collaborator — can identify any term without hunting through old Parts.
**Every dimensioned symbol now carries an explicit SI Units column** (added
2026-09-06, folding in what would otherwise have been a separate SI_Units.md —
see the Maintenance rule below for why this file is the single source of truth).

**Location note:** moved from `docs/technical/term_glossary.md` to
`docs/term_glossary.md` (2026-09-06) — kept next to `Methodology.md` and its
companions since, like them, it is a project-wide working reference consulted
constantly, not a topic-specific technical doc.

**Companion files:**
- `docs/technical/glossary.md` — plain-English conceptual glossary (start here if new;
  checked 2026-09-06, still accurate — no units or equations to go stale)
- `docs/research/equation_reference.md` — all equations with status tags
- `docs/research/g_units_audit_scoping.md` — T68's full units audit; source of
  the corrections in Section 4 below
- `CLAUDE.md` — project rules and standards

**Maintenance rule:** Update this file whenever a new symbol or named concept is
introduced to the framework — including its SI units. **Before using any symbol
in a new derivation, check here first** that it is not already in use for a
different quantity (see Section 4 for what happens when that check is skipped).
One row per symbol is enough.

---

## 1. The Two Core Fields

Everything in PDTP is built from two kinds of oscillating fields — two sets of
"clocks" that can pull each other into sync. Gravity IS the syncing.

| Symbol | LaTeX | Name | What it is |
|--------|-------|------|-----------|
| **φ** | `\phi` | Spacetime phase field | The "clock angle" of the spacetime condensate at each point in space. The medium that carries gravity. Single scalar in U(1); 3×3 matrix in SU(3). |
| **ψ** | `\psi` | Matter phase field | The "clock angle" of a matter particle (electron, proton, etc.). Every particle has its own ψ. |
| **Δ** | `\Delta` | Phase gap | Δ = ψ − φ. How far out of sync matter and spacetime are. Δ=0 means fully locked (maximum gravity). Δ=π/2 means fully decoupled (zero gravity — the Leidenfrost point). |
| **α** | `\alpha` | Coupling strength | α = cos(Δ). Ranges from 1 (fully locked, normal gravity) to 0 (fully decoupled). The core physical quantity in PDTP. |

---

## 2. The Two-Phase Extension (Part 61)

The single φ field splits into two components when surface effects are included —
like a superfluid having a bulk interior and a surface layer.

| Symbol | LaTeX | Name | What it is |
|--------|-------|------|-----------|
| **φ_b** | `\phi_b` | Bulk phase | Interior gravity condensate. Appears in the +cos term of the Lagrangian. Responsible for gravitational attraction. |
| **φ_s** | `\phi_s` | Surface phase | Surface condensate. Appears in the −cos term. Responsible for surface tension / short-range repulsion. |
| **φ₊** | `\phi_+` | Gravity mode | φ₊ = (φ_b + φ_s)/2. The average of the two condensates. Locking ψ to φ₊ produces Newton's law. |
| **φ₋** | `\phi_-` | Surface mode | φ₋ = (φ_b − φ_s)/2. The difference of the two condensates. Massless in vacuum; gains mass near matter (reversed Higgs). Also the dark energy field. |
| **Δ₊** | `\Delta_+` | Gravity coupling gap | Δ₊ = ψ − φ₊. Phase gap for the gravity channel. At Δ₊ = π/2 the system hits the Leidenfrost decoupling transition. |
| **Δ₋** | `\Delta_-` | Surface mode phase | Δ₋ = φ₋. The surface mode's own phase angle. Controls dark energy and surface coupling. |
| **β** | `\beta` | Partial lock angle | How far the universe is from fully locked. β=0 means perfectly synced (today, full lock). β≠0 means still syncing (early universe, partial lock). Key variable in the EDE term (Part 117). |
| **χ** | `\chi` | Phase shift variable | χ = φ₊ + π/2. A change of variable that maps two-phase equilibrium (Δ₊=π/2) exactly onto single-phase equations (Δ_χ=0). Proved all 16 single-phase results survive in two-phase (Part 63). |

---

## 3. Mass and Energy Parameters

| Symbol | LaTeX | Name | SI Units | Value / Definition | What it is |
|--------|-------|------|----------|--------------------|-----------|
| **m_cond** | `m_\text{cond}` | Condensate quantum mass | kg | = m_P (set by observed G) | Mass of one "grain" of spacetime. PDTP's one free parameter. Everything gravitational follows from this single number. Cannot be derived internally (Part 115 no-go theorem — proven). |
| **m_P** | `m_P` | Planck mass | kg | ≈ 2.176×10⁻⁸ kg ≈ 22 μg | The natural scale where quantum mechanics and gravity meet. Absurdly heavy for a particle — that absurdity IS the hierarchy problem. |
| **m_cond_QCD** | `m_{\text{cond,QCD}}` | QCD-condensate quantum mass | kg (or MeV/c²) | ≈ 367 MeV/c² [Part 37] | The analogous "grain mass" for the SEPARATE QCD-layer condensate (not the gravitational one) — inferred from matching the SU(3) string tension. Coincidentally close to M₀ and m_p/3 (unexplained). |
| **m_DM** | `m_\text{DM}` | Dark matter particle mass | kg | = m_P = m_cond [DERIVED, Part 116] | Mass of the dark matter candidate. No longer a free parameter — vortex stability forces winding n=1, so m_DM = m_cond. Two independent derivations (energy argument + Kibble-Zurek Monte Carlo). |
| **m_e** | `m_e` | Electron mass | kg | ≈ 9.109×10⁻³¹ kg | Standard electron mass. Used in winding number and hierarchy ratio calculations. |
| **m_p** | `m_p` | Proton mass | kg | ≈ 1.673×10⁻²⁷ kg | Standard proton mass. Note: lower-case m_p = proton; upper-case m_P = Planck mass. |
| **M** | `M` | Body mass | kg | Context dependent | Large mass in gravity calculations (Earth, Sun, black hole). Not to be confused with m_cond. |
| **M₀** | `M_0` | Koide mass scale | kg (or MeV/c²) | ≈ 313.84 MeV ≈ m_p/3 | Base mass in the Koide lepton formula. Close to m_p/3 (0.3% match) and to m_cond_QCD = 367 MeV (Part 37). Origin of this coincidence is open. |
| **E_P** | `E_P` | Planck energy | J (or GeV) | = m_P·c² ≈ 1.22×10¹⁹ GeV | The energy equivalent of the Planck mass. Same information as m_P, expressed as an energy. |

---

## 4. Coupling Constants — CORRECTED 2026-09-06 (TODO_05 T68)

**Read this box before using any "g" symbol anywhere in the project.**
T68 (`docs/research/g_units_audit_scoping.md`) found that "g" had been
used for at least three related-but-distinct quantities across the
project's history, all informally treated as if dimensioned `1/s` or
`1/s²`. The actual bare Lagrangian coupling has SI units **1/length²**.
The historical `1/time²`-labeled quantities (g_Λ, g_dyn below) are each
`c² × (a bare coupling)` — not errors in their own numerical results
(each was self-consistently derived and calibrated within its own
context), but not literally the same object as the bare g either. **Do
not substitute one row of this table for another without re-deriving the
c-factor relating them** — that mistake is exactly what T68 spent a full
audit untangling.

| Symbol | LaTeX | Name | SI Units | Value / Definition | What it is |
|--------|-------|------|----------|--------------------|-----------|
| **g** or **gᵢ** | `g_i` | Bare phase-locking coupling | **1/length² (m⁻²)** — corrected from an earlier "[rad/s]" claim | `g_bare = ω_gap²/c²` | The TRUE dimension of the coupling in `L = g·cos(ψ−φ)` and `□φ = g·sin(ψ−φ)`, re-derived directly from the field equation (SymPy-verified, `t68_g_units_field_equation.py`). Strength of the cos(ψ−φ) coupling for particle i. |
| **ω_gap** | `\omega_\text{gap}` | Breathing-mode gap frequency | 1/time (s⁻¹) | = m_cond·c²/ℏ ≈ 1.86×10⁴³ rad/s [Part 33/94] | A genuine angular frequency (E=ℏω). **NOT the same dimension as bare g** — historically written "g = ω_gap" (Part 94 Eq 94.1), which is now understood as a labeling shorthand, not a literal dimensional identity. See also T72 (open): Part 99's pendulum equation separately implies ω_gap² = 2g_pendulum for a possibly-different "ω_gap" — not yet reconciled with Part 94's. |
| **g_Λ** | `g_\Lambda` | Lambda-formula coupling | 1/time² (s⁻²) | = 3·Ω_Λ·ω_gap² ≈ 7.07×10⁸⁶ s⁻² [Part 128/T51] | The coupling that correctly reproduces Λ_obs when used in `Λ = g_Λ·φ₋_vac²/c²`. Equals `c² × (bare coupling for the Λ context)` — carries the same "1/time²" mislabeling as historically written, but its own Λ-matching result is unaffected (the formula's explicit `/c²` already supplies the correction). NOT the same physical quantity as g_dyn (differ by 122 orders — T51 Eq T51.4). |
| **g_dyn** | `g_\text{dyn}` | Present-epoch dynamical coupling | 1/time² (s⁻²) | = 9·H₀²·ε₀/2 ≈ 2.03×10⁻³⁶ s⁻² [Part 119/T51] | Governs φ₋'s present-day mass (m² = 2·g_dyn) and the freeze condition (m<H ⟺ ε<1/9). Calibrated by fitting DESI w₀ data through the (historically c²-incomplete, but self-consistently used) slow-roll formula — its own numerical value and every Part 119 result built on it are correct and unaffected by T68. Traces to the SAME missing-c² bug as g_Λ, at its root in Part 99's Eq 99.1 (T68 Section 7d) — NOT a coincidence that it shares the letter g. |
| **G** or **G_N** | `G` | Newton's gravitational constant | m³·kg⁻¹·s⁻² | ≈ 6.674×10⁻¹¹ m³/(kg·s²) | Standard measured gravity. DERIVED in PDTP as G = ℏc/m_cond² [Part 33], but remains a free parameter because m_cond is free. |
| **G_eff** | `G_\text{eff}` | Effective Newton's constant | m³·kg⁻¹·s⁻² | = 2·G_bare [DERIVED, Part 61] | In the two-phase system, effective gravity is twice the bare coupling. The factor of 2 is derived from Newton's 3rd law (ψ̈ = −2φ̈₊). |
| **K** | `K` | Lattice stiffness | J (or dimensionless in natural units) | = ℏ/(4πc) | Stiffness of the condensate medium. Sets how rigid spacetime is. Dimensionless in natural units: K₀ = 1/(4π) ≈ 0.0796. |
| **g_GP** | `g_\text{GP}` | Gross-Pitaevskii interaction | J·m³ | = ℏ³/(m_cond²·c) [DERIVED, Part 34] | Interaction constant in the BEC description of the condensate. Equivalent to the scattering length in a real superfluid. |
| **λ₄** | `\lambda_4` | Quartic coupling (EDE term) | 1/length² (matches bare g, since kbar²=2g uses the same dimension — Part 117, T68 Section 7c) | = 2g²sin²(β)/(3k̄²) [DERIVED, Part 117] | The Early Dark Energy term. Positive, generated by the existing Lagrangian at partial lock. Self-switches off as β→0 (full lock today), giving w=−1 automatically. No new physics required. Part 117 stays entirely symbolic/ratio-based and never substitutes a numeric g — unaffected by T68's correction, and independently confirms it (see k̄ below). |
| **σ** | `\sigma` | String tension | GeV² (energy²; ~ 1/length² in natural units) | ≈ 0.173 GeV² (PDTP SC) | Energy per unit length of a quark flux tube. QCD measured: 0.18 GeV². PDTP strong-coupling formula is 4% off (Parts 37–41). |
| **k̄** | `\bar{k}` | Reference wavenumber | 1/length (m⁻¹) | Context dependent; at the two-phase gap scale, k̄² = 2g | Wavenumber scale in the EDE quartic (Part 117) — a genuine spatial wavenumber from the φ₊ kinetic term. Its identification k̄²=2g is dimensionally consistent with `[g]=1/length²` (both 1/length²) — an independent confirmation of the corrected g dimension, found without ever computing a numeric g. |

---

## 5. Length and Frequency Scales

| Symbol | LaTeX | Name | SI Units | Value | What it is |
|--------|-------|------|----------|-------|-----------|
| **a₀** | `a_0` | Condensate lattice spacing | m | = ℏ/(m_cond·c) = l_P | Distance between adjacent "grains" of spacetime. Equals the Compton wavelength of m_cond = Planck length. |
| **ξ** | `\xi` | Healing length | m | = a₀/√2 ≈ 0.707·a₀ [DERIVED, Part 34] | How far a disturbance in the condensate spreads before healing back. The condensate's coherence length (BEC physics). |
| **l_P** | `l_P` | Planck length | m | ≈ 1.616×10⁻³⁵ m | Smallest meaningful length scale. In PDTP = a₀ (they are the same thing). |
| **t_P** | `t_P` | Planck time | s | ≈ 5.39×10⁻⁴⁴ s | Planck length / c. The condensate oscillation period at m_cond. |
| **ω_gap** | `\omega_\text{gap}` | Breathing mode gap | 1/time (s⁻¹) | = m_cond·c²/ℏ ≈ 1.86×10⁴³ rad/s [DERIVED, Part 33] | Minimum frequency the spacetime condensate can oscillate at. Like the lowest "note" of spacetime. 43 orders above LISA — undetectable directly. **See Section 4 above — NOT the same dimension as the bare coupling g** (corrected 2026-09-06, T68). |
| **L_H** | `L_H` | Hubble radius | m | ≈ 1.3×10²⁶ m | Size of the observable universe. A cosmological INPUT to PDTP — not derived internally. |
| **Φ** | `\Phi` | Newtonian gravitational potential | dimensionless | = GM/(rc²) | Dimensionless gravity depth. Earth surface: ≈ 7×10⁻¹⁰. Neutron star: ≈ 0.2. Black hole horizon: = 0.5. Used in the Schwarzschild mapping sin(Δ₊) = √(2Φ). |
| **H, H₀** | `H, H_0` | Hubble rate (present-day: H₀) | 1/time (s⁻¹) | H₀ ≈ 2.2×10⁻¹⁸ s⁻¹ | Cosmic expansion rate. A cosmological INPUT, not derived internally (same status as L_H, which is c/H₀). Appears throughout the g_dyn chain (Section 4) always as H², always self-consistently 1/time². |

---

## 6. Derived Quantities and Diagnostic Ratios

| Symbol | LaTeX | Name | SI Units | Definition | What it is |
|--------|-------|------|----------|-----------|-----------|
| **n** | `n` | Winding number | dimensionless (integer) | = m_cond/m_particle [DERIVED, Part 33] | How many times a particle's phase winds around as you orbit it. Electron: n ≈ 2.4×10²². Planck-mass particle: n=1. Sets which vortex type a particle is. Dark matter: n=1 (Part 116). |
| **n_PDTP** | `n_\text{PDTP}` | PDTP refractive index | dimensionless | = 1/α = 1/cos(Δ) [DERIVED, Part 98] | How much the condensate slows phase waves near a mass. Analogous to optical refractive index. Diverges at the horizon (n→∞ = total internal reflection). |
| **κ_GL** | `\kappa_\text{GL}` | Ginzburg-Landau parameter | dimensionless | = √2 [DERIVED, Part 36] | Ratio of penetration depth to healing length. κ_GL = √2 means Type II behaviour — the condensate naturally forms Abrikosov flux tubes (like a Type II superconductor), giving quark confinement. |
| **c_s** | `c_s` | Speed of sound in condensate | m/s | = c (exact) [DERIVED, Part 34] | Speed of disturbances in the spacetime condensate. Exactly the speed of light — not a coincidence; it follows from the self-consistency condition. |
| **ρ_cond** | `\rho_\text{cond}` | Condensate density | kg/m³ | ~ m_cond/a₀³ | Mass per unit volume of the spacetime medium. |
| **α_G** | `\alpha_G` | Gravitational fine-structure | dimensionless | = (m/m_P)² | Gravitational equivalent of α_EM. Extremely tiny because m << m_P — that ratio IS the hierarchy problem. |
| **α_gr** | `\alpha_\text{gr}` | Dvali-Gomez gravitational coupling | dimensionless | = G·m²/(ℏc) [Part 115/124] | NOT the same as α_G above (different normalization) — this is the "how close to being its own black hole" ratio. α_gr=1 identically under the PDTP bridge (Part 115); a stability-boundary attractor from above under external-G dynamics (Part 124). |
| **α_EM** | `\alpha_\text{EM}` | EM fine-structure constant | dimensionless | ≈ 1/137 | Strength of electromagnetism. The benchmark for comparing coupling strengths. |
| **T_H** | `T_H` | Hawking temperature | K | = ℏc³/(8πGMk_B) [VERIFIED, Part 111] | Temperature of radiation emitted by a black hole. Reproduced from PDTP without modification by the refractive index n_PDTP. |
| **κ** | `\kappa` | Surface gravity | m/s² | = c²/(2r_S) | Gradient of the metric at the horizon. Determines T_H. In PDTP: κ = (c²/2)|d(1/n²)/dr| at r_S [PDTP Original, Part 111]. |
| **N_eff** | `N_\text{eff}` | Effective induced-gravity DOF count | dimensionless | Target = 6π ≈ 18.85 [Part 83]; range [8,34] depending on field content | How many quantum fields' worth of vacuum energy would exactly reproduce G via the Sakharov mechanism. PARTIAL — bounded, not pinned. Part 140 (T70) ruled out a proposed spin-weighted refinement (PDTP has no true vectors/fermions to plug in). |
| **N_v, N_f, N_s** | `N_v, N_f, N_s` | Vector / fermion / scalar DOF counts | dimensionless (integer) | Used in the (unverified, Part 140) formula N_eff = N_v + (11/2)N_f + (1/6)N_s | Standard QFT species counts. PDTP's own field content has N_v=0, N_f=0 always (Part 140) — it is a nonlinear sigma model, not a gauge theory with true vectors/spinors. |
| **ε** | `\epsilon` | Slow-roll parameter | dimensionless | = K/V (kinetic/potential energy ratio); ε₀ ≈ 0.095 from DESI [Part 25/99/119] | How fast φ₋ is rolling relative to its potential. ε<1/9 means the field is "frozen" by Hubble friction (Part 119 freeze condition). Feeds g_dyn (Section 4). |
| **C1, C2, C3** | `C_1, C_2, C_3` | Condensate "layers" | — (naming label, not a physical unit) | Part 89+ | Informal names for PDTP's three interpenetrating condensates: C1 = QCD/hadronic, C2 = EM, C3 = gravitational (context-dependent boundary — check the citing Part). Boundaries between them (e.g. "B1" = the C1/C2 boundary) are where mode-mismatch trapping (dark matter Mechanism 2, Part 89/96) occurs. |

---

## 7. Cosmological Terms

| Symbol / Name | LaTeX | SI Units | What it is |
|--------------|-------|----------|-----------|
| **Λ** (Lambda) | `\Lambda` | 1/length² (m⁻²) | Cosmological constant / dark energy strength. In PDTP = g_Λ·φ₋_vac²/c² (Part 87 reframe, corrected units per Section 4). The universe's "leftover tilt" — why space is not quite empty. Second free parameter alongside m_cond. The worst fine-tuning problem in physics (10¹²¹ times smaller than naive estimate). |
| **w** | `w` | dimensionless | Dark energy equation of state. w = pressure/density. w=−1 = pure cosmological constant (today). w≠−1 means dark energy is evolving. DESI 2024 data hints at w≠−1. |
| **w₀, w_a** | `w_0, w_a` | dimensionless | CPL parameterization. w(z) ≈ w₀ + w_a·z/(1+z). Two numbers describing how w evolves with redshift. DESI measures these. PDTP predicts w_a from the loss tangent (Part 102). |
| **Ω_m** | `\Omega_m` | dimensionless | Matter density fraction ≈ 0.315. What fraction of the universe's energy is in matter (vs dark energy). |
| **Ω_Λ** | `\Omega_\Lambda` | dimensionless | Dark energy density fraction ≈ 0.685. Appears directly in g_Λ = 3·Ω_Λ·ω_gap² (Section 4) and in the causal-sync coefficient C=3Ω_Λ (Part 123). |
| **z** | `z` | dimensionless | Cosmological redshift. z=0 is today; z increases into the past. |
| **β(z)** | `\beta(z)` | dimensionless | Locking history function. How the partial-lock angle β evolved with redshift z. UNKNOWN — the open question in T46. If derived, it would simultaneously predict EDE + today's Λ + DESI w(z). |
| **EDE** | — | — | Early Dark Energy. A brief period of dark-energy-like behaviour before recombination, proposed to resolve the Hubble tension. PDTP derives an EDE term (λ₄) from the existing Lagrangian (Part 117) — no new field required. |
| **r** (tensor-to-scalar) | `r` | dimensionless | Amplitude of primordial gravitational waves in the CMB B-mode polarisation. The kill test for Part 116's DM candidate (m_DM = m_P). No r signal = DM candidate dead. Target experiment: LiteBIRD / CMB-S4. |

---

## 8. Mathematical Operators

| Symbol | LaTeX | Name | What it is |
|--------|-------|------|-----------|
| **□** | `\Box` | d'Alembertian | Wave operator: ∂²/∂t² − c²∇². Every PDTP field equation has the form □φ = source. |
| **∇²** | `\nabla^2` | Laplacian | Spatial second derivative (divergence of gradient). Appears in Poisson's equation. |
| **∇⁴** | `\nabla^4` | Biharmonic | Two Laplacians applied in series. Appears in the biharmonic gravity equation ∇⁴Φ + 4g²Φ = source — a testable 4th-order deviation from standard Poisson (∇²Φ = source). |
| **T_μν** | `T_{\mu\nu}` | Stress-energy tensor | Encodes energy, momentum, and pressure at each spacetime point. The source term in Einstein's equations. |
| **Re[Tr(Ψ†U)]/N** | — | Wilson loop coupling | The SU(3) generalisation of cos(ψ−φ). Reduces exactly to cos(ψ−φ) in the U(1) limit (N=1). Connects PDTP to Wilson's lattice gauge theory (1974). |

---

## 9. Named Physics Mechanisms

| Name | What it means in PDTP |
|------|----------------------|
| **Phase-locking** | Two oscillators pulling into sync. In PDTP: matter-wave (ψ) locks to spacetime-wave (φ). Gravity IS this locking. Stronger lock = stronger gravity. Quantified by α = cos(Δ). |
| **Leidenfrost decoupling** | The transition at Δ→π/2 (α→0) where matter loses gravitational coupling. Named by analogy with a water droplet hovering on a vapour cushion — partial decoupling, not contact. Critical exponents: β=1, ν=1/2, γ=1 (non-equilibrium laser-threshold class, Part 110). |
| **Reversed Higgs** | φ₋ is massless in vacuum (Goldstone boson), gains mass near matter: m²(φ₋) = 2g·sin(Δ₊) [DERIVED, Part 62]. The opposite of the standard Higgs (massive everywhere, massless at the phase transition). **Units note (T68, Section 4):** the code's original numerical evaluation of this formula used the wrong power of ω_gap for g — corrected result is ~4.5×10¹⁴ GeV at Earth's surface, not the originally-stated ~105 eV (see `g_units_audit_scoping.md` Sec 7b). |
| **Biharmonic gravity** | ∇⁴Φ + 4g²Φ = source. The PDTP gravity field equation — 4th order instead of Poisson's 2nd order. Reduces to Poisson at long range (low k), deviates at short range (high k). A testable prediction [DERIVED, Part 61]. |
| **Kibble-Zurek (KZ) mechanism** | Process by which topological defects (vortices) form when a phase transition sweeps through a system at finite speed. Used in Part 116 to show n=1 vortices form at 96% probability — selecting m_DM = m_P. |
| **Planck vortex relic** | The Part 116 dark matter candidate. A winding n=1 vortex in the condensate with mass m_cond = m_P. Formed at the cosmological phase transition. KZ abundance is 50 OoM too low — needs post-inflation production channel. |
| **Sudoku consistency check** | The project's internal validation method: substitute a new result into 10+ known equations and score ratios. Within 1% = PASS. A wrong input cascades like a wrong digit in Sudoku, revealing WHERE the assumption breaks. Not a failure — contradictions are the finding. Reference: `simulations/sudoku_consistency_check.py`. |
| **BEC (Bose-Einstein Condensate)** | What the spacetime medium IS in PDTP — a macroscopic quantum condensate of m_cond-mass particles, analogous to a superfluid at cosmological scale. All condensate physics (healing length, speed of sound, vortices, flux tubes) applies. |
| **Abrikosov flux tubes** | Magnetic flux tubes in a Type II superconductor. PDTP condensate has κ_GL = √2 (exactly Type II), so it naturally forms these — which become quark confinement flux tubes in the SU(3) extension. |
| **No-go theorem (Part 115)** | Algebraic proof that m_cond cannot be derived from inside PDTP. Every internally constructible observable scales as a pure power of m_cond — changing m_cond just rescales everything uniformly. The answer MUST come from outside (measurement or external theory). |
| **Dvali-Gomez criticality** | The condition α_gr = 1: each condensate quantum is marginally its own black hole (Schwarzschild radius ≈ Compton wavelength). This is WHY all Part 77/78 bounds on m_cond kept saturating — they all encode the same condition. Consolation prize from Part 115. |
| **JPD testbed** | Josephson Phase-Drive experiment concept. A Nb superconducting ring + Josephson junction array tuned near ω_gap harmonics. Designed to give a ~6 ppm signal if PDTP is correct — provides an indirect window on ω_gap without needing Planck-frequency hardware. |

---

## 10. Abbreviations and Acronyms

| Abbreviation | Full name | Context |
|-------------|-----------|---------|
| PDTP | Phase-Decoupled Transport Physics | This project. |
| U(1) | Unitary group of dimension 1 | Single phase angle φ ∈ ℝ. The original PDTP Lagrangian. |
| SU(3) | Special Unitary group of dimension 3 | 3×3 matrix extension. Produces 8 gluons and Z₃ vortices (quarks). Part 37+. |
| BEC | Bose-Einstein Condensate | The spacetime medium in PDTP. |
| EDE | Early Dark Energy | Transient dark energy before recombination. Derived from λ₄ in Part 117. |
| EOS | Equation of State | Relation w = p/ρ between pressure and density. Determines dark energy behaviour. |
| GL | Ginzburg-Landau | Framework for describing superconductors / condensates. κ_GL = √2 in PDTP. |
| GR | General Relativity | Standard gravity theory. PDTP must reproduce all GR predictions and then deviate testably. |
| KZ | Kibble-Zurek | Mechanism for vortex/defect formation at phase transitions. Used in Part 116. |
| PPN | Parameterized Post-Newtonian | Framework for testing gravity theories. PDTP must give γ=1, β=1 (Part 112). |
| SymPy | Symbolic Python | Library used for algebraic verification. Every PDTP Original result requires SymPy confirmation or written reason why not. |
| FCC | Forced Checklist Check | Escalation protocol: go through every item in Methodology.md when 3+ standard approaches have failed. |
| CPL | Chevallier-Polarski-Linder | Parameterization w(z) = w₀ + w_a·z/(1+z) for dark energy. What DESI measures. |
| CMB | Cosmic Microwave Background | Earliest light in the universe. B-mode polarisation carries tensor-mode (r) signal — kill test for DM candidate. |
| DESI | Dark Energy Spectroscopic Instrument | Current survey finding hints at w≠−1 (evolving dark energy). PDTP has a natural candidate explanation (Part 117, T46). |
| LISA | Laser Interferometer Space Antenna | Planned space-based GW detector. ω_gap is 43 orders above its sensitivity band. |
| LLR | Lunar Laser Ranging | Tests PPN β parameter. PDTP must give β=1. |

---

*Last updated: 2026-09-06. Update this file whenever a new symbol or mechanism
is introduced — including its SI units.*

**Changelog:**
- 2026-09-06: Moved from `docs/technical/term_glossary.md` to `docs/term_glossary.md`.
  Added an explicit SI Units column throughout (folding in what would otherwise
  have been a separate SI_Units.md). Corrected the g/g_cond/ω_gap entries per
  TODO_05 T68's units audit ([g]=1/length², not [rad/s] as previously stated;
  ω_gap is a genuine but DIFFERENT-dimensioned frequency). Added g_Λ, g_dyn,
  N_eff, N_v/N_f/N_s, α_gr, ε, H/H₀, Ω_Λ, z, m_cond_QCD, E_P, C1/C2/C3 (all
  previously missing, spanning Parts 83-140 that had accumulated since this
  file's last update on 2026-07-01). Verified `docs/technical/glossary.md`
  (the plain-English companion) separately — still accurate, no units or
  equations in it to go stale.
- 2026-07-01: Initial version.

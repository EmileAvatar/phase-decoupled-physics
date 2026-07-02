# PDTP Term and Symbol Glossary

**Purpose:** Complete reference of every symbol, variable, and named concept used
in PDTP research docs, scripts, and TODO files. Written so a new reader — or a
returning collaborator — can identify any term without hunting through old Parts.

**Companion files:**
- `docs/technical/glossary.md` — plain-English conceptual glossary (start here if new)
- `docs/research/equation_reference.md` — all equations with status tags
- `CLAUDE.md` — project rules and standards

**Maintenance rule:** Update this file whenever a new symbol or named concept is
introduced to the framework. One row per symbol is enough.

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

| Symbol | LaTeX | Name | Value / Definition | What it is |
|--------|-------|------|--------------------|-----------|
| **m_cond** | `m_\text{cond}` | Condensate quantum mass | = m_P (set by observed G) | Mass of one "grain" of spacetime. PDTP's one free parameter. Everything gravitational follows from this single number. Cannot be derived internally (Part 115 no-go theorem — proven). |
| **m_P** | `m_P` | Planck mass | ≈ 2.176×10⁻⁸ kg ≈ 22 μg | The natural scale where quantum mechanics and gravity meet. Absurdly heavy for a particle — that absurdity IS the hierarchy problem. |
| **m_DM** | `m_\text{DM}` | Dark matter particle mass | = m_P = m_cond [DERIVED, Part 116] | Mass of the dark matter candidate. No longer a free parameter — vortex stability forces winding n=1, so m_DM = m_cond. Two independent derivations (energy argument + Kibble-Zurek Monte Carlo). |
| **m_e** | `m_e` | Electron mass | ≈ 9.109×10⁻³¹ kg | Standard electron mass. Used in winding number and hierarchy ratio calculations. |
| **m_p** | `m_p` | Proton mass | ≈ 1.673×10⁻²⁷ kg | Standard proton mass. Note: lower-case m_p = proton; upper-case m_P = Planck mass. |
| **M** | `M` | Body mass | Context dependent | Large mass in gravity calculations (Earth, Sun, black hole). Not to be confused with m_cond. |
| **M₀** | `M_0` | Koide mass scale | ≈ 313.84 MeV ≈ m_p/3 | Base mass in the Koide lepton formula. Close to m_p/3 (0.3% match) and to m_cond_QCD = 367 MeV (Part 37). Origin of this coincidence is open. |

---

## 4. Coupling Constants

| Symbol | LaTeX | Name | Value / Definition | What it is |
|--------|-------|------|--------------------|-----------|
| **g** or **gᵢ** | `g_i` | Phase-locking coupling | [rad/s] | Strength of the cos(ψ−φ) coupling for particle i. Controls how strongly matter pulls on spacetime. |
| **g_cond** | `g_\text{cond}` | Condensate coupling | = m_P·c²/ℏ ≈ 1.86×10⁴³ rad/s | The coupling constant at Planck scale. Numerically equals ω_gap. Sets the breathing mode frequency. |
| **G** or **G_N** | `G` | Newton's gravitational constant | ≈ 6.674×10⁻¹¹ m³/(kg·s²) | Standard measured gravity. DERIVED in PDTP as G = ℏc/m_cond² [Part 33], but remains a free parameter because m_cond is free. |
| **G_eff** | `G_\text{eff}` | Effective Newton's constant | = 2·G_bare [DERIVED, Part 61] | In the two-phase system, effective gravity is twice the bare coupling. The factor of 2 is derived from Newton's 3rd law (ψ̈ = −2φ̈₊). |
| **K** | `K` | Lattice stiffness | = ℏ/(4πc) | Stiffness of the condensate medium. Sets how rigid spacetime is. Dimensionless in natural units: K₀ = 1/(4π) ≈ 0.0796. |
| **g_GP** | `g_\text{GP}` | Gross-Pitaevskii interaction | = ℏ³/(m_cond²·c) [DERIVED, Part 34] | Interaction constant in the BEC description of the condensate. Equivalent to the scattering length in a real superfluid. |
| **λ₄** | `\lambda_4` | Quartic coupling (EDE term) | = 2g²sin²(β)/(3k̄²) [DERIVED, Part 117] | The Early Dark Energy term. Positive, generated by the existing Lagrangian at partial lock. Self-switches off as β→0 (full lock today), giving w=−1 automatically. No new physics required. |
| **σ** | `\sigma` | String tension | ≈ 0.173 GeV² (PDTP SC) | Energy per unit length of a quark flux tube. QCD measured: 0.18 GeV². PDTP strong-coupling formula is 4% off (Parts 37–41). |
| **k̄** | `\bar{k}` | Reference wavenumber | Context dependent | Wavenumber scale in the EDE quartic (Part 117). Sets the momentum scale at which λ₄ is evaluated. |

---

## 5. Length and Frequency Scales

| Symbol | LaTeX | Name | Value | What it is |
|--------|-------|------|-------|-----------|
| **a₀** | `a_0` | Condensate lattice spacing | = ℏ/(m_cond·c) = l_P | Distance between adjacent "grains" of spacetime. Equals the Compton wavelength of m_cond = Planck length. |
| **ξ** | `\xi` | Healing length | = a₀/√2 ≈ 0.707·a₀ [DERIVED, Part 34] | How far a disturbance in the condensate spreads before healing back. The condensate's coherence length (BEC physics). |
| **l_P** | `l_P` | Planck length | ≈ 1.616×10⁻³⁵ m | Smallest meaningful length scale. In PDTP = a₀ (they are the same thing). |
| **t_P** | `t_P` | Planck time | ≈ 5.39×10⁻⁴⁴ s | Planck length / c. The condensate oscillation period at m_cond. |
| **ω_gap** | `\omega_\text{gap}` | Breathing mode gap | = m_cond·c²/ℏ ≈ 1.86×10⁴³ rad/s [DERIVED, Part 33] | Minimum frequency the spacetime condensate can oscillate at. Like the lowest "note" of spacetime. 43 orders above LISA — undetectable directly. The same as g_cond numerically. |
| **L_H** | `L_H` | Hubble radius | ≈ 1.3×10²⁶ m | Size of the observable universe. A cosmological INPUT to PDTP — not derived internally. |
| **Φ** | `\Phi` | Newtonian gravitational potential | = GM/(rc²) | Dimensionless gravity depth. Earth surface: ≈ 7×10⁻¹⁰. Neutron star: ≈ 0.2. Black hole horizon: = 0.5. Used in the Schwarzschild mapping sin(Δ₊) = √(2Φ). |

---

## 6. Derived Quantities and Diagnostic Ratios

| Symbol | LaTeX | Name | Definition | What it is |
|--------|-------|------|-----------|-----------|
| **n** | `n` | Winding number | = m_cond/m_particle [DERIVED, Part 33] | How many times a particle's phase winds around as you orbit it. Electron: n ≈ 2.4×10²². Planck-mass particle: n=1. Sets which vortex type a particle is. Dark matter: n=1 (Part 116). |
| **n_PDTP** | `n_\text{PDTP}` | PDTP refractive index | = 1/α = 1/cos(Δ) [DERIVED, Part 98] | How much the condensate slows phase waves near a mass. Analogous to optical refractive index. Diverges at the horizon (n→∞ = total internal reflection). |
| **κ_GL** | `\kappa_\text{GL}` | Ginzburg-Landau parameter | = √2 [DERIVED, Part 36] | Ratio of penetration depth to healing length. κ_GL = √2 means Type II behaviour — the condensate naturally forms Abrikosov flux tubes (like a Type II superconductor), giving quark confinement. |
| **c_s** | `c_s` | Speed of sound in condensate | = c (exact) [DERIVED, Part 34] | Speed of disturbances in the spacetime condensate. Exactly the speed of light — not a coincidence; it follows from the self-consistency condition. |
| **ρ_cond** | `\rho_\text{cond}` | Condensate density | ~ m_cond/a₀³ | Mass per unit volume of the spacetime medium. |
| **α_G** | `\alpha_G` | Gravitational fine-structure | = (m/m_P)² | Gravitational equivalent of α_EM. Extremely tiny because m << m_P — that ratio IS the hierarchy problem. |
| **α_EM** | `\alpha_\text{EM}` | EM fine-structure constant | ≈ 1/137 | Strength of electromagnetism. The benchmark for comparing coupling strengths. |
| **T_H** | `T_H` | Hawking temperature | = ℏc³/(8πGMk_B) [VERIFIED, Part 111] | Temperature of radiation emitted by a black hole. Reproduced from PDTP without modification by the refractive index n_PDTP. |
| **κ** | `\kappa` | Surface gravity | = c²/(2r_S) | Gradient of the metric at the horizon. Determines T_H. In PDTP: κ = (c²/2)|d(1/n²)/dr| at r_S [PDTP Original, Part 111]. |

---

## 7. Cosmological Terms

| Symbol / Name | LaTeX | What it is |
|--------------|-------|-----------|
| **Λ** (Lambda) | `\Lambda` | Cosmological constant / dark energy strength. In PDTP = g·φ₋_vac² (Part 87 reframe). The universe's "leftover tilt" — why space is not quite empty. Second free parameter alongside m_cond. The worst fine-tuning problem in physics (10¹²¹ times smaller than naive estimate). |
| **w** | `w` | Dark energy equation of state. w = pressure/density. w=−1 = pure cosmological constant (today). w≠−1 means dark energy is evolving. DESI 2024 data hints at w≠−1. |
| **w₀, w_a** | `w_0, w_a` | CPL parameterization. w(z) ≈ w₀ + w_a·z/(1+z). Two numbers describing how w evolves with redshift. DESI measures these. PDTP predicts w_a from the loss tangent (Part 102). |
| **Ω_m** | `\Omega_m` | Matter density fraction ≈ 0.315. What fraction of the universe's energy is in matter (vs dark energy). |
| **β(z)** | `\beta(z)` | Locking history function. How the partial-lock angle β evolved with redshift z. UNKNOWN — the open question in T46. If derived, it would simultaneously predict EDE + today's Λ + DESI w(z). |
| **EDE** | — | Early Dark Energy. A brief period of dark-energy-like behaviour before recombination, proposed to resolve the Hubble tension. PDTP derives an EDE term (λ₄) from the existing Lagrangian (Part 117) — no new field required. |
| **r** (tensor-to-scalar) | `r` | Amplitude of primordial gravitational waves in the CMB B-mode polarisation. The kill test for Part 116's DM candidate (m_DM = m_P). No r signal = DM candidate dead. Target experiment: LiteBIRD / CMB-S4. |

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
| **Reversed Higgs** | φ₋ is massless in vacuum (Goldstone boson), gains mass near matter: m²(φ₋) = 2g·sin(Δ₊) [DERIVED, Part 62]. The opposite of the standard Higgs (massive everywhere, massless at the phase transition). |
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

*Last updated: 2026-07-01. Update this file whenever a new symbol or mechanism is introduced.*

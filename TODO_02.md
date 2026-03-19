# TODO_02 — Active Roadmap

Summary of completed work: [TODO_Summary.md](TODO_Summary.md)
Full archive: [TODO_01.md](TODO_01.md)

---

## Current Status

Parts 1–41 complete. The QCD lattice progression has reached:
- Strong-coupling sigma = 0.1729 GeV² (4% off QCD) — analytically closed
- Physical beta (β=6.0) confirmed working with small-step Metropolis
- N=4 CPU demo done; N≥16 GPU required for reliable Cornell fit

**Central open problem:** m_cond is underdetermined. G = ħc/m_cond² is exact but
m_cond = m_P cannot be derived perturbatively (Parts 29–35 exhausted this path).
This is analogous to Λ in GR.

---

## Part 42 — GPU Lattice at Physical Beta (NEXT TASK)

**Goal:** Run SU(3) lattice at β=6.0, N=16 on GPU (RTX 3060 + CuPy) to get a
box size of 1.5 fm and reliable Cornell fit giving σ_phys ≈ 0.18 GeV².

**Why N≥16 is required:**
- At β=6.0, lattice spacing a = 0.093 fm (Necco-Sommer 2001)
- Confinement onset at R > 0.5 fm = ~5 lattice spacings
- N=4 box = 0.37 fm < onset → only Coulomb regime accessible
- N=16 box = 1.5 fm → R up to 8 spacings → linear regime accessible

**Steps:**
- [ ] Install CuPy for CUDA 12.x on RTX 3060 (`pip install cupy-cuda12x`)
- [ ] Add GPU support to `simulations/solver/su3_physical_beta.py`
  - Replace `np` with `cp` (CuPy) for link matrices
  - Keep CPU fallback when CuPy not available
- [ ] Run: `python su3_physical_beta.py --N 16 --beta 6.0 --meas 500 --gpu`
- [ ] Verify Cornell fit: V(R) = σR + A/R + c with R = 1..8
- [ ] Target: σ_lat ~ 0.04 → σ_phys ~ 0.18 GeV² (standard quenched QCD)
- [ ] Optional: beta scan β = 5.7, 5.9, 6.0, 6.2 to confirm scaling window

**Expected Sudoku scorecard:** 7/7 (S26 should now pass with N=16)

**Files to update:**
- `simulations/solver/su3_physical_beta.py` — add GPU mode
- `docs/research/su3_physical_beta.md` — update with GPU results
- `simulations/solver/main.py` — no change needed (Phase 16 already wired)

---

## Open Problems (from TODO_01.md — still unresolved)

### Structural

- [x] **SU(3) gauge structure from phase lattice** *(from Part 27b — RESOLVED 2026-03-08)*
  - 8 gluons as normal modes: YES — SU(3) small fluctuations give 8 massless spin-1 modes ✓
  - Asymptotic freedom: NEGATIVE — β(K)=+K²/(8π²)>0 (IR free); QCD AF is a gauge-level property ✓
  - SU(2) from Z₂: PARTIAL — generator count matches, chirality/mass incomplete
  - Key insight: K (condensate stiffness) ≠ g (QCD coupling) — distinct levels
  - Docs: `docs/research/su3_gauge_structure.md`; Script: Phase 17 `su3_gauge_structure.py`

- [x] **Scalar sector backreaction on tensor sector** *(RESOLVED 2026-03-08)*
  - T_μν^φ = 0 in vacuum: U(1) shift symmetry makes condensate vacuum-insensitive ✓
  - Excited condensate (breathing mode) gives w = −1 (potential) to +1 (kinetic) → dark energy ✓
  - Bridges Part 25 w(z) result: phase drift IS a geometric backreaction on the Einstein eq ✓
  - Does NOT fully solve Λ problem: matter-sector vacuum energy still contributes T_μν^vac^matter
  - 11/11 Sudoku tests pass
  - Docs: `docs/research/scalar_tensor_backreaction.md`; Script: Phase 18 `scalar_backreaction.py`

- [x] **Derive hierarchy ratio R = α_G/α_EM from lattice topology** *(Strategy B — RESOLVED 2026-03-08)*
  - **PDTP Original:** R = 1/(n² × α_EM) where n = m_cond/m (vortex winding number, Part 33) ✓
  - Hierarchy problem = winding number problem: why is n_p = m_P/m_p ~ 10¹⁹?
  - Path A (QCD chain): m_cond = Λ_QCD ≈ 200 MeV correctly inferred from σ_QCD; G off by 10⁴⁰ (hierarchy gap)
  - Path B (Dirac large numbers): Eddington off 10²¹, Hubble off 10¹¹ — no clean coincidence
  - Path C (Dvali species): N_required = n² ~ 10³⁸ >> N_SM ~ 118 — circular (needs G) and off by 10³⁶
  - Two free parameters block derivation: m_cond (undetermined) AND α_EM (not derived in PDTP)
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/hierarchy_ratio.md`; Script: Phase 19 `hierarchy_ratio.py`
  - Open path: Sakharov route — N_eff from lattice symmetry + a from breathing mode measurement

### Black Holes

- [x] **Black hole singularity as topological defect** *(RESOLVED 2026-03-08)*
  - **PDTP Original:** r=0 replaced by vortex core of radius ξ = l_P/√2 ✓
  - Condensate order parameter f(r) → 0 smoothly; no divergence, no singularity ✓
  - Penrose theorem (1970): condition 4 (smooth manifold) broken by PDTP lattice at a₀ ~ l_P ✓
  - Exterior GR unchanged: ξ/r_s = m_P/(2√2 M) << 1 for M >> m_P ✓
  - Core energy ~ m_P c² (one Planck quantum, finite) ✓
  - Evaporation endpoint: M_evap = m_P/(8π) — where T_H = T_P and core fills horizon ✓
  - Analogy: Abrikosov vortex in Type II SC (Part 36); core has finite radius, not a point ✓
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/bh_topological_defect.md`; Script: Phase 20 `bh_topological_defect.py`
  - Open: what happens to winding number at evaporation endpoint? → information paradox

- [x] **Hawking radiation information paradox in PDTP condensate** *(RESOLVED 2026-03-08)*
  - PDTP Original: W = Σnᵢ (winding numbers) is the information carrier; W ~ S_BH/k_B (same order) ✓
  - Topological protection (Mermin 1979) rules out information loss (Resolution C) ✓
  - Resolution A supported: information exits via phase correlations of Hawking radiation ✓
  - BEC analogue: Steinhauer (2016) confirms entanglement between Hawking pairs at scale ξ ✓
  - Open: endpoint M ~ m_P/(8π) is non-perturbative — information paradox restated at Planck scale
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/hawking_info_paradox.md`; Script: Phase 21 `hawking_info_paradox.py`

- [x] **Black hole evaporation endpoint** *(RESOLVED 2026-03-08)*
  - PDTP prediction: complete evaporation — no remnant ✓
  - r_s(M_evap) = l_P/(4π); t_evap = (10/π²)T_P ≈ 1 Planck time (PDTP Original) ✓
  - S_BH/k_B = 1/(16π) < 1 bit — no classical BH structure possible ✓
  - E_final/M_evap c² = 8π — semiclassical completely breaks down at endpoint ✓
  - Phase soliton (A) ruled out: W=0 at endpoint + no flat potential direction ✓
  - Type II SC analogy: ξ/r_s = 8.89 >> 1 — past B_c2 dissolution point ✓
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/bh_evaporation_endpoint.md`; Script: Phase 22 `bh_evaporation_endpoint.py`

### Standard Model Gaps (from OP#1 — SU(2) partial result)

PDTP now explains the *structure* of SU(3)×SU(2)×U(1) (force carriers, confinement,
symmetry groups). The following **values and mechanisms** remain open:

- [x] **Weak coupling strength g_W** *(RESOLVED 2026-03-08 — NEGATIVE RESULT)*
  - g_W = √(4πα_EM/sin²θ_W) — not an independent parameter ✓
  - PDTP Original: g_W is DOUBLY underdetermined — needs α_EM (Part 44) AND sin²θ_W (new) ✓
  - sin²θ_W is a new free parameter: ratio of SU(2)/U(1)_Y condensate stiffnesses ✓
  - Dimensional transmutation inapplicable: SU(2) is broken (not confining) ✓
  - Structure exact: 3 W bosons (N²−1=3), C₂=3/4, b₀=19/6 (AF), Z₂ vortices ✓
  - Analogy: g_W:SU(2) condensate :: G:gravitational condensate (free parameter) ✓
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/weak_coupling_gw.md`; Script: Phase 23 `weak_coupling_gw.py`

- [x] **W and Z boson masses (Higgs mechanism)** — Part 49 RESOLVED
  - Three PDTP condensate layers: gravitational (m_P), QCD (Lambda_QCD), electroweak (v=246.22 GeV)
  - Structural results: m_W = g_W*v/2 = 80.428 GeV, m_Z = m_W/cos(tW) = 91.76 GeV, rho=1 (custodial SU(2))
  - N_Goldstone = 3 (exact); Higgs = amplitude mode of EW condensate (breathing mode analogy)
  - NEGATIVE RESULT: v = 246.22 GeV is 3rd free condensate scale; m_W/m_Z DERIVED not predicted
  - Three condensate layers span 84 decades in energy density: EW~10^46, QCD~10^29, gravity~10^113 J/m^3
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/wz_boson_masses.md`; Script: Phase 24 `wz_boson_masses.py`

- [x] **Chirality — why SU(2) couples only to left-handed particles** — Part 50 RESOLVED (partial)
  - PDTP Original: Z2 vortex winding direction (+1/2/-1/2) = chirality (left/right)
  - PDTP Original: maximal parity violation A=-1 is AUTOMATIC — binary winding is not tunable; no partial violation possible
  - PDTP Original: right-handed neutrino absent = -1/2 winding state decoupled from EW condensate
  - NEGATIVE RESULT: which hand (L vs R) the EW condensate chose = free parameter of vacuum (spontaneous P-breaking)
  - PDTP Lagrangian is P-symmetric; vacuum breaks parity analogous to ferromagnet choosing magnetization direction
  - CKM matrix: (N-1)^2 = 4 parameters for N=3 generations (3 angles + 1 CP phase); all underdetermined
  - 10/10 Sudoku tests pass (Dirac algebra exact; gamma5 eigenvalues exact; Wu asymmetry; CKM count)
  - Docs: `docs/research/chirality_parity_violation.md`; Script: Phase 25 `chirality_parity.py`

- [x] **Three generations of fermions (electron, muon, tau + neutrinos)** — Part 51 RESOLVED (partial)
  - PDTP Original: 3 generations = 3 lowest radial vortex excitation modes (n_r=0,1,2)
  - PDTP Original: lepton universality DERIVED — g_i couples to winding n, not radial mode n_r; all generations identical to W/Z
  - PDTP Original: decay cascade gen3→gen2→gen1 DERIVED — excited vortex relaxes to lower radial mode
  - Koide formula K=2/3 CONSISTENT (0.0009% agreement) — not yet derived from condensate potential
  - NEGATIVE RESULT: mass values require EW condensate potential V(r) near vortex core (new unknown, analogous to m_cond Part 29)
  - NEGATIVE RESULT: why exactly 3 stable modes underdetermined — needs decay width Gamma(n_r) from V(r)
  - Anomaly cancellation: Σ Q_L = 0 per generation (exact structural, inherited from SU(3)×SU(2)×U(1))
  - PMNS mixing: (N-1)^2 = 4 parameters for N=3 (same structure as CKM; values underdetermined)
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/three_generations.md`; Script: Phase 26 `three_generations.py`

- [x] **Coupling constant values (α_EM, α_W, α_S)** *(RESOLVED 2026-03-09 — NEGATIVE RESULT)*
  - **PDTP Original:** Beta functions b₀ DERIVED from group theory (no free parameters) ✓
  - b₀(QCD) = 11 − (2/3)×6 = 7 > 0: asymptotic freedom in SU(3) EXACT ✓
  - b₀(SU(2)) = 19/6 ≈ 3.167 > 0: asymptotically free above EW scale EXACT ✓
  - b₀(QED) = −2 < 0: IR free (coupling grows at high E); Landau pole ~10²⁸⁶ GeV EXACT ✓
  - GUT convergence direction DERIVED; exact scale sensitive to initial values ✓
  - α_EM = 1/137, α_S = 0.118, sin²θ_W = 0.231: all FREE PARAMETERS [NEGATIVE] ✗
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/coupling_constants.md`; Script: Phase 27 `coupling_constants.py`

- [x] **Z₃ phase positions → Koide formula → derive m_cond and G (HIGH PRIORITY)** *(RESOLVED 2026-03-09 — PARTIAL)*
  - **PDTP Original:** SU(3) coupling Re[Tr(Ψ†U)]/3 at Z₃ centers → cos(2πk/3 − ψ₀) = Brannen modulation ✓
  - **PDTP Original:** Y-junction 120° (Part 37) = Z₃ phase spacing (Part 53) = same geometry ✓
  - **PDTP Original:** δ = √2 DERIVED from equal partition (45° angle, |v‖|² = |v⊥|²) ✓
  - **PDTP Original:** Free parameter reduction: 3 lepton masses → 2 free params (M₀, θ₀); δ eliminated ✓
  - M₀ = 313.84 MeV ≈ m_p/3 (0.3%) ≈ m_cond_QCD (Part 37: 367 MeV, factor 1.2) [CONSISTENT] ✓
  - G derivation FAILS: hierarchy factor ~10⁴⁰ (two-condensate hypothesis) [NEGATIVE] ✗
  - θ₀ = 2/9 underdetermined — no SU(3) derivation [NEGATIVE] ✗
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/koide_z3_derivation.md`; Script: Phase 28 `koide_z3.py`

### Cosmological

- [x] **Cosmological Constant via Forced Checklist Check** *(RESOLVED 2026-03-10 — PARTIAL)*
  - **Method: Forced Checklist Check** — went through ALL ~30 Methodology.md items
  - Part 43: condensate T_μν^φ = 0 in vacuum (U(1) shift) — does NOT add to Λ ✓
  - **Three paths converge:** ρ_Λ ~ ρ_Planck × (l_P / L_H)² ~ 10⁻¹²² ρ_Planck
    - Path A: BEC quantum depletion analog (f_dep ~ l_P/L_H → ρ ~ f²)
    - Path B: Topological sector energy differences on compact manifold
    - Path C: Working backwards from ρ_Λ → L_required ~ 3.5 L_H (same order)
  - **CKN bound:** ρ_CKN = c²/(G L_H²) = 7.1×10⁻²⁶ kg/m³ vs ρ_Λ = 5.8×10⁻²⁷ (factor 12) ✓
  - **Geometric mean:** L_eff = √(l_P × L_H) ~ 47 μm; ρ(L_eff) matches CKN ✓
  - **NEGATIVE:** BEC Bogoliubov invalid — n a_s³ ~ 1 (not dilute; strongly interacting) ✗
  - **NEGATIVE:** L_H is NOT a PDTP parameter — cosmological input (free parameter) ✗
  - **NEGATIVE:** Λ is a SECOND free parameter alongside G (= ℏc/m_cond²) ✗
  - Analogy: G is to PDTP as Λ is to GR — both free parameters of the condensate
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/cosmological_constant_fcc.md`; Script: Phase 29 `cosmo_constant.py`
  - Tachyon condensate postulation remains speculative — moved to Speculation section

- [ ] **CP violation and baryogenesis**
  - PDTP Lagrangian is C, P, T invariant separately → no CP violation
  - Sakharov baryogenesis blocked — needs an extension to break CP

### G Determination — Fresh Reframe Ideas

Five fresh approaches to reframing the problem of determining G (or equivalently m_cond).
Each needs a full investigation before becoming a Part.

- [x] **Idea 1: Measure the ratio alpha_G/alpha_EM instead of G alone** *(RESOLVED 2026-03-12 — NEGATIVE)*
  - n = m_P/m_particle ~ 10^22 for electron, ~ 10^19 for proton
  - Integer constraint on n requires ALL mass ratios to be exact rationals
  - m_mu/m_e = 206.768... and m_p/m_e = 1836.15... are NOT simple rationals
  - At n ~ 10^22, "integer vs non-integer" is unmeasurable anyway
  - **CONCLUSION:** Integer winding constraint does NOT narrow m_cond

- [x] **Idea 2: Count modes (oscillators per volume) instead of measuring stiffness** *(RESOLVED 2026-03-12 — NEGATIVE)*
  - Mode counting (n_cond = 1/a_0^3) is mathematically identical to knowing m_cond
  - All observational routes checked: GW spectrum gives G*M not G; CMB depends on H(z) which contains G
  - Graviton scattering cross-section ~ G^2, not mode count
  - **CONCLUSION:** Counting modes IS measuring m_cond — same circularity in different language

- [x] **Idea 3: Time dilation as phase offset — measure condensate phase directly** *(RESOLVED 2026-03-12 — NEGATIVE)*
  - Clocks measure gravitational redshift = GM/(rc^2) — gives GM combined, not G alone
  - Equivalence principle: ALL frequencies shift by the same fraction GM/(rc^2)
  - omega_gap is invisible because it shifts identically to every other frequency
  - Could show up in GW dispersion at Planck frequency (~10^43 Hz) — completely inaccessible
  - **CONCLUSION:** Equivalence principle makes omega_gap invisible to clock comparisons

- [x] **Idea 4: Structural stability — what m_cond values allow self-consistent condensate?** *(RESOLVED 2026-03-12 — NEGATIVE)*
  - Checked 6 stability criteria: c_s=c, kappa_GL=sqrt(2), vortex binding, core stability,
    Z3 fractional winding, Landau criterion — ALL hold for ANY m_cond > 0
  - Energy density positive for any m_cond; confinement (sigma > 0) for any m_cond
  - **CONCLUSION:** Condensate is structurally stable at all scales. m_cond is truly free.

- [x] **Idea 5: alpha_EM ~ K_0 ~ 1/(4pi) near-coincidence — derivable relationship?** *(RESOLVED 2026-03-12 — NEGATIVE)*
  - K_0/alpha_EM = 10.905 — not close to any integer, simple fraction, or group theory factor
  - Tested: Casimir factors (4/3, 3/4, 3), powers of K_0, sqrt combinations — no match
  - Historical note: deriving 1/137 from pure numbers has been tried (Eddington, Wyler) — all failed
  - alpha_EM runs with energy (QED RG flow), so its low-energy value is not a pure number
  - **CONCLUSION:** No derivable relationship between K_0 and alpha_EM

---

## Speculation (not part of PDTP — ideas to investigate)

These are unverified intuitions. No Sudoku check, no Part number, no derivation yet.
They are recorded here so they are not lost. Each needs a full plan and user approval before becoming a Part.

- [x] **Gravity-EM unification: one condensate, different frequency bands (truth table)** (DONE 2026-03-12)
  - Inspired by the EM spectrum: what if all forces are frequency bands of ONE medium?
  - Historical precedent: electricity + magnetism + light were "three things" until Maxwell unified them (1865)
  - **Idea A: Gravity is weak because it is the slow beat frequency (envelope)**
    - Condensate carrier: omega_P ~ 10^43 Hz (Planck frequency)
    - Matter modulates this carrier at omega_matter = m c^2 / hbar
    - What we feel as gravity = the BEAT = |omega_condensate - omega_matter|
    - Modulation depth = m / m_cond = 1/n ~ 10^-19; coupling ~ 1/n^2 ~ 10^-38 = alpha_G
    - Analogy: AM radio — you hear the slow audio envelope, not the MHz carrier
  - **Idea B: Gravity and EM are the same condensate at different scales**
    - PDTP already has three layers (gravitational/QCD/EW) with identical Lagrangian structure
    - What if they're not separate condensates but frequency bands of ONE medium?
    - Like radio vs gamma rays: same EM field, different frequencies
    - Hierarchy of forces = frequency ratio spectrum of one medium
  - **Truth table evaluation:**
    - **(1) A true, B false:** Gravity IS a beat frequency, but gravity and EM are SEPARATE condensates
      - Explains why gravity is weak (carrier >> signal)
      - Does NOT explain why alpha_EM = 1/137 (separate medium, separate coupling)
      - Three condensate layers remain independent — no unification
      - Testable: beat frequency structure should produce sidebands detectable in GW spectrum
    - **(2) A false, B true:** Gravity and EM are the same medium, but gravity is NOT a beat frequency
      - Forces are different excitation modes (spin-0/2 vs spin-1) of one medium
      - Still needs to explain WHY gravity is weak if not from beat/envelope mechanism
      - Spin problem: must explain how one medium produces different spin excitations at different scales
      - Testable: force unification at high energy (GUT-scale convergence already observed in running couplings)
    - **(3) A true AND B true:** One medium, gravity = beat of that medium's self-oscillation
      - Cleanest picture: alpha_force ~ (m_particle / m_condensate_layer)^2 for all forces
      - Hierarchy problem becomes: "why does the spectrum have gaps at these specific scales?"
      - Problem: naive scaling gives alpha_EM ~ (m_e/v_EW)^2 ~ 10^-12, not 10^-2 — coupling mechanism differs between bands
      - Would predict: all forces converge at one frequency (= GUT scale); force strength = how far from carrier
      - Testable: frequency-dependent deviations from 1/r^2 at the crossover between bands
    - **(4) A false AND B false:** Gravity and EM are separate condensates AND gravity is not a beat
      - This is the current PDTP baseline: three independent condensate layers, G = hbar c / m_cond^2
      - Gravity is weak because m_cond = m_P is large (but WHY m_P is large = underdetermined)
      - No unification — forces are genuinely different media with different stiffnesses
      - Still consistent with all current results; just offers no explanation for the hierarchy
  - Key obstacle for (3): spin problem — gravity excitations are spin-0/2, EM is spin-1
    - BUT: PDTP lattice already produces both scalar (breathing) and tensor (shear) modes from ONE lattice (Part 28)
    - Different vibration modes of one medium CAN produce different spins — this is not a showstopper
  - What would make this a Part: derive coupling strength alpha = (m/m_layer)^2 for EM from the PDTP Lagrangian;
    show that the same medium produces spin-0, spin-1, and spin-2 excitations at different scales;
    predict a crossover scale or frequency-dependent deviation testable in experiment
  - **Investigation findings (2026-03-12):**
  - **Ocean wave spin-depth analogy** (from `assets/images/waves long and trans image072.png`)
    - Ocean waves: surface = circular orbits (transverse + longitudinal), bottom = horizontal only (longitudinal)
    - Transverse/longitudinal ratio = tanh(k*z) where z = height above bottom
    - tanh is an L-shaped curve that NEVER reaches 0 — coupling always nonzero
    - Higher spin modes (more transverse character) decay faster with depth
    - Part 28 already confirmed: ONE lattice produces spin-0 (breathing) + spin-2 (shear)
    - Mapping: "surface" = Planck scale (all spins excited), "depth" = lower energy (higher spin decays)
  - **Coupling curve shapes — NOT exponential, L-shaped power law**
    - alpha_G = (m/m_P)^2 is a POWER LAW (L-shape on linear plot), not exponential
    - tanh^2(kz) approx (kz)^2 for small kz — matches power-law behavior near the "bottom"
    - alpha_EM ~ 1/137 nearly flat (logarithmic running: 1/137 at low E, 1/128 at m_Z)
    - alpha_s runs logarithmically (strong at low E, weak at high E — asymptotic freedom)
    - GUT convergence at ~10^16 GeV: all three gauge couplings nearly cross at one point
    - If forces are modes of one medium, GUT crossing = node where all modes have equal amplitude
  - **Spin ordering matches observation (qualitative WIN)**
    - Spin-2 (gravity): weakest at low energy — decays fastest with depth (most transverse)
    - Spin-1 (EM/strong): intermediate coupling — intermediate decay rate
    - Spin-0 (scalar/Higgs): persists to all scales — longitudinal, decays slowest
    - Physical reason: transverse modes decay faster than longitudinal in any bounded medium
    - This ordering is CORRECT and non-trivial — it is a genuine prediction of the depth model
  - **Three quantitative problems found:**
    - **(P1) Decay rate mismatch:** Need k_spin2/k_spin1 ~ 22 to get 43-order hierarchy.
      Naive spin ratio gives k_2/k_1 = 2. Off by factor ~11. No physical justification for 22:1.
    - **(P2) Mass-independence of alpha_EM (KILLER TEST):**
      Gravity couples to MASS: alpha_G(electron) = 1.75e-45, alpha_G(proton) = 6.0e-37
      EM couples to CHARGE: alpha_EM = 1/137 for BOTH electron and proton (mass-independent)
      The beat/depth model inherently produces mass-dependent coupling for ALL modes.
      EM's mass-independence requires a fundamentally different coupling mechanism (charge, not mass).
    - **(P3) SU(3) vs U(1) same spin, different coupling:**
      Strong force (spin-1, alpha_s ~ 1 at low E) and EM (spin-1, alpha_EM ~ 1/137) differ by ~137x.
      Both are spin-1 gauge bosons. Depth model predicts same-spin = same coupling. FAILS.
  - **Possible resolution: topological charge vs continuous phase (needs investigation)**
    - Gravity couples to continuous phase gradient (proportional to mass) -> mass-dependent
    - EM couples to discrete winding number (quantized charge) -> mass-independent
    - In PDTP: vortex winding number W is integer; electron and proton both have |W| = 1 -> same alpha_EM
    - Would explain mass-independence while keeping depth mechanism for gravity
    - For SU(3): Z3 fractional winding (W = 1/3 per quark) -> different effective coupling from U(1)
    - This is speculative but testable: script should check if alpha_EM ~ (1/N_colors)^2 or similar
  - **LISA connection (from Phase 7 — lisa_sim.py):**
    - omega_gap = m_P*c^2/hbar = 2.95e42 Hz (Planck frequency)
    - In the beat model, this IS the carrier frequency of the gravitational condensate
    - LISA band: 1e-4 to 0.1 Hz — gap of 43 orders = the hierarchy problem in frequency space
    - The 43-order gap is NOT a failure of detection — it IS the hierarchy problem restated
  - **Script plan: `gravity_em_truth_table.py` (standalone investigation, NOT integrated into main.py)**
    - Script computes quantitative checks for all 4 truth table cases, with Sudoku-style PASS/FAIL:
    - **S1: Frequency scale map** — omega for all 3 condensate layers (Planck, QCD, EW) + 6 SM particles
    - **S2: Beat frequency test (Idea A)** — alpha_G = (m/m_P)^2 for e, mu, tau, p, W, Z; compare to G*m^2/(hbar*c)
    - **S3: Naive beat for EM** — alpha_EM_beat = (m/v_EW)^2 for e, mu, p; expect FAIL (should all = 1/137)
    - **S4: Ocean wave depth model** — fit tanh^2(k*z) to alpha_G and alpha_EM at electron scale
      - Compute required k_spin2, k_spin1; report ratio (expect ~22, spin gives only ~2)
    - **S5: Mass-independence test** — compute depth-model alpha_EM for e, mu, p (expect all different = FAIL)
    - **S6: GUT convergence** — do alpha_1, alpha_2, alpha_3 converge near one energy? (reference values)
    - **S7: Topological charge test** — if alpha_EM ~ (W/N)^p, what W, N, p gives 1/137?
    - **S8: Spin ordering check** — rank forces by spin; compare to observed coupling strengths
    - **S9: Power-law vs exponential** — fit alpha_G(m) to (m/m_P)^n and exp(-k*z); which fits?
    - **S10: LISA carrier frequency** — omega_gap as carrier; sideband separation delta_f/f for each particle
    - **S11: Score each truth table case** — tally passes/fails per case; overall verdict

- [x] **Multiple layers of spacetime / condensate** (DONE 2026-03-14 -- investigation, no Part)
  - PDTP already has three confirmed condensate layers: gravitational (m_P), QCD (Lambda_QCD), electroweak (v=246 GeV)
  - Speculation: each SM gauge group (U(1), SU(2), SU(3)) = a separate condensate layer nested inside the one below
  - Deeper layer = higher energy scale = larger condensate stiffness
  - Particles at each layer only "see" the layer below as a fixed background medium — they ride it without knowing it's there
  - Open question: what is the gravitational condensate itself condensed FROM?
    - Either infinite regress (layer below layer below...) or bottoms out at something genuinely discrete
    - PDTP analogue of "what is the ether made of?"
    - Loop quantum gravity answer: spin network (discrete spacetime); string theory answer: branes
  - Observable consequence (if true): each layer transition (EW → QCD → gravity) should leave a signature
    - EW phase transition at v=246 GeV: already observed (Higgs)
    - QCD confinement transition at Lambda_QCD: already observed (hadronisation)
    - Gravitational condensate transition: unknown scale — possibly at Planck energy
  - What would make this a Part: a falsifiable prediction that differs from SM; a mechanism for the nesting;
    or a derivation that the SM gauge groups MUST be separate condensates (not just an analogy)
  - Precedent: Wen (2004) string-net condensation — all SM forces emerge from one underlying quantum liquid
  - **Oil-and-water analogy — density stratification + immiscibility**
    - Real fluids form layers by TWO mechanisms:
      1. **Density stratification** — heavier fluid sinks, lighter floats (ocean thermocline, atmosphere)
      2. **Immiscibility** — fluids that CANNOT mix even if forced (oil/water, liquid metals/slag)
    - PDTP condensate layers may use BOTH:
      - Stratification: layers ordered by energy density (EW~10^46, QCD~10^29, gravity~10^113 J/m^3)
      - Immiscibility: different gauge groups (U(1), SU(2), SU(3)) cannot mix — topologically distinct
    - Real-world parallels to investigate:
      - Ocean halocline: salt density gradient creates stable layering
      - Density tower experiment: honey/syrup/soap/water/oil/alcohol stack in order
      - Magma chambers: molten rock separates by mineral density
      - Planetary atmospheres (Jupiter): gas density layering creates visible bands
    - Key physics questions for PDTP:
      - Is the ordering by ENERGY DENSITY (like gravity stratification) or by TOPOLOGY (like immiscibility)?
      - Can layers partially mix at boundaries (like alcohol/water) or are they strictly immiscible (like oil/water)?
      - Does each layer have a sharp boundary (phase transition) or a gradual crossover?
      - If immiscible: what property makes U(1), SU(2), SU(3) unable to mix? (different homotopy groups?)
      - If stratified: what plays the role of "gravity" that orders the layers? (energy minimisation?)
    - Possible effects of layering:
      - Interfacial tension between layers — energy cost of a boundary = phase transition latent heat
      - Capillary effects at layer boundaries — particles trapped at interfaces (like surfactants)
      - Rayleigh-Taylor instability — if a heavier layer sits above a lighter one, it's unstable
      - Mixing zones — partial mixing at boundaries could produce effective field theories (EFTs)
  - **Investigation plan: `condensate_layers.py` (standalone script)**
    - S1: Layer catalog — three layers with scales, gauge groups, energy densities, condensate masses
    - S2: Density ordering — are layers ordered by energy density? Which is "heaviest"?
    - S3: Scale ratios — are the gaps between layers uniform or patterned? (log spacing? power law?)
    - S4: Immiscibility test — do different gauge groups allow mixing? (homotopy compatibility)
    - S5: Phase transition signatures — EW and QCD transitions observed; predict gravitational transition
    - S6: Inter-layer coupling — does PDTP Lagrangian have cross-layer terms? Should it?
    - S7: Interfacial tension — energy cost of layer boundaries (latent heat of EW/QCD transitions)
    - S8: What's below gravity? — self-termination vs infinite regress vs discrete base
    - S9: Oil-water mapping — which real-world stratification system best matches PDTP?
    - S10: Scorecard — derived vs interpretive vs speculative; falsifiable predictions
  - **Results (2026-03-14): 13/17 PASS**
    - ALL PASS: density ordering, immiscibility (topology), inter-layer coupling, interfacial tension, oil-water mapping
    - PARTIAL: phase transitions (2/3 observed), below gravity (bootstrap yes, why 3 layers unknown)
    - FAIL: scale ratios (gaps NOT geometric — hierarchy problem restated)
    - Best analogy: He-3/He-4 superfluid mixture (Andreev-Bashkin coupling through shared matter)
    - Conclusion: CONSISTENT and CLARIFYING but mostly INTERPRETIVE — no new predictions beyond SM + PDTP
    - Does NOT warrant a Part number. Useful analogy framework for non-specialists.
    - Script: `simulations/solver/condensate_layers.py`

- [x] **Idea C: Two coupling channels in one medium (amplitude vs topology) -- INVESTIGATED (Part 55)**
  - Motivated by truth table investigation (gravity_em_truth_table.py): beat/depth model FAILS for EM
    because EM is mass-independent (S5 killer test: 0/4 pass)
  - **The problem:** gravity couples to MASS (continuous), EM couples to CHARGE (discrete).
    Any model where coupling depends on mass (beat frequency, ocean wave depth) inherently
    gives different alpha_EM for electron vs proton. Observed: same 1/137 for both.
  - **Proposed resolution:** one medium, TWO coupling channels:
    - Channel 1 (gravity): couples to the AMPLITUDE of the phase gradient = how fast the vortex winds
      = mass. Continuous, particle-dependent. alpha_G = (m/m_P)^2. **DERIVED (Part 33).**
    - Channel 2 (EM): couples to the TOPOLOGY of the phase = does it wind or not, which direction.
      Discrete (integer winding number), particle-independent. alpha_EM = f(topology). **INTERPRETIVE (Part 23).**
  - Analogy: a knotted rope. You can measure its tension (continuous = mass/gravity) or count its
    knots (discrete = charge/EM). Both measurements on the SAME rope.
  - Reference image: `assets/images/Left-Macroscopic-structure-of-quantized-vortex-line-in-He-superfluids-The-core-radius.webp`
    — real vortex line in superfluid He, from Finne, Eltsov, Hanninen & Volovik (2006)
    — Source: https://www.researchgate.net/figure/Left-Macroscopic-structure-of-quantized-vortex-line-in-He-superfluids-The-core-radius_fig1_1854091
  - **Part 55 Results (two_channels.py, Phase 17):**
    - Vortex-vortex interaction in BEC gives Coulomb 1/r law (established physics: Fetter 2009)
    - The EM coupling depends on m_cond (condensate), NOT m_particle -- **mass-independent by construction**
    - S5 killer test: **ALL 6 models PASS** (alpha_EM identical for e, mu, tau, proton)
    - Best candidate: alpha = K_0^2 = 1/(4*pi)^2 = 1/157.9 -- **13.2% off from 1/137**
    - Physical meaning: each vortex contributes one factor of K_0 to the coupling
    - Also derived: charge quantization (topology), conservation (invariant), sign (attract/repel)
    - Sudoku: **10/12 PASS** (S6 and S9 fail: exact value of alpha not reproduced)
    - **STATUS: PARTIAL SUCCESS** -- form derived (mass-independent, 1/r, quantized), magnitude not exact
    - The 13.2% gap between 1/158 and 1/137 could be closed by Idea D (RG running)
    - Script: `simulations/solver/two_channels.py`

- [x] **Idea D: Derive 1/137 from RG running of condensate coupling K_0 = 1/(4*pi) -- NEGATIVE RESULT (Part 56)**
  - Motivated by truth table S7: no clean topological number (W/N)^p gives 1/137.
    But alpha_EM RUNS with energy (1/137 at low E, 1/128 at m_Z). This means 1/137 is DYNAMICAL.
  - PDTP already has the bare coupling: K_0 = 1/(4*pi) ~ 0.0796 (Part 35, dimensionless in natural units)
  - Question: does RG running from K_0 at Planck scale give alpha_EM = 1/137 at low energy?
  - **Part 56 Results (rg_alpha_em.py, Phase 18):**
    - Model R1 (PDTP beta for K, alpha=K^2): K shrinks at low E -> 1/158 becomes 1/175 -> **WRONG direction**
    - Model R2 (QED beta, start at K_0^2): alpha shrinks at low E -> 1/158 becomes 1/202 -> **WRONG direction**
    - Model R3 (run 1/137 UP to Planck): alpha(E_P) = 1/98, vs K_0^2 = 1/158 -> **60% gap, NOT close**
    - Backward solve: bare coupling needed for 1/137 at m_e = 1/93.3; this is K_0^1.79 (not clean power)
    - QED running validated: alpha(m_Z) = 1/131.8 predicted vs 1/128.0 measured (3% off, 1-loop only)
    - Sudoku: **8/10 PASS** (S8 K_0^2 = alpha(E_P) FAIL; S10 gap closure FAIL)
    - **STATUS: NEGATIVE RESULT** -- RG running cannot derive 1/137 from K_0
    - alpha_EM remains a free parameter in PDTP (as in the Standard Model)
    - The two-channel STRUCTURE (Part 55) stands; the MAGNITUDE is not fixed by K_0
    - Script: `simulations/solver/rg_alpha_em.py`

- [x] **Idea E: Running couplings as condensate dispersion (ocean wave 2.0) -- NEGATIVE RESULT (Part 57)**
  - Reframe of the ocean wave analogy that KEEPS the qualitative wins (spin ordering)
    while fixing the quantitative failures (43-order gap)
  - Instead of "higher spin decays with depth" -> "different modes disperse differently"
  - **Part 57 Results (dispersion_coupling.py, Phase 19):**
    - Dispersion hypothesis: alpha_eff(E) = alpha_0 * v_g(E)/c = alpha_0 * sqrt(1-(E_gap/E)^2)
    - 4 fatal problems:
      (1) Gravity: hard cutoff at E_P (alpha=0 below), not gradual alpha_G~m^2
      (2) EM/strong: massless carriers have no dispersion -> no running
      (3) Strong force runs WRONG way (asymptotic freedom = grows at low E)
      (4) GUT scale: E_P (10^19) vs observed 10^16 GeV (3 orders off)
    - 4 qualitative wins: ordering correct, curve shape matches gravity, high-E universality, weak force gap IS genuine dispersion
    - Root cause: coupling running is QUANTUM (vacuum polarization, loops), not classical dispersion
    - Sudoku: **3/10 PASS** (only S2, S3, S4 pass)
    - **STATUS: NEGATIVE RESULT** -- retain as qualitative analogy only, not quantitative
    - Confirms: topological two-channel model (Part 55) is the better path
    - Script: `simulations/solver/dispersion_coupling.py`

- [x] **Idea F: Homotopy classification explains different forces from one medium**
  - Motivated by truth table S8 problem P3: EM (spin-1) and strong (spin-1) have SAME spin but
    differ by factor ~16 in coupling. Depth model can't distinguish same-spin modes.
  - **Topology background (current science):**
    - Topology = properties unchanged by stretching/bending, only by cutting/gluing
    - Homotopy = classifying the fundamentally different ways to wrap one shape around another
    - Example: rubber band around a pole — 0 wraps, 1 wrap, 2 wraps are topologically distinct
    - pi_1(X) = ways to wrap a circle around space X. For U(1): pi_1 = Z (integers). For SU(3): pi_1 = Z_3.
    - Source: Mermin (1979), "The topological theory of defects in ordered media" (cited in Part 33)
  - **PDTP already uses this:**
    - pi_1(U(1)) = Z -> integer winding vortices -> leptons (Part 33)
    - pi_1(SU(3)/Z_3) = Z_3 -> fractional 1/3 winding -> quarks (Part 37)
    - Winding number n = m_cond/m -> mass (Part 33, DERIVED)
    - Charge = winding number sign (Part 23, INTERPRETIVE)
  - **Why EM and strong differ despite same spin:**
    - EM = U(1) gauge group -> vortices classified by Z (all integers) -> charge = +/-1
    - Strong = SU(3) gauge group -> vortices classified by Z_3 (only 3 classes: 0, 1/3, 2/3) -> colour
    - Different GROUP STRUCTURE -> different effective coupling, even at same spin
    - The coupling depends on the topology (Z vs Z_3), not just the spin
  - Status: **REAL MATH, SPECULATIVE CONNECTION** — the homotopy classification is established physics;
    the connection to coupling STRENGTH (why alpha_s ~ 1 and alpha_EM ~ 1/137) is NOT derived
  - What would make this a Part: derive coupling strength from group structure (Z vs Z_3);
    show why Casimir factor alone is insufficient (it gives 4/3, not 137)
  - Reference image for vortex lines: `assets/images/Left-Macroscopic-structure-of-quantized-vortex-line-in-He-superfluids-The-core-radius.webp`
    — Finne et al. (2006), shows real quantized vortex in superfluid He with core radius r_c,
    superfluid velocity v_s ~ 1/r, and density rho_s = 0 inside core.
    PDTP mapping: r_c = Compton wavelength, v_s(r_c) = c, rho_s = 0 inside = "the particle"
    — Source: https://www.researchgate.net/figure/Left-Macroscopic-structure-of-quantized-vortex-line-in-He-superfluids-The-core-radius_fig1_1854091
  - **Part 58 Results (homotopy_classification.py, Phase 20):**
    - Four forces from four topological sectors of ONE condensate:
      Gravity (smooth, no vortex), EM (Z vortex, Coulomb 1/r),
      Strong (Z_3 vortex, flux tube sigma*r), Weak (Z_2 vortex, Yukawa)
    - WHY interaction law changes: Z vortex can unwind -> flux leaks -> 1/r;
      Z_3 vortex cannot unwind -> flux trapped in tube -> linear confinement
    - Casimir factor 4/3 is insufficient (gives ratio 1.33, measured ~69 at 1 GeV)
    - Missing factor ~51 is non-perturbative (Z_3 confinement phase transition)
    - Homotopy explains STRUCTURE (which force is confining/Coulomb/Yukawa)
      but NOT exact values (1/137, sigma = 0.18 GeV^2)
    - Sudoku: **10/10 PASS** (all exact math + experimental consistency)
    - **STATUS: PARTIAL SUCCESS** -- correct framework, qualitative not quantitative
    - Cumulative (Parts 55-58): PDTP force STRUCTURE is correct;
      coupling VALUES remain free parameters (same as Standard Model)
    - Script: `simulations/solver/homotopy_classification.py`

- [x] **Idea G: Strider model — particles FLOAT on gravity (+cos lock vs -cos surface tension)**
  - Motivated by oil/water layer analogy and water strider physics
  - **Surface tension equation (real physics):**
    - Water strider: F = 2 * gamma * L * cos(theta)
    - gamma = surface tension (N/m), L = contact length (legs), theta = contact angle
    - cos(theta) controls coupling: cos(0)=1 sinks, cos(90)=0 floats
    - Source: Young-Laplace equation (1805)
  - **PDTP mapping:** cos(theta) <-> cos(psi - phi) — SAME COSINE, SAME PHYSICS
    - theta (contact angle) = psi - phi (phase difference)
    - gamma (surface tension) = K/a_0 (condensate stiffness / lattice spacing)
    - L (contact length) = lambda_C (Compton wavelength)
  - **Sign insight (user idea):** Lagrangian sign was corrected -cos -> +cos.
    Add strider as -cos (opposite sign = competition):
    - L = +g*cos(psi - phi_bulk) - g*cos(psi - phi_surface)
    - +cos = phase-locking (pulls particle INTO condensate)
    - -cos = surface tension (keeps particle FLOATING)
    - Trig identity: g_eff = 2g * sin(Delta), where Delta = bulk-surface phase gap
  - **Key result (Model C):** If Delta = (m/m_P)^2 * pi/2, then:
    - g_eff gives correct alpha_G for ALL particles (ratio = pi/2, constant)
    - Black hole = Delta -> pi/2 (strider breaks through surface = sinks)
    - Hierarchy problem reframed: "why is Delta so tiny?" (10^-45 rad for electron)
    - Physical meaning: bulk and surface are ALMOST identical; tiny mismatch IS gravity
  - **Why reframing matters:** seeing the problem from different angles prevents getting
    stuck inside it. "Why is G so weak?" and "why is Delta so small?" and "why does the
    strider barely dimple the surface?" are the SAME question viewed from 3 directions.
    Each view suggests different attack strategies.
  - **Naive strider (L = lambda_C) gives WRONG mass dependence:** lighter particles have
    longer Compton wavelength = more contact = stronger coupling. But gravity is WEAKER
    for lighter particles. The -cos sign fixes the direction but not the magnitude.
    Model C (two phases) is needed to get quantitative agreement.
  - Status: **INTERPRETIVE** — correct cosine form, beautiful physical picture,
    reorganises hierarchy problem but does not solve it. Model C most promising.
  - What would make this a Part: derive Delta = (m/m_P)^2 from vortex core depth
    or condensate profile; show the two-phase Lagrangian produces new predictions
    distinct from the single-phase version
  - Script: `simulations/solver/strider_test.py` (Models A-E tested, Model C works)
  - **Air-Water-Oil layer analogy (user idea):** particles live in DIFFERENT layers
    based on how deeply they sit in the condensate stack:
    - AIR (top/lightest): Leptons — float freely, not trapped by any surface tension.
      Can move anywhere. Lighter = higher up = more free.
    - WATER (middle/EW): W, Z, Higgs — the interface layer. Forces that connect
      the free layer (air) to the confined layer (oil) live here.
    - OIL (bottom/QCD): Quarks, gluons — stuck in the dense layer. Surface tension
      between oil and water prevents escape = quark confinement.
    - **Lepton freedom:** leptons float on air, no boundary traps them
    - **Quark confinement:** quarks are IN the oil; pulling one out stretches the
      oil-water interface = energy cost grows with distance = linear confinement
    - **Leptons sticking to quarks:** a lepton can "land" on the water surface
      (touch the EW interface) and interact with quarks below via W/Z exchange.
      Like a bird dipping into water to catch a fish, then flying off.
    - **Atoms:** proton (3 quarks in oil) creates a disturbance reaching up through
      water to air; electron (in air) orbits the disturbance = EM attraction
    - This maps onto the condensate layer table:
      Gravitational (honey, deepest) > EW (water, middle) > QCD (oil, upper)
    - Status: **ANALOGY** — qualitatively maps confinement, freedom, and cross-layer
      interactions. Quantitative test needed: does surface tension between QCD and EW
      layers reproduce sigma = 0.18 GeV^2?
  - **Part 59 Results (strider_model.py, Phase 21):**
    - Model A (naive): FAILS -- g_eff negative for all m << m_P
    - Model C (two-phase): WORKS -- g_eff = 2g*sin(Delta), Delta = (m/m_P)^2 * pi/2
      gives alpha_G ~ (m/m_P)^2 with constant ratio pi/2 for ALL particles
    - Two-phase field equations: box(phi_b) = +g*sin, box(phi_s) = -g*sin (paired)
    - NEW prediction: surface breathing mode phi_- = (phi_b - phi_s)/2 (TESTABLE)
    - Black hole = Delta -> pi/2 (strider sinks through surface = max coupling)
    - Air-water-oil layers: confinement/freedom explained qualitatively
    - QCD layer tension: 0.0016 GeV^2 (vs 0.18 measured, factor ~100 off)
    - Sudoku: **9/10 PASS** (S8 fails: QCD tension factor 100 off)
    - **STATUS: INTERPRETIVE** -- correct mass dependence, beautiful picture,
      new predictions, but Delta = (m/m_P)^2 assumed not derived
    - Hierarchy reframe: "why is G weak?" = "why is Delta tiny?" = "why does
      strider barely dimple surface?" (same question, 3 views)
    - Script: `simulations/solver/strider_model.py`

- [x] **Idea H: G is not one thing — it's the net effect of multiple condensate layers**
  - Motivated by: ChatGPT decomposition G = l_P^2 * c^3 / hbar and user insight that G might
    be a composite of MULTIPLE interacting effects that APPEAR as one constant.
  - **G decomposed (Haug 2024):** G = l_P^2 * c^3 / hbar
    - l_P^2 = gravitational condensate lattice spacing squared (layer 1 property)
    - c^3 = propagation speed cubed (shared by all layers)
    - 1/hbar = quantum scale (frequency-energy conversion)
    - Mathematically identical to PDTP's G = hbar*c / m_cond^2 (since l_P = hbar/(m_P*c))
    - Source: Haug (2024), "The Compton Wavelength Is the True Matter Wavelength"
      (assets/pdfs/The_Compton_Wavelength_Is_the_True_Matter_Waveleng.pdf)
  - **User's key insight:** what if G is like the stiffness of a LAYERED material?
    - Springs in series: 1/k_eff = 1/k_1 + 1/k_2 + 1/k_3
    - Light through glass panes: each pane reduces intensity
    - G is weak not because any ONE layer is weak, but because coupling passes through
      MULTIPLE interfaces, each reducing it
    - Each component of G (l_P, c, hbar) may come from a DIFFERENT layer
  - **Haug's key results relevant to PDTP:**
    - ALL gravity formulas reduce to just l_P and lambda_C (Compton wavelength)
    - The ratio l_P/lambda_C = Compton frequency per Planck time = quantum of gravity
    - In PDTP: l_P/lambda_C = a_0/lambda_C = m/m_cond = 1/n (inverse winding number, Part 33)
    - Planck constant hbar CANCELS OUT of Schrodinger, Dirac, Klein-Gordon equations
      when mass is written as m = hbar/(lambda_C * c)
    - What remains is the Compton frequency c/lambda_C — the particle's internal clock
    - PDTP parallel: vortex core size = Compton wavelength (Part 33); vortex phase
      rotation rate = Compton frequency
  - **Strassler's "wavicle" concept (2024) — supports PDTP vortex picture:**
    - Electrons are not particles or waves — they're "wavicles" (standing wave patterns
      with definite frequency AND definite energy)
    - Compton wavelength = critical scale: box smaller than lambda_C → energy explodes;
      box larger → energy barely changes
    - Massive wavicles can be standing waves in FREE SPACE (no container needed)
    - PDTP mapping: vortex = self-sustaining standing wave pattern in the condensate
      = wavicle. Container = condensate itself.
    - Source: Strassler (2024), "Particles, Waves, and Wavicles"
      (assets/pdfs/Particles, Waves, and Wavicles.pdf)
  - **Connection to layers and strider model (Idea G):**
    - If G passes through multiple layers, each layer adds a "surface tension" barrier
    - Total coupling = product of all layer transmissions
    - G_eff = G_grav * T_EW * T_QCD where T = transmission coefficient at each interface
    - This naturally gives a VERY SMALL G_eff even if individual layers are stiff
    - Like light through fog: each droplet scatters a little, net effect = very dim
  - Status: **INTERPRETIVE** — Haug's decomposition is established math; the multi-layer
    interpretation of G is speculative but physically motivated by the oil-water analogy
  - What would make this a Part: derive G_eff from layer transmission coefficients;
    show that 3 layers (grav/EW/QCD) with known properties produce G = 6.674e-11;
    or show that adding/removing a layer changes G (testable at phase transitions)
  - Reference image: `assets/images/Density Tower Experiment images.jpg` (density layering)
  - **Part 60 Results (composite_g.py, Phase 22):**
    - Haug decomposition: G = l_P^2*c^3/hbar = hbar*c/m_P^2 (exact, both verified)
    - Compton frequency = vortex rotation rate; l_P/lambda_C = 1/n (Part 33)
    - Model 1 (springs in series): FAILS -- dominated by QCD (softest spring),
      gives G ~ 10^29 (off by ~10^40). Wrong direction.
    - Model 2 (transmission): FAILS -- T_total ~ 10^-59 makes G even smaller
    - Model 3 (impedance): Z mismatch ~ 10^68 between Planck and EW layers.
      The mismatch IS the hierarchy in disguise.
    - Circularity: m_EW + m_QCD alone give G ~ 10^29 (need m_P = need G)
    - Numerology: m_P = m_EW^2/m_QCD off by 10^14 (no simple combination works)
    - Sudoku: **9/10 PASS** (S4 fails by design: 3-layer model doesn't give G)
    - **STATUS: NEGATIVE RESULT** -- all 3 models REORGANISE hierarchy, don't solve it
    - G confirmed as FREE PARAMETER (same conclusion as Parts 29, 35)
    - Useful structure: impedance reframes hierarchy; phase transition prediction
    - Cumulative (Parts 55-60): force STRUCTURE correct; force VALUES remain free
    - Script: `simulations/solver/composite_g.py`

- [x] **Two-phase Lagrangian: derive what +cos/-cos produces (Maxwell-style scaffolding)**
  - **Part 61 (Phase 30) -- COMPLETED**
  - Full Euler-Lagrange: 3 coupled PDEs derived and SymPy-verified
    - box(phi_b) = +g*sin(psi-phi_b) [attractive, gravity]
    - box(phi_s) = -g*sin(psi-phi_s) [repulsive, surface tension]
    - box(psi) = -g*sin(psi-phi_b) + g*sin(psi-phi_s) [matter]
  - Change of variables: phi_+ = (phi_b+phi_s)/2, phi_- = (phi_b-phi_s)/2
    - Kinetic term diagonalises (no cross term)
    - Coupling: g*cos(psi-phi_b) - g*cos(psi-phi_s) = 2g*sin(psi-phi_+)*sin(phi_-)
    - PRODUCT coupling: gravity mode and surface mode multiplicatively linked
  - **KEY RESULTS:**
    - Newton's 3rd law: psi_ddot = -phi_+_ddot (EXACT, derived from Lagrangian)
    - Jeans instability: coupled system has one growing mode (lambda = +2*sqrt(2)*g)
      -- gravitational collapse IS the unstable eigenmode
    - Biharmonic gravity: nabla^4(Phi) + 4g^2*Phi = 4g^2*psi
      -- reduces to Poisson at short range (L << L_heal ~ l_P)
      -- 4th-derivative corrections at long range
    - phi_- is a NEW scalar field: massless in vacuum, gains mass in gravitational fields
      -- reversed Higgs mechanism (matter gives mass, not vacuum)
      -- on Earth: m_eff ~ 100 eV, lambda ~ 2 nm
    - Complex scalar: Phi = phi_+ + i*phi_- (natural complex field)
    - U(1) shift preserved, Z_2 exchange sends V -> -V (anti-symmetry, not symmetry)
    - Testable: sub-mm gravity experiments constrain phi_- if m_cond < ~1 meV
  - Sudoku: **10/10 PASS**
  - Script: `simulations/solver/two_phase_lagrangian.py`

- [x] **Reversed Higgs: phi_- environment-dependent mass research (Part 62)**
  - **Part 62 (Phase 31) -- COMPLETED**
  - CORRECTION to Part 61: phi_- = 0 is NOT the equilibrium near matter!
    - V(phi_-) = -2g * Phi * sin(phi_-), where Phi = G*M/(r*c^2)
    - V'(0) = -2g*Phi (nonzero!) -> 0 is NOT equilibrium
    - V'(pi/2) = 0 -> TRUE equilibrium at phi_- = pi/2
    - V''(pi/2) = 2g*Phi > 0 -> STABLE minimum
  - In vacuum (Phi=0): V = 0 everywhere -> phi_- is GOLDSTONE-LIKE flat direction
  - Near matter: phi_- rolls to pi/2, gains mass m^2 = 2g*Phi
  - Compared to 3 known environment-dependent scalar fields:
    - Chameleon (Khoury & Weltman 2004): couples to DENSITY rho
    - Symmetron (Hinterbichler & Khoury 2010): VEV depends on density
    - PDTP phi_-: couples to GRAVITATIONAL POTENTIAL Phi (nonlocal!)
  - **KEY DIFFERENCE:** chameleon = heavy in dense matter; phi_- = heavy near potential wells
  - **Hollow shell experiment:** DISTINGUISHES phi_- from chameleon
    - Inside shell: rho=0 but Phi=const > 0
    - Chameleon: massless (no density) -> long-range force -> DETECTABLE
    - phi_-: massive (nonzero Phi) -> short-range force -> SUPPRESSED
  - G_eff = 2*G_bare at equilibrium (measured G includes phi_- contribution)
    - Roll time ~ 10^-18 s on Earth -> instantaneous, always at equilibrium
  - Mass on Earth: ~106 eV; NS surface: ~1.8 MeV; vacuum: 0 (flat)
  - 4 new testable predictions (Predictions 7-10 for falsifiable_predictions.md)
  - Sudoku: **10/10 PASS**
  - Script: `simulations/solver/reversed_higgs.py`

- [x] **Two-phase Lagrangian: re-derive ALL previous results (Parts 1-60) — CRITICAL** (Part 63, DONE)
  - **Result: 16/16 PASS.** All single-phase results reproduced.
  - phi_-, biharmonic gravity, Jeans instability promoted from [SPECULATIVE] to [DERIVED]
  - **CORRECTION:** Newton's 3rd law is psi_ddot = -2*phi_+_ddot (not -1*phi_+_ddot)
    Factor of 2 consistent with G_eff = 2*G_bare (Part 62)
  - Key mechanism: chi = phi_+ + pi/2 maps two-phase to single-phase exactly
  - Script: `simulations/solver/two_phase_rederivation.py` (Phase 32)
  - Research: `docs/research/two_phase_rederivation.md`
  - **Checklist (all DERIVED and VERIFIED):**
    - [x] Newton's 1st law: g=0 gives zero force (S1 PASS)
    - [x] Newton's 2nd law: F = -g*cos(psi-phi_+) at equilibrium (S2 PASS)
    - [x] Newton's 3rd law: psi_ddot = -2*phi_+_ddot (S3 PASS, CORRECTED from Part 61)
    - [x] Newtonian 1/r potential recovery (S4 PASS)
    - [x] PPN parameters gamma=1, beta=1 (S9 PASS)
    - [x] Hawking temperature T_H = hbar*c^3/(8*pi*G*M*k_B) (S10 PASS)
    - [x] GW tensor modes at c (S12 PASS)
    - [x] Breathing mode dispersion: omega^2 = c^2*k^2 + 2*g*Phi (S7 PASS)
    - [x] Double pulsar orbital decay — U(1) shift preserved (S11 PASS)
    - [x] Vortex winding number n = m_cond/m (S6 PASS)
    - [x] G = hbar*c/m_cond^2 (S5 PASS)
    - [x] c_s = c (S8 PASS)
    - [x] SU(3) Wilson action limit (S13 PASS)
    - [x] String tension sigma = 0.173 GeV^2 (S14 PASS)
    - [x] Koide Q = 2/3 (S15 PASS)
    - [x] Dark energy w(z) from phase drift (S16 PASS)

- [x] **Temperature in PDTP — what is temperature in the phase-locking picture?** (Part 64, 2026-03-15)
  - Standard physics: T = average kinetic energy per DOF; k_B T = (2/3) <E_kin>
  - QFT: temperature = periodicity of imaginary time (KMS condition)
  - PDTP mapping: temperature = degree of phase incoherence among oscillators
    - Hot = random phases (disordered); Cold = locked phases (synchronized)
    - Absolute zero = perfect phase-locking (all oscillators in sync)
    - Phase transition = Kuramoto synchronization transition (Part 1)
  - Key questions:
    1. Derive PDTP partition function Z = Sum exp(-H_PDTP / k_B T)
    2. Show Kuramoto critical coupling K_c = thermal phase transition at T_c
    3. Derive T_c for gravitational condensate (what temperature destroys spacetime?)
    4. Does k_B emerge or remain free? (probably free — like G and Lambda)
    5. Temperature-dependent gravity: does thermal matter couple differently? (Prediction 3)
    6. Reversed Higgs + temperature: does phi_- mass depend on T as well as Phi?
    7. SM compatibility: does thermal PDTP reproduce Bose-Einstein/Fermi-Dirac statistics?
  - Already touched: Hawking T (Part 24), BEC vs thermal (Prediction 3), two-fluid model (Part 19)
  - Missing: dedicated treatment of temperature as a PDTP concept
  - What would make this a Part: derive Z, T_c, and show standard thermodynamics emerges

- [x] **Chirality from condensate refractive index — path to making handedness DERIVED not free** (Part 65, 2026-03-15)
  - Current Part 50 result: which hand the EW vacuum chose = free parameter (vacuum choice)
  - Speculation: the EW condensate is chirally birefringent — two different effective refractive indices
    for +1/2 and -1/2 winding vortices, forced by the condensate's own winding background
  - Mechanism: +1/2 vortex in +1/2-wound condensate → slides freely (n_eff = 1)
  - Mechanism: -1/2 vortex in +1/2-wound condensate → must "unwind" medium as it moves → energy cost ~ path length
  - In infinite-volume limit: energy cost infinite → -1/2 vortex CANNOT propagate = topologically confined
  - Observational signature: right-handed fermions not absent but CONFINED (locally exist near vortex core, cannot travel)
  - This is identical to "not there" observationally — but the mechanism is propagation suppression, not non-existence
  - Key prediction: parity restoration above EW scale
    - Below v=246 GeV: condensate wound → n_eff splits → left propagates freely, right confined
    - Above v=246 GeV: condensate melts → n_eff -> 1 for both → parity restored
    - This IS observed: parity violation is an IR (low energy) phenomenon; EW theory is parity-symmetric above the phase transition
  - Cascade hypothesis (links to multiple-layers speculation above):
    - Deepest condensate layer winds in one direction (quantum fluctuation or topological charge of universe)
    - Each layer transition (gravity -> QCD -> EW) acts as a polarizing filter, seeding the next layer's winding
    - Chirality of the universe = amplified memory of the first symmetry-breaking event
    - Analogy: each layer is a birefringent crystal in series; each passes only one polarization to the next
  - Connection to Part 28b: spacetime birefringence already predicted for GWs; this extends it to fermion propagation
  - What would make this a Part: derive n_eff(+1/2) and n_eff(-1/2) from the SU(2) PDTP Lagrangian;
    show the confinement condition; predict the energy scale at which parity is restored; compare to v=246 GeV

- [x] **Phase-gradient coil drum — proposed analog experiment** (2026-03-15)
  - Core idea: instead of driving matter at 10^23 Hz (proton Compton frequency), create a SPATIAL phase gradient
    that travels through a stack of coils, each offset in phase — a slow-wave traveling phase structure
  - Engineering concept: N coils in a drum/toroid, each carrying the signal at phase offset 360/N degrees
    - Coil 1: phase 0deg, Coil 2: phase 120deg, Coil 3: phase 240deg (three-phase minimum; more = smoother)
    - Creates a phase wave traveling axially at v_phase = omega * coil_spacing (controllable, not c)
    - This is exactly how a linear induction motor and traveling wave tube amplifier work — proven technology
  - PDTP connection: driving EM phase pattern -> couples (weakly) to gravitational condensate phase phi
    - If EM-to-gravitational coupling exists (Tajmar 2006 hint: anomalous gravitomagnetic field from spinning SC)
    - Then coil array is a lever: EM phase drive -> gravitational condensate phase shift -> alpha = cos(psi-phi) -> 0
    - The collective condensate mode frequency (omega_gap) is the target, NOT individual particle Compton frequency
    - Analogy: BCS gap (100 GHz) vs electron Compton frequency (10^20 Hz) — 9 orders lower because COLLECTIVE
  - Saucer geometry: toroidal field is contained (no exhaust, no external reaction force visible)
    - Three amplifiers at 120deg spacing = three-phase — matches Lazar's claimed craft geometry
    - Force appears as internal pressure with no external propulsion signature
  - Visual references:
    - Phase sequence (3-phase rotating field): ![phase sequence](assets/images/phase sequesnce 02182.png)
    - Coil array schematic (toroidal phase-gradient ring): ![coil schematic](assets/images/phase_gradient_coil_schematic.png)
    - Analog simulation concepts (EM levitation, eddy current inertia reduction): ![analog sim](assets/images/pdtp_analog_simulation.png)
  - Testable TODAY (no exotic materials):
    1. Build toroidal coil drum (copper wire, fiberglass former, STM32 controller — ~£200)
    2. Place YBCO superconducting ring inside (liquid nitrogen, 77K — ~£100)
    3. Sweep phase rotation frequency through coil array
    4. Measure assembly weight on precision scale (mg resolution)
    - Prediction: if Tajmar coupling is real, frequency-dependent weight anomaly appears
    - PDTP would predict the resonance frequency once m_cond is known
  - What would make this a Part: derive the EM-to-gravitational phase coupling constant from PDTP Lagrangian;
    predict the resonance frequency; design a discriminating test vs classical EM effects

- [x] **Acoustic standing wave levitation — inverted as decoupling mechanism** (2026-03-16)
  - Standard acoustic levitation: transducer generates standing wave; object sits PASSIVELY at pressure node
    - Object trapped where pressure gradient = gravity (node = zero net acoustic force)
    - No propulsion, no contact — pure wave interaction with matter
  - Visual references:
    - How acoustic levitation works (transducer/reflector/node diagram): ![acoustic levitation](assets/images/acoustic standing waves levitation H19fQ==.jpg)
    - Actual levitation experiment (multiple objects at nodes, pressure heatmap): ![acoustic nodes](assets/images/acoustic standing waves levitation 472926_1_En_2_Fig1_HTML.png)
  - The KEY INVERSION (PDTP speculation):
    - Standard: external wave source -> object trapped at node (object is PASSIVE)
    - PDTP Goal 2: object GENERATES the phase wave in the spacetime condensate itself
    - If matter can drive an oscillation in the phi field (gravitational condensate),
      it creates its own standing wave pattern — and sits at its own node IN the gravitational field
    - Result: matter decoupled from gravity at that node point; alpha = cos(psi-phi) -> 0 locally
    - This is the physics of "the craft generates its own gravity bubble" — not shielding, self-generated node
  - Analogy chain:
    - Acoustic: transducer -> pressure standing wave -> object at node (passive levitation)
    - PDTP: coil/reactor -> phi standing wave in condensate -> craft at node (active decoupling)
    - The "reactor" in Lazar's description = the transducer in the acoustic analogy
    - The "gravity amplifiers" = the phased array that shapes the standing wave geometry
  - Why saucer shape: toroidal standing wave has a natural flat equatorial node plane
    - A disk-shaped craft centered on this plane = maximum decoupling area for minimum energy
    - Matches observed UAP geometry: flat disc, no exhaust, silent
  - Open physics questions for PDTP to answer:
    1. What is the coupling constant between matter oscillation and phi field? (needed to size the "transducer")
    2. What frequency of phi oscillation creates a standing wave at craft scale? (sets the reactor frequency)
    3. Is the node stable? (acoustic nodes are stable equilibria — is the gravitational node?)
    4. Energy budget: how much power to sustain the node against condensate restoring force?
       (Part 29 estimate: ~10 kW/ton if decoupling is complete; acoustic analogy suggests much less for partial)
  - What would make this a Part: formulate the phi field wave equation in the presence of an oscillating matter source;
    find the standing wave solutions; calculate node stability and energy cost

- [x] **Quantum geometry formalism for PDTP condensate — quantum metric + Berry curvature (Part 66)** ✅ DONE
  - Source paper: Liu et al. (2025), "Quantum geometry in condensed matter", Natl Sci Rev 12, nwae334
    https://academic.oup.com/nsr/article/12/3/nwae334/7762198
  - The quantum geometric tensor Q^ab = g^ab - (i/2)*Omega^ab describes the geometry of wave functions
    in momentum space. g^ab = quantum metric (distances), Omega^ab = Berry curvature (rotations).
  - This is the RIGOROUS version of what PDTP does heuristically with alpha = cos(psi - phi).
  - **5 connections to PDTP identified:**
  - **Connection 1 (HIGH): Quantum metric = phase geometry**
    - PDTP coupling alpha = cos(psi-phi) is a U(1) phase relationship
    - The quantum geometric tensor describes exactly this — geometry of U(1) phases
    - Upgrade path: replace heuristic cos(psi-phi) with quantum geometric tensor Q^ab of condensate
    - This would make PDTP's coupling a proper geometric quantity, not just a trig function
  - **Connection 2 (HIGH): Quantum metric gives mass in flat bands**
    - Paper Eq. 31: (1/m_eff)^ab = (U*V)/(N*hbar^2) * integral[g^ab dk]
    - Cooper pairs get effective mass from quantum metric even in perfectly flat bands
    - PDTP Part 33: mass from winding number n = m_cond/m (topological origin)
    - BOTH say: mass arises from phase geometry, not classical kinetic energy
    - Paper PROVES this experimentally: twisted bilayer graphene Tc = 2.2 K vs 0.05 K conventional
    - The 44x enhancement IS the quantum metric contribution — measured, not theoretical
  - **Connection 3 (HIGH): Superfluid weight from geometry**
    - D = D_conv + D_geom (conventional + geometric superfluid weight)
    - D_conv vanishes for flat bands; D_geom survives (from quantum metric)
    - PDTP condensate IS a superfluid (Part 34: c_s = c, xi = a_0/sqrt(2))
    - The PDTP condensate's superfluid weight has a geometric contribution from its quantum metric
    - Could this break the one-parameter degeneracy (m_cond undetermined, Part 34-35)?
    - If D_geom constrains the condensate, it might fix m_cond independently of G
  - **Connection 4 (MEDIUM): Uniform Berry curvature = stability**
    - Fractional Chern insulators: stable ONLY when Berry curvature is uniform in Brillouin zone
    - Non-uniform -> charge density waves (instability)
    - PDTP analogue: uniform condensate phase = stable gravity; non-uniform = instabilities
    - Possible link to Jeans instability (Part 61): eigenvalue +2*sqrt(2)*g > 0 could be the
      Berry curvature non-uniformity threshold
  - **Connection 5 (MEDIUM): Nonlinear Hall effect from phase dipoles**
    - Berry curvature DIPOLE produces J ~ E^2 (nonlinear transport)
    - PDTP: phase gradient dipole in condensate -> nonlinear gravitational effects?
    - Potential falsifiable prediction: nonlinear gravitational "Hall effect" from condensate geometry
    - Distinct from GR (which is linear in weak field limit) — could be testable
  - **Detailed implementation plan (Part 66):**
    - Phase A: Mathematical foundation
      1. Define the quantum geometric tensor for the PDTP condensate field phi
         - Start from the U(1) Lagrangian: L = 1/2(d_mu phi)(d^mu phi) + g*cos(psi - phi)
         - The Bloch states |phi_k> of the condensate have a QGT: Q^ab = g^ab - (i/2)*Omega^ab
         - Derive g^ab and Omega^ab for the PDTP cosine coupling
      2. Show alpha = cos(psi-phi) emerges as a SPECIAL CASE of the quantum metric
         - The overlap <psi|phi> = cos(psi-phi) is the inner product of two states
         - The quantum metric g^ab measures how this overlap CHANGES with parameters
         - alpha is the zeroth-order term; g^ab gives the first-order corrections
      3. Derive the effective mass formula for PDTP vortices using paper's Eq. 31
         - Substitute PDTP quantum metric into (1/m_eff) = integral[g^ab dk]
         - Compare to Part 33 result: m = m_cond/n
         - Check: do they agree? If yes, quantum metric formalism validates Part 33
    - Phase B: Superfluid weight and m_cond
      4. Compute D_geom for the PDTP condensate
         - Use paper's Eq. 34 with PDTP band structure
         - The geometric superfluid weight determines condensate rigidity
      5. Check if D_geom constrains m_cond
         - Part 34 showed condensate is self-consistent for ANY m_cond
         - The quantum metric adds a NEW constraint: D_geom must be positive and finite
         - If this fixes m_cond -> the hierarchy problem is solved (or at least constrained)
      6. Compute Berry curvature distribution for PDTP condensate
         - Check uniformity condition (Connection 4)
         - Non-uniformity -> instabilities -> relate to Jeans criterion
    - Phase C: Predictions and falsifiability
      7. Derive nonlinear gravitational transport from Berry curvature dipole
         - By analogy with nonlinear Hall effect: J_grav ~ (grad phi)^2 * Berry_dipole
         - This is a NEW prediction not in standard GR
      8. Compute numerical values for testable predictions
         - Nonlinear gravity magnitude (relative to Newtonian)
         - Energy scale where geometric effects dominate (flat-band regime)
         - Compare to existing gravitational measurements (torsion balance, LISA)
      9. Sudoku consistency check: all new equations against 10+ known results
      10. Update falsifiable_predictions.md with any new testable predictions
    - Phase D: Cross-references and documentation
      11. Update vortex_winding_derivation.md (Part 33) with quantum metric validation
      12. Update condensate_selfconsist.md (Part 34) with geometric superfluid weight
      13. Update chirality_refractive_index.md (Part 65) — birefringence IS quantum metric anisotropy
      14. Full research doc: quantum_geometry_pdtp.md with complete derivations
  - **Key question this Part answers:** Can the quantum geometric tensor formalism
    promote PDTP from a heuristic phase-coupling model to a rigorous geometric field theory?
    If yes, it connects PDTP to the active experimental program in condensed matter
    (twisted graphene, Moire materials, kagome magnets) — those labs are ALREADY measuring
    the quantum metric effects that PDTP claims operate in the gravitational condensate.
  - **Risk assessment:**
    - HIGH probability: Connections 1-3 will work (the math is straightforward U(1) geometry)
    - MEDIUM probability: Connection 5 yields a new falsifiable prediction
    - LOW probability: D_geom actually fixes m_cond (would be a breakthrough, but don't count on it)
  - What would make this a Part: derive Q^ab for PDTP condensate; recover alpha = cos(psi-phi) as
    special case; compute m_eff from quantum metric and compare to Part 33; compute D_geom and
    check if it constrains m_cond; derive at least one new falsifiable prediction from Berry curvature dipole
  - Script: `simulations/solver/quantum_geometry.py` (Phase 35); Doc: `docs/research/quantum_geometry_pdtp.md`
  - **Results (10/10 Sudoku pass):**
    - **KEY RESULT 1:** PDTP kinetic term (1/4)(d_mu(psi-phi))^2 IS (1/4)*Tr(g^ab_PDTP) — SymPy verified, residual = 0
    - **KEY RESULT 2:** Berry curvature = 0 for 1D U(1) (real parameter space) — SymPy verified
    - **KEY RESULT 3:** g^ab = omega_PDTP^2/omega_gap^2 = 1/2 (dimensionless, m_cond-independent) — SymPy verified
    - **KEY RESULT 4:** Vortex quantum metric: g_tt = n^2/r^2 (topological), g_rr = (f'/f)^2 (amplitude, from GP nonlinear core)
    - **KEY RESULT 5:** D_geom scales as m_cond^3 exactly (power-law fit exponent = 3.0000) — does NOT fix m_cond
    - GP vortex profile solved by shooting method (scipy solve_ivp); amplitude contribution 10-30x larger than simple estimate
    - Eq. 66.35 corrected: mixed-unit formula replaced with consistent frequency-unit derivation
    - **NEGATIVE:** D_geom smooth and monotonic — no special point, does NOT break one-parameter degeneracy (Part 34-35)
    - Connections 1-3 confirmed (HIGH); Connection 4-5 remain open for future work (nonlinear Hall prediction)s

- [x] **Part 67: White et al. (2026) — Emergent Quantization from Dynamic Vacuum** (HIGH PRIORITY) DONE
  - **Source:** White, Vera, Sylvester & Dudzinski, Phys. Rev. Research 8, 013264 (2026).
    DOI: 10.1103/l8y7-r3rm. "Emergent quantization from a dynamic vacuum."
  - **What they do:** Model the vacuum as a dynamic acoustic medium (compressible continuum
    with spatially varying density rho(r) and bulk modulus B(r)). Add quadratic temporal
    dispersion omega = D*k^2 with D = hbar/(2*m_eff), derived from Madelung hydrodynamics.
    With constitutive profile 1/c_s^2(r) = A(omega) + C(omega)/r, the Helmholtz equation
    becomes EXACTLY the hydrogenic Coulomb equation. Recovers full hydrogen spectrum, all
    eigenfunctions, angular momentum quantization — zero free parameters after one calibration.
  - **Why this matters for PDTP:** This is the CLOSEST published peer-reviewed work to the
    PDTP condensate vacuum model. Both frameworks:
    - Treat the vacuum as a physical medium (acoustic/condensate)
    - Derive quantum behaviour as emergent from classical-like wave equations
    - Use Madelung/BEC hydrodynamics as the bridge
    - Produce biharmonic (nabla^4) wave equations from quantum pressure
    - Have bound states from stop bands / phase-locking
  - **Key parallels:**
    - White: 1/c_s^2(r) = A + C/r (Coulombic sound speed profile)
    - PDTP: cos(psi - phi) coupling creates effective potential from mass source ~ 1/r
    - White: omega = D*k^2 (Schrodinger-type, non-relativistic)
    - PDTP: omega^2 = c^2*k^2 + omega_gap^2 (Klein-Gordon, relativistic)
    - White: nabla^4 from quantum pressure (Eq. A17: d^2 rho/dt^2 = c_L^2 nabla^2 rho - (hbar^2/4mu^2) nabla^4 rho)
    - PDTP: nabla^4 from two-phase Lagrangian (Part 61: nabla^4 Phi + 4g^2 Phi = source)
    - White: bound states from A(omega) < 0 (reactive stop band)
    - PDTP: bound states from phase-locking (alpha = cos(psi-phi) > 0)
    - White: m_eff = mu (reduced mass, calibrated)
    - PDTP: m_cond = m_P (free parameter)
  - **Key difference:** White et al. is non-relativistic (omega = D*k^2); PDTP is relativistic
    (omega^2 = c^2*k^2 + gap^2). White does hydrogen only; PDTP attempts gravity + full SM.
    White assumes constitutive profile; PDTP derives from Lagrangian.
  - **Three questions for PDTP to answer:**
    1. Can PDTP derive the White constitutive profile 1/c_s^2 = A + C/r from cos(psi-phi)?
       A vortex (particle) modifies local condensate -> local c_s changes -> other particles
       see Coulombic effective potential. This would DERIVE what White ASSUMES.
    2. Does PDTP's relativistic dispersion reduce to omega = D*k^2 in the non-relativistic limit?
       If yes, PDTP contains White et al. as a special case. Check: expand omega^2 = c^2*k^2 + gap^2
       for k << gap/c and see if it gives omega ~ const + D*k^2.
    3. Is the nabla^4 term the same physics? White's comes from Madelung quantum pressure;
       PDTP's comes from the two-phase Lagrangian (phi_b, phi_s). If they match, the two-phase
       extension has a physical interpretation: quantum pressure of the condensate.
  - **Implementation plan:**
    - Phase A: Mathematical comparison (research, no code)
      1. Write out both dispersion relations side by side; take non-relativistic limit of PDTP
      2. Compare biharmonic terms: White Eq. A17 vs PDTP Part 61 biharmonic
      3. Attempt to derive 1/c_s^2 = A + C/r from PDTP's cos coupling near a vortex source
      4. Check: does the PDTP acoustic metric (Part 12, c_s = c) produce Coulombic sound speed?
    - Phase B: SymPy verification
      5. Verify non-relativistic limit gives omega = D*k^2 with D = hbar/(2*m_cond)
      6. Derive effective Coulomb potential from linearised PDTP near a point source
      7. Check isospectrality: does the PDTP Helmholtz equation give hydrogen-like spectrum?
    - Phase C: Implications
      8. If PDTP contains White et al.: hydrogen spectrum is a DERIVED PREDICTION (not assumed)
      9. If not: identify where the frameworks diverge and what PDTP would need to match
      10. Update falsifiable_predictions.md: hydrogen spectrum as PDTP prediction (if derived)
    - Phase D: Documentation
      11. Full research doc: white_emergent_quantization.md
      12. Sudoku consistency check on all new equations
      13. Update this TODO with results
  - **Risk assessment:**
    - HIGH probability: non-relativistic limit will give omega ~ D*k^2 (standard physics)
    - MEDIUM probability: PDTP can derive the constitutive profile (requires solving linearised
      field equations near a vortex source — doable but non-trivial)
    - HIGH payoff: if PDTP derives the White constitutive profile, it EXPLAINS what White assumes
      and the hydrogen spectrum becomes a PDTP prediction with no free parameters (beyond m_cond)
  - **What would make this a Part:** derive non-relativistic limit; show PDTP contains White et al.;
    derive constitutive profile from Lagrangian; reproduce hydrogen spectrum as emergent prediction
  - Script: `simulations/solver/white_comparison.py` (Phase 36); Doc: `docs/research/white_emergent_quantization.md`
  - **Results (12/12 Sudoku pass):**
    - **Q1 ANSWER (Constitutive profile): PARTIAL YES**
      - Metric perturbation (gravity) gives 1/c_eff^2 = A + C/r (matches White) [DERIVED]
      - Condensate density (GP vortex) gives 1/c_s^2 = A + B/r^2 (different from White) [DERIVED]
      - The 1/r profile requires the gravitational potential -> same circularity as Parts 29-35
      - C_grav = -2GM/c^4 = -2.76e-71 m (for proton); ~10^50 smaller than White's EM profile
    - **Q2 ANSWER (NR limit): YES** [DERIVED, SymPy VERIFIED]
      - omega ~ omega_gap + [hbar/(2*m_cond)]*k^2 + O(k^4)
      - D_PDTP = hbar/(2*m_cond) = D_White when m_cond = m_eff (exact same form)
      - **PDTP contains White et al. as non-relativistic special case**
      - k^4 correction: -hbar^3*k^4/(8*m_cond^3*c^2) [SymPy verified]
    - **Q3 ANSWER (nabla^4): STRUCTURALLY YES, PHYSICALLY NO** [PDTP Original]
      - Both nabla^4 arise from two-field -> one-field elimination (same mathematical pattern)
      - White: (rho, S) -> eliminate S -> dispersive nabla^4 in wave equation (dynamic)
      - PDTP: (phi_+, phi_-) -> eliminate phi_- -> biharmonic field equation (static)
      - Deep connection identified: structural equivalence of the reduction [PDTP Original]
    - **Two-phase cross-check: ALL PRESERVED**
      - Breathing mode NR limit works (D = c^2/(2*sqrt(2*g*Phi))) [SymPy VERIFIED]
      - Newton's 3rd law (psi_tt = -2*phi_+_tt) unchanged [SymPy VERIFIED]
      - Jeans eigenvalue (+2*sqrt(2)*g) unchanged [SymPy VERIFIED]
    - **What PDTP adds beyond White:**
      1. Lagrangian foundation (derives what White assumes)
      2. Relativistic (White is NR limit of PDTP)
      3. Gravity included (White has hydrogen only)
      4. Two-phase structure (breathing mode + biharmonic gravity)
      5. Less circular (classical Lagrangian, not Madelung-from-QM)
    - **NEGATIVE:** Hydrogen spectrum not directly derivable from PDTP gravitational profile
      (gravitational C_grav ~ 10^-71 m vs EM scale ~ 10^-11 m; need SU(2)xU(1) extension for EM)

- [x] **Part 68: Cosmological Constant — Two-Phase Deep Investigation (Forced Checklist Check)** (DONE 2026-03-19)
  - **KEY RESULT: Omega_beat = 2/3 EXACTLY (vs observed Omega_Lambda = 0.685, 2.6% off)**
  - rho_beat = c^2/(4*pi*G*L_H^2) = (2/3)*rho_crit [DERIVED, step-by-step]
  - The 2/3 factor comes from two-phase beat STRUCTURE (not tuning)
  - Uses G and H_0 as inputs — consistency check, not G-free prediction
  - phi_- is NOT shift-protected (unlike phi_+ in single-phase)
  - phi_- is Goldstone-like: massless in vacuum, massive near matter
  - phi_- naive ZPE ~ rho_Planck (CC problem NOT solved by two-phase alone)
  - Sudoku: 15/15 pass; Script: cosmo_constant_v2.py (Phase 37)
  - Docs: docs/research/cosmo_constant_two_phase.md
  - **Status upgrade from Part 54:** Lambda no longer "completely free" — constrained to 2/3 of rho_crit
  - **Method: Forced Checklist Check** — every Methodology.md item applied to Lambda with two-phase Lagrangian
  - **Why revisit:** Part 54 FCC concluded "Lambda is a second free parameter." Since then we built
    powerful new tools: two-phase Lagrangian (Parts 61-63), frequency reframe, reversed Higgs (Part 62),
    White comparison (Part 67), quantum geometry (Part 66), chirality refractive (Part 65), scalar
    backreaction (Part 43). These were NOT available during Part 54.
  - **Significance:** Solving (or significantly constraining) the cosmological constant problem would be
    a landmark result. The 10^122 discrepancy is the worst prediction in physics.
  - **Central questions:**
    1. Can the two-phase Lagrangian DERIVE Lambda from its own structure? (without L_H as input)
    2. Is phi_- the dark energy field? (massless in vacuum = can have cosmological-frequency modes)
    3. Does the beat frequency interpretation survive a proper derivation? (delta/omega_P ~ 10^-61)
    4. Does phi_- break the U(1) shift symmetry that makes T_mu_nu^phi = 0? (Part 43 used single-phase)
    5. Can impedance mismatch / interface physics naturally produce 10^-122?
  - **What holds from frequency reframe (keep and strengthen):**
    - Cosine coupling = nonlinear mixer -> valid (heterodyne/beat physics)
    - Gap frequency omega_gap -> physically grounded (BEC, superconductors, waveguides)
    - Two-phase structure (phi_+, phi_-) -> strongest result; produces two natural scales [DERIVED]
    - Interface interpretation (bulk/surface) -> consistent with known multi-phase systems
  - **Critical issues to address (from ChatGPT review):**
    - Beat-frequency explanation for Lambda requires 10^-61 precision tuning -> physically unexplained
    - No mechanism selecting detuning values -> violates PDTP rigor rules; mark [SPECULATIVE]
    - Large frequency mismatch: if omega_P >> omega_particle -> mixing does NOT generate new scales
    - "Particle masses = detuning hierarchy" is numerical fit, not derivation -> mark [SPECULATIVE]
    - Must replace "hierarchy from beat frequencies" with "hierarchy from MULTI-MODE structure"
  - **Clean physical picture (from ChatGPT):**
    - phi_+ (bulk mode): high frequency (~Planck), sets G via omega_gap [DERIVED]
    - phi_- (surface/interface mode): low frequency (possibly cosmological), independent DOF [SPECULATIVE]
    - psi (matter): localised excitation at interface
    - Mixing: produces local modulation (fine structure), NOT necessarily global scale hierarchy
    - Two-phase frequency split -> [DERIVED / CORE RESULT]
    - Beat-frequency cosmology -> [SPECULATIVE] until mechanism for detuning is found
    - Central open problem: WHY omega_+ >> omega_- ?
  - **Forced Checklist Check — all ~30 items:**
    - **1. Reframe the Problem:**
      - [ ] Change the field/lens — condensed matter (BEC vacuum energy), topologist (phi_- winding),
            information theorist (entropy bound / CKN)
      - [ ] What-if — what if phi_- has a tiny mass in vacuum (not exactly zero)?
            What if the two phases are NOT exactly detuned?
      - [ ] Invert — what vacuum energy does the two-phase Lagrangian predict? (derive, don't assume)
      - [ ] Zoom in — 1D two-phase model; compute vacuum energy exactly
      - [ ] Zoom out — does Lambda change with cosmic time? (phi_- is dynamical — could evolve)
      - [ ] Rename — "surface mode vacuum occupation" instead of "cosmological constant"
      - [ ] One sentence — "What is the vacuum energy of the phi_- field in the two-phase Lagrangian?"
    - **2. Introduce Something New:**
      - [ ] New term — does phi_- self-interaction (phi_-^4) generate vacuum energy?
      - [ ] New variable — is there a phi_- condensate alongside the phi_+ condensate?
      - [ ] New constraint — T_mu_nu conservation for the FULL two-phase system
      - [ ] Change symmetry — phi_- breaks Z_2 exchange; does this generate Lambda?
      - [ ] Postulate and derive — if Lambda = (H_0/omega_P)^2 * rho_Planck, what does this imply?
      - [ ] Introduce a scale — can L_H emerge from phi_- dynamics? (not external input)
      - [ ] Order parameter — phase transition in phi_- at cosmological scales?
    - **3. Consistency Checks:**
      - [ ] Sudoku — substitute Lambda candidates into all 13+ engine tests
      - [ ] Limiting cases — Lambda -> 0 when phi_- -> 0? When phi_b = phi_s?
      - [ ] Dimensional analysis — dimensions of phi_- vacuum energy
      - [ ] Sign — does two-phase vacuum energy have the RIGHT sign (positive = accelerating)?
      - [ ] Overcounting — phi_+ and phi_- vacuum energies: separate or combined?
      - [ ] Circular — does any path use Lambda as input?
      - [ ] Order of magnitude — does two-phase calculation land near 10^-122?
    - **4. Use Analogies:**
      - [ ] Air/water/oil — interface energy between layers = vacuum energy?
      - [ ] Beat frequency — two detuned Planck oscillators (mark [SPECULATIVE])
      - [ ] AM radio — DC component of modulation envelope = Lambda?
      - [ ] Impedance mismatch — energy stored in bulk/surface mode mismatch
      - [ ] BEC analogue — quantum depletion of phi_- condensate (Part 54 Path A, now two-phase)
      - [ ] Chirality refractive — birefringence energy splitting of the vacuum?
    - **5. Handle Negative Results:**
      - [ ] If Lambda remains free, document exactly WHICH two-phase paths tried and failed
      - [ ] Find the correction factor — if all paths give 10^-122 * (something), what is that?
      - [ ] Find the sub-group — which consistency tests constrain Lambda? Which don't?
    - **6. Mathematical Strategies:**
      - [ ] Work backwards — assume rho_Lambda = observed; what phi_- vacuum state required?
      - [ ] Invariants — what is conserved in the phi_- sector? (topological charge? winding?)
      - [ ] Change coordinates — phi_- in Fourier space; vacuum mode occupation
      - [ ] Symmetry argument — most general phi_- vacuum consistent with all symmetries
      - [ ] Topological — topological contribution to Lambda from phi_- winding sectors?
      - [ ] Perturbation — expand phi_- around pi/2 equilibrium; 1-loop zero-point energy
    - **7. When Completely Stuck:**
      - [ ] List every assumption
      - [ ] What would have to be true?
      - [ ] What would falsify this?
      - [ ] Is Lambda the free parameter, or is it m_cond? (or both?)
  - **Derivation path (core mathematical work):**
    1. Write dispersion relations: phi_+: omega^2 = c^2*k^2 + m_+^2; phi_-: omega^2 = c^2*k^2 + m_-^2
    2. Derive m_-(Phi) from Lagrangian (reversed Higgs, Part 62, already started)
    3. Show omega_- emerges from symmetry/boundary conditions (NOT from tuning)
    4. Compute energy density contribution of phi_- -> compare to Lambda
    5. Compute T_mu_nu for FULL two-phase system (not just T_00; need T_ij too)
    6. Evaluate in vacuum: psi=0, phi_+=const, phi_-=0; check if U(1) shift still kills vacuum energy
    7. If not: compute rho_vacuum from phi_- zero-point fluctuations (1-loop)
    8. SymPy verification of all results
  - **Real physics mapping (validation / sanity check):**
    - Map phi_+/phi_- system to known systems:
      - BEC: phi_+ -> density (Higgs-like mode), phi_- -> phase (Goldstone mode)
      - Superfluid: bulk vs surface excitations
      - QFT: massive vs massless fields from symmetry breaking
    - Test: does ANY known system naturally produce omega_high/omega_low ~ 10^61?
      - If yes: same mechanism could apply to PDTP
      - If no: PDTP needs a NEW mechanism (and this is itself a finding)
  - **Implementation phases:**
    - Phase A: Two-phase vacuum energy (T_mu_nu, U(1) shift, 1-loop)
    - Phase B: Beat frequency derivation (delta, self-consistency, SymPy)
    - Phase C: Interface/impedance (surface energy, Hubble volume, CKN)
    - Phase D: Cross-checks (Part 63 16/16, Newton 3rd, Jeans, scalar backreaction,
               White NR limit, quantum geometry D_geom, chirality birefringence)
    - Phase E: Sudoku (15+ tests) + documentation
  - **Files:**
    - CREATE: `simulations/solver/cosmo_constant_v2.py` (Phase 37)
    - CREATE: `docs/research/cosmo_constant_two_phase.md`
    - EDIT: `simulations/solver/main.py` (add Phase 37)
    - EDIT: `TODO_02.md` (results)
    - READ ONLY: all existing phase modules for cross-checks
  - **Success criteria:**
    - BEST: Lambda derived from two-phase structure (no free parameters beyond m_cond)
    - GOOD: Lambda constrained to narrow range by two-phase consistency
    - ACCEPTABLE: mechanism (beat/interface) rigorously established, Lambda still free but understood
    - NEGATIVE: all paths fail — Lambda confirmed independent free parameter (closes investigation)
  - **Risk assessment:**
    - HIGH probability: T_mu_nu two-phase will show phi_- contributes to vacuum energy
    - MEDIUM probability: beat frequency gives correct ORDER of magnitude (10^-122 +/- few decades)
    - LOW probability: exact Lambda derivation with no new free parameters (would be breakthrough)
  - **Status markers to enforce:**
    - [DERIVED]: two-phase frequency split, phi_- dispersion, T_mu_nu
    - [SPECULATIVE]: beat-frequency cosmology, particle masses as detunings
    - [OPEN]: mechanism for omega_+ >> omega_-, detuning selection

- [ ] **Xi_cc+ baryon (LHCb 2026) — SU(3) flux tube benchmark**
  - LHCb confirmed Xi_cc+ (ccd) at 3619.97 MeV/c^2, ~915 events, decay Xi_cc+ -> Lambda_c+ K- pi+
  - Source: https://phys.org/news/2026-03-scientists-play-key-role-discovery.html
  - Two charm quarks + one down quark: doubly-heavy baryon
  - PDTP test: Part 37 Y-junction geometry + Part 38 string tension should predict binding energy
  - Mass = 2*m_charm + m_down + string tension corrections; compare to sigma = 0.173 GeV^2
  - Future work: when SU(3) lattice simulation (Part 42 GPU) is running, compute Xi_cc+ mass

- [ ] **Leidenfrost Effect as PDTP decoupling analogue**
  - Standard Leidenfrost: droplet on a hot pan vaporises its bottom layer instantly; the resulting
    steam cushion (~0.1mm) insulates the droplet from the surface — droplet floats on its own vapour,
    thermally decoupled, for minutes. Critical temperature ~193C for water.
  - PDTP analogue: matter (psi) in gravitational condensate (phi); if matter drives phi oscillation
    hard enough, local condensate becomes phase-incoherent ("vapour phase") — alpha = cos(psi-phi) -> 0
    — matter decoupled from gravity. Self-sustains as long as driving energy continues.
  - Mapping: hot surface = condensate, droplet = craft, steam layer = phase-incoherent boundary,
    Leidenfrost temperature = critical coupling energy (Delta V = g per oscillator)
  - phi_- connection (Part 61-62): phi_- is massless in vacuum, massive near matter (reversed Higgs).
    phi_- IS environment-dependent — could it act as the "vapour layer" boundary field?
    Question: can phi_- grow large enough to screen cos(psi - phi_+) -> 0?
  - Z3 Y-junction geometry — the craft mechanism:
    - Part 37: 3 quarks held by flux tubes in Y-junction at 120 degrees = Z3 symmetry
    - Lazar's craft description: 3 "gravity amplifiers" arranged in triangle at 120 degrees = same geometry
    - Hypothesis: 3 oscillating drums at 120 degree spacing create a Z3 topological defect in the
      gravitational condensate (same topology as a baryon/Y-junction)
    - Craft hull sits INSIDE this Z3 defect where phi is wound — cos(psi-phi) averages to 0
    - The "Leidenfrost layer" = the wound condensate boundary of the Z3 defect
    - Inverted acoustic levitation: craft generates its own standing wave pattern and sits at the node
  - UAP EM interference observations: suggests decoupling mechanism involves EM oscillation coupling
    to the gravitational condensate — consistent with the coil drum / phase-gradient concept
  - Why Goal 1 is prerequisite: if GR + QM emerge from ONE phase-locking system, then the same
    equations that explain quarks (Z3 confinement) tell you how to BUILD a Z3 decoupler.
    You cannot engineer decoupling without understanding the coupling first.
  - What would make this a Part: derive the phase-incoherent boundary condition from PDTP Lagrangian;
    show the Z3 defect geometry creates alpha -> 0 inside; calculate energy cost; compare to Leidenfrost
    critical temperature as a scaling argument

- [ ] **ChatGPT review gaps — items flagged by external critical review (2026-03-15)**
  - Context: ChatGPT given only two_phase_rederivation.md (old 157-line version without derivations).
    Some criticisms were documentation quality (now fixed: expanded to 1074 lines with full derivations).
    The items below are genuine PHYSICS gaps, not documentation gaps.
  - [ ] **Full stress-energy tensor T_mu_nu** — currently only T_00 (energy density, Part 43).
    Need spatial components T_ij. Required for: any reviewer who wants to check energy-momentum
    conservation, gravitational source terms, equation of state. Formula: T_mu_nu = dL/d(d^mu phi) d_nu phi - g_mu_nu L.
    Derive for all three fields (phi_b, phi_s, psi) in both single-phase and two-phase.
  - [ ] **Emergent metric g_mu_nu in closed form** — currently have acoustic metric (c_s = c, S8),
    tetrad extension (Part 12), PPN match (S9). But no single clean formula g_mu_nu(phi_b, phi_s, psi).
    Strong-field regime untested. Needed for: light bending calculation, frame-dragging, Kerr limit.
    Approach: use Part 12 tetrad Phi = sqrt(rho_0) exp(i*phi) e^a_mu and write g_mu_nu = eta_ab e^a_mu e^b_nu.
  - [ ] **Einstein equations from PDTP Lagrangian alone** — currently derived via imported GR machinery
    (tetrad, Part 12). Can we derive G_mu_nu = 8*pi*G T_mu_nu purely from phase-locking?
    This is the HARDEST open problem. If solved, it proves gravity IS emergent phase-locking.
    If it cannot be solved, PDTP remains a scalar-tensor complement to GR, not a replacement.
  - [ ] **Eigenvalue vs frequency clarification** — Part 61 Jeans eigenvalue +2*sqrt(2)*g is a
    growth rate (lambda), not omega^2. The system d^2x/dt^2 = Mx has: lambda > 0 = unstable (growth),
    lambda < 0 = oscillatory (omega = sqrt(-lambda)). Research docs should distinguish these clearly.
    Currently correct in the Python script but could confuse a reviewer reading only the .md file.
  - [ ] **ODE vs PDE assumption made explicit in all docs** — Python script states [A1]: spatially
    uniform fields (phi = phi(t) only). This is standard (Peskin & Schroeder sec 2.2) but research docs
    must state it prominently. Full PDE adds nabla^2 to LHS; RHS (coupling terms) unchanged.
    Every derivation that uses ODE form must say so, and state what changes when going to full PDE.
  - Items already addressed (do NOT redo):
    - "No SM path" — WRONG: Parts 37-53 cover SU(3), quarks, gluons, string tension, Koide, chirality
    - "Unsupported claims" — FIXED: 16/16 scorecard now has full derivations (1074 lines)
    - "PASS/FAIL scoreboards bad" — DISAGREE: scorecard WITH derivations is a powerful consistency tool
    - "Symbolic fields as Functions" — SymPy implementation choice, not physics; current approach is standard

---

## Methodology Note

Before starting any new part, follow the Problem-Solving Protocol (CLAUDE.md):
1. Read `docs/Methodology.md` and select relevant checklist items
2. Write a plan and present to user
3. Only proceed after approval

---

## Rules

- Do one part at a time (CLAUDE.md)
- User approves before committing/pushing to GitHub
- Every new equation needs a source citation or **PDTP Original** label
- All new Python files: ASCII only (no Unicode — Windows cp1252)
- Sudoku check on every new value/equation introduced

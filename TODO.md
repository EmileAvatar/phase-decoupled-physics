# TODO: Mathematical Formalization Roadmap

This file tracks the critical mathematical gaps that must be resolved for PDTP
to move from conceptual framework to testable physical theory.

See [math_status.md](docs/research/math_status.md),
[quantum_gravity_deep_dive.md](docs/research/quantum_gravity_deep_dive.md), and
[mathematical_formalization.md](docs/research/mathematical_formalization.md) for
full context.

---

## Critical Gaps

- [x] **Field equation for coupling parameter alpha**
  - ~~No governing equation exists for alpha(x,t)~~
  - Alpha is now derived from the Lagrangian: α = cos(ψ − φ)
  - Field equations derived via Euler-Lagrange in
    [mathematical_formalization.md](docs/research/mathematical_formalization.md) Section 3
  - **Sign error corrected:** coupling must be +cos for stability (Section 2.3)

- [x] **Energy cost of phase control**
  - Derived from Hamiltonian in Section 8
  - Decoupling energy per mode: ΔE = gᵢ (coupling constant)
  - Order of magnitude: ~10⁻⁹ J per kg (gravitational self-energy scale)
  - Gradient energy cost: E_grad = ∫ ½(∇(ψ−φ))² d³x

- [x] **Stability analysis**
  - Linearized perturbations satisfy Klein-Gordon equation (Section 6.2)
  - Dispersion relation: ω² = k² + 2g > 0 — all modes stable (Section 6.3)
  - Lyapunov stability proved via bounded Hamiltonian (Section 6.5)
  - Asymptotic stability holds in overdamped (Kuramoto) limit

- [x] **Conservation law compliance**
  - Energy conservation: proved via Noether's theorem + direct verification
    (Section 5.1, 5.4)
  - Momentum conservation: proved via Noether's theorem (Section 5.2)
  - Phase charge conservation: proved via global phase symmetry (Section 5.3)
  - Causality: preserved by Lorentz-invariant Lagrangian construction

- [x] **Quantum description of spacetime phase field (phi)**
  - ~~phi is currently undefined in standard physics~~
  - φ identified as the phase of a vacuum superfluid condensate (SVT)
  - Connected to established research: Volovik (2003), Barceló-Liberati-Visser (2005)
  - Lorentz invariance emerges at low energies (Volovik mechanism)
  - See [advanced_formalization.md](docs/research/advanced_formalization.md) §1
  - **Remaining:** microscopic structure of the condensate is unknown

- [x] **Quantitative GR recovery (Newtonian limit)**
  - Newtonian 1/r potential recovered in weak-field static limit (Section 7)
  - Poisson equation ∇²φ = −ρ_phase recovered (Section 7.5)
  - Newton's constant G identified via coupling-to-mass mapping (Section 7.5)
  - **Remaining:** Post-Newtonian corrections (perihelion, lensing, waves)

- [x] **Numerical experimental predictions**
  - δα at Earth surface: ~10⁻¹⁹ (Section 9.1)
  - BEC coherence amplification factor: √N (Section 9.2)
  - BEC prediction (N=10⁶): δα ~ 10⁻⁷ (approaching testability)
  - Falsifiable: coherent vs incoherent matter should show different free-fall

- [x] **Connect to Kuramoto model formally**
  - Overdamped limit of PDTP = standard Kuramoto model (Section 4.1)
  - PDTP is a relativistic, spatially-extended, second-order Kuramoto (Section 4.3)
  - Known Kuramoto results imported: critical coupling, phase transition,
    spontaneous synchronization (Section 4.2)

---

## Structural Requirements

- [x] Preserve Lorentz invariance — Lagrangian is Lorentz scalar by construction
- [x] Preserve energy-momentum conservation — proved via Noether (Section 5)
- [x] Be derivable from a consistent Lagrangian — Sections 2–3
- [x] Be experimentally testable — predictions in Section 9
- [x] Be distinguishable from existing GR/QFT predictions — coherence-dependent
  gravity is unique to PDTP (advanced_formalization.md §4.1)

---

## Completed (Advanced Topics — Part 2)

- [x] **Post-Newtonian corrections** ([advanced_formalization.md](docs/research/advanced_formalization.md) §2)
  - Cosine nonlinearity gives 1/r² correction to potential → perihelion precession ✓
  - Correct functional form (1/r³ force); magnitude depends on parameter fit
  - Gravitational waves propagate at c ✓ (Lorentz invariant by construction)
  - **Unresolved:** GW polarization (PDTP: scalar; GR: tensor); PPN parameter γ exact value
  - **Unresolved:** Shapiro delay, frame-dragging require full PPN calculation

- [x] **Quantum description of spacetime phase field** ([advanced_formalization.md](docs/research/advanced_formalization.md) §1)
  - φ = phase of vacuum superfluid condensate (SVT identification)
  - Connected to Volovik (2003), Barceló-Liberati-Visser (2005), Unruh (1981)
  - **Remaining:** microscopic condensate structure

- [x] **EM and nuclear force integration** ([advanced_formalization.md](docs/research/advanced_formalization.md) §3)
  - PDTP adds gravitational coupling to Standard Model (doesn't replace it)
  - Full combined Lagrangian written (L_PDTP + L_SM)
  - Gauge invariance resolved: gravity couples to de Broglie phase (gauge-invariant)
  - **Remaining:** photon coupling to φ (needs tensor extension)

- [x] **Experimental test design** ([advanced_formalization.md](docs/research/advanced_formalization.md) §4)
  - Dual-state BEC atom interferometry protocol designed
  - Three-phase experiment: baseline → increased coherence → phase modulation
  - Signal estimates: conservative ~10⁻¹⁶, optimistic ~10⁻¹³ (Δg/g)
  - Current precision ~10⁻¹² — approaching testability

## Remaining Work (Hard Open Problems)

- [x] **Gravitational wave polarization mismatch**
  - ~~PDTP gives 1 scalar mode; GR gives 2 tensor modes (LIGO-confirmed)~~
  - Resolved: tensor modes emerge from condensate tetrad structure (Volovik mechanism)
  - PDTP predicts E(2) class N₃: 2 tensor + 1 breathing mode
  - Breathing mode is a new testable prediction (multi-detector GW polarimetry)
  - See [hard_problems.md](docs/research/hard_problems.md) §1

- [x] **Full PPN parameter calculation**
  - γ = 1 from acoustic metric density perturbation (equal g₀₀ and gᵢⱼ)
  - β = 1 from Lorentz invariance and linear weak-field superposition
  - Independently: massive scalar Yukawa suppression → γ ≈ 1 at solar system scales
  - Nordtvedt parameter η_N = 0 (consistent with LLR)
  - **Caveat:** γ = 1 depends on condensate equation of state parameter κ = −2
  - See [hard_problems.md](docs/research/hard_problems.md) §2

- [x] **Vacuum condensate microscopic structure**
  - Constraints from PDTP Lagrangian: U(1) symmetry, Lorentz-invariant ground state,
    correct dispersion relation, cosine coupling emergence
  - Connected to Group Field Theory (Oriti 2014, Gielen & Sindoni 2016): spacetime
    as condensate of quantum tetrahedra
  - **Remains genuinely open:** microscopic constituents unknown (open in SVT itself)
  - See [hard_problems.md](docs/research/hard_problems.md) §3

- [x] **Photon coupling to φ**
  - Resolved: photons couple INDIRECTLY via acoustic metric (not via cos coupling)
  - Photons follow null geodesics of the acoustic metric
  - Light bending: θ = 4GM/(bc²) — matches GR (factor of 2 from γ = 1)
  - Gravitational redshift: Δν/ν = ΔU/c² — matches GR
  - No tensor extension of fundamental Lagrangian needed; tensor structure is emergent
  - See [hard_problems.md](docs/research/hard_problems.md) §4

## Remaining Questions (Identified During Part 3 Work)

- [x] **Derive κ = −2 from first principles**
  - ~~Currently assumed; should be derived from the condensate dynamics~~
  - Derived via Painlevé-Gullstrand representation: acoustic metric with constant
    density + free-fall velocity = Schwarzschild metric, which has γ = 1
  - κ is coordinate-dependent (0 in PG, −2 in isotropic); γ = 1 is physical
  - Independently confirmed: relativistic Euler equation with c_s = c gives δρ/ρ₀ = 2U
  - See [hard_problems.md](docs/research/hard_problems.md) §2.11

- [x] **Condensate tetrad structure**
  - Analyzed: He-3A order parameter (Volovik) provides the physical precedent
  - PDTP scalar Lagrangian does NOT produce tetrads — explicit extension needed
  - Minimal extension: Φ_vacuum = √ρ₀ e^{iφ} e^a_μ (tetrad + phase)
  - **Remains the most important structural gap in PDTP**
  - See [hard_problems.md](docs/research/hard_problems.md) §1.10

- [x] **Breathing mode amplitude relative to tensor**
  - Mapped to Brans-Dicke: h_breathing/h_tensor < 1/(2ω+3) < 1.25 × 10⁻⁵ (Cassini)
  - Massive scalar adds Yukawa suppression above threshold frequency
  - Below current LIGO detection threshold; may be accessible with 5+ detectors in 2030s
  - See [hard_problems.md](docs/research/hard_problems.md) §1.9

- [x] **EM coupling constant G_EM in equation (4.3)**
  - ~~Should be fixed by requiring equivalence principle (E = mc²)~~
  - **Resolved: the G_EM term must be REMOVED.** EM stress-energy tensor is traceless
    (T^μ_μ = 0), so photons cannot source a scalar field at classical level. This is
    Nordström's problem. Equation (4.3) replaced by equation (4.7) with only matter sources.
  - Photons still gravitate via acoustic metric geodesics (test particles) and through
    bound EM energy in composite matter (gravitational sources)
  - See [hard_problems.md](docs/research/hard_problems.md) §4.8

## New Questions (Identified During Part 3b Work)

- [x] **Free photon radiation as gravitational source**
  - Free photons don't source □φ (EM trace = 0) — established physics
  - Energy bookkeeping: emitter loses mass E/c², absorber gains it back
  - Thermal equilibrium suppression: t_interaction/t_grav ~ 10⁻¹⁴ in stellar interiors
  - Solar system deficit: ΔM/M☉ ~ 2 × 10⁻²¹ per second — undetectable
  - Self-limiting argument: radiation dominates only when tightly coupled
  - **Conclusion:** cosmological problem, not astrophysical; negligible for all
    post-equality physics. Radiation-era implications addressed separately.
  - See [photon_gravity_analysis.md](docs/research/photon_gravity_analysis.md)

- [x] **Radiation-dominated era cosmology**
  - Matter-era Friedmann equation derived from condensate Euler + continuity
  - Cosmic expansion = condensate Hubble flow v_i = H(t) x_i
  - Tight-coupling resolves photon contribution: effective mass m_eff = m_b + ρ_γ/(n_b c²)
  - Self-limiting: radiation dominates only when tightly coupled to baryons
  - **Genuine gap:** decoupled neutrinos at BBN (41% of ρ_total missing, ~23% error in H)
  - Resolution requires acoustic metric tensor channel or condensate extension
  - See [radiation_era_cosmology.md](docs/research/radiation_era_cosmology.md)

- [x] **Derive Newton's constant G from coupling constants gᵢ independently**
  - Dimensional analysis: G = 𝒞 c^(5/2)/√(ℏρ₀), exact for ρ₀ = ρ_Planck (§2)
  - Coupling gᵢ shown to be geometric (~4πRᵢ), not independent parameters (§3)
  - Reduces N+2 apparent free parameters to 1 effective unknown (𝒞 or ρ₀)
  - Energy-cost circularity resolved: decoupling energy from gᵢ, not Gm²/R (§7)
  - **Remaining gap:** dimensionless prefactor 𝒞 requires condensate microphysics
  - Full derivation needs: what condenses, why, and the ground-state density
  - See [G_derivation.md](docs/research/G_derivation.md)

- [x] **Strong-field equivalence principle**
  - Phase difference δψ = compactness Ξ = GM/(Rc²): 0.21 for NS, 0.50 at BH horizon
  - Nonlinearity sin(δψ)/δψ: 0.7% for NS, 4.1% at horizon — mild throughout
  - Strong-field Nordtvedt parameter: η ~ Ξ²/6 ≈ 7×10⁻³ for NS
  - Gravitational binding energy gravitates correctly to leading order: M_eff = M(1−Ξ/2)
  - Cosine saturation unobservable: δψ < 0.5 for all objects outside their horizons
  - Acoustic horizon at r = 2GM/c² (exact Schwarzschild radius)
  - **Tension:** Double pulsar Ṗ_b (0.013% precision) vs ~1% PDTP GW emission deficit
  - Resolution requires numerical NS interior solution or self-consistent metric proof
  - See [strong_field_ep.md](docs/research/strong_field_ep.md)

- [x] **Explicit momentum balance for phase-gradient motion**
  - Derived local momentum transfer force density: F^k_j = −gⱼ sin(ψⱼ−φ) ∂^k ψⱼ
  - Worked Example 1: Test particle in static phase gradient — field absorbs equal/opposite momentum
  - Worked Example 2: Two-body exchange — spacetime field acts as transparent intermediary
  - Newton's second law (F = mg) recovered from momentum transfer rate
  - "Reactionless drive" objection fully resolved: propellant-free ≠ momentum-violating
  - EM analogy: Poynting vector ↔ (∂₀φ)(∇φ) structural correspondence
  - Earth–Sun quantitative budget: field momentum ~10⁻⁸ of matter momenta (post-Newtonian hierarchy)
  - Key result: dP^k_ψ/dt = −dP^k_φ/dt (Newton's third law for phase-gradient motion)
  - See [momentum_balance.md](docs/research/momentum_balance.md)

---

## Stretch Goals (Would Strengthen the Framework)

- [x] **Derive the Koide formula** from phase harmonic geometry
  - Proved: Z₃ phase parametrization √mᵢ = μ(1 + δ cos(θ₀ + 2πi/3)) gives Q = (1+δ²/2)/3
  - Q = 2/3 ⟺ δ = √2 (exact mathematical result)
  - Geometric interpretation: √m vector at 45° to democratic direction (1,1,1)
  - Lepton fit: μ = 17.72 MeV^{1/2}, θ₀ ≈ 2/9 (Brannen)
  - Quark extension: (c,b,t) near-Koide Q = 0.669, signed (s,c,b) ≈ 0.675
  - Physical argument: δ = √2 from equal partition of symmetric/breaking energy
  - See [koide_derivation.md](docs/research/koide_derivation.md)

- [x] **Derive the fine-structure constant** from phase impedance matching
  - Exact identity: α = Z₀/(2R_K) = (EM impedance)/(2 × quantum impedance) = 1/137.036
  - PDTP interpretation: coupling efficiency between EM and matter-wave phase media
  - Impedance mismatch explains why α is small: R_K/Z₀ ≈ 69 (media stiffness ratio)
  - Length scale cascade: r_e = αλ̄_C = α²a₀ as standing-wave harmonics
  - Running of α: energy-dependent quantum impedance from vacuum polarization
  - Wyler's formula discussed (α_W⁻¹ = 137.036..., 0.6 ppm, but no solid derivation)
  - **Honest status:** structural interpretation achieved; numerical derivation remains open
  - See [fine_structure_derivation.md](docs/research/fine_structure_derivation.md)

- [x] **Simulation of emergent GR**
  - N-body simulation of phase-coupled oscillators → 5 independent tests
  - Smooth curvature from N=10 to N=1000 discrete oscillators (< 0.5% error)
  - Quantitative match to Newtonian predictions: 1/r potential (1.35% error),
    1/d force law (exponent −0.984), Kuramoto synchronization (R = 1.0000),
    weak-field linearization (machine-precision match)
  - See [emergent_gr_results.md](docs/research/emergent_gr_results.md)
  - Simulation: [emergent_gr_simulation.py](simulations/emergent_gr_simulation.py)

- [x] **Derive Hawking temperature from acoustic horizon** *(Part 24 — 2026-02-25)*
  - PDTP condensate flow v = −√(2GM/r); acoustic horizon at r_H = 2GM/c² (Schwarzschild)
  - Surface gravity: κ_s = (1/2)|d(c²−v²)/dr|_{r_H} = c⁴/(4GM) — exact match to GR
  - Hawking temperature: T_H = ℏκ_s/(2πk_Bc) = ℏc³/(8πGMk_B) ✓ (Unruh formula applied)
  - Trans-Planckian resolved: lattice cutoff at ω_Planck; spectrum preserved by Unruh & Schützhold (2003)
  - Robustness check: ω_Planck/(κ_s/c) ~ 10¹¹ for stellar BHs — condition well satisfied
  - Physical mechanism: phonon pair separation at sonic horizon (cf. Steinhauer 2016 BEC experiment)
  - Key references: Unruh (1981) PRL 46 1351; Visser (1998) CQG 15 1767; Unruh & Schützhold (2003) PRD 71 024028
  - See [hawking_radiation_pdtp.md](docs/research/hawking_radiation_pdtp.md)

---

## Open Problems (Future Work)

### Structural Gaps

- [x] **Condensate tetrad extension**
  - Extended order parameter: Φ = √ρ₀ e^{iφ} e^a_μ (phase + tetrad)
  - Extended Lagrangian: Palatini action + covariantized phase coupling (eq. 4.8)
  - Field equations derived: torsion (vanishes), Einstein, covariant □_g φ, covariant □_g ψ
  - DOF counting: 16 − 6 (Lorentz) − 4 (diffeo) = 6 off-shell → 2 tensor + 1 breathing
  - Linearized analysis: □h^{TT}_{ij} = 0 (tensor at c) + □θ + 2gθ = 0 (massive breathing)
  - E(2) class N₃: matches LIGO observations (2 tensor) + suppressed breathing
  - All Parts 1–11 results preserved in weak-field limit
  - Symmetry breaking: GL(4,ℝ) × U(1) → SO(3,1), Goldstone interpretation
  - New predictions unlocked: frame-dragging, Kerr metric, torsion at extreme densities
  - GFT condensate identified as candidate microscopic origin
  - **Remaining:** microscopic origin of tetrad structure, symmetry breaking potential
  - See [tetrad_extension.md](docs/research/tetrad_extension.md)

- [x] **Double pulsar tension resolution**
  - Original tension: scalar-only PDTP predicts ~1.5% GW emission deficit (sin(Ξ)/Ξ)²
  - Double pulsar Ṗ_b measured to 0.013% precision — was 100× tension
  - **Resolution via two arguments:**
    1. Tetrad extension (Part 12): dominant GW channel = tensor modes → Einstein equation → quadrupole formula = GR
    2. U(1) symmetry: φ → φ+c, ψ → ψ+c leaves Lagrangian invariant → scalar charge α_A = 0 for all bodies → zero scalar radiation
  - Ṗ_b^PDTP = Ṗ_b^GR exactly (tensor emission = GR, scalar emission = 0)
  - Spontaneous scalarization ruled out (β_A = 0 identically, unlike DEF theory)
  - Consistent with double pulsar (0.013%), Hulse-Taylor (0.3%), and all future binary pulsar tests
  - **Remaining:** numerical NS interior solution desirable (not required) for independent confirmation
  - See [double_pulsar_resolution.md](docs/research/double_pulsar_resolution.md)

### Genuinely Open Problems

- [x] **Condensate microphysics (microscopy)**
  - What are the microscopic constituents of the vacuum condensate?
  - **Status:** Genuinely open — thorough analysis completed (Part 14)
  - 10 constraints on the condensate compiled from Parts 1–13
  - 5 candidate theories analyzed: Volovik (trans-Planckian), GFT, LQG, causal sets, string theory
  - **GFT identified as best candidate** (7/10 constraints satisfied)
    - Natural tetrad structure from quantum tetrahedra
    - Condensate phase = PDTP phase φ
    - Already derives Friedmann equation (Gielen, Oriti, Sindoni 2013)
    - Critical gap: cos(ψ−φ) coupling not yet derived from GFT
  - Downstream blockage analysis: phenomenological predictions (PPN, GW, binary pulsars) UNAFFECTED by universality; only "deep" quantities (G prefactor, Λ, α_EM) blocked
  - Universality argument: PDTP works as effective theory regardless of microphysics (Volovik)
  - GFT-PDTP dictionary constructed with 3 missing links identified
  - Research roadmap: near-term (equation correspondence), medium-term (matter coupling), long-term (coupling constants)
  - **Remaining:** This is the deepest open problem — genuinely unsolved across all QG programs
  - See [condensate_microphysics.md](docs/research/condensate_microphysics.md)

- [x] **Decoupled neutrino energy at BBN**
  - At Big Bang nucleosynthesis (z ~ 10⁹), neutrinos carry 41% of ρ_total
  - In scalar-only PDTP: neutrinos don't source □φ (trace = 0) → 23% error in H at BBN
  - **Resolution via tetrad extension (Part 15):**
    1. Extended PDTP (Part 12) derives Einstein equation G_μν = 8πG T_μν
    2. The (0,0) component gives Friedmann equation with FULL ρ_total including ρ_ν
    3. The tensor sector uses T_00 = ρ_ν directly — the trace T = 0 is irrelevant
    4. Same pattern as double pulsar resolution (Part 13): scalar-only artifact resolved by tensor sector
  - Result: H²_PDTP = H²_GR at ALL epochs (BBN, equality, recombination, present)
  - Two-sector structure: tensor (all energy) + scalar (phase-locking mechanism)
  - See [radiation_era_cosmology.md](docs/research/radiation_era_cosmology.md) §8

### Cosmological Open Problems

- [x] **Hubble tension from phase drift**
  - Standard physics: H₀ = 73.0 ± 1.0 km/s/Mpc (local, SH0ES) vs
    H₀ = 67.4 ± 0.5 km/s/Mpc (CMB + ΛCDM, Planck) — ~5σ tension
  - **Quantitative analysis completed (Part 16):**
    1. Phase drift rate ∝ 1/ρ_local (nonlinear enhancement from cosine coupling)
    2. Direct scalar drift mechanism: Cassini bound ε_s < 10⁻⁵ → quantitatively insufficient
    3. Backreaction from phase inhomogeneity: σ²_δψ ~ 10⁻¹⁰ → also insufficient (~9 orders of magnitude)
    4. Both mechanisms fail because phase mismatches Φ/c² ~ 10⁻⁵ are too small
  - **Honest conclusion:** PDTP cannot currently explain the 8% Hubble tension
  - Deep connection identified: Hubble tension ↔ dark energy ↔ phase drift (common root)
  - Conditional predictions: if scalar sector relevant, H₀ should correlate with environment density
  - See [hubble_tension_analysis.md](docs/research/hubble_tension_analysis.md)

- [x] **Cosmological constant / dark energy from phase drift**
  - Standard physics: ρ_Λ ≈ 6 × 10⁻²⁷ kg/m³ (68% of universe), origin unknown
  - Cosmological constant problem: QFT predicts ρ_vacuum ~ ρ_Planck, observed
    value is 10¹²² times smaller — worst prediction in physics
  - **Quantitative analysis completed (Part 17):**
    1. Scalar sector phase-filters vacuum fluctuations (⟨sin(ψ_vac − φ)⟩ = 0)
    2. ρ₀ vs ρ_Λ reframing: dark energy = condensate perturbation δρ₀/ρ₀ ~ 10⁻¹²³
    3. Phase drift → dynamical dark energy with w ≠ −1 (consistent with DESI 4.2σ evidence)
    4. BUT: tensor sector has G_μν = 8πG T_μν → inherits GR's full Λ problem
  - **Honest conclusion:** PDTP provides partial reframing (scalar sector novel mechanism)
    but cannot solve the cosmological constant problem (tensor sector unsolved)
  - Cannot derive ρ_Λ from first principles; drift rate requires microphysics
  - Common root with Hubble tension and phase drift mechanism (Part 16)
  - See [cosmological_constant_analysis.md](docs/research/cosmological_constant_analysis.md)

- [x] **Aharonov-Bohm effect and PDTP phase structure**
  - The AB effect (Tonomura 1986) proves phase is physically real and can
    alter physics without any local force — the same paradigm PDTP uses
  - **Deep analysis completed (Part 18):**
    1. COW experiment: PDTP reproduces gravitational phase shift exactly
       (Δφ = (m/ℏ)∫Φdt) — consistency check via weak-field limit
    2. Fiber bundle classification: PDTP = U(1)_global × SO(3,1) product
       bundle (trivial scalar bundle + GR frame bundle)
    3. Topological defects: cosmic strings interpreted as quantized vortex
       lines in the condensate phase field (∮∇φ·dl = 2πn)
    4. EM–gravity: genuine structural parallel (both phase coupling), but
       gauging PDTP's U(1) does NOT naturally produce electromagnetism
    5. Impact assessment: no modifications to existing results needed —
       geometric consistency confirmed across all previous Parts
  - 2022 Overstreet et al. (Science) observed gravitational AB phase shift
    with atom interferometry — strongest experimental support for phase paradigm
  - **Honest conclusion:** PDTP is geometrically consistent; topological
    aspects (cosmic strings as vortices) are suggestive but speculative;
    EM–gravity parallel is real but not unification
  - See [aharonov_bohm_pdtp.md](docs/research/aharonov_bohm_pdtp.md)

- [x] **Phase drift mechanism** *(Part 19 — 2026-02-22)*
  - Analyzed four candidate mechanisms for cosmic-scale phase de-synchronization:
    1. Finite coherence length ξ = c/√(2g) (★★★★ — primary mechanism, explains
       scale transition directly via exponential decay of phase correlations)
    2. Cosmological expansion (★★★ — provides time evolution through a(t),
       self-consistent but circular)
    3. Thermal fluctuations / two-fluid model (★★★ — maps dark energy to
       condensate normal fraction; universe is deep in superfluid phase, T ≪ T_c)
    4. Topological defects / phase vortices (★★☆ — Kibble-Zurek formation
       mechanism, inter-vortex spacing sets effective ξ, most speculative)
  - Developed effective Langevin equation: δφ̈ + 3H(t)δφ̇ + g_eff(t)δφ = η(t)
  - Qualitative w(z) matches DESI DR2: w₀ > −1, w_a < 0 emerge naturally from
    overdamped → resonant → relaxation dynamics without fine-tuning
  - Honest conclusion: framework, not solution — quantitative predictions require
    condensate microphysics (g, T_cond, n_vortex, γ_micro all unknown)
  - See [phase_drift_mechanism.md](docs/research/phase_drift_mechanism.md)

### Structural Directions (from external review, Part 17)

These items were identified through independent external review of the
cosmological constant analysis. Both reviews converged on the same
structural diagnosis and recommended directions.

- [x] **Vacuum energy and the tensor sector: background subtraction mechanism** *(2026-02-24)*
  - The "PDTP trilemma": cannot simultaneously have (a) exact GR recovery,
    (b) scalar vacuum filtering, and (c) cosmological constant solution
  - Both external reviews recommend Option 3: condensate background subtraction
  - Key idea: if the condensate ground state defines the metric background,
    then ρ₀ is "already included" in the geometry — only deviations δρ gravitate
  - Possible implementation: T_μν^phys = T_μν − ⟨T_μν⟩_condensate
  - This modifies what emerges from the Palatini variation in Part 12
  - Related approaches: unimodular gravity, vacuum energy sequestering,
    emergent gravity models, analogue gravity (acoustic metric doesn't feel
    total fluid mass — only perturbations)
  - **Answered:** Palatini variation does NOT naturally produce background
    subtraction — explicit action modification required (Option B: perturbative
    expansion around ground state is the most natural implementation)
  - **Risk assessed:** Uniform subtraction does not modify local gravitational
    dynamics — solar system tests are passed; time-varying subtraction is
    bounded by Brans-Dicke constraints
  - See [vacuum_background_subtraction.md](docs/research/vacuum_background_subtraction.md)
  - Status: completed 2026-02-24

- [x] **Dark energy as condensate normal fraction (temperature model)** *(2026-02-24)*
  - Map dark energy to condensate thermodynamics near critical temperature T_c
  - Superfluid analogy: below T_c → full coherence; near T_c → normal fraction grows
  - Dark energy density ∝ normal fraction of condensate = (T/T_c)^β or similar
  - This would naturally produce: time evolution of w, w₀ > −1, w_a < 0
  - Must model: order parameter evolution, condensate fraction f(t), effective
    equation of state from φ dynamics
  - **Key question:** Is the universe sitting near criticality? Is this stable
    or accidental? If criticality is an attractor state, this becomes powerful
  - Connects to: DESI DR2 results (energy density peaked at z ≈ 0.45),
    condensate microphysics (Part 14), phase drift mechanism
  - **Answered:**
    - ρ_DE = f_n × ρ₀ (normal fraction of Planck-density condensate)
    - Equation of state: w_drift = (K−V)/(K+V) naturally gives w₀ > −1, w_a < 0
    - Universe is NOT near criticality: T_cond/T_c ~ 10⁻³¹ (f_n ~ 10⁻¹²³)
    - No attractor mechanism known — coincidence problem persists
    - Qualitative DESI DR2 match (peaked density at z ~ 0.45) from Langevin dynamics
    - Canonical scalar cannot produce phantom w < −1 (DESI tension noted)
  - See [dark_energy_normal_fraction.md](docs/research/dark_energy_normal_fraction.md)
  - Status: completed 2026-02-24

- [x] **Derive explicit w(z) from phase drift dynamics** *(Part 25 — 2026-02-25)*
  - Slow-roll approximation: ε = g_eff/(9H²) (phase-locking coupling / Hubble friction)
  - Equation of state: w(z) = [ε(z) − 1] / [ε(z) + 1]
  - CPL prediction: w_a = −(1 − w₀²)/2 × (m + 3Ω_m)  for g_eff ∝ a^m
  - Constant coupling (m=0): w_a ≈ −0.15  (2.1σ below DESI central value)
  - DE-tracking coupling (m=3): w_a ≈ −0.62  (consistent with DESI, 0.4σ)
  - Best-fit m ≈ 3.8 matches DESI's w_a = −0.75 exactly
  - Consistency line in (w₀, w_a) plane: falsifiable by future surveys (Euclid, DESI Y5)
  - R ≡ −w_a/[(1−w₀²)/2] = m + 3Ω_m directly measures condensate coupling evolution
  - Phantom tension: PDTP canonical scalar cannot produce w < −1 (honest assessment)
  - See [wz_dark_energy_pdtp.md](docs/research/wz_dark_energy_pdtp.md)

- [x] **Free parameter m analysis** *(Part 26 — 2026-02-26)*
  - The coupling evolution exponent m in g_eff(a) = g₀ a^m was a free parameter
  - Self-consistency condition derived: m = 6ε (ε = slow-roll parameter)
  - With DESI ε₀ = 0.095 → m = 0.57, giving w_a ≈ −0.24 (1.8σ from DESI)
  - Dynamical scaling argument: m = 2 − η ≈ 2.0 (XY universality class)
  - Thermal activation (speculative): m = 3 (2D) or m = 4.5 (3D)
  - **Honest finding:** m = 3 (from Part 25) was curve-fitting, not a derivation
  - Best internal prediction: m ≈ 0.57 (self-consistency) or m ≈ 2 (scaling)
  - Escape hatch: non-constant ε(a) could boost effective m (calculable)
  - Falsifiable predictions robust regardless of m: consistency line R = m + 3Ω_m,
    phantom bound w ≥ −1
  - See [free_parameter_m_analysis.md](docs/research/free_parameter_m_analysis.md)

- [x] **Scalar vs tensor gravity analysis** *(Part 27 — 2026-02-26)*
  - Scalar PDTP predicts breathing mode GWs; LIGO confirms tensor (+ and ×) modes
  - **Key insight:** Part 21 oscillator lattice already has shear rigidity
  - Lattices support transverse (shear) waves → these ARE the tensor modes
  - Scalar PDTP has been using only the longitudinal branch of the lattice
  - Two transverse branches contain the missing tensor GW polarizations
  - Required condition: shear modulus μ = bulk modulus B = v² (gives c_T = c)
  - Three approaches identified: tetrad extension, lattice shear modes, elastic condensate
  - **Most promising:** extract all three wave branches from the Part 21 lattice
  - This is a mathematical completion task, not a conceptual redesign
  - See [scalar_vs_tensor_gravity.md](docs/research/scalar_vs_tensor_gravity.md)

- [ ] **PRIORITY: Derive tensor GW modes from oscillator lattice** *(Part 28 — planned)*
  - Compute full dispersion relation of Part 21 lattice (all branches)
  - Show transverse modes propagate at c in continuum limit
  - Identify two transverse polarizations with GR's + and × modes
  - Derive effective metric g_μν = η_ab ∂_μφ^a ∂_νφ^b from lattice
  - Verify shear modulus = bulk modulus condition (μ = B = κ = v²)
  - Show accelerating phase defect emits transverse waves (quadrupole formula)
  - If successful: closes the single biggest gap in PDTP
  - **Depends on:** efv_microphysics.md (Part 21), tetrad_extension.md (Part 12)

- [ ] **Scalar sector backreaction on tensor sector**
  - Does the scalar sector modify the effective T_μν seen by the tensor sector?
  - If φ dynamics change the condensate stress-energy, this could feed back
    into the Einstein equation through modified G or effective Λ
  - Could bridge the gap between scalar (vacuum-insensitive) and tensor
    (vacuum-sensitive) sectors
  - Related to whether G varies dynamically through condensate evolution

### Black Holes in PDTP

- [ ] **Black hole singularity as topological defect**
  - Standard GR: r=0 singularity (curvature → ∞, classical divide-by-zero)
  - In PDTP: phase θ is periodic (θ mod 2π), gradients bounded by lattice spacing a ~ ℓ_Planck
  - r=0 is replaced by a vortex core: a topological defect with finite energy density
    (analogous to a superfluid vortex, where the core has finite healing length ξ)
  - Needs: formal treatment of condensate structure at r < ℓ_Planck; what replaces the
    curvature singularity in the PDTP picture?
  - Possible resolution: Penrose singularity theorems assume continuous manifold — lattice
    cutoff evades them (similar to LQC bounce)

- [ ] **Hawking radiation information paradox in PDTP condensate**
  - Standard paradox: Hawking radiation is thermal (random) → information about infalling
    matter appears lost, violating unitarity
  - PDTP angle: infalling matter perturbs the condensate phase field φ; these phase
    perturbations propagate outward as phonons — phase correlations persist outside horizon
  - Question: do exterior condensate phase correlations encode the phase pattern of
    infalling matter? (analogous to superfluid vortex retaining circulation information)
  - May be testable in analogue systems (sonic black holes in BECs — Steinhauer 2016)
  - Status: speculative — requires explicit calculation of phase correlations in condensate

- [ ] **Black hole evaporation endpoint in PDTP**
  - As BH evaporates: M decreases → T_H = ℏc³/(8πGMk_B) increases → evaporation
    accelerates → M → M_Planck
  - At M ~ M_Planck: condensate picture breaks down (BH radius ~ lattice spacing ~ ℓ_Planck)
  - What replaces the classical singularity in the final state? Topological defect?
    Phase soliton? Complete decoherence of the condensate locally?
  - Status: genuinely open — requires full lattice-scale condensate theory (GFT/LQG)

### Standard Model Mapping

- [ ] **Part 22: Antimatter as Opposite-Winding Topological Defects** *(planned)*
  - Antiparticle = opposite winding number (−1) vs particle (+1)
  - Vortex/antivortex analogy from BEC/superfluid
  - Annihilation as winding cancellation → energy radiated as φ-waves
  - CPT symmetry in PDTP: explicit verification needed
  - Matter-antimatter asymmetry: initial condensate asymmetry (open)
  - Gravity of antimatter: same cos coupling → falls down ✓ (ALPHA 2023)
  - Status: planned — not yet written

- [x] **Part 23: Charge, Color, Hadrons, and Quantum Numbers in PDTP** *(Part 23 — 2026-02-23)*
  - Electric charge: U(1) symmetry + winding number interpretation
  - Fractional charges: Z₃ structure, partial topological cycles
  - Hadrons: baryons (3 quarks = complete cycle) and mesons (quark+antiquark)
  - Color as phase position (0, 2π/3, 4π/3) in condensate wave
  - Confinement = completing the wave cycle (3 × 1/3 = integer)
  - Gluons as condensate phase transfer between partial defects
  - Nuclear binding as phase wave packet overlap (Yukawa range check ✓)
  - Speculative section: condensate wave model (crest=particle, trough=antiparticle)
  - Status: completed 2026-02-23

- [x] **Standard Model and PDTP particle-force mapping** *(Part 20 — 2026-02-22)*
  - Systematic side-by-side mapping of all 17 SM particles to PDTP interpretations
  - Key equations for each SM force (EM, strong, weak) + PDTP gravity
  - Complete particle table with PDTP coupling constant estimates gᵢ
  - Combined Lagrangian: L_total = L_spacetime + L_SM + L_PDTP_gravity
  - Higgs ↔ PDTP condensate structural parallel identified
  - Mass hierarchy reframed as coupling hierarchy (not solved)
  - Honest conclusion: PDTP adds gravity as phase-locking, preserves all SM
    gauge structure unchanged. Mapping is interpretive, not predictive.
  - See [standard_model_pdtp_mapping.md](docs/research/standard_model_pdtp_mapping.md)

### Microphysics Priority (from external review)

These items target the keystone open problem: condensate microphysics.
Strategic priority: derive κ → G from first principles.

- [x] **Energy-Frequency-Vibration microphysics approach** *(Part 21 — 2026-02-22)*
  - Tesla-inspired framework: assume universe = energy, frequency, vibration
  - Defined E/F/V rigorously in established physics AND PDTP
  - Built oscillator lattice Hamiltonian: H = Σ(I/2)(∂ₜθ)² + (K/2)Σ(θᵢ−θⱼ)²
  - Derived: c² = κ/ρ, G = c²/(4πκ), M_eff = (ρ/3)∫(∇θ₀)²d³x
  - Cosine coupling derived from |Φ−Ψ|² symmetry breaking: g = 2λ√(ρσ)
  - Lattice parameters computed: K ≈ 5.78 × 10⁻¹⁰ J, I ≈ 5.03 × 10⁻⁹⁶ kg·m²
  - Constraint check: 5/10 (scalar model; tensor constraints need Part 12)
  - Isolated from main PDTP — exploratory microphysics document
  - See [efv_microphysics.md](docs/research/efv_microphysics.md)

- [x] **Derive cosine coupling from symmetry breaking** *(Part 21 — 2026-02-22)*
  - Started with complex fields Φ = √ρ e^{iφ}, Ψ = √σ e^{iψ}
  - Expanded |Φ − Ψ|² = ρ + σ − 2√(ρσ) cos(ψ − φ)
  - Cosine coupling emerges naturally with g = 2λ√(ρσ)
  - Status: plausibility argument (choice of |Φ−Ψ|² needs justification)

- [x] **Derive phase stiffness κ from condensate equation of state**
  - κ = v² (condensate order parameter squared) — from Goldstone effective Lagrangian
  - Equals bulk modulus B = ρ_mass × c_s² = ρ_mass × c² for a c_s = c condensate
  - Compressibility χ_s = 4πG/c² (extraordinarily small — gravity weak ↔ condensate stiff)
  - G = c²/(4πv²): Newton's constant set by inverse square of the condensate vev
  - Remaining open: what sets v? Requires μ and λ from microscopic theory (GFT, Part 14)
  - See [efv_microphysics.md](docs/research/efv_microphysics.md) §8.7

- [x] **Derive inertial mass–frequency relation explicitly** *(Part 21 — 2026-02-22)*
  - Derived M_eff = (ρ/3)∫(∇θ₀)²d³x from moving defect kinetic energy
  - Rest energy E₀ = M_eff c², Compton frequency ω₀ = M_eff c²/ℏ
  - Mass = localized frequency detuning = integrated phase distortion energy
  - Structural win: mass is emergent, not fundamental (polaron/soliton analogy)

- [x] **Oscillator lattice Hamiltonian for spacetime** *(Part 21 — 2026-02-22)*
  - Minimal discrete model: H = Σ(I/2)(∂ₜθ)² + (K/2)Σ(θᵢ−θⱼ)²
  - Continuum limit with careful dimensional analysis: ℋ = (ρ/2)(∂ₜθ)² + (κ/2)(∇θ)²
  - Derived c² = κ/ρ, G = c²/(4πκ), M_eff = (ρ/3)∫(∇θ₀)²d³x
  - GFT connection noted (Part 14) — tetrahedra as possible oscillators

---

## Status

```
Mathematical formalization complete (three parts + follow-up).

Part 1: Lagrangian, field equations, conservation laws, stability,
Newtonian recovery, order-of-magnitude predictions.

Part 2: Quantum φ definition (superfluid vacuum), post-Newtonian corrections,
Standard Model integration, experimental test design.

Part 3: GW polarization (emergent tensor + breathing mode), PPN parameters
(γ=1, β=1), vacuum condensate constraints (GFT connection), photon coupling
(indirect via acoustic metric, factor-of-2 recovered).

Part 3b (follow-up): κ=−2 derived (PG representation), breathing mode
amplitude quantified (<10⁻⁵), tetrad structure analyzed (extension needed),
G_EM resolved (removed — trace problem). Field equation simplified.

All "Remaining Questions" from Part 3 addressed.
Part 4: Koide formula derived from Z₃ phase harmonic geometry. Proved
Q = 2/3 ⟺ δ = √2. Extended to quarks: (c,b,t) near-Koide. Physical
origin of δ = √2 from equal energy partition. θ₀ = 2/9 remains empirical.

Koide stretch goal completed.
Part 5: Fine-structure constant analyzed as impedance ratio. α = Z₀/(2R_K)
exact identity. Impedance mismatch interpretation, length scale hierarchy,
running coupling, Wyler's formula. Numerical value NOT derived — requires
condensate microscopic structure (open in SVT itself).

Fine-structure constant stretch goal completed (structural analysis).
Part 6: Emergent GR simulation. Five independent numerical tests: 1/r
potential recovery (Thomas algorithm, 1.35% err), smooth curvature emergence
from N=10–1000 discrete oscillators (0.44% err), Kuramoto synchronization
(R: 0.329→1.000), two-body 1/d force law (exponent −0.984), weak-field
linearization validation (machine-precision match to |1−sin(x)/x|).
Runtime ~10s. All tests PASS.

Simulation stretch goal completed.
Part 7: Free photon gravity analysis. Quantitative assessment: solar
deficit ~10⁻²¹/s, thermal suppression ~10⁻¹⁴, trace anomaly ~0.04%.
Key insight: radiation dominates only when tightly coupled (pre-
recombination), and free-streams only when subdominant. Problem is
cosmological, not astrophysical. Plasma frequency effective mass as
possible pre-recombination coupling mechanism.

Free photon analysis completed.
Part 8: Radiation-era cosmology. Matter-era Friedmann equation derived
from condensate dynamics (Euler + continuity). Tight-coupling argument
resolves photon contribution (effective mass). Genuine gap: decoupled
neutrino kinetic energy at BBN (41% of ρ_total, 23% error in H).
Requires acoustic metric tensor channel for full resolution.

Radiation-era cosmology analysis completed.
Part 9: Newton's constant G derivation. Dimensional analysis gives
G = 𝒞 c^(5/2)/√(ℏρ₀), exact when ρ₀ = ρ_Planck. Coupling constants
gᵢ shown to be geometric (~4πRᵢ), not free parameters. Reduces N+2
apparent parameters to 1 unknown (𝒞). Energy-cost circularity resolved.
Full derivation requires condensate microphysics (deepest open problem).

G derivation completed (partial — one free parameter remains).
Part 10: Strong-field equivalence principle. Phase difference = compactness
parameter: δψ = GM/(Rc²). Nonlinearity sin(δψ)/δψ is 0.7% for NS, 4.1%
at BH horizon. Strong-field Nordtvedt η ~ Ξ²/6. Binding energy gravitates
correctly to O(Ξ). Acoustic horizon at r = 2GM/c² (exact). Tension with
double pulsar Ṗ_b at ~1% level — critical open question.

Strong-field EP analysis completed.
Part 11: Momentum balance for phase-gradient motion. Derived local force
density F^k_j = −gⱼ sin(ψⱼ−φ) ∂^k ψⱼ. Two worked examples: test particle
(field absorbs recoil) and two-body (field as intermediary). Newton's F=mg
recovered. "Reactionless drive" resolved: propellant-free but momentum-
conserving. Earth–Sun budget: field momentum ~10⁻⁸ of matter momenta.

Momentum balance completed.
Part 12: Condensate tetrad extension. Extended order parameter
Φ = √ρ₀ e^{iφ} e^a_μ. Palatini + phase-coupling Lagrangian. Four field
equations derived. Linearized analysis: 2 tensor modes (□h^TT = 0) +
1 massive breathing mode. E(2) class N₃. All Parts 1–11 preserved.
Symmetry breaking GL(4,R)×U(1) → SO(3,1). Frame-dragging, Kerr metric
recovered. GFT condensate as microscopic origin candidate.

Tetrad extension completed.
Part 13: Double pulsar tension resolution. The ~1.5% GW emission deficit
was an artifact of scalar-only PDTP. In extended PDTP (Part 12), dominant
GW emission is through tensor modes (Einstein equation → quadrupole formula
= GR). Global U(1) symmetry (φ→φ+c, ψ→ψ+c) guarantees scalar charge
α_A = 0 for all bodies → zero scalar radiation. Result: Ṗ_b^PDTP = Ṗ_b^GR
exactly. Spontaneous scalarization ruled out (β_A = 0). All binary pulsar
tests consistent.

Double pulsar tension resolved.
Part 14: Condensate microphysics analysis. 10 constraints compiled from
Parts 1–13. 5 candidate theories compared: GFT is best candidate (7/10).
GFT-PDTP dictionary constructed. Downstream blockage analysis: all
phenomenological predictions independent of microphysics (universality).
Three missing links for GFT derivation identified. Research roadmap
provided. Status: genuinely open — thorough analysis, no resolution claimed.

Condensate microphysics analysis completed.
Part 15: Neutrino BBN resolution via tetrad extension. The 41% neutrino
energy deficit at BBN was an artifact of scalar-only PDTP — the same
pattern as the double pulsar tension (Part 13). Extended PDTP (Part 12)
derives Einstein equation G_μν = 8πG T_μν, whose (0,0) component gives
the Friedmann equation with ALL energy density including ρ_ν. The tensor
sector uses T_00 (not the trace T = 0), so neutrinos contribute fully.
Result: H²_PDTP = H²_GR at all epochs. Two-sector cosmological structure:
tensor handles all energy-momentum, scalar provides phase-locking mechanism.

Neutrino BBN problem resolved.
Part 16: Hubble tension analysis. Developed quantitative model of
environment-dependent phase drift rate. Two mechanisms analyzed:
(1) direct scalar drift (1/ρ dependence) — Cassini bound ε_s < 10⁻⁵
makes this negligible; (2) backreaction from phase inhomogeneity —
σ²_δψ ~ 10⁻¹⁰, also negligible. Both mechanisms ~9 orders of magnitude
too small. Honest conclusion: PDTP cannot currently explain the 8% H₀
discrepancy. Deep connection identified between Hubble tension, dark
energy, and phase drift mechanism (common root in condensate coherence
evolution). Conditional predictions provided for future surveys.

Hubble tension analysis completed (genuinely open — no resolution claimed).

Part 17: Cosmological constant / dark energy analysis. Scalar sector
phase-filters vacuum fluctuations (⟨sin(ψ_vac − φ)⟩ = 0 for random phases).
ρ₀ vs ρ_Λ reframing: dark energy = condensate perturbation δρ₀/ρ₀ ~ 10⁻¹²³.
Phase drift → dynamical dark energy with w ≠ −1 (qualitatively consistent
with DESI DR2 4.2σ evidence for evolving dark energy). Tensor sector inherits
GR's full cosmological constant problem (G_μν = 8πG T_μν includes vacuum
energy). Honest conclusion: partial reframing with genuinely novel scalar
sector mechanism, but not a solution. Common root with Hubble tension
(Part 16) and phase drift mechanism — all require condensate microphysics.

Cosmological constant analysis completed (partial reframing — not solved).

Part 18: Aharonov-Bohm effect and PDTP phase structure — deep analysis.
COW experiment derivation: PDTP reproduces Δφ = (m/ℏ)∫Φdt exactly via
weak-field limit (consistency check, not new prediction). Overstreet et al.
(2022, Science) observed gravitational AB phase shift with atom interferometry
— strongest experimental support for PDTP's phase-centric paradigm. Fiber
bundle classification: PDTP = U(1)_global × SO(3,1) product bundle (trivial
scalar bundle for phase dynamics + GR frame bundle for spacetime geometry).
Topological defects: cosmic strings interpreted as quantized vortex lines
in condensate phase field (∮∇φ·dl = 2πn ↔ deficit angle Δθ = 8πGμ/c²).
EM–gravity parallel: both involve phase coupling, but gauging PDTP's U(1)
does NOT naturally produce electromagnetism (coupling constant mismatch,
charge structure incompatible). Impact assessment: no modifications to
previous Parts needed — geometric consistency confirmed. Speculative:
cosmological vortex networks could relate to phase drift (Part 17).

Aharonov-Bohm deep analysis completed (geometric consistency confirmed).

Part 19: Phase drift mechanism — deep analysis of why spacetime phase
de-synchronizes at cosmic scales. Four candidate mechanisms analyzed:
(1) finite coherence length ξ = c/√(2g) as primary mechanism — exponential
decay of phase correlations beyond ξ explains the ~100 Mpc transition;
(2) cosmological expansion stretches condensate wavelength, accumulating
frequency mismatch; (3) thermal fluctuations map to Landau two-fluid model
— dark energy as normal fraction (universe deep in superfluid phase,
T ≪ T_c); (4) topological defects via Kibble-Zurek mechanism — primordial
vortex networks set effective coherence scale. Key result: effective
Langevin equation δφ̈ + 3H(t)δφ̇ + g_eff(t)δφ = η(t) unifies all four
mechanisms. Qualitative w(z) matches DESI DR2 (w₀ > −1, w_a < 0) via
overdamped → resonant → relaxation dynamics. Honest conclusion: framework
analysis, not solution — quantitative predictions blocked by unknown
condensate microphysics (g, T_cond, n_vortex, γ_micro).

Phase drift mechanism analysis completed (framework established).

All formalization tasks (Parts 1–21) and stretch goals completed.

Part 20: Standard Model and PDTP particle-force mapping. Systematic side-by-side
comparison of all 17 SM particles and 4 forces with PDTP interpretations. Key
finding: PDTP adds gravity (phase-locking) while preserving the entire SM gauge
structure (SU(3)×SU(2)×U(1)) unchanged. Complete particle table with coupling
constant estimates. Combined Lagrangian L_total written. Higgs ↔ PDTP condensate
parallel identified. Mass hierarchy reframed as coupling hierarchy. Honest
conclusion: mapping is interpretive, not predictive — no new particle physics
predictions. Strategic assessment: confirms external review recommendation to
focus on microphysics as the keystone problem.

Part 21: Energy-Frequency-Vibration condensate microphysics (exploratory, isolated
from main PDTP). Tesla-inspired premise: universe = energy, frequency, vibration.
Built oscillator lattice Hamiltonian H = Σ(I/2)(∂ₜθ)² + (K/2)Σ(θᵢ−θⱼ)². Derived:
c² = κ/ρ (speed of light = stiffness/inertia), G = c²/(4πκ) (gravity = inverse
stiffness), M_eff = (ρ/3)∫(∇θ₀)²d³x (mass = phase distortion energy). Cosine
coupling derived from |Φ−Ψ|² symmetry breaking: g = 2λ√(ρσ). Lattice parameters
computed from known G: K ≈ 5.78 × 10⁻¹⁰ J. Constraint satisfaction: 5/10 (scalar
model limitation — tensor constraints require Part 12 extension). Honest conclusion:
framework for G derivation established, but true first-principles prediction requires
independent determination of lattice coupling K.

All formalization tasks (Parts 1–21) and stretch goals completed.
Open problems documented in "Open Problems (Future Work)" section:
- Cosmological: phase drift mechanism analyzed (Part 19) — framework established,
  quantitative predictions still require condensate microphysics
- Structural: vacuum energy tensor sector, temperature model, w(z) derivation,
  scalar-tensor backreaction (from external review of Part 17)
- Microphysics priority: EFV approach completed (Part 21), cosine coupling derived
  (plausibility), oscillator lattice built, mass-frequency derived. Remaining:
  phase stiffness κ from first principles (deepest gap), tensor lattice extension
- Topological: vortex dynamics in PDTP condensate, condensate phase transition

Part 25: Dark energy w(z) from phase drift dynamics. Derived CPL parametrization:
w_a = −(1−w₀²)/2 × (m + 3Ω_m) for g_eff ∝ a^m. DE-tracking coupling (m=3)
gives 0.4σ match to DESI DR2. Consistency line R = m + 3Ω_m is falsifiable.
Phantom bound w ≥ −1 is a hard constraint from canonical scalar.

Part 26: Free parameter m analysis. Derived self-consistency condition m = 6ε
(most robust internal prediction: m ≈ 0.57). Dynamical scaling gives m ≈ 2.
Honest finding: m = 3 was phenomenological curve-fitting, not a derivation.
The non-constant ε(a) integral is the most promising route to larger m values.

Part 27: Scalar vs tensor gravity analysis. Identified the single biggest gap
(breathing mode vs LIGO tensor modes) AND the path to closing it: the Part 21
oscillator lattice already has shear rigidity → supports transverse waves →
these are the tensor GW modes. Extracting all three lattice wave branches is
the highest-priority next task (Part 28).

CURRENT PRIORITY: Part 28 — derive tensor GW modes from oscillator lattice.
This is the most impactful task remaining: if successful, it closes PDTP's
biggest observational gap (GW polarization) using physics already present
in the framework (lattice shear rigidity from Part 21).
```

---

End of TODO

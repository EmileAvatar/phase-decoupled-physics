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

- [ ] **Coupling constant values (α_EM, α_W, α_S)**
  - The three coupling constants run with energy and unify near 10¹⁶ GeV (GUT scale)
  - PDTP predicts the group structure but not the coupling values
  - Strategy B (hierarchy ratio R = α_G/α_EM) is the existing path toward this

- [ ] **Z₃ phase positions → Koide formula → derive m_cond and G (HIGH PRIORITY)**
  - Key insight: Y-junction 120° (Part 37) and three-generation 120° spacing ARE THE SAME Z₃ geometry
    - Part 37: baryon Y-junction, force balance ê₁+ê₂+ê₃=0 → 120° in physical space
    - Three generations: Z₃ phase positions 0, 2π/3, 4π/3 in phase space
    - Same SU(3) Z₃ symmetry expressed at two levels simultaneously
  - Koide formula recast as Z₃ geometry (PDTP Original):
    - Koide: (√m_e + √m_μ + √m_τ)² = (3/2)(m_e + m_μ + m_τ) = 2/3 normalization
    - This is EXACTLY the identity for three equal-length vectors at 120°
    - √mᵢ are the natural Z₃ coordinates — amplitudes of vortex wavefunctions at each minimum
    - Y-junction force balance ê₁+ê₂+ê₃=0 = same identity — NOT a coincidence
  - Path to deriving m_cond without circularity:
    - Step 1: Z₃ positions (0, 2π/3, 4π/3) are FIXED by SU(3) topology — not free parameters
    - Step 2: If mass function m_i = f(Z₃ position, m_cond_QCD) is derivable from PDTP Lagrangian
    - Step 3: Koide formula = geometric constraint from Z₃ → reduces 3 mass free parameters to 1 (overall scale)
    - Step 4: Absolute scale m_e = 0.511 MeV fixes m_cond_QCD → m_cond_QCD ~ Λ_QCD (cross-check with Part 38)
    - Step 5: G = ħc/m_cond² — closes the derivation loop that Part 29 failed to close
  - Observable consequence: condensate oscillation frequency ω_gap = m_cond_QCD c²/ħ ~ 3×10²³ Hz
    - This is the QCD scale, not Planck scale — potentially accessible via heavy-ion signatures
  - What would make this a Part:
    - Derive mass function m_i = f(Z₃ position, m_cond) from the SU(3) PDTP coupling Re[Tr(Ψ†U)]/3
    - Show Koide formula follows from Z₃ geometry alone (no fitting)
    - Test whether m_e fixes m_cond_QCD ~ Λ_QCD (Sudoku check vs Part 38 result)
    - If chain closes: this is the non-circular G derivation; if not: identify where it breaks
  - Why this is higher priority than the radial modes path (Part 51):
    - Z₃ is already in the framework (Parts 36, 37) — not a new assumption
    - Koide is already verified to 0.0009% (Part 32, Part 51)
    - Y-junction is already derived (Part 37) — same geometry confirmed twice
    - Could reduce free parameter count from 6 to 4 (replacing m_e, m_μ, m_τ with one scale + Z₃ topology)

### Cosmological

- [ ] **Cosmological Constant via Forced Checklist Check**
  - Part 43: condensate T_μν^φ = 0 in vacuum (U(1) shift) — does NOT add to Λ ✓
  - But: matter-sector vacuum energy (quarks, leptons, Higgs zero-point) still unresolved
  - Observed: Λ_obs ~ 1.1×10⁻⁵² m⁻²; QFT predicts ~10¹²⁰ × Λ_obs (worst prediction in physics)
  - **Method: Forced Checklist Check** — go through ALL Methodology.md items one by one
  - Question: can any checklist path reduce or explain the Λ problem in PDTP?
  - Candidate paths not yet tried: topological argument (Λ from lattice winding?), order parameter (Λ as condensate gap?), analogy (BCS gap → Λ?), postulate-and-derive
  - **Candidate: Tachyon condensate as second spacetime layer (postulation)**
    - Postulate: a second condensate field φ_T exists, operating above c (FTL layer)
    - Normal matter does NOT phase-lock to φ_T (analogous to neutrinos not coupling to EM)
    - Tachyon particle: couples to φ_T, NOT to φ (the normal spacetime condensate); no violation of +cos rule
    - φ_T has its own condensate scale m_cond_T, its own coupling constant g_T, potentially different topology
    - Dispersion of φ_T sector: ω² = k²c² − m_cond_T²c⁴/ħ² (tachyonic, FTL group velocity v > c)
    - Condensation endpoint: ψ_T − φ_T rolls from 0 → π; α_T = cos(π) = −1 → repulsive + w = −1 (Λ-like)
    - Three-phase picture: FTL phase (v→∞) → rolling (v>c, α: +1→−1) → condensed (v→c⁺, w = −1 = Λ)
    - Candidate for dark matter: decoupled from φ (no normal gravity) + decoupled from EM → invisible ✓
    - Candidate for Λ: condensed φ_T sector contributes constant w=−1 term to Einstein eq
    - Precedent: Sen (2002) hep-th/0203265 — tachyon condensation in string theory → cosmological constant
    - Limits: m_cond_T undetermined; φ_T/φ coupling (if any) undetermined; two-layer architecture unverified
    - Status: postulation only — no Sudoku check yet; needs a Part number and full derivation to proceed

- [ ] **CP violation and baryogenesis**
  - PDTP Lagrangian is C, P, T invariant separately → no CP violation
  - Sakharov baryogenesis blocked — needs an extension to break CP

---

## Speculation (not part of PDTP — ideas to investigate)

These are unverified intuitions. No Sudoku check, no Part number, no derivation yet.
They are recorded here so they are not lost. Each needs a full plan and user approval before becoming a Part.

- [ ] **Multiple layers of spacetime / condensate**
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

- [ ] **Chirality from condensate refractive index — path to making handedness DERIVED not free**
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

- [ ] **Phase-gradient coil drum — proposed analog experiment**
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

- [ ] **Acoustic standing wave levitation — inverted as decoupling mechanism**
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

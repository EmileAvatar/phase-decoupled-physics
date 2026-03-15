# PDTP: What We Know, What We've Found, and What Remains

**Phase-Decoupled Transport Physics — Complete Findings Summary**

*For readers who know some physics but are new to PDTP.
No prior knowledge of the framework required.*

*Last updated: 2026-03-15 (Parts 1-62)*

---

## 1. The Core Idea (One Paragraph)

Everything in the universe is a wave. Electrons, protons, atoms — each one
vibrates at its own precise frequency, determined by its mass. Spacetime itself
also vibrates — it is not a passive stage but a medium, like an ocean. **Gravity,
in this picture, is what happens when a matter-wave and a spacetime-wave lock
their rhythms together.** Locked rhythms pull toward each other. A rhythm mismatch
weakens the pull. If the two waves go completely out of step (90 degrees out of
phase), the gravitational coupling drops to zero — this is the "phase decoupled"
state the framework is named after.

---

## 2. The Core Equations

### U(1) Lagrangian (single-phase, gravitational condensate)

```
L = (1/2)(d_mu phi)(d^mu phi) + Sum_i (1/2)(d_mu psi_i)(d^mu psi_i) + Sum_i g_i cos(psi_i - phi)
```

- phi = spacetime condensate phase (the "medium")
- psi_i = matter-wave phase of particle i
- g_i = coupling constant (proportional to particle mass)
- The **+cos** sign is required for stable phase-locking (attractive gravity)

**Field equations** (derived via Euler-Lagrange):
```
box(phi) = Sum_i g_i sin(psi_i - phi)        [spacetime responds to matter]
box(psi_j) = -g_j sin(psi_j - phi)           [matter responds to spacetime]
```

### Two-Phase Lagrangian (Part 61)

```
L = +g cos(psi - phi_b) - g cos(psi - phi_s)
```

- phi_b = bulk phase (+cos, attractive = gravity)
- phi_s = surface phase (-cos, repulsive = surface tension)
- phi_+ = (phi_b + phi_s)/2 = gravity mode
- phi_- = (phi_b - phi_s)/2 = NEW surface mode

### SU(3) Extension (Part 37)

```
L = K Tr[(d_mu U^dag)(d^mu U)] + Sum_i K_i Tr[(d_mu Psi_i^dag)(d^mu Psi_i)]
    + Sum_i g_i Re[Tr(Psi_i^dag U)] / 3
```

- U(x) in SU(3) = spacetime condensate (3x3 unitary matrix)
- Re[Tr(Psi^dag U)]/N is the Wilson loop action (Wilson 1974)
- U(1) limit: Re[Tr(Psi^dag U)]/1 = cos(psi - phi) (recovers single-phase exactly)

---

## 3. Established Results (Mathematically Proven)

These results are derived rigorously from the PDTP equations and verified
numerically. Each is tagged [DERIVED] and [VERIFIED].

### 3.1 Core GR Recovery (Parts 1-15)

| Result | Status | Evidence |
|--------|--------|----------|
| Newtonian 1/r potential | EXACT | Simulation: emergent_gr_simulation.py |
| General relativity (PPN: gamma=1, beta=1) | EXACT | hard_problems.md |
| Hawking temperature T_H = hbar*c^3/(8*pi*G*M*k_B) | EXACT | hawking_radiation_pdtp.md |
| Double pulsar orbital decay | EXACT (0.013%) | double_pulsar_resolution.md |
| BBN / Friedmann equation all epochs | EXACT | radiation_era_cosmology.md |
| GW tensor modes propagate at c | EXACT | Lorentz invariance by construction |
| E(2) class N_3: 2 tensor + 1 breathing | DERIVED | tetrad_extension.md |

### 3.2 Particle Physics Structure (Parts 20-27, 37-41, 49-53)

| Result | Status | Evidence |
|--------|--------|----------|
| Koide formula Q = 2/3 from Z_3 phase geometry | EXACT | koide_derivation.md |
| delta = sqrt(2) from equal partition | DERIVED | koide_z3.py (Part 53) |
| 8 gluons from N^2-1 = 8 SU(3) generators | EXACT | su3_condensate.py |
| Z_3 fractional vortices = quarks | DERIVED | su3_condensate_extension.md |
| Vortex winding number n = m_cond/m | DERIVED | vortex_winding.py (Part 33) |
| G = hbar*c/m_cond^2 (G-free given m_cond) | DERIVED | vortex_winding.py |
| c_s = c exactly (speed of sound = speed of light) | EXACT | condensate_selfconsist.py (Part 34) |
| kappa_GL = sqrt(2) (Type II superconductor) | DERIVED | Part 36 |
| Chirality = Z_2 vortex winding direction | DERIVED | chirality_parity.py (Part 50) |
| Maximal parity violation A=-1 automatic | DERIVED | Part 50 |
| 3 generations = 3 radial vortex modes (n_r=0,1,2) | DERIVED | three_generations.py (Part 51) |
| Lepton universality (all generations couple same to W/Z) | DERIVED | Part 51 |
| Beta functions b_0 from group theory (QCD, SU(2), QED) | EXACT | coupling_constants.py (Part 52) |
| W/Z mass ratio from custodial SU(2) symmetry | EXACT | wz_boson_masses.py (Part 49) |

### 3.3 QCD Lattice (Parts 37-41)

| Result | Status | Evidence |
|--------|--------|----------|
| SU(3) Casimir factor C_2(fund) = 4/3 | EXACT (textbook) | su3_condensate.py |
| String tension sigma_SC = 0.173 GeV^2 (4% off QCD 0.18) | DERIVED | su3_lattice.py (Part 38) |
| 4D lattice confirms 2D at leading order | VERIFIED | su3_lattice_4d.py (Part 39) |
| Sea quarks REDUCE sigma (by ~6%) | DERIVED | su3_fermion.py (Part 40) |
| Quenched result is the correct comparison | DERIVED | Part 40 |

### 3.4 Two-Phase System (Parts 61-62)

| Result | Status | Evidence |
|--------|--------|----------|
| 3 coupled EL equations (SymPy verified) | DERIVED | two_phase_lagrangian.py |
| Product coupling: 2g*sin(psi-phi_+)*sin(phi_-) | DERIVED | trig identity, verified |
| Newton's 3rd law: psi_ddot = -phi_+_ddot | EXACT | Lagrangian symmetry |
| Jeans instability (eigenvalue +2*sqrt(2)*g > 0) | DERIVED | eigenvalue analysis |
| Biharmonic gravity: nabla^4(Phi) + 4g^2*Phi = source | DERIVED | weak-field limit |
| phi_- massless in vacuum, massive near matter | DERIVED | reversed_higgs.py |
| phi_- equilibrium at pi/2 (not 0) near matter | DERIVED, CORRECTED | Part 62 |
| G_eff = 2*G_bare at equilibrium | DERIVED | Part 62 |

### 3.5 Black Holes (Parts 20, 24, 45-47)

| Result | Status | Evidence |
|--------|--------|----------|
| BH singularity replaced by vortex core (xi = l_P/sqrt(2)) | DERIVED | bh_topological_defect.py |
| Penrose theorem evaded by lattice (condition 4 broken) | DERIVED | Part 45 |
| Winding number W = information carrier | DERIVED | hawking_info_paradox.py |
| Topology protects information (Mermin 1979) | DERIVED | Part 46 |
| Complete evaporation (no remnant) | DERIVED | bh_evaporation_endpoint.py |
| Endpoint: S < 1 bit, t_evap ~ T_P | DERIVED | Part 47 |

---

## 4. Negative Results (Tried and Failed)

These are equally important — they define the boundaries of what PDTP can explain.

### 4.1 The Central Open Problem: m_cond Is Underdetermined

**G = hbar*c/m_cond^2 is exact, but m_cond = m_P cannot be derived.**

This has been proven through exhaustive testing:

| Approach | Part | Result | Why it fails |
|----------|------|--------|-------------|
| Substitution chains (8 algebraic paths) | 29 | ALL CIRCULAR | 1 equation, 2 unknowns |
| Power-law sweep (729 combinations) | 29 | Best: 1.31x off | Still uses l_P (contains G) |
| Mass-combo sweep (all pairs/triplets) | 29 | ALL FAIL | Hierarchy gap = (m_P/m)^2 |
| Analytical proof | 29 | PROVEN CIRCULAR | Constraint eq always forces a = l_P |
| Condensate self-consistency | 34 | DOES NOT FIX m_cond | c_s=c is tautological identity |
| Dimensional transmutation (1-loop RG) | 35 | NEGATIVE | beta(K)>0 (IR free, not QCD-like) |
| Five fresh reframes (Ideas 1-5) | 44 | ALL NEGATIVE | Integer winding, mode counting, time dilation, stability, K_0 coincidence |

**Conclusion:** m_cond is a FREE PARAMETER of PDTP, analogous to Lambda in GR.
All perturbative paths are exhausted (Parts 29-35).

### 4.2 Coupling Constants Are Free Parameters

| Constant | Part | Result |
|----------|------|--------|
| alpha_EM = 1/137 | 52 | Free parameter (structure derived, value not) |
| sin^2(theta_W) = 0.231 | 48 | Free parameter (ratio of SU(2)/U(1)_Y stiffnesses) |
| v_EW = 246 GeV | 49 | Free parameter (3rd condensate scale) |
| theta_0 = 2/9 (Koide) | 53 | Free parameter (no SU(3) derivation) |
| RG running of K_0 | 56 | Does NOT give 1/137 (wrong direction) |
| Dispersion coupling | 57 | FAILS (3/10 pass; quantum not classical) |

### 4.3 Other Negative Results

| Topic | Part | Key finding |
|-------|------|-------------|
| Hubble tension | 16 | Both mechanisms ~9 orders too small |
| Lambda problem | 17, 54 | Lambda is a SECOND free parameter alongside G |
| CP violation | 22 | PDTP Lagrangian is C,P,T invariant; Sakharov baryogenesis blocked |
| Composite G from layers | 60 | All 3 models reorganise hierarchy, don't solve it |
| BEC Bogoliubov for Lambda | 54 | Invalid (n*a_s^3 ~ 1, not dilute) |

---

## 5. Speculative Results (Interpretation Beyond Math)

These are consistent with the math but not uniquely implied by it.
Clearly marked [SPECULATIVE].

| Claim | Part | Status | What's missing |
|-------|------|--------|---------------|
| Gravity = emergent phase-locking | 1 | SPECULATIVE | No experiment yet; math is consistent |
| Particle = vortex in condensate | 33 | SPECULATIVE | Works mathematically; physical condensate unknown |
| Dark energy = phase drift | 19, 25 | SPECULATIVE | Qualitatively matches DESI; quantitative params unknown |
| BH core = vortex core | 45 | SPECULATIVE | Penrose evasion rigorous; core structure assumed |
| 4 forces from homotopy of one medium | 58 | SPECULATIVE | Structure correct; coupling values not derived |
| Two-channel coupling (amplitude+topology) | 55 | SPECULATIVE | Mass-independence derived; alpha value not |
| Strider model (particles float on gravity) | 59 | SPECULATIVE | Correct mass dependence; Delta not derived |
| phi_- = environment-dependent mass scalar | 62 | SPECULATIVE | Math rigorous; experimental test proposed |

---

## 6. Free Parameters

PDTP has the following undetermined quantities:

| Parameter | What it controls | Status |
|-----------|-----------------|--------|
| m_cond (= m_P) | Newton's constant G = hbar*c/m_cond^2 | FREE — all perturbative paths exhausted |
| Lambda | Cosmological constant | FREE — second parameter alongside G |
| alpha_EM | Electromagnetic coupling | FREE — structure derived, value not |
| sin^2(theta_W) | Weak mixing angle | FREE — ratio of condensate stiffnesses |
| v_EW = 246 GeV | Electroweak condensate scale | FREE — 3rd condensate mass |
| theta_0 = 2/9 | Koide formula angular parameter | FREE — no SU(3) derivation |
| CKM/PMNS matrices | Quark/lepton mixing | FREE — (N-1)^2 = 4 parameters each |

**Note:** The Standard Model also cannot derive these values. PDTP explains their
*structure* (why they exist, what determines their form) but not their *values*.

---

## 7. Key Structural Insights

These are the most important conceptual results from 62 parts of work:

1. **Circularity is algebraically inevitable** (Part 29): No algebra, no matter how
   clever, can derive G from non-gravitational measurements. You need an independent
   measurement (like Cavendish 1798 for Newton's G).

2. **Strategy A = Strategy B** (Part 33): The breathing mode frequency (omega_gap)
   and the vortex winding number (n) both reduce to the same unknown: m_cond.

3. **c_s = c exactly** (Part 34): The speed of sound in the PDTP condensate equals
   the speed of light, for any m_cond. This is not an approximation.

4. **Type II superconductor** (Part 36): kappa_GL = sqrt(2), which means Abrikosov
   flux tubes form naturally. This gives confinement (linear potential between quarks).

5. **Force structure from topology** (Parts 55-58): Gravity couples to continuous
   phase gradients (mass-dependent). EM couples to discrete winding numbers
   (mass-independent, quantized). This explains why alpha_G depends on mass but
   alpha_EM does not.

6. **Two-phase system produces Jeans instability** (Part 61): The +cos/-cos
   Lagrangian automatically has an unstable eigenmode — gravitational collapse
   emerges directly from the Lagrangian without additional assumptions.

7. **Reversed Higgs mechanism** (Part 62): phi_- is massless in vacuum but gains
   mass near matter. This is the opposite of the standard Higgs (where the field
   gains mass in vacuum via VEV). Distinguishable from chameleon fields via hollow
   shell experiment.

---

## 8. Falsifiable Predictions

See [falsifiable_predictions.md](../research/falsifiable_predictions.md) for full
details. Summary:

### Currently Testable (2025-2030)

| # | Prediction | Test | Status |
|---|-----------|------|--------|
| 5 | w(z) != -1 (dark energy has dynamics) | DESI, Euclid, Rubin | Hints of w_0 > -1 (2-3 sigma) |
| 4 | Screened fifth force at sub-mm range | Torsion balance, atom interferometry | No detection (consistent if m_b > 4 meV) |

### Near-Future (2030-2040)

| # | Prediction | Test | Status |
|---|-----------|------|--------|
| 1 | Massive breathing mode GW | Einstein Telescope, LISA (triangular detectors) | Not yet detectable |
| 3 | Phase-dependent gravity (BEC vs thermal) | BEC atom interferometry | No experiment designed |

### Requires New Physics

| # | Prediction | Test | Status |
|---|-----------|------|--------|
| 2 | GW birefringence | Multi-messenger timing | Requires breathing mode detection first |
| 6 | Planck-scale dispersion | Gamma-ray burst timing | Current bounds consistent |

### New Predictions (Parts 61-62, not yet in predictions doc)

| # | Prediction | Test | Distinguishes from |
|---|-----------|------|-------------------|
| 7 | phi_- massive near matter, massless in vacuum | Lab: sub-mm force modification | Chameleon (couples to density, not potential) |
| 8 | Hollow shell: phi_- massive inside (Phi>0) | Torsion balance inside lead shell | Chameleon is massless inside shell |
| 9 | G_eff = 2*G_bare (factor hidden in measurement) | Precision gravity at varying Phi | Standard GR (G is constant) |
| 10 | phi_- oscillation frequency depends on local Phi | Resonant cavity near massive object | No GR analogue |

---

## 9. Project Structure

### Three Condensate Layers

PDTP identifies three condensate layers with identical Lagrangian structure:

| Layer | Scale | Gauge group | What it explains |
|-------|-------|-------------|-----------------|
| Gravitational | m_P ~ 10^19 GeV | U(1) | Gravity, spacetime structure |
| QCD | Lambda_QCD ~ 200 MeV | SU(3) | Strong force, confinement |
| Electroweak | v ~ 246 GeV | SU(2) x U(1)_Y | Weak force, W/Z masses, Higgs |

### Strategies Forward

| Strategy | Method | Status |
|----------|--------|--------|
| A: Measure omega_gap | LISA/ET breathing mode detection | Required freq ~10^43 Hz (Planck) — out of reach |
| B: Derive n from topology | Hierarchy ratio R = alpha_G/alpha_EM | All 5 approaches failed (Part 44) |
| C: Non-perturbative lattice | GPU SU(3) at beta=6.0, N>=16 | Next task (Part 42) |
| D: Postulate K | Accept m_cond as free parameter | Current status (like Lambda in GR) |

---

## 10. Glossary (Quick Reference)

| Term | Plain English meaning |
|------|-----------------------|
| Lagrangian (L) | Energy accounting formula; the master equation |
| Phase (phi, psi) | Current position in an oscillation cycle |
| Phase-locking | Two oscillators matching rhythms — the PDTP mechanism for gravity |
| Compton wavelength | How "big" a particle is as a wave: lambda = hbar/(mc) |
| Compton frequency | How fast a particle oscillates: omega = mc^2/hbar |
| Vortex winding number (n) | How many times the phase winds around a particle core |
| Koide formula | Mass pattern: Q = 2/3 among electron/muon/tau |
| Hierarchy problem | Why is gravity 10^37x weaker than electromagnetism? |
| Breathing mode | Third GW polarization (isotropic expansion/contraction) |
| Coupling constant (g) | How strongly two things interact |
| Phase decoupling | When psi - phi -> 90 degrees, cos -> 0 and gravity turns off |
| m_cond | Condensate mass (= Planck mass); the central free parameter |
| phi_+ | Gravity mode (average of bulk and surface phases) |
| phi_- | Surface mode (difference of bulk and surface phases); new scalar field |
| Sudoku check | Test a new equation against 10+ known physics equations for consistency |

---

*For full mathematical derivations, see [mathematical_formalization.md](../research/mathematical_formalization.md).*
*For the active roadmap, see [TODO_02.md](../../TODO_02.md). For completed work summary, see [TODO_Summary.md](../../TODO_Summary.md).*
*For falsifiable predictions, see [falsifiable_predictions.md](../research/falsifiable_predictions.md).*
*For coding standards, see [CODING_STANDARDS.md](../../CODING_STANDARDS.md).*

# PDTP Equation Reference — Central Registry

**Purpose:** Single source of truth for all PDTP equations. Copy-pasteable for external review.
Update this file whenever a new equation is derived or status changes.

**Status tags:** `[ASSUMED]` `[DERIVED]` `[VERIFIED]` `[PDTP Original]` `[CONSISTENCY RELATION]` `[ANSATZ]` `[CANDIDATE]` `[REJECTED]` `[SPECULATIVE]` `[NEGATIVE]`

---

## 1. Core Lagrangians

### 1a. U(1) Single-Phase Lagrangian [ASSUMED]
```
L = (1/2)(d_mu phi)(d^mu phi) + Sum_i (1/2)(d_mu psi_i)(d^mu psi_i) + Sum_i g_i cos(psi_i - phi)
```
- Field equation: Box(phi) = Sum_i g_i sin(psi_i - phi) [DERIVED]
- Matter equation: Box(psi_j) = -g_j sin(psi_j - phi) [DERIVED]
- Coupling: alpha = cos(psi - phi), alpha=1 normal gravity, alpha->0 decoupled
- Sign: +cos required for stability (verified Part 1)
- **Source:** Parts 1-11

### 1b. Two-Phase Lagrangian [PDTP Original, DERIVED] (Part 61)
```
L = +g cos(psi - phi_b) - g cos(psi - phi_s)
```
- phi_b = bulk phase (+cos, gravity); phi_s = surface phase (-cos, surface tension)
- Change of variables: phi_+ = (phi_b + phi_s)/2; phi_- = (phi_b - phi_s)/2
- Product coupling: cos(psi-phi_b) - cos(psi-phi_s) = 2 sin(psi-phi_+) sin(phi_-)
- **STATUS:** 16/16 re-derivation tests PASS (Part 63)
- **Source:** Part 61, verified Part 63

### 1c. SU(3) Extension [PDTP Original] (Part 37)
```
L = K Tr[(d_mu U^dag)(d^mu U)] + Sum_i K_i Tr[(d_mu Psi_i^dag)(d^mu Psi_i)] + Sum_i g_i Re[Tr(Psi_i^dag U)] / 3
```
- U(x) in SU(3) -- spacetime condensate; Psi_i(x) in SU(3) -- matter fields
- U(1) limit: Re[Tr(Psi^dag U)]/1 = cos(psi-phi) [EXACT recovery]
- Wilson loop action (Wilson 1974)
- **Source:** Part 37, `su3_condensate_extension.md`

---

## 2. Gravitational Equations

### 2a. Newton's Constant [PDTP Original, DERIVED] (Part 33)
```
G = hbar * c / m_cond^2
```
- G-free given m_cond; topological, coupling-independent
- m_cond = m_P gives G_known exactly (but m_P not derived)
- **Source:** Part 33, vortex winding derivation

### 2b. Lattice Spacing [PDTP Original, DERIVED]
```
a_0 = hbar / (m_cond * c)
```
- = Compton wavelength of condensate particle
- For m_cond = m_P: a_0 = l_P (Planck length)
- **Source:** Parts 29, 33

### 2c. G from Lattice [DERIVED]
```
G_pred = c^3 * a_0^2 / hbar
```
- Equivalent to 2a via substitution of a_0
- **Source:** Part 29, solver Phase 1-6

### 2d. Newton's 3rd Law [PDTP Original, DERIVED] (Part 61)
```
psi_ddot = -2 * phi_+_ddot
```
- Factor 2 exact (not 1); consistent with G_eff = 2*G_bare
- From two-phase Lagrangian symmetry
- **Source:** Part 61, verified Part 63

### 2e. Biharmonic Gravity [PDTP Original, DERIVED] (Part 61)
```
nabla^4 Phi + 4g^2 Phi = source
```
- 4th order (not Poisson); from eliminating phi_- in two-phase system
- 4g^2 = 1.376e+87 rad^2/s^2
- **Source:** Part 61

### 2f. Jeans Instability Eigenvalue [PDTP Original, DERIVED]
```
Coupled ODE system [A1: spatially uniform, k=0 limit]:
  d^2/dt^2 [Phi, phi_-] = M [Phi, phi_-]
Matrix: M = [[0, 4g], [2g, 0]]
Characteristic equation: lambda^2 - 8g^2 = 0
Eigenvalues: lambda = +/- 2*sqrt(2)*g
```
- **lambda is a growth-rate parameter, NOT a frequency (omega^2).**
- The trial solution is x ~ exp(sigma*t) where sigma^2 = lambda:
  - lambda > 0: sigma real => exponential growth (UNSTABLE = Jeans instability)
  - lambda < 0: sigma imaginary => oscillation with omega = sqrt(|lambda|)
- lambda_1 = +2*sqrt(2)*g > 0: gravitational collapse from Lagrangian (not assumed)
- lambda_2 = -2*sqrt(2)*g < 0: oscillation (breathing mode) with omega = (2*sqrt(2)*g)^(1/2)
- **Note:** The PDE version (Section 6b) gives omega^2 = c^2*k^2 +/- 2*sqrt(2)*g.
  The ODE eigenvalue is the k=0 limit of that dispersion relation.
- **Source:** Part 61; see `two_phase_lagrangian.py` Step 3 for full derivation

---

## 3. Vortex & Topological Equations

### 3a. Winding Number [PDTP Original, DERIVED] (Part 33)
```
n = m_cond / m_particle
```
- From core condition: v_s(r_core) = c
- Particle = vortex line; phi(r,theta) = n*theta
- G-free chain: m_cond -> n -> a_0 -> G
- **Source:** Part 33, `vortex_winding_derivation.md`

### 3b. Healing Length [DERIVED]
```
xi = a_0 / sqrt(2) = l_P / sqrt(2) ~ 1.143e-35 m
```
- Vortex core size; replaces r=0 singularity in BH
- **Source:** Parts 33-34, Part 45

### 3c. GL Parameter [PDTP Original, DERIVED]
```
kappa_GL = sqrt(2)
```
- Type II superconductor -> Abrikosov flux tubes form
- Universal for any m_cond
- **Source:** Part 36

### 3d. Y-Junction Geometry [PDTP Original, EXACT]
```
e_1 + e_2 + e_3 = 0 (120 degree angles)
```
- Three Z_3 vortices at Steiner point
- Baryon = Y-junction of three quarks
- **Source:** Part 37

---

## 4. Condensate & BEC Equations

### 4a. GP Interaction Constant [PDTP Original, DERIVED] (Part 34)
```
g_GP = hbar^3 / (m_cond^2 * c)
```
- Units: J*m^3; from mu = g_GP * n = m_cond * c^2
- **Source:** Part 34, `condensate_selfconsist.py`

### 4b. Speed of Sound [PDTP Original, DERIVED] (Part 34)
```
c_s = sqrt(g_GP * n / m_cond) = c   (EXACTLY, any m_cond)
```
- PDTP condensate always at sonic limit
- Key result: cubic equation reduces to c_s = c tautology
- Does NOT fix m_cond
- **Source:** Part 34

### 4c. Chemical Potential [DERIVED]
```
mu = g_GP * n = m_cond * c^2
```
- **Source:** Part 34

### 4d. Number Density [DERIVED]
```
n = (m_cond * c / hbar)^3
```
- Units: m^-3, G-free
- **Source:** Part 34

### 4e. Lagrangian Coupling [PDTP Original]
```
g_PDTP = m_cond * c^2 / hbar
```
- Units: rad/s (angular frequency, NOT GP interaction constant)
- **Source:** Part 34

---

## 5. QCD / String Tension

### 5a. U(1) String Tension [PDTP Original]
```
sigma_U1 = hbar / (8*pi*c)
```
- sigma ~ m_cond^2; value ~0.04 GeV^2 (factor 4.5 from QCD 0.18)
- **Source:** Part 36

### 5b. SU(3) Casimir Enhancement [PDTP Original, DERIVED]
```
sigma_SU3 = (4/3) * sigma_U1
```
- C_2(fund) = 4/3; result ~0.053 GeV^2 (factor 3.4 from QCD)
- **Source:** Part 37

### 5c. Strong Coupling Formula [DERIVED] (Part 38)
```
sigma_lat = ln(2*N/beta) * (hbar*c/a_0)^2
```
- At K_NAT = 1/(4*pi): sigma = 0.1729 GeV^2 (4% off QCD 0.18)
- Source: Creutz (1980) Phys.Rev.D 21
- Confirmed in 4D (Part 39): identical at leading order
- **Source:** Parts 38-39

### 5d. Dimensionless Coupling [PDTP Original]
```
K_NAT = 1/(4*pi) ~ 0.0796
```
- K = hbar/(4*pi*c) in SI; K_0 = 1/(4*pi) in natural units
- **Source:** Part 35

### 5e. Inferred QCD Condensate Mass [PDTP Original]
```
m_cond_QCD ~ 367 MeV (from sigma fit)
```
- Factor 1.8 from Lambda_QCD = 200 MeV
- **Source:** Part 37

---

## 6. Dispersion Relations

### 6a. Breathing Mode [DERIVED]
```
omega^2 = c^2 * k^2 + omega_gap^2
```
- omega_gap = m_cond * c^2 / hbar (Planck frequency for m_cond = m_P)
- Massive scalar GW with threshold
- **Source:** Parts 7, 33

### 6b. Two-Phase Branches [PDTP Original, DERIVED] (Part 61)
```
omega^2 = c^2 * k^2 +/- 2*sqrt(2)*g
```
- Branch A (+): gapped breathing mode (always stable)
- Branch B (-): Jeans unstable mode at k < k_J (gravitational collapse)
- These are omega^2 (frequency squared), NOT eigenvalues of the ODE matrix M.
  The ODE eigenvalue lambda = +/- 2*sqrt(2)*g (Section 2f) is the k=0 limit.
- **Source:** Part 61

### 6c. phi_- Reversed Higgs Mass [PDTP Original, DERIVED] (Part 62)
```
m_phi_minus^2 = 2*g*Phi   (near matter)
m_phi_minus^2 = 0          (in vacuum)
```
- Opposite of Higgs: massless in vacuum, massive near sources
- **Source:** Part 62, `reversed_higgs.py`

---

## 7. Cosmological Constant

### 7a. Dark Energy Fraction [CONSISTENCY RELATION] (Part 68)
```
Omega_beat = 2/3
```
- rho_beat = c^2 / (4*pi*G*L_H^2) = (2/3)*rho_crit
- Uses G and H_0 as inputs; NOT a prediction
- Observed Omega_Lambda = 0.685 (2.6% discrepancy)
- **Source:** Part 68, `cosmo_constant_v2.py`

### 7b. CKN Bound [DERIVED]
```
rho_CKN = c^2 / (G * L_H^2) = 7.1e-26 kg/m^3
```
- Factor 12 above rho_Lambda; consistent with geometric mean
- L_H is NOT a PDTP parameter (cosmological input)
- **Source:** Part 54

### 7c. Planck Energy Density [VERIFIED]
```
rho_Planck = c^5 / (hbar * G^2) ~ 10^96 kg/m^3
```
- Note: c^5 not c^7 (corrected Part 54)
- **Source:** Standard

### 7d. phi_- ZPE [DERIVED] (Part 68)
```
rho_phi_minus_ZPE ~ rho_Planck ~ 10^122 * rho_Lambda
```
- CC problem NOT solved by two-phase structure alone
- phi_- is correct DOF but mechanism unproven
- **Source:** Part 68

### 7e. phi_- as Dark Energy [CANDIDATE]
```
phi_- field: NOT shift-protected, Goldstone-like, massless in vacuum
```
- Correct DOF for dark energy; occupation mechanism unproven
- "One quantum per Hubble mode" is [ANSATZ] (not derived)
- **Source:** Part 68

---

## 8. Koide Formula

### 8a. Q Parameter [VERIFIED, DERIVED from Z_3] (Part 53)
```
Q = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3
```
- Z_3 center structure of SU(3) -> Q = 2/3
- **Source:** Part 4, Part 53

### 8b. Delta Parameter [PDTP Original, DERIVED]
```
delta = sqrt(2)
```
- From equal partition (45 deg, |v_par|^2 = |v_perp|^2)
- Reduces free params: 3 lepton masses -> 2 (M_0, theta_0)
- **Source:** Part 53

### 8c. Mass Scale [DERIVED]
```
M_0 = 313.84 MeV ~ m_p/3 (0.3%) ~ m_cond_QCD/0.86
```
- theta_0 = 2/9 underdetermined (no SU(3) derivation)
- **Source:** Part 53

---

## 9. Hawking & Black Holes

### 9a. Hawking Temperature [DERIVED]
```
T_H = hbar * c^3 / (8*pi*G*M*k_B)
```
- From acoustic horizon in PDTP condensate
- Exact match with standard result
- Preserved in two-phase framework
- **Source:** Part 24

### 9b. BH Core (Vortex) [PDTP Original, DERIVED] (Part 45)
```
r_core = xi = l_P / sqrt(2)
```
- Replaces r=0 singularity; Penrose theorem evaded by lattice
- **Source:** Part 45

### 9c. Evaporation Endpoint [PDTP Original, DERIVED] (Part 47)
```
r_s_final = l_P / (4*pi)
S_BH/k_B = 1/(16*pi) < 1 bit
t_evap ~ (10/pi^2) * T_Planck ~ 1 Planck time
E_final / (M_evap * c^2) = 8*pi
```
- Complete evaporation; information preserved by winding topology
- **Source:** Part 47

---

## 10. Chirality & Generations

### 10a. Effective Mass (Chirality) [DERIVED] (Part 65)
```
m_eff = v * Delta_w
```
- Co-winding (+1/2): m_eff = 0 (massless, propagates freely)
- Counter-winding (-1/2): m_eff = v = 246 GeV (confined)
- **Source:** Part 65, `chirality_refractive_index.md`

### 10b. Refractive Index [DERIVED] (Part 65)
```
n_eff = E / sqrt(E^2 - m_eff^2)
```
- Confinement range: lambda = 1/v ~ 0.0008 fm
- High E: n_eff -> 1 (parity restoration)
- **Source:** Part 65

### 10c. Three Generations [PDTP Original, DERIVED] (Part 51)
```
Radial vortex modes: n_r = 0, 1, 2
```
- Three generations from radial excitations of vortex
- Lepton universality derived (same coupling to all n_r)
- **Source:** Part 51

### 10d. Z_2 Chirality [PDTP Original, DERIVED] (Part 50)
```
Chirality = Z_2 vortex winding (+1/2 or -1/2)
```
- Maximal parity violation A = -1 automatic
- Vacuum choice selects handedness
- **Source:** Part 50

---

## 11. Coupling Constants & Running

### 11a. Beta Function (PDTP) [DERIVED, NEGATIVE] (Part 35)
```
beta(K) = +K^2 / (8*pi^2)
```
- Positive sign = IR free (NOT asymptotically free like QCD)
- K changes only 5.5% over 22 decades (m_e to m_P)
- **Source:** Part 35

### 11b. Landau Pole [DERIVED]
```
E_Landau = E_ref * exp(32*pi^3) ~ 10^431 * E_ref
```
- Far above Planck scale; irrelevant
- **Source:** Part 35

### 11c. Hierarchy Ratio [PDTP Original]
```
R = alpha_G / alpha_EM = 1 / (n^2 * alpha_EM)
```
- n = m_P/m (winding number)
- **Source:** Part 44

### 11d. Gravitational Fine Structure [VERIFIED]
```
alpha_G = G * m_p^2 / (hbar * c) ~ 5.9e-39
```
- **Source:** Standard; Part 44

---

## 12. Temperature & Statistical (Part 64)

### 12a. Exchange Energy [DERIVED]
```
J = E_Planck / (4*pi)
```
- **Source:** Part 64

### 12b. Critical Temperature [DERIVED]
```
T_c^MF = 3*J/k_B = 3*T_Planck/(4*pi)    (mean field)
T_c^MC = 2.202*J/k_B                      (Monte Carlo, Gottlob & Hasenbusch 1993)
T_KT  = pi*J/(2*k_B) = T_Planck/8        (Kosterlitz-Thouless)
```
- **Source:** Part 64

### 12c. Temperature-Dependent Coupling [DERIVED]
```
alpha(T) = exp(-k_B*T / (6*J))
```
- From spin-wave theory
- **Source:** Part 64

---

## 12b. Scale Selection (Part 69) [NEGATIVE]

### 12b-a. phi_- EOM (cosine-Gordon) [PDTP Original, DERIVED]
```
phi_-_tt - c^2*nabla^2(phi_-) = 2*g*sin(delta)*cos(phi_-)
```
- delta = psi - phi_+ (matter-gravity mismatch)
- Shift chi = phi_- - pi/2 maps to standard sine-Gordon [SymPy verified]
- In vacuum (delta=0): free wave, NO scale selection
- **Source:** Part 69

### 12b-b. Coupled delta-phi_- System [PDTP Original, DERIVED]
```
delta_tt - c^2*nabla^2(delta) = -2g*sin(delta - phi_-)
```
- delta = psi - phi_+ is a derived variable (not Lagrangian coordinate)
- SymPy verified
- **Source:** Part 69

### 12b-c. Kink Width [DERIVED]
```
L_kink = c / sqrt(2g) = 2^(1/4) * l_P ~ 1.19 * l_P
```
- All internal PDTP scales within factor 10 of l_P
- L_H / l_P = 8.49e60 (the hierarchy)
- sin(delta) for L_kink = L_H: ~10^-122 (= CC problem)
- **Source:** Part 69

### 12b-d. Dark Energy Mass Scale [DERIVED]
```
m_DE = hbar * H_0 / c^2 ~ 1.44e-33 eV
```
- What PDTP would need as a 2nd mass scale (not derived from m_cond)
- **Source:** Part 69

---

## 13. Symmetries

### 13a. U(1) Shift Symmetry [VERIFIED]
```
phi -> phi + c,  psi -> psi + c   (global constant c)
```
- phi_+ IS shift-protected; phi_- is NOT
- Consequence: phi_+ vacuum T_00 = 0; phi_- CAN contribute
- **Source:** Part 43, Part 68

### 13b. CPT Invariance [VERIFIED]
```
L is C, P, T invariant
```
- CP violation absent -> Sakharov baryogenesis blocked (gap)
- **Source:** Part 22

---

## 14. Numerical Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| m_P (Planck mass) | 2.176e-8 kg | Standard |
| l_P (Planck length) | 1.616e-35 m | Standard |
| omega_P (Planck freq) | 1.85e43 Hz | Standard |
| K_NAT (dimensionless coupling) | 1/(4*pi) ~ 0.0796 | Part 35 |
| xi (healing length) | l_P/sqrt(2) ~ 1.14e-35 m | Part 33 |
| sigma_SC (string tension) | 0.1729 GeV^2 | Part 38 |
| sigma_QCD (measured) | 0.18 GeV^2 | Lattice QCD |
| m_cond_QCD (inferred) | ~367 MeV | Part 37 |
| M_0 (Koide scale) | 313.84 MeV | Part 53 |
| Omega_beat | 2/3 ~ 0.667 | Part 68 |
| Omega_Lambda (observed) | 0.685 | Planck 2018 |
| L_kink (sine-Gordon) | 2^(1/4)*l_P ~ 1.92e-35 m | Part 69 |
| m_DE (dark energy scale) | ~1.44e-33 eV | Part 69 |

---

## 15. Xi_cc+ Baryon Benchmark (Part 70)

| Equation | Formula | Status | Source |
|----------|---------|--------|--------|
| Current mass sum | 2*m_c + m_d = 2554.7 MeV | [KNOWN] | PDG 2024 |
| Constituent mass sum | 2*m_c(const) + m_d(const) = 3430 MeV | [KNOWN] | EFG 2002 |
| Diquark separation | r_cc = hbar*c/(2*m_c) ~ 0.064 fm | [DERIVED] | Part 70 |
| String energy (PDTP) | E_str = sigma_PDTP * L_total = 494 MeV | [DERIVED] | Part 70 |
| String energy (QCD) | E_str = sigma_QCD * L_total = 514 MeV | [DERIVED] | Part 70 |
| PDTP combined mass | M = 3430 + 494 - 25 = 3899 MeV (+7.7%) | [DERIVED] | Part 70 |
| Mass difference (sigma gap) | Delta_M = 20 MeV (from 4% sigma gap) | [DERIVED] | Part 70 |
| Measured Xi_cc+ | 3619.97 +/- 0.40 MeV | [KNOWN] | LHCb 2026 |
| Color factor (diquark-quark) | C_F = 2/3 | [KNOWN] | Textbook |

---

## 16. Leidenfrost Decoupling Analogue (Part 71)

| Equation | Formula | Status | Source |
|----------|---------|--------|--------|
| Decoupling energy per oscillator | Delta_E = m_P*c^2/(2*sqrt(2)) | [DERIVED] | Part 71 |
| Bulk decoupling energy | E_dec = M*c^2/(2*sqrt(2)) | [DERIVED] | Part 71 |
| phi_- screening | <sin(A*sin(omega*t))> = 0 (all A) | [DERIVED] | Part 71 |
| Z3 phase cancellation | psi_1+psi_2+psi_3 = 0 (120 deg spacing) | [DERIVED] | Part 71 |
| Z3 coupling at centre | <alpha> = 0 (exact, any phi) | [DERIVED] | Part 71 |
| phi_- resonant frequency | omega = sqrt(2*g*Phi), f = 6.55e37 Hz at Earth | [DERIVED] | Part 71 |
| Metastability condition | g2/g1 >= 0.25 for V = -g1*cos + g2*cos(2*theta) | [DERIVED] | Part 71 |
| Metastable angle | cos(theta*) = g1/(4*g2) | [DERIVED] | Part 71 |

---

## 17. Full Stress-Energy Tensor T_mu_nu (Part 72)

**Single-phase** (phi condensate, psi matter):

| # | Equation | Status |
|---|----------|--------|
| 72.1 | T_00 = 1/2 phi_dot^2 + 1/2 \|grad phi\|^2 + 1/2 psi_dot^2 + 1/2 \|grad psi\|^2 - g cos(psi-phi) | [DERIVED] |
| 72.2 | T_0i = phi_dot d_i phi + psi_dot d_i psi | [DERIVED] |
| 72.3 | T_ij = d_i phi d_j phi + d_i psi d_j psi + delta_ij L | [DERIVED] |

**Two-phase** (phi_b bulk, phi_s surface, psi matter):

| # | Equation | Status |
|---|----------|--------|
| 72.4 | T_00 = 1/2 \|d phi_b\|^2 + 1/2 \|d phi_s\|^2 + 1/2 \|d psi\|^2 - g cos(psi-phi_b) + g cos(psi-phi_s) | [DERIVED] |
| 72.5 | T_0i = phi_b_dot d_i phi_b + phi_s_dot d_i phi_s + psi_dot d_i psi | [DERIVED] |
| 72.6 | T_ij = d_i phi_b d_j phi_b + d_i phi_s d_j phi_s + d_i psi d_j psi + delta_ij L_2 | [DERIVED] |

**Mode basis and identities:**

| # | Equation | Status |
|---|----------|--------|
| 72.7 | 1/2(d phi_b)^2 + 1/2(d phi_s)^2 = (d phi_+)^2 + (d phi_-)^2 | [DERIVED] |
| 72.8 | nabla^mu T_mu_nu = 0 (from Euler-Lagrange / Noether) | [DERIVED] |
| 72.9 | T_xx(grad=0) = L (pressure = Lagrangian for uniform field) | [DERIVED] |

**Source:** Peskin & Schroeder (1995) sec 2.2; Noether (1918). Script: `stress_energy_full.py` (Phase 41).
**SymPy verification:** 6/6 identities pass. **Sudoku:** 10/10 pass.

---

## 18. Emergent Metric g_mu_nu in Closed Form (Part 73)

**PDTP emergent metric** (Painleve-Gullstrand form, from acoustic metric):
```
ds^2 = -(c^2 - v^2) dt^2 - 2 v_i dx^i dt + delta_ij dx^i dx^j
```
where v_i = (hbar/m_cond) d_i phi (single-phase) or d_i phi_+ (two-phase).

- **73.1** g_00 = -(c^2 - v^2) [DERIVED, from Unruh 1981 acoustic metric]
- **73.2** g_0i = -v_i [DERIVED]
- **73.3** g_ij = delta_ij [DERIVED]
- **73.4** v_r = -sqrt(2GM/r) [radial free-fall] [ESTABLISHED, Visser 1998]
- **73.5** g_00 = -(c^2 - 2GM/r) = Schwarzschild in PG coords [DERIVED]
- **73.6** g_0r = sqrt(2GM/r) [DERIVED]
- **73.7** r_H = 2GM/c^2 (sonic horizon = Schwarzschild) [DERIVED]
- **73.8** v_i = (hbar/m_cond) d_i phi_+ (two-phase: only gravity mode) [PDTP Original]
- **73.9** gamma_PPN = 1 [DERIVED, matches Cassini bound]
- **73.10** beta_PPN = 1 [DERIVED, matches perihelion bound]
- **73.11** v_r = -sqrt(2GM/r) (Kerr radial) [DERIVED]
- **73.12** v_phi = a_J c sin(theta)/r (frame-dragging) [DERIVED, Doran 2000]
- **73.13** r_H = GM/c^2 + sqrt(G^2M^2/c^4 - a_J^2) (Kerr horizon) [DERIVED]

**Limitations:** Acoustic metric = propagation metric (not from action principle);
Einstein equations NOT derived; tensor modes need tetrad extension (Part 12).

**Sudoku:** 10/10 pass. Doc: `emergent_metric.md`. Script: `emergent_metric.py`.

---

## 19. Einstein Equations from PDTP Lagrangian (Part 74)

### 74a. Linearized Gravity DOF Count [DERIVED]
```
PDTP acoustic metric: 1 propagating scalar DOF (phase phi)
GR metric: 2 propagating tensor DOF (h_+, h_x)
Level 4: FAIL -- scalar theory cannot reproduce tensor modes
```
- Known limitation of ALL analogue gravity models (Barcelo, Liberati, Visser 2005)
- Tetrad extension (Part 12) required for tensor modes

### 74b. Sakharov Induced Gravity [DERIVED]
```
S_eff = integral d^4x sqrt(-g) * [N*Lambda^2/(96*pi^2)] * R + ...    ... (74b.1)
G_ind = 6*pi*hbar*c / (N * Lambda_mass^2)                             ... (74b.4)
Lambda_mass = m_cond  (physical UV cutoff)                             ... (74b.5)
N_eff = 6*pi ~ 18.85  (for G_Sakharov = G_PDTP)                       ... (74b.8)
```
- **Source:** Sakharov (1968), Visser (2002)
- **PDTP Original:** Lambda = m_cond is physical (healing length), not arbitrary regulator
- Achieves Levels 1, 3, 4; Level 2 partial (N_eff undetermined)

### 74c. Phase Frustration Density [PDTP Original]
```
F(x) = g * [1 - cos(psi(x) - phi(x))]                                ... (74c.1)
F ~ g/2 * (psi - phi)^2  [weak field]                                 ... (74c.2)
R ~ (gradient of phase frustration)                                    ... (74c.3)
```
- PDTP field equation nabla^2 phi = g*sin(psi-phi) IS the Poisson equation
- Phase frustration = mass density; curvature = gradient of frustration
- Josephson junction analogy: sin(delta_phi) drives response

### 74d. Jacobson Thermodynamic Route [DERIVED]
```
delta_Q = T_Unruh * delta_S_BH                                        ... (74d.1)
-> G_mu_nu = (8*pi*G/c^4) * T_mu_nu                                   ... (74d.2)
S = A/(4*a_0^2)  [lattice interpretation]                              ... (74d.3)
```
- **Source:** Jacobson (1995)
- Achieves all 4 levels; cost: S = A/(4*l_P^2) [ASSUMED]

### 74e. Direct Variational [NEGATIVE]
```
delta_S/delta_g_mu_nu is NOT well-defined (g_mu_nu composite)          ... (74e.1)
delta_S/delta_phi gives SCALAR equation only (Box phi = g*sin(psi-phi))
```
- g_mu_nu depends on phi -> variation gives 1 scalar eq, not 10 tensor eqs

### Overall Classification
**Case B (Partial):** Einstein equations motivated (Sakharov, Jacobson) but not
derived from cos(psi-phi) alone. DOF mismatch (1 scalar vs 2 tensor) is fundamental.
Same status as He-3A (Volovik 2003).

---

## 20. SU(3) Tensor Metric Construction (Part 75)

### 20a. Emergent Metric from SU(3) Linearization

```
g_mu_nu = Tr(d_mu U_dag * d_nu U)                               ... (75.0)

Linearized: U = I + i*eps*sum_a chi^a T^a
h_mu_nu = (eps^2/2) * sum_{a=1}^{8} (d_mu chi^a)(d_nu chi^a)   ... (75.1) [DERIVED]
```

**Source:** Non-linear sigma model pullback metric; Weinberg (1996) QFT Vol II Ch. 19
**SymPy verified:** Tr(M_mu * M_nu) = (1/2)*sum_a dchi_mu^a dchi_nu^a, residual = 0

### 20b. Pure Gauge Escape

phi^a tetrad (Part 74): h = d_mu chi_nu + d_nu chi_mu -> pure gauge, rank <= 2
SU(3) metric (Part 75): h = sum_a V^a (V^a)^T -> NOT pure gauge, rank 4 generically

Key: quadratic in chi (product of gradients) cannot equal linear (symmetrized gradient). [DERIVED]

### 20c. TT Mode Count

Transverse-traceless components for wave in z-direction:

```
h_+ = (1/2) sum_a [(d_1 chi^a)^2 - (d_2 chi^a)^2]
h_x = sum_a (d_1 chi^a)(d_2 chi^a)
```

Both can be independently excited -> 2 TT modes (matches GR). [DERIVED]

### 20d. Wave Equation

```
Box h_mu_nu = 2 * sum_a (d^rho d_mu chi^a)(d_rho d_nu chi^a)   ... (75.4) [DERIVED]
```

For on-shell plane waves (k^2 = 0): RHS = 0 -> Box h_mu_nu = 0  ... (75.5) [DERIVED]
Matches linearized Einstein equation in vacuum.

### 20e. PSD Constraint (New Prediction)

```
h_+^2 + h_x^2 <= h_trace^2 / 4                                 ... (75.6) [PDTP Original, SPECULATIVE]
```

Tensor GW amplitude bounded by scalar (breathing) mode. Absent from GR. Falsifiable.

### 20f. Part 75b: Full Einstein Recovery

**Induced gravitational constant (Sakharov, N_s = 8 SU(3) scalars):**
```
G_ind = (6*pi / N_s) * hbar * c / m_cond^2 = (3*pi/4) * G    ... (75b.1) [DERIVED]
```
With N_eff = 6*pi: G_ind = G exactly. N_eff identification remains open.

**Automatic Lorenz gauge (from EOM Box chi^a = 0):**
```
d^mu h_mu_nu = (1/2) d_nu h                                    ... (75b.2) [DERIVED, PDTP Original]
```
In GR this is IMPOSED; here it is AUTOMATIC from the SU(3) structure.
Consequence: vector modes constrained, only 2 TT modes propagate.

**Matter coupling (from propagation on emergent background):**
```
L_int = -(1/2) h^{mu nu} T_mu_nu^(psi)                        ... (75b.3) [DERIVED]
```
Standard graviton-matter coupling emerges from g_mu_nu = eta + h.

**Breathing mode Yukawa range:**
```
lambda_B = hbar/(m_B * c) = l_P ~ 1.6e-35 m                   ... (75b.4) [DERIVED]
```
Breathing mode massive (m_B ~ m_P), invisible at astro distances.
PSD constraint Eq. 75.6 applies at source, not at detector.

**Simulation:** su3_einstein_recovery.py Phase 45. Sudoku: 12/12 PASS.

---

## 20g. Part 76 — SU(3) Graviton Validation

**Fierz-Pauli from Sakharov** (76a):
```
L_EH^(2) = (1/64*pi*G) * [(d h)^2 - 2*(d.h)^2 + 2*(d.h)(dh) - (dh)^2]
                                                          ... (76a.1) [DERIVED]
```
Unique ghost-free massless spin-2 structure. Emerges via Sakharov 1-loop.

**Isaacson GW stress-energy** (76b):
```
T^GW_mu_nu = (1/32*pi*G) * <d_mu h_ab * d_nu h^ab>      ... (76b.1) [DERIVED]
```
Source: Isaacson (1968), MTW (1973). Non-zero for any non-trivial chi^a.

**O(eps^4) SU(3) correction** (76g):
```
h^(4)_mu_nu ~ f^{abc} f^{ade} chi^b chi^d (d chi^c)(d chi^e)
                                                          ... (76g.1) [DERIVED]
```
Structure constants introduce self-interaction at GR-nonlinear order.

**Key results:**
- O(chi) IS pure gauge (expected); O(chi^2) is NOT (rank 4 > 2). [DERIVED]
- Bianchi identity automatic (3 arguments). [DERIVED]
- 2-DOF deficit: 8 fields < 10 metric components. [LIMITATION]
- Spin connection: SU(3) != SO(3,1); omega emerges from Sakharov metric. [NEGATIVE]

**Simulation:** su3_graviton_validation.py Phase 46. Sudoku: 12/12 PASS.

---

## 21. Central Open Problem

**m_cond is underdetermined** -- G = hbar*c/m_cond^2 is exact but m_cond = m_P is not derived.
This is analogous to Lambda in GR. All perturbative AND SU(3) paths exhausted (Parts 29-35, 77-78).

**Free parameters:** m_cond (or equivalently G), and L_H (or equivalently Lambda)

### Part 77 additions (SU(3) dimensional transmutation FCC):

| # | Equation | Status | Source |
|---|----------|--------|--------|
| 77.4 | beta_lat = N_c * K_NAT = 3/(4*pi) = 0.2387 | [DERIVED] | Lattice coupling identification |
| 77.6 | alpha_s(PDTP) = 2/K_NAT = 2.0 (strong coupling) | [DERIVED] | PDTP = strong SU(3) |
| 77.10 | Lambda/mu = exp(-pi/11) = 0.752 (mild suppression) | [DERIVED] | No hierarchy from SU(3) AF |
| 77.19 | m_cond_QCD = hbar/(c*sqrt(ln(6/beta_lat)/sigma_QCD)) = 0.236 GeV | [PDTP Original] | Reverse chain |
| 77.24 | m_cond <= m_P/sqrt(2) (BH consistency bound) | [DERIVED] | Compton >= Schwarzschild |
| 77.25 | m_cond = m_P saturates BH bound | [OBSERVED] | Extremal condensate hypothesis |

### Part 78 additions (Extremal Condensate — 4 remaining A1 paths):

| # | Equation | Status | Source |
|---|----------|--------|--------|
| 78.1 | S_Bek = 2*pi*k_B per cell (m_cond cancels) | [DERIVED] | Bekenstein (1981); R=a_0, E=m_cond*c^2 |
| 78.2 | S_holo = pi per cell (l_P = a_0 tautology) | [DERIVED] | 't Hooft/Susskind; holographic limit by construction |
| 78.3 | N_modes = V*(m_cond*c/hbar)^3/(6*pi^2) | [ESTABLISHED] | Mode counting; monotonic in m_cond |
| 78.4 | eta = 1/(4*a_0^2) = m_cond^2*c^2/(4*hbar^2) | [DERIVED] | Jacobson entropy density |
| 78.5 | M_P^2 = N*Lambda_grav^2; N=1 for PDTP | [ESTABLISHED] | Dvali (2007); one condensate field |
| 78.7 | rho_0 = 12*K_NAT = 3/pi = 0.955 (VEV) | [PDTP Original] | Mexican hat from cosine expansion |
| 78.9 | S_inst = 8*pi^2/g^2 = pi exactly | [PDTP Original] | BPST instanton with g^2=8*pi |
| 78.10 | exp(-S_inst) = exp(-pi) = 0.0432 (10^15x QCD) | [PDTP Original] | Instanton weight; not suppressed |

**Conclusion (Parts 29-35, 77-78):** PDTP determines dimensionless structure (S_Bek, S_holo,
rho_0, S_inst) but not dimensional scale (m_cond). Confirmed after 11 independent paths.

### Part 79 additions (alpha_EM FCC — fine-structure constant):

| # | Equation | Status | Source |
|---|----------|--------|--------|
| 79.1 | alpha_EM(M_P) = 1/64.1 needed for 1/137 at m_e | [DERIVED] | 1-loop QED RG backward solve |
| 79.2 | K_NAT^2 = 1/(4*pi)^2 = 1/157.9 (PDTP coupling^2) | [DERIVED] | Part 55; 13.2% off alpha_EM |
| 79.3 | alpha = Z_0/(2*R_K) = e^2/(4*pi*eps_0*hbar*c) | [EXACT] | Established impedance identity |
| 79.4 | e*g_m = 2*pi*n*hbar (Dirac quantization) | [ESTABLISHED] | Dirac (1931) |
| 79.5 | g_m/e = 1/(2*alpha) = R_K/Z_0 = 68.5 | [DERIVED] | Impedance duality |
| 79.6 | Wyler: alpha_W^{-1} = 137.03608 (0.6 ppm) | [ESTABLISHED] | Wyler (1969); O(4,2) geometry |
| 79.7 | sin^2(theta_W) = 3/8 at GUT scale | [DERIVED] | SU(5) group theory |

**Conclusion (Parts 52, 55-57, 79):** alpha_EM = 1/137.036 is a free parameter of PDTP,
analogous to m_cond for gravity. Same barrier: structure derived, values not.
8 independent approaches, all negative. Confirmed after Part 79 FCC.

### Part 80 additions (dispersion two-phase re-examination):

| # | Equation | Status | Source |
|---|----------|--------|--------|
| 80.1 | E_gap(phi_-) = hbar*sqrt(2*g*Phi) | [DERIVED] | Part 62 + Part 80 Check 1 |
| 80.2 | phi_- does not couple to A_mu or A_mu^a | [DERIVED] | Part 80 Check 2 (spin-0 vs spin-1) |
| 80.3 | b0_QCD = 7 unchanged by phi_- | [DERIVED] | Part 80 Check 3 (quantum loops) |
| 80.4 | E_gap(BH) = hbar*sqrt(g) ~ 2.83 MeV << E_GUT | [DERIVED] | Part 80 Check 4 |

**Conclusion (Part 80):** Dispersion model re-examined with two-phase phi_-. All 4 fatal
problems persist (2 improved, 2 unchanged). Root cause: coupling running is quantum
(vacuum polarization), not classical dispersion. D3 closed as NEGATIVE CONFIRMED.

### Part 81 additions (wave effects audit — G as combination effect):

| Eq. | Formula | Status | Source |
|-----|---------|--------|--------|
| 81.1 | 1/(16*pi*G) = N_eff * Lambda^2 / (192*pi^2) | [ASSUMED] | Sakharov (1967), Visser (2002) |
| 81.2 | N_eff = 12*pi ~ 37.7 (PDTP-Sakharov consistency) | [DERIVED] | PDTP Original |
| 81.3 | G = hbar*c * m_cond^(-2); all ingredients scale same way | [DERIVED] | PDTP Original |
| 81.4 | Box(phi_+) = -g*cos(psi-phi_+)*sin(phi_-) | [VERIFIED] | Part 61 + Part 81 |

**Conclusion (Part 81):** SOFAR hypothesis REJECTED — all G ingredients scale as m_cond^(-2),
no cross-constraint. 55 wave effects audited: 30 YES, 12 NO. 9 candidate terms tested; none
pin m_cond. DeepSeek derivation has 6 errors (factors, dimensions, wrong mechanism).
Sakharov one-loop with PDTP layer confinement remains open (N_eff = 12*pi needed, 23-29 available).
10/10 Sudoku PASS.

### Part 82 additions (Koide circularity re-examination — D4):

| Eq. | Formula | Status | Source |
|-----|---------|--------|--------|
| 82.1 | r_Yukawa = sqrt(hbar * Phi / (4 * m_P)) | [DERIVED] | PDTP Original (reversed Higgs + screened Poisson) |
| 82.2 | M_0 = mu^2 = 313.84 MeV ~ m_p/3 | [CONFIRMED, 0.3%] | Brannen parametrization |
| 82.3 | theta_0 ~ theta_C = arcsin(V_us) | [SPECULATIVE, 2.2%] | Near-miss; excluded by m_e precision |
| 82.4 | G(M_0)/G = (m_P/M_0)^2 ~ 3.6e38 | [CONFIRMED] | Hierarchy wall |

**Conclusion (Part 82):** D4 remains NEGATIVE — Koide is structure theorem, not scale theorem.
New findings (Parts 37-81) do not change this. phi_- reversed Higgs = chameleon mechanism
(environment-dependent mass, PDTP Original). Yukawa screening at Earth surface ~10^-18 m
(too short for fifth-force tests, consistent with non-observation). theta_0 ~ theta_C at
2.2% but excluded by electron mass sensitivity. M_0 ~ m_p/3 at 0.3% is structural.
7/10 Sudoku PASS (3 expected failures: ratio mismatch, hierarchy, Yukawa range).

### Part 83 additions (N_eff = 6pi gap in Sakharov formula — B1 FCC):

| Eq. | Formula | Status |
|-----|---------|--------|
| 83.1 | G_ind = (6pi/N_eff) * hbar*c / m_cond^2 | [VERIFIED] |
| 83.2 | N_eff = sum_i epsilon_i * nu_i (signed helicity sum) | [STANDARD] |
| 83.3 | N_eff(PDTP, minimal) = 8 (gluon scalars) | [DERIVED] |
| 83.4 | N_eff(PDTP, two-phase) = 10 (+ phi_+, phi_-) | [DERIVED] |
| 83.5 | N_eff(PDTP, +matter) = 34 (+ 24 vortex phases) | [ESTIMATED] |
| 83.6 | G_ind/G = 6pi/N_eff (scheme-independent ratio) | [DERIVED] |

**Conclusion (Part 83):** B1 = PARTIAL — gap characterized, not closed. G_ind = 2.356*G
with 8 gluons confirmed. PDTP N_eff range: 10 (two-phase) to 34 (with matter); target
6pi ~ 18.85 lies between them — physically reasonable. Near-miss: 8 + (4/3)*8 = 18.67
(Casimir enhancement, 1% off). SM signed sum = -62 (fermion-dominated, known issue).
The gap is UNIVERSAL — shared by all induced gravity approaches. 10/10 Sudoku PASS.

### Part 84 additions (Tetrad from SU(3) — B3 FCC Resolution):

| Eq | Expression | Status |
|----|-----------|--------|
| 84.1 | Phi_extended = sqrt(rho_0) * exp(i*phi) * e^a_mu | [ASSUMED] |
| 84.2 | g_mu_nu = eta_ab * e^a_mu * e^b_nu | [ESTABLISHED] |
| 84.4 | g_mu_nu = Tr(d_mu U_dag * d_nu U) | [PDTP Original] |
| 84.5 | h_mu_nu = (eps^2/2) * sum_a (d_mu chi^a)(d_nu chi^a) | [DERIVED] |
| 84.6 | DOF deficit = 10 - 8 = 2 (metric components - SU(3) fields) | [DERIVED] |
| 84.9 | G_ind = (6*pi / N_eff) * hbar*c / m_cond^2 | [DERIVED] |
| 84.10 | G_ind(N_s=8) = (3*pi/4) * G = 2.356 * G | [DERIVED] |

**Conclusion (Part 84):** B3 = PARTIALLY RESOLVED. SU(3) emergent metric (Part 75)
replaces explicit tetrad (Part 12) for linearized gravity: 2 TT modes derived (not
postulated), auto-Lorenz gauge, Fierz-Pauli emergent, pure gauge escaped. Head-to-head:
Part 75 wins 6, Part 12 wins 4, ties 7. Two-phase compatible (4/4 checks pass).
Remaining: 2-DOF deficit for strong-field, N_eff gap (B1). 12/12 Sudoku PASS.

---

## 22. Three Lagrangians — Multiple Mathematical Forms

Each Lagrangian can be expressed in equivalent forms. Different forms expose
different structure — use all forms when testing and deriving.

### 21a. Lagrangian Density (the defining form)

```
U(1):       L = (1/2)(d_mu phi)(d^mu phi) + Sum_i g_i cos(psi_i - phi)
Two-Phase:  L = +g cos(psi - phi_b) - g cos(psi - phi_s)
SU(3):      L = K Tr[(d_mu U^dag)(d^mu U)] + Sum_i g_i Re[Tr(Psi_i^dag U)] / 3
```

### 21b. Action Integral (variational principle)

```
U(1):       S = int d^4x [ (1/2)(d phi)^2 + Sum g_i cos(psi_i - phi) ]
Two-Phase:  S = int d^4x  g [ cos(psi - phi_b) - cos(psi - phi_s) ]
SU(3):      S = int d^4x { K Tr(dU^dag dU) + Sum g_i Re[Tr(Psi_i^dag U)] / 3 }
```

### 21c. Field Equations (Euler-Lagrange) [DERIVED]

```
U(1):       Box(phi) = Sum g_i sin(psi_i - phi)
Two-Phase:  Box(phi_+) = g sin(psi - phi_+) cos(phi_-)
            Box(phi_-) = -g cos(psi - phi_+) sin(phi_-)
SU(3):      K d_mu(U^dag d^mu U) = Sum g_i Psi_i^dag / (6i) + h.c.
```

### 21d. Quadratic (Small Oscillation) Expansion [DERIVED]

cos(x) ~ 1 - x^2/2 for small x:

```
U(1):       L ~ (1/2)(d phi)^2 - (1/2) g (psi - phi)^2     [harmonic oscillator]
Two-Phase:  L ~ 2g (psi - phi_+) phi_-                       [bilinear coupling]
SU(3):      L ~ K Tr(d chi)^2 + Sum g_i (1 - Tr(chi^2)/6)   [U = exp(i chi^a T^a)]
```

### 21e. Product / Lattice Form [DERIVED]

```
U(1):       cos(psi - phi)   [single coupling]
Two-Phase:  2 sin(psi - phi_+) sin(phi_-)   [product of two modes]
SU(3):      -K Re[Tr(U_plaquette)] / 3      [Wilson action on lattice]
```

### 21f. Emergent Metric [DERIVED where noted]

```
U(1):       g_mu_nu from acoustic analogy (Part 12, postulated)
Two-Phase:  g_mu_nu from phi_+ sector (inherits U(1) form)
SU(3):      g_mu_nu = Tr(d_mu U^dag d_nu U)   [DERIVED, Part 75; 2 TT modes]
```

### 21g. Newtonian Limit [DERIVED]

```
U(1):       nabla^2 Phi = 4 pi G rho                        [Poisson equation]
Two-Phase:  nabla^4 Phi + 4g^2 Phi = source                 [biharmonic]
SU(3):      nabla^2 Phi = 4 pi G rho + O(chi^2) corrections [Poisson + SU(3)]
```

### 21h. Summary Table

| Property | U(1) | Two-Phase | SU(3) |
|----------|------|-----------|-------|
| Symmetry | U(1) shift | U(1) x U(1) | SU(3) gauge |
| DOF | 1 scalar | 2 scalars (phi_+, phi_-) | 8 (N^2 - 1) |
| Gravity | +cos phase-lock | phi_+ sector | Tr coupling |
| Novel mode | breathing (massive) | phi_- reversed Higgs | 8 gluons, Z_3 quarks |
| Newton limit | Poisson | biharmonic | Poisson + corrections |
| GW modes | 2 TT + 1 breathing | same + phi_- mode | 2 TT (Fierz-Pauli) |
| Status | 76 parts tested | 16/16 PASS (Part 63) | Einstein recovery (Part 75b) |

**Source:** Parts 1, 37, 61, 75. Cross-reference: Sections 1a-1c above.

---

### Part 86 additions (Nonlinear Einstein — B2 FCC Resolution):

| Eq | Expression | Status |
|----|-----------|--------|
| 86.0 | S_PDTP = K * int d^4x Tr(d_mu U_dag d^mu U)  [principal chiral model] | [ASSUMED] |
| 86.1 | U = I + i*eps*(chi^a T^a) - (eps^2/2)*(chi^a T^a)^2 + ... | [DERIVED] |
| 86.2 | Tr(dU_dag dU)|_{O(eps^2)} = eps^2 * (d_mu chi^a)^2  [linearized] | [DERIVED] |
| 86.3 | Tr(dU_dag dU)|_{O(eps^4)} ~ f^{abc}f^{ade} chi^b chi^d (d chi^c)(d chi^e)  [chi^2*(d chi)^2] | [DERIVED, PDTP Original] |
| 86.4 | R^(2)_EH ~ (d_mu h_nu_rho)^2 - (1/2)(d_mu h)^2  [GR O(h^2)] | [KNOWN] |
| 86.5 | d_mu(U_dag d^mu U) = 0  [sigma model field eq; NOT Einstein] | [DERIVED] |
| 86.6 | N_boundary = A / a_0^2  [horizon boundary cells] | [DERIVED, PDTP Original] |
| 86.7 | S_PDTP = k_B * ln(2) * A / a_0^2  [microscopic entropy] | [DERIVED, PDTP Original] |
| 86.8 | S_BH = k_B * A / (4*l_P^2)  [Bekenstein-Hawking] | [KNOWN] |
| 86.9 | S_PDTP/S_BH|_{a_0=l_P} = 4*ln(2) = 2.773  [entropy gap at baseline] | [DERIVED, PDTP Original] |
| 86.10 | a_0 = 2*sqrt(ln(2))*l_P ~ 1.665*l_P  [entropy matching condition] | [DERIVED, PDTP Original] |
| 86.11 | delta_Q = hbar*a*ln(2)/(2*pi*c*a_0^2) * dA  [PDTP Clausius] | [DERIVED, PDTP Original] |
| 86.12 | G_mu_nu = 8*pi*G_eff T_mu_nu  [Jacobson + S_PDTP; exact at a_0=1.665*l_P] | [DERIVED, PARTIAL] |
| 86.13 | nabla^4 Phi + 4*g^2*Phi = source  [biharmonic GR, Part 61] | [DERIVED] |
| 86.14 | Phi(r) ~ source/(8*pi*r)  [biharmonic Green's fn at r << r* = l_P] | [DERIVED] |

**Conclusion (Part 86):** B2 = PARTIALLY RESOLVED. Three strategies explored:
(1) O(eps^4) sigma model: NEGATIVE — generates chi^2*(d chi)^2 but GR needs (d h)^2; field equations structurally different.
(2) PDTP microscopic entropy: S = k_B*ln(2)*A/a_0^2 [PDTP Original]; entropy-area law holds at a_0 = 1.665*l_P.
(3) Jacobson + S_PDTP: full GR derived at corrected a_0 [PARTIAL].
Gap convergence: entropy gap 4*ln(2)=2.773 and Sakharov gap 3*pi/4=2.356 both ~2-3 independently. 12/12 PASS.

---

### Part 87 additions (Cosmological Constant — A3 FCC):

| Eq | Expression | Status |
|----|-----------|--------|
| 87.1 | rho_vac ~ N_eff * hbar*c / (16*pi^2 * a_0^4)  [Sakharov vacuum sum] | [DERIVED] |
| 87.2 | rho_vac_PDTP = hbar/(c*a_0^4) = rho_Planck/(4*ln(2))^2 = rho_P/7.68  [entropy-corrected] | [DERIVED, PDTP Original] |
| 87.3 | V(phi_-) = -2*g*cos(phi_-)  [two-phase vacuum potential] | [DERIVED, Part 61] |
| 87.4 | rho_Lambda_PDTP = g_phys * phi_-_vac^2  [Lambda = phi_- VEV] | [DERIVED, PDTP Original] |
| 87.5 | phi_-_vac = sqrt(rho_Lambda/g_phys) ~ 10^-70 rad  [cosmological phase offset] | [DERIVED, PDTP Original] |
| 87.6 | Lambda(t) = g * phi_-_vac(t)^2  [dynamical cosmological constant] | [SPECULATIVE, PDTP Original] |

**Conclusion (Part 87):** A3 = CONFIRMED FREE PARAMETER -- CLOSED. Seven approaches all fail to
derive Lambda. Reframe succeeds: Lambda = g*phi_-_vac^2 (VEV of phi_- field). Lambda is
dynamical in PDTP: w(z) != -1 [SPECULATIVE, consistent with DESI 2024]. rho_Planck_PDTP =
rho_Planck/7.68 [PDTP Original from entropy correction]. 12/12 Sudoku PASS.

---

### Part 88 additions (Hubble Tension — C1 FCC):

| Eq | Expression | Status |
|----|-----------|--------|
| 88.0a | H_0^CMB = 67.4 km/s/Mpc [Planck 2020] | [ASSUMED] |
| 88.0b | H_0^SH0ES = 73.04 km/s/Mpc [Riess+2022] | [ASSUMED] |
| 88.1 | phi_-_ddot + 3*H(z)*phi_-_dot + m_phi_-^2*phi_- = 0  [phi_- EOM in FRW] | [DERIVED] |
| 88.2 | m_phi_-^2 = 0 in vacuum (reversed Higgs, Part 62)  -> phi_-_dot = 0 -> w = -1 | [DERIVED] |
| 88.3 | rho_phi_-(z=3000)/rho_EDE_req = 4.4e-10  (9.4 orders deficit) | [COMPUTED, PDTP Original] |
| 88.4 | phi_-_vac_EDE = sqrt(rho_EDE/g_phys) ~ 5.41e-66 rad  (4.7 orders above today) | [COMPUTED, PDTP Original] |
| 88.5 | delta_H_0/H_0 ~ (l_P/r_s)^2 = 1.27e-119  (biharmonic; 118 orders too small) | [COMPUTED] |
| 88.6 | V_EDE(phi_-) = g*phi_-^2 + lambda*phi_-^4  [tracking attractor; NOT in PDTP] | [SPECULATIVE, PDTP Original] |

### Part 89 additions (Condensate Layer Optics):

| Eq | Expression | Status |
|----|-----------|--------|
| 89.1 | omega^2 = c^2*k^2 + omega_gap^2  [condensate phonon dispersion] | [ASSUMED] |
| 89.2 | omega_gap = m_cond * c^2 / hbar  [gap from condensate mass] | [DERIVED] |
| 89.3 | n_eff(omega) = sqrt(1 - (omega_gap/omega)^2)  [plasma-type index] | [DERIVED] |
| 89.4 | sin(theta_c) = n_C2/n_C1  [Snell's law critical angle at B1] | [DERIVED] |
| 89.5 | lambda_evan(B1,E=0) = hbar/(Lambda_QCD*c) = 0.987 fm  [QCD scale] | [DERIVED, PDTP Original] |
| 89.6 | lambda_evan(B2,E=0) = hbar/(m_W*c) = 0.00245 fm  [weak force range] | [DERIVED, PDTP Original] |
| 89.7 | lambda_evan(B1)/lambda_evan(B2) = m_W/Lambda_QCD = 402  [force range ratio] | [DERIVED, PDTP Original] |
| 89.8 | sigma_DM/m = G/c^4 ~ 10^-43 cm^2/g << Bullet Cluster bound  [DM self-interaction] | [DERIVED] |

**Conclusion (Part 89):** B7 first investigation complete. Force ranges of QCD (~1 fm) and
weak interaction (~0.002 fm) derived as evanescent penetration depths at C1/C2 and C2/C3
boundaries. n_eff hierarchy confirmed: n_C1=1 > n_C2(E) > n_C3(E). Dark matter as
mode-mismatch U(1)-only C1 vortex: gravity-only coupling, Bullet Cluster safe. Full FCC +
wave effects check pending (TODO_03 B7, Priority 12). 12/12 Sudoku PASS.

---

**Conclusion (Part 88):** C1 = NEGATIVE (confirmed) -- CLOSED. All 5 mechanisms fail:
(1) phi_- EDE: frozen (m=0 -> w=-1) AND 9.4 orders too weak.
(2) phi_- -> G variation: G constant; phi_- not coupled to m_cond.
(3) Biharmonic: 118 orders too small (sub-Planck only).
Missing physics: positive phi_-^4 quartic term in condensate potential.
Falsifiable: DESI w(z) distinguishes systematics vs real physics. 12/12 Sudoku PASS.

---

## Changelog
- 2026-03-29: Added Part 89 (condensate layer optics; n_eff, TIR, evanescent depths; lambda_evan(B1)=0.987 fm, lambda_evan(B2)=0.00245 fm; force ranges derived; DM mode-mismatch; 12/12 PASS)
- 2026-03-29: Added Part 88 (Hubble tension C1 FCC; NEGATIVE confirmed; phi_- frozen w=-1; 9.4 orders deficit; phi_-^4 missing; biharmonic 118 orders off; 12/12 PASS)
- 2026-03-29: Added Part 87 (Lambda A3 FCC; CONFIRMED FREE PARAM; Lambda=g*phi_-_vac^2; rho_vac=rho_P/7.68; phi_-_vac~10^-70 rad; DESI w(z) consistent; 12/12 PASS)
- 2026-03-29: Added Part 86 (Nonlinear Einstein B2 FCC; PARTIALLY RESOLVED; sigma model NEGATIVE; S_PDTP=k_B*ln(2)*A/a_0^2; a_0=1.665*l_P for area law; Jacobson full GR; entropy gap 4*ln(2)~Sakharov 3*pi/4; 12/12 PASS)
- 2026-03-29: Added Part 85 (CP violation B4 FCC; PARTIALLY RESOLVED; L5 sin(2phi_-)=real CP; delta=-eps/g; eps/g~3e-7 gives eta~6e-10; L6=theta-term; 12/12 PASS)
- 2026-03-28: Added Part 84 (Tetrad B3 FCC; PARTIALLY RESOLVED; SU(3) replaces tetrad for linearized gravity; 6 replaced, 2 partial, 1 not; 12/12 PASS)
- 2026-03-28: Added Part 83 (N_eff=6pi gap B1 FCC; PARTIAL; G_ind=2.356G confirmed; N_eff range 10-34; 6pi between; Casimir near-miss 1%; 10/10 PASS)
- 2026-03-27: Added Part 82 (Koide D4 re-exam; STILL NEGATIVE; chameleon=reversed Higgs; r_Yukawa~10^-18 m; theta_0~theta_C 2.2%; 7/10 PASS)
- 2026-03-25: Added Part 81 (wave effects audit; SOFAR rejected; 55 effects audited, 12 missing; N_eff=12pi; DeepSeek 6 errors; 10/10 PASS)
- 2026-03-24: Added Part 80 (dispersion two-phase; 4 checks, 2 improved, 2 unchanged; E_gap=hbar*sqrt(2gPhi); 10/10 PASS)
- 2026-03-22: Added Part 79 (alpha_EM FCC; 5 paths NEGATIVE; impedance duality; Wyler 0.6 ppm; backward-solve 1/64; 9/10 PASS)
- 2026-03-22: Added Part 78 (extremal condensate; 4 paths NEGATIVE; S_Bek=2pi, S_holo=pi, VEV=3/pi, S_inst=pi; 9/9 PASS)
- 2026-03-22: Added Section 21 (three Lagrangians in multiple mathematical forms)
- 2026-03-22: Added Part 77 (SU(3) dim transmutation FCC; alpha_s=2.0; BH bound; m_cond_QCD reverse chain; 8/8 PASS)
- 2026-03-22: Renumbered: Section 21=Open Problem, Section 22=Three Lagrangians (was duplicate 21)
- 2026-03-22: Added Part 76 (SU(3) graviton validation; gauge exclusion; FP; Isaacson; Bianchi; 12/12 PASS)
- 2026-03-22: Added Part 75b (SU(3) Einstein recovery; auto-Lorenz; massive breathing; 12/12 PASS)
- 2026-03-21: Added Part 75 (SU(3) tensor metric; NOT pure gauge; 2 TT modes; PSD constraint)
- 2026-03-21: Clarified eigenvalue vs frequency in Sections 2f and 6b (lambda is growth rate, not omega^2); added [A1] ODE tag
- 2026-03-21: Added Part 74 (Einstein from PDTP; Sakharov, Jacobson, frustration; Case B partial)
- 2026-03-21: Added Part 73 (emergent metric g_mu_nu, PG form, PPN, Kerr)
- 2026-03-21: Added Part 72 (full T_mu_nu, all components, conservation law, two-phase)
- 2026-03-20: Added Part 71 (Leidenfrost decoupling analogue, phi_- screening, Z3 cancellation)
- 2026-03-20: Added Part 70 (Xi_cc+ baryon benchmark, string energy, mass prediction)
- 2026-03-20: Added Part 69 (scale selection, cosine-Gordon, kink width, m_DE)
- 2026-03-20: Initial creation from Parts 1-68

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
eigenvalue = +2*sqrt(2)*g > 0
```
- Positive = gravitational collapse from Lagrangian (not assumed)
- **Source:** Part 61

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
- Branch A (+): gapped breathing mode
- Branch B (-): Jeans unstable mode (gravitational collapse)
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

## 15. Central Open Problem

**m_cond is underdetermined** -- G = hbar*c/m_cond^2 is exact but m_cond = m_P is not derived.
This is analogous to Lambda in GR. All perturbative paths exhausted (Parts 29-35).

**Free parameters:** m_cond (or equivalently G), and L_H (or equivalently Lambda)

---

## Changelog
- 2026-03-20: Added Part 69 (scale selection, cosine-Gordon, kink width, m_DE)
- 2026-03-20: Initial creation from Parts 1-68

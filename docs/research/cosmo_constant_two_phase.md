# Cosmological Constant -- Two-Phase Deep Investigation (Part 68)

**Method:** Forced Checklist Check applied to the cosmological constant problem
**Status:** Partially derived (Omega_beat = 2/3); Lambda still uses H_0 as input
**Script:** `simulations/solver/cosmo_constant_v2.py` (Phase 37)
**Previous:** Part 54 (`cosmo_constant.py`) -- concluded Lambda = free parameter (single-phase)
**Date:** 2026-03-19

---

## 1. Motivation

Part 54 concluded that Lambda is a second free parameter alongside G (= hbar*c/m_cond^2).
Since then, we built powerful new tools:

- Two-phase Lagrangian (Parts 61-63): L = g*cos(psi-phi_b) - g*cos(psi-phi_s)
- Reversed Higgs (Part 62): phi_- massless in vacuum, massive near matter
- White comparison (Part 67): NR limit D = hbar/(2*m_cond)
- Quantum geometry (Part 66): quantum metric in Lagrangian
- Frequency reframe: omega_gap, beat frequencies, dispersion branches

**Central question:** Does the two-phase Lagrangian derive Lambda?

---

## 2. Two-Phase Lagrangian (recap)

**Source:** Part 61, `two_phase_lagrangian.py`

Starting point [ASSUMED]:
```
L = g*cos(psi - phi_b) - g*cos(psi - phi_s)                         (1)
```

Change of variables [DERIVED]:
```
phi_+ = (phi_b + phi_s) / 2    (gravity mode)
phi_- = (phi_b - phi_s) / 2    (surface mode)
```

Product coupling identity [DERIVED, SymPy VERIFIED]:
```
cos(A-B) - cos(A+B) = 2*sin(A)*sin(B)
=> L_coupling = 2*g*sin(psi - phi_+)*sin(phi_-)                     (2)
```

Full Lagrangian in (+/-) variables [DERIVED]:
```
L = phi_+_dot^2 + phi_-_dot^2 + (1/2)*psi_dot^2
    + 2*g*sin(psi - phi_+)*sin(phi_-)                                (3)
```

---

## 3. Phase A: Two-Phase Vacuum Energy

### 3.1 Stress-Energy Tensor (T_mu_nu)

**PDTP Original.** Canonical Hamiltonian construction.

Starting from (3):
```
pi_+ = dL/d(phi_+_dot) = 2*phi_+_dot                                (4a)
pi_- = dL/d(phi_-_dot) = 2*phi_-_dot                                (4b)
pi_psi = dL/d(psi_dot) = psi_dot                                    (4c)
```

Hamiltonian (energy density) [DERIVED, SymPy VERIFIED]:
```
T_00 = H = sum(pi_i * qi_dot) - L
     = 2*phi_+_dot^2 + 2*phi_-_dot^2 + psi_dot^2 - L
     = phi_+_dot^2 + phi_-_dot^2 + (1/2)*psi_dot^2
       - 2*g*sin(psi-phi_+)*sin(phi_-)                              (5)
```

Pressure (Hilbert convention, spatially uniform) [DERIVED]:
```
p = L = phi_+_dot^2 + phi_-_dot^2 + (1/2)*psi_dot^2
        + 2*g*sin(psi-phi_+)*sin(phi_-)                             (6)
```

**Source:** Peskin & Schroeder (1995), sec 2.2
**SymPy verification:** `check_equal(H, T00_expected)` -- residual = 0

### 3.2 Vacuum Evaluation

**Case 1: phi_- = 0 (standard vacuum)**

Set phi_- = 0, all time derivatives = 0:
```
V(phi_-=0) = 2*g*sin(psi-phi_+)*sin(0) = 0
T_00 = 0, p = 0                                                     (7)
```
[DERIVED, SymPy VERIFIED] **Same as single-phase: zero vacuum energy.**

**Case 2: phi_- = pi/2, psi = phi_+ (locked)**
```
V(phi_-=pi/2) = 2*g*sin(psi-phi_+)*sin(pi/2) = 2*g*sin(psi-phi_+)
At psi = phi_+: sin(0) = 0
T_00 = 0                                                            (8)
```
[DERIVED] **Locked state: still zero.**

**Case 3: phi_- = pi/2, psi = phi_+ + delta (mismatch)**
```
T_00 = -2*g*sin(delta)                                              (9)
```
[DERIVED] **Nonzero vacuum energy requires psi-phi_+ mismatch.**

### 3.3 U(1) Shift Symmetry

Under uniform shift: phi_+ -> phi_+ + alpha, psi -> psi + alpha, phi_- unchanged:
```
V(psi+a, phi_++a, phi_-) = 2*g*sin(psi-phi_+)*sin(phi_-) = V(psi,phi_+,phi_-)
```
[DERIVED, SymPy VERIFIED] **Shift-invariant.**

**Key finding:** phi_- is NOT shifted by the U(1) symmetry. It's a physical DOF
with its own dynamics. The shift protects (psi - phi_+) but NOT phi_-.

### 3.4 phi_- Potential at Equilibrium

```
V = 2*g*sin(psi-phi_+)*sin(phi_-)
dV/d(phi_-) = 2*g*sin(psi-phi_+)*cos(phi_-)
d^2V/d(phi_-)^2 = -2*g*sin(psi-phi_+)*sin(phi_-)

At equilibrium (phi_- = 0, psi = phi_+):
  dV/d(phi_-) = 0
  d^2V/d(phi_-)^2 = 0                                              (10)
```

[DERIVED, SymPy VERIFIED] **phi_- is a FLAT direction at equilibrium.**
This means phi_- is Goldstone-like: massless in vacuum.

**Source:** Goldstone (1961), Nuovo Cimento 19
**PDTP context:** Part 62 (reversed Higgs) already identified this.

### 3.5 phi_- Zero-Point Energy (1-loop)

Standard QFT result for a massless scalar with UV cutoff Lambda_UV = 1/a_0 = 1/l_P:

```
rho_ZPE = hbar*c*Lambda_UV^4 / (16*pi^2)
        = hbar*c / (16*pi^2*l_P^4)
        ~ 3.26e94 kg/m^3 ~ 0.006 * rho_Planck                     (11)
```

**Source:** Peskin & Schroeder (1995), sec 11.4
**Source:** Weinberg (1989), "The Cosmological Constant Problem", Rev.Mod.Phys. 61

[DERIVED] **phi_- naive ZPE ~ rho_Planck.** The CC problem is reproduced.

phi_- is NOT shift-protected, so this ZPE is NOT automatically cancelled.
The two-phase structure alone does NOT solve the CC problem.

---

## 4. Phase B: Dispersion Relations and Beat Frequencies

### 4.1 Linearised Two-Phase Dispersion

Starting from Part 61 linearised equations (with spatial gradients added):
```
delta_tt - c^2*delta_xx = 4*g*epsilon      (Phi = psi - phi_+)
epsilon_tt - c^2*epsilon_xx = 2*g*delta     (phi_-)                 (12)
```

Plane wave ansatz: delta, epsilon ~ exp(i(kx - omega*t)):
```
(c^2*k^2 - omega^2)*delta = 4*g*epsilon
(c^2*k^2 - omega^2)*epsilon = 2*g*delta
```

Eliminate to get:
```
(c^2*k^2 - omega^2)^2 = 8*g^2
c^2*k^2 - omega^2 = +/- 2*sqrt(2)*g                               (13)
```

**Two dispersion branches** [DERIVED]:
```
Branch A (Jeans):     omega^2 = c^2*k^2 - 2*sqrt(2)*g              (14a)
Branch B (breathing): omega^2 = c^2*k^2 + 2*sqrt(2)*g              (14b)
```

- Branch A: unstable at k < k_J (Jeans instability = gravitational collapse)
- Branch B: gapped, always stable, omega_gap = sqrt(2*sqrt(2)*g)

Jeans wavenumber [DERIVED]:
```
k_J = sqrt(2*sqrt(2)*g) / c = omega_gap / c                        (15)
lambda_J = 2*pi/k_J = 2*pi*l_P ~ 1.02e-34 m
```

### 4.2 Beat Frequency Between Branches

For k >> k_J (short wavelengths):
```
omega_+ ~ c*k + sqrt(2)*g/(c*k)
omega_- ~ c*k - sqrt(2)*g/(c*k)
omega_beat = omega_+ - omega_- = 2*sqrt(2)*g/(c*k)                 (16)
```

[DERIVED] The beat frequency is k-dependent: lower k = larger beat.

### 4.3 Beat Energy Density at Hubble Scale

One quantum per Hubble-scale mode of the beat frequency:
```
rho_beat = hbar * omega_beat(k_H) * k_H^3 / (16*pi^3)             (17)
```

**Step-by-step simplification** [DERIVED]:

Step 1: omega_beat at k_H = 2*pi/L_H:
```
omega_beat = 2*sqrt(2)*g / (c*k_H) = omega_gap^2*L_H/(2*pi*c)     (18)
```
(using g = omega_gap^2/(2*sqrt(2)))

Step 2: Substitute into (17):
```
rho_beat = hbar * [omega_gap^2*L_H/(2*pi*c)] * [(2*pi/L_H)^3] / (16*pi^3)
         = hbar * omega_gap^2 / (4*pi*c*L_H^2)                    (19)
```

Step 3: Convert to mass density (/c^2):
```
rho_beat = hbar * omega_gap^2 / (4*pi*c^3*L_H^2)                  (20)
```

Step 4: Substitute omega_gap = m_P*c^2/hbar:
```
rho_beat = m_P^2*c / (4*pi*hbar*L_H^2)                            (21)
```

Step 5: Substitute m_P^2 = hbar*c/G:
```
rho_beat = c^2 / (4*pi*G*L_H^2)                                   (22)
```

Step 6: Compare to critical density:
```
rho_crit = 3*H_0^2/(8*pi*G) = 3*c^2/(8*pi*G*L_H^2)               (23)
```

Step 7: Take ratio:
```
Omega_beat = rho_beat/rho_crit = [c^2/(4*pi*G*L_H^2)] / [3*c^2/(8*pi*G*L_H^2)]
           = 8*pi / (4*pi*3) = 2/3                                 (24)
```

### KEY RESULT:

```
Omega_beat = 2/3 = 0.6667    [EXACT, from two-phase beat structure]
Omega_Lambda(observed) = 0.6847
Discrepancy: 2.6%
```

**PDTP Original.** The factor 2/3 comes from the mathematical structure of one quantum
per Hubble-scale mode of the beat frequency between two dispersion branches.

**Caveats:**
1. Equation (22) contains G and L_H = c/H_0. NOT a G-free prediction.
2. This is a CONSISTENCY CHECK: if dark energy is one beat quantum per Hubble mode,
   the two-phase structure predicts Omega ~ 2/3.
3. The 2.6% discrepancy could come from matter corrections (Omega_matter ~ 0.315
   changes the effective Hubble radius).

**SymPy verification:** Omega_beat = 0.666667 (numerical), exact = 2/3 (analytical).

### 4.4 Mode Splitting Reframe (replaces beat frequency interpretation)

**PDTP Original.** ChatGPT insight: reframe "beat frequency" as "normal mode splitting."

The two-phase Lagrangian produces two coupled modes. In the normal mode basis:

```
phi_+ (bulk/gravity):    omega_+^2 = c^2*k^2                       (26a)
phi_- (boundary/interface): omega_-^2 = c^2*k^2 + 2*kappa          (26b)
```

where the effective coupling is:
```
kappa_PDTP = 2*sqrt(2)*g = omega_gap^2                              (27)
```

[DERIVED] **kappa is NOT a free parameter** -- it is omega_gap^2, fully determined by
the Lagrangian coupling constant g.

**Mapping to ChatGPT's linear model:**

| ChatGPT | PDTP |
|---------|------|
| kappa (free param) | kappa = omega_gap^2 [DERIVED] |
| omega_0 (base freq) | c*k (free field) |
| Both modes stable | One stable (breathing) + one unstable (Jeans) |
| Splitting Delta_omega = kappa/omega_0 | Delta_omega ~ omega_gap (strong coupling) |

**Coupling regime at Hubble scale:**
```
kappa / omega_0^2(k_H) = omega_gap^2 / (c*k_H)^2 ~ 1.8e120       (28)
```

This is **STRONG coupling** (kappa >> omega_0^2), not weak. The "small Lambda from
small kappa" argument does NOT apply. The smallness of Lambda comes from evaluating
at the Hubble scale k_H, not from small kappa.

**Conclusion:** Mode splitting and beat frequency give the SAME numerical result
(Omega = 2/3) because in strong coupling, Delta_omega ~ omega_gap. The reframe
is conceptually cleaner (structural mode splitting, not tuned beat) but
mathematically equivalent.

[DERIVED] Mode splitting reframe confirmed. Omega = 2/3 unchanged.

---

## 5. Phase C: Interface Energy

Domain wall (bulk/surface interface) energy density [SPECULATIVE]:
```
sigma ~ hbar*c/xi^2   (energy per area, xi = healing length)
rho_interface = sigma/L_H = hbar*c/(xi^2*L_H) ~ 10^27 * rho_Lambda
```
[SPECULATIVE] Interface energy is 27 decades too large. Not the right mechanism.

Geometric mean scale [from Part 54]:
```
L_eff = sqrt(l_P * L_H) = 47 microns
rho(L_eff) ~ 12 * rho_Lambda                                       (25)
```
[DERIVED] Within 1.1 decades -- consistent with CKN bound.

---

## 6. Sudoku Consistency Tests

15/15 PASS. Key tests:
- CC2-S1: rho_Planck definition (exact)
- CC2-S2: Hierarchy ~ 10^122 (exact)
- CC2-S3: CKN bound (within 1.5 decades)
- CC2-S4: T_00(vacuum, phi_-=0) = 0 (exact)
- CC2-S5: U(1) shift preserved (exact)
- CC2-S6: phi_- flat direction (exact)
- CC2-S7-S9: Dispersion relations (exact)
- CC2-S10: phi_- ZPE ~ rho_Planck (expected)
- CC2-S13: phi_- mass near matter = sqrt(2g) (exact)
- CC2-S14: Newton's 3rd law preserved (exact)

---

## 7. Summary and Conclusions (updated per ChatGPT review)

### What Holds [DERIVED]:
1. Two-phase T_mu_nu = T_kin - V (SymPy verified)
2. U(1) shift preserves (psi - phi_+) but NOT phi_-
3. phi_- is Goldstone-like at equilibrium (flat direction, massless in vacuum)
4. Two dispersion branches: omega^2 = c^2*k^2 +/- 2*sqrt(2)*g
5. Jeans wavelength = 2*pi*l_P
6. Mode splitting kappa = omega_gap^2 [derived from Lagrangian, NOT free]
7. Density scaling rho ~ c^2/(4*pi*G*L_H^2) = (2/3)*rho_crit

### Status Tags:
- [DERIVED] Two-phase field structure, dispersion, mode splitting, kappa
- [CONSISTENCY RELATION] Omega = 2/3 (uses G and H_0 as inputs; not a prediction)
- [REJECTED] "Beat frequency = dark energy" (121 orders off at Hubble scale)
- [REJECTED] Interface energy = Lambda (27 decades too large)
- [ANSATZ] "One quantum per Hubble mode" (not derived from Lagrangian)
- [CANDIDATE] phi_- as dark energy field (correct DOF, mechanism unproven)

### What the real physics is:
Two-phase Lagrangian produces two dispersion branches (mode splitting).
The low-energy branch (phi_-) evaluated at cosmological scale gives a density
scaling rho ~ 1/(G*L_H^2), yielding Omega ~ O(1), specifically 2/3.
This is already better than standard QFT (which gives 10^122).
The 2/3 is a consistency relation, not yet a prediction.

### Negative Results:
- phi_- naive ZPE = rho_Planck (CC problem NOT solved by two-phase alone)
- Beat frequency at Hubble scale is 121 orders off H_0 [REJECTED]
- "One quantum per Hubble mode" is an ANSATZ, not derived
- Interface energy 27 decades too large [REJECTED]

### Open Questions (critical next steps):
1. **Derive phi_- mode occupation from first principles** — WHY does phi_- populate
   modes at Hubble scale? The "one quantum per mode" assumption MUST be derived or abandoned.
2. Can H_0 be derived from PDTP? (would upgrade Omega = 2/3 to a true prediction)
3. Does the 2.6% discrepancy have a systematic origin (matter corrections)?
4. Is there a non-perturbative mechanism that suppresses phi_- ZPE below rho_Planck?

### Comparison to Standard Physics:

| Approach | Omega_Lambda | Free parameters |
|----------|-------------|----------------|
| Standard QFT (naive) | ~10^122 | zero (prediction fails) |
| Part 54 PDTP (single-phase) | free parameter | Lambda itself |
| Part 68 PDTP (two-phase beat) | 2/3 = 0.667 | G, H_0 |
| Observed | 0.685 +/- 0.007 | -- |

---

## 8. References

- Peskin & Schroeder (1995), "An Introduction to Quantum Field Theory", sec 2.2, 11.4
- Weinberg (1989), "The Cosmological Constant Problem", Rev.Mod.Phys. 61, 1
- Cohen, Kaplan, Nelson (1999), "Effective Field Theory, Black Holes, and the Cosmological Constant", Phys.Rev.Lett. 82, 4971
- Goldstone (1961), Nuovo Cimento 19, 154
- Planck Collaboration (2018), A&A 641, A6
- PDTP Part 61: two_phase_lagrangian.py (Euler-Lagrange derivation)
- PDTP Part 62: reversed_higgs.py (phi_- environment-dependent mass)
- PDTP Part 54: cosmo_constant.py (original FCC, Lambda = free parameter)

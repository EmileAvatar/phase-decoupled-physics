# Scale-Selection Mechanism for Lambda (Part 69)

**Method:** Three-path investigation of scale selection in two-phase Lagrangian
**Status:** NEGATIVE RESULT -- all paths fail; H_0 confirmed as 2nd free parameter
**Script:** `simulations/solver/scale_selection.py` (Phase 38)
**Previous:** Part 68 (`cosmo_constant_v2.py`) -- Omega = 2/3 [CONSISTENCY RELATION]
**Date:** 2026-03-20

---

## 1. Motivation

Part 68 showed that the two-phase Lagrangian gives Omega_beat = 2/3 (2.6% from observed 0.685).
But this requires evaluating at the Hubble scale k_H = 2*pi/L_H, with H_0 as input.

ChatGPT correctly diagnosed: **"No mechanism selects the scale k ~ H_0."**

ChatGPT proposed fix: add -(lambda/2)(nabla phi_-)^2 - (beta/4)*phi_-^4

This Part investigates:
1. Does the EXISTING Lagrangian already select a scale? (sine-Gordon analysis)
2. Is ChatGPT's quartic proposal valid?
3. Can Jeans instability provide the scale?

---

## 2. Path A: phi_- Equation of Motion Classification

### 2.1 Exact EOM (from Part 61, with spatial gradients)

Starting from the two-phase Lagrangian [ASSUMED]:
```
L = phi_+_dot^2 + phi_-_dot^2 + (1/2)*psi_dot^2
    - c^2*(nabla phi_+)^2 - c^2*(nabla phi_-)^2 - (c^2/2)*(nabla psi)^2
    + 2*g*sin(psi - phi_+)*sin(phi_-)                                    (1)
```

Euler-Lagrange for phi_- [DERIVED, Part 61, SymPy verified]:
```
phi_-_tt - c^2*nabla^2(phi_-) = 2*g*sin(psi - phi_+)*cos(phi_-)        (2)
```

Define delta = psi - phi_+ (matter-gravity phase mismatch).

### 2.2 Vacuum case (delta = 0)

```
phi_-_tt - c^2*nabla^2(phi_-) = 0                                       (3)
```

[DERIVED] **Free wave equation. NO scale selection in vacuum.**

This is the fundamental problem: phi_- is a massless free field in vacuum.
No potential, no preferred wavelength, no scale.

### 2.3 Matter present (delta != 0)

With uniform matter background (delta = const):
```
phi_-_tt - c^2*nabla^2(phi_-) = 2*g*sin(delta)*cos(phi_-)              (4)
```

[DERIVED] **This is a cosine-Gordon equation.**

### 2.4 Mapping to sine-Gordon

**PDTP Original.** Shift variable: chi = phi_- - pi/2. Then:

```
cos(chi + pi/2) = -sin(chi)                                             (5)
```

[DERIVED, SymPy VERIFIED] Residual = 0.

So equation (4) becomes:
```
chi_tt - c^2*nabla^2(chi) = -2*g*sin(delta)*sin(chi)                   (6)
```

[DERIVED] **Standard sine-Gordon equation** with mass parameter:
```
mu^2 = 2*g*sin(delta)                                                   (7)
```

**Source:** Rajaraman (1982), "Solitons and Instantons", Chapter 5

### 2.5 Sine-Gordon characteristic scales

The sine-Gordon equation has well-known solutions:

**Kink (topological soliton):**
```
phi(x) = 4*arctan(exp(x/L_kink))
L_kink = c / sqrt(mu^2) = c / sqrt(2*g*sin(delta))                     (8)
```

At maximal mismatch (delta = pi/2, sin(delta) = 1):
```
L_kink = c / sqrt(2g) = 2^(1/4) * hbar/(m_cond*c) = 2^(1/4) * l_P    (9)
```

Numerical: L_kink = 1.922e-35 m, ratio L_kink/l_P = 1.189

[DERIVED] **Kink width is Planck scale. NOT cosmological.**

**Breather (oscillating bound state):**
```
phi(x,t) = 4*arctan[sin(omega*t) * sech(mu*x) / (omega/mu_rest)]
```

where omega < mu_rest is a free parameter. The breather size:
```
L_breather ~ 1 / (mu_rest * sqrt(1 - omega^2/mu_rest^2))              (10)
```

- Minimum size (omega -> 0): L_breather = L_kink ~ l_P
- Maximum size (omega -> mu_rest): L_breather -> infinity

[DERIVED] **Breather family is continuous.** No preferred scale.
Any wavelength is allowed; sine-Gordon does not select one.

**Source:** Rubinstein (1970), J.Math.Phys. 11, 258

### 2.6 Could delta be tuned to give L_H?

From equation (8), requiring L_kink = L_H:
```
sin(delta) = c^2 / (2*g*L_H^2) = 1.96e-122                            (11)
```

[DERIVED] This number IS the cosmological constant problem:
sin(delta) ~ rho_Lambda/rho_Planck ~ 10^-122.

The phi_- kink width equals L_H only if the matter-gravity mismatch is
tuned to 10^-122. This is not scale selection -- it's the hierarchy problem
in disguise.

---

## 3. Path A (continued): Coupled System

### 3.1 Delta equation of motion

**PDTP Original.** From the psi and phi_+ equations:
```
psi_ddot = -2g*cos(phi_-)*sin(delta)
phi_+_ddot = -2g*cos(delta)*sin(phi_-)
```

Subtract:
```
delta_ddot = psi_ddot - phi_+_ddot
           = -2g*[cos(phi_-)*sin(delta) - cos(delta)*sin(phi_-)]
           = -2g*sin(delta - phi_-)                                     (12)
```

[DERIVED, SymPy VERIFIED]

With spatial gradients:
```
delta_tt - c^2*nabla^2(delta) = -2g*sin(delta - phi_-)                 (13)
```

### 3.2 Full coupled system

```
delta_tt - c^2*nabla^2(delta) = -2g*sin(delta - phi_-)                 (13)
phi_-_tt - c^2*nabla^2(phi_-) = 2g*sin(delta)*cos(phi_-)               (4)
```

[PDTP Original] This is a coupled sine-Gordon-like system.

Note: delta = psi - phi_+ is a DERIVED variable (not a Lagrangian coordinate).
Its dynamics come from combining two separate Euler-Lagrange equations,
not from a single potential. This means standard Lagrangian analysis
(Noether theorem, etc.) does not directly apply to delta.

### 3.3 Does coupling introduce a new scale?

The coupled system has:
- The same mass parameter mu^2 = 2g (at maximal mismatch)
- The same kink/breather solutions (perturbed by coupling)
- No new length scale beyond l_P

[DERIVED] **Coupling does NOT introduce a new scale.**

---

## 4. Path B: Effective Potential Analysis

### 4.1 Taylor expansion of the coupling potential

The coupling potential [DERIVED]:
```
V = 2*g*sin(delta)*sin(phi_-)                                          (14)
```

Expand sin(phi_-) around phi_- = 0:
```
sin(phi_-) = phi_- - phi_-^3/6 + phi_-^5/120 - phi_-^7/5040 + ...     (15)
```

[DERIVED] **Only ODD powers of phi_-.** No phi_-^2, no phi_-^4.

This means:
```
V = 2*g*sin(delta) * [phi_- - phi_-^3/6 + phi_-^5/120 - ...]          (16)
```

- Linear term: 2*g*sin(delta)*phi_- (mass-like, but linear not quadratic)
- Cubic: -(g*sin(delta)/3)*phi_-^3
- Quintic: (g*sin(delta)/60)*phi_-^5

### 4.2 Assessment of ChatGPT's quartic proposal

ChatGPT proposed adding -(beta/4)*phi_-^4 to the Lagrangian.

**Problem 1: Gradient term is redundant.**
The kinetic term phi_-_dot^2 - c^2*(nabla phi_-)^2 already contains
the spatial gradient. Adding another -(lambda/2)(nabla phi_-)^2 would
change the propagation speed of phi_-, not add new physics.

**Problem 2: Quartic is not generated by the sine coupling.**
The Taylor expansion (15) produces only odd powers. A phi_-^4 term
would need a separate physical origin.

**Problem 3: Scale selection requires NEGATIVE mass-squared.**
The formula k_*^2 ~ m_-^2/lambda requires m_- != 0.
In vacuum (delta = 0), m_- = 0 (flat direction, Part 62/68).
So k_* = 0: no scale selection in vacuum.

Even with a quartic added, a Mexican hat potential V = -mu^2*phi^2/2 + lambda*phi^4/4
requires mu^2 > 0 (tachyonic mass). But PDTP phi_- has m^2 >= 0 always
(reversed Higgs: massless in vacuum, massive near matter).

[DERIVED] **ChatGPT's quartic proposal is insufficient for scale selection.**

### 4.3 Coleman-Weinberg mechanism

Could quantum corrections generate a Mexican hat?

Coleman-Weinberg (1973): 1-loop corrections to a classically massless scalar
can generate symmetry breaking with VEV:
```
VEV ~ Lambda_UV * exp(-const/lambda)                                    (17)
```

For PDTP:
- Lambda_UV = 1/l_P (Planck cutoff)
- lambda ~ O(1) (strong coupling from sine nonlinearity)
- VEV ~ l_P (Planck scale, not Hubble)

[DERIVED] **Coleman-Weinberg gives Planck-scale VEV, not Hubble.**

**Source:** Coleman & Weinberg (1973), Phys.Rev.D 7, 1888

---

## 5. Path C: Jeans Instability

### 5.1 PDTP Jeans scale

From Part 68 [DERIVED]:
```
k_J = omega_gap / c = m_cond*c/hbar = 1/l_P                           (18)
lambda_J = 2*pi/k_J = 2*pi*l_P = 1.016e-34 m                          (19)
```

[DERIVED] **PDTP Jeans wavelength is Planck scale.**

### 5.2 Cosmological Jeans (standard physics)

With c_s = c (Part 34) and rho = rho_crit:
```
lambda_J = c * sqrt(pi/(G*rho_crit))
         = c * sqrt(8*pi^2 / (3*H_0^2))
         = sqrt(8*pi^2/3) * L_H
         = 5.13 * L_H                                                  (20)
```

[DERIVED] lambda_J ~ L_H. **But this is CIRCULAR** -- it uses H_0
through rho_crit = 3*H_0^2/(8*pi*G).

This is just the Hubble scale rewritten, not derived.

---

## 6. Synthesis: All Internal PDTP Scales

| Scale | Value (m) | Ratio to l_P | Source |
|-------|-----------|-------------|--------|
| l_P (Planck length) | 1.616e-35 | 1.00 | Standard |
| a_0 = hbar/(m_P*c) | 1.616e-35 | 1.00 | Part 29 |
| xi = l_P/sqrt(2) | 1.143e-35 | 0.71 | Part 33 |
| L_kink = c/sqrt(2g) | 1.922e-35 | 1.19 | Part 69 [NEW] |
| lambda_J = 2*pi*l_P | 1.016e-34 | 6.28 | Part 68 |
| **L_H (Hubble, EXTERNAL)** | **1.373e+26** | **8.49e+60** | Observation |

[DERIVED] **All five internal scales are within factor 10 of l_P.**
The Hubble radius is 60 orders of magnitude away.

The two-phase Lagrangian has ONE mass scale: m_cond.
All internal lengths ~ hbar/(m_cond*c).
The Hubble scale requires a SECOND mass scale:
```
m_DE = hbar*H_0/c^2 = 1.44e-33 eV                                     (21)
```

This IS the known dark energy mass scale. PDTP does not produce it.

---

## 7. Sudoku Consistency Tests

10/10 PASS. Key tests:
- SS-S1: phi_- EOM -> cosine-Gordon (SymPy shift identity)
- SS-S2: L_kink/l_P = 1.19 (expected ~1)
- SS-S3: sin(delta) for L_kink = L_H: 1.96e-122 (<<1, = CC hierarchy)
- SS-S5: delta EOM SymPy verified
- SS-S6: sin(phi_-) expansion: only odd powers (no quartic)
- SS-S8: Cosmo Jeans/L_H = 5.13 (exact, but circular)
- SS-S9: m_DE = 1.44e-33 eV (observed dark energy scale)
- SS-S10: All internal scales within [0.1, 100]*l_P

---

## 8. Summary and Conclusions

### NEGATIVE RESULT

The two-phase Lagrangian does NOT select the Hubble scale from its own parameters.

### What we proved:

1. **phi_- EOM = cosine-Gordon** (via chi = phi_- - pi/2 shift) [PDTP Original]
2. **Kink width L_kink = 2^(1/4) * l_P ~ 1.19 * l_P** [DERIVED]
3. **Breather family is continuous** (no preferred scale) [DERIVED]
4. **sin(delta) = 10^-122 to get L_kink = L_H** (hierarchy problem restated) [DERIVED]
5. **delta EOM: delta_ddot = -2g*sin(delta-phi_-)** [PDTP Original, SymPy verified]
6. **Sine expansion gives only odd powers** (no phi_-^4 from coupling) [DERIVED]
7. **ChatGPT quartic: insufficient** (needs negative mass-squared) [DERIVED]
8. **Coleman-Weinberg: VEV at Planck scale** (not Hubble) [DERIVED]
9. **Cosmological Jeans ~ L_H but circular** (uses H_0 through rho_crit) [DERIVED]

### Status tags:
- [DERIVED] phi_- EOM classification as cosine-Gordon
- [DERIVED] Coupled (delta, phi_-) system
- [DERIVED] All internal scales ~ l_P
- [NEGATIVE] Scale selection from existing Lagrangian
- [NEGATIVE] ChatGPT quartic proposal (needs tachyonic mass)
- [NEGATIVE] Coleman-Weinberg (Planck-scale VEV)
- [NEGATIVE] Jeans saturation (circular)

### Free parameters in PDTP (confirmed):
1. **m_cond** (equivalently G = hbar*c/m_cond^2)
2. **H_0** (equivalently Lambda or L_H)

Same as GR: G and Lambda are both free parameters of the theory.

### What would change this:
- A second mass scale m_2 ~ 10^-33 eV derivable from m_cond
- A non-perturbative mechanism (instantons, tunneling) selecting L_H
- A cosmological boundary condition built into the Lagrangian
- A connection between m_cond and the cosmological horizon

---

## 9. References

- Rajaraman (1982), "Solitons and Instantons", North-Holland
- Rubinstein (1970), J.Math.Phys. 11, 258
- Coleman & Weinberg (1973), Phys.Rev.D 7, 1888
- Coleman (1975), Phys.Rev.D 11, 2088
- Cuevas-Maraver et al. (2014), "The sine-Gordon Model and its Applications"
- Peskin & Schroeder (1995), sec 11.4
- PDTP Part 61: two_phase_lagrangian.py
- PDTP Part 62: reversed_higgs.py
- PDTP Part 68: cosmo_constant_v2.py

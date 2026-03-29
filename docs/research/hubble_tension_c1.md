# Hubble Tension — C1 FCC (Part 88)

**Status:** NEGATIVE (confirmed) — CLOSED
**Script:** `simulations/solver/hubble_tension_c1.py` (Phase 58)
**Sudoku:** 12/12 PASS
**Date:** 2026-03-29

---

## Summary

The Hubble tension is an 8.4% (5-sigma) disagreement between two independent
measurements of the present-day Hubble constant H_0:

- CMB (Planck 2020): H_0^CMB = 67.4 km/s/Mpc
- Cepheid distances (Riess+2022): H_0^SH0ES = 73.04 km/s/Mpc

This Part is a Forced Checklist Check using all PDTP findings through Part 87.
Five mechanisms are tested. All fail. The failure is informative: it pinpoints
a specific missing term (phi_-^4 quartic potential) and a specific observable
(DESI w(z) data) that could distinguish the two scenarios.

**Plain English:** Two telescopes disagree on the universe's expansion rate by
8%. PDTP cannot explain this gap. We tried five independent approaches. The
closest candidate — the phi_- dark energy field from Part 87 — is stuck at
w = -1 (acts like a cosmological constant, not a dynamical field) and is also
nine orders of magnitude too weak in energy. BUT this tells us exactly what
PDTP is missing: a quartic phi_-^4 correction to the condensate potential.

---

## 1. Problem Statement

### Observed tension [ASSUMED]

```
H_0^CMB   = 67.4 km/s/Mpc   [Planck 2020, CMB+LCDM]           ... (88.0a)
H_0^SH0ES = 73.04 km/s/Mpc  [Riess+2022, Cepheids+SH0ES]       ... (88.0b)
Delta_H_0 = 5.64 km/s/Mpc  (8.4% tension, ~5 sigma)
```

**Source:** Planck Collaboration (2020), Riess et al. (2022)

### LCDM Hubble parameter [ASSUMED]

```
H(z)^2 = H_0^2 [Omega_R*(1+z)^4 + Omega_M*(1+z)^3 + Omega_L]   ... (88.0c)
```

Standard values used:
- Omega_M = 0.3111 (matter)
- Omega_L = 0.6889 (Lambda)
- Omega_R = 9.13e-5 (radiation)
- Omega_total = 1.0000 (flat universe)

### Prior PDTP work (Part 16)

Two mechanisms were tested in Part 16:
1. G-drift dark energy: ~9 orders too small
2. Early-time acceleration: ~9 orders too small

This Part reexamines with new findings: two-phase Lagrangian (Part 61),
phi_- reversed Higgs (Part 62), phi_- dark energy (Parts 68-69), Lambda
reframe (Part 87), biharmonic GR (Part 86).

### What resolution requires

Early Dark Energy (EDE) models (Poulin et al. 2019) need:
```
delta_rho_EDE / rho_total(z~3000) ~ 10%                          ... (88.0d)
w_EDE > -1  transiently at z ~ 3000 (then w -> -1)
```

This decreases the sound horizon r_s by ~4%, shifting H_0^CMB up by ~4-8%.

---

## 2. Approach A — phi_- as Early Dark Energy

### Setup [ASSUMED from Part 61]

The phi_- field has equation of motion in FRW background:

```
phi_-_ddot + 3*H(z)*phi_-_dot + m_phi_-^2(z)*phi_- = 0           ... (88.1)
```

From Part 62 (reversed Higgs):
```
m_phi_-^2 = 0   in vacuum (massless)                              ... (88.2a)
m_phi_-^2 = 2*g*Phi   near matter (small in radiation era)        ... (88.2b)
```

### Slow-roll analysis [DERIVED]

In vacuum, Eq. (88.1) reduces to:
```
phi_-_ddot + 3*H*phi_-_dot = 0                                    ... (88.3)
```

General solution: `phi_-_dot ~ a(t)^-3` — decays with expansion.

In the overdamped limit where `3H >> m_phi_-`, phi_- is frozen:
```
phi_-(t) = phi_-_vac = const   (overdamped, m=0 in vacuum)        ... (88.4)
```

Since `m_phi_- = 0` exactly, the field is strictly frozen at all times in
vacuum. The equation of state:
```
w_phi_- = (KE - PE)/(KE + PE)
        = (phi_-_dot^2/2 - V)/(phi_-_dot^2/2 + V)                 ... (88.5)
```

With `phi_-_dot = 0` (frozen): `w_phi_- = -1` exactly. [DERIVED]

This means phi_- acts identically to a cosmological constant — it CANNOT
produce the transient `w > -1` spike required by EDE models.

### Energy density comparison [COMPUTED]

```
rho_total(z=3000) = 3*H(z=3000)^2 / (8*pi*G) = 1.358e-16 kg/m^3  ... (88.6a)
rho_EDE_required  = 10% * rho_total(z=3000)   = 1.358e-17 kg/m^3  ... (88.6b)
rho_phi_-(z=3000) = rho_Lambda                = 6.021e-27 kg/m^3  ... (88.6c)
```

(phi_- is frozen so rho_phi_- = rho_Lambda at all z.)

```
Ratio: rho_phi_- / rho_EDE_req = 4.4e-10   (9.4 orders deficit)  ... (88.6d)
```

**Verdict: NEGATIVE** — phi_- is both frozen (w=-1) and 9.4 orders too
low in energy density. Two independent reasons for failure.

Plain English: The phi_- field is like a frozen statue — it never moves, so
it can't produce the early dark energy burst needed to shift H_0. And even
if it could move, it's 10 billion times weaker than needed.

---

## 3. Approach B — Time-Varying G from phi_- Back-reaction

### Setup [DERIVED from Part 33]

PDTP gives:
```
G = hbar*c / m_cond^2                                             ... (88.7)
```

G is fixed by m_cond, which is the condensate particle mass — a constant
of the condensate. phi_- is a collective mode; m_cond is fundamental.

### Required G variation

For an 8% H_0 shift: delta_G/G ~ delta_H_0/H_0 ~ 8%.

This would require:
```
G_needed = G * (1 + 0.084) = 7.23e-11 m^3 kg^-1 s^-2             ... (88.8a)
m_cond_needed = sqrt(hbar*c/G_needed) = 2.09e-8 kg                ... (88.8b)
delta_m_cond/m_P = -3.9%                                          ... (88.8c)
```

### Why this fails

phi_- energy density << m_cond energy density by ~70 orders of magnitude.
phi_- has no coupling to m_cond in the current PDTP Lagrangian. m_cond
is not a dynamical field — it sets the condensate ground state energy.

**Verdict: NEGATIVE** — G is constant in PDTP; phi_- back-reaction is
negligible.

---

## 4. Approach C — Biharmonic GR Correction to Sound Horizon

### Biharmonic field equation [DERIVED from Part 61]

```
nabla^4*Phi + 4*g^2*Phi = 4*pi*G*rho   (biharmonic gravity)      ... (88.9)
```

This differs from Poisson (nabla^2*Phi = 4*pi*G*rho) only at scales r < r*,
where r* ~ l_P (Part 86 shows r* ~ l_P exactly).

### Correction to CMB sound horizon

The CMB sound horizon is:
```
r_s = 147.09 Mpc = 4.539e+24 m                                   ... (88.10a)
```

The biharmonic correction at scale r_s:
```
delta_H_0 / H_0 ~ (l_P / r_s)^2 = (1.616e-35 / 4.539e+24)^2
                = 1.27e-119                                        ... (88.10b)
```

Required correction: ~8%. Biharmonic provides: ~1e-117%.

Deficit: 118 orders of magnitude.

**Verdict: NEGATIVE** — biharmonic correction is 118 orders too small.

Plain English: The biharmonic correction only acts at distances smaller
than the Planck length (10^-35 m). The sound horizon is 10^24 m. The ratio
is 10^-59, squared = 10^-118. Completely negligible.

---

## 5. Reframe — Missing Physics Diagnosis

### Summary of all PDTP attempts

| Mechanism | Source | Deficit | Why it fails |
|-----------|--------|---------|-------------|
| G drift | Part 16 | ~9 orders | Too smooth |
| Early acceleration | Part 16 | ~9 orders | Too smooth |
| phi_- EDE | Parts 87+88 | 9.4 orders | Frozen (w=-1) AND too weak |
| phi_- -> G variation | Parts 33+88 | ~70 orders | Not coupled to m_cond |
| Biharmonic correction | Parts 86+88 | ~120 orders | Sub-Planck only |

The pattern: PDTP mechanisms are either dynamically frozen (w=-1) or
Planck-suppressed. Neither can produce a 10% energy perturbation at z=3000.

### What EDE models actually need [ASSUMED — Poulin+2019]

A scalar field phi with potential:
```
V(phi) ~ phi^n,  n > 2   (tracking attractor, w > -1)            ... (88.11)
```

The field must:
1. Contribute ~10% of total energy at z ~ 3000
2. Have w > -1 transiently (rolling phase)
3. Roll away after z ~ 3000, diluting faster than matter
4. Have a potential minimum at phi=0 with non-trivial mass

### What phi_- has vs what EDE needs

Current phi_- potential (from Part 61):
```
V(phi_-) = -2*g*cos(phi_-) ~ g*phi_-^2  [harmonic, w=-1]         ... (88.12a)
```

Quartic EDE potential (not in current PDTP):
```
V_EDE(phi_-) = g*phi_-^2 + lambda*phi_-^4  [tracking attractor]  ... (88.12b)
```

SymPy verification:
```
dV/dphi = 2*g*phi + 4*lam*phi^3  [EDE restoring force]           ... (88.12c)
```

The quartic term creates a tracking attractor and transient `w > -1`.
It is NOT in the current PDTP two-phase Lagrangian.

### Origin of quartic term (speculative)

The cosine potential `V = -2g*cos(phi_-)` contains ALL powers of phi_-:
```
-2g*cos(phi_-) = -2g + g*phi_-^2 - g*phi_-^4/12 + ...           ... (88.13)
```

The phi_-^4 term is already present with coefficient `-g/12`. However:
- Sign is NEGATIVE (stabilising, not tracking)
- Coefficient is too small (g/12 << g)
- Would need a positive quartic with coefficient ~ g to produce EDE

A positive quartic could arise from:
- Higher-order condensate corrections (beyond leading-order Lagrangian)
- Coupling to the gravitational condensate (phi_b) at second order
- SU(3) structure corrections (Part 37) modifying the effective potential

These require new physics beyond the current two-phase Lagrangian. [SPECULATIVE]

### Falsifiable prediction [PDTP Original, SPECULATIVE]

```
IF H_0 tension is real physics:
  PDTP predicts it requires phi_-^4 quartic extension             ... (88.14a)
  This would produce w(z) deviating from -1 at z ~ 3000
  Observable: DESI BAO + CMB-S4 joint constraints on w(z)

IF H_0 tension is Cepheid systematic error:
  PDTP requires no modification; phi_- remains harmonic           ... (88.14b)
```

The next 5-10 years of DESI + CMB-S4 data will distinguish these.

---

## 6. Sudoku Consistency Tests

| Test | Description | Result |
|------|-------------|--------|
| S1 | H_0^CMB = 67.4 km/s/Mpc [Planck 2020] | PASS |
| S2 | tension = (H_SH0ES - H_CMB)/H_CMB = 0.084 | PASS |
| S3 | Omega_total = Omega_M + Omega_L + Omega_R = 1.000 | PASS |
| S4 | phi_- frozen indicator = 1 (m=0 in vacuum) | PASS |
| S5 | rho_EDE_req = 10% * rho_total(z=3000) | PASS |
| S6 | rho_phi_-(z=3000) = rho_Lambda (frozen field) | PASS |
| S7 | phi_-_vac_EDE = sqrt(rho_EDE/g_phys) | PASS |
| S8 | G_needed = G*(1+tension_frac) for 8.3% H_0 shift | PASS |
| S9 | biharmonic correction = (l_P/r_s)^2 = 1.27e-119 | PASS |
| S10 | r_s = 147.09 Mpc = 4.539e+24 m | PASS |
| S11 | quartic EDE negligible today: 6*phi_vac^2 << 1 | PASS |
| S12 | EDE f_EDE ~ 10% required [literature] | PASS |

**Score: 12/12 PASS**

---

## 7. Conclusions

### C1 Verdict: NEGATIVE — CLOSED

All five PDTP mechanisms fail to explain the Hubble tension.

### New PDTP Original results

1. **phi_- EDE deficit precisely: 9.4 orders at z=3000** [PDTP Original]
   phi_- energy density / EDE requirement = 4.4e-10 at z=3000.

2. **phi_- strictly frozen in radiation era** [CONFIRMED, PDTP Original]
   m_phi_- = 0 in vacuum → phi_-_dot = 0 → w = -1 exactly (not approximation).

3. **EDE would need phi_-_vac ~ 5.41e-66 rad at z=3000** [PDTP Original]
   4.7 orders of magnitude larger than the cosmological constant value today.

4. **PDTP missing physics identified: phi_-^4 quartic term** [PDTP Original]
   Current cosine-Gordon potential has phi_-^4 but with wrong sign and coefficient.
   A positive quartic from higher-order condensate corrections could produce EDE.

5. **Falsifiable: DESI w(z) distinguishes the two scenarios** [PDTP Original]
   Hubble tension = systematics → PDTP fine as-is.
   Hubble tension = real physics → PDTP predicts phi_-^4 extension required.

### Connection to other Parts

- Part 16: First identified the 9-order deficit
- Part 61: Two-phase Lagrangian gives V(phi_-) = -2g*cos(phi_-) [harmonic]
- Part 62: phi_- massless in vacuum [reversed Higgs] — makes it frozen
- Part 87: Lambda = g*phi_-_vac^2 — phi_-_vac set by rho_Lambda
- Part 86: Biharmonic correction only at r < l_P — irrelevant at cosmological scales

The C1 result is consistent with and predicted by the combination of Parts 61+62+87.
The phi_- field is simultaneously the cosmological constant (Part 87) AND frozen (Part 62).
These two properties together make it impossible for phi_- to act as EDE.

---

## References

- Planck Collaboration (2020), "Planck 2018 results. VI. Cosmological parameters"
- Riess, A.G. et al. (2022), "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team"
- Poulin, V. et al. (2019), "Early Dark Energy can Resolve the Hubble Tension", Phys. Rev. Lett. 122, 221301
- **PDTP Parts 61, 62, 86, 87** (all PDTP Original)

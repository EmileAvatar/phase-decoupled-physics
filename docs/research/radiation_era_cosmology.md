# Radiation-Dominated Era Cosmology in PDTP

**Status:** PDTP Original analysis (builds on established cosmology)

This document derives PDTP's cosmological equations from condensate
dynamics, identifies where the radiation-era problem arises, and
presents the tight-coupling resolution.

**Prerequisites:** [photon_gravity_analysis.md](photon_gravity_analysis.md)
(free photon trace problem), [hard_problems.md](hard_problems.md) §2.11
(acoustic metric and PG representation).

---

## 1. Standard Cosmology Review

### 1.1 The Friedmann equations

In GR, a homogeneous isotropic universe with scale factor a(t) obeys:

```
(ȧ/a)² = (8πG/3) ρ_total − k/a²                             ... (1.1)

ä/a = −(4πG/3)(ρ + 3P/c²)                                    ... (1.2)
```

where ρ_total = ρ_m + ρ_r + ρ_Λ includes matter, radiation, and dark
energy.

**Source:** [Friedmann equations — Wikipedia](https://en.wikipedia.org/wiki/Friedmann_equations)

The energy conservation equation (from ∇_μ T^μν = 0):

```
dρ/dt + 3H(ρ + P/c²) = 0                                     ... (1.3)
```

gives ρ_m ∝ a⁻³ (matter, P = 0) and ρ_r ∝ a⁻⁴ (radiation, P = ρc²/3).

### 1.2 Key epochs

| Epoch | Redshift z | Dominant component | Key physics |
|-------|-----------|-------------------|-------------|
| Radiation era | > 3400 | ρ_r | H² ∝ ρ_r ∝ a⁻⁴ |
| Matter-radiation equality | ≈ 3400 | ρ_r = ρ_m | Transition |
| Matter era | 3400 to ~0.4 | ρ_m | H² ∝ ρ_m ∝ a⁻³ |
| Dark energy era | < ~0.4 | ρ_Λ | Accelerated expansion |

**Source:** [Lambda-CDM model — Wikipedia](https://en.wikipedia.org/wiki/Lambda-CDM_model)

### 1.3 How GR sees radiation

GR uses the full tensor Einstein equation G_μν = (8πG/c⁴) T_μν. For
a radiation fluid with energy density ρ_r:

```
T_00 = ρ_r                (nonzero)
T_ij = (ρ_r/3) δ_ij       (nonzero)
T = T^μ_μ = −ρ_r + ρ_r = 0   (trace is zero)
```

The (0,0) component of Einstein's equation gives the Friedmann equation
(1.1), which uses T_00 = ρ_r directly. The trace T = 0 is irrelevant
because GR is a tensor theory — it uses the full T_μν, not just T.

---

## 2. PDTP Cosmological Equations from Condensate Dynamics

### 2.1 The acoustic metric in cosmological form

**PDTP Original.** The PDTP acoustic metric (advanced_formalization.md
§1.4) is:

```
g_μν^acoustic = (ρ₀/c_s) ×
  [ −(c_s² − v²)   |  −v_j     ]
  [  −v_i           |   δ_ij    ]                              ... (2.1)
```

For a homogeneous, isotropic expanding universe, we set:

```
ρ₀ = ρ₀(t)          (time-dependent condensate density)
v_i = H(t) x_i      (Hubble flow)
c_s = c              (Lorentz-invariant condensate)
```

Substituting into (2.1):

```
ds²_acoustic ∝ −(c² − H²r²) dt² − 2Hr dt dr + dr² + r² dΩ²  ... (2.2)
```

**Source:** [Gullstrand-Painlevé coordinates — Wikipedia](https://en.wikipedia.org/wiki/Gullstrand%E2%80%93Painlev%C3%A9_coordinates)

This is the flat FRW metric in Painlevé-Gullstrand-like cosmological
coordinates. The standard FRW form ds² = −c²dt² + a²(t) dx² is
recovered by the coordinate transformation r → a(t) χ with
v = Hr = ȧχ.

**PDTP Original:** The Hubble expansion corresponds to the condensate
superfluid velocity field v_i = H(t) x_i. Cosmic expansion IS
condensate flow.

### 2.2 Condensate continuity equation

The condensate density satisfies the continuity equation:

```
∂ρ₀/∂t + ∇ · (ρ₀ v) = 0                                     ... (2.3)
```

**Source:** [Continuity equation — Wikipedia](https://en.wikipedia.org/wiki/Continuity_equation)

For homogeneous density ρ₀(t) and Hubble flow v = Hx:

```
∇ · (ρ₀ v) = ρ₀ ∇ · v = ρ₀ · 3H
```

So:

```
dρ₀/dt + 3H ρ₀ = 0                                           ... (2.4)
```

This gives ρ₀ ∝ a⁻³, meaning the condensate density dilutes like
non-relativistic matter under expansion. This is expected: the
condensate is a conserved fluid expanding in volume.

### 2.3 Condensate Euler equation

The irrotational superfluid condensate obeys the Euler equation:

```
∂v/∂t + (v · ∇)v = −(c²/ρ₀) ∇ρ₀ − ∇Φ_N                    ... (2.5)
```

where Φ_N is the Newtonian gravitational potential sourced by matter.

**Source:** [Euler equations (fluid dynamics) — Wikipedia](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics))

For homogeneous, isotropic flow v = H(t) x:

```
∂v/∂t = Ḣ x_i
(v · ∇)v = H² x_i
∇ρ₀ = 0   (homogeneous)
```

The gravitational potential for uniform matter density ρ_m:

```
∇²Φ_N = 4πG ρ_m   →   ∇Φ_N = (4πG/3) ρ_m x_i              ... (2.6)
```

**Source:** [Poisson's equation — Wikipedia](https://en.wikipedia.org/wiki/Poisson%27s_equation)

Substituting into (2.5):

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Ḣ + H² = −(4πG/3) ρ_m                          ... (2.7)  │
│                                                              │
│  This is the Raychaudhuri equation for pressureless matter.  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Raychaudhuri equation — Wikipedia](https://en.wikipedia.org/wiki/Raychaudhuri_equation)

### 2.4 The PDTP Friedmann equation (matter only)

Equation (2.7) can be integrated using the continuity equation (2.4).
Multiplying (2.7) by 2ȧ/a and using ρ_m ∝ a⁻³:

```
d/dt(H²) = d/dt(ȧ/a)² = 2(ä/a − H²)H = 2(−(4πG/3)ρ_m − H²)H
```

Using dρ_m/dt = −3Hρ_m, the energy integral gives:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  H² = (8πG/3) ρ_m − k/a²                        ... (2.8)  │
│                                                              │
│  The Friedmann equation for matter-dominated expansion.      │
│  k is an integration constant (spatial curvature).           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original:** PDTP correctly reproduces the matter-era Friedmann
equation from condensate dynamics alone, without invoking Einstein's
equations. The scalar field φ sources the Newtonian potential through
□φ = Σ gᵢ sin(ψᵢ − φ), and the condensate flow responds through
the Euler equation.

### 2.5 The missing radiation term

Comparing with the full GR Friedmann equation (1.1):

```
GR:   H² = (8πG/3)(ρ_m + ρ_r) − k/a²
PDTP: H² = (8πG/3) ρ_m        − k/a²                        ... (2.9)
```

**The radiation density ρ_r is absent from the PDTP scalar channel.**

This is because:
- The Poisson equation (2.6) has ρ_m as its source
- ρ_m comes from the PDTP field equation □φ = Σ gᵢ sin(ψᵢ − φ)
- Only massive matter (with de Broglie phase ψᵢ) appears
- Free radiation has T^EM = 0 and cannot source the scalar field

This is the cosmological manifestation of the trace problem analyzed
in [photon_gravity_analysis.md](photon_gravity_analysis.md).

---

## 3. The Tight-Coupling Resolution

### 3.1 Photon-baryon plasma before recombination

Before recombination (z > 1100), photons scatter off free electrons
via Thomson scattering with cross-section σ_T = 6.65 × 10⁻²⁹ m².

**Source:** [Thomson scattering — Wikipedia](https://en.wikipedia.org/wiki/Thomson_scattering)

The photon mean free path is:

```
λ_γ = 1/(n_e σ_T)                                            ... (3.1)
```

At redshift z, the electron density is:

```
n_e(z) = n_{e,0} (1+z)³ ≈ 0.22 (1+z)³ m⁻³                  ... (3.2)
```

**Source:** [Baryon density — Wikipedia](https://en.wikipedia.org/wiki/Baryon_asymmetry)

At key epochs:

| Epoch | z | n_e (m⁻³) | λ_γ (m) | t_scatter (s) | t_Hubble (s) |
|-------|---|-----------|---------|---------------|-------------|
| Recombination | 1100 | 2.9 × 10⁸ | 5.2 × 10¹⁹ | 1.7 × 10¹¹ | 1.2 × 10¹³ |
| Equality | 3400 | 8.6 × 10⁹ | 1.7 × 10¹⁸ | 5.8 × 10⁹ | 1.7 × 10¹² |
| BBN | 10⁹ | 2.2 × 10²⁶ | 6.8 × 10¹ | 2.3 × 10⁻⁷ | ~1 |
| Neutrino decoupling | 10¹⁰ | 2.2 × 10²⁹ | 6.8 × 10⁻² | 2.3 × 10⁻¹⁰ | ~0.01 |

The scattering time t_scatter = λ_γ/c is always much shorter than the
Hubble time t_Hubble = 1/H in the radiation-dominated era. The ratio:

```
t_scatter / t_Hubble ≪ 1   for all z > 1100                  ... (3.3)
```

This means photons are **tightly coupled to baryons** throughout the
entire radiation-dominated era.

### 3.2 Effective mass argument

**PDTP Original.** In the tightly coupled photon-baryon plasma, each
baryon interacts with photons on timescales far shorter than the
gravitational (Hubble) timescale. The photon energy is effectively
"carried by" the baryons.

Define the effective gravitational mass per baryon:

```
m_eff = m_b + (ρ_γ / n_b) / c²                               ... (3.4)
```

where ρ_γ/n_b is the photon energy per baryon.

The effective matter density entering the PDTP field equation is:

```
ρ_eff = n_b × m_eff × c² = n_b m_b c² + ρ_γ = ρ_b + ρ_γ    ... (3.5)
```

**This recovers the total energy density** ρ_total = ρ_b + ρ_γ.

The PDTP Friedmann equation with tight coupling becomes:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  H² = (8πG/3)(ρ_b + ρ_γ) − k/a²                ... (3.6)  │
│                                                              │
│  Matches the GR Friedmann equation when photon-baryon        │
│  plasma is tightly coupled (z > 1100).                       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 3.3 Physical justification

The effective mass argument is not ad hoc — it follows from the
equivalence of mass and energy (E = mc²). A baryon immersed in a
thermal photon bath absorbs and re-emits photons continually. At any
instant, the baryon's recent history of absorption means it carries
thermal energy above its rest mass. This excess energy gravitates.

More precisely: in the frame comoving with a baryon, the photon
field surrounding it contributes to the local stress-energy. In the
tight-coupling limit, this contribution is always associated with the
nearest baryon (it was absorbed/emitted within the last scattering
time, during which the baryon barely moved). So the photon energy
is assigned to specific massive particles, which DO source the PDTP
field equation.

### 3.4 Radiation pressure correction

In GR, the Raychaudhuri equation (1.2) includes a pressure term:

```
ä/a = −(4πG/3)(ρ + 3P/c²)                                    ... (1.2)
```

For radiation, P = ρ_r c²/3, so the effective source is ρ_r + 3P_r/c²
= 2ρ_r — radiation decelerates expansion twice as strongly as matter
of the same energy density.

In PDTP, the condensate Euler equation (2.5) must be modified to
include the pressure of the photon-baryon plasma:

```
∂v/∂t + (v · ∇)v = −(1/ρ_eff) ∇P_total − ∇Φ_N              ... (3.7)
```

For the homogeneous case, ∇P = 0 (spatial gradients vanish), so the
pressure term does not affect the Friedmann equation (2.8). But it
does affect the **Raychaudhuri equation** through the relativistic
correction:

```
Ḣ + H² = −(4πG/3)(ρ_eff + 3P_eff/c²)                        ... (3.8)
```

With the photon-baryon plasma: P_eff = ρ_γ c²/3 (radiation pressure
dominates), and ρ_eff = ρ_b + ρ_γ. In the radiation-dominated limit
(ρ_γ ≫ ρ_b):

```
ρ_eff + 3P_eff/c² ≈ ρ_γ + ρ_γ = 2ρ_γ                        ... (3.9)
```

This matches the GR result: radiation causes deceleration twice as
strong as pressureless matter.

**PDTP Original:** The pressure correction (3.8) enters naturally
through the condensate Euler equation when radiation pressure is
included. This requires the condensate to respond to the total
pressure of the matter + radiation system, which is physically
reasonable for a tightly coupled plasma.

---

## 4. Epoch-by-Epoch Analysis

### 4.1 BBN epoch (z ~ 10⁹, T ~ 1 MeV)

**Tight coupling:** t_scatter/t_Hubble ~ 10⁻⁷ — extremely tight.

**Effective mass:** ρ_γ/ρ_b ~ 6 × 10⁵ at this epoch. Each baryon
carries enormous photon energy, giving m_eff ≈ 6 × 10⁵ m_b.

**Neutrino complication:** At z ~ 10⁹, neutrinos have already
decoupled (ν decoupling at z ~ 10¹⁰, T ~ 1 MeV). Free-streaming
neutrinos contribute ρ_ν ≈ 0.68 ρ_γ (for 3 species) to the
expansion rate.

**Source:** [Cosmic neutrino background — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_neutrino_background)

In PDTP, neutrinos are massive fermions (m_ν ~ 0.05 eV), so they
have a de Broglie phase ψ_ν and CAN source the scalar field even
when free-streaming. However, at BBN temperatures (kT ~ 1 MeV ≫
m_ν c² ~ 0.05 eV), neutrinos are ultra-relativistic: their kinetic
energy dominates rest mass by a factor ~ 10⁷.

For ultra-relativistic neutrinos, the effective coupling is:

```
g_ν sin(ψ_ν − φ) where g_ν ∝ m_ν
```

The rest-mass coupling g_ν captures only m_ν c²/E_ν ~ 10⁻⁷ of
the neutrino's total energy. The kinetic energy, like photon energy,
does not enter the scalar source.

**Honest assessment:** The neutrino kinetic energy is a genuine gap.
The tight-coupling argument does not apply to decoupled neutrinos.
The missing ρ_ν contribution to the Friedmann equation is:

```
δH²/H² = ρ_ν / ρ_total ≈ 0.41 (for 3 ν species + photons)  ... (4.1)
```

This is a ~41% error in the expansion rate, which would significantly
affect BBN predictions (light element abundances depend sensitively
on H at T ~ 1 MeV).

**Source:** [Big Bang nucleosynthesis — Wikipedia](https://en.wikipedia.org/wiki/Big_Bang_nucleosynthesis)

### 4.2 Matter-radiation equality (z ≈ 3400)

**Tight coupling:** t_scatter/t_Hubble ~ 10⁻³ — still well-coupled.

**Effective mass:** ρ_γ ≈ ρ_b at equality, so m_eff ≈ 2 m_b.

With tight coupling, the PDTP Friedmann equation gives:

```
H² = (8πG/3)(ρ_b + ρ_γ + ρ_CDM)                             ... (4.2)
```

Here ρ_CDM (cold dark matter) enters through its own mass coupling
(dark matter is massive and sources φ normally). The photon
contribution enters through the effective mass argument.

**Neutrino contribution:** At equality, neutrinos are still
relativistic (kT ~ 0.9 eV, m_ν ~ 0.05 eV, ratio ~ 18). The
neutrino kinetic energy gap persists but is smaller:

```
δH²/H² = ρ_ν / ρ_total ≈ 0.10                               ... (4.3)
```

A ~10% error in H at equality would shift the matter-radiation
equality redshift and affect the CMB power spectrum shape.

### 4.3 Recombination (z ≈ 1100)

**Tight coupling breaks down:** Photons decouple from baryons as
electrons recombine with protons into neutral hydrogen.

After recombination:
- Photons free-stream (the CMB)
- ρ_γ/ρ_m ≈ 0.3 (photons still non-negligible but subdominant)

The effective mass argument no longer applies. But ρ_γ < ρ_m, so the
missing radiation term is a sub-leading correction:

```
δH²/H² = ρ_γ / (ρ_m + ρ_γ) ≈ 0.23 at z = 1100              ... (4.4)
```

This decreases rapidly: by z ~ 100, δH²/H² < 0.02.

### 4.4 Present universe (z = 0)

ρ_γ/ρ_total ≈ 5 × 10⁻⁵. The free photon problem is completely
negligible. PDTP Friedmann = GR Friedmann to better than 0.01%.

---

## 5. The Neutrino Problem

### 5.1 Statement

The tight-coupling argument resolves the photon contribution but
**does not resolve the neutrino contribution** in the radiation era.

Cosmic neutrinos decouple at z ~ 10¹⁰ and free-stream thereafter.
They are massive but ultra-relativistic in the early universe,
meaning their rest-mass coupling g_ν ∝ m_ν captures only a tiny
fraction of their total energy.

The missing neutrino energy density:

```
ρ_ν = N_eff × (7/8)(4/11)^{4/3} ρ_γ ≈ 0.68 ρ_γ             ... (5.1)
```

with N_eff = 3.044 (standard value for 3 neutrino species).

**Source:** [Neutrino decoupling — Wikipedia](https://en.wikipedia.org/wiki/Neutrino_decoupling)

### 5.2 Impact on BBN

BBN predictions depend on the expansion rate H during nucleosynthesis.
The helium-4 abundance Y_p is particularly sensitive:

```
Y_p ∝ (H / H_standard)^{1/2}                                 ... (5.2)
```

**Source:** [Big Bang nucleosynthesis — Wikipedia](https://en.wikipedia.org/wiki/Big_Bang_nucleosynthesis)

If PDTP's Friedmann equation is missing the neutrino contribution
(41% of ρ_total at BBN), the expansion rate would be:

```
H_PDTP / H_GR = √(1 − ρ_ν/ρ_total) ≈ √0.59 ≈ 0.77         ... (5.3)
```

This 23% reduction in H would significantly alter the neutron-to-
proton freeze-out ratio and predicted element abundances. This is
a quantitative conflict with observations.

### 5.3 Possible resolutions

**Resolution A: Neutrino effective mass at high T.** In a dense
plasma, neutrinos acquire an effective mass from interactions with
the thermal background (MSW effect generalization). If this effective
mass is large enough, the coupling g_ν,eff could capture the full
neutrino energy. However, the standard MSW potential is:

```
V_eff ∝ G_F n_e ∝ G_F T³                                     ... (5.4)
```

**Source:** [MSW effect — Wikipedia](https://en.wikipedia.org/wiki/Mikheyev%E2%80%93Smirnov%E2%80%93Wolfenstein_effect)

At BBN temperatures (T ~ 1 MeV): V_eff ~ 10⁻¹¹ eV. This is far too
small compared to kT ~ 10⁶ eV to serve as an effective gravitational
mass.

**Resolution B: Condensate response to neutrino stress-energy.**
Even if neutrinos don't source the scalar φ efficiently, their
stress-energy may affect the condensate density ρ₀ through the
full acoustic metric dynamics. If ρ₀ responds to ρ_ν, the metric
g_μν would see the neutrino contribution.

**Resolution C: Modified dispersion at high energy.** At energies
approaching the condensate scale, the effective field equation may
differ from the low-energy form. This connects to the condensate
microscopic structure (genuinely open problem).

**Resolution D: Accept as a regime limitation.** PDTP may be valid
only for matter-dominated physics, with the radiation era requiring
a UV completion. This is common for effective field theories.

---

## 6. Comparison with Brans-Dicke Cosmology

Brans-Dicke theory faces the same trace problem:

```
□Φ_BD = (8π / (2ω+3)) T                                      ... (6.1)
```

Since T^EM = 0 and T^ν ≈ 0 (ultra-relativistic), the BD scalar Φ
is not driven by radiation. However, BD cosmology works because:

1. The **tensor sector** (Einstein's equations with Φ-dependent G)
   handles radiation normally
2. The scalar provides only a small correction (suppressed by 1/ω)
3. For ω > 40,000 (Cassini bound), the scalar contribution to
   cosmology is < 10⁻⁵ of the tensor

**Source:** [Brans-Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)

**PDTP analog:** The acoustic metric provides a tensor-like sector
that could play the role of BD's tensor equations. In the PG
representation (hard_problems.md §2.11), the acoustic metric
reproduces the Schwarzschild geometry. If the cosmological acoustic
metric responds to radiation through the condensate equation of
state, PDTP could handle radiation similarly to BD.

The key difference: BD has GR's tensor equations explicitly built in.
PDTP must derive its tensor-like behavior from condensate dynamics.
This derivation exists for static fields (§2.11 of hard_problems.md)
but has not been carried out for cosmology.

---

## 7. Summary

### What has been derived

| Result | Type | Status |
|--------|------|--------|
| Matter-era Friedmann equation from condensate dynamics | **PDTP Original** | Rigorous derivation (§2) |
| Cosmic expansion = condensate Hubble flow | **PDTP Original** | Direct identification (§2.1) |
| ρ₀ ∝ a⁻³ from condensate continuity | **PDTP Original** | Follows from conservation (§2.2) |
| Raychaudhuri equation for matter | **PDTP Original** | From Euler equation (§2.3) |
| Tight-coupling resolves photon contribution | **PDTP Original** | Semi-quantitative (§3) |
| Radiation pressure correction in Euler equation | **PDTP Original** | Extends Raychaudhuri (§3.4) |
| Self-limiting property of photon problem | **PDTP Original** | From photon_gravity_analysis.md |

### What remains open

| Problem | Severity | Notes |
|---------|----------|-------|
| Decoupled neutrino energy at BBN | **High** | 41% of ρ_total missing; alters Y_p prediction |
| Neutrino energy at equality | Medium | 10% of ρ_total; shifts equality redshift |
| Post-recombination CMB contribution | Low | < 23% and decreasing |
| Full acoustic metric cosmology | Needed | Tensor channel may resolve neutrino problem |
| Condensate behavior at high T | Open | Phase transition could change effective eq. |

### Honest assessment

**PDTP can derive the correct matter-era Friedmann equation** from
condensate dynamics — a non-trivial result showing the framework
is cosmologically viable for the dominant epoch of structure formation.

The tight-coupling argument successfully resolves the photon
contribution throughout the radiation-dominated era (when photons are
always coupled to baryons) and becomes unnecessary after recombination
(when photons are subdominant).

The **genuine problem is neutrinos**: decoupled at z ~ 10¹⁰ but
ultra-relativistic until z ~ 100, their kinetic energy is not
captured by the rest-mass coupling. This creates a quantitative
conflict at BBN (~23% error in H) that requires resolution through
either condensate tensor dynamics or a fundamental extension of the
framework.

This places radiation-era PDTP cosmology in a similar position to
early Brans-Dicke theory: viable for matter-dominated epochs, with
the radiation era requiring the tensor sector (acoustic metric) to
carry the additional degrees of freedom.

---

## References

### Established Sources
1. [Friedmann equations — Wikipedia](https://en.wikipedia.org/wiki/Friedmann_equations)
2. [Lambda-CDM model — Wikipedia](https://en.wikipedia.org/wiki/Lambda-CDM_model)
3. [Raychaudhuri equation — Wikipedia](https://en.wikipedia.org/wiki/Raychaudhuri_equation)
4. [Thomson scattering — Wikipedia](https://en.wikipedia.org/wiki/Thomson_scattering)
5. [Continuity equation — Wikipedia](https://en.wikipedia.org/wiki/Continuity_equation)
6. [Euler equations (fluid dynamics) — Wikipedia](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics))
7. [Cosmic neutrino background — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_neutrino_background)
8. [Neutrino decoupling — Wikipedia](https://en.wikipedia.org/wiki/Neutrino_decoupling)
9. [Big Bang nucleosynthesis — Wikipedia](https://en.wikipedia.org/wiki/Big_Bang_nucleosynthesis)
10. [MSW effect — Wikipedia](https://en.wikipedia.org/wiki/Mikheyev%E2%80%93Smirnov%E2%80%93Wolfenstein_effect)
11. [Brans-Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)
12. [Thomson scattering cross-section — Wikipedia](https://en.wikipedia.org/wiki/Thomson_scattering)

### PDTP Original Results
1. Matter-era Friedmann equation from condensate Euler + continuity (§2)
2. Cosmic expansion identified as condensate Hubble flow (§2.1)
3. Tight-coupling resolution of photon contribution (§3.2–3.3)
4. Radiation pressure enters through modified Euler equation (§3.4)
5. Epoch-by-epoch quantitative assessment (§4)
6. Neutrino problem identified and quantified: 41% at BBN (§5.2)

---

End of radiation_era_cosmology.md

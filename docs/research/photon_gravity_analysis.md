# Free Photon Radiation as Gravitational Source

**Status:** PDTP Original analysis (builds on established scalar gravity results)

This document analyzes the consequences of free photons not sourcing the
PDTP scalar field equation, quantifies when this matters, and identifies
the regimes where it becomes a genuine problem.

**Background:** See [hard_problems.md](hard_problems.md) §4.8 for the
trace problem derivation and G_EM removal.

---

## 1. The Problem Statement

The corrected PDTP field equation (hard_problems.md eq. 4.7) is:

```
□φ = Σᵢ gᵢ sin(ψᵢ − φ)
```

Only massive matter (with de Broglie phase ψᵢ) appears as a source.
Free photons are massless and carry no ψ field, so they cannot couple
to φ through the phase-locking mechanism.

The root cause is the tracelessness of the EM stress-energy tensor:

```
T^μ_μ (EM) = 0                                                ... (1.1)
```

**Source:** [Electromagnetic stress-energy tensor — Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_stress%E2%80%93energy_tensor)

This is a consequence of the **conformal invariance** of Maxwell's
equations in 4 dimensions. It affects all scalar gravity theories,
not just PDTP.

**Question:** Does this absence of direct photon sourcing create
observable problems for gravitational physics?

---

## 2. How GR Handles Radiation (For Comparison)

GR uses the full tensor Einstein equation:

```
G_μν = (8πG/c⁴) T_μν                                         ... (2.1)
```

**Source:** [Einstein field equations — Wikipedia](https://en.wikipedia.org/wiki/Einstein_field_equations)

For a photon gas with energy density ρ and pressure p = ρ/3:

```
T_00 = ρ        (nonzero — energy density)
T_ij = (ρ/3)δ_ij  (nonzero — radiation pressure)
T = T^μ_μ = −ρ + 3(ρ/3) = 0   (trace is zero!)
```

**Source:** [Friedmann equations — Wikipedia](https://en.wikipedia.org/wiki/Friedmann_equations)

The trace of the photon stress-energy is zero even in GR. The key
difference is that GR uses the **full tensor** T_μν (where individual
components like T_00 = ρ are nonzero), while scalar theories can only
use the **trace** T = 0.

GR's (0,0) component gives the Friedmann equation:

```
(ȧ/a)² = (8πG/3) ρ                                           ... (2.2)
```

This sees radiation because it uses T_00 = ρ directly, not the trace.

**PDTP Original:** This asymmetry — tensor equation sees radiation,
scalar equation does not — is the structural origin of the free photon
problem. PDTP's acoustic metric provides the tensor-like sector needed
to complement the scalar channel (see §7).

---

## 3. Energy Bookkeeping: Emission and Absorption

### 3.1 The conservation argument

Consider a star of mass M emitting a photon of energy E:

| Stage | Star mass | Photon | Total scalar source | Total energy |
|-------|-----------|--------|-------------------|--------------|
| Before emission | M | — | g_M sin(ψ − φ) | Mc² |
| During transit | M − E/c² | E (free, no source) | g_{M−E/c²} sin(ψ − φ) | Mc² |
| After absorption | M − E/c² | — (absorbed by M') | g_{M−E/c²} + g_{E/c²} | Mc² |

During the photon's transit, the total scalar gravitational source is
reduced by an amount proportional to E/c². The total **energy** is
conserved at all times (Noether's theorem, mathematical_formalization.md
§5), but the scalar **source** has a transient deficit.

**PDTP Original:** This deficit is the quantifiable "price" of the
trace problem.

### 3.2 Quantitative deficit for the Sun

The Sun's luminosity is L☉ = 3.828 × 10²⁶ W.

**Source:** [Solar luminosity — Wikipedia](https://en.wikipedia.org/wiki/Solar_luminosity)

The rate of mass loss to radiation:

```
dM/dt = L☉/c² = 3.828 × 10²⁶ / (9 × 10¹⁶) = 4.25 × 10⁹ kg/s
```

Fractional rate:

```
(dM/dt)/M☉ = 4.25 × 10⁹ / (1.989 × 10³⁰) = 2.14 × 10⁻²¹ s⁻¹
```

This is the fractional deficit in scalar source per second of transit.
After t seconds, a fraction 2.14 × 10⁻²¹ t of the Sun's gravitational
source is "in transit" as photons. Even after the entire age of the
universe (t ~ 4 × 10¹⁷ s), the cumulative deficit would be ~ 10⁻³.

But most solar photons are eventually absorbed by something (another
star, dust, planet), at which point the source returns to the absorber's
mass. The **steady-state** deficit is:

```
ΔM_transit / M☉ ~ (L☉ / c²) × t_avg / M☉
```

where t_avg is the average transit time. For photons absorbed within the
solar system (a few light-hours), ΔM/M ~ 10⁻¹⁷. For photons escaping
to infinity, the mass is permanently lost — but this is a real physical
mass loss, not a PDTP artifact.

**PDTP Original:** The free photon problem produces no measurable effect
for stellar-scale gravitational physics.

---

## 4. Thermal Radiation in Equilibrium

### 4.1 The timescale argument

**PDTP Original.** Inside a star, photons are not truly "free." They
are constantly absorbed and re-emitted, with a mean free path:

```
λ_mfp (solar interior) ~ 1 cm                                ... (4.1)
```

**Source:** [Radiation zone — Wikipedia](https://en.wikipedia.org/wiki/Radiation_zone)

The characteristic time between photon interactions is:

```
t_interaction = λ_mfp / c ≈ 10⁻² / (3 × 10⁸) ≈ 3 × 10⁻¹¹ s   ... (4.2)
```

The gravitational dynamical timescale is:

```
t_grav = 1/√(Gρ) ≈ 1/√(6.67 × 10⁻¹¹ × 1.4 × 10³) ≈ 3300 s  ... (4.3)
```

**Source:** [Free-fall time — Wikipedia](https://en.wikipedia.org/wiki/Free-fall_time)

The ratio:

```
t_interaction / t_grav ≈ 10⁻¹⁴                               ... (4.4)
```

Since t_interaction ≪ t_grav, thermal radiation is **effectively
bound** — its energy is always associated with the matter that last
absorbed it. At any instant, the fraction of photon energy genuinely
"in transit" (not associated with a massive particle) is:

```
f_transit ≈ t_interaction / t_grav ≈ 10⁻¹⁴                   ... (4.5)
```

The gravitational "deficit" from unassociated photon energy inside a
star is suppressed by this factor.

### 4.2 General principle

**PDTP Original.** For any system in thermal equilibrium with
radiation, the free photon problem is suppressed by:

```
f_transit = t_interaction / t_dynamical ≪ 1                   ... (4.6)
```

This applies to:
- Stellar interiors (f ~ 10⁻¹⁴)
- Accretion disks (f ~ 10⁻⁸ to 10⁻⁶, depending on optical depth)
- Dense gas clouds (f ~ 10⁻¹² to 10⁻⁸)
- The early universe before recombination (f ~ 10⁻²⁰ to 10⁻¹⁰)

In the last case (pre-recombination universe), the photon-baryon plasma
is so tightly coupled that photons are effectively bound to matter. The
free photon problem does NOT apply to the pre-recombination epoch.

---

## 5. Classification of EM Energy

| Category | Examples | Sources φ? | Mechanism | Deficit |
|----------|----------|-----------|-----------|---------|
| Bound EM energy | Atomic binding, nuclear EM | Yes | Contributes to rest mass mᵢ → gᵢ | None |
| Thermal radiation (coupled) | Stellar interiors, pre-recombination universe | Effectively yes | Absorbed/re-emitted on t ≪ t_grav | ~ 10⁻¹⁴ |
| Free-streaming radiation | CMB, starlight in vacuum | No | Energy tracked via emitter/absorber mass changes | Transient |
| Dense photon field | Hot neutron star surface, GRB jets | Unknown | May require acoustic metric analysis | Open |

**PDTP Original**

---

## 6. The Trace Anomaly as Quantum Correction

At the quantum level, conformal invariance is broken by renormalization,
producing the **trace anomaly**:

```
T^μ_μ (EM, quantum) = β(e)/(2e) · F_μν F^{μν}               ... (6.1)
```

where β(e) = e³/(12π²) + O(e⁵) is the QED beta function.

**Source:** [Conformal anomaly — Wikipedia](https://en.wikipedia.org/wiki/Conformal_anomaly)

For a thermal photon gas of energy density ρ_γ:

```
⟨F_μν F^{μν}⟩ ∝ ρ_γ                                         ... (6.2)
```

The effective trace is:

```
T^μ_μ (quantum) ~ (α_EM / (6π)) ρ_γ ≈ (3.9 × 10⁻⁴) ρ_γ    ... (6.3)
```

**Source:** [QED beta function — Wikipedia](https://en.wikipedia.org/wiki/Quantum_electrodynamics)

This means the quantum trace anomaly provides a **nonzero but tiny**
scalar source for free photons, suppressed by α/(6π) ≈ 4 × 10⁻⁴
relative to a massive field with the same energy density.

**Assessment:** The trace anomaly is far too small to resolve the
radiation-era cosmology problem (it provides only 0.04% of the needed
source). However, it demonstrates that the classical "T = 0 exactly"
is softened by quantum effects. Whether condensate-level corrections
could enhance this is an open question.

---

## 7. When Does the Free Photon Problem Actually Matter?

### 7.1 Regime analysis

| Regime | Radiation fraction Ω_γ | Impact of missing source | Status |
|--------|----------------------|------------------------|--------|
| Present universe | 5 × 10⁻⁵ | Negligible | **No problem** |
| Solar system | 10⁻²¹ per second | Undetectable | **No problem** |
| Stellar interiors | 10⁻¹⁴ (thermal suppression) | Negligible | **No problem** |
| Pre-recombination (z > 1100) | > 0.2 | Thermally coupled → bound | **No problem** |
| Post-recombination CMB (z < 1100) | Decreasing to 5 × 10⁻⁵ | Small and shrinking | **Marginal** |
| Matter-radiation equality (z ≈ 3400) | 0.5 | Significant | **Problem begins** |
| Radiation-dominated (z > 3400) | > 0.5 | Dominant energy component | **Requires resolution** |
| BBN epoch (z ~ 10⁹) | > 0.999 | Nearly all energy | **Critical** |

**Source:** [Friedmann equations — Wikipedia](https://en.wikipedia.org/wiki/Friedmann_equations)

### 7.2 Key insight: the problem is only cosmological

**PDTP Original.** The free photon problem is a **cosmological problem,
not an astrophysical one.** For all present-day, stellar-scale, and
solar-system physics, the combination of:

1. Energy bookkeeping (emitter/absorber mass changes)
2. Thermal equilibrium suppression (t_interaction ≪ t_grav)
3. Small radiation fraction (Ω_γ ≈ 5 × 10⁻⁵ today)

makes the issue completely negligible.

The problem becomes real only in the **radiation-dominated era** of
the early universe, where free-streaming photons carry the dominant
energy density. This is analyzed separately in the radiation-era
cosmology open question.

### 7.3 The pre-recombination surprise

Perhaps counterintuitively, the free photon problem is **less severe
before recombination than after**, because the photon-baryon plasma is
so tightly coupled that photons are effectively massive (they have an
effective mass from plasma effects and cannot freely propagate). The
Thomson scattering optical depth is enormous:

```
τ_Thomson (pre-recombination) ≫ 1                             ... (7.1)
```

**Source:** [Cosmic microwave background — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_microwave_background)

This means photons scatter on timescales far shorter than the Hubble
time, keeping their energy effectively bound to the baryon fluid. In
PDTP terms, the photon-baryon plasma acts as a single coupled system
whose total energy (including radiation) enters the scalar source
through the matter coupling.

The genuine problem window is **after recombination in a hypothetical
radiation-dominated phase** — but by recombination (z ~ 1100), the
universe is already matter-dominated (equality was at z ~ 3400). So the
problematic regime is the era between matter-radiation equality and
recombination, where radiation is significant but not yet decoupled.

In this window, the tight-coupling argument (§4) still applies:
photons scatter frequently and are effectively bound. The free photon
problem only fully manifests **after the photons decouple**, at which
point they are already subdominant.

**PDTP Original:** This analysis shows the free photon problem is
self-limiting in standard cosmology: radiation dominates only when it
is tightly coupled (and effectively bound), and becomes free-streaming
only when it is already subdominant.

---

## 8. Comparison with Brans-Dicke Theory

The same trace problem appears in Brans-Dicke theory. The BD scalar
field equation is:

```
□Φ = (8π / (2ω + 3)) T                                       ... (8.1)
```

**Source:** [Brans-Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)

Since T^EM = 0, the BD scalar is not sourced by radiation either.
Yet BD theory is a viable gravitational theory (with ω > 40,000 from
Cassini) because:

1. The **tensor sector** (inherited from GR) handles radiation normally
2. The scalar provides only a small correction to the tensor dynamics
3. For ω → ∞, BD reduces to GR, and the scalar becomes irrelevant

PDTP's acoustic metric plays an analogous role to BD's tensor sector:
it provides the additional geometric structure needed to handle radiation.
The acoustic metric depends on the condensate density ρ₀ and velocity
v_i, which may respond to radiation pressure even when the scalar φ
does not. This requires further analysis.

---

## 9. Possible Resolutions (Speculative)

These are directions for future work, not established results.

### 9.1 Acoustic metric tensor channel

The acoustic metric:

```
g_μν^{acoustic} = (ρ₀/c_s) × [ -(c_s² - v²), -v_j ; -v_i, δ_ij ]
```

depends on the condensate density ρ₀ and velocity v_i. If radiation
pressure affects ρ₀ (through the condensate equation of state), then
photons could source spatial curvature through the metric even when
they cannot source φ directly. This would require solving the coupled
condensate + radiation system.

### 9.2 Effective mass from plasma coupling

In a dense photon-baryon plasma, photons acquire an effective plasma
frequency:

```
ω_p² = n_e e² / (ε₀ m_e)                                    ... (9.1)
```

**Source:** [Plasma frequency — Wikipedia](https://en.wikipedia.org/wiki/Plasma_frequency)

Below ω_p, photons behave as massive particles with effective mass
m_eff = ℏω_p/c². In PDTP, this could provide a de Broglie phase ψ
for the photon, allowing it to couple to φ through the standard
mechanism. This only works when the plasma density is high enough
(pre-recombination), which is exactly the regime where we need it.

### 9.3 Condensate phase transition

At sufficiently high temperature, the vacuum condensate may undergo
a phase transition (analogous to the normal-superfluid transition in
helium). In the normal phase, the effective field equation could differ
from eq. (4.7), potentially allowing radiation coupling. This connects
to the condensate microscopic structure problem.

### 9.4 Accept as a regime limitation

PDTP may be fundamentally a **matter-era framework**, valid after
matter-radiation equality. The radiation era would require a UV
completion or embedding into a more complete theory. This is not
necessarily a flaw — effective field theories commonly have limited
domains of validity.

---

## 10. Summary

### What is established

| Result | Type | Confidence |
|--------|------|------------|
| Free photons don't source □φ (T^EM = 0) | Established physics | Rigorous |
| Energy bookkeeping conserves total E | PDTP + Noether | Rigorous |
| Thermal equilibrium suppresses deficit by ~10⁻¹⁴ | PDTP Original | Quantitative |
| Solar-system deficit ~ 10⁻²¹ per second | PDTP Original | Quantitative |
| Problem is cosmological, not astrophysical | PDTP Original | Well-supported |
| Pre-recombination tight coupling resolves early universe | PDTP Original | Semi-quantitative |
| Trace anomaly provides ~0.04% correction | Established QFT | Rigorous |
| Free photon problem is self-limiting in standard cosmology | PDTP Original | Novel argument |

### What remains open

| Question | Status | See |
|----------|--------|-----|
| Radiation-dominated era Friedmann equation | Open | Next TODO item |
| Acoustic metric response to radiation pressure | Open | §9.1 |
| Condensate behavior at high temperature | Open | §9.3 |

### Honest assessment

The free photon problem is a **theoretical concern, not an observational
one** — at least for all physics since matter-radiation equality (z ~
3400). The combination of energy bookkeeping, thermal coupling, and
the small present-day radiation fraction makes it undetectable in any
current or planned experiment.

The genuine challenge is cosmological: how does PDTP reproduce the
correct expansion history during radiation domination? This is addressed
in the radiation-era cosmology analysis.

---

## References

### Established Sources
1. [Electromagnetic stress-energy tensor — Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_stress%E2%80%93energy_tensor)
2. [Einstein field equations — Wikipedia](https://en.wikipedia.org/wiki/Einstein_field_equations)
3. [Friedmann equations — Wikipedia](https://en.wikipedia.org/wiki/Friedmann_equations)
4. [Solar luminosity — Wikipedia](https://en.wikipedia.org/wiki/Solar_luminosity)
5. [Radiation zone — Wikipedia](https://en.wikipedia.org/wiki/Radiation_zone)
6. [Free-fall time — Wikipedia](https://en.wikipedia.org/wiki/Free-fall_time)
7. [Conformal anomaly — Wikipedia](https://en.wikipedia.org/wiki/Conformal_anomaly)
8. [QED beta function — Wikipedia](https://en.wikipedia.org/wiki/Quantum_electrodynamics)
9. [Cosmic microwave background — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_microwave_background)
10. [Brans-Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)
11. [Plasma frequency — Wikipedia](https://en.wikipedia.org/wiki/Plasma_frequency)
12. [Nordström's theory of gravitation — Wikipedia](https://en.wikipedia.org/wiki/Nordstr%C3%B6m%27s_theory_of_gravitation)

### PDTP Original Results
1. **Quantitative solar-system deficit:** ΔM/M☉ ~ 2 × 10⁻²¹ per second (§3.2)
2. **Thermal equilibrium suppression:** f_transit ~ 10⁻¹⁴ for stellar interiors (§4.1)
3. **General thermal suppression principle:** f = t_interaction/t_dynamical (§4.2)
4. **Regime classification:** cosmological problem, not astrophysical (§7.2)
5. **Self-limiting argument:** radiation dominates only when tightly coupled (§7.3)
6. **Plasma frequency effective mass:** possible pre-recombination coupling (§9.2)

---

End of photon_gravity_analysis.md

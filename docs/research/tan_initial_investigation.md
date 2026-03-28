# Tangent Function in PDTP — Initial Investigation

**Status:** Initial investigation — reference document for full FCC + Wave check
**Date:** 2026-03-28
**Prerequisite reading:** Part 28b (polarization analogy), Part 28c (wave effects),
Part 31 (phase refraction), Part 61 (two-phase Lagrangian), Part 71 (Leidenfrost)

---

## 1. Motivation

PDTP uses cos(psi - phi) for coupling and sin(psi - phi) for the restoring force.
But the tangent function — tan = sin/cos — appears throughout wave physics,
optics, and geometry in contexts directly relevant to PDTP: slopes, refraction,
polarization, impedance, and critical angles.

**Plain English:** We already use sine and cosine everywhere. Tangent is their
ratio, and it shows up in exactly the kinds of physics PDTP deals with — wave
bending, reflection, polarization filtering. This document explores what
tan(psi - phi) means physically and what new predictions it might produce.

**Why not tan in the Lagrangian?** tan(x) diverges to infinity at x = pi/2.
A Lagrangian with tan would have infinite energy at 90-degree phase difference.
But tan is extremely useful as a **diagnostic ratio** — a derived quantity that
reveals physics the Lagrangian alone doesn't make obvious.

---

## 2. Definition: The Gravitational Phase Tangent

Define the phase difference:

```
Delta = psi - phi        (matter phase minus spacetime phase)             (T.1)
```

The three trig functions in PDTP:

```
cos(Delta) = alpha       (coupling strength, in Lagrangian)       [Part 1]
sin(Delta)               (restoring force, in field equations)    [Part 1]
tan(Delta) = sin/cos     (phase slope — NEW diagnostic)                   (T.2)
```

**Plain English:** If cos tells you "how well-connected are the waves" and sin
tells you "how hard are they being pulled back," then tan tells you "how much
force per unit of connection." It's the slope of the phase relationship — like
asking how steep a hill is, not just how high or how far.

### 2.1 Phase Tangent Table

| Delta (deg) | cos(Delta) | sin(Delta) | tan(Delta) | Physical regime |
|-------------|-----------|-----------|-----------|-----------------|
| 0 | 1.000 | 0.000 | 0.000 | Perfect lock — flat, no force |
| 15 | 0.966 | 0.259 | 0.268 | Weak perturbation — gentle slope |
| 30 | 0.866 | 0.500 | 0.577 | Moderate — coupling > force |
| **45** | **0.707** | **0.707** | **1.000** | **Critical point — force = coupling** |
| 60 | 0.500 | 0.866 | 1.732 | Steep — force > coupling |
| 75 | 0.259 | 0.966 | 3.732 | Near-escape — coupling collapsing |
| **90** | **0.000** | **1.000** | **infinity** | **DECOUPLING — alpha = 0** |

**Key insight:** tan(Delta) = 1 at exactly Delta = pi/4 (45 degrees). This is
a **critical transition point** where the restoring force exactly equals the
coupling strength. Below: coupling wins (bound). Above: force wins (escaping).

[PDTP Original] The 45-degree critical point divides the phase space into
coupling-dominated and force-dominated regimes.

---

## 3. Four Physical Interpretations

### 3.1 Slope / Roof Pitch — "Gravitational Phase Slope"

**Source:** Basic trigonometry — tan(angle) = rise/run = slope of incline

In architecture, tan(angle) gives the steepness of a roof. In PDTP:

```
tan(Delta) = "steepness" of the phase coupling landscape             (T.3)
```

- tan = 0: flat ground — no tendency to move (equilibrium)
- tan = 1: 45-degree slope — critical tipping point
- tan → infinity: vertical cliff — the system falls off (decouples)

**PDTP connection:** The potential V(Delta) = -g*cos(Delta) has slope:

```
dV/d(Delta) = g*sin(Delta)                                            (T.4)
V(Delta)     = -g*cos(Delta)                                          (T.5)

Phase slope ratio = -dV/d(Delta) / V(Delta) = tan(Delta)              (T.6)
```

[DERIVED] The phase tangent IS the ratio of potential slope to potential depth.
When tan > 1, the slope exceeds the depth — the system is on the "escaping" side
of the potential well.

**Plain English:** Imagine a ball in a bowl. cos tells you how deep the bowl is
at your position. sin tells you how steep the wall is. tan tells you whether the
wall is steep enough to escape — if tan > 1, the wall is steeper than the bowl
is deep at that point.

---

### 3.2 Snell's Law — Gravitational Refractive Index

**Source:** [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law) (Wikipedia)
**Source:** Eddington (1920) — gravitational light deflection as refraction
**PDTP previous work:** Part 31 (phase refraction analysis), Part 28c (wave catalog)

#### The PDTP refractive index

In GR, light near a mass M travels through an effective refractive medium:

```
n_GR(r) = 1 + 2*G*M/(r*c^2) = 1 + 2*Phi/c^2                  [ESTABLISHED]
```

**Source:** [Gravitational lens](https://en.wikipedia.org/wiki/Gravitational_lens)
(Wikipedia) — Eddington (1920), confirmed by solar eclipses

In PDTP, the coupling alpha = cos(Delta) modifies the effective wave speed.
The PDTP refractive index is:

```
n_PDTP = 1 / cos(Delta) = 1 / alpha                                   (T.7)
```

[PDTP Original] Check limits:
- alpha = 1 (flat space): n = 1 — no refraction (correct)
- alpha < 1 (near mass): n > 1 — waves slow down, bend toward mass (correct)
- alpha → 0 (horizon): n → infinity — total internal reflection (Part 28c)

#### Snell's law for gravitational phase refraction

```
n_1 * sin(theta_1) = n_2 * sin(theta_2)                         [ESTABLISHED]
```

Substituting n_PDTP:

```
sin(theta_1) / cos(Delta_1) = sin(theta_2) / cos(Delta_2)             (T.8)
```

where Delta_1 and Delta_2 are the phase differences in regions 1 and 2.

#### Critical angle (total internal reflection)

```
sin(theta_c) = n_2/n_1 = cos(Delta_2) / cos(Delta_1)                  (T.9)
```

[DERIVED] For light leaving a strong-gravity region (Delta_1 large) into
weak-gravity (Delta_2 small ≈ 0, cos ≈ 1):

```
sin(theta_c) = cos(Delta_1) = alpha_1                                 (T.10)
```

At a black hole horizon: alpha_1 → 0, so theta_c → 0. ALL angles exceed the
critical angle — total internal reflection. Nothing escapes. This is the
photon sphere / event horizon in PDTP language.

**Plain English:** Near a black hole, spacetime becomes so "dense" (high
refractive index) that light bends inward at every angle — just like light
trapped inside a diamond because the diamond is too dense for it to escape
at any angle.

**Connection to Part 31:** This was already established qualitatively.
The tan formulation makes it quantitative via n_PDTP = 1/alpha.

---

### 3.3 Brewster's Angle — Gravitational Polarization Splitting

**Source:** [Brewster's angle](https://en.wikipedia.org/wiki/Brewster%27s_angle)
(Wikipedia) — tan(theta_B) = n_2/n_1

#### What Brewster's angle is

When light hits a boundary between two media (like air/glass), BOTH
reflection and transmission happen. But at one special angle — Brewster's
angle — the reflected beam is 100% polarized. One polarization component
has ZERO reflection; it all transmits through.

The formula:

```
tan(theta_B) = n_2 / n_1                                        [ESTABLISHED]
```

**Plain English:** Shine a flashlight at a window. Most of the light goes
through, some reflects. But at one specific angle (~56 degrees for glass),
the reflected light is perfectly polarized — like putting on polarized
sunglasses, one orientation is completely gone from the reflection.

#### PDTP Brewster angle for gravitational waves

PDTP predicts multiple gravitational wave polarizations (Part 28b):
- **Tensor modes** (h_+, h_x): standard GR modes, transverse, massless
- **Breathing mode** (h_b): scalar, massive — PDTP's key prediction

When a GW crosses a boundary between two gravitational potential regions
(e.g., entering a galaxy cluster), there is partial reflection and
transmission. At the PDTP Brewster angle:

```
tan(theta_B) = n_2/n_1 = cos(Delta_1)/cos(Delta_2) = alpha_1/alpha_2  (T.11)
```

[PDTP Original] At this angle, one GW polarization mode has zero reflection —
it passes through completely. The other mode partially reflects.

**Prediction:** The breathing mode and tensor modes have different reflection
coefficients at gravitational potential boundaries. At the Brewster angle:
- One mode transmits completely (zero reflection)
- The other mode partially reflects

This is a **new falsifiable prediction**: gravitational wave polarization
splitting at density boundaries.

**Why this matters:** If you observe GWs from a source behind a galaxy cluster,
PDTP predicts the breathing mode and tensor mode arrive with different
amplitudes depending on the incidence angle. GR predicts no such splitting
(GR has only tensor modes, no breathing mode).

#### Connection to LIGO and Part 28b

Part 28b showed LIGO is "blind" to the breathing mode (scalar mode has zero
response in a 90-degree interferometer). The Brewster angle prediction adds
a new dimension: even if we build a detector sensitive to breathing modes,
the relative amplitude of breathing vs tensor depends on the angle of
incidence through intervening gravitational potentials.

---

### 3.4 Loss Tangent — Gravitational Phase Dissipation

**Source:** [Dielectric loss](https://en.wikipedia.org/wiki/Dielectric_loss)
(Wikipedia) — tan(delta) = epsilon''/epsilon' in dielectrics

#### What loss tangent is

In electrical engineering, every capacitor wastes a little energy as heat.
The loss tangent tan(delta) measures the ratio:

```
tan(delta) = power dissipated / power stored = resistive / reactive
```

- tan(delta) << 1: good capacitor (stores energy, little waste)
- tan(delta) ~ 1: critical — equal storage and dissipation
- tan(delta) >> 1: poor capacitor (wastes energy, little storage)

#### PDTP gravitational loss tangent

```
tan(Delta) = sin(Delta)/cos(Delta) = force/coupling                   (T.12)
           = "gravitational loss tangent"
```

[PDTP Original] Physical regimes:

| Regime | tan(Delta) | Interpretation |
|--------|-----------|----------------|
| tan << 1 | Coupling-dominated | Energy stored in phase-lock >> energy exchanged. Bound orbits. Stable gravity. |
| **tan = 1** | **Critical damping** | **Equal exchange. Transition point. Delta = pi/4 = 45 degrees.** |
| tan > 1 | Force-dominated | Energy exchanged >> stored. System unbinding. Phase drift begins. |
| tan → infinity | Decoupled | Zero coupling, maximum force. Complete phase independence. No gravity. |

#### Connection to dark energy (Parts 19, 25)

The cosmic expansion gradually increases Delta (the average phase difference
between matter-waves and spacetime-waves). As Delta crosses pi/4:

- **Before transition (z > 0.7):** tan(Delta) < 1, coupling dominates →
  matter-dominated era, deceleration
- **At transition (z ~ 0.7):** tan(Delta) = 1 → the tipping point
- **After transition (z < 0.7):** tan(Delta) > 1, force dominates →
  dark energy era, acceleration

[SPECULATIVE] If this mapping is correct, the deceleration-to-acceleration
transition corresponds to Delta crossing 45 degrees — a specific, testable
phase angle.

**What this predicts:**
From Part 19: w(z) = (epsilon - 1)/(epsilon + 1) where epsilon = g_eff/(9H^2).
If the transition occurs at tan(Delta) = 1 (i.e., Delta = pi/4), then at the
transition: alpha = cos(pi/4) = 1/sqrt(2) = 0.707. This means the coupling
dropped to 70.7% of its maximum value at the moment acceleration began.

**Plain English:** The universe is like a capacitor that started out storing
almost all its gravitational energy (tan ~ 0, perfect coupling). Over cosmic
time, expansion gradually increased the "losses" (phase drift). At z ~ 0.7,
the losses crossed 50% — the tipping point. Now the universe is losing more
gravitational coupling than it's storing, and that shows up as accelerating
expansion.

---

## 4. Connection to Leidenfrost Decoupling (Part 71)

Part 71 established the Leidenfrost analogy: gravitational decoupling requires
driving the phase difference to Delta = pi/2 (where alpha = cos(pi/2) = 0).

The tan formulation adds precision to this picture:

### 4.1 Leidenfrost in tan language

```
Coupled:     Delta = 0,    tan = 0      (droplet on cold surface — full contact)
Partial:     Delta = pi/4, tan = 1      (critical point — sizzling transition)
Leidenfrost: Delta = pi/2, tan → inf    (droplet floating — full decoupling)
```

**Plain English:** A water droplet on a hot plate goes through three stages:
1. Cold plate — droplet sits flat, full contact (tan = 0, fully coupled)
2. Warm plate — droplet sizzles violently, half-boiling half-touching (tan = 1, critical)
3. Hot plate (> 193 C) — droplet floats on its own steam, no contact (tan → infinity, decoupled)

The Leidenfrost temperature IS the temperature where tan crosses from finite
to effectively infinite — the phase difference reaches pi/2.

### 4.2 The vapour layer = phase-incoherent boundary

In Leidenfrost:
- **Liquid droplet** = matter (phase psi)
- **Hot surface** = spacetime (phase phi)
- **Steam layer** = phase-incoherent boundary (Delta ≈ pi/2 locally)

The steam layer is a thin region where the two phases (liquid/solid → matter/spacetime)
are completely out of sync. The droplet doesn't touch the surface — it floats
on its own incoherence.

### 4.3 Air / Water / Oil layers

[PDTP Original] The Leidenfrost analogy extends to multi-layer systems:

**Air on water:** A thin air layer between two surfaces acts as a thermal
insulator (poor conductor). In PDTP: a phase-incoherent layer between two
regions reduces gravitational coupling.

**Oil on water:** Oil and water don't mix — they maintain a sharp boundary.
In PDTP: two condensate phases that don't phase-lock create a natural
decoupling boundary.

**Multi-layer stack (air/water/oil):** In optics, thin-film interference
from multi-layer coatings creates wavelength-selective reflection. In PDTP:
stacked layers with different phase relationships could create
frequency-selective gravitational shielding.

```
Multi-layer effective coupling:

alpha_eff = alpha_1 * alpha_2 * alpha_3 * ...                         (T.13)
          = cos(Delta_1) * cos(Delta_2) * cos(Delta_3) * ...

tan_eff = product of individual tan values (for small angles)         (T.14)
```

[SPECULATIVE] If ANY layer reaches Delta = pi/2 (tan → infinity), the
overall coupling goes to zero regardless of all other layers. One fully
decoupled layer breaks the chain — just like one layer of perfect insulation
blocks all heat transfer.

**Plain English:** Think of stacking blankets. Each blanket reduces heat flow
a bit. But if one of those blankets is a perfect vacuum gap (zero conduction),
it doesn't matter how thin it is — no heat crosses. Similarly, one layer of
complete phase-incoherence would block gravitational coupling completely.

### 4.4 Tan divergence as phase transition

The tan → infinity behaviour at Delta = pi/2 has the mathematical signature
of a **phase transition**:
- Order parameter: alpha = cos(Delta) → 0
- Susceptibility: tan(Delta) → infinity (diverges at critical point)
- Correlation length: xi = healing length → this should diverge at decoupling

This matches the structure of a second-order phase transition. The decoupling
point is not just "gravity going to zero" — it is a genuine phase transition
in the condensate, with divergent susceptibility and (potentially) critical
fluctuations.

[SPECULATIVE] If decoupling is a true phase transition, it may exhibit:
- Critical slowing down (harder to push past the transition)
- Universal exponents (independent of microscopic details)
- Fluctuation enhancement near the transition (anomalous gravitational noise)

---

## 5. Cross-References to Previous PDTP Results

### 5.1 Results that tan connects

| Part | Previous result | Tan connection |
|------|----------------|----------------|
| 1 | alpha = cos(psi-phi) coupling | tan = sin/cos = force/coupling ratio (T.2) |
| 12 | Tetrad extension, GR recovery | n_PDTP = 1/alpha appears in linearized gravity |
| 19, 25 | Dark energy as phase drift | tan = 1 at deceleration→acceleration transition (Sec 3.4) |
| 28b | LIGO blind to breathing mode | Brewster angle predicts mode splitting (Sec 3.3) |
| 28c | Wave effects: lensing=refraction, horizon=TIR | n_PDTP = 1/alpha quantifies both (Sec 3.2) |
| 31 | Phase refraction, Snell's law for gravity | Tan appears naturally in bending angle integral |
| 33 | Vortex winding n = m_cond/m | Vortex velocity: v_s/c = tan of some angle? (TO CHECK) |
| 34 | c_s = c exactly | Sound speed in terms of refractive index: c_s = c/n? (TO CHECK) |
| 35 | Dimensional transmutation, IR free | Beta function slope involves tan-like ratios |
| 61 | Two-phase: phi_+, phi_- | phi_- mass couples to Phi → affects n_PDTP locally (TO CHECK) |
| 65 | Chirality from birefringence | Birefringent medium has TWO refractive indices → two Brewster angles |
| 71 | Leidenfrost decoupling at pi/2 | tan → infinity IS the decoupling transition (Sec 4) |
| 75 | Emergent metric g_mu_nu = Tr(dU†dU) | Metric components involve tan of SU(3) group angles? (TO CHECK) |
| 83 | N_eff = 6pi (Sakharov) | Heat kernel on curved space uses n_PDTP → tan in spectral sums? (TO CHECK) |

### 5.2 Results that need rechecking with tan

These previous results may gain new insight or corrections when tan is included:

1. **Dark energy equation of state (Part 19, 25):** Does the tan = 1 transition
   predict the exact redshift z_transition? If so, it's testable against DESI data.

2. **Leidenfrost energy budget (Part 71):** The tan divergence at pi/2 means the
   "force per unit coupling" goes to infinity. Does this change the energy
   calculation? (Part 71 used V = -g*cos, which already captures this, but
   the tan formulation may reveal instabilities.)

3. **Phase refraction (Part 31):** The n_PDTP = 1/alpha refractive index should
   be substituted back into the Part 31 Snell's law analysis. Do the ionization
   angles change? (Part 31 found 60 degrees, not 90.)

4. **Brewster angle — new prediction:** Does this survive a full derivation?
   Need to compute reflection/transmission coefficients for breathing mode
   vs tensor mode at a step potential. This would be Part 84+ work.

5. **Birefringence (Part 65):** The EW condensate has two refractive indices
   (left/right chirality). Each has its own Brewster angle. Does this produce
   observable parity violation in GW propagation?

6. **Multi-layer decoupling:** The air/water/oil layer model needs quantitative
   treatment. How thick must a phase-incoherent layer be to effectively decouple?
   Is it the healing length xi = l_P/sqrt(2) (Part 71) or something larger?

---

## 6. New Predictions from Tan Analysis

### 6.1 Gravitational Brewster angle (NEW)

**Statement:** When gravitational waves cross a boundary between regions of
different gravitational potential, there exists a Brewster-like angle where
one polarization mode (breathing or tensor) has zero reflection.

**Formula:** tan(theta_B) = alpha_1/alpha_2 = cos(Delta_1)/cos(Delta_2)

**Test:** Observe GWs from behind a galaxy cluster. Compare breathing mode
amplitude to tensor mode amplitude at different incidence angles.

**Distinguishes from GR:** GR has no breathing mode, hence no Brewster splitting.

### 6.2 tan = 1 transition redshift (NEW)

**Statement:** The deceleration-to-acceleration transition occurs when the
cosmic average phase tangent reaches unity: tan(<Delta>) = 1.

**Formula:** At transition: alpha = cos(pi/4) = 1/sqrt(2) ≈ 0.707

**Test:** If alpha at z=0.7 is 0.707, this constrains the phase drift rate.
Combined with the w(z) formula from Part 19, this should predict the exact
value of w at the transition.

**Distinguishes from Lambda-CDM:** Lambda-CDM has no phase angle; the
transition is purely density-driven. PDTP predicts a specific coupling
value at the transition.

### 6.3 Phase transition at decoupling (NEW)

**Statement:** Gravitational decoupling (alpha → 0) is a second-order
phase transition with divergent susceptibility (tan → infinity).

**Test:** Near the decoupling point, gravitational noise should increase
(critical fluctuations). If a mechanism exists to approach pi/2, anomalous
gravitational fluctuations would precede full decoupling.

---

## 7. Established Uses of Tan in Science

For reference — where tan appears in current mathematics and physics:

| Domain | Formula | What tan does |
|--------|---------|---------------|
| Trigonometry | tan = opposite/adjacent | Slope of a right triangle's hypotenuse |
| Architecture | pitch = tan(angle) | Roof steepness |
| Surveying/navigation | tan(elevation) = height/distance | Measuring heights from angles |
| Optics (Brewster) | tan(theta_B) = n_2/n_1 | Zero-reflection angle for one polarization |
| Optics (Snell) | Bending angle involves tan in approximations | Refraction at interfaces |
| Electrical engineering | tan(delta) = loss tangent | Dielectric dissipation ratio |
| Pendulum (large angle) | Period involves tan(theta/2) | Exact non-linear oscillation |
| Relativity | v/c = tanh(rapidity) | Velocity addition without exceeding c |
| Scattering theory | tan(delta_l) = phase shift | S-matrix partial wave analysis |
| Complex analysis | Poles of tan(z) at pi/2 + n*pi | Counting zeros, residues |
| Signal processing | Hilbert transform phase = arctan(Q/I) | Instantaneous phase extraction |
| Fluid dynamics | tan(alpha) = v_y/v_x | Flow direction angle |
| Ballistics | Range = v^2*sin(2*theta)/g; optimal at theta = 45 deg (tan=1) | Maximum range angle |

**Key pattern:** tan appears whenever you need a RATIO of two perpendicular
components, or whenever there is a CRITICAL ANGLE where behaviour changes
qualitatively. Both of these are central to PDTP.

---

## 8. Open Questions for Full Investigation

These questions require proper FCC + Wave check treatment:

1. **Does tan(Delta) = 1 predict z_transition exactly?** Needs numerical work
   with Part 19 w(z) formula.
2. **Brewster angle for GWs:** Full reflection/transmission coefficient
   calculation for breathing + tensor modes at a step potential.
3. **Multi-layer phase stacks:** Quantitative treatment of air/water/oil
   analogy. Transfer matrix method for gravitational wave propagation
   through multiple layers.
4. **Leidenfrost + tan:** Does the tan divergence change the Part 71 energy
   budget? Is there a "Leidenfrost temperature" in phase space?
5. **SU(3) tan:** Does tan appear naturally in the SU(3) Wilson action or
   group manifold geometry? The SU(3) generators involve sqrt(3) and 1/2 —
   these are tan(30) and tan(arctan(1/2)).
6. **Hawking temperature:** Does n_PDTP = 1/alpha modify the Hawking
   calculation (Part 24)? The Hawking temperature involves the surface
   gravity — which is related to the gradient of alpha.
7. **PPN parameters:** Do gamma and beta pick up tan-dependent corrections?
8. **Two-phase tan:** In the two-phase Lagrangian (Part 61), there are TWO
   phase differences (Delta_+ and Delta_-). What does tan(Delta_-) mean?
   The reversed Higgs (Part 62) has mass m^2 = 2g*Phi — does this create
   a local Brewster angle?
9. **Koide angle:** The Koide formula has theta_0 = 2/9. Is tan(2/9) or
   arctan(2/9) meaningful? Does it connect to Z_3 geometry?
10. **N_eff and tan:** The Sakharov formula has N_eff = 6*pi. Does tan appear
    in the heat kernel expansion coefficients? The a_1 coefficient involves
    curvature integrals — these are sensitive to the refractive index.

---

## 9. Summary

| Finding | Equation | Status | Significance |
|---------|----------|--------|-------------|
| Phase tangent defined | tan(Delta) = sin/cos = force/coupling | [PDTP Original] | New diagnostic ratio |
| Critical point at 45 deg | tan(pi/4) = 1 | [DERIVED] | Divides bound/unbound regimes |
| PDTP refractive index | n = 1/alpha = 1/cos(Delta) | [PDTP Original] | Quantifies gravitational refraction |
| Snell's law for gravity | sin(theta)/cos(Delta) = const | [DERIVED] | Gravitational lensing as refraction |
| Total internal reflection | theta_c: sin = alpha | [DERIVED] | Black hole horizon (Part 28c confirmed) |
| Brewster angle for GWs | tan(theta_B) = alpha_1/alpha_2 | [SPECULATIVE] | New prediction — mode splitting |
| Loss tangent | tan(Delta) = dissipation/storage | [PDTP Original] | Dark energy transition at tan = 1 |
| Leidenfrost = tan → inf | Decoupling = divergent phase slope | [PDTP Original] | Phase transition character confirmed |
| Multi-layer coupling | alpha_eff = product of alpha_i | [SPECULATIVE] | One decoupled layer blocks all coupling |
| Transition redshift | tan = 1 at z ~ 0.7 | [SPECULATIVE] | Testable with DESI w(z) data |

**Bottom line:** tan(psi - phi) is not in the Lagrangian, but it is a physically
meaningful diagnostic that connects phase-locking to refraction, polarization,
impedance, and critical transitions. It unifies multiple previous PDTP results
under a single framework and generates at least 3 new predictions worth investigating.

---

## 10. Equations for Reference File

```
(T.1)  Delta = psi - phi
(T.2)  tan(Delta) = sin(Delta)/cos(Delta) = force/coupling
(T.3)  tan(Delta) = gravitational phase slope
(T.4)  dV/d(Delta) = g*sin(Delta)
(T.5)  V(Delta) = -g*cos(Delta)
(T.6)  Phase slope ratio = -[dV/d(Delta)] / V(Delta) = tan(Delta)
(T.7)  n_PDTP = 1/cos(Delta) = 1/alpha
(T.8)  sin(theta_1)/cos(Delta_1) = sin(theta_2)/cos(Delta_2)
(T.9)  sin(theta_c) = cos(Delta_2)/cos(Delta_1)
(T.10) sin(theta_c) = alpha_1  (for Delta_2 ~ 0)
(T.11) tan(theta_B) = alpha_1/alpha_2
(T.12) Gravitational loss tangent = tan(Delta)
(T.13) alpha_eff = product of cos(Delta_i)
(T.14) tan_eff = product of tan(Delta_i) (small angle approx)
```

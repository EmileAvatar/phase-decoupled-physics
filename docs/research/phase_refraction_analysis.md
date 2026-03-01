# Phase Refraction Analysis: Gravity and Atomic Binding

**Part 31** — Phase refraction as the physical mechanism for gravity and atomic binding

**Status:** Completed analysis — interpretive framework confirmed, not predictive

**Depends on:** Part 28c (wave effects catalog), Part 27b (universal phase-locking),
Part 28b (polarization/decoupling), Part 23 (atomic phase coupling)

---

## 1. Executive Summary

In plain English: imagine spacetime as a medium that waves travel through — like
water or glass. Near a massive object, this medium gets "denser" (waves slow down).
When a wave enters a denser medium, it bends inward — this is refraction, the same
thing that makes a straw look bent in a glass of water. In PDTP, this bending IS
gravity: matter-waves refract toward mass because spacetime is denser there.

The same picture works for atoms. A proton's electric field creates a much denser
"EM phase medium" around it. Electron waves entering this medium refract inward
and get trapped — bouncing back and forth in standing wave patterns. Those standing
waves are atomic orbitals. Different orbital shapes (s, p, d, f) correspond to
different angles of incidence — like different bouncing patterns inside a curved
mirror.

**Key findings:**
1. The PDTP wave equation reduces to the Schrodinger equation in the appropriate
   limit — **confirmed** (standard result, not new)
2. Ionization corresponds to a phase angle of **60 degrees, not 90 degrees** —
   the simple "critical angle = 90 degrees" picture **fails** for ionization
   (virial theorem correction)
3. Orbital angular momentum maps qualitatively to refraction angle — **works**
   as a physical picture, not yet as a derivation
4. Sudoku consistency check: **11/11 tests pass** for g_EM = 27.2 eV
5. Gravity and EM are the **same mechanism** (phase refraction) at vastly different
   coupling strengths — ratio ~10^39. This restates the hierarchy problem, not solves it.

---

## 2. Refraction — Established Physics

**Source:** [Refraction](https://en.wikipedia.org/wiki/Refraction) (Wikipedia)
**Source:** [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law) (Wikipedia)
**Source:** [Total internal reflection](https://en.wikipedia.org/wiki/Total_internal_reflection) (Wikipedia)

When a wave passes from one medium to another with different wave speeds, it bends.
The fundamental law is Snell's law:

    n_1 sin(theta_1) = n_2 sin(theta_2)

where n = c/v is the refractive index (ratio of vacuum speed to speed in medium).
Higher n means the wave travels slower in that medium.

Key consequences:
- **Toward denser medium:** wave bends toward the normal (smaller angle)
- **Away from denser medium:** wave bends away from the normal (larger angle)
- **Critical angle:** when going from dense to less dense, there is an angle
  beyond which the wave cannot escape — **total internal reflection**
- **Critical angle formula:** sin(theta_c) = n_2/n_1 (for n_1 > n_2)

---

## 3. Gravitational Refraction (Review)

This section reviews results already established in Part 28c (wave effects catalog).

**Source:** [Gravitational lens](https://en.wikipedia.org/wiki/Gravitational_lens) (Wikipedia)
**Source:** Part 28c, Effects 15-16 (wave_effects_pdtp.md)

In PDTP, spacetime is a condensate with position-dependent wave speed. Near a mass:
- The condensate is compressed (higher density)
- Waves travel slower (lower local c)
- The effective refractive index increases: n(r) = c_far / c_local

This means matter-waves (and light) **refract toward mass** — exactly as observed
in gravitational lensing. The event horizon (black hole boundary) is the point
where n(r) becomes infinite — total internal reflection with zero critical angle.

    Effective refractive index (weak field):
    n(r) = 1 / sqrt(1 - 2*G*M/(r*c^2))   approximately = 1 + G*M/(r*c^2)

**Source:** [Schwarzschild metric](https://en.wikipedia.org/wiki/Schwarzschild_metric) (Wikipedia)

This was established in Part 28c at HIGH confidence. No new content here — the
contribution of this document is extending the picture to atomic binding.

---

## 4. The Two-Coupling Problem

This is the critical honesty section. The PDTP Lagrangian has one coupling per
matter field:

    L = ... + g_i cos(psi_i - phi)

For gravity, the coupling strength is:

    g_grav = G * m_e * m_p / a_0 = 1.92 x 10^-57 J = 1.20 x 10^-38 eV

For the electromagnetic interaction at the Bohr radius:

    g_EM = e^2 / (4*pi*epsilon_0*a_0) = 27.2 eV  (the Hartree energy)

**Source:** [Hartree](https://en.wikipedia.org/wiki/Hartree) (Wikipedia)

These differ by a factor of ~10^39. They CANNOT be the same coupling constant.
The refraction mechanism is the same — waves bending in a denser medium — but
the "density" of the EM phase medium is enormously greater than the gravitational
phase medium.

In dimensionless terms:
- Gravitational coupling: alpha_G = G * m_e * m_p / (hbar * c) = 3.22 x 10^-42
- EM coupling: alpha_EM = e^2 / (4*pi*epsilon_0*hbar*c) = 1/137 = 7.30 x 10^-3
- Hierarchy ratio: alpha_EM / alpha_G = 2.27 x 10^39

**Source:** [Gravitational coupling constant](https://en.wikipedia.org/wiki/Gravitational_coupling_constant) (Wikipedia)

**PDTP Original:** The refraction picture accommodates both forces naturally:
gravity and EM are both phase refraction, at different coupling strengths. But this
**restates** the hierarchy problem rather than solving it. The question becomes:
WHY is the EM refractive index 10^39 times larger than the gravitational one?

### 4.1 Proposed EM Phase Coupling

**PDTP Original:** By analogy with the gravitational coupling, the EM sector would
have a PDTP-style Lagrangian:

    L_EM_coupling = g_EM * cos(psi_e - A)

where A is the EM phase field (related to the photon/gauge field) and g_EM is the
Coulomb energy. This was already suggested in Part 27b (phase-locking as universal
force mechanism).

The Coulomb potential V(r) = -e^2/(4*pi*epsilon_0*r) emerges from this coupling in
the weak-field limit, just as the Newtonian potential V(r) = -G*M/r emerges from
the gravitational coupling (Part 1, Section 7).

---

## 5. Calculation 1: PDTP Wave Equation Reduces to Schrodinger

**Source:** [Klein-Gordon equation](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation) (Wikipedia)
**Source:** [Schrodinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) (Wikipedia)

### Step 1: Weak-field linearization

The PDTP field equation for matter:

    Box(psi) = -g sin(psi - phi)

For small phase mismatch |psi - phi| << 1:

    sin(psi - phi) ~ psi - phi
    Box(psi) ~ -g(psi - phi)

This is the standard linearization used throughout PDTP (Part 1, Section 7).

### Step 2: Background phase field as potential

The background spacetime/EM phase field phi(r) acts as the potential. For the
Coulomb interaction:

    phi(r) relates to V(r) = -e^2/(4*pi*epsilon_0*r)

### Step 3: Non-relativistic limit

Write the matter wave as a slowly-varying envelope times the rest-mass oscillation:

    psi(x,t) = Psi(x,t) * exp(-i*m*c^2*t/hbar)

where Psi varies slowly compared to the Compton frequency m*c^2/hbar.

Substituting into Box(psi) and keeping only first-order time derivatives
(the standard Klein-Gordon to Schrodinger reduction):

    i*hbar * dPsi/dt = -(hbar^2 / 2m) * nabla^2(Psi) + V(r) * Psi

**This IS the Schrodinger equation.**

### Verification

Hydrogen energy levels from this equation:

| n | E_n (eV) | -13.6/n^2 (eV) | Match? |
|---|----------|----------------|--------|
| 1 | -13.606  | -13.600        | YES    |
| 2 | -3.401   | -3.400         | YES    |
| 3 | -1.512   | -1.511         | YES    |
| 4 | -0.850   | -0.850         | YES    |
| 5 | -0.544   | -0.544         | YES    |

**Source:** [Hydrogen atom](https://en.wikipedia.org/wiki/Hydrogen_atom) (Wikipedia)

### Honest assessment

This reduction is a standard result in relativistic QM — it is NOT unique to PDTP.
Any wave equation with a background potential reduces to Schrodinger in the
non-relativistic limit. This confirms **compatibility** between PDTP and QM, but
does not prove that refraction IS the mechanism. The Coulomb potential is **input**,
not derived from PDTP.

---

## 6. Calculation 2: Critical Angle and Ionization

### The simple picture

In the PDTP phase coupling, the potential energy is:

    V(theta) = -g_EM * cos(theta)    where theta = psi - phi

- At theta = 0: V = -g_EM = -27.2 eV (fully phase-locked, ground state)
- At theta = 90 deg: V = 0 (total decoupling)
- At theta = 180 deg: V = +g_EM = +27.2 eV (anti-phase, maximum repulsion)

### The 60-degree finding

**Source:** [Virial theorem](https://en.wikipedia.org/wiki/Virial_theorem) (Wikipedia)

The ionization energy of hydrogen is 13.6 eV = g_EM/2, NOT g_EM. This is because
of the virial theorem: for a 1/r potential, the kinetic energy equals minus half
the potential energy:

    2 * <KE> = -<V>
    E_total = <KE> + <V> = <V>/2 = -g_EM/2

So ionization (E_total = 0) requires only half the full Coulomb energy. In the
phase angle picture:

    cos(theta_ion) = 1 - E_ion/g_EM = 1 - 1/2 = 0.5
    theta_ion = 60 degrees

**PDTP Original:** The ionization angle is 60 degrees, not 90 degrees.

| n | E_n (eV) | Ionization energy (eV) | Phase angle (deg) | Meaning |
|---|----------|------------------------|-------------------|---------|
| 1 | -13.606  | 13.606                 | 60.0              | Ground state |
| 2 | -3.401   | 3.401                  | 29.0              | First excited |
| 3 | -1.512   | 1.512                  | 19.2              | Second excited |
| 4 | -0.850   | 0.850                  | 14.4              | n=4 |
| 5 | -0.544   | 0.544                  | 11.5              | n=5 |

### Physical interpretation of the different angles

- **0 degrees:** Perfect phase lock. Maximum binding. Ground state.
- **60 degrees:** Virial equipartition threshold. The kinetic energy accumulated
  from the phase gradient equals the remaining potential energy. The electron
  is just barely unbound. This is ionization.
- **90 degrees:** Total phase decoupling. The electron has no EM coupling at all
  (cos = 0). This requires 27.2 eV — twice the ionization energy. It corresponds
  to stripping ALL Coulomb energy, including the kinetic energy the electron
  gained while falling into the potential well.
- **180 degrees:** Anti-phase. Maximum repulsion. cos = -1. This is the
  antiparticle configuration (cf. Part 22).

### What this means for Goal 2 (phase decoupling)

The 60-vs-90 distinction matters for the engineering goal:
- **Ionization** (escaping a bound state) requires reaching 60 degrees
- **Total phase decoupling from spacetime** requires reaching 90 degrees
- These are different energy costs: ionization = g/2, total decoupling = g

For gravity, g_grav is extraordinarily small, so both are negligible. But the
distinction is important for understanding what "decoupling" means physically.

### Snell's law connection

The effective refractive index near a proton:

| Type | Delta_n at Bohr radius | Physical effect |
|------|----------------------|-----------------|
| Gravitational | 2.35 x 10^-44 | Negligible wave bending |
| Electromagnetic | 5.33 x 10^-05 | Traps electron waves (atoms exist) |
| Ratio | 2.27 x 10^39 | = the hierarchy problem |

The EM medium bends electron waves 10^39 times more effectively than the
gravitational medium. This is why atoms exist at angstrom scales but
"gravitational atoms" would need to be 10^29 times larger (a_G = 1.2 x 10^29 m,
larger than the observable universe!).

---

## 7. Calculation 3: Angular Momentum as Refraction Angle

**Source:** [Whispering-gallery wave](https://en.wikipedia.org/wiki/Whispering-gallery_wave) (Wikipedia)
**Source:** [Hydrogen atom](https://en.wikipedia.org/wiki/Hydrogen_atom) (Wikipedia)

### The whispering gallery analogy

In optics, a wave bouncing inside a spherical cavity has different modes depending
on its angle of incidence. Waves hitting nearly head-on bounce back and forth
through the center (radial modes). Waves hitting at a grazing angle skim along
the surface (whispering gallery modes).

In quantum mechanics, the orbital angular momentum quantum number l plays exactly
this role:
- l = 0 (s-orbital): spherically symmetric, radial standing wave = "head-on bounce"
- l = 1 (p-orbital): dumbbell shape, one angular node = oblique incidence
- l = n-1 (maximum l): electron stays near the outer edge = "whispering gallery"

### Semiclassical incidence angle

The semiclassical approximation gives:

    sin(theta_inc) = sqrt(l*(l+1)) / n

**PDTP Original:** This maps orbital quantum numbers to refraction geometry:

| n | l | L/hbar | theta_inc (deg) | Orbital type |
|---|---|--------|----------------|-------------|
| 1 | 0 | 0.000  | 0.0            | s (radial)  |
| 2 | 0 | 0.000  | 0.0            | s (radial)  |
| 2 | 1 | 1.414  | 45.0           | p (dumbbell)|
| 3 | 0 | 0.000  | 0.0            | s (radial)  |
| 3 | 1 | 1.414  | 28.1           | p (dumbbell)|
| 3 | 2 | 2.449  | 54.7           | d (clover)  |
| 4 | 0 | 0.000  | 0.0            | s (radial)  |
| 4 | 1 | 1.414  | 20.7           | p (dumbbell)|
| 4 | 2 | 2.449  | 37.8           | d (clover)  |
| 4 | 3 | 3.464  | 60.0           | f (complex) |

The pattern is clear:
- l = 0 always gives theta = 0 (radial, head-on)
- l = n-1 gives theta approaching 90 degrees for large n (tangential, grazing)
- Higher l at fixed n means more oblique incidence

### The centrifugal barrier as refraction geometry

The centrifugal barrier in the radial Schrodinger equation:

    V_centrifugal = l*(l+1)*hbar^2 / (2*m*r^2)

prevents radial modes from penetrating close to the nucleus for high l. In the
refraction picture, this is simply the statement that waves at oblique angles
reflect from the boundary before reaching the center — they cannot penetrate
as deeply.

### Honest assessment

This mapping is **qualitative**. The whispering gallery analogy correctly describes
the orbital geometry, but the quantitative derivation — showing that the centrifugal
barrier formula emerges directly from PDTP refraction geometry — has not been done.
This would require solving the PDTP wave equation in a spherically-varying phase
field and showing that the angular separation gives l*(l+1)*hbar^2/(2mr^2) exactly.

---

## 8. Sudoku Consistency Check

**New value tested:** g_EM = e^2/(4*pi*epsilon_0*a_0) = 27.2 eV (Hartree energy)

**New claim tested:** g_EM plays the role of the PDTP coupling constant for the
EM sector, analogous to g_grav for gravity.

### Results

| Test | Predicted | Known | Ratio | Status |
|------|-----------|-------|-------|--------|
| H ground state E_1 = -g_EM/2 | -2.180e-18 J | -2.180e-18 J | 1.000 | MATCH |
| Bohr radius from g_EM | 5.292e-11 m | 5.292e-11 m | 1.000 | MATCH |
| alpha_EM = g_EM*a_0/(hbar*c) | 7.297e-03 | 7.297e-03 | 1.000 | MATCH |
| Rydberg = m_e*c^2*alpha^2/2 | 2.180e-18 J | 2.180e-18 J | 1.000 | MATCH |
| a_0/lambda_C = 1/alpha | 137.04 | 137.04 | 1.000 | MATCH |
| a_0/r_e = 1/alpha^2 | 18779 | 18779 | 1.000 | MATCH |
| g_EM = m_e*c^2*alpha^2 | 4.360e-18 J | 4.360e-18 J | 1.000 | MATCH |
| alpha_EM/alpha_G = g_EM/g_grav | 2.269e+39 | 2.269e+39 | 1.000 | MATCH |
| Ionization angle = 60 deg | 60.00 | 60.00 | 1.000 | MATCH |
| Lyman-alpha = 3*g_EM/8 | 1.635e-18 J | 1.634e-18 J | 1.000 | MATCH |
| H-alpha = 5*g_EM/72 | 3.028e-19 J | 3.028e-19 J | 1.000 | MATCH |

**SUDOKU SCORECARD: 11 matches, 0 contradictions out of 11 tests**

All tests pass. This is expected because g_EM IS the Hartree energy, which is
established physics. The tests confirm that the **mapping** (identifying the
Hartree energy as the PDTP coupling constant for the EM sector) is algebraically
consistent. It does not prove the mapping is physically correct — only that it
does not contradict any known result.

---

## 9. The Hierarchy as Refractive Index Ratio

**PDTP Original:** If both gravity and EM are phase refraction, then the hierarchy
problem becomes a question about refractive indices:

    WHY is Delta_n_EM / Delta_n_grav = 10^39 ?

Or equivalently: why is the EM phase medium 10^39 times denser than the
gravitational phase medium?

The gravitational "Bohr radius" — the size of a gravitational atom where an
electron orbits a proton purely by gravity — would be:

    a_G = hbar^2 / (G * m_e^2 * m_p) = 1.2 x 10^29 m

This is about 10^13 light-years — larger than the observable universe. Gravitational
atoms don't exist because gravity's refractive index is too weak to bend electron
waves into compact orbits.

This is the **same hierarchy problem** seen in Part 29 and Part 30, now expressed
in refraction language. The refraction picture does not solve it but provides a
vivid physical interpretation: EM creates a "thick lens" that traps electron waves
easily, while gravity creates an incomprehensibly thin lens that barely bends
anything at quantum scales.

---

## 10. Conclusions

### What this analysis achieves

1. **Unified physical picture:** Gravity and atomic binding are both wave refraction
   in phase media of different densities. The mechanism is identical; only the
   coupling strength differs.

2. **Compatibility confirmed:** The PDTP wave equation reduces to the Schrodinger
   equation in the non-relativistic limit. PDTP is compatible with all of quantum
   mechanics.

3. **Orbital geometry explained:** The whispering gallery analogy correctly maps
   orbital angular momentum l to refraction angle. s-orbitals are head-on modes,
   high-l orbitals are grazing modes.

4. **60-degree finding:** Ionization corresponds to theta = 60 degrees, not 90
   degrees. The virial theorem for 1/r potentials means ionization requires only
   half the full Coulomb energy. This corrects the naive critical-angle picture
   from the TODO item.

5. **Sudoku scorecard:** 11/11 — the g_EM = Hartree energy mapping is internally
   consistent.

### What this analysis does NOT achieve

1. **No new predictions:** The refraction picture is interpretive. It does not
   predict anything that standard QM does not already predict.

2. **Hierarchy problem unsolved:** The ratio alpha_EM/alpha_G ~ 10^39 is restated
   as a refractive index ratio, not derived.

3. **Quantitative orbital derivation incomplete:** The centrifugal barrier has not
   been derived from PDTP refraction geometry (only mapped qualitatively).

4. **Coulomb potential is input:** The analysis takes V(r) = -e^2/(4*pi*epsilon_0*r)
   as given. PDTP does not derive the Coulomb potential from phase dynamics — it
   would need to derive the EM coupling from the condensate microphysics.

5. **Strong force extension speculative:** The TODO mentioned quarks as refraction.
   This remains entirely speculative — SU(3) gauge structure cannot be derived from
   the simple cos(psi - phi) coupling (cf. Part 27b).

### Connection to other Parts

- **Part 28c:** Gravitational refraction already established there (HIGH confidence).
  This document extends to EM sector.
- **Part 27b:** The universal phase-locking picture proposed g*cos(psi_1 - psi_2)
  for all forces. This document tests that picture quantitatively for EM.
- **Part 28b:** The 90-degree decoupling point (crossed polarizers) is confirmed
  but shown to be distinct from ionization (60 degrees).
- **Part 29/30:** The hierarchy problem encountered here (alpha_EM/alpha_G ~ 10^39)
  is the same circularity identified in Part 29.
- **Goal 2 (decoupling):** For gravitational decoupling, the energy cost is g_grav
  per oscillator, which is extraordinarily small. The bottleneck is the mechanism,
  not the energy (Part 29 finding confirmed).

---

## 11. References

**Source:** [Refraction](https://en.wikipedia.org/wiki/Refraction) (Wikipedia)
**Source:** [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law) (Wikipedia)
**Source:** [Total internal reflection](https://en.wikipedia.org/wiki/Total_internal_reflection) (Wikipedia)
**Source:** [Gravitational lens](https://en.wikipedia.org/wiki/Gravitational_lens) (Wikipedia)
**Source:** [Klein-Gordon equation](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation) (Wikipedia)
**Source:** [Schrodinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) (Wikipedia)
**Source:** [Hydrogen atom](https://en.wikipedia.org/wiki/Hydrogen_atom) (Wikipedia)
**Source:** [Virial theorem](https://en.wikipedia.org/wiki/Virial_theorem) (Wikipedia)
**Source:** [Hartree](https://en.wikipedia.org/wiki/Hartree) (Wikipedia)
**Source:** [Bohr radius](https://en.wikipedia.org/wiki/Bohr_radius) (Wikipedia)
**Source:** [Gravitational coupling constant](https://en.wikipedia.org/wiki/Gravitational_coupling_constant) (Wikipedia)
**Source:** [Schwarzschild metric](https://en.wikipedia.org/wiki/Schwarzschild_metric) (Wikipedia)
**Source:** [Whispering-gallery wave](https://en.wikipedia.org/wiki/Whispering-gallery_wave) (Wikipedia)
**Source:** [Ionization energy](https://en.wikipedia.org/wiki/Ionization_energy) (Wikipedia)
**Source:** [Rydberg constant](https://en.wikipedia.org/wiki/Rydberg_constant) (Wikipedia)

**Simulation:** [phase_refraction_hydrogen.py](../../simulations/phase_refraction_hydrogen.py)
**Output:** [phase_refraction_output.md](../../simulations/phase_refraction_output.md)

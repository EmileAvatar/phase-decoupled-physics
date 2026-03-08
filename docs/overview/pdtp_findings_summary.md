# PDTP: What We Know, What We've Found, and What Remains

**Phase-Decoupled Transport Physics — Plain-Language Summary**

*For readers who know some physics but are new to PDTP.
No prior knowledge of the framework required.*

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

## 2. The Core Equation (Plain English)

The whole framework follows from one equation (the Lagrangian):

```
L = (energy stored in spacetime wave)
  + (energy stored in matter wave)
  + g * cos(phase of matter - phase of spacetime)
```

The **cos** term is the key. It is maximum (=1) when the two waves are perfectly
in step — this is full gravitational coupling, normal gravity. It drops toward
zero as the waves drift out of step. It reaches zero at 90 degrees out of step —
that is the "decoupled" condition.

The coupling strength **g** is proportional to the particle's mass, which is why
heavy objects fall harder than light ones (before you cancel the mass in Newton's
law, it is right there in the coupling).

---

## 3. What the Waves Actually Are

| Wave | In ordinary terms | In PDTP |
|------|-------------------|---------|
| Spacetime wave (φ) | The gravitational field | A phase oscillation of the vacuum — a superfluid-like medium filling all of space |
| Matter wave (ψ) | The quantum wavefunction of a particle | The de Broglie phase of the particle; every particle already has one |
| Phase difference (ψ − φ) | The "mismatch" between the two | The quantity that controls how strongly gravity acts |
| Coupling (g) | Newton's gravitational coupling | A spring constant; proportional to mass |

Every particle IS a wave. Its Compton wavelength λ = ℏ/(mc) tells you how long
the wave is. Its Compton frequency ω = mc²/ℏ tells you how fast it oscillates.
Heavier particles oscillate faster and have shorter wavelengths.

---

## 4. What We Have Mathematically Confirmed

These results are derived rigorously from the PDTP equations:

| Result | What it means | Evidence |
|--------|---------------|----------|
| **Newtonian gravity emerges** | The 1/r² force law falls out of the wave equations automatically | Simulation: [emergent_gr_simulation.py](../../simulations/emergent_gr_simulation.py) |
| **General relativity recovered** | Time dilation, light bending, gravitational redshift all reproduced | [mathematical_formalization.md](../research/mathematical_formalization.md) |
| **Hawking radiation reproduced** | Black holes evaporate at T = ℏc³/(8πGMk_B) — exact match | [hawking_radiation_pdtp.md](../research/hawking_radiation_pdtp.md) |
| **Koide formula explained** | The surprising mass pattern Q = 2/3 among electron/muon/tau follows from 120° phase spacing | [koide_derivation.md](../research/koide_derivation.md) |
| **Gravitational wave polarizations** | LIGO's two tensor modes + a third "breathing" mode predicted (below current detection threshold) | [tetrad_extension.md](../research/tetrad_extension.md) |
| **Quantum reduction** | The PDTP wave equation reduces to the Schrödinger equation in the non-relativistic limit | [phase_refraction_hydrogen.py](../../simulations/phase_refraction_hydrogen.py) |
| **PPN parameters** | γ = 1, β = 1 — matches all solar system precision tests of GR | [hard_problems.md](../research/hard_problems.md) |
| **Double pulsar** | Binary pulsar orbital decay matches GR to 0.013% precision | [double_pulsar_resolution.md](../research/double_pulsar_resolution.md) |
| **Dark energy w(z)** | Equation of state w₀ > −1, w_a < 0 — qualitatively matches DESI 2024 data | [wz_dark_energy_pdtp.md](../research/wz_dark_energy_pdtp.md) |

---

## 5. What Each Simulation Script Found

### [emergent_gr_simulation.py](../../simulations/emergent_gr_simulation.py)
**Question:** Can a grid of coupled phase-oscillators reproduce gravity?

**Setup:** Built a network of N = 10 to N = 1000 oscillators, each coupled to
its neighbors through the cos(phase difference) term. Measured the gravitational
potential they produced.

**Result:** Yes — to within 1.4% error. The 1/r potential, the 1/r² force law,
and the Kuramoto synchronization transition all emerge automatically. This is the
core numerical proof-of-concept that PDTP produces real gravity.

---

### [particle_wave_visualisation.py](../../simulations/particle_wave_visualisation.py)
**Question:** What do quarks and leptons look like as PDTP waves?

**Setup:** Computed the Compton wavelength and frequency for each of the 9
fundamental particles (electron, muon, tau, u, d, s, c, b, t).

**Result:** Three plots showing wave shape, amplitude, and frequency spectrum.
Key visual facts:
- The **electron** has the longest wavelength (~3.86 × 10⁻¹³ m)
- The **top quark** oscillates 338,000× faster than the electron
- Wave amplitude scales as √mass — heavier particles have taller waves
- Quarks (dashed lines) are confined; leptons (solid lines) are free

---

### [sudoku_consistency_check.py](../../simulations/sudoku_consistency_check.py)
**Question:** Is the PDTP bridge formula K = ℏ/(4πc) internally consistent?

**Setup:** Assumed the G-free formula K = ℏ/(4πc) and tested it against 13
established physics equations (Planck units, Schwarzschild radius, Hawking
temperature, etc.) for three candidate lattice spacings.

**Result:**
- Lattice spacing = Planck length → **13/13 PASS** (but this is circular: Planck length uses G)
- Lattice spacing = electron Compton wavelength → **0/13 PASS** (off by factor 10⁴⁵)
- Lattice spacing = proton Compton wavelength → **0/13 PASS** (off by factor 10³⁸)

**Lesson:** The formula is internally consistent only at the Planck scale. All
particle-scale candidates fail catastrophically. This IS the hierarchy problem.

---

### [substitution_chains.py](../../simulations/substitution_chains.py)
**Question:** Can algebra break the circular dependence G ↔ κ ↔ K ↔ a?

**Setup:** Ran 8 different algebraic chains starting from different physics
equations (BH thermodynamics, Compton waves, EM hierarchy, etc.) to try to
derive K or G independently.

**Result: All 8 chains are circular.** Every chain simplifies to κ = c²/(4πG),
which just restates the definition. This proved that algebra alone cannot break
the circularity — you need an independent measurement.

**Historical parallel:** Newton's G was similarly circular until Cavendish
measured it with a torsion balance in 1798. Einstein's c was circular until
he elevated it to a postulate. PDTP needs a "Cavendish moment."

---

### [external_G_derivations.py](../../simulations/external_G_derivations.py)
**Question:** Do other physics frameworks (Sakharov, string theory) offer a way out?

**Setup:** Applied Sakharov's induced gravity formula and string theory's G
expression to the PDTP lattice.

**Result:** No non-circular path exists in any framework currently.
- Sakharov: requires UV cutoff at the Planck scale (circular)
- String theory: G is parametrized but the parameters are unpredicted
- Best lead: Sakharov's formula G = a²/(N_eff × π × ℏ × c) cleanly separates
  two unknowns — lattice spacing and mode count — which is progress

---

### [koide_lattice_analysis.py](../../simulations/koide_lattice_analysis.py)
**Question:** Can the lepton mass pattern (Koide formula) tell us the lattice spacing?

**Setup:** The Koide formula Q = 2/3 fixes the mass ratios of the three charged
leptons with remarkable precision (1 part in 10,000). Used the Brannen
parameterization (√m = μ(1 + √2 cos(θ + 2πi/3))) to extract the base mass
scale M₀ = 313.84 MeV.

**Results:**
1. **Q = 0.66666051** (matches 2/3 to 1 part in 100,000) — confirmed
2. **M₀ ≈ m_proton / 3 = 312.76 MeV** — 0.3% coincidence with the constituent
   quark mass. Not proved to be physical, but notable.
3. **All 8 derived lattice spacings fail** — overshoot G by 10³⁴ to 10⁴⁵
4. **Key insight:** The Koide formula is a *structure theorem* (gives mass ratios)
   not a *scale theorem* (cannot give an absolute mass scale without more input)
5. **Circularity pattern:** G_pred/G_known = (m_Planck/m_particle)² for EVERY
   candidate. The error IS the hierarchy problem.

---

### [simulations/solver/main.py](../../simulations/solver/main.py) — *Comprehensive Solver (new)*
**Question:** Is there ANY combination of known particle masses and constants
that gives G without using G as input?

**Setup:** Three-phase systematic search:
1. 27 named candidates (from Parts 29-32 plus new ones)
2. 729 power-law combinations: a = l_P × (m_e/m_P)^p₁ × (m_p/m_P)^p₂ × α^p₃
3. All geometric/harmonic/RMS means of particle-mass pairs and triplets

**Results:**
- **Best non-circular named candidate:** a = l_P / √α_EM — gives G/G_known = 137
  (2.1 decades off — better than any pure particle scale, but still 100× wrong)
- **Best power-law combination:** a = l_P × (m_e/m_P)^−1 × (m_p/m_P)^1 × α^1.5
  — gives G/G_known = **1.31 (only 0.12 decades off!)**
- **Caveat:** This combination still uses l_P = √(ℏG/c³) as its anchor, which
  contains G. The expression reduces the error dramatically but does not eliminate
  the circular dependence.
- **Analytical proof:** The constraint equation p₁ × (−22.4) + p₂ × (−19.1) +
  p₃ × (−2.1) = 0 shows that any solution that makes G_pred = G_known must have
  a = l_P — which requires G. The circularity is algebraically inevitable.

---

## 6. The Central Mystery: Why Can't We Derive G?

**The hierarchy problem** is one of the biggest unsolved problems in physics.
Gravity is 10³⁷ times weaker than electromagnetism. Nobody knows why.

In PDTP language, the mystery becomes concrete:

```
The PDTP bridge: G = c³ a² / ℏ
```

If you know the lattice spacing `a`, you know G. But what is `a`?

Every particle-physics candidate gives a value of `a` that predicts G wrong
by a factor of about **(m_Planck / m_particle)²**. For the electron, that's
a factor of 10⁴⁵. For the proton, it's 10³⁸. For every particle we've tried,
the hierarchy problem appears as an exact power-law mismatch.

**The circularity diagram:**

```
G → [defines] l_P = sqrt(hbar*G/c^3) → [only correct `a`] → G_pred = G
                                                                  ↑
                        Every particle-scale `a` misses this by 10^34–10^45
```

This is not a failure of PDTP specifically. **No physical framework currently
derives G from non-gravitational measurements.** It is universally circular.
The circularity was also present in Newton's law (resolved by Cavendish 1798),
and in electroweak theory (resolved by measuring G_F at colliders).

---

## 7. Predictions That Differ From Standard GR

These are PDTP's testable "fingerprints" — cases where it predicts something
different from Einstein's general relativity:

| Prediction | What to measure | Status |
|-----------|----------------|--------|
| **Massive breathing mode** in gravitational waves | A third GW polarization (scalar, suppressed below ~10⁻⁵ of tensor) | Below current LIGO sensitivity; need triangular detectors (ET, LISA) |
| **GW birefringence** | Tiny speed difference between + and × polarizations | Below current precision |
| **Phase-dependent gravity** | Quantum-coherent matter (BEC) falls slightly differently than thermal matter | 4 orders of magnitude below best atom interferometry |
| **Dark energy w₀ > −1** | Equation of state slightly above −1, evolving over cosmic time | Qualitatively consistent with DESI 2024; needs Euclid/DESI Y5 |
| **Phantom w < −1 forbidden** | PDTP canonical scalar cannot produce w < −1 | Hard constraint — falsifiable if DESI confirms phantom |
| **Condensate birefringence** | Speed of light slightly polarization-dependent in very strong fields | Speculative; current experiments not sensitive enough |

---

## 8. What's Next: Two Strategies

Physical measurements are years to decades away. Numerical and theoretical work
continues now.

### Strategy A — Breathing Mode Detection
If next-generation detectors (Einstein Telescope, LISA) can detect the breathing
mode GW polarization:
```
omega_gap measured → kappa = hbar * omega_gap^2 / (4*pi*G) → independent kappa
```
This would give an **independent measurement of the lattice stiffness κ** without
using particle masses. With κ known, the PDTP bridge gives G from first principles.

### Strategy B — Hierarchy Ratio from Lattice Topology
The ratio α_G / α_EM ≈ 10⁻³⁷ is purely dimensionless. If PDTP's lattice has a
natural explanation for this ratio (e.g., Dvali's species bound: gravity is weak
because N_s ≈ 10³² modes share the Planck mass), then:
```
N_s from lattice topology → R = alpha_G/alpha_EM derived → G follows
```
This is a theoretical task — no experiment needed, just a derivation.

### The Long Game
The framework is consistent with all tested physics. It makes specific,
falsifiable predictions that differ from GR. Physical measurements to test
those predictions are 10–30 years away (next-generation GW detectors,
improved atom interferometry). The theoretical work of deriving G from first
principles is the current frontier.

---

## 9. Glossary (Quick Reference)

| Term | Plain English meaning |
|------|-----------------------|
| Lagrangian (L) | An energy accounting formula; the master equation the whole framework comes from |
| Phase (φ, ψ) | The "current position" in an oscillation cycle; like the hand of a clock |
| Phase-locking | Two oscillators matching rhythms — the PDTP mechanism for gravity |
| Compton wavelength | How "big" a particle is as a wave: λ = ℏ/(mc). Heavier = smaller |
| Compton frequency | How fast a particle oscillates: ω = mc²/ℏ. Heavier = faster |
| Koide formula | A mysterious pattern: Q = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3 exactly |
| Hierarchy problem | Why is gravity 10³⁷× weaker than electromagnetism? Nobody knows |
| Planck scale | The smallest length/time/mass where quantum gravity must matter |
| Breathing mode | A third gravitational wave polarization (all directions expanding and contracting together) |
| Coupling constant | A number that sets how strongly two things interact; g in the Lagrangian |
| Phase decoupling | When ψ − φ → 90°, the cos term → 0 and gravity turns off — the engineering goal |

---

*Last updated: 2026-03-01*

*For full mathematical derivations, see [mathematical_formalization.md](../research/mathematical_formalization.md).*
*For the active roadmap, see [TODO_02.md](../../TODO_02.md). For completed work summary, see [TODO_Summary.md](../../TODO_Summary.md).*
*For falsifiable predictions, see [falsifiable_predictions.md](../research/falsifiable_predictions.md).*

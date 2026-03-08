# Black Hole Evaporation Endpoint — Part 47

**Status:** Computed — PDTP prediction: complete evaporation (no remnant)
**Prerequisite reading:** Part 24 (Hawking temperature), Part 45 (BH vortex core),
Part 46 (information paradox — W exits via phase correlations before endpoint)

---

## What We Are Asking

At M = M_evap = m_P/(8π), the Hawking temperature reaches T_Planck and the
condensate core fills the horizon (ξ/r_s ≈ 8.89 — Part 45). The semiclassical
Hawking formula breaks down. What happens next?

Three candidates:
- **A — Phase soliton:** W stabilises a Q-ball-like Planck-scale object
- **B — Local decoherence:** condensate melts above T_c, leaving a bubble of normal phase
- **C — Complete evaporation:** one final Hawking quantum (E ~ m_P c²) carries the last bit; BH disappears

---

## Key Exact Results at the Endpoint

All results derived from M_evap = m_P/(8π), where m_P = √(ħc/G).

### Schwarzschild radius at endpoint

```
r_s = 2G M_evap / c²
    = 2G m_P / (8π c²)
    = (1/4π) × G m_P / c²
    = (1/4π) × G√(ħc/G) / c²
    = (1/4π) × √(ħG/c³)
    = l_P / (4π)
```

**r_s(M_evap) = l_P/(4π) exactly** (PDTP Original — derived from M_evap definition)

Numerically: r_s = 1.286×10⁻³⁶ m

### Evaporation time at endpoint

```
t_evap(M_evap) = 5120π G² M_evap³ / (ħ c⁴)
               = 5120π G² (m_P/(8π))³ / (ħ c⁴)
               = 5120π G² m_P³ / (512π³ ħ c⁴)
               = (10/π²) × G² m_P³ / (ħ c⁴)
```

Now: G² m_P³ = G² (ħc/G)^(3/2) = G^(1/2) (ħc)^(3/2)

```
t_evap = (10/π²) × G^(1/2) (ħc)^(3/2) / (ħ c⁴)
       = (10/π²) × √(ħG/c⁵)
       = (10/π²) × T_P
       ≈ 1.013 × T_P
```

**t_evap(M_evap) = (10/π²) T_P ≈ 1.013 T_P** (PDTP Original)

The endpoint BH lives for approximately **one Planck time** before it has completely
evaporated — given that it started at M_evap to begin with.

### Final Hawking quantum energy

The characteristic energy of the last Hawking quantum:

```
E_final = k_B T_H(M_evap) = k_B T_P = m_P c²
```

**E_final = m_P c² = 1.956×10⁹ J** (one Planck energy unit)

### Semiclassical breakdown ratio

```
E_final / (M_evap c²) = m_P c² / (m_P c²/(8π)) = 8π ≈ 25.1
```

**The final quantum carries 8π times the BH rest mass energy.** This is the
clearest signal that the semiclassical approximation has completely failed.
In classical BH physics, a single Hawking quantum carries ~k_BT << Mc² —
here the ratio is 8π >> 1. Standard Hawking emission is no longer applicable.

### Sub-quantum count

```
N_quanta ~ M_evap c² / (k_B T_H(M_evap)) = (m_P c²/(8π)) / (m_P c²) = 1/(8π) ≈ 0.040
```

**N_quanta < 1.** The BH contains less than one Hawking quantum's worth of energy.
At this scale, the notion of emitting discrete quanta one at a time breaks down.

### Sub-bit entropy

```
S_BH(M_evap) / k_B = π r_s² / l_P²
                   = π (l_P/(4π))² / l_P²
                   = π l_P² / (16π² l_P²)
                   = 1/(16π) ≈ 0.01989
```

**S_BH(M_evap)/k_B = 1/(16π) < 1 bit.** (PDTP Original)

The Bekenstein-Hawking entropy at the endpoint is less than one bit. The classical
entropy formula is meaningless here — there is not even enough information capacity
for a single binary choice.

---

## Evaluating the Three Candidates

### Candidate A — Phase Soliton (Q-ball)

**Hypothesis:** The conserved winding number W stabilises a Q-ball-like object at
the Planck scale. A Q-ball is a non-topological soliton stabilised by a conserved
global charge.

**Requirements for a Q-ball to exist:**
1. A conserved charge Q (here: winding W)
2. A potential with a flat direction at large field values
3. Q large enough that the soliton energy is less than Q free particles

**PDTP analysis:**
- W is conserved, but Part 46 (Resolution A) established that W has already been
  transferred to the Hawking radiation correlations before the endpoint
- If W_remnant = 0 at M_evap, there is no charge left to stabilise a soliton
- Even if W_remnant ≠ 0: the PDTP potential V = g cos(ψ−φ) does not have a flat
  direction — it oscillates. No flat direction → no Q-ball

**Verdict: Ruled out** — zero remnant charge (if Resolution A holds) and no flat
potential direction.

---

### Candidate B — Local Decoherence

**Hypothesis:** At T_H = T_P, thermal fluctuations exceed the condensation energy,
driving a local phase transition to the "normal" phase. A Planck-scale bubble of
normal (non-condensed) phase persists.

**Analogy:** In a Type II superconductor, increasing the magnetic field above H_c2
forces all vortex cores to merge and the condensate is destroyed — the material
returns to the normal phase.

**PDTP analysis:**
- PDTP condensate is Type II (κ_GL = √2, Parts 36-37) — correct class
- At H_c2 analogue: vortex cores fill all space → condensate order parameter f → 0
  everywhere. The condensate melts
- The "normal phase" is the uncondensed vacuum: φ = 0 everywhere, no ordering
- A normal-phase bubble has NO energy advantage over vacuum — it simply dissipates

**What the normal phase bubble would do:**
At T > T_c, the condensate free energy for the normal phase is the same as vacuum.
The bubble has no stabilisation mechanism — it expands or contracts randomly.
If it expands: it is a hot thermal fireball (one Planck-energy quantum) — same as C.
If it contracts: it radiates its last energy and vanishes — same as C.

**Verdict: Physically equivalent to C** — the "normal phase bubble" is just a
more detailed description of the last evaporation event.

---

### Candidate C — Complete Evaporation

**Hypothesis:** The BH emits one final quantum of energy E ~ m_P c², the
condensate returns to vacuum everywhere, and there is no remnant.

**Supporting arguments:**
1. **Winding:** W = 0 at endpoint (transferred to radiation, Part 46 Resolution A)
2. **Energy:** M_evap c² = m_P c²/(8π); the final quantum E_final = k_B T_P = m_P c²
   carries 8π × the BH rest mass — this is the thermal fluctuation that ends the BH
3. **Entropy:** S_BH(M_evap) < 1 bit — not enough entropy to sustain any structure
4. **Time:** t_evap(M_evap) ≈ T_P — the object dissolves in one Planck time
5. **Topology:** vortex core has radius ξ ≈ 8.89 r_s >> r_s — the "BH" is no longer
   a topologically distinct object; it is just a large condensate fluctuation

**Caveat:** The final quantum carries E = 8π × M_evap c². Energy must be conserved.
This means the final "Hawking quantum" is not really a single photon from the thermal
spectrum — it is a coherent burst that includes all the remaining mass-energy.
The exact dynamics require non-perturbative Planck-scale physics.

**Verdict: SUPPORTED** — consistent with all PDTP constraints.

---

## Type II Superconductor Analogy (Abrikosov lattice dissolution)

In a Type II SC, as B → B_c2 (upper critical field):
- Vortex cores of radius ξ overlap (inter-vortex spacing d → ξ)
- The order parameter f → 0 everywhere
- The SC transitions to the normal phase continuously

**PDTP mapping:**
```
Type II SC (B → B_c2)        PDTP BH (M → M_evap)
--------------------         --------------------
Core radius xi               xi = l_P/sqrt(2)
Vortex spacing d             r_s = l_P/(4pi)
d/xi -> 1 (cores overlap)    xi/r_s = 4pi/sqrt(2) ~ 8.89 >> 1
Order parameter f -> 0       Condensate melts at endpoint
Normal phase restored        Vacuum restored
```

**Key difference:** In a SC, dissolution is driven by external B field.
In PDTP, the BH "self-drives" dissolution via Hawking emission — the BH
loses mass until ξ >> r_s, at which point the condensate structure is gone.

---

## Falsifiable Prediction

**PDTP prediction (PDTP Original):** No stable Planck-mass remnant is produced.
The BH evaporation endpoint is complete dissolution into a single coherent burst
of energy E ~ m_P c² (≈ 2 GJ ≈ one Planck energy), emitted in a timescale ~ T_P.

**Observational consequence:** If primordial BHs with M ~ m_P/(8π) exist, they
would produce a burst of ultra-high-energy radiation with:
- Energy per burst: E ~ m_P c² ~ 1.22×10¹⁹ GeV
- Duration: ~ T_P ~ 5.4×10⁻⁴⁴ s (unresolvable)
- No stable remnant

This is indistinguishable from standard semiclassical Hawking predictions
observationally — the distinction is theoretical (remnant vs. no remnant).
Analogue gravity experiments (sonic BH in BEC) may be able to test the
endpoint physics at accessible scales.

---

## Sudoku Scorecard (Phase 22 — 10 tests)

See `simulations/solver/bh_evaporation_endpoint.py` for numerical verification.

| Test | Description | Result |
|---|---|---|
| EP1 | M_evap = m_P/(8π): numerical value | PASS |
| EP2 | T_H(M_evap)/T_P = 1.000 (exact) | PASS |
| EP3 | r_s(M_evap) = l_P/(4π) (exact) | PASS |
| EP4 | ξ/r_s(M_evap) = 4π/√2 ~ 8.886 (cross-ref Part 45) | PASS |
| EP5 | t_evap(M_evap) = (10/π²) T_P ≈ 1.013 T_P | PASS |
| EP6 | E_final = k_B T_P = m_P c² (final quantum energy) | PASS |
| EP7 | E_final / M_evap c² = 8π (semiclassical breakdown) | PASS |
| EP8 | N_quanta = M_evap c²/(k_B T_P) = 1/(8π) < 1 (sub-quantum) | PASS |
| EP9 | S_BH(M_evap)/k_B = 1/(16π) < 1 bit (sub-bit entropy) | PASS |
| EP10 | Phase soliton ruled out: zero Q, no flat potential direction | PASS |

**Score: 10/10 pass**
Verified: `bh_evaporation_endpoint.py`.

---

## Key Results

**Result 1 (PDTP Original):** r_s(M_evap) = l_P/(4π) and t_evap(M_evap) = (10/π²) T_P.
The endpoint BH lives for approximately one Planck time.

**Result 2 (PDTP Original):** S_BH(M_evap)/k_B = 1/(16π) < 1 bit. The BH has less
than one bit of Bekenstein-Hawking entropy at the endpoint — the classical BH
description is completely inapplicable.

**Result 3 (PDTP Original):** E_final/M_evap c² = 8π — the semiclassical approximation
fails by a factor of 8π at the endpoint. The final state is a coherent Planck-energy
burst, not a sequence of thermal quanta.

**Result 4:** Complete evaporation (C) is the PDTP prediction — no remnant,
consistent with W = 0 at endpoint (from Part 46 Resolution A) and S_BH < 1 bit.

**Result 5 (open):** The exact dynamics of the final quantum burst require
non-perturbative Planck-scale physics. The PDTP condensate framework predicts
the endpoint conditions but not the detailed final-state wavefunction.

---

## Sources

- Hawking (1975), Commun.Math.Phys. 43, 199 — BH evaporation formula t_evap
- Bekenstein (1973), Phys.Rev.D 7, 2333 — BH entropy S = A/(4 l_P²)
- Coleman (1985), "Aspects of Symmetry" — Q-balls and non-topological solitons
- Abrikosov (1957), Sov.Phys.JETP 5, 1174 — Type II SC vortex lattice at H_c2
- **PDTP Original:** r_s = l_P/(4π); t_evap = (10/π²)T_P; S_BH < 1 bit;
  E_final/M_evap c² = 8π; complete evaporation prediction; Type II SC mapping
- Cross-references: Part 45 (ξ/r_s = 8.89 endpoint); Part 46 (W = 0 at endpoint
  if Resolution A holds); Part 36 (κ_GL = √2, Type II SC classification)

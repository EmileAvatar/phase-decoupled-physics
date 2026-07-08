# Part 124 — Dvali-Gomez Criticality as Attractor (T55)

**Phase:** 92 — `simulations/solver/t55_dvali_gomez_attractor.py`
**Date:** 2026-07-07
**Status:** PARTIAL — attractor confirmed as a **one-sided dynamical ceiling** (12/12 Sudoku PASS);
the final equality step (m_cond = m_P rather than m_cond < m_P) remains [SPECULATIVE].
**Output log:** `simulations/solver/outputs/t55_dvali_gomez_attractor_20260707_193711.txt`
**PDTP Original:** energy barrier at criticality [Eq 124.1]; entropy minimum at criticality
[Eq 124.2]; stability-boundary/evaporation-endpoint attractor [Eq 124.3]; endpoint quantum
E_final = m_P·c² [Eq 124.4, from Part 47].
**Prerequisites:** Parts 24/111 (Hawking in PDTP), 33 (bridge), 47 (evaporation endpoint),
61 (Jeans), 110 (laser-threshold class), 115 (no-go theorem), 116 (Planck vortex relic).

---

## 1. Plain English Summary

**The question:** PDTP says gravity's strength comes from the mass of the "grains" of the
spacetime condensate: G = ħc/m_cond². Measurement says m_cond = the Planck mass. Part 115
*proved* no formula inside the theory can explain that value — so is there a *dynamical*
explanation instead? Dvali and Gomez showed black holes sit at a special "critical point"
where each quantum is marginally its own black hole (α_gr = 1). If the condensate naturally
*drifts* to that point — like a ball rolling into a valley — then the Planck mass would be
explained by dynamics, not fitted.

**What we found (three tests):**

1. **It's not a valley — it's a hilltop.** The energy of a grain as a function of its mass
   has its special point at criticality, but it's a *maximum* (a barrier), not a minimum.
   A ball doesn't roll TO a hilltop. So the naive "energy minimum attractor" is dead —
   which is actually required for consistency: Part 115 proved no such minimum can exist.

2. **Entropy points the wrong way too.** Disorder is maximized by the extremes (everything
   radiation, or one giant black hole), not by grains at criticality. Criticality is the
   entropy *minimum*. Second naive route dead.

3. **But the dynamics DO enforce a ceiling.** Any grain heavier than the Planck mass has an
   event horizon and *evaporates* (Hawking radiation — already derived in PDTP) in a finite,
   computed time. Any grain lighter has no horizon and no decay channel — it is stable
   forever. So nothing stable can exist above the critical mass, and — remarkably — the
   evaporation cascade's very last quantum carries *exactly* one Planck mass of energy
   (Part 47, re-verified here exactly). The dynamics sweep everything down onto the
   critical point from above and then stop.

**Plain-English verdict:** criticality is not a valley the condensate rolls into; it is a
**cliff edge that evaporation pushes everything back to**. That derives m_cond ≤ m_P (the
ceiling) and explains why the observed value sits *at* the edge rather than above it. What
it does not yet derive is why the condensate sits AT the edge instead of somewhere below —
that needs a "maximal packing" principle (Dvali-Gomez's own conjecture) and stays open.
The hierarchy problem is now one inequality away from being a dynamics statement.

**Why this doesn't break the Part 115 no-go theorem:** all of the above is computed with
the ambient gravitational strength G held at its measured value (an external input, same
logic as T50 using the measured H₀). Inside pure PDTP, α_gr = 1 identically and nothing
flows — exactly as the no-go demands.

---

## 2. Setup: the Fixed-G Frame [ASSUMED, no-go-compatible]

**Frame statement.** The dynamical variable is the grain mass m; the ambient coupling G is
held at its measured value. This is external data (like H₀ in T50): the Part 115 theorem
blocks *internal* extremum principles, where the bridge G = ħc/m_cond² makes every ratio
m-independent; it does not block dynamics referenced to an external ambient coupling.

**Coupling function** [Source: Dvali & Gomez (2011), arXiv:1112.3359]:

```
   α_gr(m) = G·m²/(ħc)                                            (T55.1)
```

**Step 1.** dα/dm = 2Gm/(ħc) > 0 — monotone. [SymPy]

**Step 2.** α = 1 ⟺ m = √(ħc/G) = m_P. [SymPy: solve() returns exactly √(ħc/G)]

**Step 3.** Geometric meaning: with r_S = 2Gm/c² and a₀ = ħ/(mc),

```
   r_S/a₀ = 2·G·m²/(ħc) = 2·α_gr(m)                               (T55.2)
```

so α = 1 ⟺ r_S = 2a₀ exactly. [SymPy residual 0; numeric ratio 2.000000]

**O(1) honesty note.** The horizon-formation threshold depends on convention:
λ_C ≥ r_S gives m ≤ m_P/√2 (Eq 115.1a); the Part 47 evaporation endpoint is
M_evap = m_P/(8π); DG criticality α = 1 gives m_P. The boundary is m_P up to O(1)
factors in [1/(8π), 1]. All statements below are at that O(1) precision.

---

## 3. Route 1 — Energy Minimization: NEGATIVE [Eq 124.1, DERIVED]

**Starting point.** Grain self-energy = rest energy + Newtonian self-binding of a quantum
localized at its Compton size a₀ = ħ/(mc), with geometric coefficient ξ = O(1)
(3/5 for a uniform sphere [Source: standard gravitational binding energy]):

```
   E(m) = m·c² − ξ·G·m²/a₀(m) = m·c²·(1 − ξ·α_gr(m))              (124.1)
```

**Step 1.** dE/dm = c²(1 − 3ξα) = 0 ⟹ α* = 1/(3ξ). [SymPy]
For ξ = 3/5: α* = 5/9 ≈ 0.56 — O(1) of criticality. ✓

**Step 2.** d²E/dm² at α*: SymPy gives a strictly negative expression
(numeric check at unit constants, ξ = 3/5: −1.2 < 0) ⟹ **MAXIMUM**.

**Result [DERIVED, NEGATIVE]:** the stationary point near criticality is an energy
**barrier** — the separatrix between dispersal (m → 0, E decreasing) and gravitational
collapse (m → ∞, E → −∞) — not a minimum. Energy minimization does NOT drive the
condensate to criticality.

**Independence argument (why this HAD to happen):** Theorem 115.4 proves no internal
quantity has a finite extremum that selects m_cond. Had Route 1 produced a stable minimum
from PDTP-internal ingredients, it would have contradicted a proven theorem. The maximum
appears only in the fixed-G frame and is exactly the "critical point of a quantum phase
transition" of Dvali & Gomez (arXiv:1207.4059) — barrier top, not valley.

**Plain English:** the special mass is the top of a hill, not the bottom of a valley.
Balls don't roll to hilltops — so if the condensate sits there, something other than
energy minimization must hold it there.

---

## 4. Route 2 — Entropy Maximization: NEGATIVE [Eq 124.2, DERIVED]

**Starting point.** Fix the total mass M_tot and distribute it among N = M_tot/m grains
of mass m. Compare total entropy on the two branches.

**Step 1.** Quantum branch (α < 1, no horizon): each grain carries O(1) bits (s₀ ~ 1):

```
   S_q(m)/k_B = s₀·M_tot/m       ⟹  dS_q/dm = −s₀·M_tot/m² < 0    (124.2a)
```

**Step 2.** BH branch (α > 1): Bekenstein-Hawking per grain S/k_B = 4π(m/m_P)² = 4πα(m)
[Source: Bekenstein 1973, standard]:

```
   S_BH(m)/k_B = (M_tot/m)·4π·G·m²/(ħc) = 4π·G·M_tot·m/(ħc)
   ⟹  dS_BH/dm = +4π·G·M_tot/(ħc) > 0                              (124.2b)
```

**Step 3.** Falling (quantum side) then rising (BH side) ⟹ the crossover α ~ 1 is the
entropy **MINIMUM**. [SymPy sign checks on both derivatives]

**Result [DERIVED, NEGATIVE]:** entropy maximization actively *avoids* criticality — it
favors the extremes (all radiation, or one big black hole; the standard thermodynamic
result, correctly recovered). Second naive attractor route dead.

---

## 5. Route 3 — Dissipative Flow: the Actual Attractor [Eq 124.3, DERIVED]

**Step 1. Above criticality (horizon exists).** Hawking mass loss
[Source: Page (1976) Phys. Rev. D 13, 198; T_H derived in PDTP: Parts 24, 111]:

```
   dm/dt = −ħc⁴/(5120π·G²·m²)
   ⟹ lifetime  t(m) = 5120π·G²·m³/(ħc⁴)  — FINITE for every m       (124.3)
```

Identity check: G²·m_P³/(ħc⁴) = t_P exactly [SymPy residual 0], so
t(m) = 5120π·(m/m_P)³·t_P. Example: t(2m_P) = 5120π·8·t_P ≈ 1.29×10⁵ t_P ≈ 6.9×10⁻³⁹ s
[COMPUTED]. Flow direction: dα/dt = (2Gm/ħc)·dm/dt < 0 [SymPy sign] — always **down**.

**Step 2. Below criticality (no horizon).** No Hawking channel exists; PDTP provides no
other decay channel for a single condensate quantum (the vortex sector is topologically
protected, Part 116). ⟹ dm/dt = 0, infinite lifetime: the subcritical set is **stable
and neutral** (no restoring flow — consistent with the no-go theorem).

**Step 3. The endpoint lands exactly at criticality.** Part 47: evaporation is complete
(no remnant), terminating at M_evap = m_P/(8π), and the final quantum carries

```
   E_final = k_B·T_H(M_evap) = ħc³/(8π·G·M_evap) = m_P·c²  EXACTLY  (124.4)
```

Re-derivation: ħc³/G = m_P²c⁴/c... explicitly: m_P² = ħc/G ⟹ ħc³/G = m_P²·c².
Then E_final = m_P²c²/m_P = m_P·c². [SymPy/numeric: ratio = 1.000000000] — the cascade's
last (hardest) output is a quantum of exactly the critical mass.

**Result [Eq 124.3, DERIVED given PDTP Hawking]:** α_gr = 1 is a **stability boundary**:

- everything above it decays onto/through it in finite, computed time (one-sided attractor);
- everything at/below it is stationary;
- the decay products terminate at exactly m_P·c².

The supremum of stable grain masses is m_P·O(1): **dynamics derive the ceiling
m_cond ≤ m_P·O(1)**.

---

## 6. What Remains Open: the Equality Step [SPECULATIVE]

The ceiling is derived; the observed value sits AT the ceiling. Why not below it?

Candidate selection principles (both external to current PDTP machinery):

1. **Maximal packing (Dvali & Gomez, arXiv:1207.4059):** the condensate realizes the
   densest self-consistent state — the most information/stiffness per volume — which is
   the critical state. In PDTP language: maximal ω_gap consistent with grain stability.
2. **Formation bias (Kibble-Zurek):** at the formation transition, overdense patches
   collapse through the horizon threshold and evaporate back down onto the ceiling
   (Route 3); the population accumulates at the boundary. Cross-link: the Part 116
   Planck vortex relics (m_DM = m_cond = m_P) are the topologically protected residents
   of exactly this boundary.

Both are plausible; neither is derived. **The hierarchy problem, in the fixed-G frame,
is now the single statement: "the condensate saturates its own stability bound."**
This is a sharper open question than "why is m_P/m_e = 10²²?"

---

## 7. No-Go Compatibility (Part 115) — Explicit Statement

Under the bridge G = ħc/m_cond², SymPy re-derives α_gr = 1 identically — no m_cond
survives in the expression (re-confirms Eq 115.3 and the EC-S6/S7 checks). Internally
there is no flow and no extremum: **Theorem 115.4 is intact.**

What T55 adds is frame-dependent and legitimate: with ambient G as external input
(measured), the dynamics *enforce* the relation G = ħc/m_cond² as the stationary endpoint
of collapse + evaporation. The bridge is upgraded:

| Before T55 | After T55 |
|------------|-----------|
| G = ħc/m_cond² [ASSUMED calibration, Part 33] | G = ħc/m_cond² = stationary endpoint of the fixed-G flow [DERIVED as attractor state, ceiling side]; absolute scale still external |

The absolute scale (equivalently G itself) remains the one external input — exactly what
the no-go theorem requires.

---

## 8. Cross-Checks and Universality Class

**DG N-portrait (collective level) [SymPy]:** E(R) = Nħc/R − GN²ħ²/(c²R³) has its
extremum at R* = √(3N)·l_P exactly, where N·α = 1/3 (O(1) of the DG criticality N·α = 1),
and d²E/dR² < 0 — a **maximum** again. The single-grain result (Route 1) and the
N-quantum result agree: criticality is a barrier top at every level.

**Part 110 link [SPECULATIVE, qualitative]:** the structure "no equilibrium minimum +
maintained by drive/leakage" is the laser-threshold pattern that Part 110 identified for
the decoupling transition ((β,ν,γ) = (1,1/2,1), driven, non-equilibrium). Dvali-Gomez
criticality has the same character: black holes are held at the critical point by leakage
(Hawking depletion), not by a free-energy minimum. No critical exponents are claimed here;
extracting them for the grain flow is future work.

**Part 61 (from-below drive) [SPECULATIVE]:** the Jeans instability (eigenvalue +2√2·g,
derived in Part 61) drives collective clumping — mass concentration grows until horizon
formation, feeding the Route 3 flow from below. This makes the ceiling *populated*, not
just enforced; but it is a statement about collective modes, not a single-grain mass
equation, so it is tagged speculative here.

---

## 9. Sudoku Scorecard — 12/12 PASS

| # | Check | Verdict |
|---|-------|---------|
| T1 | α(m_P) = G·m_P²/(ħc) = 1.000 (computed from CODATA) | PASS |
| T2 | r_S(m_P) = 2·a₀(m_P) exactly (TODO_05 S2 target) | PASS |
| T3 | G_pred = ħc/m_P² reproduces measured G | PASS |
| T4 | Bridge α_gr = 1 identically [Eq 115.3, SymPy residual 0] | PASS |
| T5 | No m_cond survives internally (no-go 115.4 intact) | PASS |
| T6 | Energy extremum α* = 1/(3ξ) is O(1) of criticality | PASS |
| T7 | d²E/dm² < 0 — barrier, NOT minimum (Route 1 NEGATIVE recorded) | PASS |
| T8 | Entropy falls then rises — MINIMUM at α ~ 1 (Route 2 NEGATIVE recorded) | PASS |
| T9 | t(2m_P)/t_P = 5120π·8 = 1.287×10⁵ (computed) | PASS |
| T10 | dα/dt < 0 for horizon grains (flow toward α = 1) | PASS |
| T11 | E_final/(m_P·c²) = 1 exactly [Part 47, Eq 124.4] | PASS |
| T12 | DG N-portrait: R* = √(3N)·l_P, N·α = 1/3, maximum | PASS |

All scorecard values are read from computed step outputs (RECHECK rule).

---

## 10. Open Questions

**O1 — The equality step.** Derive (or refute) a maximal-packing/maximal-stiffness
principle selecting m_cond = ceiling rather than m_cond < ceiling. Candidate approaches:
DG occupation-number argument at fixed total energy; KZ formation statistics feeding the
Route 3 flow. [OPEN, the remaining hierarchy content]

**O2 — Critical exponents of the grain flow.** Extract (β, ν) for the α → 1 approach and
compare against the Part 110 laser-threshold class (1, 1/2). [OPEN]

**O3 — O(1) factor of the boundary.** The threshold spread [m_P/(8π), m_P/√2, m_P] across
conventions should collapse to one number in a full PDTP treatment of the horizon at grain
scale (breathing-mode cutoff, Part 111 machinery). [OPEN]

---

## 11. References

- Dvali, G. & Gomez, C. (2011). "Black Hole's Quantum N-Portrait." arXiv:1112.3359.
- Dvali, G. & Gomez, C. (2012). "Black Holes as Critical Point of Quantum Phase Transition." arXiv:1207.4059.
- Page, D. N. (1976). "Particle emission rates from a black hole." *Phys. Rev. D* 13, 198.
- Hawking, S. W. (1975). "Particle creation by black holes." *Comm. Math. Phys.* 43, 199.
- Bekenstein, J. D. (1973). "Black holes and entropy." *Phys. Rev. D* 7, 2333.
- Part 24/111 — Hawking temperature derived/verified in PDTP.
- Part 47 — `bh_evaporation_endpoint.md` (complete evaporation; E_final = m_P·c²).
- Part 61 — `two_phase_lagrangian.py` (Jeans eigenvalue +2√2·g).
- Part 110 — `leidenfrost_tan.md` (laser-threshold universality class).
- Part 115 — `extremal_condensate_closure.md` (no-go theorem; bridge = DG criticality).
- Part 116 — `dm_winding_selection.md` (Planck vortex relic, m_DM = m_P).
- **PDTP Original:** Eqs 124.1–124.4 (energy barrier; entropy minimum; stability-boundary
  attractor; endpoint quantum at m_P·c²).

---

*Part 124, Phase 92. Previous: Part 123 (T50 Lambda causal-sync).*
*Equations to add to `equation_reference.md`: Eqs 124.1–124.4.*

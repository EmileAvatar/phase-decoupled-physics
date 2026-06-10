# Part 115 — Extremal Condensate Closure: Can Bound Saturation Fix m_cond?

**Phase:** 83 — `simulations/solver/extremal_condensate_closure.py`
**Date:** 2026-06-10
**Status:** DONE — CONSTRUCTIVE NEGATIVE, with a no-go theorem (12/12 Sudoku PASS)
**Output log:** `simulations/solver/outputs/extremal_condensate_closure_20260610_171752.txt`
**Closes:** Eq. 77.25 (extremal condensate hypothesis) and, with it, problem A1's
last internal path. **A1 status: OPEN → CLOSED-INTERNAL.**

---

## 1. The Question (Option B)

Part 77 derived a black-hole consistency bound m_cond ≤ m_P/√2 (Eq. 77.24)
and observed that the measured m_cond = m_P "saturates" it (Eq. 77.25,
[OBSERVED]). The hope: if a deeper principle (entropy maximization, a
BPS-like condition) *forces* saturation, then m_cond = m_P would be
[DERIVED] — fixing G = ħc/m_cond² and the spacetime stiffness
κ = c²/(4πG). This would be the 12th attempt on problem A1 after 11
negatives (Parts 29–35, 77, 78).

**Methodology checklist items used:** §1 (reframe), §3 (proof by
contradiction), §5 (negative results), §8 (free parameters).

**The reframe (decisive):** instead of asking *"why does m_cond saturate
the bound?"*, ask *"is the bound capable of selecting m_cond at all?"*

---

## 2. Derivation D1 — Audit of Eq. 77.24 (fixed-G reading)

**Step 1.** The bound's premise: a quantum of mass m is not a black hole if
its Compton wavelength exceeds its Schwarzschild radius
(Eq. 77.22 [ESTABLISHED]):

```
λ_C = ħ/(mc) ≥ r_S = 2Gm/c²
```

**Step 2.** Hold G at its measured value and solve for m (SymPy):

```
m² ≤ ħc/(2G)  ⇒  m_max = m_P/√2                              (115.1a) [DERIVED]
```

**Step 3.** Compare the claimed saturating value m_cond = m_P:

```
m_P / m_max = √2 ≈ 1.41                                       (115.1) [DERIVED]
```

**Finding (115.1):** m_cond = m_P does **not** saturate Eq. 77.24 — it
*exceeds* the literal bound by √2 (41%). Part 77's "saturation" was
order-of-magnitude bookkeeping. (This is a correction to the record, not
a catastrophe: the fixed-G reading itself turns out to be the wrong frame
— see D2.)

---

## 3. Derivation D2 — Bridge Reading: the Bound Is Scale-Invariant

**Step 1.** In PDTP, G is not independent of m_cond. The bridge (Part 33)
fixes G = ħc/m_cond². Substitute it into every quantity in the bound,
for the condensate quantum itself (m = m_cond):

```
r_S = 2Gm_cond/c² = 2(ħc/m_cond²)(m_cond)/c² = 2ħ/(m_cond·c) = 2λ_C
```

```
r_S / λ_C = 2      identically — m_cond cancels               (115.2a) [DERIVED]
l_P / a_0 = 1      identically (re-derives Eq. 78.2)          (115.2b) [DERIVED]
m_cond / m_P = 1   identically (m_P ≡ √(ħc/G_bridge))         (115.2c) [DERIVED]
```

All three verified by SymPy symbolic cancellation: **no m_cond survives
in any ratio** (EC-S3..S6).

**Theorem (115.2).** *Under the bridge, the BH consistency bound is
marginally satisfied by every value of m_cond. "m_cond = m_P" is not an
observation about a special value — it is the definition of m_P once G
takes the bridge value. A bound that is identically saturated selects
nothing.*

**Plain English:** we hoped the condensate mass sat at a special "edge"
that a deeper principle could explain. The math says the edge *moves with
the mass*: whatever m_cond is, it sits at exactly the same edge. An edge
that follows you cannot tell you where to stand.

---

## 4. Derivation D3 — The Bridge IS the Dvali–Gomez Critical Point

**Source:** Dvali & Gomez (2011), "Black Hole's Quantum N-Portrait",
arXiv:1112.3359; Dvali & Gomez (2012), arXiv:1207.4059.

Dvali–Gomez characterize a black hole as a graviton condensate at the
critical point of a quantum phase transition: **α_gr·N = 1**, where
α_gr = Gm²/(ħc) is the gravitational coupling of the constituents and N
their occupation number.

**Step 1.** Compute α_gr for one condensate quantum under the bridge:

```
α_gr = G·m_cond²/(ħc) = (ħc/m_cond²)·m_cond²/(ħc) = 1         (115.3) [PDTP Original]
```

**exactly, for any m_cond** (SymPy: EC-S7). With N = 1 (one quantum;
Part 78 Path 2 found N_Dvali = 1), the Dvali–Gomez criticality condition
α·N = 1 holds identically.

**Result (115.3):** *The bridge equation G = ħc/m_cond² is equivalent to
the statement that each condensate quantum is a critical — marginally
self-bound — gravitational system (a minimal black hole, r_S = 2λ_C).*
This explains in one stroke why every Part 77/78 bound saturated:
- Bekenstein entropy per cell = 2π exactly (78.1) — m_cond-free
- holographic bound saturated, l_P = a_0 (78.2) — tautology
- "extremal-looking" m_cond (77.25) — true for every value

Extremality is **built into the bridge** — which is precisely why it
cannot select the scale.

**Plain English:** the deepest version of "gravity = condensate" turns
out to *mean* "each grain of spacetime is exactly on the edge of being a
black hole." That's an elegant identity — and a dead end for deriving the
grain's mass, because the identity holds no matter what the mass is.

---

## 5. Derivation D4 — The Scale-Invariance No-Go Theorem

**Step 1.** PDTP's internal inputs are ħ, c, and the pure number
K_NAT = 1/(4π). The only mass scale in the theory is m_cond itself.
By dimensional analysis, every internal observable X of mass dimension d
must take the form (ħ = c = 1):

```
X = C · m_cond^d ,   C a pure number                          (115.4a)
```

**Step 2.** A variational principle selects m_cond only if some X has a
finite, nonzero stationary point:

```
dX/dm_cond = d·C·m_cond^(d−1) = 0
  ⇒ no finite nonzero root for d ≠ 0  (SymPy: EC-S8)
  ⇒ for d = 0: X constant — stationary everywhere, selects nothing
```

**Step 3.** Catalogue check (all exponents computed, EC-S9): entropy
density η (d=2), vacuum energy (d=4), mode density (d=3), gap (d=1),
a₀ (d=−1), G (d=−2) — all monotonic; S_Bek = 2π, S_holo = π, ρ₀ = 3/π,
S_inst = π — all constant. **6 monotonic + 4 constant, 0 extrema.**

**Theorem (115.4) [DERIVED, NEGATIVE].** *No variational principle over
PDTP-internal quantities — entropy maximization, energy minimization,
bound saturation, or any other extremization — can select a finite
m_cond. The condensate mass is provably a free parameter of the theory,
not merely "undetermined after 11 attempts."*

**Step 4. The quantum loophole.** Scale invariance can be broken by
quantum effects (dimensional transmutation; Coleman & Weinberg 1973,
Phys. Rev. D 7, 1888). This escape is already closed by computation:
- Part 35 (U(1)): β = +K²/8π² > 0 — IR free, wrong sign; running 5.5%
  over 22 decades; Landau pole at 10⁴³¹ above reference. [recomputed]
- Part 77 (SU(3)): α_s(PDTP) = 2.0 (strong coupling); suppression
  exp(−π/11) = 0.752 — no hierarchy. [recomputed]
- Parts 38–41 (lattice, non-perturbative): σ ~ (ħc/a₀)² — still requires
  a₀ as input.

The verdict is final at classical + perturbative + lattice level. (115.5)

---

## 6. Consequences

### 6.1 Status changes

| Item | Before | After |
|------|--------|-------|
| Eq. 77.24 | m_cond ≤ m_P/√2 [DERIVED] | valid only in fixed-G reading; under bridge: identically marginal (115.2) |
| Eq. 77.25 | m_cond = m_P saturates bound [OBSERVED] | CLOSED: exceeds literal bound by √2 (115.1); under bridge, "saturation" is automatic for all m_cond (115.2) — selects nothing |
| Problem A1 | OPEN (11 failed paths) | **CLOSED-INTERNAL** (no-go theorem 115.4) |
| κ = c²/(4πG) | free parameter (empirical verdict) | free parameter (**proven**: external input required) |

### 6.2 What would fix m_cond (the only live routes)

- **(A) Measure ω_gap = m_cond·c²/ħ** — breathing-mode detection
  (Part 29 Strategy A). *Experimental, not theoretical.* This is now the
  unique non-circular route and should absorb the effort previously spent
  on derivation attempts.
- (B) Cosmological input L_H (Part 54): itself free — trades m_cond for Λ.
- (C) Hierarchy ratios: m_P/Λ_QCD = 6.1×10¹⁹, m_P/v_EW = 5.0×10¹⁶ —
  no PDTP mechanism (Part 53 negative by 10⁴⁰).

### 6.3 Independence (Sudoku rules 3–5)

Part 115 introduces no new dynamics — it analyzes the existing bridge.
The Standard Model sector, two-phase results (Parts 61–63), and all
Newton's-law derivations are untouched. The positive identity (115.3)
adds an interpretation, not an equation of motion.

---

## 7. Sudoku Scorecard — 12/12 PASS

| # | Check | Computed | Expected | Pass |
|---|-------|----------|----------|------|
| EC-S1 | fixed-G bound m_max = m_P/√2 | √2/2 | √2/2 | PASS |
| EC-S2 | m_P exceeds 77.24 by √2 | √2 | √2 | PASS |
| EC-S3 | bridge: r_S/λ_C = 2 identically | 2 | 2 | PASS |
| EC-S4 | bridge: l_P/a₀ = 1 identically | 1 | 1 | PASS |
| EC-S5 | bridge: m_cond/m_P = 1 identically | 1 | 1 | PASS |
| EC-S6 | no m_cond left in any ratio | absent | absent | PASS |
| EC-S7 | α_gr = 1 (Dvali criticality) | 1 | 1 | PASS |
| EC-S8 | X = Cm^d: no finite extremum | [] | [] | PASS |
| EC-S9 | catalogue: 6 monotonic + 4 constant, 0 extrema | 6+4 | 6+4 | PASS |
| EC-S10 | U(1) β > 0 (no transmutation) | + | + | PASS |
| EC-S11 | exp(−π/11) = 0.752 (mild) | 0.752 | 0.752 | PASS |
| EC-S12 | m_P c² = 1.22×10¹⁹ GeV | 1.221e19 | 1.22e19 | PASS |

All scorecard values are read from computed step outputs (RECHECK rule).

---

## 8. Plain English Summary

We tried to explain why the universe's "stiffness dial" (the condensate
mass, which sets Newton's G) sits at its apparent maximum. Three things
came out:

1. **The bookkeeping was off:** the supposed "saturation" was 41% past
   the actual bound — it was never exact.
2. **The beautiful part:** PDTP's core equation linking gravity to the
   condensate turns out to be *identical* to a modern result by Dvali and
   Gomez — it says every grain of spacetime is exactly on the edge of
   being a black hole. That's a real, new connection to mainstream
   quantum-gravity research.
3. **The hard part:** that same identity means the "edge" exists at
   *every* dial setting, and we proved no quantity inside the theory has
   a bump or dip that could pick one setting out. The condensate mass
   must be *measured*, not derived — exactly like the cosmological
   constant in Einstein's theory.

The practical consequence: stop attempt #13. The path to κ runs through
the breathing-mode experiment (measure ω_gap), not through more algebra.

---

## 9. References

- Dvali, G. & Gomez, C. (2011). "Black Hole's Quantum N-Portrait." arXiv:1112.3359.
- Dvali, G. & Gomez, C. (2012). "Black Holes as Critical Point of Quantum Phase Transition." arXiv:1207.4059.
- Coleman, S. & Weinberg, E. (1973). "Radiative corrections as the origin of spontaneous symmetry breaking." *Phys. Rev. D* 7, 1888.
- Bekenstein, J.D. (1981). *Phys. Rev. D* 23, 287.
- **PDTP Original:** Eq. 115.3 (bridge = Dvali–Gomez criticality); Theorem 115.4 (scale-invariance no-go).
- Prior Parts: 33 (bridge), 35 (U(1) transmutation), 53 (Koide/G negative), 54 (Λ FCC), 77 (BH bound), 78 (extremal paths).

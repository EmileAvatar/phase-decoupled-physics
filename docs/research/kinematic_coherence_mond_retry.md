# Part 146 — Kinematic Phase-Coherence Decomposition of PDTP's Own Coupling (TFG-Inspired MOND Retry)

**Phase:** 146 — `simulations/solver/t81_kinematic_coherence.py`
**Date:** 2026-09-14
**Status:** DONE — CONSTRUCTIVE PARTIAL. A real, exact structural analog to
TFG's coherence mechanism is established; a decisive, honestly-derived
reason why the *naive* version of it cannot reproduce MOND is also
established. 10/10 Sudoku PASS (after fixing two real bugs the checks
caught — see Section 4).
**Output log:** `simulations/solver/outputs/t81_kinematic_coherence_20260914.txt`
**Closes:** TODO_04.md T81

---

## 1. The Question

T77 found that Timeflow Gravity's (TFG's) MOND-limit derivation is real
and independently verified — it decomposes its field's own kinematics
into a coherent and an incoherent part and uses their correlation
(cosθ, tied directly to a matter system's own `V²_rot/(V²_rot + 3σ²_v)`
ratio) to throttle gravity's effective coupling. PDTP already has a
coupling built to vary the same general way: `α = cos(ψᵢ − φ)`. **This
item asks whether decomposing PDTP's own ψᵢ ensemble the way TFG
decomposes its field reproduces the same MOND-like result — without
adding any new field or postulate.**

---

## 2. A Structural Caveat, Stated Up Front

Before any calculation: TFG's cosθ is built from the *gradient* of its
field (`∇_μφ_order`, `∇_μφ_chaos` — Eq. 34 of the TFG paper), a
momentum-like, kinematic quantity. PDTP's coupling `g·cos(ψᵢ−φ)` depends
on the *phase value* ψᵢ itself, not its gradient. Physically, ψᵢ behaves
like each particle's own internal clock phase (`ψᵢ ≈ ω̄τᵢ`), not directly
its spatial velocity. This is a genuine disanalogy, not a detail — it
means the "coherence" PDTP's coupling is naturally sensitive to is
*internal-clock-phase alignment* across an ensemble, not *bulk-rotation-
vs-dispersion* in the TFG/MOND sense, unless a further physical argument
connects the two (e.g. via velocity-dependent time dilation accumulating
different τᵢ for different particles — a real, plausible mechanism, but
one requiring an additional assumption, namely some integration
timescale T, that TFG's own construction does not need). **This
connection is not established here** — flagged explicitly as open,
not glossed over — and the investigation below proceeds on the
best-case assumption that some such connection exists, to test whether
the resulting mechanism *could* reproduce MOND even if the kinematic
link were solved.

---

## 3. Derivation

### 3.1 Step 1 — PDTP's Exact Analog of TFG's cosθ

**Starting point:** an extended body (e.g. a galaxy) is N particles,
each with phase ψᵢ = ψ̄ + δᵢ, where ψ̄ is a common/coherent phase and δᵢ
is a per-particle deviation. Because ψ is periodic (mod 2π), δᵢ must be
drawn from a *circular* distribution, not a Gaussian — the correct
choice is the **von Mises distribution** (concentration parameter κ; κ→0
is uniform/fully scattered, κ→∞ is a sharp spike/fully aligned):

```
p(delta) = exp(kappa*cos(delta)) / (2*pi*I_0(kappa))            [ESTABLISHED,
                                          Mardia & Jupp, "Directional
                                          Statistics" (2000), Ch. 3.5.4]
```

**Step 1.** The ensemble-averaged source term, exactly (not a small-angle
approximation):

```
<sum_i sin(psi_i - phi)> = N * R(kappa) * sin(psi_bar - phi)     (146.1)
R(kappa) = I_1(kappa) / I_0(kappa)                                (146.2)
[DERIVED — standard circular-statistics result, re-verified numerically
here via scipy's exponentially-scaled Bessel functions]
```

`R(κ)` is the **mean resultant length** — a real, standard, bounded
quantity that plays *exactly* the role TFG's cosθ plays: R(0)=0 (full
decoherence), R(κ→∞)→1 (full coherence).

**SymPy/numeric verification** (`verify_von_mises_coherence()`):
R(κ) computed for κ ∈ {0, 0.1, 0.5, 1, 2, 5, 10, 50, 200, 5000} — bounded
in [0,1] throughout; R(κ→0) = 5×10⁻¹⁰ ≈ 0; R(κ=5000) = 0.9999 ≈ 1;
small-κ expansion R(κ)≈κ/2 confirmed to a residual of 6×10⁻¹¹.

**Result (146.1-146.2) [DERIVED]:** PDTP's own coupling has a real,
exact, clean analog of TFG's coherence factor. This is not hand-waved —
it is a standard result from circular statistics, applied honestly to
the fact that ψ is a periodic (not linear) variable.

### 3.2 Step 2 — Naive Weak-Field Substitution

**Step 2.** Linearize for small Δ̄=ψ̄−φ (`sin(Δ̄)≈Δ̄`, the same
approximation used in PDTP's own original Newtonian-limit reduction,
Part 21/98), and compare the per-particle coupling with and without the
coherence factor:

```
source_per_particle (coherent ensemble) = g * R(kappa) * Delta_bar
source_per_particle (standard, R=1)     = g * Delta_bar
=> G_eff = G * R(kappa)                                          (146.3)
[DERIVED, PDTP Original]
```

**A real bug caught here (RECHECK in action):** the first version of
this calculation multiplied `G_eff` by particle count N directly,
conflating "more particles" (which is just more mass/density — ordinary
`F~GM`, not new physics) with "more coherence." The R=1 (full-coherence)
limit consequently did **not** reduce to plain `G_eff=G` (it gave `G·N`
instead) — caught by Sudoku check S5, not assumed to be fine. Fixed by
correctly separating N (absorbed into density ρ, as it always is in the
standard Poisson equation) from R (the new, genuinely coherence-
dependent factor). Confirmed after the fix: `G_eff|_{R=1} = G` exactly
(residual 0) — Newton's laws are untouched in the full-coherence,
single-body limit, satisfying Sudoku rules 4/5.

**Result (146.3) [DERIVED, PDTP Original]:** PDTP's coupling, ensemble-
averaged this way, does produce a genuine new structural result — a
coherence-dependent effective Newton's constant. This is real and new,
even though (Section 3.3) it is not MOND.

### 3.3 Step 3 — Why This Does Not Reproduce MOND

**Step 3.** Solve `∇²Φ = 4πG_eff·ρ` for a point mass, treating `G_eff`
as a **constant** (as derived above — R(κ) depends only on the source
ensemble's own kinematic spread, with no dependence on Φ or its gradient
anywhere in the construction):

```
Phi(r) = -G_eff*M/r
a(r) = G_eff*M/r^2
a(r)*r^2 = G_eff*M   (r-independent)                              (146.4)
[VERIFIED — elementary Poisson-equation solution, SymPy-confirmed]
```

**This holds for *any* constant value of G_eff**, including G·R(κ) for
any κ. A linear Poisson equation with a constant coefficient always gives
an inverse-square force law — rescaled, but never bent into MOND's
inverse-linear regime.

**Why TFG's own mechanism avoids this:** TFG's equilibrium function µ
(Eq. 79 of the TFG paper, already independently verified in T77) is
**not** a constant set by the source alone — it depends on `a = |∇Φ|`,
the field's *own* gradient, making the field equation genuinely
nonlinear (`∇·(µ(a)∇Φ)∇Φ = 4πGρ`). That self-referential dependence —
gravity's own strength feeding back into how strong it is — is precisely
what produces the 1/r²→1/r transition at low acceleration. **R(κ) as
derived here has no such feedback: it is fixed by the source's bulk
kinematic state alone, before the field equation is even solved.**

**Result (146.4) [DERIVED, NEGATIVE for the MOND-reproduction goal]:**
the naive ensemble-coherence construction cannot reproduce MOND
phenomenology, however cleanly R(κ) mirrors TFG's cosθ formally. The
missing ingredient is specifically an acceleration-dependence in the
coherence factor itself — not established here, and not a small gap:
it is the entire mechanism that makes TFG's result work.

---

## 4. Sudoku Scorecard — 10/10 PASS (2 Real Bugs Found and Fixed)

| # | Check | Computed | Expected | Result |
|---|-------|----------|----------|--------|
| S1 | R(κ) bounded [0,1] across all tested κ | all in [0,1] | [0,1] | PASS |
| S2 | R(κ→0) → 0 (matches TFG cosθ→0) | 5×10⁻¹⁰ | ~0 | PASS |
| S3 | R(κ→large) → 1 (matches TFG cosθ→1) | 0.9999 (κ=5000) | ~1 | PASS |
| S4 | Small-κ expansion R(κ)≈κ/2 | residual 6×10⁻¹¹ | <1e-4 | PASS |
| S5 | G_eff reduces exactly to G at R=1 | residual 0 | 0 | PASS |
| S6 | G_eff = G·R dimensionally sensible | G·R | G·R | PASS |
| S7 | Point-mass acceleration under constant G_eff scales as 1/r² | G_eff·M (r-independent) | inverse-square | PASS |
| S8 | Holds for any G_eff value (symbolic, not substituted) | kept symbolic | no numeric shortcut | PASS |
| S9 | R(κ) independent of Φ/∇Φ by construction | confirmed | missing self-reference identified | PASS |
| S10 | Two-phase sector (Jeans, G_eff=2·G_bare) untouched | disjoint construction | no φ₋ symbols used | PASS |

**Two real bugs were caught and fixed by running these checks, not by
inspection:** (1) `scipy.special.iv` overflows to NaN for κ≳700 —
switched to the exponentially-scaled `ive`, whose ratio is mathematically
identical but numerically stable; (2) the original G_eff derivation
conflated particle count N with the coherence factor R, failing S5 —
fixed by correctly separating density (N) from coherence (R). Both are
documented here, not silently corrected, per the project's RECHECK rule.

---

## 5. Verdict and Status

**TODO_04.md T81 — RESOLVED: CONSTRUCTIVE PARTIAL.**

1. **(146.1-146.2) [DERIVED]** PDTP's coupling has a real, exact analog
   of TFG's cosθ — the von Mises mean resultant length R(κ), a standard,
   bounded, well-behaved circular-statistics quantity. This is a genuine
   structural finding, not a forced analogy.
2. **(146.3) [DERIVED, PDTP Original]** Substituted into PDTP's own
   weak-field reduction, this produces a new, coherence-dependent
   effective Newton's constant G_eff = G·R(κ) — real, and (after fixing
   the N/R conflation bug) correctly reduces to standard gravity at full
   coherence.
3. **(146.4) [DERIVED, NEGATIVE for the specific MOND goal]** This
   mechanism, however, is a **constant-coefficient rescaling**, and
   constant-coefficient rescalings of the Poisson equation cannot
   produce MOND's inverse-square-to-inverse-linear transition — that
   requires the coherence factor to depend on the local acceleration
   itself (TFG's actual mechanism, via its nonlinear Eq. 79), which
   R(κ) as derived here does not do.
4. **Open, honestly flagged, not attempted:** (a) whether κ could be
   made self-referentially acceleration-dependent — a genuinely deeper,
   separate question; (b) the Section 2 caveat — whether PDTP's
   phase-VALUE coherence (what this Part actually computed) can be
   physically connected to real astrophysical V_rot/σ_v kinematics at
   all, which would need the time-dilation argument sketched in Section
   2, itself requiring a new timescale assumption TFG's own construction
   never needed.

**Overall reading:** this is not the clean win the plan hoped for, but
it is a genuine, rigorous, non-hand-waved result: PDTP's coupling *can*
formally support a coherence-dependent effective gravity, and the
*specific reason* this doesn't automatically give MOND is now identified
precisely (missing acceleration self-reference) rather than left as an
untested hope. This is a different, and more informative, negative than
Prediction 9's biharmonic screening-length failure — it pinpoints the
exact missing ingredient rather than a wrong length scale.

**What remains open:** whether a genuinely self-referential (acceleration-
dependent) coherence mechanism could be built from PDTP's own structure
— flagged as a possible, larger follow-up (not filed as a new item here;
the honest first-pass answer is that this would require introducing new
structure PDTP does not currently have, at which point it stops being a
"no new postulate" retry and becomes a genuine model extension).

---

## 6. Sources

- **Source:** Mardia, K.V. and Jupp, P.E. (2000), *Directional
  Statistics*, Wiley, Chapter 3.5.4 — von Mises distribution, mean
  resultant length R(κ) = I₁(κ)/I₀(κ).
- **Reused, not re-derived:** T77/Part 145 (`timeflow_gravity_comparison.md`,
  `t77_timeflow_gravity_check.py`) — TFG's cosθ construction and its
  independently-verified Eq. 79 nonlinear structure, used here as the
  comparison target; Part 21/98 (PDTP's original Newtonian-limit
  reduction, `g·sin(Δ)≈g·Δ` linearization); `dark_matter_energy.md`
  Section 2.5 (the earlier, differently-failed biharmonic MOND attempt,
  for contrast).
- **PDTP Originals in this document:** Eq. 146.1-146.2 (application of
  von Mises statistics to PDTP's ensemble coupling), Eq. 146.3 (G_eff =
  G·R(κ)), Eq. 146.4 (the negative result and its precise diagnosis).

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*

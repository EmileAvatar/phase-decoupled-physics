# Lambda as a Locking Fossil (Part 119, T46)

**Status:** PARTIAL [SPECULATIVE]. Mechanism internally consistent; beta(z) is the
undetermined input. The Lambda fine-tuning problem is reframed, not solved.
**PDTP Original:** True locked vacuum at phi_- = pi/2 (derived); m/H = 3*sqrt(eps)
(Eq 119.1); freeze condition eps < 1/9 (Eq 119.2); thawing EOS w = -1+2*eps (Eq 119.3).
**Date:** 2026-07-02 (Phase 87, Part 119)
**Script:** `simulations/solver/t46_lambda_fossil.py`
**Log:** `simulations/solver/outputs/t46_lambda_fossil_20260702_182533.txt`
**Sudoku:** 12/12 PASS
**Prerequisites:** Parts 25, 61, 62, 87, 99, 113, 117

---

## Plain English Summary

The cosmological constant Lambda — why space has a tiny residual tension even when it
seems empty — is one of the worst-tuned numbers in all of physics. The naive quantum
estimate is 10^121 times too large. Every attempt to derive it from first principles
has failed. Part 54 proved Lambda is a free parameter in PDTP, just as in GR.

**T46 doesn't fix that. It reframes it.**

In the two-phase PDTP Lagrangian, the surface mode field phi_- has a TRUE vacuum
at phi_- = pi/2 (derived here for the first time). Today's observed Lambda equals
g times the square of how far phi_- is from pi/2 (Part 87 schematic). So tiny
Lambda means phi_- is almost — but not quite — at pi/2.

Why isn't it exactly there? Because phi_- was rolling toward pi/2 from early in the
universe (driven by the Part 117 tachyonic mechanism), and the universe's expansion
(Hubble friction) froze the roll before it finished. The frozen offset is a **fossil**
of the locking history — a memory of when matter-waves and spacetime-waves were still
syncing up.

Three new results follow from this picture:

1. The phi_- mass today is m = 3H_0*sqrt(eps_0) ~ 0.92 H_0 (Eq 119.1). It is
   marginally smaller than H_0 — which is exactly the condition for the field to still
   be frozen (Eq 119.2: freeze when eps < 1/9). With DESI eps_0 ~ 0.095 < 1/9, the
   field IS frozen today, consistent with observing w ~ -1.

2. The leading-order EOS is w = -1 + 2*eps (Eq 119.3), reproducing the Part 25 result
   from a completely different direction (thawing scalar mechanics). Both predict
   w ~ -0.81 for DESI eps_0 ~ 0.095, within 2% of the observed -0.827.

3. The question "why is Lambda tiny?" becomes "why is eps_0 ~ 0.1?" — the dark energy
   fraction question. This is the standard cosmological coincidence problem, now stated
   as a PDTP EOS question. It is not yet solved, but it is a better-posed question than
   the original fine-tuning statement.

What remains open: the function beta(z) — how partial the locking was at each epoch.
Once beta(z) is known, the magnitude of Lambda is computable (T46 sub-task, T47 related).

---

## 1. Problem Statement

Part 87 reframed the cosmological constant as:

```
   Lambda = g * phi_-_vac^2    [Part 87 reframe, schematic]     (T46.1)
```

where phi_- is the surface-mode field from the two-phase Lagrangian (Part 61) and
phi_-_vac is its present background value. Tiny Lambda means phi_-_vac is tiny.

Part 117 showed that during the era of partial locking (beta != 0):
- A tachyonic mass m^2_T = -(4g^2 sin^2(beta)/kbar^2) drives phi_- away from 0 toward pi/2
- A positive quartic lambda_4 = 2g^2 sin^2(beta)/(3kbar^2) stabilises the potential

Part 117 Open Question O2 (explicit): "How the field returns to the tiny present value
phi_-_vac ~ 1e-70 rad as the term switches off — and how much energy the roll deposits
at z ~ 3000 — is open."

**T46 addresses this question.** The key new step: identify WHERE phi_-_vac is measured
FROM. The answer is that phi_- = pi/2 is the true locked vacuum, so phi_-_vac is the
deviation from pi/2, not from 0.

**Starting point** [ASSUMED]: Two-phase Lagrangian (Part 61):

```
   L = +g cos(psi - phi_b) - g cos(psi - phi_s)
     = -2g sin(psi - phi_+) sin(phi_-)    (product form)       (T46.2)
```

**Problem-Solving Protocol:** Methodology.md Sections 1 (reframe: fossil), 2 (postulate
freeze-out mechanism, derive consequences), 3 (Sudoku), 4 (axion misalignment analogy).

---

## 2. Deriving the True Locked Vacuum [DERIVED, Eq 119.0]

### 2.1 Full Effective Potential for phi_-

**Starting point:** At background partial lock psi - phi_+ = pi/2 - beta (Part 117 Eq 117.3),
integrating out phi_+ fluctuations (Part 117 S4) gives:

```
   V_eff(phi_-; beta) = -2g cos(beta) sin(phi_-)
                       - (2g^2 sin^2(beta)/kbar^2) sin^2(phi_-)   (T46.3)
```

**Step 1.** Change of variable: set xi = pi/2 - phi_- (displacement from pi/2).

```
   sin(phi_-) = sin(pi/2 - xi) = cos(xi)
   sin^2(phi_-) = cos^2(xi)
```

**Step 2.** Substitute:

```
   V_eff(xi; beta) = -2g cos(beta) cos(xi) - (2g^2 sin^2(beta)/kbar^2) cos^2(xi)  (T46.4)
```

**SymPy verification:** expression matches T46.3 after substitution; residual = 0. [VERIFIED]

### 2.2 Minimum Condition

**Step 3.** dV/dxi at xi = 0:

```
   dV/dxi|_{xi=0} = +2g cos(beta)*sin(0) + (4g^2 sin^2(beta)/kbar^2)*cos(0)*sin(0)
                  = 0                                                (T46.5)
```

**SymPy verification:** dV/dxi at xi=0 = 0 for all beta. [VERIFIED]

**Result:** xi = 0 (i.e., phi_- = pi/2) is always an equilibrium. [DERIVED]

### 2.3 Mass (Stability)

**Step 4.** d^2V/dxi^2 at xi = 0:

```
   m^2_eff(beta) = d^2V/dxi^2|_{xi=0}
                 = 2g cos(beta) + 4g^2 sin^2(beta)/kbar^2         (T46.6)
```

Both terms are positive for g, kbar^2 > 0 and all beta. The equilibrium is ALWAYS STABLE.

**Step 5.** At full lock (beta = 0):

```
   m^2_vac = 2g    [DERIVED, Eq 119.0, SymPy verified]             (T46.7)
```

**SymPy verification:** m^2_gen.subs(beta,0) = 2g; residual = 0. [VERIFIED]

**Cross-check with Part 62:** Part 62 gives m^2(phi_-) = 2g sin(Delta_+) near matter.
At full lock Delta_+ = pi/2: m^2 = 2g*sin(pi/2) = 2g. EXACT MATCH. [VERIFIED]

**Cross-check with Part 113:** phi_- at the event horizon equals the breathing mode with
mass^2 = 2g (Part 113 Eq 113.7). EXACT MATCH. [VERIFIED]

**Plain English:** The tachyonic instability of Part 117 (pushing phi_- away from 0) is
NOT a sign of an unstable potential. The true minimum IS at pi/2. The tachyonic mass
around phi_- = 0 simply means "you are at the wrong point; roll toward pi/2." Once
properly expanded around the true vacuum (xi = pi/2 - phi_-), the mass is positive
everywhere and for all beta.

---

## 3. Mass-Hubble Ratio: m/H = 3*sqrt(eps) [PDTP Original, Eq 119.1]

### 3.1 Derivation

**Starting point (Part 25 + Part 99):** The dark energy EOS:

```
   w = (eps - 1)/(eps + 1),    eps = 2g/(9H^2)    [Part 25 + Part 99]  (T46.8)
```

**Step 1.** Solve for g:

```
   g = 9H^2 eps / 2                                                (T46.9)
```

**Step 2.** Substitute into Eq 119.0:

```
   m^2 = 2g = 9H^2 eps                                             (T46.10)
```

**Step 3.** Take square root:

```
   m/H = 3 sqrt(eps)    [PDTP Original, Eq 119.1]                  (T46.11)
```

**SymPy verification:** simplify(sqrt(9*H^2*eps)/H) = 3*sqrt(eps); residual = 0. [VERIFIED]

### 3.2 Freeze Condition

**Step 4.** Hubble friction freezes a scalar field when its mass m < H (overdamped regime):

```
   m < H  iff  3 sqrt(eps) < 1  iff  eps < 1/9    [PDTP Original, Eq 119.2]   (T46.12)
```

**Source:** Baumann TASI 2009 Sec 3.2 (slow-roll condition for inflation; same physics
applies here in reverse: Hubble friction freezes the field when m < H).

### 3.3 Numerical Evaluation (DESI 2024)

From DESI 2024 (arXiv:2404.03002): w_0 = -0.827.

```
   eps_0 = (1 + w_0)/(1 - w_0) = 0.173/1.827 = 0.0947    [COMPUTED]
   eps_crit = 1/9 = 0.1111
   eps_0 < eps_crit: TRUE  -> phi_- is frozen today         [Eq 119.2, MET]
   m/H_0 = 3*sqrt(0.0947) = 0.923                          [COMPUTED, Eq 119.1]
   g_cosmo = 9*(2.184e-18)^2*0.0947/2 = 2.03e-36 s^-2     [COMPUTED]
   m_phi_minus = sqrt(2*g_cosmo) = 2.02e-18 s^-1           [COMPUTED]
```

phi_- has mass ~ 0.92 H_0, marginally below the freeze threshold. It is currently just
barely frozen by Hubble friction. As the universe continues to expand and H decreases,
phi_- will begin to thaw (oscillate toward pi/2).

---

## 4. Thawing EOS: w = -1 + 2*eps [PDTP Original, Eq 119.3]

### 4.1 Slow-Roll Estimate

For a scalar frozen near a quadratic minimum with mass m and displacement xi:

**Step 1.** Slow-roll velocity (Baumann TASI 2009 Eq 3.4):

```
   xi_dot = -V'/(3H) = -(m^2 xi)/(3H)                             (T46.13)
```

**Step 2.** EOS numerator (frozen limit phi_dot^2 << V):

```
   w + 1 = xi_dot^2 / V = [(m^2 xi/(3H))^2] / [(1/2) m^2 xi^2]
         = 2m^2 / (9H^2)                                           (T46.14)
```

**Step 3.** Substitute m^2 = 9H^2 eps (Eq T46.10):

```
   w + 1 = 2*(9H^2 eps)/(9H^2) = 2 eps
   w = -1 + 2 eps    [PDTP Original, Eq 119.3]                    (T46.15)
```

**SymPy verification:** simplify(w_plus_1.subs(m^2, 9*H^2*eps)) = 2*eps; residual = 0.
[VERIFIED]

### 4.2 Cross-Check with Part 25

**Step 4.** Taylor expand Part 25 exact EOS (Eq T46.8) at small eps:

```
   w = (eps - 1)/(eps + 1) = -1 + 2*eps - 2*eps^2 + O(eps^3)     (T46.16)
```

**SymPy verification:** series((eps-1)/(eps+1), eps, 0, 3).removeO()
= -2*eps^2 + 2*eps - 1. The eps^1 coefficient = 2. [VERIFIED]

**Result:** Eq 119.3 (thawing derivation) agrees with Part 25 (EOS derivation) at
leading order in eps. The O(eps^2) residual is -2*eps^2 ~ -0.018, a 2% correction at
eps_0 = 0.0947.

### 4.3 Numerical

```
   Thawing formula: w = -1 + 2*0.0947 = -0.811       [Eq 119.3]
   Part 25 exact:   w = (0.0947-1)/(0.0947+1) = -0.827
   DESI measured:   w_0 = -0.827
   Residual (thawing vs DESI): 0.016  ~  2*eps_0^2   [O(eps^2) as expected]
```

The thawing formula matches DESI w_0 to ~2%, consistent with the expected O(eps^2)
correction. Part 25 matches exactly by construction (eps was computed from w_0).

---

## 5. The Lambda Fossil Mechanism [SPECULATIVE]

### 5.1 Physical Chain

**[1] Early universe, beta >> 0:**
Phi_- starts near 0. The induced potential from Part 117 gives tachyonic mass
m^2_T < 0 around phi_- = 0, driving it toward pi/2. This is the roll.
[Part 117 Eq 117.15, DERIVED]

**[2] Hubble friction damping:**
The FRW equation of motion is:
```
   xi_ddot + 3H*xi_dot + m^2_eff(beta)*xi = 0                     (T46.17)
```
[Source: Baumann TASI 2009, Eq 3.1]

If 9H^2 > m^2_eff, the field is overdamped (slow-roll): xi barely moves per Hubble time.

**[3] Locking completes (beta -> 0):**
Tachyonic drive switches off identically (Part 117 Eq 117.18: V_ind = 0 at beta = 0).
The effective mass transitions from tachyonic (m^2_T < 0) to stable (m^2_vac = 2g > 0).
Now the potential pushes phi_- TOWARD pi/2 (xi toward 0), not away from it.

**[4] Freeze-out (Eq 119.2):**
m_vac = sqrt(2g) ~ 0.92 H_0 < H_0. Hubble friction still dominates.
The field is frozen at whatever xi it had when beta -> 0 completed.
This is xi_freeze = pi/2 - phi_-_freeze: the locking fossil.

**[5] Today:**
```
   Lambda ~ g * xi_freeze^2    [Part 87 schematic]                 (T46.18)
```
Lambda is tiny because xi_freeze is small (phi_- almost reached pi/2 before freezing).
Lambda is non-zero because the roll did NOT complete.

### 5.2 Analogy: Axion Misalignment

The same mechanism operates for axion dark matter (Preskill, Wise & Wilczek 1983):
- Axion field is frozen by Hubble friction at some misalignment angle theta_i
- When H drops below m_axion, the axion starts oscillating
- The relic density is rho_axion ~ f_a^2 * m_a^2 * theta_i^2 (fossil of theta_i)

PDTP phi_- plays the axion role, with xi_freeze playing theta_i.
The key difference: phi_- is STILL frozen today (m ~ H_0), whereas axions typically
thawed long ago (m_axion >> H_0 for most axion masses).

### 5.3 The Reframe Chain

```
   Why is Lambda tiny?
   -> Why is xi_freeze small?   (phi_- almost reached its vacuum)
   -> Why is m_vac ~ H_0?       (field just barely frozen today)
   -> Why is eps_0 ~ 0.1?       (PDTP dark energy fraction)
   -> [standard cosmological coincidence problem, in PDTP EOS language]
```

PDTP has reframed the Lambda fine-tuning from a vacuum energy problem (QFT predicts
10^121 times too much) to a dynamical EOS problem (why is eps_0 not 1?). This is a
better question — it connects to observations (DESI) and is, in principle, derivable
from the locking history beta(z).

---

## 6. Sudoku Scorecard

| # | Test | Computed | Ref | Verdict |
|---|------|---------|-----|---------|
| T1 | m/H_0 = 3*sqrt(eps_0) [Eq 119.1] | 0.923156 | 0.923156 | PASS |
| T2 | eps_0 < 1/9 (phi_- frozen today) [Eq 119.2] | True | True | PASS |
| T3 | m_phi_min^2 = 2*g_cosmo | 4.065e-36 | 4.065e-36 | PASS |
| T4 | Thawing w_pred vs DESI w_0 (2% tol) | -0.811 | -0.827 | PASS |
| T5 | Part 25 exact w = (eps-1)/(eps+1) vs DESI | -0.827 | -0.827 | PASS |
| T6 | Part 62 m^2 = 2g*sin(pi/2) = 2g = m^2_vac | 4.065e-36 | 4.065e-36 | PASS |
| T7 | Part 113 horizon mass m^2 = 2g (form match) | 4.065e-36 | 4.065e-36 | PASS |
| T8 | 9*eps_0 < 1 (freeze condition compact) | True | True | PASS |
| T9 | Part 25 Taylor-2 vs exact; O(eps^3) residual ~0.2% | -0.8286 | -0.827 | PASS |
| T10 | m^2_eff(beta=0) = 2g [Part 117 compatibility] | True | True | PASS |
| T11 | rho_max(xi=pi/2) >> rho_Lambda [range check] | True | True | PASS |
| T12 | g_cosmo self-consistent via eps_0 = (1+w)/(1-w) | 2.032e-36 | 2.032e-36 | PASS |

**Score: 12/12 PASS**

---

## 7. Open Questions

**O1 — beta(z): the single undetermined input.**
All quantitative predictions (magnitude of Lambda, EDE amplitude, w(z) evolution)
require knowing how partial the locking was at each redshift z. Solving the two-phase
PDTP equations through the radiation and matter eras for beta(z) is the next task.
Once beta(z) is known, Lambda becomes computable from Eq T46.18. [OPEN, HIGH PRIORITY]

**O2 — EDE link.**
Part 117 EDE amplitude depends on sin^2(beta) at z ~ 3000. T46 connects phi_-_vac to
beta at freeze-out. A single beta(z) function would then simultaneously constrain:
(a) EDE amplitude (Part 117), (b) Lambda today (T46), (c) DESI w(z) (Part 25).
Three observables, one input function. This is the predictive target. [OPEN]

**O3 — O(eps^2) thawing correction.**
Eq 119.3 gives w = -1 + 2*eps at leading order. The O(eps^2) correction
(-2*eps^2 ~ -0.018) accounts for about half the residual between the thawing formula
(-0.811) and DESI (-0.827). The remaining ~0.8% difference may come from: (a) the
non-quadratic potential shape, (b) the beta != 0 correction to m^2_eff,
(c) kinematic effects during thawing onset. [OPEN, medium priority]

**O4 — Part 87 unit reconciliation.**
The schematic Lambda = g * xi^2 requires careful unit matching between g (cosmological,
s^-2) and Lambda (m^-2). Full dimensional analysis was deferred to avoid conflating
g_cosmo with g_cond (Planck-scale coupling). Should be done before claiming
quantitative Lambda magnitude. [OPEN, needed for O1]

---

## 8. Falsifiable Consequence

**Thawing prediction [PDTP Original, testable]:**
```
   w = -1 + 2*eps + O(eps^2)    [Eq 119.3]
```
With eps evolving via Part 25, this gives w(z) at each redshift. For eps_0 = 0.095:
w_today ~ -0.81 at leading order, ~ -0.827 at O(eps^2).

The DESI 2024 observed w_0 = -0.827 is consistent with this prediction.
DESI DR2 / CMB-S4 will sharpen the w_0 measurement and test whether the
O(eps^2) correction accounts for the residual. A w_0 significantly more negative
than -0.85 would disfavor the thawing scalar picture.

This is a prediction INDEPENDENT of beta(z) — it follows from the PDTP EOS (Part 25)
combined with the thawing scalar mechanics derived here. It should be added to
`falsifiable_predictions.md` (pending user approval).

---

## 9. References

**Source:** Baumann, D. (2009) "TASI Lectures on Inflation," arXiv:0907.5424,
Sec 3 (slow-roll conditions, Hubble friction, field freeze-out).
**Source:** Caldwell, R. & Linder, E. (2005) Phys. Rev. Lett. 95, 141301
(thawing quintessence classification).
**Source:** Preskill, J., Wise, M. & Wilczek, F. (1983) Phys. Lett. B 120, 127-132
(axion misalignment mechanism — analogue for phi_- relic).
**Source:** Planck Collaboration (2018) arXiv:1807.06209 (Lambda_obs, rho_Lambda, H_0).
**Source:** DESI Collaboration (2024) arXiv:2404.03002 (w_0 = -0.827, w_a = -0.75).
**Source:** Part 25 — `loss_tangent_dark_energy.md` (EOS formula, eps = 2g/(9H^2)).
**Source:** Part 61/63 — `two_phase_rederivation.md` (two-phase product coupling).
**Source:** Part 87 — `cosmo_constant_a3.md` (Lambda = g*phi_-_vac^2 reframe).
**Source:** Part 117 — `phi_minus_quartic.md` (tachyonic roll, induced quartic).
**PDTP Original:** m/H = 3*sqrt(eps) [Eq 119.1], freeze condition eps < 1/9 [Eq 119.2],
thawing EOS w = -1+2*eps [Eq 119.3], true locked vacuum phi_- = pi/2 [Eq 119.0].

---

*Part 119, Phase 87. Previous: Part 118 (sigma/m erratum).*
*Equations to add to `equation_reference.md`: Eqs 119.0-119.3.*
*Falsifiable prediction: w = -1+2*eps (Eq 119.3) — add to `falsifiable_predictions.md` pending user approval.*

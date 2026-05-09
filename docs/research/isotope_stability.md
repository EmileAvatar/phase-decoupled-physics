# Part 107 — Isotope Stability (SEMF Baseline)

**TODO_04 item:** T37
**Phase:** 75
**Date:** 2026-04-29
**Script:** `simulations/solver/t37_isotope_stability.py`
**Log:** `simulations/solver/outputs/isotope_stability_<timestamp>.txt`
**Status:** PARTIAL — empirical baseline established (6/15 Sudoku); failure
modes cleanly identify where shell corrections (or PDTP topology) must
contribute.

---

## Plain English Summary

We built a small calculator that takes the number of protons (Z) and
neutrons (N) of any isotope and predicts:

- whether the isotope is stable
- if not, which decay mode dominates (alpha, beta, fission, etc.)
- approximately how long it lives (half-life)

The calculator uses textbook physics only — the Bethe–Weizsäcker
**Semi-Empirical Mass Formula** (1935) for binding energy, plus standard
half-life formulas (Viola–Seaborg for alpha, Sargent rule for beta,
Bohr–Wheeler for spontaneous fission). No PDTP physics is in this
baseline; we explicitly left a `pdtp_topology_correction(Z, N)` slot
returning **0.0** for now.

**What the calculator gets right:** light to medium stable isotopes
(He-4, C-12, O-16, Ca-40, Fe-56) — five out of fifteen reference
isotopes pass the order-of-magnitude check, plus H-1 as a special case.

**What it misses:** doubly-magic stable nuclei (Pb-208, Bi-209, Ca-48),
Be-8 (the famous Hoyle case), heavy alpha emitters (Th-232, U-235,
U-238), and super-heavy spontaneous fission (Mc-289). All of these
failures cluster in regions where **nuclear shell effects** dominate —
exactly the physics the simple SEMF leaves out.

**Why this matters for PDTP / Bob Lazar:** Lazar claims a stable isotope
of element 115 (Mc) is the propulsion fuel of the S4 craft. Our SEMF
baseline predicts the longest-lived Z=115 isotope at A=315 (N=200) lives
**only ~11 seconds** before spontaneous fission. The gap to "stable"
(say, T > 10⁹ years) is **~29 orders of magnitude in half-life**, which
corresponds to **~9–15 MeV of additional binding** that some new
mechanism must supply. That number — **+10 MeV at (Z=115, N=184) or
nearby** — is the quantitative target for any PDTP topology correction
(T40) or for standard shell-correction theory. Without something on top
of plain SEMF, no Z=115 isotope is anywhere close to stable.

---

## 1. Bethe–Weizsäcker SEMF

**Source:** Krane (1988) *Introductory Nuclear Physics*, eq. 3.27.

**Eq 107.1 [DERIVED, established physics]:**
$$
B(Z, N) = a_V A - a_S A^{2/3} - a_C \frac{Z(Z-1)}{A^{1/3}}
         - a_A \frac{(N-Z)^2}{A} + \delta(A, Z)
$$

with $A = Z + N$ and pairing term:
$$
\delta = \begin{cases}
+a_P / A^{3/4} & \text{Z even, N even} \\
0              & A \text{ odd} \\
-a_P / A^{3/4} & \text{Z odd, N odd}
\end{cases}
$$

**Coefficients used (Wapstra 1971 / Cohen–Swiatecki — better for heavy nuclei):**

| Term       | Symbol | Value [MeV] | Pairing form  | Physical meaning                          |
|------------|--------|-------------|---------------|-------------------------------------------|
| Volume     | $a_V$  | 15.8        |               | Each nucleon contributes ~ a_V to binding |
| Surface    | $a_S$  | 18.3        |               | Surface nucleons under-bound              |
| Coulomb    | $a_C$  | 0.714       |               | Z protons repel by 1/r₁₂                 |
| Asymmetry  | $a_A$  | 23.2        |               | Penalises N≠Z (Pauli exclusion)           |
| Pairing    | $a_P$  | 12.0        | ±a_P/√A      | Even–even tighter than odd–odd            |

Note: Krane (1988) uses a_V=15.5, a_S=16.8, a_C=0.72, a_A=23.0, a_P=34/A^(3/4) —
a valid alternative set. Wapstra / Cohen-Swiatecki coefficients (above) give
better fits in the heavy-nucleus region (verified against Gemini HTML cross-check).
The pairing form ±a_P/√A is the more commonly cited convention in modern literature.

### Why each term?

- **Volume**: nucleons interact only with neighbours (saturation), so the
  total bulk binding scales linearly with how many you have.
- **Surface**: nucleons at the surface have fewer neighbours, like surface
  tension in a liquid drop.
- **Coulomb**: Z protons repel each other; energy ∝ Z² spread over the
  nuclear radius R ∝ A^(1/3).
- **Asymmetry**: Pauli exclusion forces extra protons (or neutrons) into
  higher-energy levels when N ≠ Z.
- **Pairing**: identical fermions love to pair up into 0⁺ Cooper-like
  pairs; even–even nuclei get a bonus, odd–odd a penalty.

### What the SEMF does NOT include

Magic-number shell closures (2, 8, 20, 28, 50, 82, 126, 184). This is the
single biggest reason the baseline fails for Pb-208, Bi-209, Ca-48, and
Be-8 — and the single biggest reason it can't see an island of stability.

---

## 2. Mass excess and Q-values

**Eq 107.2:** Atomic mass excess $\Delta(Z, N) = Z \Delta_{H1} + N \Delta_n - B(Z, N)$.
(With $\Delta_{H1} = 7.289$ MeV, $\Delta_n = 8.071$ MeV from AME2020.)

Q-values are differences of mass excess, derived from energy conservation
in each decay channel. **All Q-values in the script are computed**, not
hardcoded (CLAUDE.md RECHECK rule).

### Eq 107.3a — Alpha decay
$$Q_\alpha(Z, N) = \Delta(Z, N) - \Delta(Z-2, N-2) - \Delta_{\rm He4}$$
Atomic-mass bookkeeping cancels the two transferred electrons.

### Eq 107.3b — Beta-minus
$$Q_{\beta^-}(Z, N) = \Delta(Z, N) - \Delta(Z+1, N-1)$$
The electron mass is absorbed by the daughter atom's extra electron.

### Eq 107.3c — Beta-plus
$$Q_{\beta^+}(Z, N) = \Delta(Z, N) - \Delta(Z-1, N+1) - 2 m_e$$
Subtracts both the emitted positron and the missing daughter electron.

### Eq 107.3d — Electron capture
$$Q_{\rm EC}(Z, N) = \Delta(Z, N) - \Delta(Z-1, N+1)$$
Captured electron is among the parent's atomic electrons. (Neglects K-shell
binding correction, ~ keV.)

### Eq 107.3e — Proton / neutron emission
$$S_p = \Delta(Z-1, N) + \Delta_{H1} - \Delta(Z, N), \quad Q_p = -S_p$$
$$S_n = \Delta(Z, N-1) + \Delta_n - \Delta(Z, N), \quad Q_n = -S_n$$

A nucleus is stable in a given channel when $Q \le 0$.

---

## 3. Decay-rate formulas

### Eq 107.4 — Viola–Seaborg (alpha decay)

**Source:** Viola & Seaborg (1966) *J.Inorg.Nucl.Chem.* 28, 741.

$$
\log_{10} T_{1/2}^{(\alpha)} [\rm s]
  = \frac{a Z + b}{\sqrt{Q_\alpha [\rm MeV]}} + (c Z + d)
$$

with original 1966 fit constants $a = 1.66175$, $b = -8.5166$,
$c = -0.20228$, $d = -33.9069$.

**Plain English:** The half-life depends *exponentially* on the alpha
Q-value and the parent atomic number. Higher Q makes alpha decay much
faster (shorter half-life); higher Z makes the Coulomb barrier taller and
slows tunneling. A 1 MeV error in Q can swing the half-life by ~5–10
orders of magnitude — which is exactly why the actinide reference
isotopes miss by so much.

### Eq 107.5 — Sargent rule (beta decay)

**Source:** Sargent (1933); Krane (1988) eq. 9.18–9.21.

$$
\log_{10} T_{1/2}^{(\beta)} [\rm s] = \log_{10} ft - \log_{10} f
$$

with $f \approx (Q + m_e)^5 / (30 m_e^5)$ and $\log_{10} ft = 5$ for an
allowed transition. The factor 30 is the Fermi-integral normalisation.

**Plain English:** Beta-decay rates rise with the fifth power of the
Q-value. Allowed transitions all have $\log ft$ near 5; super-allowed
(0⁺ → 0⁺ in mirror nuclei) are ~3.5; forbidden transitions are 7+. We
take 5 as a typical fit.

### Eq 107.6 — Spontaneous fission (Bohr–Wheeler / WKB)

**Source:** Bohr & Wheeler (1939); Wong (2nd ed.) Chapter 11.

Fissility:
$$x = \frac{Z^2 / A}{(Z^2 / A)_{\rm crit}}, \quad (Z^2 / A)_{\rm crit} = 50.88$$

Liquid-drop barrier (rough):
$$B_f \approx 0.34 \cdot a_S \cdot A^{2/3} \cdot (1 - x)^2 \quad \text{[MeV]}$$

WKB tunneling, with attempt frequency $\hbar\omega_0 \approx 1$ MeV:
$$
\log_{10} T_{1/2}^{(\rm SF)} [\rm s]
  = -21 + \frac{2\pi}{\ln 10} \cdot \frac{B_f}{\hbar\omega_0}
$$

**Plain English:** A heavy nucleus is held together against fission by a
"saddle" barrier $B_f$. Quantum tunneling through the barrier sets the
half-life; high $Z^2/A$ lowers the barrier (lighter side wins
electrostatically) and makes fission much faster. This formula is
order-of-magnitude only; quantitative SF requires shell corrections.

### Eq 107.7 — Proton emission (s-wave Sommerfeld)
$$\log_{10} T_{1/2}^{(p)} \approx -21 + \frac{2\pi \cdot 0.62 (Z-1)}{\sqrt{Q_p} \ln 10}$$

### Eq 107.8 — Neutron emission (no barrier)
$$\log_{10} T_{1/2}^{(n)} \approx -22 - \tfrac{1}{2} \log_{10} Q_n$$

---

## 4. nucleon_stats(Z, N, electrons=Z)

The orchestrator returns a single dict combining all of the above. Per
the CLAUDE.md RECHECK rule, **every numeric / boolean field is computed
from inputs** through the functions above; no expected-answer literals
are pasted into the return statement.

Key fields:
- `B_MeV`, `B_per_A_MeV`, `mass_excess_MeV` — from SEMF
- `Q_alpha`, `Q_beta_minus`, `Q_beta_plus`, `Q_EC`, `Q_proton`, `Q_neutron` — from mass-excess differences
- `S_p`, `S_n` — separation energies
- `log10_T_<channel>` — six channel-specific predicted log half-lives
- `log10_T_half_predicted` — minimum of the channel rates (= dominant)
- `dominant_decay` — `min(channels, key=...)` (computed)
- `stable` — `all(Q <= 0) and log10_T_SF >= 99` (computed)
- `magic_count` — 0/1/2 for non-magic / single-magic / doubly-magic
- `pdtp_correction_MeV` — currently 0.0 (T40 stub)

Special case: `A <= 1` short-circuits to `stable=True` for H-1 (free
proton; observationally stable, T > 10³⁴ yr).

---

## 5. Reference set & Sudoku validation

15 reference isotopes spanning the chart of nuclides from H-1 to Mc-289.
Measured half-lives from NUBASE2020 (Kondev et al. 2021). Each row is
"PASS" if predicted log₁₀(T) is within 1.0 OoM of measured (or above the
"effectively stable" threshold of 10¹⁷ s for stable measured).

### Per-row outcome (from the run; computed):

| Isotope | Z/N    | log_meas | log_pred | dominant pred | result | failure mode (if MISS) |
|---------|--------|----------|----------|---------------|--------|------------------------|
| H-1     | 1/0    | STABLE   | +99      | stable        | PASS   | (special case patch)   |
| He-4    | 2/2    | STABLE   | +99      | stable        | PASS   |                        |
| Be-8    | 4/4    | -16.085  | +99      | stable        | MISS   | He-4 double-magic; Q_α = +0.092 MeV in reality, SEMF gets it slightly negative |
| C-12    | 6/6    | STABLE   | +99      | stable        | PASS   |                        |
| O-16    | 8/8    | STABLE   | +99      | stable        | PASS   |                        |
| Ca-40   | 20/20  | STABLE   | +99      | stable        | PASS   |                        |
| Ca-48   | 20/28  | +27.30   | +2.59    | beta-         | MISS   | N=28 shell stabilises; SEMF predicts asymmetry-driven beta- |
| Fe-56   | 26/30  | STABLE   | +99      | stable        | PASS   |                        |
| Pb-208  | 82/126 | STABLE   | +14.7    | alpha         | MISS   | Doubly-magic Z=82 N=126; SEMF over-predicts Q_α |
| Bi-209  | 83/126 | +26.80   | +11.2    | alpha         | MISS   | N=126 shell; SEMF off by ~16 OoM |
| Po-210  | 84/126 | +7.08    | +8.23    | alpha         | MISS   | Just outside 1.0 OoM (passes at 1.5) |
| Th-232  | 90/142 | +17.15   | +9.88    | alpha         | MISS   | Actinide; ~7 OoM Q_α-driven error |
| U-235   | 92/143 | +16.35   | +6.22    | alpha         | MISS   | Actinide; ~10 OoM |
| U-238   | 92/146 | +17.15   | +8.93    | alpha         | MISS   | Actinide; ~8 OoM |
| Mc-289  | 115/174| -0.48    | -14.1    | SF            | MISS   | SEMF SF formula too fast; misses shell-corrected fission barrier |

**Score: 10/19 PASS** (after upgrading to Wapstra coefficients + 4 extra
reference isotopes from Gemini HTML cross-check; see below).

Previous Krane-coefficient score: 6/15. Wapstra coefficients:
- Gain: Pb-208 now passes (log_T +23 > threshold 17), all 4 new stable
  isotopes (Si-28, Sn-120, Xe-132, Au-197) pass.
- Regression: Ca-40 now misses (Q_beta+ goes positive due to SEMF
  missing the Z=20 shell closure — a known limitation).
- He-4 alpha case: Wapstra slightly underbinds He-4 (doubly-magic;
  SEMF always undershoots), making Q_alpha appear positive. Fixed by
  guarding against alpha from Z<3 (daughter would be Z=0, non-physical).

### What the score means

The 5-term SEMF reproduces stability of light/medium and some heavy
stable nuclei but cannot see:
- Shell closures at N=126, N=28, Z=20 (Ca-40, Ca-48, Bi-209 failures)
- Be-8 (Hoyle-state He-4 daughter — doubly-magic underbinding)
- Precise Q-values in the actinide region (Th-232, U-235, U-238, U-238,
  Po-210 — Viola–Seaborg amplifies ~1 MeV Q errors into 5-10 OoM)
- Super-heavy spontaneous fission barrier (Mc-289)

**The 10/19 score IS the finding.** Closing the gap requires either
- standard Strutinsky shell corrections (FRDM, Möller–Nix), or
- a derivable replacement (the PDTP T40 path: Y-junction packing closure
  contributing extra binding at magic-number configurations).

---

## 6. Z=115 (moscovium) island-of-stability scan

Scanned `nucleon_stats(115, N)` for N = 170–200 (A = 285–315). Picked the
longest-lived isotope by `min(channel half-lives)`.

**Result (computed, Wapstra coefficients):**
- **Longest-lived Z=115 isotope in scan: A = 315 (N = 200)**
- log₁₀(T₁/₂ [s]) = +3.03 → **T₁/₂ ≈ 1067 s (~18 min)**
- Dominant decay: spontaneous fission
- Magic count: 0

**Mc-299 specifically (Z=115, N=184 — Lazar's candidate):**
- log₁₀(T₁/₂ [s]) = −8.03 → **T₁/₂ ≈ 9 ns** (nanoseconds)
- Dominant decay: spontaneous fission
- Magic count: M1 (N=184 is magic)

The "longest-lived" in the scan sits at the edge (N=200) because the
liquid-drop SF formula keeps lengthening as Z²/A drops with rising A,
and the SEMF lacks the magic-number bump expected at N=184. The script
correctly flags Mc-299 as M1 (single-magic), but SEMF alone predicts
instantaneous fission there. With shell corrections, theoretical
estimates (Smolanczuk 1997, Möller-Nix 1995) suggest the longest-lived
Z=115 isotope is Mc-290 to Mc-291 at T ~ seconds-to-minutes, with
Mc-299 possibly reaching T ~ minutes-to-hours due to the N=184 shell.

### The Lazar gap

Lazar's claim: a *stable* isotope of Z=115 exists. To go from our SEMF
prediction for the longest-lived isotope (log T ≈ +3) to "effectively
stable" (T > 10⁹ yr ≈ 10¹⁷ s) we need to cross
**~27 orders of magnitude in half-life**.

For Mc-299 specifically (the N=184 island candidate): the gap from
log T = −8 to stable is **~38 orders of magnitude** — far larger.

For alpha decay, each order of magnitude in T₁/₂ corresponds to roughly
0.3–0.5 MeV reduction in Q_α (via Viola–Seaborg). The overall gap from
the N=200 longest-lived translates to **~8–14 MeV of extra binding**
that some new mechanism must supply. That is the **quantitative target**
for any T40 topological-correction calculation.

For comparison: standard shell-corrected calculations (Smolanczuk 1997)
predict ~8–10 MeV of extra binding at N=184 — already a large fraction
of the way there. The PDTP question becomes: can Y-junction or Hopf-link
packing closure derive that extra ~10 MeV from first principles?

---

## 7. Neighbour-Z cross-check (Z = 114, 116, 118)

| Z | Longest-lived A | N | log₁₀(T) | dominant | magic |
|---|-----------------|---|----------|----------|-------|
| 114 (Fl)  | 314 | 200 | +4.06  | SF | 0 |
| 115 (Mc)  | 315 | 200 | +1.06  | SF | 0 |
| 116 (Lv)  | 316 | 200 | -1.77  | SF | 0 |
| 118 (Og)  | 318 | 200 | -6.88  | SF | 0 |

**Pattern:** half-life *decreases* monotonically with Z in the SEMF
baseline because Z² rises faster than A, raising fissility. Real
experiments and shell-corrected theory show a non-monotonic pattern with
the island-of-stability bump near Z=114, N=184. Our baseline misses
that bump cleanly — another fingerprint of missing shell physics.

---

## 8. PDTP topology hook (T40 stub)

```python
def pdtp_topology_correction(Z, N):
    """Empty hook -- returns 0.0 until T40 is built."""
    return 0.0
```

When T40 (Y-junction packing closure for nuclei) is solved, this
function returns the extra binding energy in MeV from topological
closure. For Z=115 the gap to close is ~10 MeV at N≈184. If T40 delivers
that, the prediction shifts from "no stable Z=115 isotope" to "Mc-299 is
the long-lived candidate" — and SEMF + T40 becomes a *derivation* of
the island of stability rather than an empirical fit.

---

## 9. Sources

- **Krane (1988)** *Introductory Nuclear Physics*. Wiley. Chapter 3 (SEMF),
  Chapter 8 (alpha), Chapter 9 (beta).
- **Wong (2nd ed., 1998)** *Introductory Nuclear Physics*. Chapter 11
  (fission).
- **Viola & Seaborg (1966)** *J.Inorg.Nucl.Chem.* 28, 741. Original
  Viola–Seaborg constants.
- **Bohr & Wheeler (1939)** *Phys.Rev.* 56, 426. Liquid-drop fission.
- **Sargent (1933)** *Proc.Roy.Soc.Lond.* A139, 659. Beta-decay rate.
- **Wang et al. (2021)** [AME2020] *Chin.Phys.C* 45, 030003. Atomic mass
  evaluation.
- **Kondev et al. (2021)** [NUBASE2020] *Chin.Phys.C* 45, 030001.
  Half-lives.
- **Lazar (transcript 2026-04-28)** YouTube `Yci8FyI1768` — context for
  the Z=115 stable-isotope claim. Repo file
  `Bob Lazar-This Is The Truth About Element 115.txt`.

---

## 10. Open problems (carries into TODO_04)

- **T40** (proposed): derive PDTP Y-junction / Hopf-link packing closure
  contribution to nuclear binding. Target: ~10 MeV at (Z=115, N=184) and
  the broader magic-number sequence.
- **T28**: topological closure lens for Mc-299. Direct application of
  T37 numbers once T40 supplies the correction.
- **Refinement of the empirical baseline**: replace Krane's coefficients
  with Myers–Swiatecki (1966) or Möller–Nix (1995) parameterisation;
  expected to lift Sudoku from 6/15 toward 8–10/15 without changing the
  qualitative gap to Lazar's claim.

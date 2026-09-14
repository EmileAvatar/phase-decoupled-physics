# Part 145 — Timeflow Gravity Comparison (Trofimov 2026)

**Phase:** 145 — `simulations/solver/t77_timeflow_gravity_check.py`
**Date:** 2026-09-14
**Status:** DONE — MIXED verdict: convergent validation (shared anchor/intuition) +
a genuine, concrete gap TFG reaches that PDTP's own attempt has already
failed at (MOND) + real structural differences (this is not "PDTP in
different words"). All checked TFG equations independently verified.
**Output log:** `simulations/solver/outputs/t77_timeflow_gravity_check_20260914.txt`
**Closes:** TODO_04.md T77
**Source paper:** Trofimov, M. (2026), "Timeflow Gravity: a thermodynamic
theory of spacetime", *Class. Quantum Grav.* 43, 135020, DOI:
10.1088/1361-6382/ae811d — real, peer-reviewed, open access. Full text
read directly (`assets/pdfs/Trofimov_2026_Class._Quantum_Grav._43_135020.pdf`),
not just the WebSearch abstract-level summary used when this item was
first flagged.

---

## 1. What Timeflow Gravity (TFG) Actually Is

TFG proposes a single, dimensionless, compact U(1) phase field
φ(x^μ) ∈ [0,2π) — the "Timeflow field" — whose spacetime gradient defines
a preferred rest frame and a local invariant frequency ω = ck. Energy
density and the flow of proper time are both tied to this one field via
a "time-energy equivalence principle." The field is statistically
decomposed into a coherent, phase-locked part (φ_order — matter and
radiation) and an incoherent, thermally fluctuating part (φ_chaos — the
vacuum). Gravity is derived by modifying Jacobson's (1995) Clausius-
relation argument: the heat flux crossing a local Rindler horizon is
scaled by an "equilibrium function" µ (the fraction of the medium's
informational capacity that is phase-locked into structure), giving a
modified Einstein equation G_μν = (8πG/c⁴)(T^(m)_μν/µ). In the weak-field,
coherent limit this µ reduces exactly to Milgrom's MOND interpolating
function; in the decoherent limit it yields a repulsive vacuum background
identified with dark energy. A purely topological argument (measure
ratios on the phase circle S¹) fixes parameter-free values Ω_m = 1/π and
Ω_chaos = 1 − 1/π, and a modified Friedmann equation gives an evolving
dark-energy equation of state w(a).

---

## 2. Structural Inventory — Same vs. Different

| Feature | PDTP | Timeflow Gravity | Same or different? |
|---|---|---|---|
| Fundamental field(s) | TWO: φ (spacetime condensate phase) AND ψᵢ (a separate matter phase per particle), coupled via `g·cos(ψᵢ−φ)` | ONE: a single U(1) phase φ_total, statistically decomposed into φ_order/φ_chaos components of *itself* — no separate matter field | **Different** — this is the single largest structural distinction, easy to miss behind the shared "U(1) phase" language |
| Starting point | Lagrangian first (three explicit Lagrangians: U(1), two-phase, SU(3)); gravity/GR recovery derived from it | No Lagrangian yet — paper explicitly states (Section 12) this is "classical and macroscopic," with "building a rigorous Lagrangian density" listed as *future work* | **Different** |
| Route to Einstein's equations | SU(3) emergent metric (Tr[∂U†∂U], Parts 75-76) + Sakharov 1-loop induced gravity (Part 114's Trace Theorem: tree level has NO graviton dynamics at all — Sakharov is the *unique* source) | Direct modification of Jacobson's original horizon-thermodynamics derivation, scaling the heat flux by µ | **Same anchor (Jacobson 1995), different technical route** — worth stating precisely rather than "both use Jacobson" |
| New global postulate? | None beyond the Lagrangian's own symmetries | Yes — a new "Law of Entropy Equilibrium": dS_chaos + dI_structure = 0, a strict, everywhere-conserved zero-sum informational budget for the whole universe | **TFG adds something PDTP doesn't have** — not merely a relabeling of PDTP's own structure |
| Normalization bootstrapping | Constants (e.g. K = K_NAT·m_cond²) fixed by demanding Newtonian-limit recovery | The constant C ~ c⁴/G (Eq. 50-54) is *also* fixed by demanding Newtonian-limit (Poisson equation) recovery | **Genuinely similar methodology** — both frameworks use the same "fix the free constant by requiring the weak-field limit" move |
| MOND-like behavior | Attempted once (biharmonic screening, `dark_matter_energy.md` Section 2.5) — **already a documented failure**, ~54 orders of magnitude too small a screening length (corrects a stale "20 orders" figure caught while writing this comparison — see Section 4.1) | Derived cleanly: µ → Milgrom's interpolating function exactly in the coherent limit (Eq. 88) — **independently verified below, holds up** | **TFG succeeds where PDTP's own attempt has already failed** — the sharpest, most consequential comparison point |
| Assumption-tagging discipline | Explicit `[ASSUMED]`/`[DERIVED]`/`[SPECULATIVE]` tags on every equation (CLAUDE.md requirement) | Less consistently separated — e.g. Eq. 33 restricts the phase-coherence correlation to ρ∈[0,1] by a plausibility argument ("a random thermal bath cannot spontaneously generate sustained anti-aligned work"), not a derivation, without flagging it as a distinct assumption from the surrounding derived steps | **Methodological difference, not a "gotcha"** — noted fairly, not to dismiss the paper |

---

## 3. Independent Verification of TFG's Own Key Claims

Per this project's own standing rule (never build a comparison on an
external claim without checking it), the following TFG equations were
independently re-derived with SymPy (`t77_timeflow_gravity_check.py`),
**not accepted on the paper's authority alone**:

| # | TFG equation checked | Result |
|---|---|---|
| 1 | Eq. 86 → 87: speed of light cancels from µ(a,a₀,θ) | **Confirmed**, residual 0 |
| 2 | Eq. 87 → 88: coherent limit (cosθ→1) reduces to Milgrom's a/(a+a₀) | **Confirmed**, residual 0 |
| 3 | Eq. 89 → 90: deep-MOND limit gives a = √(g_N·a₀) | **Confirmed**, residual 0 |
| 4 | Eq. 99: f_order = 2A₀/(2πA₀) = 1/π | **Arithmetic confirmed** — but see Section 2's methodological note: the diameter-vs-circumference measure choice is a modeling assumption, not forced by the field equations alone |
| 5 | Eq. 133 → 137 → 138: continuity-equation derivation of w(a), numeric w(1) | **Confirmed**, residual 0 at every step; w(1) = −0.8444 computed independently (paper states ≈ −0.84) |

**Result:** every TFG derivation chain actually checked here is internally
consistent — this is not a paper with hidden algebra errors. The one
place a critical eye is warranted is not the *math* but a *modeling
choice* (Section 2's partition argument) presented with more certainty
than it has.

---

## 4. Head-to-Head on Overlapping Claims

### 4.1 MOND / Galactic Rotation Curves — the sharpest comparison point

**TFG:** derives Milgrom's exact interpolating function as the coherent
limit of a general thermodynamic efficiency factor (verified above,
Section 3 #1-2) — no free parameter, no tuning, a direct algebraic
consequence of the framework's own definitions.

**PDTP:** `dark_matter_energy.md` Section 2.5 (that file's own internally
labeled "Falsifiable Prediction 9" — a separate numbering track from the
project's canonical `falsifiable_predictions.md` list, worth reconciling
as a minor housekeeping item sometime, not attempted here) already
attempted a structural MOND analogue via the biharmonic screening length
(∇⁴Φ + 4g²Φ = source, Part 61): **already found to fail by ~54 orders of
magnitude** (L_heal ~ l_Planck ~ 1.6×10⁻³⁵ m vs. a representative galactic
scale of 1 kpc ~ 3.1×10¹⁹ m, computed directly — corrects a stale "20
orders" figure in `dark_matter_energy.md`, caught and fixed while writing
this comparison). T74/Part 142 (this session, 2026-09-10) independently
re-derived the same Planck-scale screening conclusion via a completely
different route (the φ₋ dispersion relation, ~50 orders short by the same
comparison), corroborating the negative twice over — with two different
numbers, not the same calculation repeated, since the routes evaluate
different quantities (vacuum healing length vs. Earth-potential decay
length).

**This is a genuine, concrete gap.** PDTP has tried and failed, twice
independently, at the exact thing TFG's derivation (verified above to
hold up) reaches cleanly. This should be stated plainly, not softened —
it is the single most important finding of this comparison.

### 4.2 Ω_m = 1/π ≈ 0.3183 — parameter-free, close to measurement

Compares to Planck 2018's Ω_m = 0.315 ± 0.007 — TFG's figure sits about
0.5% high, just outside the quoted 1-σ band (0.008 over 0.007) but well
within the "right ballpark" standard this project itself applies to its
own geometric-factor results (e.g. Part 37's σ_SU3 estimate, 3.4× off,
still counted a genuine success). The arithmetic is confirmed (Section 3
#4); the modeling choice behind it (why "diameter" specifically measures
the coherent sector) is not independently re-derived here and should be
read as an assumption, not a proof, exactly as PDTP would tag its own
analogous choices (e.g. Part 126's O(1) cluster-widening finding for a₀).

### 4.3 Dark Energy w(z) — TFG lands closer to DESI than PDTP's own number

**TFG:** w(1) = −0.8444 (independently verified, Section 3 #5).
**DESI DR2 + CMB + Pantheon+ (as cited in TFG's own paper):**
w₀ = −0.838 ± 0.055. **Deviation: 0.12σ.**

**PDTP's own canonical prediction** (`falsifiable_predictions.md`
Prediction 5, Parts 25-26): w₀ ≈ −0.92, w_a ≈ −0.02.
**Deviation from the same DESI figure: (−0.838 − (−0.92))/0.055 ≈ 1.5σ.**

**This is an honest asymmetry worth stating directly, not minimizing:**
on this specific, actual measured number, TFG's parameter-free result
currently sits closer to the data than PDTP's own project-wide prediction
does. PDTP's own w(z) story has evolved since Part 25/26 (Part 117/T44's
transient EDE, Part 119/T46's "Lambda as locking fossil" with β(z) still
explicitly OPEN for magnitude) — none of those newer threads yet produce
a single, settled, citable w₀ number sharper than the original
Prediction 5 figure this comparison uses.

### 4.4 Bullet Cluster — complementary, not competing

**TFG:** explains the *spatial offset* (lensing peak vs. gas) as a
shock-induced decoherence transition — hot, collisional gas loses phase
coherence (cosθ→0) and "sheds" its lensing halo, while collisionless
galaxies retain coherence and keep organizing the vacuum.

**PDTP (T69/Part 138):** addresses a *different* aspect entirely — the
self-interaction cross-section bound (σ/m must be small enough that DM
doesn't visibly interact during the collision), with a corrected 47.3
order-of-magnitude margin.

These are not rival explanations of the same fact — TFG explains *why
the lensing peak is where it is*; PDTP's result constrains *how strongly
DM can self-interact*. Both could be true simultaneously; neither result
bears directly on the other. Stated precisely here so future work doesn't
conflate them as competing claims.

### 4.5 Jacobson's Argument — shared anchor, different machinery

Both frameworks build on T. Jacobson's 1995 derivation of Einstein's
equations from the Clausius relation on local Rindler horizons — but not
in the same way. PDTP's own route (Part 86) counts lattice cells
(S_PDTP = k_B·ln(2)·A/a₀²) to get an *induced* (Sakharov) graviton
kinetic term, with Part 114's Trace Theorem proving this 1-loop route is
the framework's *only* source of graviton dynamics — a very different
technical object from what TFG does, which keeps Jacobson's original
horizon argument intact but rescales the *heat flux itself* by the
efficiency factor µ. Citing "both use Jacobson" without this distinction
would overstate the convergence.

---

## 5. Falsifiability Comparison

TFG's own criterion (Section 11): the intrinsic scatter of the Radial
Acceleration Relation (RAR) should anti-correlate with local kinematic
entropy, via cosθ = V²_rot/(V²_rot + 3σ²_v) — directly measurable from
integral-field spectroscopy (Cappellari 2016; Lelli et al. 2016 SPARC
data). This is a clean, near-term, quantitative test, distinct from any
of PDTP's own 16 ranked predictions in `falsifiable_predictions.md`.

**No direct overlap or conflict** between TFG's RAR/kinematic-entropy
test and PDTP's own prediction list (breathing mode, GW birefringence,
screened fifth force, hollow-shell test, etc.) — the two frameworks
would be falsified or supported by different, non-overlapping
observations. Worth noting for completeness, not resolved further here.

---

## 6. Verdict and Status

**TODO_04.md T77 — RESOLVED: MIXED — convergent validation + a concrete,
honestly-stated gap + real structural differences.**

1. **Convergent validation (weak-to-moderate signal):** two independently
   motivated frameworks, built by different people with no apparent
   connection, both landed on a compact U(1) phase field as the
   fundamental object, both use Jacobson's entropic-gravity argument as
   an anchor, and both fix a normalization constant by demanding
   Newtonian-limit recovery. This is a real, if modest, corroborating
   signal for the general "gravity from phase coherence" family of
   ideas — not proof of either specific framework.
2. **A genuine gap, not just a thematic echo (the main finding):** TFG's
   MOND-limit derivation independently checks out (Section 3) and lands
   exactly on Milgrom's function; PDTP's own structural MOND attempt is
   an already-documented, twice-confirmed ~54-order-of-magnitude failure
   (corrected from a stale "20 orders" figure caught while writing this
   comparison).
   Separately, TFG's parameter-free w₀ sits 0.12σ from DESI where PDTP's
   own canonical prediction sits ~1.5σ away. These are places TFG's
   framework currently reaches that PDTP's has not — stated plainly, as
   the honest reading of the actual numbers, not softened for either
   framework's benefit.
3. **Real structural differences mean this is not "PDTP in different
   words":** TFG's single-field order/chaos decomposition, its
   Lagrangian-free status, and its new global entropy-conservation
   postulate are all genuinely different from PDTP's two-field,
   Lagrangian-first, no-extra-postulate construction. Any future work
   should not assume TFG's successes transfer to PDTP by analogy alone —
   the underlying objects are not the same object.

**What remains open:** whether PDTP's own field content could be
restructured to reach TFG's MOND result (a large, separate undertaking,
not attempted here); reconciling the two "Falsifiable Prediction 9"
labels across `falsifiable_predictions.md` and `dark_matter_energy.md`
(minor housekeeping); whether newer PDTP threads (T44/T46) could be
pushed to a sharper w₀ figure than Prediction 5's original −0.92.

---

## 7. Sources

- **Source:** Trofimov, M. (2026), "Timeflow Gravity: a thermodynamic
  theory of spacetime", *Class. Quantum Grav.* 43, 135020, DOI:
  10.1088/1361-6382/ae811d — full text read directly for this comparison.
- **Reused, not re-derived:** Jacobson, T. (1995), *Phys. Rev. Lett.* 75,
  1260 (cited by both frameworks); Milgrom, M. (1983), *ApJ* 270, 365
  (MOND); Planck Collaboration (2020), *A&A* 641, A6 (Ω_m = 0.315±0.007);
  DESI DR2 + CMB + Pantheon+ (w₀ = −0.838±0.055, as cited in the TFG
  paper itself).
- **PDTP results reused, not re-derived:** Part 86 (Jacobson/lattice-cell
  entropy), Part 114 (Trace Theorem), `dark_matter_energy.md` Section 2.5
  (biharmonic MOND attempt, NEGATIVE), T74/Part 142 (independent
  Planck-scale screening re-derivation), `falsifiable_predictions.md`
  Prediction 5 (w₀≈−0.92, w_a≈−0.02), T69/Part 138 (Bullet Cluster
  self-interaction margin).
- **PDTP Originals in this document:** none — this Part is a comparison,
  reusing established results on both sides; the independent SymPy
  verification of TFG's own equations (Section 3) is the only new
  computational work performed here.

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*

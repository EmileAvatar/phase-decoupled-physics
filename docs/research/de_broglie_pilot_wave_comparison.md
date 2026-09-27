# Part 151 — De Broglie Double-Solution Pilot-Wave Comparison (Darrow & Bush 2024)

**Phase:** 151 — comparison doc, no new derivation (matches this item's own
scoping) and no new script — same rigor level as T27 (Elastic Universe
review) and T75 (TeVeS structural comparison): extract useful structural
parallels and differences honestly, without claiming either framework
validates the other.
**Date:** 2026-09-27
**Status:** DONE.
**Closes:** TODO_04.md T78
**Source read directly, in full (31 pages), not from a secondhand
summary:** Darrow, D. and Bush, J.W.M. (2024), "Revisiting de Broglie's
Double-Solution Pilot-Wave Theory with a Lorentz-Covariant Lagrangian
Framework," *Symmetry* 16, 149,
[doi:10.3390/sym16020149](https://doi.org/10.3390/sym16020149),
[arXiv:2408.06972](https://arxiv.org/abs/2408.06972) — real,
peer-reviewed, open-access. PDF at `assets/pdfs/2408.06972v1.pdf`.
**Note on the source note:** `docs/misc/notes 2026-09-10.txt` included a
Google AI summary of this paper and flagged it explicitly ("so we need to
double check"). The summary's four bullet points (variational foundation,
two-way coupling, Compton-scale oscillations, harmony of phases) all
check out against the actual text — but the primary source contains
substantially more structure (the exact action, field/particle equations,
the specific AM coupling, the effective-mass and uncertainty-principle
derivations) needed for a real structural comparison, none of which the
summary captured. Read directly here, as this project's own standard requires.

---

## 1. Plain English Summary

Darrow & Bush (D&B) build a real, rigorous, peer-reviewed alternative to
standard quantum mechanics: a classical particle and a classical wave
field that push and pull on each other (not the one-way "wave guides
particle, particle doesn't affect wave" picture of ordinary Bohmian
mechanics). They show that if you set this up correctly and make it
properly relativistic, several things de Broglie originally *guessed*
in 1923 — that a particle has an internal clock vibrating at the Compton
frequency, that this clock stays in "harmony" with its own guiding wave,
that momentum and wavelength satisfy `p=ℏk` — all fall out as genuine
mathematical *consequences*, not assumptions.

**PDTP shares the same target and the same overall spirit** (a matter
phase kept "in phase" with a guiding field, both dynamical, both
pushing on each other) **but gets there by a structurally different
route, and the comparison surfaces two honest, useful gaps** — one
about what PDTP currently assumes rather than derives, one about
relativistic completeness. Neither framework validates the other; this
is a mapping exercise, per the item's own scope.

---

## 2. The Darrow & Bush Framework, As Actually Presented

### 2.1 The Action

A complex Klein-Gordon field `φ` (mass `m̃`) plus a relativistic point
particle (mass `m`), coupled through a real coupling function
`σ(φ(q_p), φ*(q_p))` evaluated **at the particle's own position**:

```
S = S_field + S_part
S_field = Int d^4q [ d_mu(phi*) d^mu(phi) - m_tilde^2 |phi|^2 ]
S_part  = -Int dt  gamma^-1 * m * sigma(phi, phi*)
```

**[ESTABLISHED, re-derived directly from the source]** Varying against
`φ*` and the particle position/velocity gives the coupled Lorentz-
covariant equations:

```
(d_mu d^mu + m_tilde^2) phi = m^-1 gamma^-1 delta^3(q - q_p) d(sigma)/d(phi*)
d_t(m sigma gamma u) = gamma^-1 m grad(sigma)
```

**Plain English:** the particle sources the field at its own location
(first equation — a point source whose strength is set by `∂σ/∂φ*`),
and the field's local gradient pushes the particle (second equation).
Genuinely two-way, exactly Lorentz-covariant, and — a structural
detail worth keeping in mind for §5 — `σ` enters the particle's action
as a **multiplier on its rest mass**, which is what keeps the particle
exactly on-shell (`E²=m²+p²`) at all times.

### 2.2 The Worked Case: Amplitude-Modulated (AM) Coupling

D&B's entire detailed analysis uses one specific, simple choice:

```
sigma = 1 + b^2/(4*pi) + b * Re(phi)                    [linear in phi]
```

for a coupling constant `b`. This decouples the imaginary part of `φ`,
giving a real scalar field sourced by a point particle with fixed
strength `b`, and a particle equation `d_t(mγu) ≈ bmγ⁻¹∇φ` — the
particle accelerates along the local gradient of a field it sources
with **constant** strength, structurally a relativistic Yukawa-coupled
scalar (the same mathematical family as a scalar-Yukawa QFT toy model,
not a periodic/phase-locking coupling).

### 2.3 Key Results (Read Directly From the Paper, Not Summarized)

1. **Static dressing.** A particle at rest carries a static Yukawa
   wavepacket `φ = (b/4πm|q|)e^(−m|q|)` — range = the Compton wavelength
   `1/m`. Boosted, this becomes a Lorentz-contracted packet (their Eq. 15).
2. **Zitterbewegung emerges, it is not imposed.** Solving the coupled
   equations numerically (and confirming analytically, §3.4 of the
   paper), the particle spontaneously oscillates at frequency `γ⁻¹ω_c`
   — the Compton frequency, Doppler-shifted into the particle's own
   rest frame — **without any oscillation being put into the coupling
   by hand.** Contrast explicitly drawn by the authors against their
   own prior HQFT work (Dagan & Bush), where a `cos(2ω_c t)` forcing
   *is* imposed by construction.
3. **Dynamical harmony of phases.** As the particle accelerates, the
   wave's local wavelength and the particle's oscillation frequency
   both update in real time to keep `p=ℏk` satisfied at the particle's
   position — de Broglie's own "harmony of phases," now a proven
   consequence of the dynamics rather than a postulate.
4. **Effective mass.** The particle's own trailing wavepacket carries
   momentum that adds to its inertial response: `P_eff = (m + b²δm)γu`
   — a real, derived mass renormalization from the coupling (§3.5 of
   the paper, their Eq. 21).
5. **Classical uncertainty principle.** Combining the oscillation
   amplitude and the effective mass in a wall-bounded geometry gives
   `σ_x σ_p ≥ ½ħ(m_eff/m)n_b⁻²`, which the authors show reduces to the
   ordinary Heisenberg relation for sufficiently large coupling `b`
   (their Eq. 24) — explicitly flagged by the authors themselves as
   a *different kind* of uncertainty than quantum mechanics' own
   (no squeezing between position and momentum is possible in their
   version), not claimed as a full derivation of QM.

---

## 3. PDTP's Own Matter-Wave Framework, Recapped

```
L = (1/2)(d_mu phi)^2 + Sum_i (1/2)(d_mu psi_i)^2 + Sum_i g_i cos(psi_i - phi)
```

- `φ` = spacetime condensate phase; `ψᵢ` = matter phase field for particle `i`.
- Coupling: `g·cos(ψᵢ−φ)` — periodic (trigonometric) in the **phase
  difference**, not linear in either field's value.
- Field equations: `□φ = Σgᵢsin(ψᵢ−φ)`, `□ψⱼ = −gⱼsin(ψⱼ−φ)` — both
  fields are symmetric, dynamical, mutually sourcing.
- **The de Broglie relation is a stated prerequisite**, not a derived
  consequence: `mathematical_formalization.md` §1.5 imports
  `ψ(x,t) = A·exp(i(k·x−ωt+φ₀))` directly from standard matter-wave
  theory (cited to Wikipedia) as one of the "established mathematical
  tools used throughout this document," alongside Euler-Lagrange,
  Noether, and the Kuramoto model. PDTP's own `ψᵢ` is understood to
  carry this same oscillating-phase character from the start (matching
  T81/Part 146's own framing, `ψᵢ ≈ ω̄τᵢ`, an internal clock phase).

---

## 4. Structural Comparison Table

| Feature | Darrow & Bush (2024) | PDTP |
|---|---|---|
| Field content | One complex Klein-Gordon field `φ` + one external point particle | Two (or more) real phase fields `φ`, `ψᵢ`, symmetric roles |
| Coupling form | `σ` **linear** in `φ` (AM case) | `g·cos(ψᵢ−φ)`, **periodic** in the phase difference |
| Two-way coupling | Yes — particle sources field, field pushes particle | Yes — same structural idea |
| Source strength | **Constant** (`b`, fixed) — always radiating at the same rate | **Variable**, `∝sin(ψᵢ−φ)` — vanishes when phases align, maximal at 90° mismatch |
| Compton/de Broglie oscillation | **Emergent** — falls out of solving the coupled equations | **Assumed** — imported as a prerequisite (§1.5) |
| Relativistic treatment | Exact, throughout (γ factors, on-shell mass via `σ` multiplying `m` in the action) | Largely weak-field/non-relativistic-limit first (per this item's own filing) |
| Effective mass from coupling | Derived quantitatively, `m_eff = m + b²δm` | Not yet derived in this form (PDTP has `G_eff=2G_bare` from a different mechanism, Part 61) |
| Uncertainty principle | Derived (different in kind from QM's own) | Not attempted |

---

## 5. Key Question 1 — Does the Compton-Scale Oscillation Mechanism Match Structurally, or Only by Analogy?

**Only by analogy, and it's worth being precise about why.** D&B's
central achievement is showing that a coupling with **no built-in
oscillation** (`σ` is a plain linear function of the field value) still
produces a spontaneously oscillating particle, because the particle
"surfs" over its own retarded, self-sourced wave. The oscillation is a
genuine *output* of the dynamics.

PDTP's `ψᵢ` is not built up this way. `mathematical_formalization.md`
§1.5 imports the oscillating matter-wave `ψ(x,t)=A·exp(i(k·x−ωt+φ₀))`
directly, before any dynamics from the PDTP coupling term is applied —
the de Broglie oscillation is a **prerequisite ingredient**, the same
way Euler-Lagrange or Noether's theorem are prerequisites. PDTP has not
(at least not yet, not in any document reviewed for this comparison)
shown that its own `g·cos(ψᵢ−φ)` coupling, starting from a
*non*-oscillating `ψᵢ`, forces an oscillation to emerge the way D&B's
linear coupling does. **This is a real, identifiable gap, not a minor
wording difference**: it means PDTP currently presupposes the very
thing (matter-wave oscillation at the correct frequency) that D&B's
paper derives from a simpler starting point. Both target de Broglie's
own 1923 "harmony of phases" concept — literally the same phrase — but
by different means: D&B derive it, PDTP imports it.

---

## 6. Key Question 2 — Is Their Two-Way Coupling the Same Mechanism as `cos(ψ−φ)`, or Different?

**Different mechanism, real parallel at one level only.** Both
frameworks reject the standard one-way Bohmian coupling (wave guides
particle; particle doesn't source the wave) in favor of genuine
backreaction — that specific choice is a real, legitimate structural
match, not a coincidence, and worth crediting as such: it is the same
foundational move de Broglie's own original double-solution program
called for, and both this paper and PDTP make it explicitly.

But the coupling **functions themselves** are different in kind:

- D&B's `σ = 1 + b²/4π + b·Re(φ)` is **linear** in the field value, with
  a **constant** source strength `b` — structurally a relativistic
  Yukawa coupling (the same functional family used for scalar-mediated
  forces generally), always "on," never self-quenching.
- PDTP's `g·cos(ψᵢ−φ)` is **periodic** in the phase *difference* between
  two dynamical fields, with a source strength `∝sin(ψᵢ−φ)` that
  **vanishes exactly when the phases align** and peaks at 90°
  mismatch — structurally closer to a Josephson-junction coupling (this
  project's own recurring analogy, e.g. T80/Part 147) than to a Yukawa
  coupling.

**Practical consequence:** D&B's particle is always radiating/sourcing
at a fixed rate regardless of its own phase state; PDTP's matter phase
*self-quenches* its sourcing of the spacetime field exactly at
lock (`ψᵢ=φ`) — this self-quenching behavior, central to PDTP's whole
gravity-as-phase-locking picture, has no counterpart in D&B's AM
coupling at all. **One genuine shared feature is worth naming
explicitly:** in both frameworks, the coupling function directly
modulates the particle's effective inertial response (D&B's `σ`
multiplies `m` in the action; PDTP's `α=cos(ψ−φ)` is explicitly
described, per CLAUDE.md, as "α=1 is normal gravity, α→0 is
decoupled" — both are, in spirit, "how strongly is this particle
coupled to its guiding field" knobs) — same spirit, different
functional form.

---

## 7. Key Question 3 — Does the Lorentz-Covariant Formulation Offer Anything PDTP Hasn't Addressed?

**Yes, genuinely.** D&B's framework is relativistic **by construction**
from the first line: proper time `τ`, exact four-vectors, `γ` factors
carried through every equation, and — the more substantial point — the
coupling `σ` enters as a literal multiplier on the particle's rest mass
in the action, which is specifically what keeps the particle exactly
on-shell (`E²=m²+p²`) throughout its motion, even while exchanging
energy with the field. This is a nontrivial relativistic consistency
requirement, explicitly derived and checked in the paper (their §2,
Remark following Eq. 3).

PDTP's own Lagrangian is *written* in a covariant-looking form
(`∂_μφ∂^μφ` kinetic terms), but this item's own filing already flagged
PDTP's derivations as "largely non-relativistic-limit-first," and
nothing reviewed for this comparison shows PDTP checking the analogous
question for its own matter sector: does `g·cos(ψᵢ−φ)`, treated as a
term that could modify a particle's effective relativistic mass the
way D&B's `σ` does, keep a moving matter-phase particle correctly
on-shell at all velocities, not just in the weak-field/non-relativistic
limit already worked out (main document §7)? **This is a concrete,
well-posed open question this comparison surfaces, not previously
stated this precisely anywhere in the project** — flagged here as a
finding of the comparison itself, not filed as a new TODO item (per
this item's own Low-Medium, comparison-only scope).

---

## 8. Verdict and Status

**TODO_04.md T78 — RESOLVED: real, useful structural comparison; two
genuine PDTP gaps identified, no claim of validation either way.**

1. **Shared spirit, confirmed genuine, not just marketing:** both
   frameworks build a two-way-coupled, classical, field-theoretic
   version of de Broglie's own "harmony of phases" concept, explicitly
   rejecting the one-way Bohmian alternative.
2. **Key Question 1 — gap identified:** PDTP currently *imports* the
   matter-wave oscillation as a prerequisite (§1.5) rather than
   *deriving* it dynamically from a non-oscillating coupling, the way
   D&B do. Not fatal to PDTP, but an honest asymmetry worth recording.
3. **Key Question 2 — different mechanism, correctly distinguished:**
   D&B's linear/constant-strength coupling is a different mathematical
   object from PDTP's periodic/self-quenching phase-locking coupling,
   despite both being genuinely two-way. Conflating them would be a
   real error this comparison specifically avoids.
4. **Key Question 3 — gap identified:** PDTP has not shown its matter
   sector remains correctly on-shell under a relativistic (not just
   weak-field) treatment the way D&B's on-shell-preserving mass-coupling
   does. A concrete, well-posed open question, surfaced but not
   resolved here, matching this item's own comparison-only scope.
5. **What this comparison does NOT claim:** that D&B's paper validates
   PDTP, that PDTP validates D&B's paper, or that either framework's
   success transfers to the other. They target the same historical
   idea from different starting assumptions and reach genuinely
   different mathematical structures.

---

## 9. Sources

- **Source:** Darrow, D. and Bush, J.W.M. (2024), "Revisiting de
  Broglie's Double-Solution Pilot-Wave Theory with a Lorentz-Covariant
  Lagrangian Framework," *Symmetry* 16, 149,
  [doi:10.3390/sym16020149](https://doi.org/10.3390/sym16020149) —
  read directly in full (31 pages) for this comparison.
- **Reused, not re-derived:** `mathematical_formalization.md` §1.5 (de
  Broglie relation prerequisite), CLAUDE.md's own U(1) Lagrangian, T81/
  Part 146 (`kinematic_coherence_mond_retry.md`, `ψᵢ≈ω̄τᵢ` framing),
  T80/Part 147 (`em_from_geometry_gauging.md`, the Josephson-junction
  analogy for PDTP's coupling), Part 61 (two-phase Lagrangian, `G_eff`).
- **Context:** `docs/misc/notes 2026-09-10.txt` (source flagging + AI
  summary, independently verified against the primary text here) and
  its embedded Consensus.app review, which cited this paper as
  literature support for PDTP's "wave-based matter models" claim
  (rated "Moderate, 6/10") — this comparison neither confirms nor
  disputes that rating; it is a separate, structural exercise.

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*
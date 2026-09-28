# G_eff = 2·G_bare Audit (Part 156)

**TODO:** TODO_04.md T83, sub-task **83d** — worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-09-28.
**Script:** `simulations/solver/t83d_geff.py`
**Log:** `simulations/solver/outputs/t83d_geff_<timestamp>.txt`
**Scorecard:** 8 matches, 3 contradictions out of 11 tests (the
contradictions locate exactly which readings of the factor 2 fail).
**Status:** CLARIFIED. G_eff = 2·G_bare is **correct as a comparison at
equal g**, but (1) it is **not** caused by, or "consistent with", the
Newton's-3rd-law factor ψ̈ = −2φ̈₊ — that factor is a naming convention;
(2) it is **not observable** (g is free, so it is absorbed into the measured
G); (3) two-phase is **not** "single-phase with g doubled"; (4) away from
the vacuum G_eff/G = 2 sin²φ₋, not 2 sin φ₋.

---

## Plain-English Summary

The two-phase Lagrangian has two couplings of strength g (bulk and
surface). At the vacuum (φ₋ = π/2) they line up and add, so matter feels a
coupling of **2g** instead of g. Spacetime's gravity mode φ₊ is also twice
as "heavy/stiff", so a given source makes the **same** field as in the
single-phase theory — but a test body feels it **twice** as strongly.
Net: gravity comes out twice as strong for the same g. That part of
Part 62's claim holds.

Three things said *about* it do not hold:

1. **It has nothing to do with ψ̈ = −2φ̈₊.** That "2" appears only because
   φ₊ was defined as the *average* of the bulk and surface phases. Define it
   as their *sum* and the same law reads ψ̈ = −Σ̈ (factor 1) — nothing
   physical changed. The G_eff factor, by contrast, is the same in every
   choice of variables. Two unrelated 2s.
2. **It can't be measured.** g is a free parameter. Whatever g is, the
   measured Newton's constant already includes the factor 2 — you can never
   see "G_bare" separately. (Part 62 and Part 100 already said this; it
   stands.)
3. **It is not a simple "double g".** If two-phase were just single-phase
   with g → 2g, every quantity would scale by 2. The frequency of the
   matter–spacetime wobble scales by 3/2 instead. So the factor 2 is
   specific to the gravitational interaction strength.

**Bonus correction:** Part 62 suggested that when φ₋ lags behind its
vacuum value, the effective coupling is 2g·sin φ₋. The *gravitational*
strength goes as the coupling squared over the stiffness, so
G_eff/G = 2 sin²φ₋. At φ₋ = π/4 that is 1.0, not 1.41. This matters for
Part 62's proposed "frequency-dependent G" in merging binaries.

**Caveat carried from Part 153 (83a):** all of this compares strengths
*given* a maintained phase offset. The Lagrangian by itself does not supply
that offset (sub-task 83i).

---

## 1. Setup [ASSUMED]

```
L_1 = 1/2 (d phi)^2 + 1/2 (d psi)^2 + g cos(psi - phi)                              (156.1)
L_2 = 1/2 [(d psi)^2 + (d phi_b)^2 + (d phi_s)^2] + g cos(psi - phi_b) - g cos(psi - phi_s)   (156.2)
```

$$
\mathcal L_1 = \tfrac12(\partial\phi)^2 + \tfrac12(\partial\psi)^2 + g\cos(\psi-\phi),\qquad
\mathcal L_2 = \tfrac12\left[(\partial\psi)^2 + (\partial\phi_b)^2 + (\partial\phi_s)^2\right] + g\cos(\psi-\phi_b) - g\cos(\psi-\phi_s)
$$

Field equation for a field with inertia/stiffness I (Lorentz-invariant
kinetic term, so the same I multiplies ∂_t² and ∇²): I(q_tt − ∇²q) = F_q,
F_q = ∂L_int/∂q; static ∇²q = −F_q/I [Goldstein §13.3].
Newtonian interaction energy between a source and a test body through a
field of stiffness K scales as (a_source · a_test)/K, where a are the
couplings (Green's function of K∇²; cf.
[Poisson's equation — Wikipedia](https://en.wikipedia.org/wiki/Poisson%27s_equation)).

**Assumptions:** [A1] φ₋ held at the Part 119 vacuum π/2 unless stated;
[A2] linear response; [A3] a phase offset Δ is given (Part 153).

---

## 2. Derivations [DERIVED, VERIFIED]

### 2.1 Coherent amplitude at the vacuum

With φ_b = φ₊ + φ₋, φ_s = φ₊ − φ₋ and φ₋ = π/2:
cos(ψ − φ₊ − π/2) = sin(ψ − φ₊) and −cos(ψ − φ₊ + π/2) = sin(ψ − φ₊), so

```
L_int(phi_- = pi/2) = 2 g sin(psi - phi_+) = 2 g cos(psi - phi_+ - pi/2)           (156.3)
```

$$
\mathcal L_\text{int}\big|_{\phi_-=\pi/2} = 2g\,\cos\!\left(\psi-\phi_+-\tfrac{\pi}{2}\right)
$$

[VERIFIED: S1, residual 0.] Amplitude in general: 2g sin φ₋.

### 2.2 Source → field and field → test (at equal g)

Let Δ = ψ − φ (single) or Δ = ψ − φ₊ − π/2 (two-phase), linearised.

**Single phase** (I_φ = 1): F_φ = g sin Δ ≈ gΔ, so ∇²φ = −gΔ (source → field
coefficient −g). F_ψ = −g sin Δ ≈ −gΔ (field → test coefficient −g).

**Two phase** (I₊ = 2): F₊ = ∂/∂φ₊[2g cos(ψ − φ₊ − π/2)] = 2g sin Δ, so
∇²φ₊ = −F₊/2 = −gΔ (coefficient −g). F_ψ = −2g sin Δ ≈ −2gΔ (coefficient −2g).

```
source->field ratio = 1,   field->test ratio = 2,   G_eff / G_single(g) = 1 x 2 = 2     (156.4)
```

$$
\frac{G_\text{eff}}{G_\text{single}(g)} = \underbrace{1}_{\text{source}\to\text{field}}\times\underbrace{2}_{\text{field}\to\text{test}} = 2
$$

[VERIFIED: S6, S7, S8 — ratios read from the computed linear coefficients.]
Equivalently (a_s a_t)/K = (2g)(2g)/2 = 2g² vs g·g/1 = g².

### 2.3 The Newton's-3rd-law factor is a naming convention

Joint shift ψ, φ_b, φ_s → +a is a symmetry; the gravity-mode variable X
shifts by w_X. Noether: F_ψ + w_X F_X = 0. With inertia I_X:
ψ̈ = F_ψ, Ẍ = F_X/I_X ⇒ ψ̈ = −(I_X/w_X) Ẍ.

| Variable | Definition | I_X | w_X | Factor k = I_X/w_X |
|----------|-----------|-----|-----|--------------------|
| φ₊ | (φ_b + φ_s)/2 | 2 | 1 | **2** (Part 61) |
| Σ | φ_b + φ_s | 1/2 | 2 | **1** |

[VERIFIED: S2, S3 (Noether balance 0 in both bases), S4, S5.] The factor 2
depends on the arbitrary normalisation of the variable, whereas (156.4) is
an interaction energy and does not. The CLAUDE.md phrase "factor 2
consistent with G_eff = 2G_bare" links two unrelated numbers.

### 2.4 Not a uniform rescaling of g

Relative-mode frequency at the lock (ω² = g_amp(1/I_ψ + 1/I_field)):
single 2g; two-phase 2g(1 + 1/2) = 3g; ratio **3/2**, not 2 [S9]. Two-phase
equals single-phase with (g → 2g **and** I_φ → 2), not g → 2g alone
(consistent with Part 154's √3·g).

### 2.5 φ₋ dependence

Amplitude a(φ₋) = 2g sin φ₋ for both source and test; stiffness 2:

```
G_eff(phi_-) / G_single(g) = (2 g sin phi_-)^2 / 2 / g^2 = 2 sin^2(phi_-)           (156.5)
```

$$
\frac{G_\text{eff}(\phi_-)}{G_\text{single}(g)} = 2\sin^2\phi_-
$$

[VERIFIED: S10 (=2 at π/2), S11 (=1 at π/4, vs √2 from Part 62's linear
reading).]

---

## 3. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|----|------|----------|----------|--------|
| S1 | L_int at φ₋=π/2 = 2g cos(ψ−φ₊−π/2) | 0 | 0 | MATCH |
| S2 | Noether balance, φ₊ basis | 0 | 0 | MATCH |
| S3 | Noether balance, Σ basis (weight 2) | 0 | 0 | MATCH |
| S4 | Newton factor, φ₊ basis | 2 | 2 | MATCH |
| S5 | Newton factor basis-independent? | 1 (Σ basis) | 2 | **CONTRADICTION** |
| S6 | source→field ratio | 1 | 1 | MATCH |
| S7 | field→test ratio | 2 | 2 | MATCH |
| S8 | G ratio | 2 | 2 | MATCH |
| S9 | Mode ω² ratio (uniform g→2g ⇒ 2) | 3/2 | 2 | **CONTRADICTION** |
| S10 | G_eff/G at φ₋ = π/2 | 2 | 2 | MATCH |
| S11 | G_eff/G at φ₋ = π/4: sin² vs linear | 1 | √2 | **CONTRADICTION** |

**Score: 8/11.** Each contradiction rejects one *reading* of the factor 2
(tied to the Newton factor; a uniform g-rescaling; linear in sin φ₋); the
factor itself (S8, S10) is confirmed. **RECHECK note:** the first run of
S3 failed because the check used Noether weight 1 in the Σ basis (a bug in
the check, not the physics); fixed to weight 2 and documented in the script.
**Two-phase checks:** Newton's 3rd law holds in both bases (S2, S3).
**Standard Model compatibility:** no new term; no impact.

---

## 4. Impact

| Where | Change |
|-------|--------|
| `reversed_higgs.py` (Part 62) S8 | Was hardcoded `True` (RECHECK violation) → computed (a_s a_t/K); 10/10 PASS; comment adds sin² profile |
| `two_phase_lensing.md` (Part 100) Eq 100.A2 | Route "ψ̈ = −2φ̈₊ ⇒ G_eff = 2G_bare" invalid; factor still 2 by §2.2; **verdict (NEGATIVE, absorbed into G_N) unchanged** |
| `two_phase_rederivation.md` S3, table; `equation_reference.md` §2d; `pdtp_refractive_index.md`; `hawking_n_pdtp.md` | "consistent with / from Newton's 3rd law" wording corrected |
| Part 62 "frequency-dependent G" (binary mergers) | Use 2 sin²φ₋, not 2 sin φ₋ |
| CLAUDE.md | Wording fix deferred to 83h |

**Status:** 83d DONE. No falsifiable prediction changes (factor unobservable).

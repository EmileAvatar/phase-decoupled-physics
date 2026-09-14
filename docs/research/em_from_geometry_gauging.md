# Part 147 — Electromagnetism-from-Geometry (U(1) Connection) as a Blueprint for PDTP's EM Gap

**Phase:** 147 — `simulations/solver/t80_em_gauging.py`
**Date:** 2026-09-14
**Status:** DONE — the gauging construction WORKS exactly (a real new field,
correctly transforming, with the full Lagrangian exactly locally invariant),
but under minimal coupling alone that field is proven to carry **zero net
physical effect** on any PDTP prediction (non-dynamical, solved out exactly,
reproduces the original theory). A genuine EM-like sector would require a
further postulate PDTP's own structure does not currently supply or force.
13/13 Sudoku PASS.
**Output log:** `simulations/solver/outputs/t80_em_gauging_20260914.txt`
**Closes:** TODO_04.md T80

---

## 1. The Question

The source video ("Electromagnetism Derived From Geometry!", transcript in
`docs/misc/note 2026-09-14.txt`) lays out the standard textbook route from
local U(1) phase invariance to Maxwell's equations: demanding a matter
field's Lagrangian stay invariant under a *local* (x-dependent) phase
rotation forces a covariant derivative `D_μ = ∂_μ − ieA_μ`, and the new
connection field `A_μ`'s curvature `F_μν` gives Gauss's and Ampère's laws.

PDTP's absence of any such field has been flagged four separate times
across this project (`polarization_analogy.md` §3.5/§8.2, T66/Part 136's
closed torsion/rotation route, T70/Part 140's NLSM-scalar classification,
T75/Part 143's TeVeS comparison). **T80 asks whether applying this exact
construction to PDTP's own coupling term forces a genuine new field into
existence the same way.** T80's filing posed two central questions:

1. Does demanding LOCAL invariance of PDTP's coupling force a new field,
   the way the video's derivation forces `A_μ`?
2. If such a field emerges, does its own kinetic term naturally take the
   Maxwell-like `−¼F²` form with a physically sensible (stable) sign?

---

## 2. A Correction, Stated Up Front

T80's filing posed Key Question 1 as invariance under
`ψᵢ(x) → ψᵢ(x) + α(x)` **alone**, holding `φ` fixed. Checked directly
(`verify_global_symmetry()`): this is **not a symmetry at all**, not even
for constant `α` —

```
g*cos(psi - phi)  ->  g*cos(psi + alpha - phi)  != g*cos(psi-phi)  for alpha != 0
```

— SymPy residual: `g*(-cos(phi-psi) + cos(alpha-phi+psi))`, nonzero (S1).
The actual (and only) global symmetry of
`L₀ = ½φ̇² + ½ψ̇² + g·cos(ψ−φ)` is the **combined** shift,
`φ→φ+α, ψ→ψ+α`, with the *same* `α` for both fields — verified exactly
(residual 0, S2). This makes sense once stated plainly: the coupling term
only ever depends on the *difference* `ψ−φ`, so only a shift that leaves
that difference unchanged can be a symmetry of it. **This is the symmetry
gauged below**; the filing's literal wording is corrected here before any
derivation, per the project's RECHECK discipline, not silently adjusted.

---

## 3. Derivation

**Convention used throughout** (matching `sympy_checks.py`'s own
`verify_pdtp_field_equation()` style exactly): each field is represented by
a (value, "dot") symbol pair — e.g. `(phi, phi_dot)` — standing for the
field and its generic derivative at one representative point. A *local*
gauge transformation is captured by shifting the value by `α` and the
"dot" by an *independent* symbol `α_dot` (standing for `dα/dx` at that
point). This is rigorous, not a shortcut: for smooth `α(x)`, the value and
derivative of `α` can be prescribed independently at any single point, so
invariance for arbitrary `(α, α_dot)` there is exactly equivalent to
invariance under arbitrary smooth `α(x)` everywhere.

### 3.1 Step 1 — The Combined-Shift Symmetry (Eq. 147.1)

Established in Section 2 above:

```
phi -> phi + alpha,  psi -> psi + alpha   (same alpha, both fields)
=> L0 exactly invariant, for any constant alpha                    (147.1)
[DERIVED, SymPy residual = 0]
```

### 3.2 Step 2 — Noether Current (Eq. 147.2)

**Step 2.** The canonical Noether current for this symmetry,
`j = ∂L/∂φ̇ · 1 + ∂L/∂ψ̇ · 1`, re-derived (not assumed) together with both
fields' own Euler-Lagrange equations from `L₀` directly:

```
j = phi_dot + psi_dot                                               (147.2)
phi_ddot_eom = -g*sin(phi-psi)   [ = +g*sin(psi-phi), CLAUDE.md's
                                    field equation -- SymPy's canonical
                                    argument order differs by a sign
                                    flip inside sin(), same physics]
psi_ddot_eom = +g*sin(phi-psi)
dj/dx |_on-shell = phi_ddot_eom + psi_ddot_eom = 0        [DERIVED, exact]
```

**Plain English:** Noether's theorem says every continuous symmetry has a
conserved quantity. Here that quantity is just the *sum* of the two
fields' rates of change — and it is exactly conserved, confirmed by
direct computation on the original (ungauged) equations of motion, not
assumed from the theorem's general statement. This current is what `A_μ`
will end up coupling to once gauged (Section 3.5).

### 3.3 Step 3 — Gauging: the Full Lagrangian Is Exactly Locally Invariant (Eq. 147.3)

**Step 3.** Promote `α` to a function of `x`. Introduce covariant
derivatives with charge 1 for *both* fields (since both shift by the same
`α`):

```
D(phi) = phi_dot - A,   D(psi) = psi_dot - A,   A -> A + alpha_dot   (147.3)

L_gauged = (1/2)*D(phi)^2 + (1/2)*D(psi)^2 + g*cos(psi-phi)
```

Three things verified separately (`verify_local_gauge_invariance()`):

```
(i)   coupling term alone:      residual = 0            [no A needed at all]
(ii)  bare kinetic term alone:  residual = alpha_dot*(alpha_dot+phi_dot+psi_dot)
                                  != 0                   [motivates needing A]
(iii) full L_gauged:            residual = 0             [exactly invariant]
```

**Result (147.3) [DERIVED]: Key Question 1, corrected, answered YES.**
A real field `A` is forced into existence by demanding local invariance
of the combined-shift symmetry, transforming exactly the way the video's
`A_μ` does (`A → A + ∂_μα`). A genuinely new structural fact, not
present anywhere in PDTP before this Part: **the coupling term itself
needs no modification whatsoever** — unlike ordinary QED, where the
potential `V(|Φ|)` is separately invariant only because it depends on the
field's modulus, here `g·cos(ψ−φ)` is *already* exactly gauge invariant
before any covariant derivative is introduced, because it depends only on
the already gauge-invariant combination `ψ−φ`. Only the kinetic terms
need covariantizing.

### 3.4 Step 4 — Center/Relative Variables Diagonalize the Kinetic Term (Eq. 147.4)

**Step 4.** Define `Σ = (φ+ψ)/2` (carries the gauge charge — shifts by
`α` under the combined transformation) and `θ = ψ−φ` (gauge invariant —
carries *all* of PDTP's coupling physics, `g·cos(θ)`). SymPy-verified
identity:

```
(1/2)*phi_dot^2 + (1/2)*psi_dot^2  =  Sigma_dot^2 + (1/4)*theta_dot^2   (147.4)
[DERIVED, residual = 0 -- exact algebraic identity]

L_gauged  =  (Sigma_dot - A)^2 + (1/4)*theta_dot^2 + g*cos(theta)
             [re-expressed in Sigma/theta -- residual vs the (phi,psi,A)
             form above = 0, confirming the two descriptions are the
             same theory in different variables]

A appears in the theta (coupling/physics) sector: FALSE
```

**Plain English:** this is the *same* trick PDTP already used in Part
61's two-phase Lagrangian (splitting into `φ₊`/`φ₋` modes) — split the
system into a "center of mass" combination and a "relative" combination.
Here, the gauge field `A` only ever touches the center-of-mass mode `Σ`;
the relative mode `θ` — which is the *only* thing PDTP's coupling term
and every PDTP prediction actually depends on — never sees `A` directly
in the Lagrangian. This looked, at the planning stage, like it might mean
`A` is simply irrelevant to PDTP's physics. Step 5 shows that conclusion
is *almost* right, but for a sharper and more interesting reason than
"doesn't touch θ in the Lagrangian."

### 3.5 Step 5 — The Central Finding: `A` Is Non-Dynamical, and Drops Out Completely (Eq. 147.5–147.6)

**Step 5a.** Check whether `A` has its own kinetic term (a conjugate
momentum `π_A = ∂L/∂Ȧ`):

```
pi_A = dL_gauged/d(A_dot) = 0          [A_dot does not appear in L_gauged
                                         at all -- minimal coupling alone
                                         gives A NO kinetic term]        (147.5)
```

This matters structurally: without a `d(π_A)/dx` term to balance it,
`A`'s own Euler-Lagrange equation is not a wave equation — it degenerates
into an algebraic **constraint**:

```
force_A = dL_gauged/dA = 2*A - phi_dot - psi_dot = 0
=> A = (phi_dot + psi_dot)/2 = Sigma_dot                                (147.5')
[DERIVED -- A is forced, instant by instant, to equal the average rate
 of change of the two phases it couples]
```

**Step 5b.** What happens if this constraint is substituted back into
`φ`'s own (gauged) field equation? Two independent routes were computed
and compared:

```
Route 1 (solve the constraint, substitute into phi's gauged EOM,
         rewrite in terms of theta):
  phi_ddot - A_dot = g*sin(psi-phi),  A_dot = (phi_ddot+psi_ddot)/2
  => theta_ddot = -2*g*sin(theta)

Route 2 (Euler-Lagrange applied DIRECTLY to the isolated theta-sector
         Lagrangian from Step 4, (1/4)*theta_dot^2 + g*cos(theta),
         with NO A anywhere in it):
  => theta_ddot = -2*g*sin(theta)

Residual (Route 1 - Route 2) = 0                                        (147.6)
[DERIVED -- two independent derivations of the SAME equation agree exactly]
```

**Result (147.5–147.6) [DERIVED, the central finding]:** solving out the
non-dynamical `A` reproduces PDTP's **original, ungauged** equation of
motion for `θ = ψ−φ` **exactly**, with `A` cancelling out completely.
This is a precise, quantitative answer to Key Question 2, not a vague
"well, it's like QED": **minimal coupling alone is physically vacuous
for PDTP.** It introduces a field with exactly the right formal
transformation properties (Section 3.3), but that field carries zero
information of its own — it is entirely determined, at every instant, by
the two fields it couples to, and once solved for, changes nothing about
any PDTP prediction. This is the standard fate of a gauge field with no
independent kinetic term (a Lagrange-multiplier-like auxiliary field) —
worth noting as structurally reminiscent of the *disformal, non-dynamical
role* the vector field `A_μ` plays in TeVeS's construction (T75/Part 143),
though the underlying mechanism there is different (TeVeS's vector has an
independent kinetic term but is constrained to unit norm; here `A` has no
kinetic term at all).

### 3.6 Step 6 — If a Kinetic Term Is Postulated (Eq. 147.7)

**Step 6.** Section 3.5 makes precise exactly what PDTP's own structure
does *not* supply: an independent kinetic term for `A`. The video's own
construction gets this term from `−¼F_μν F^μν`, added to the Lagrangian
as a *separate* postulate — not something forced purely by demanding
invariance of the matter sector (the matter sector only forces `A` to
exist and transform correctly, not to propagate). This is structurally
the **same kind of move as Maxwell's own historical scaffolding**
(Methodology.md's own worked example: Maxwell added `∂E/∂t` to fix
Ampère's law's inconsistency with charge conservation, not because it was
observed — the term was later confirmed by Hertz).

A standalone two-coordinate check (`verify_F_munu_gauge_invariance_and_sign()`),
independent of the `(φ,ψ)` matter sector above, confirms this term is at
least well-formed if postulated:

```
F_01 = d(A1)/d(x0) - d(A0)/d(x1)
Under A_mu -> A_mu + d(alpha)/d(x_mu):  F01 residual = 0   [gauge invariant]

Metric signature diag(1,-1):
  -1/4 * F_mn*F^mn  =  (1/2)*F01^2                          (147.7)
  [VERIFIED -- positive-definite coefficient, i.e. the standard,
   non-ghost, healthy kinetic-term sign, same rigor standard as
   CLAUDE.md's own +cos stability requirement]
```

**Result (147.7) [VERIFIED, standard physics]:** IF such a term is added,
its curvature is gauge invariant and its sign is healthy — no obstruction
on that front. But nothing derived in Sections 3.1–3.5 supplies or
motivates this term from PDTP's own structure; it would be a genuinely
new, independent postulate, exactly on the same epistemic footing as
Maxwell's own historical move, not a "free" consequence of gauging.

### 3.7 Step 7 — Generalization to N=2 Matter Phases (Eq. 147.8)

**Step 7.** Repeat the construction with `φ` plus **two** matter phases
`ψ₁, ψ₂` (all charge 1), matching CLAUDE.md's full `Σᵢ gᵢcos(ψᵢ−φ)` form
rather than just the N=1 illustrative case:

```
Combined shift (phi,psi1,psi2 -> +alpha together): residual = 0  [symmetry holds]
Coupling rewritten via theta1=psi1-phi, theta2=psi2-phi: residual = 0
  [coupling = g1*cos(theta1)+g2*cos(theta2), no A needed, as before]

A-dependent piece of the gauged kinetic term:
  A*(3*A - 2*phi_dot - 2*psi1_dot - 2*psi2_dot)/2
  = (3/2)*A^2 - 3*A*Sigma3_dot,   Sigma3 = (phi+psi1+psi2)/3            (147.8)

Rewritten in (Sigma3_dot, theta1_dot, theta2_dot): depends on NEITHER
theta1_dot NOR theta2_dot -- confirmed by direct substitution, not assumed.
```

**Result (147.8) [DERIVED]:** the N=1 result (Sections 3.4–3.5) is not a
special case — for N=2, `A` still couples *only* to the fully-symmetric
center mode `Σ₃`, never to either relative (physics-carrying) mode. The
**independence argument** for general N (per CODING_STANDARDS.md §6):
this is a standard linear-algebra fact about a quadratic form with an
equal-weight shift symmetry acting on all N+1 variables — such a
symmetry always singles out exactly one "center of mass" combination
that carries the charge, with the remaining N combinations forming a
charge-neutral orthogonal complement. Having confirmed this holds for
N=1 (Section 3.4) and N=2 (this section) with the *same* mechanism in
each case (not two different tricks that happen to agree), there is no
structural reason it would fail for larger N.

### 3.8 Step 8 — Two-Phase Lagrangian (Part 61) Compatibility

**Step 8.** CLAUDE.md's Sudoku protocol item 4 requires checking any new
result against Part 61's two-phase Lagrangian,
`L = g·cos(ψ−φ_b) − g·cos(ψ−φ_s)`. Checked whether the combined-shift
symmetry (now for **three** fields — `ψ, φ_b, φ_s`, all shifting
together) survives the minus sign on the surface term:

```
coupling_two_phase -> (psi+alpha, phi_b+alpha, phi_s+alpha):
  residual = 0                                                    [holds]
```

**Result [DERIVED]:** yes — both cosine arguments (`ψ−φ_b` and `ψ−φ_s`)
are separately invariant under any *common* shift of all three fields,
regardless of the relative sign between the two terms, so the symmetry
this Part gauges survives Part 61's extension unchanged. **Full gauging
of the two-phase case is out of scope for this pass** (it would mean
repeating Sections 3.3–3.5 for three coupled fields instead of two) —
flagged as a natural, well-scoped follow-up if this direction is pursued
further, not attempted here.

### 3.9 Kaluza-Klein Cross-Check (Key Question 3) — Short, Bounded Comparison

T80's filing asked whether the video's "phase as a literal compact extra
dimension" reading offers a genuinely *different* route from the direct
local-symmetry route above. **Answer: no — it is the same underlying
symmetry, packaged geometrically, and inherits Section 3.5's finding
rather than escaping it.**

Kaluza's own 1921 construction starts from pure 5D general relativity
compactified on a small circle; the 5D metric's off-diagonal components
`g_5μ` are identified with the 4D `A_μ`, and the 5D Einstein-Hilbert
curvature term, expanded in the compact-circle radius, is what supplies
`A_μ`'s Maxwell kinetic term in 4D — the kinetic term does not appear
"for free" there either; it descends from an independent geometric
input (5D curvature dynamics) that has no counterpart in PDTP's current
condensate Lagrangian. PDTP's own gravity sector is not built this way —
it comes from the SU(3) emergent metric plus Sakharov induced gravity
(Parts 75–76, 114; see T79 Item 1), a structurally different mechanism
with no independent 5D-curvature term to draw a kinetic term from. So the
KK reading does not offer an escape from Section 3.5's central finding;
it would face the *identical* "where does the kinetic term come from"
question, just phrased geometrically instead of via minimal coupling.
**Not attempted as a full derivation here** — this is exactly the
"short, bounded comparison" the plan scoped it as, not a new item.

---

## 4. Sudoku Scorecard — 13/13 PASS

| # | Check | Computed | Expected | Result |
|---|-------|----------|----------|--------|
| S1 | Filed wording ("ψ alone shifts") is NOT a symmetry | nonzero residual | nonzero | PASS |
| S2 | Combined shift IS the exact global symmetry | residual 0 | 0 | PASS |
| S3 | Noether current conserved on-shell | residual 0 | 0 | PASS |
| S4 | Coupling term alone already locally invariant (no A needed) | residual 0 | 0 | PASS |
| S5 | Bare kinetic term alone NOT invariant without A | nonzero residual | nonzero | PASS |
| S6 | Full gauged Lagrangian exactly locally invariant | residual 0 | 0 | PASS |
| S7 | Σ/θ kinetic diagonalization exact | residual 0 | 0 | PASS |
| S8 | A does not appear in θ (coupling) sector | False | False | PASS |
| S9 | A has no independent kinetic term | confirmed | confirmed | PASS |
| S10 | Solving out A's constraint reproduces original θ EOM exactly (2 independent routes agree) | residual 0 | 0 | PASS |
| S11 | Postulated F₀₁ gauge invariant, healthy sign | (0, 0) | (0, 0) | PASS |
| S12 | N=2: A-dependent piece depends only on Σ₃, not θ₁/θ₂ | (False, False) | (False, False) | PASS |
| S13 | Two-phase Lagrangian (Part 61) compatibility | residual 0 | 0 | PASS |

**SM compatibility (CLAUDE.md Sudoku item 3) — N/A, and stated as such,
not skipped:** a direct consequence of S9/S10 is that minimal coupling
alone produces *no propagating field* — there is no physical degree of
freedom yet to check against the Standard Model photon's charge, mass,
or gauge-boson phenomenology. This check becomes applicable only if a
kinetic term is separately postulated (Section 3.6) and `A` is not
integrated out — i.e. it is deferred, not avoided, pending that further
postulate.

**Two-phase Lagrangian compatibility (item 4):** S13, Section 3.8.

No bugs were caught during this Part's RECHECK pass — every function's
first run matched its hand-derived expectation exactly (residuals of 0
where predicted, nonzero where predicted). This is recorded here plainly
per the project's own standard for honest reporting (compare T81/Part
146, where two real bugs *were* caught and are documented as such) —
absence of a bug is not evidence of insufficient scrutiny; each of the
13 checks reads a genuinely computed value, not a hardcoded literal.

---

## 5. Verdict and Status

**TODO_04.md T80 — RESOLVED: real construction succeeds structurally;
minimal coupling alone is physically vacuous for PDTP.**

1. **(147.1) [DERIVED, correction]** T80's own filed wording for Key
   Question 1 was imprecise — "ψ alone shifts" is not a symmetry. The
   actual symmetry is the combined shift of every field together.
2. **(147.2–147.3) [DERIVED] Key Question 1 (corrected): YES.** Gauging
   the combined shift forces a real new field `A` into existence, with
   exactly the QED-like transformation law, and the full Lagrangian is
   exactly locally invariant. The coupling term `g·cos(ψ−φ)` needs no
   modification at all — a clean structural fact specific to PDTP (its
   coupling already depends only on a gauge-invariant combination).
3. **(147.4–147.6) [DERIVED] Key Question 2: precisely NO, for the
   reason that matters.** Minimal coupling gives `A` no kinetic term, so
   it is a non-dynamical constraint, not a propagating field. Solving it
   out reproduces PDTP's *original*, ungauged dynamics exactly — the
   construction is real but carries zero net physical content on its
   own. This is a sharp, quantitative negative, not a vague one.
4. **(147.7) [VERIFIED] If a kinetic term is postulated separately** (a
   further, PDTP-external assumption, on the same footing as Maxwell's
   own historical scaffolding), it is well-formed (gauge invariant,
   healthy sign) — but nothing in PDTP's own structure currently
   supplies or motivates it.
5. **(147.8, Section 3.7–3.8) [DERIVED]** The result generalizes cleanly
   to the full multi-matter-phase case and is compatible with the
   two-phase Lagrangian's symmetry structure.
6. **(Section 3.9) Key Question 3: the Kaluza-Klein route is not an
   escape** — it inherits the same missing-kinetic-term problem, since
   PDTP has no independent curvature dynamics of the kind KK's own
   construction draws the kinetic term from.

**Key Question 4 — impact on T79 Item 2 and `polarization_analogy.md`
§3.5:** both verdicts should be **sharpened, not overturned**. T79 Item
2 currently states gauge fields are "entirely UNBUILT in PDTP." This
Part shows the *formal* obstruction (no local-symmetry route available
at all) was already the wrong way to state the gap — a local-symmetry
route **does** exist and **does** force a connection field to exist. The
real, sharper gap is: **PDTP has no mechanism, of any kind, that
generates an independent kinetic term for a gauge field** — not "PDTP
has no route to a connection field" but "PDTP's route to a connection
field produces one with nothing to propagate it." `polarization_analogy.md`
§3.5/§8.2's open item ("can the lattice provide local U(1) gauge
symmetry?") is answered: yes, PDTP's *existing* matter-spacetime coupling
already admits an exact local U(1) gauging without needing the lattice's
torsion/rotation modes at all (T66's route) — but this elevates the
analogy only partway "from metaphor to mathematical equivalence," since
the resulting field is inert. **Edits applied as part of this Part's own
TODO_04.md sync:** T79 Item 2's wording has been updated to reflect this
sharper diagnosis; cross-reference notes have been added to
`polarization_analogy.md` §3.5 and §8.2 Item 2.

**Plain English summary:** PDTP's gravity-matter coupling turns out to
have exactly the right hidden symmetry to support the same "add a
connection field" trick that gives ordinary physics electromagnetism —
and demanding that symmetry hold locally really does force a new field
into existence, transforming exactly the way a real gauge field should.
That is a genuine, clean, useful structural result. But the trick alone
doesn't get you a working electromagnetism: the new field has no "spring"
of its own (no kinetic term) making it want to ripple outward, so instead
of becoming a propagating force-carrier, it collapses into a bookkeeping
device — instantly fixed by whatever the matter fields are doing, and
when you follow through the math, it makes no difference whatsoever to
any prediction PDTP already made. Real electromagnetism's `-¼F²` term —
the part that makes light waves possible — has to be added as a separate
ingredient; nothing here forces it to appear on its own. **Either outcome
promised at filing time was said to be valuable, and this is the outcome
that landed:** not a working EM sector (which would have been a major
milestone), but a long-standing open question converted into a precise,
well-understood, and — importantly — *correctly located* negative: the
gap isn't "PDTP can't be gauged," it's "PDTP's gauge field has nothing to
make it move."

**What remains open:** whether some PDTP-intrinsic mechanism (e.g. a
Sakharov-style induced kinetic term from integrating out matter degrees
of freedom, paralleling Part 114's induced-gravity playbook) could supply
the missing kinetic term without an external postulate. Flagged as a
natural, well-scoped possible follow-up, not attempted here (per the
plan's own scoping, Phase 3's explicit note) and not filed as a new
TODO_04.md item at this time.

---

## 6. Sources

- **Source:** YouTube video "Electromagnetism Derived From Geometry!"
  (transcript in `docs/misc/note 2026-09-14.txt`) — standard textbook
  U(1) gauge-theory derivation of Maxwell's equations; not itself a new
  or contested claim.
- **Source:** Kaluza, T. (1921), "Zum Unitätsproblem der Physik,"
  *Sitzungsberichte der Preußischen Akademie der Wissenschaften* —
  original 5D compactification construction (Section 3.9).
- **Historical parallel:** Maxwell's displacement current, Methodology.md
  — cited directly for Section 3.6's characterization of a postulated
  kinetic term as scaffolding, not a forced consequence.
- **Reused, not re-derived:** `polarization_analogy.md` §3.5/§8.2 (the
  standing open item this Part addresses); T66/Part 136 (closed
  torsion/rotation route — not conflated with this Part's direct route);
  T70/Part 140 (NLSM-scalar classification); T75/Part 143 (TeVeS
  comparison, vector-field absence, and the disformal-vector analogy in
  Section 3.5); Part 61 (two-phase Lagrangian, Section 3.8); Parts 75-76,
  114 (SU(3) emergent metric + Sakharov induced gravity, Section 3.9).
- **PDTP Originals in this document:** Eq. 147.1 (corrected symmetry
  identification), Eq. 147.2 (Noether current), Eq. 147.3 (gauging
  construction), Eq. 147.4 (Σ/θ diagonalization), Eq. 147.5–147.6 (the
  non-dynamical-constraint finding and its zero-net-effect consequence),
  Eq. 147.7 (postulated-kinetic-term sign check), Eq. 147.8 (N=2
  generalization).

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*

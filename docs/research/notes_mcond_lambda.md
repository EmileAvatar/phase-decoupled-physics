# Notes — The Two Free Parameters: m_cond and Lambda

**Status:** DISCUSSION NOTES — no new derivations in this document. This records
a session discussion (2026-06-11, after Parts 116-118) summarising the status of
the framework's two free parameters and two proposed future directions (T46, T47).
All cited results live in their original Parts; everything new here is tagged
[SPECULATIVE] and is untested.
**Prerequisites:** Parts 29-35 (circularity), Part 54 (Lambda FCC), Part 87
(Lambda reframe), Part 115 (no-go theorem), Part 116 (DM selection), Part 117
(induced quartic).

---

## HANDOFF SUMMARY — Read this first to get up to speed

This is a speculative physics project called **PDTP (Phase-Decoupled Transport
Physics)**. The core idea: gravity is not a fundamental force — it is emergent
phase-locking between matter-waves and spacetime-waves, like two tuning forks
pulling each other into sync. The medium is a quantum condensate (think: the
universe is a superfluid). The framework is Lagrangian-based (no hand-waving),
every result is SymPy-verified and Sudoku-tested, and nothing is accepted
without showing full working. The CLAUDE.md in the repo root is the project
bible — read it before doing anything.

### The Lagrangian (two-phase form, current)

```
L = +g cos(psi - phi_b) - g cos(psi - phi_s)
```

- `psi` = matter-wave phase field
- `phi_b` = bulk (gravity) condensate phase
- `phi_s` = surface condensate phase
- Change of variables: `phi_+ = (phi_b+phi_s)/2` (gravity mode),
  `phi_- = (phi_b-phi_s)/2` (surface / dark-energy mode)
- Product identity: `cos(psi-phi_b) - cos(psi-phi_s) = 2 sin(psi-phi_+) sin(phi_-)`
- Newton's 3rd law DERIVED: `psi_ddot = -2 phi_+_ddot` [Part 61]
- All 16 single-phase results reproduced in two-phase framework [Part 63, 16/16 PASS]

### The three most recent breakthroughs (Parts 116-118, 2026-06-11)

**Part 116 — Dark matter mass is no longer a free parameter.**
DM = a vortex in the condensate. Vortex energy scales as n^2 (SymPy verified),
so any n >= 2 vortex spontaneously splits into n=1 pieces (stability). A
2M-sample Monte Carlo of the Kibble-Zurek birth mechanism independently gives
|n|=1 at 96%. Therefore n=1 and m_DM = m_P (Planck mass). Sudoku: 12/12.
Honest catch: KZ abundance is 50 orders of magnitude too low — needs
post-inflation production channel. Kill test: CMB tensor modes (LiteBIRD/
CMB-S4). No tensor signal = this candidate is dead.
Script: `simulations/solver/dm_winding_selection.py`
Doc: `docs/research/dm_winding_selection.md`

**Part 117 — Missing early-dark-energy stiffening term found inside existing Lagrangian.**
The two-phase Lagrangian at partial lock (beta != 0, matter and spacetime still
syncing) generates a positive quartic for phi_- via back-reaction of phi_+:
  `lambda_4 = 2g^2 sin^2(beta) / (3 kbar^2) > 0`  [PDTP Original, SymPy verified]
This is the transient Early Dark Energy term needed for Hubble tension. It
self-switches off as locking completes (beta -> 0 today), giving w=-1 automatically.
No new fundamental term needed — it falls out of the same Lagrangian. Sudoku: 10/10.
Script: `simulations/solver/phi_minus_quartic.py`
Doc: `docs/research/phi_minus_quartic.md`

**Part 118 — Eq 89.17 corrected (three simultaneous errors).**
The DM self-interaction formula sigma/m ~ G/c^4 was dimensionally wrong (SymPy
units check), numerically off by x100, and its cm^2/g conversion was off by x1000.
Correct formula (gravitational Rutherford scattering):
  `sigma/m = 4*pi*G^2*m_DM/v^4 = 5.2e-49 m^2/kg`
Bullet Cluster margin actually improves (39 -> 44 orders of magnitude). Sudoku: 7/7.
Script: `simulations/solver/sigma_m_erratum.py`

### Two open tasks (T46, T47 in TODO_04.md)

**T46 (HIGH PRIORITY) — Lambda as a locking fossil [SPECULATIVE]**
Today's cosmological constant Lambda = g * phi_-_vac^2 (Part 87 reframe).
Question: is phi_-_vac today simply the residue of the Part 117 roll that
froze via Hubble friction before finishing? If yes, one function beta(z) would
simultaneously predict Early Dark Energy, today's Lambda, and the DESI w(z)
evolution. Must plan first (Problem-Solving Protocol) before any math.

**T47 — m_cond consequence scanner**
m_cond (the "grain mass" of spacetime) is the framework's one free parameter
that cannot be derived internally (Part 115 no-go theorem — algebraically proven).
But we CAN scan candidate values from ~1 eV to m_P and tabulate what each predicts:
omega_gap, G_pred, condensate density, healing length, DM mass, JPD signal size, etc.
User added pseudocode below (Section 2). This is a lookup table for experimentalists,
NOT a finder — the no-go theorem closes the finder approach permanently.

### Key negative results (know these before proposing solutions)

- G cannot be derived internally — any algebraic chain is circular (Parts 29-35,
  algebraically proven, 729-combination scan, Part 115 scale-invariance no-go theorem)
- Lambda is also a free parameter — every internal route tried failed (Part 54 FCC)
- Dimensional transmutation (the QCD trick) fails: PDTP coupling runs the WRONG WAY
  (Part 35); no Landau pole anywhere near Planck scale
- Kibble-Zurek abundance for m_DM = m_P: 50 OoM too low (Part 116, NEGATIVE)
- Quark string tension: SC formula gives 0.173 GeV^2 (4% off QCD), sea quarks
  make it WORSE not better (Part 40, NEGATIVE for quark-correction route)

### Coding standards (enforced, non-negotiable)

- All .py files: ASCII only (no Unicode — Windows cp1252 crashes). Greek letters
  as words: alpha, beta, sigma, hbar, etc.
- Every returned value must be COMPUTED from arithmetic, not hardcoded
- Every PDTP Original result needs SymPy verification (or written reason why not)
- Sudoku consistency check: 10+ known equations, ratio within 1% = MATCH
- Save all script output to `simulations/solver/outputs/` with tee
- Functions: derive_*, verify_*, compute_* (separate concerns)
- check_equal() and check_sign() in sympy_checks.py return (bool, str) tuples
  — unpack as `ok, msg = check_equal(...)`, then use `rw.print(msg)`

### Where things live

- Active TODO: `TODO_04.md` (T43-T47 are the most recent)
- Completed summary: `TODO_Summary.md`
- All equations with status tags: `docs/research/equation_reference.md`
- Falsifiable predictions: `docs/research/falsifiable_predictions.md`
- Methodology checklist: `docs/Methodology.md`
- SymPy checks utility: `simulations/solver/sympy_checks.py`
- URL checker: `github-repo misc/check_urls.py`
  (run as: `python "github-repo misc/check_urls.py"` from project root)

---

---

## 1. m_cond — "how stiff is spacetime?"

### What it is

If spacetime is a condensate (a medium), it has a characteristic quantum — one
"grain" of spacetime-stuff with mass m_cond. Everything gravitational in PDTP
hangs off this single number through the bridge:

```
G = hbar*c / m_cond^2          [Part 33, DERIVED given m_cond]
omega_gap = m_cond*c^2/hbar    [breathing-mode gap = same question, Part 33]
```

Plugging in the observed G gives m_cond = m_P (Planck mass, ~22 micrograms) —
absurdly heavy for a "particle". That absurdity IS the hierarchy problem
restated: why is gravity so weak = why is the spacetime grain so heavy compared
to every known particle?

### The issue (why it is stuck)

A ~dozen-Part campaign (29, 30-35, 77, 78, 115) ended in a PROOF, not just a
failure. Part 115's scale-invariance no-go theorem: every internally
constructible PDTP observable scales as a pure power of m_cond. Change m_cond
and the whole picture rescales together — like zooming a photograph; nothing
inside the photo can tell you how big the photo is. Therefore NO internal
principle (energy minimisation, self-consistency, algebra) can select the
value. The quantum loophole (dimensional transmutation, the way QCD generates
its scale) is closed: the PDTP coupling runs the wrong way (Part 35).
Consolation prize: the bridge is exactly the Dvali-Gomez black-hole criticality
condition alpha_gr = 1 — each condensate quantum is marginally its own black
hole (Part 115), which explains why all the Part 77/78 bounds kept saturating.

### Resolution routes (honest list)

1. **Measure it** (the Cavendish move). The observable is omega_gap. Direct
   detection is hopeless (Planck frequency, ~43 orders above LISA). Live hope:
   an INDIRECT low-energy signature that depends on omega_gap — see the
   falsifiable predictions list and the JPD testbed concept.
2. **Go outside.** An independent theory (no G, no PDTP input) that predicts
   m_cond. The no-go theorem says the answer MUST come from outside.
3. **Accept it** as the framework's one measured constant — GR also takes G as
   input; PDTP would explain more structure from the same number of inputs.

### Can brute force find m_cond? (session question)

**No — and we can say precisely why.** A brute-force scan needs a SCORING
function. The only scorer PDTP can offer internally is the Sudoku engine, and
every one of its tests contains G (or a Planck quantity) as the reference —
so the scan trivially "finds" m_P, but only because G was the input. That is
the circularity proven algebraically in Phase 4 (729-combination scan, Part 30)
and then structurally in Part 115. There is no independent referee inside the
theory; brute force cannot manufacture one. [DERIVED — this is the no-go
theorem applied to scanning]

**What a scan CAN legitimately do:** invert the logic. Instead of scanning to
FIND m_cond, scan to TABULATE what every candidate m_cond would predict — a
lookup table for experimentalists: for each m_cond from (say) 1 eV to m_P, list
omega_gap, G_pred, condensate density, healing length, DM vortex mass, JPD-type
signal size, etc. Then every future measurement RULES OUT a band of the table.
This is the measurement route (#1) made systematic. Filed as **T47**.

---

## 2. If m_cond becomes known — the equation cascade

The point of measuring m_cond: one number unlocks a chain of NO-free-parameter
predictions, each independently checkable. (All relations already derived in
the cited Parts; this is the dependency map.)

### Immediate outputs (fall out of m_cond directly)

| Quantity | Relation | Part |
|----------|----------|------|
| Newton's G | G = hbar*c/m_cond^2 | 33 |
| Breathing-mode gap | omega_gap = m_cond*c^2/hbar | 33 |
| Lattice spacing | a_0 = hbar/(m_cond*c) | 33 |
| Winding number (any particle) | n = m_cond/m | 33 |
| Dark matter mass | m_DM = m_cond (n=1 vortex) | 116 |
| Condensate density | rho_cond ~ m_cond/a_0^3 | 21/34 |
| Healing length | xi = a_0/sqrt(2) | 34 |
| GP interaction constant | g_GP = hbar^3/(m_cond^2 c) | 34 |
| Biharmonic screening scale | L_heal ~ 1/(2g), g tied to omega_gap | 61/86 |
| GL parameter | kappa_GL = sqrt(2) (m_cond-independent — a CHECK, not output) | 36/37 |

User Notes: Turn above into a function and each line it self a function that returns one awnser. and we output to as a line on a table
```
loop through values: call calculate(m_cond)
calculate(m_cond) {
   (m_cond) conditon used
   Newtons(m_cond)
   BreathingMode(m_cond)
   LatticeSpacing(m_cond)
   WindingNumber(m_cond)
   DarkMaterMass(m_cond)
   Condenstate density(m_cond)
   Healing length(m_cond)
   Gp InteractionConstant(m_cond)
   BiharmonicScreeningScale(m_cond)
   GLParameter
   ouput all this and return as one line in a 
}
```

### Verification targets (known equations m_cond must reproduce)

This is exactly the Part 33 Sudoku suite — with a MEASURED m_cond it stops
being circular and becomes a genuine test battery:

Planck length/mass/time/energy/temperature, Schwarzschild radius, Hawking
temperature, gravitational alpha_G, hierarchy ratio alpha_G/alpha_EM, Hubble
critical density, Earth surface gravity (13 tests, `vortex_winding.py`).
Score rule unchanged: ratio within 1% = MATCH; any contradiction must be
explained or the measurement interpretation is rejected.

**Falsification logic:** if omega_gap is measured and G_pred = hbar*c/m_cond^2
disagrees with Cavendish G by more than experimental error, the PDTP bridge is
DEAD. That is the cleanest possible kill shot for the whole framework — which
is why measuring omega_gap stays the #1 strategic goal.

---

## 3. Lambda — "why is empty space almost, but not exactly, nothing?"

### What it is

The cosmological constant: dark energy's strength, observed ~10^121 times
smaller than the naive vacuum-energy estimate (the worst prediction in
physics). PDTP's reframe (Part 87): Lambda = g*phi_-_vac^2 — Lambda measures
the residual background "tilt" of the surface mode, phi_-_vac ~ 1e-70 rad.
So "why is Lambda tiny?" becomes "why is the universe locked ALMOST perfectly,
but not perfectly?"

### The issue

Part 54 (Forced Checklist Check): Lambda is a SECOND free parameter, exactly as
in GR. The suggestive numerology Lambda ~ (l_P/L_H)^2 has the right size, but
L_H (Hubble radius) is a cosmological input, not PDTP-internal — that trades
one input for another. The BEC depletion path failed (condensate not dilute).

### Resolution routes — including a NEW untested idea

1. **[SPECULATIVE — NEW, this session] Lambda as a locking relic.** Part 117
   showed that while locking was incomplete (beta != 0), phi_- was actively
   pushed away from zero; the push switches off as beta -> 0. Question: is
   today's phi_-_vac simply the LEFTOVER RESIDUE of that roll — the part that
   had not finished relaxing (Hubble friction freezes rolling fields) when the
   driving force vanished? If yes, Lambda stops being a free constant and
   becomes a FOSSIL OF COSMIC HISTORY, computable from the locking history
   beta(z) + Hubble friction. One unexplained function beta(z) would then set
   THREE observables at once: early dark energy (Part 117), today's Lambda,
   and the DESI w(z) evolution — three falsifiable outputs from one input.
   Filed as **T46** (plan-first per Problem-Solving Protocol).
2. **Holographic/CKN route:** tie Lambda to the horizon scale and explain why
   that is not circular (Part 54 partial).
3. **Accept** as second measured constant (the proven-analog position).

### The shape of the whole problem

m_cond is PROVABLY external (theorem); Lambda is EMPIRICALLY stuck at external
(every internal path tried failed). One sets the medium's smallest scale, the
other its faintest residual tension; their ratio spans the famous ~10^122.
PDTP has compressed physics' two worst fine-tuning embarrassments into: "we do
not know the grain size or the leftover tension of the medium." Everything in
between, it derives.

---

## 4. Appendix — GR vs quantum field theory (session question, plain English)

**Why they conflict (mainstream statement):** GR treats spacetime as a smooth,
deterministic geometry that bends; QFT (incl. QED) treats everything as
quantized fields with probabilistic fluctuations living ON a fixed spacetime.
Try to quantize gravity like the other forces and the theory is
non-renormalizable — infinitely many infinities; try to feed quantum
uncertainty into GR and the smooth geometry has no way to represent a
superposition of shapes. Each theory is near-perfect in its own domain; they
collide where both matter at once (black hole interiors, the Big Bang).

**Mainstream attempts:** string theory (everything is strings, graviton
included), loop quantum gravity (quantize geometry itself), asymptotic safety
(gravity becomes well-behaved at high energy), emergent gravity (gravity is
not fundamental).

**PDTP's position [SPECULATIVE]:** the conflict dissolves because it was a
category error. Gravity is not a fundamental force to be quantized — it is the
collective, long-wavelength behaviour of an already-quantum medium, the way
sound is the collective behaviour of molecules. You do not "reconcile" sound
waves with molecular physics by quantizing sound harder; you recognise sound
as emergent. In PDTP: the condensate is quantum from the start (its quanta
have mass m_cond); GR is its hydrodynamic limit (recovered in Parts 73-76,
86); the "graviton problem" never arises because the graviton is a phonon-like
collective mode, not a fundamental particle, and phonon theories are not
required to be renormalizable — they come with a physical cutoff (a_0 = the
lattice spacing) built in. The price of this elegance is the open question
above: the cutoff scale IS m_cond, and we cannot derive it. Sakharov (1967)
"induced gravity" is the historical ancestor of this position.

---

## References (all internal)

Parts 29-35 (circularity campaign), 54 (Lambda FCC), 73-76/86 (GR recovery),
87 (Lambda = g*phi_-_vac^2), 115 (no-go theorem + Dvali-Gomez criticality),
116 (DM winding selection), 117 (induced quartic / locking).
Sakharov (1967), "Vacuum quantum fluctuations in curved space and the theory
of gravitation", Dokl. Akad. Nauk SSSR 177, 70 (induced/emergent gravity).

*Follow-ups filed: T46 (Lambda as locking relic), T47 (m_cond consequence
scanner). See TODO_04.md.*

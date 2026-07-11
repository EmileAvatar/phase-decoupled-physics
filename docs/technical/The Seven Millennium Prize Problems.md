# The Seven Millennium Prize Problems

**Type:** General background reference (not PDTP-specific research).
**Source:** Clay Mathematics Institute, problems listed 2000 (each carries a $1,000,000 prize).
**Purpose:** Background reference for this project. Compiled 2026-07-11 after reviewing an
external paper (Klingman, *"The Origin of Quarks in Quantum Gravity,"* JMP 2024) that
misappropriated the name of one of these problems (Yang-Mills mass gap) to lend unearned
credibility to an unrelated derivation. Kept here so future sessions can quickly check
whether a claim invoking one of these problems is using the term correctly.
**Companion doc:** see `TODO_05.md` Group D for PDTP-specific follow-up items on the
problems below that have any real (even if indirect) connection to this project.

---

## 1. P vs NP — posed 1971 (Stephen Cook; independently Leonid Levin, 1973)

**a. Broad description:** Asks whether every problem whose solution can be *verified*
quickly by a computer (in polynomial time) can also be *found/solved* quickly. Formally:
does the complexity class P equal the class NP?

**b. Simplified:** If checking someone's answer is easy, is finding that answer *also*
always easy? Most think no — but nobody can prove it.

**c. Type:** Pure mathematics / theoretical computer science.

**d. Possible solution paths:** Diagonalization, circuit complexity lower bounds, or
proving fundamental barriers (like the already-found "natural proofs" and "relativization"
obstructions) that explain *why* current techniques can't settle it — several major proof
strategies have been shown to be structurally incapable of resolving it, which is itself
progress.

**e. PDTP relevance:** None. No connection — computational complexity theory and PDTP's
physics have nothing in common.

---

## 2. Hodge Conjecture — posed 1950 (William Hodge, ICM address)

**a. Broad description:** In algebraic geometry, asks whether certain topological classes
("Hodge classes") on smooth complex projective varieties can always be represented by
algebraic cycles — i.e., whether purely topological data is secretly always algebraic.

**b. Simplified:** For a certain class of geometric shapes, can every "topological pattern"
always be built out of honest algebraic equations, or are some patterns topological-only,
with no algebraic origin?

**c. Type:** Pure mathematics (algebraic geometry / complex geometry).

**d. Possible solution paths:** Deeper development of Hodge theory, motives, and the
theory of algebraic cycles; no consensus approach — considered one of the most opaque of
the seven even to working mathematicians outside the subfield.

**e. PDTP relevance:** None. No overlap with PDTP's condensate/phase-locking framework.

---

## 3. Riemann Hypothesis — posed 1859 (Bernhard Riemann)

**a. Broad description:** Conjectures that all "nontrivial" zeros of the Riemann zeta
function ζ(s) have real part exactly 1/2. This would pin down the distribution of prime
numbers with extraordinary precision.

**b. Simplified:** There's a mathematical function whose zeros encode how prime numbers
are spread out. This says all the interesting zeros line up perfectly on one specific
line — nobody can prove they all do, though billions have been checked and none deviate.

**c. Type:** Pure mathematics (number theory / complex analysis) — though it has real
physics-adjacent tendrils (see below).

**d. Possible solution paths:** The Hilbert-Pólya conjecture — that the zeros are
eigenvalues of some yet-unknown Hermitian (quantum mechanical) operator — is the most
physics-flavored hope; random matrix theory has found statistical zero-spacing matches to
quantum chaotic systems, but no operator has been found.

**e. PDTP relevance:** Indirect, and explicitly flagged in this project as unexplored.
TODO_03.md Category H (Riemann Zeta) has items H1-H4, all tagged SPECULATION with no
calculation started — plus a Riemann Hypothesis screenshot folder in `assets/images/`.
A real but dormant thread, not a result. See TODO_05.md Group D, T61.

---

## 4. Yang-Mills Existence and Mass Gap — theory 1954 (Yang & Mills); rigorous problem
crystallized 1960s-70s (constructive QFT program), formalized as a Millennium Problem 2000
(Jaffe & Witten)

**a. Broad description:** Demands a mathematically rigorous construction of quantum
Yang-Mills theory in 4D (satisfying the Wightman/Osterwalder-Schrader axioms of QFT) *and*
a proof that it has a mass gap — that the lightest excitation above the vacuum has strictly
positive mass.

**b. Simplified:** Physicists use Yang-Mills theory (the math behind the strong and weak
nuclear forces) constantly and it works — but nobody has proven, with full mathematical
rigor, that the theory is even logically well-defined, or that it necessarily produces
massive particles the way experiments show.

**c. Type:** Mathematical physics — straddles physics and pure math; this is the one most
often misused by fringe papers claiming casual "mass gap" derivations.

**d. Possible solution paths:** Constructive QFT (rigorously building the theory from the
lattice up and taking a continuum limit with control over all approximations), or lattice
gauge theory combined with renormalization group techniques that can be made fully
rigorous — decades of numerical lattice QCD evidence strongly *suggests* the mass gap
exists, but numerical evidence isn't proof.

**e. PDTP relevance:** Indirect — methodological overlap, not a claim to solve it. PDTP's
SU(3) extension (Parts 37-41) runs actual lattice gauge theory calculations (Wilson
action, Monte Carlo, string tension) — the same *kind* of machinery used to numerically
probe Yang-Mills confinement. PDTP also has its own internal "mass gap" results (e.g.
m² = 2g for the φ₋ mode, ω_gap terminology throughout) — but these are gaps in PDTP's own
emergent effective field theory, not a resolution of the axiomatic Millennium Problem. This
distinction must stay explicit — see TODO_05.md Group D, T62.

---

## 5. Navier-Stokes Existence and Smoothness — equations 1822/1845 (Navier, Stokes); open
problem framed by Jean Leray's 1934 work on weak solutions

**a. Broad description:** Asks whether solutions to the 3D Navier-Stokes equations
(governing viscous fluid flow) always exist for all time and remain smooth, or whether
they can blow up (develop a singularity) in finite time from smooth initial data.

**b. Simplified:** We have the equations that describe how fluids like water and air move.
Do they always behave — stay smooth and well-defined forever — or could a fluid
theoretically "tear itself apart" mathematically, even though that's never observed
physically?

**c. Type:** Applied mathematics / mathematical physics (PDE theory).

**d. Possible solution paths:** Either prove global regularity via new energy
estimates/scaling arguments, or construct an explicit blow-up solution; partial results
exist (2D is solved, weak solutions exist in 3D via Leray, but uniqueness/smoothness is
open).

**e. PDTP relevance:** Indirect at most. PDTP treats the spacetime condensate as a
superfluid (Gross-Pitaevskii-style), and fluid-dynamics language shows up in interpretive
sections (wave effects catalog, condensate compression), but the project doesn't engage
the classical Navier-Stokes existence/smoothness problem itself — different equations,
different regime. See TODO_05.md Group D, T63.

---

## 6. Birch and Swinnerton-Dyer Conjecture — posed ~1965 (Bryan Birch & Peter
Swinnerton-Dyer, based on early-1960s computations)

**a. Broad description:** Relates the rank of the group of rational points on an elliptic
curve to the order of vanishing of an associated L-function at s = 1 — connecting an
algebraic/arithmetic property to an analytic one.

**b. Simplified:** For a certain family of curves used heavily in number theory (and
cryptography), this predicts how many "rational solutions" a curve has, based on behavior
of a related function — checked extensively by computer for small cases, unproven in
general.

**c. Type:** Pure mathematics (number theory / arithmetic geometry).

**d. Possible solution paths:** Deeper Iwasawa theory, modularity techniques (in the
tradition of the methods used to prove Fermat's Last Theorem), or new results on Selmer
groups.

**e. PDTP relevance:** None. No connection.

---

## 7. Poincaré Conjecture — posed 1904 (Henri Poincaré) — **SOLVED 2002-2003**

**a. Broad description:** States that every simply connected, closed 3-dimensional
manifold is topologically equivalent (homeomorphic) to the 3-sphere S³ — i.e., the
simplest possible "shape without holes" in 3D is unique.

**b. Simplified:** If a 3D shape has no holes and is finite/self-contained, it has to
secretly be a (distorted) sphere — no exotic alternatives exist. Poincaré asked if this
was actually always true.

**c. Type:** Pure mathematics (geometric topology / geometric analysis).

**d. How it was actually solved:** Grigori Perelman proved it using Richard Hamilton's
Ricci flow program — an equation (∂g/∂t = −2·Ric(g)) that evolves a manifold's geometry
over "time" the way heat diffusion smooths temperature, tending to round the shape out.
Hamilton's approach stalled because the flow can develop singularities (the manifold
"pinches" in finite time). Perelman's breakthrough, in three dense papers posted
2002-2003, introduced a new monotonic entropy-like functional that let him control the
geometry near these pinch points, and developed "Ricci flow with surgery" — a procedure to
cut out singular regions, cap them, and continue the flow. This showed the manifold always
decomposes into standard pieces, proving both the Poincaré Conjecture and the more general
Geometrization Conjecture. Several teams (Cao-Zhu, Kleiner-Lott, Morgan-Tian) spent years
independently verifying and expanding his terse proofs. Perelman was awarded the Fields
Medal (2006) and the $1M Clay Prize (2010) — and turned down both.

**e. PDTP relevance:** Indirect — shared topological toolkit, not the theorem itself.
PDTP's topology work (vortex windings, Hopf-link vs. Y-junction baryon comparison in
Part 106, Z₃ defects) draws on the same general geometric-topology vocabulary (homotopy,
winding/linking numbers, manifold classification) as the Poincaré Conjecture, but doesn't
engage the specific 3-manifold classification question it resolves. See TODO_05.md
Group D, T64 for whether Perelman's actual TOOL (Ricci flow / geometric flow with
surgery) — as opposed to the theorem itself — could be useful methodology for PDTP's own
topological-defect stability questions.

---

## Summary Table

| # | Problem | Posed | Type | Status | PDTP relevance |
|---|---------|-------|------|--------|-----------------|
| 1 | P vs NP | 1971 | CS / math | Open | None |
| 2 | Hodge Conjecture | 1950 | Algebraic geometry | Open | None |
| 3 | Riemann Hypothesis | 1859 | Number theory | Open | Indirect (dormant, TODO_03 Cat. H) |
| 4 | Yang-Mills Mass Gap | 1954/2000 | Math physics | Open | Indirect (lattice SU(3) overlap) |
| 5 | Navier-Stokes | 1822-45/1934 | PDE / fluid dynamics | Open | Indirect (superfluid analogy) |
| 6 | Birch–Swinnerton-Dyer | 1965 | Number theory | Open | None |
| 7 | Poincaré Conjecture | 1904 | Topology | **Solved 2002-03** | Indirect (shared topology toolkit) |

---

*Compiled 2026-07-11. Not a PDTP research document — no Sudoku checks or SymPy
verification apply here; this is external reference material.*

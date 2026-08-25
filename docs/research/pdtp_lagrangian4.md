# L_4 — The Inter-Layer Lagrangian

**Date:** 2026-04-06
**Status:** [PARTIALLY VERIFIED — Parts 132-133, 2026-08-09] — Field
equations, conservation law, mass matrix, and Goldstone mode identity now
SymPy-verified (Sudoku 15/18 + 11/11 PASS; the 3 expected fails in Part 132
document a genuine sign error found and corrected in the original Field
Equations section, see Sec "SymPy Verification Results"). The b-quark "4%
match" and the product coupling rule remain **[SPECULATIVE]** — Part 132's
re-examination found the match is substantially weaker evidence than
originally presented.
**Builds on:** L_1 (U(1) single-phase), L_2 (two-phase), L_3 (SU(3))
**Motivation:** Make the off-diagonal blocks of P^{ab}_μν nonzero.
  Connect the three condensate layers (C1 gravity, C2 QCD, C3 EW).

---

## Plain English First

The three previous Lagrangians each describe ONE condensate layer in isolation.
Matter (ψ) couples to each layer, but the layers don't talk to each other.
L_4 adds a direct coupling between condensates — like adding springs between
three pendulums that were previously only connected through a common wall.

When two condensates couple, they create a NEW shared oscillation mode —
a relative-phase wave that lives BETWEEN the layers. The mass of that mode
is set by the coupling strength J_{ab}.

The key question: what is the natural value of J_{ab}?
Adopting the product rule J_{ab} = g_a × g_b / 2 (explained below),
the C2-C3 relative mode has mass = sqrt(g_QCD × g_W) = 4.01 GeV.
The b quark mass is 4.18 GeV. **4% match.** [SPECULATIVE]

---

## The Three Previous Lagrangians

```
L_1 = (1/2)(d phi)^2 + (1/2)(d psi)^2 + g cos(psi - phi)
      [single condensate phi; one coupling g]

L_2 = (1/2)(d phi_b)^2 + (1/2)(d phi_s)^2 + (1/2)(d psi)^2
    + g cos(psi - phi_b) - g cos(psi - phi_s)
      [two condensate modes phi_+/-; gravity + surface]

L_3 = K Tr[(d U_dag)(d U)] + Sum_i K_i Tr[(d Psi_i_dag)(d Psi_i)]
    + Sum_i g_i Re[Tr(Psi_i_dag U)] / 3
      [SU(3) matrix fields; 8 gluons; Z3 vortices]
```

All three have independent condensates. Matter ψ couples to each, but
φ₁, φ₂, φ₃ do not directly drive each other.

---

## L_4 — The Inter-Layer Lagrangian [PDTP Original, SPECULATIVE]

### Step 1: Three condensates + matter

Start with three independent scalar condensates, one per layer:

```
L_kinetic = (1/2)(d phi_1)^2 + (1/2)(d phi_2)^2 + (1/2)(d phi_3)^2 + (1/2)(d psi)^2

            phi_1 = gravitational condensate (C1, scale = m_P)
            phi_2 = QCD condensate           (C2, scale = Lambda_QCD)
            phi_3 = EW condensate            (C3, scale = m_W)
            psi   = matter field
```

### Step 2: Matter couples to all three

```
L_self = g_1 cos(psi - phi_1) + g_2 cos(psi - phi_2) + g_3 cos(psi - phi_3)

            g_1 = omega_P   = 1.855e43 rad/s  [Planck coupling]
            g_2 = omega_QCD = 3.039e23 rad/s  [QCD coupling ~ Lambda_QCD/hbar]
            g_3 = omega_W   = 1.221e26 rad/s  [EW coupling ~ m_W c^2/hbar]
```

Each cos term says: matter wants to phase-lock to that condensate.
The coupling strength g_a sets how strongly.

### Step 3: Add inter-layer coupling [THE NEW TERM]

```
L_cross = J_12 cos(phi_1 - phi_2)
        + J_13 cos(phi_1 - phi_3)
        + J_23 cos(phi_2 - phi_3)
```

Each J_{ab} cos(φ_a − φ_b) says: condensate a wants to phase-lock to condensate b.
This is structurally identical to L_self, but between condensates instead of matter+condensate.

### Full L_4

```
L_4 = (1/2)(d phi_1)^2 + (1/2)(d phi_2)^2 + (1/2)(d phi_3)^2 + (1/2)(d psi)^2

    + g_1 cos(psi - phi_1)     [matter-C1 coupling, gravity]
    + g_2 cos(psi - phi_2)     [matter-C2 coupling, QCD]
    + g_3 cos(psi - phi_3)     [matter-C3 coupling, EW]

    + J_12 cos(phi_1 - phi_2)  [C1-C2 inter-layer coupling]   NEW
    + J_13 cos(phi_1 - phi_3)  [C1-C3 inter-layer coupling]   NEW
    + J_23 cos(phi_2 - phi_3)  [C2-C3 inter-layer coupling]   NEW
                                                         [PDTP Original]
```

---

## Field Equations from L_4

Euler-Lagrange for each field (d_mu d^mu = Box):

```
Box phi_1 = g_1 sin(psi-phi_1) - J_12 sin(phi_1-phi_2) - J_13 sin(phi_1-phi_3)  ...(FE1)
Box phi_2 = g_2 sin(psi-phi_2) + J_12 sin(phi_1-phi_2) - J_23 sin(phi_2-phi_3)  ...(FE2)
Box phi_3 = g_3 sin(psi-phi_3) + J_13 sin(phi_1-phi_3) + J_23 sin(phi_2-phi_3)  ...(FE3)
Box psi   = -g_1 sin(psi-phi_1) - g_2 sin(psi-phi_2)   - g_3 sin(psi-phi_3)     ...(FE4)
```

**[CORRECTED, Part 132, 2026-08-09]:** the J-coupling terms in FE1-FE3 above
had the OPPOSITE sign in the original version of this document. Direct
SymPy differentiation of L_4 (`lagrangian4.py`, `derive_euler_lagrange()`)
found dL/dphi_1 = g_1 sin(psi-phi_1) **-** J_12 sin(phi_1-phi_2) **-**
J_13 sin(phi_1-phi_3), not the originally-stated + signs -- confirmed by
hand re-derivation (d/dphi_1[J_12 cos(phi_1-phi_2)] = -J_12 sin(phi_1-phi_2),
elementary chain rule) and cross-validated against FE4 (psi's equation),
which the original document DID get right and which SymPy reproduces
exactly, confirming the derivation method itself before trusting its verdict
on FE1-FE3. See Sec "SymPy Verification Results" below for the full check.

**Structure:** Each condensate is driven by matter AND by its two neighbours.
The sign pattern for J: phi_a LOSES from sin(phi_a - phi_b) (note the minus
sign on phi_a's own equation), phi_b GAINS from the same term in its own
equation (Box phi_2 has +J_12, Box phi_1 has -J_12) -- an action/reaction
pair between condensates, the same structure as Parts 61-63 proved for
φ_b and φ_s, but with the accounting corrected: it is phi_a that loses
energy to the phi_a-phi_b coupling (drags phi_a toward phi_b), not phi_a
that "gains."

---

## SymPy Verification Results (Part 132, T19, 2026-08-09)

**Script:** `simulations/solver/lagrangian4.py`. Log:
`simulations/solver/outputs/lagrangian4_run2.txt`. Sudoku 13/16 PASS (3
expected fails, documented below -- they ARE the finding, not an error in
the check).

### V1. Field equations [CORRECTED]

SymPy differentiation of L_4 directly (`derive_euler_lagrange()`, treating
each field as a function of a single time-like parameter, the project's
established convention for these ODE-level Euler-Lagrange checks) found the
J-coupling terms in the original FE1-FE3 had the wrong sign -- corrected
above. **Method validated first:** FE4 (psi's equation) matches the
original document exactly (residual = 0), so the derivation method itself
is trustworthy before its disagreement with FE1-FE3 is trusted. Hand
re-derivation confirms: d/dphi_1[J_12 cos(phi_1-phi_2)] = -J_12 sin(phi_1-phi_2)
by the elementary chain rule (d/dx cos(x) = -sin(x)), matching SymPy, not
matching the original document.

### V2. Conservation law -- stronger than originally claimed [DERIVED]

The original document claimed "FE1+FE2+FE3 = Box(phi_1+phi_2+phi_3)" as a
"Newton's 3rd law between condensates" result. As literally written this is
a tautology (FE_a is Box(phi_a) by definition) -- it asserts nothing.
SymPy checks the SUBSTANTIVE version instead: do the J_ab terms cancel when
FE1, FE2, FE3 are summed? **Yes** (verified, residual 0). More: **the FULL
four-field sum FE1+FE2+FE3+FE4 = 0 identically** (verified, residual 0) --
not stated anywhere in the original document. This is the REAL "Newton's
3rd law" content: it is the equation of motion for the exact Goldstone
direction (all four fields, phi_1,phi_2,phi_3,psi, shifting together),
following from L_4's overall U(1) symmetry (Noether's theorem, standard) --
a genuinely stronger and more complete result than what was originally
claimed.

### V3. Mass matrix -- confirmed correct, and generalized [VERIFIED + DERIVED]

Linearizing the CORRECTED FE1-FE3 (sin(x)~x, matter decoupled) and building
the Jacobian gives a 3x3 matrix that matches the document's originally-
stated mass matrix **exactly** (residual = zero matrix) -- so despite the
Field Equations section's sign error, the separately-derived Mass Matrix
section was already correct. Both the corrected sign flow (Part 1) and the
mass matrix (unchanged) are now on record as mutually consistent.

**New structural identification [PDTP Original, T19]:** the mass matrix is
exactly a **weighted graph Laplacian** -- M^2_aa = sum_{b!=a} J_ab (diagonal
= sum of edge weights touching node a), M^2_ab = -J_ab (off-diagonal =
negative edge weight), for a complete graph on the condensate layers with
edge weights J_ab. This is a standard object in graph theory (**Source:**
[Laplacian matrix](https://en.wikipedia.org/wiki/Laplacian_matrix)), and its
properties are well established: symmetric, positive semi-definite, the
all-ones vector is always in the kernel (row sums zero by construction), and
for a connected graph (true whenever all J_ab > 0) exactly one eigenvalue is
zero with all others strictly positive. This PROVES the document's claimed
properties 1-2 ("always has one zero eigenvalue," "remaining eigenvalues
positive if J_ab > 0") in general, for any number of condensate layers, not
just the specific 3x3 case -- verified with a spot-check on a random
weighted 4-node graph (`verify_graph_laplacian_general(n=4)`, Sudoku S10-S11).

### V4. Numeric eigenvalues -- recomputed, not copied [VERIFIED]

The document's Planck/QCD/EW couplings (g_1, g_2, g_3), stated in the Field
Equations section as angular frequencies (rad/s) but used in the Numerical
Predictions section directly as GeV energies, were checked explicitly: g_2 =
hbar*omega_QCD converts to 0.200 GeV, g_3 = hbar*omega_W converts to 80.37
GeV -- both matching the document's stated values to within 1% (Sudoku
S12-S13), confirming this is a legitimate (if implicit) unit conversion
between sections, not an error. The full 3x3 eigenvalue problem was
re-solved numerically (not copied from the document): smallest eigenvalue
zero to within floating-point precision relative to the matrix's own scale
(J13 ~ 5e20 GeV^2 dominates; an absolute tolerance is meaningless at this
dynamic range, so Sudoku S14 uses a tolerance relative to J13). The
isolated-pair limit (J_12, J_13 -> 0) of the full matrix reproduces
m_23 = sqrt(g_2 g_3) = 4.0095 GeV exactly (Sudoku S15) -- an internal
self-consistency check the original document did not perform (it quoted
Eq L4.1's formula and the full-matrix numbers separately, without checking
they agree in the appropriate limit).

---

## T^{μν} for L_4 — Now with Off-Diagonal Blocks

Applying T^{mu nu} = Sum_a (dL/d(d_mu phi_a)) d^nu phi_a - g^{mu nu} L_4:

```
T^{mu nu} = (d^mu phi_1)(d^nu phi_1)   [C1 self-kinetic]
          + (d^mu phi_2)(d^nu phi_2)   [C2 self-kinetic]
          + (d^mu phi_3)(d^nu phi_3)   [C3 self-kinetic]
          + (d^mu psi)(d^nu psi)       [matter kinetic]
          - g^{mu nu} L_4              [potential, includes J terms]
```

The J_{ab} cos(phi_a - phi_b) terms appear ONLY in the potential piece -g^{mu nu} L_4.
The kinetic piece remains diagonal (no kinetic mixing added in L_4).

**What the P^{ab} matrix looks like now:**

```
              C1                C2                C3
        ┌──────────────────────────────────────────────────────┐
C1      │ (d phi_1)^2          0                 0            │
        │ - g^{mu nu}(g1 cos   - g^{mu nu} J_12  - g^{mu nu} J_13 │
        │  (psi-phi1) + J_12   cos(phi1-phi2)    cos(phi1-phi3)│
        │  cos(phi1-phi2)                                      │
        │  + J_13 cos(...))                                    │
C2      │ (same)               (d phi_2)^2        0           │
        │                      - g^{mu nu}(...)  - g^{mu nu} J_23 │
        │                                         cos(phi2-phi3)│
C3      │ (same)               (same)            (d phi_3)^2  │
        │                                         - g^{mu nu} (...)│
        └──────────────────────────────────────────────────────┘
```

**In vacuum (static, uniform, all Delta_ab = 0):**

```
L_4(vacuum) = g_1 + g_2 + g_3 + J_12 + J_13 + J_23

T^{tt}(vacuum) = -(g_1 + g_2 + g_3 + J_12 + J_13 + J_23)   [total vacuum energy]
```

The J terms ADD to the cosmological constant.
If J_{ab} > 0: inter-layer coupling INCREASES the vacuum energy density.
This makes the cosmological constant problem WORSE in L_4 (not better).
[NEGATIVE result for cosmo constant, unless J < 0]

---

## Mass Matrix of New Modes

Linearise around the ground state (all phases equal: phi_1 = phi_2 = phi_3 = psi = 0).
Define relative phases: Phi_12 = phi_1 - phi_2, Phi_13 = phi_1 - phi_3.

From FE1 - FE2 (subtracting field equations):
```
Box Phi_12 = -2J_12 sin(Phi_12) - J_13 sin(Phi_13) + J_23 sin(Phi_12 - Phi_13)
           + (g_1 + g_2) sin(psi - phi_+)    [matter contribution, phi_+ = avg]
```

**[NOTE, Part 132]:** this intermediate line was not independently re-derived
or SymPy-checked (T19's verification worked directly from the corrected FE1-
FE3 to the mass matrix below, not through this specific combination step) --
it likely needs a matching sign correction given the FE1-FE3 fix above, but
since the FINAL 3x3 mass matrix below IS independently verified (Sudoku S7,
matches exactly), this unverified intermediate step does not affect any
accepted result. Flagged rather than silently left as if checked.

For the inter-condensate modes (ignore matter coupling for now):
Linearise sin(Phi) ~ Phi for small oscillations:

```
ddot Phi_12 = -2J_12 Phi_12 - (J_13 - J_23) Phi_13
ddot Phi_13 = -(J_12 - J_23) Phi_12 - 2J_13 Phi_13
```

Mass matrix M^2 for (Phi_12, Phi_13) — and equivalently for all three (phi_1, phi_2, phi_3):

```
Full 3x3 mass matrix (Laplacian structure):

M^2 = [ J_12+J_13    -J_12        -J_13    ]
      [ -J_12         J_12+J_23   -J_23    ]
      [ -J_13        -J_23         J_13+J_23]
```

**Properties of M^2:**
1. All row sums = 0 → always has one zero eigenvalue (Goldstone mode)
2. Remaining two eigenvalues are positive if J_{ab} > 0 (stable coupling)
3. Zero mode = overall phase shift phi_a → phi_a + c for all a (U(1) symmetry of L_4)

**Physical meaning of the Goldstone mode [T20, Part 133, 2026-08-09]:**
L_4 has a symmetry: shift ALL condensates simultaneously by the same angle.
phi_1 → phi_1 + c, phi_2 → phi_2 + c, phi_3 → phi_3 + c.
All cos(phi_a - phi_b) terms are invariant. This gives a massless mode.

**Script:** `simulations/solver/t20_goldstone_identification.py`. Log:
`simulations/solver/outputs/t20_goldstone_identification_run1.txt`. 11/11
Sudoku PASS.

**Plain English:** the Goldstone mode is not a new particle waiting to be
discovered so much as an ARBITRARY LABEL the theory never uses. Every
interaction in L_4 (gravity's pull on matter, QCD's pull on matter, the
inter-layer couplings) only cares about the DIFFERENCE between two phases,
never any phase's absolute value. That means there is always one direction
you can shift everything at once -- like renaming "zero" on a thermometer
-- that changes nothing anyone could ever measure. The math calls that
harmless freedom a "massless mode" because nothing pushes back against it
(no restoring force = no mass), but it is better understood as a bookkeeping
freedom than as a genuine new signal.

**T19's exact result extended:** T19 (Part 132) established FE1+FE2+FE3+FE4=0
identically -- ALL FOUR fields (phi_1, phi_2, phi_3, AND psi, not just the
three condensates) participate in the exact zero-eigenvalue direction. T20
makes this precise: define **chi = (phi_1+phi_2+phi_3+psi)/2**. Substituting
phi_a = chi + a_a (a_a = arbitrary, NOT small, "shape" offsets) into the
full potential shows **dV/dchi = 0 identically, for any field
configuration** (`verify_exact_potential_decoupling()`, Sudoku S5) -- a
non-perturbative statement, stronger than T19's linearized zero-eigenvalue
check, because every cos() argument in L_4 is a DIFFERENCE of two fields, so
the +chi shift cancels algebraically before any series expansion. chi's
kinetic term is also confirmed canonical with no mixing into the other three
independent ("shape") combinations (Sudoku S1-S4) -- so chi is a genuine,
independent, freely-propagating massless scalar degree of freedom, not a
constrained or redundant one.

**Is it the graviton? NO** (Sudoku S6-S7). This follows from representation
theory alone, not dynamics: the Goldstone theorem (**Source:** Weinberg,
*The Quantum Theory of Fields Vol. II* (1996) Sec 19.2) guarantees a
massless mode in the SAME Lorentz representation as the fields whose
symmetry is broken. phi_1, phi_2, phi_3, psi are all Lorentz scalars (spin-0),
so chi is necessarily spin-0. The graviton is the spin-2 excitation of the
metric tensor (in PDTP's own SU(3)-emergent-metric picture, Part 75, or in
standard GR). Spin-0 cannot equal spin-2 -- no further calculation changes
this.

**Is it Part 61's phi_-? NO, though the two are structurally related**
(Sudoku S8-S9, `compare_to_part61_phi_minus()`). Part 61's phi_- =
(phi_b-phi_s)/2 lives entirely within C1 (gravity), built from the bulk/
surface split of a SINGLE condensate. L_4's chi is built from FOUR fields
spanning THREE DIFFERENT condensate layers plus matter -- a strictly larger,
different field-space object, even in the special case where C1's phi_1 is
later identified with Part 61's phi_+. **The recurring pattern, not the
mode itself, is what's shared:** any Lagrangian built purely from
cos(DIFFERENCES) automatically has a "center of mass" zero mode for whatever
fields it couples. Part 61 instantiates this once, within C1's bulk/surface
split (giving phi_-); L_4 instantiates the SAME mechanism again, at a
different, higher level (across layers + matter, giving chi). Structurally
analogous, physically distinct.

**Is it eaten by a gauge field (Higgs mechanism)? Not applicable to L_4 as
written** (Sudoku S10-S11). The Higgs mechanism requires a LOCAL (gauged)
symmetry -- the shift parameter c promoted to c(x), with a covariant
derivative and gauge field A_mu (**Source:** Weinberg 1996 Sec 21.1). L_4's
phi_a -> phi_a+c uses a CONSTANT c (a global symmetry); there is no gauge
field anywhere in L_4's current definition for chi to be eaten by. Answering
"what gets mass" would require a distinct future extension (gauging this
specific U(1)), not something derivable from the Lagrangian as it stands.

**Summary verdict:** chi is a genuine, independent, exactly massless scalar
predicted by L_4 -- not the graviton, not Part 61's phi_-, and not
(currently) eaten by anything. Its potential-level decoupling from
everything else in L_4 means it does not mediate any force at the order L_4
currently specifies -- making it, if physically real, closer to a dark-
radiation-like relic than a fifth force. **[SPECULATIVE]** whether such a
mode would survive as an observable prediction (e.g. contributing to N_eff
in the CMB) is not derived here and would need its own follow-up; this
section answers T20's definitional question, not its full phenomenology.

---

## The Coupling Rule: Why J_{ab} = g_a × g_b / 2

To predict the mode masses, we need a rule for J_{ab}.

**Analogy: Lorentz-Berthelot rule** (van der Waals interactions)
In molecular physics, the cross-species interaction strength is:
```
epsilon_{AB} = sqrt(epsilon_{AA} × epsilon_{BB})   [geometric mean]
```

For PDTP, the natural analog using the PRODUCT of couplings:
```
J_{ab} = g_a × g_b / 2     [product coupling rule, PDTP Original, SPECULATIVE]
```

**Why the factor 1/2?**
The pendulum linearisation gives: omega^2 = 2J (from ddot(Phi) = -2J sin(Phi)).
To get mass^2 = g_a × g_b, we need 2J = g_a × g_b, i.e. J = g_a × g_b / 2.

**Result:**

```
J_{ab} = g_a * g_b / 2    =>    m_{ab} = sqrt(g_a * g_b)     [Eq L4.1, SPECULATIVE]
```

---

## Numerical Predictions from L_4 + Product Rule

### Isolated pair masses (ignoring full 3x3 mixing)

```
Pair       J_{ab} (GeV^2)      m_{ab} = sqrt(g_a*g_b)     Closest known scale
--------   ----------------    ----------------------     -------------------
C1 x C2    1.221e+18           1.563e+09 GeV              GUT scale? SUSY?
C1 x C3    4.908e+20           3.133e+10 GeV              Seesaw M_R? (factor 4000 off)
C2 x C3    8.040               4.010 GeV                  b quark 4.18 GeV (4% off!)
```

### Full 3x3 mass matrix eigenvalues (all J coupled simultaneously)

With J_12 = 1.221e18, J_13 = 4.908e20, J_23 = 8.040 GeV^2:

**[CORRECTED, Part 132, 2026-08-09]:** the eigenvalues originally stated here
(lambda_1~1.16e9, lambda_2~3.17e10 GeV^2) failed a basic linear-algebra
sanity check -- the sum of a matrix's eigenvalues must equal its trace, but
1.16e9+3.17e10 = 3.29e10 is ten orders of magnitude short of
trace(M^2) = 2(J_12+J_13+J_23) = 9.837e20. This was a computational error in
the original (unverified) version of this document, independent of the
FE1-FE3 sign issue above. Recomputed directly from the (sign-corrected, but
numerically identical in this case) mass matrix:

```
lambda_0 = 0                (Goldstone mode, exact)
lambda_1 ~ 1.831e18 GeV^2   =>  m_1 ~ 1.353e09 GeV  (~1.35 x 10^6 TeV)
lambda_2 ~ 9.819e20 GeV^2   =>  m_2 ~ 3.134e10 GeV  (~3.13 x 10^7 TeV)
```

(sum = 9.837e20 GeV^2, matching trace(M^2) exactly, Sudoku S17.) Both modes
remain far above any accessible energy scale -- the ORDER-OF-MAGNITUDE
conclusion below (C2-C3 mode is eaten by C1's dominant coupling) is
unaffected by this correction, only the specific TeV numbers were wrong.

**The C2-C3 mode (4 GeV) is EATEN by C1** in the full coupled system.
When J_12 and J_13 are both large (C1 couples hard to both C2 and C3),
the 4 GeV mode gets absorbed into the ~TeV modes and disappears.

**To recover the 4 GeV mode requires J_12 = J_13 = 0** — i.e. gravity decouples
from QCD and EW at low energies. This is EXACTLY what we see in nature:
gravity is negligible at the GeV scale. So the approximation is physically justified.

In the low-energy limit (J_12 = J_13 = 0, gravity decoupled):

```
L_4 (low energy) = (1/2)(d phi_2)^2 + (1/2)(d phi_3)^2 + (1/2)(d psi)^2
                 + g_2 cos(psi - phi_2) + g_3 cos(psi - phi_3)
                 + J_23 cos(phi_2 - phi_3)               [C2-C3 coupling only]

Mass of relative mode:  m_23 = sqrt(g_2 * g_3) = sqrt(0.200 * 80.4) = 4.010 GeV
b quark mass:  m_b = 4.18 GeV
Error: 4.1%
```

---

## Summary Table

**Note:** these are the ISOLATED-PAIR masses m_ab=sqrt(g_a*g_b) (each pair
computed alone, ignoring the third layer's coupling) -- not the full 3x3
coupled-system eigenvalues, which are close in magnitude but numerically
distinct (see the corrected "Full 3x3 mass matrix eigenvalues" section
above: m_1~1.35e9 GeV, m_2~3.13e10 GeV) since J13 dominates the system.

```
Layer pair   Coupling J_{ab}    New mode mass      Closest known      Error
----------   ----------------   ----------------   ---------------    -----
C1 x C2      g_P*g_QCD/2        1.56e9 GeV         GUT? (1e15 GeV)    6 orders
C1 x C3      g_P*g_W/2          3.13e10 GeV        Seesaw? (1e14 GeV) 4 orders
C2 x C3      g_QCD*g_W/2        4.01 GeV           b quark 4.18 GeV   4%
Goldstone    (always)           0 (massless)       --                 exact
```

---

## Comparison to All Four Lagrangians

```
Lagrangian   Fields         Coupling form          New modes
----------   ------         ----------------       ---------
L_1          phi, psi       g cos(psi-phi)         Breathing mode (omega_gap^2=2g)
L_2          phi_b,phi_s,   g cos - g cos          phi_- surface mode (reversed Higgs)
             psi
L_3          U in SU(3),    Re[Tr(Psi_dag U)]/3    8 gluons, Z3 vortices (quarks)
             Psi_i
L_4 (NEW)    phi_1,phi_2,   J_ab cos(phi_a-phi_b)  3 inter-layer modes:
             phi_3, psi     [inter-condensate]      Goldstone (m=0),
                                                    C1-C2 (~1.56e9 GeV),
                                                    C1-C3 (~3.13e10 GeV),
                                                    C2-C3 (~4.01 GeV if C1 decoupled)
```

---

## What Pops Out

1. **Goldstone mode is exact** — L_4 has an overall phase symmetry that guarantees
   one massless inter-condensate mode. No tuning. **[VERIFIED, Part 132]** --
   confirmed both for the specific 3x3 case (exact zero eigenvalue, eigenvector
   (1,1,1)) and in general for any number of condensate layers, by identifying
   the mass matrix as a weighted graph Laplacian (standard graph theory result).
   This is the most robust claim in the document.

2. **C2-C3 mode near 4 GeV -- much weaker evidence than originally presented
   [Part 132 re-examination].** The product rule J_23=g_QCD*g_W/2 does give
   m_23=4.01 GeV, close to the b quark's 4.18 GeV -- but Part 132 found this
   rule was adopted WITHOUT following the document's own cited justification
   (Lorentz-Berthelot actually implies a geometric mean, sqrt(g_a*g_b)/2, not
   a product); using the geometric mean instead gives m_23=2.00 GeV, a poor
   match to anything. Since both rules are equally valid dimensionally, and
   the one that was picked is the one that happens to produce an appealing
   number, the 4% "match" is much weaker evidence for the product rule than
   originally presented -- it looks more like the rule was reverse-engineered
   from the desired answer than derived independently. **[SPECULATIVE,
   downgraded]**

3. **Newton's 3rd law between condensates -- stronger than originally stated
   [Part 132].** The J_{ab} terms cancel pairwise in FE1+FE2+FE3 (verified),
   but the real content is FE1+FE2+FE3+FE4=0 identically (also verified) --
   the equation of motion for the exact overall-phase Goldstone direction
   across ALL FOUR fields (matter included), not just the three condensates.

4. **Vacuum energy increases with inter-layer coupling** — the J terms add to the
   cosmological constant. This makes the CC problem worse, not better. [NEGATIVE]

---

## What Needs To Be Done Next

1. ~~**SymPy verification**~~ **[DONE, Part 132, 2026-08-09]** — Euler-Lagrange
   equations, mass matrix, and conservation law all SymPy-verified. Found and
   corrected a real sign error in the original FE1-FE3 (the doc's FE4 and
   mass-matrix sections were already correct) and a real numerical error in
   the originally-stated full-3x3 eigenvalues (failed a basic trace check).
   See "SymPy Verification Results" section above. Sudoku 15/18 PASS
   (3 expected fails documenting the sign-error finding).

2. **Why J = g_a*g_b/2?** **[RE-EXAMINED, Part 132 -- still open, more
   skeptically]** — no first-principles symmetry or dimensional argument was
   found favoring the product rule over the geometric-mean rule the document's
   own cited analogy actually implies. Remains an open, unresolved question --
   arguably now the single most important gap in this document, since the
   headline numerical result depends entirely on which rule is chosen.

3. **What IS the C2-C3 mode?** — still open, and now lower-priority given (2)
   above substantially weakens the case that 4.01 GeV is a meaningful target
   to explain at all (as opposed to an artifact of rule selection). If (2) is
   ever resolved in the product rule's favor by independent means, revisit
   candidates: b quark (4.18 GeV, wrong quantum numbers -- no colour, not
   spin-1/2), chi_c(1P) charmonium (3.51 GeV), B meson (5.28 GeV).

4. **C1 decoupling at low energies** — Why does gravity decouple (J_12 = J_13 = 0) at GeV
   scales? Is this the hierarchy problem in disguise again?

5. **SU(3) extension of L_4** — Replace phi_a with SU(3) matrices U_a in each block.
   The cos(phi_a - phi_b) becomes Re[Tr(U_a^dag U_b)]/3.

6. ~~**T20:**~~ **[DONE, Part 133, 2026-08-09]** what physically IS the
   exact Goldstone mode identified in Sec "SymPy Verification Results" V2
   above? Answered in the "Physical meaning of the Goldstone mode" section
   above: a genuine, independent massless scalar (chi, the normalized sum
   of all 4 fields), NOT the graviton (spin mismatch) and NOT Part 61's
   phi_- (different field content, though structurally analogous), not
   currently eaten by anything (no gauge field in L_4 as written). 11/11
   Sudoku PASS.

---

*[PARTIALLY VERIFIED, Part 132] The field equations, conservation law, and
mass matrix structure are now SymPy-verified and corrected where needed (see
above). The product coupling rule J_{ab} = g_a*g_b/2 and the b quark
identification remain **[SPECULATIVE]**, and Part 132's re-examination found
the numerical "match" is substantially weaker evidence than originally
presented -- treat the b-quark connection as an unresolved open question, not
a finding. Sudoku scorecard: 15/18 PASS (Sec "SymPy Verification Results").*

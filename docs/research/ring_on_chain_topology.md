# Part 144 — Topological Dark-Matter Candidate: Ring-on-Chain Linking [SPECULATIVE]

**Phase:** 144 (structural/physical-mechanism analysis, grounded in cited
external vortex-dynamics literature — no new PDTP-Original equation
results, so no SymPy verification applies; per CLAUDE.md's own escape
clause, documented here rather than forced into a script)
**Date:** 2026-09-10
**Status:** DONE — NEGATIVE (with a genuine, informative caution flagged for T30).
**Closes:** TODO_04.md T76

**Epistemic tag, per explicit user instruction (2026-09-10): "remember all
are speculation except the scientific papers that we might build on or
use."** The ring-on-chain and Rubik's-cube/Cayley-graph ideas analyzed
here are the user's own original speculation, not citable physics claims.
Everything tagged [SPECULATIVE] below is the idea under test, not an
established result. The vortex-reconnection physics used to TEST the idea
(Section 2) is real, cited, established science.

---

## 1. The Idea Under Test

**Source:** `docs/misc/notes 2026-09-10.txt` — user's own original idea,
elevated (2026-09-10 correction) to its own dark-matter candidate item,
not a footnote on T30.

1. **[SPECULATIVE] "Ring on a chain" trick:** a chain laid out with two
   parallel lines forming a "U" at the bottom; a ring dropped over the
   two lines can become linked with the chain purely through the
   geometry/topology of the motion — no extra force, no energy input
   beyond whatever moves the ring.
2. **[SPECULATIVE, illustrative only] "Roving Bridges"** (canal tow-rope
   spiral crossings) — a second real-world example of the same class of
   effect, not a separate item.

**User's speculative question:** could a similar topological-linking
principle cause matter to become "twisted" into dark-matter-like behavior
*without* the exotic energy budget normally assumed — i.e., is dark
matter's mass/abundance possibly a topology effect rather than an
energy-cost effect?

This is a good, well-posed physical question, worth testing honestly
rather than dismissing — the plan below does that.

---

## 2. Testing the Idea Against Real Vortex-Topology Physics

### 2.1 What "Ring on a Chain" Actually Relies On

The mechanical trick works because a ring and a chain are treated as
**idealized, infinitely thin, non-interacting mathematical curves**: they
can be threaded past each other in a path that produces a nonzero linking
number, and once linked, nothing in the idealization allows them to pass
back through each other to unlink — the linking is permanent and was
"free" because the curves never had to touch, deform, or exchange energy
to acquire it.

**Key question 1 (filed):** does PDTP's condensate admit an analogous
configuration at all? **Yes, structurally** — PDTP's condensate already
supports closed vortex loops and vortex rings (used directly in T73's
Mechanism A, standard consequence of the BEC/Gross-Pitaevskii framework,
Part 34) and vortex filaments (Parts 33, 37). The configuration is
admissible in principle. The question is whether forming and keeping it
linked is actually free and stable, the way the mechanical toy suggests.

### 2.2 Where the Analogy Breaks (Methodology.md Section 4)

A real vortex — in PDTP's condensate exactly as in a real superfluid — is
**not** an idealized inextensible curve. It has a finite core (the healing
length ξ, Part 34) and a genuine energy density (the vortex line-energy
formula already used throughout this project, E/L ~ 2πK·ln(R/ξ), Part 33).
Two such vortices *can* pass close enough to interact and topologically
reconnect — merge and split, changing which loop is linked with which —
unlike idealized curves, which mathematically cannot pass through each
other at all. This single physical difference (finite core + real energy
vs. idealized infinitely-thin curve) is where the mechanical intuition
stops applying, and it is directly testable against real, established
vortex physics:

**Source:** Kleckner, D. and Irvine, W.T.M. (2013), "Creation and
dynamics of knotted vortices", *Nature Physics* 9, 253 (DOI:
10.1038/nphys2560) — the foundational experimental demonstration. Using
water (a classical fluid, but the topological mechanism is generic),
Kleckner and Irvine created linked vortex ring pairs and trefoil vortex
knots directly. **Observed result:** the linked/knotted vortices
**stretch and deform under their own geometrically-determined energy,
driving a series of local reconnections, after which the linked rings
spontaneously separate and the knots free themselves.** The linked
configuration is not a stable endpoint — it actively relaxes toward the
unlinked configuration, releasing energy as it goes.

**Source (quantum/superfluid confirmation, WebSearch-verified 2026-09-10):**
the same qualitative result holds for **quantized** vortices (the
PDTP-relevant case, not just classical fluid): numerical studies of
quantum vortex tangles find that linked and knotted configurations decay
through a **cascade** of decreasing topological complexity — a Whitehead
link, a connected sum of two Hopf links, a trefoil knot, a simple Hopf
link, ending in unknotted, unlinked loops — with total helicity
conserved but progressively transferred from *linking* helicity into
*writhe* and *twist* helicity as reconnections proceed. Reconnection
itself is an established energy-dissipation channel in quantum
turbulence (Kelvin-wave generation, phonon emission) — not a free
process.

### 2.3 Answering the Filed Key Questions

**Key question 2 (filed) — topologically stable, or transiently
entangled?** **Transiently entangled**, per Section 2.2: real (classical
and quantized) linked vortex configurations decay via reconnection
cascades in finite time, unlike an idealized mechanical ring-and-chain,
which — being infinitely thin and non-interacting — has no physical
mechanism available to unlink at all. This is the load-bearing point
where the analogy fails.

**Key question 3 (filed) — does the mechanism actually avoid an energy
cost, or does it cost the same as (or more than) winding-number
formation (Part 116/T43)?** **It costs more, and is less stable.** A
linked configuration of two vortex loops requires *at least* the sum of
each loop's own self-energy (the same E/L ~ ln(R/ξ) scaling already used
throughout this project, applied per loop) *plus* whatever additional
energy the linking geometry itself contributes — there is no regime in
which forming the linked state is cheaper than Part 116's single, simplest
n=1 winding vortex. And once formed, it doesn't even persist: Section 2.2
shows it actively decays toward the unlinked, lower-complexity state,
releasing energy rather than storing it. **This is the opposite of what
would be needed for a "topology avoids the exotic energy cost" dark-matter
mechanism** — the topology here doesn't remove an energy requirement, and
doesn't provide durable protection either.

**Key question 4 (filed) — Rubik's-cube/Cayley-graph idea:** per the
filing's own conditional trigger ("relevant only if T76's main line of
inquiry produces a genuine 'state-space topology determines mass/
abundance' result"), that trigger is **not met** — the main finding here
is negative. The Cayley-graph idea remains unexplored, exactly as
anticipated when this item was filed; no PDTP-specific field-theoretic
mapping is proposed or attempted.

---

## 3. Relationship to Existing PDTP Results (Cross-Checks, Per the Filing)

### 3.1 Vs. Part 116 / T43 (Winding-Number Selection)

**Not a restatement — genuinely distinct, and weaker.** T43's winding
number is a *static* topological classification of a single vortex's
boundary condition (an integer, conserved, present the instant the
vortex forms, no separate "linking" step needed). The ring-on-chain idea
is a *kinematic* claim about acquiring topology "for free" through a
process — and Section 2 shows that claim fails specifically because real
vortices can reconnect. T43's simplest (n=1, unlinked, single-vortex)
configuration remains the lowest-energy, most natural candidate; nothing
here challenges or improves on it. **Verdict: does not collapse into
T43 by re-description (my own pre-registered hypothesis when filing this
item was wrong) — it fails on its own, independent terms, for a
different and more decisive reason (an active decay channel, not
"secretly the same formula").**

### 3.2 Vs. T30 (Hopf-Link Topology Protection) — a Caution, Not a Resolution

T30 (still PENDING, unrelated to this item's negative) hopes that
Hopf-linked structures could give a PDTP condensate mode "decoherence
immunity... for vastly longer than simple vortex structures," citing the
standard `topological protection ~ exp(E_barrier/kT)` argument. **Section
2.2's finding is directly relevant and should be read into T30 before it
proceeds:** that exponential-protection argument implicitly assumes no
physical channel exists to change the topology at all (true for an
idealized curve, exactly as in the ring-on-chain mechanical picture) —
but real quantized vortex links, as demonstrated both classically
(Kleckner & Irvine) and in genuine quantum-turbulence numerics, **do**
have such a channel (reconnection) and use it. This does not resolve
T30 (reconnection rates depend on temperature, vortex density, and core
dynamics that T30 would need to estimate for PDTP's own condensate
parameters — not attempted here), but it means T30's optimistic
"vastly longer" framing needs to explicitly address reconnection as a
competing decay channel, not just cite the idealized topological-barrier
formula. **Flagged as an open input to T30, not a resolution of it.**

---

## 4. Verdict and Status

**TODO_04.md T76 — RESOLVED: NEGATIVE, with a genuine caution flagged
for T30.**

1. **[SPECULATIVE idea, tested against ESTABLISHED physics, NEGATIVE]:**
   the ring-on-chain mechanical intuition — that topology can produce
   linking "for free," without an exotic energy budget — does not
   transfer to real (or PDTP-modeled) vortex physics. The idealization
   it depends on (infinitely thin, non-interacting curves) is exactly
   the assumption physical vortices violate (finite core, real energy,
   reconnection). Cited directly against real experimental (Kleckner &
   Irvine 2013) and numerical quantum-turbulence results, not just
   argued qualitatively.
2. Forming a linked configuration costs *more* energy than Part 116's
   simplest single-vortex candidate, and is *less* stable (actively
   decays via reconnection) — the opposite of what the idea needed to
   succeed as a cheaper dark-matter mechanism.
3. Not a restatement of T43 (my own pre-registered "likely outcome" when
   filing this item) — it is a genuinely distinct claim that fails for
   its own, more decisive reason.
4. Rubik's-cube/Cayley-graph idea: correctly left unexplored, per its
   own conditional scope.
5. **Productive side effect:** surfaces a real physical caution (vortex
   reconnection as a decay channel) that T30 needs to address when it is
   next picked up — this Part's most useful output going forward.

**Plain English:** the appealing "it's just topology, no extra energy
needed" intuition from the ring-and-chain trick comes from treating the
ring and chain as idealized threads that can never touch each other. Real
vortices — in a superfluid, or in PDTP's own condensate — aren't like
that: they're physical, they have some thickness, and when two of them
get close enough, they can reconnect and swap which one is linked to
which. Real experiments (spinning up linked vortex rings in water) and
real quantum-vortex simulations both show the same thing: linked vortices
don't stay linked — they undo themselves and give off energy while doing
it. So the topology doesn't save you the energy cost after all; if
anything, it costs more to set up in the first place, and it doesn't even
last.

---

## 5. Sources

- **Source:** Kleckner, D. and Irvine, W.T.M. (2013), "Creation and
  dynamics of knotted vortices", *Nature Physics* 9, 253, DOI:
  10.1038/nphys2560 — foundational experimental demonstration that linked/
  knotted vortex configurations self-untie via reconnection, driven by
  their own energy.
- **Source (WebSearch-verified, quantum/superfluid case):** numerical
  studies of quantized vortex tangles showing linked/knotted
  configurations (Whitehead link, connected sum of Hopf links, trefoil
  knot, Hopf link) decay in cascade to unlinked, unknotted loops, with
  helicity transferred from linking to writhe/twist — confirms the same
  qualitative physics holds for the PDTP-relevant (quantized) case, not
  only the classical demonstration.
- **Reused, not re-derived:** Part 33/37 (vortex line-energy formula,
  E/L ~ 2πK·ln(R/ξ)); Part 34 (healing length ξ, BEC/GP framework); Part
  116/T43 (winding-number DM candidate, comparison baseline); T30
  (Hopf-link decoherence-protection hypothesis, flagged with a caution
  here, not resolved).

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*

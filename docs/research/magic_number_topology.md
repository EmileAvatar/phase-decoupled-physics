# Magic Numbers vs PDTP Z₃ Topology (Part 137)

**Method:** Combinatorial/numeric comparison of the real nuclear magic
number sequence against candidate PDTP closed-vortex-network counting
rules, plus an energy-scale check against Part 37/106's established
vortex-baryon energies.
**Status:** [DERIVED, NEGATIVE] on all three tests. Closes T28 as filed
and resolves T40's conceptual Key Questions 1-4 (T40's remaining
implementation steps 4-8 become moot — see Sec 8).
**Script:** `simulations/solver/t28_magic_number_topology.py` (Part 137)
**Cross-checks:** Part 37 (SU(3) Y-junction, string tension), Part 106
(Hopf-link baryon energies), Part 53 (Z₃ Koide), T37/Part 107 (SEMF
baseline, the ~9-15 MeV gap this was hoping to close)
**Date:** 2026-08-30

---

## Plain English Summary

Certain numbers of protons or neutrons (2, 8, 20, 28, 50, 82, 126, and
probably 184) make a nucleus unusually stable — these are the "magic
numbers," long explained by the standard nuclear shell model. T28 and T40
both ask the same underlying question from slightly different angles:
could these numbers instead come from PDTP's own three-fold (Z₃) vortex
topology — the same mathematical structure already used for quarks
(Part 37) and baryons (Part 106) — rather than from the mean-field shell
model? **The answer, checked three independent ways, is no.** No natural
"closed three-fold network" counting sequence reproduces the real magic
numbers past the first two or three entries; the real sequence's own
internal pattern isn't a multiple-of-three structure either; and even if
a topological mechanism existed, PDTP's own vortex-energy formulas
(already established for quark confinement) are 200 to 11,000 times too
large to explain nuclear shell gaps, with no existing PDTP mechanism to
shrink them down to the right scale. This is exactly the kind of
"informative negative" both TODO items said they were prepared for — it
means nuclear shell structure really is independent of PDTP's condensate
physics, which is itself worth knowing.

---

## 1. The Question — T28 and T40, Addressed Together

T28 (Key Questions 1-3) and T40 (Key Questions 1-2, 4) ask essentially the
same core question through different framings, confirmed by direct
comparison of their TODO_04.md text: does the magic-number sequence
(2, 8, 20, 28, 50, 82, 126, 184) correspond to closed Z₃ vortex-network
topology in the SU(3) condensate (Part 37), and can such topology supply
the ~1-2 MeV shell-binding gap (T28) or the specific ~8-14 MeV gap needed
to bridge T37's Lazar-claim comparison at Mc-299 (T40)? Because the
underlying test is identical, this document runs it once and reports the
result against both TODO items' specific question lists (Sec 6-7).

## 2. Established Baseline: Where Magic Numbers Actually Come From

**Source:** Mayer, M. G. (1949), *Phys. Rev.* 75, 1969, "On Closed Shells
in Nuclei II"; Haxel, O., Jensen, J. H. D., Suess, H. E. (1949), *Phys.
Rev.* 75, 1766, "On the 'Magic Numbers' in Nuclear Structure" (joint 1963
Nobel Prize work). **Source:** Wikipedia, "Magic number (physics)" —
confirms the standard list "2, 8, 20, 28, 50, 82, and 126" and states
"the sequence of spherical magic numbers cannot be extended [past 126] in
this way" without additional theory (verified present on the page,
2026-08-30) — i.e. 184 is a theoretical extrapolation (the "island of
stability" target), not yet an experimentally confirmed magic number.

The mechanism [ESTABLISHED]: a bare 3D isotropic harmonic-oscillator (HO)
potential gives shell degeneracies (N+1)(N+2) per level N (including
spin), with cumulative closed-shell numbers 2, 8, 20, 40, 70, 112, 168 —
matching the REAL magic numbers only for the first three (2, 8, 20).
Mayer, and independently Haxel/Jensen/Suess, showed the remaining
mismatch (28 vs 40, 50 vs 70, 82 vs 112, 126 vs 168) is fixed by adding a
strong **spin-orbit coupling** term, which splits the highest total
angular momentum (j = l+1/2) sub-level off each new HO shell and pulls it
down to close the PREVIOUS shell early. **This is structurally a
spin/angular-momentum (two-valued, j = l ± 1/2) effect, not a three-fold
effect** — there is no established three-fold (Z₃-type) symmetry
anywhere in the accepted derivation of the magic numbers.

## 3. Test 1: Candidate Closed-Network Counting Sequences

Three independently-established counting sequences were tested against
the confirmed real magic numbers (2, 8, 20, 28, 50, 82, 126 — the
unconfirmed 184 excluded from the match count per Sec 2):

| Candidate | Sequence (first 8 terms) | Source | Matches (of 7) |
|---|---|---|---:|
| 3D harmonic oscillator (pre-spin-orbit) | 2, 8, 20, 40, 70, 112, 168, 240 | Standard shell model (Sec 2) | 3 (2, 8, 20) |
| Cuboctahedral/FCC shells | 1, 13, 55, 147, 309, 561, 923, 1415 | Wikipedia, "Centered icosahedral number," verified 2026-08-30 — the SAME lattice type PDTP's own Part 54 uses | 0 |
| Tetrahedral numbers (Z₃-arm layer counting) | 1, 4, 10, 20, 35, 56, 84, 120, 165, 220 | Standard combinatorics (figurate numbers) | 1 (20, coincidental — 20 also matches the HO sequence independently) |

[DERIVED, computed via `t28_magic_number_topology.py`] None of the three
candidates — including the FCC/cuboctahedral sequence, which is the exact
lattice type PDTP's own cosmological-constant work (Part 54) already
relies on — reproduces the magic-number sequence beyond a small,
explicable overlap. The FCC/cuboctahedral sequence in particular gives
**zero** matches, a clean, direct negative for the specific hypothesis
that PDTP's own established closed-shell counting type applies here.

## 4. Test 2: Direct Z₃ Divisibility Check

If the magic-number sequence were generated by a three-fold (Z₃) closure
rule, its consecutive gaps would be expected to show a multiple-of-3 (or
multiple-of-6, allowing for the 2-fold spin degeneracy) structure.
Computed consecutive differences [script Sec 4]:

```
Magic numbers:  2    8   20   28   50   82  126
Differences:      6   12    8   22   32   44
Divisible by 3:  YES  YES   NO   NO   NO   NO
Divisible by 6:  YES  YES   NO   NO   NO   NO
```

[DERIVED] The pattern holds for the first two gaps (consistent with the
first three magic numbers also matching the pure-HO sequence, Sec 3 — an
already-understood coincidence, not evidence of Z₃ structure) and fails
decisively from the third gap onward (8, 22, 32, 44 are not multiples of
3 or 6). This directly answers T28 Key Question 3 ("is 2,8,20,28,50,82,
126,184 a Z₃ sequence?"): **no.**

## 5. Test 3: Energy Scale Check

Even setting aside Sec 3-4's negative result and asking hypothetically
"if closed Z₃ vortex networks DID exist at the nuclear scale, could they
plausibly supply the needed binding energy?" — the answer is also no, by
a wide margin. PDTP's own established vortex-baryon energy formulas
(Part 37, Part 106 Eq 106.4):

```
E_Y = 3*sigma*L      (Y-junction, 3-arm flux tube)                       (1)
E_H = 6*pi*sigma*R    (Hopf-link, 3-component linked loop)                (2)
```

with sigma = 0.18 GeV^2 (Part 37/38) and L = R = 1 fm (typical baryon
scale, Part 106 Sec 5.1) [script Sec 5]:

```
E_Y = 2.741 GeV = 2741 MeV
E_H = 17.223 GeV = 17223 MeV
```

Against T28's own stated target (~1.5 MeV typical shell gap) and T40's
own stated target (~11 MeV at Mc-299):

| Comparison | Ratio |
|---|---:|
| E_Y / typical shell gap (1.5 MeV) | 1827x too large |
| E_H / typical shell gap (1.5 MeV) | 11482x too large |
| E_Y / T40's Mc-299 target (11 MeV) | 249x too large |
| E_H / T40's Mc-299 target (11 MeV) | 1566x too large |

[DERIVED] These are the SAME energy formulas already established and
verified for individual-baryon (single-nucleon, quark-confinement-scale)
structure — they were never intended or derived to describe a NETWORK OF
MULTIPLE NUCLEONS within a nucleus, and Sec 3-4 already show no such
network-counting rule reproduces the target sequence in the first place.
This is not "PDTP's numbers are close but need a small correction" — it
is a 2-4 order-of-magnitude mismatch with no established suppression
mechanism anywhere in the current framework (contrast with, e.g., the
dark-matter self-interaction cross-section, Part 118, which DOES have a
derived v^4 velocity-suppression factor bridging its own scale gap — no
analogous mechanism has been derived here).

---

## 6. Answering T28's Key Questions

1. **Can the ~1-2 MeV shell binding be derived from closed Z₃ vortex-loop
   topology?** No. Sec 5 shows PDTP's only established vortex-energy
   formulas overshoot this target by 3-4 orders of magnitude, and Sec 3-4
   show there is no closed-network counting rule to attach such a formula
   to in the first place.
2. **Does Mc-299 sit at a special topological point?** No principled basis
   found. Since no Z_3-network structure reproduces the magic-number
   sequence at all (Sec 3-4), there is no topological framework within
   which N=184 (or Z=114/115) could be identified as "special" — this
   question presupposes a structure Sec 3-4 shows does not exist.
3. **Is 2,8,20,28,50,82,126,184 a Z₃ sequence?** No (Sec 4) — divisibility
   by 3 fails from the third gap onward, decisively.

**Verdict: T28 closes as a clean NEGATIVE** — exactly the outcome its own
"Likely outcome" field flagged as informative: nuclear shell structure is
independent of PDTP's condensate topology, at least via the specific
closed-Z₃-network mechanism tested here.

## 7. Answering T40's Key Questions

1. **Do the magic numbers correspond to complete closed Z₃ vortex
   networks?** No (Sec 3-4, same test as T28 KQ3).
2. **Is the sequence derivable from a Z₃ packing rule, or coincidental?**
   The first three terms (2, 8, 20) coincide with the pure-3D-HO sequence
   — already explained by standard physics (Sec 2), not evidence of Z₃
   structure. Beyond that, no candidate rule reproduces any further terms.
3. **Does Mc-299 sit one proton away from a closed Z₃ network at Z=114?**
   Not assessable — there is no established closed-Z₃-network definition
   at the nuclear (many-nucleon) scale for Mc-299 to sit near or far from
   (Sec 3-4 rule out the counting sequences that would have defined one).
4. **How much extra binding does a closed vs open Z₃ network predict?**
   No candidate network survived Sec 3-4 to compute a binding difference
   from; separately, Sec 5 shows the only established PDTP vortex-energy
   scale (GeV) is 200-11000x larger than the ~8-14 MeV target regardless.
5. **Can the correction be expressed as `pdtp_topology_correction(Z,N)`
   for T37's SEMF predictor?** No principled formula to implement — see
   Sec 8.

**Verdict: T40's conceptual Key Questions (1, 2, 4) are resolved
NEGATIVE, consistent with T40's own anticipated "clean NEGATIVE ...
rules out this mechanism" outcome.** T40's remaining implementation steps
(SymPy-verify a formula, implement `pdtp_topology_correction`, re-run
T37's Sudoku/Z=115 scan, update falsifiable_predictions.md Prediction 13)
require a surviving formula to implement — since none survived Sec 3-5,
those steps have no formula left to wire in (Sec 8).

---

## 8. Verdict: Both T28 and T40 Close Together

Because T28 and T40 test the identical core hypothesis (Sec 1), and both
explicitly anticipated a clean negative as a valid, informative outcome,
**this document closes both items together.** T40's implementation
checklist (steps 4-8: build `pdtp_topology_correction(Z,N)`, wire it into
`t37_isotope_stability.py`, re-run the Sudoku suite and Z=115 scan) is
**not executed**, because Sec 3-5 found no surviving candidate formula to
implement — implementing a null/zero correction would just reproduce
T37's existing baseline (already on record: 6/15 Sudoku, longest-lived
Z=115 isotope ~11s, Part 107), adding no new information.

**What this negative result establishes, positively:** nuclear shell
structure — one of the best-confirmed, most precisely measured structures
in all of physics — shows no trace of PDTP's Z₃/SU(3) vortex topology by
any of the three tests run here (sequence matching, divisibility
structure, energy scale). This is a meaningful constraint in its own
right: it means PDTP's SU(3) condensate sector, wherever it does apply
(Part 37's quark/gluon structure), does **not** extend its influence to
the nucleon-counting level inside a nucleus — the two scales are
decoupled, at least via this mechanism.

## 9. What Remains Open

**The underlying T37 gap is NOT closed by this document and remains a
real open problem.** The ~9-15 MeV / ~29-order-of-magnitude gap between
the SEMF baseline's Z=115 half-life prediction (~11 s) and Lazar's
"stable Element 115" claim (Part 107, T37) is untouched by this negative
result — it simply means the specific PDTP-topological explanation for
that gap does not work. Standard nuclear-structure theory's own tools for
this gap (Strutinsky shell correction, FRDM, Moller-Nix macroscopic-
microscopic models — already noted in T40's own "Why now" framing) remain
the correct, unexamined-here path if the gap is to be closed by any
established mechanism; this document takes no position on whether they
succeed, only that PDTP's topological alternative does not.

---

## 10. References

- Mayer, M. G. (1949), "On Closed Shells in Nuclei II," *Phys. Rev.* 75,
  1969.
- Haxel, O., Jensen, J. H. D., Suess, H. E. (1949), "On the 'Magic
  Numbers' in Nuclear Structure," *Phys. Rev.* 75, 1766.
- **Source:** [Magic number (physics)](https://en.wikipedia.org/wiki/Magic_number_(physics))
  (Wikipedia) — confirmed magic-number list and 184's unconfirmed status,
  verified present on the page 2026-08-30.
- **Source:** [Centered icosahedral number](https://en.wikipedia.org/wiki/Centered_icosahedral_number)
  (Wikipedia) — cuboctahedral/FCC shell sequence, verified present on the
  page 2026-08-30.
- Part 37 (`su3_condensate_extension.md`) — Y-junction geometry, string
  tension sigma = 0.18 GeV^2.
- Part 106 (`hopf_link_baryon.md`) — E_Y = 3*sigma*L, E_H = 6*pi*sigma*R
  (Eq 106.4), the energy formulas compared in Sec 5.
- Part 107 / T37 (`isotope_stability.md`) — SEMF baseline, the ~9-15 MeV
  gap referenced in Sec 9.
- Part 118 — dark-matter self-interaction v^4 suppression, cited in Sec 5
  as an example of the KIND of mechanism that would be needed here but
  has not been derived.
- Part 54 (`cosmological_constant_fcc.md`) — PDTP's own established use of
  FCC lattice structure, the basis for testing the cuboctahedral
  candidate in Sec 3.

---

*End of Part 137 (T28 + T40 conceptual resolution).*


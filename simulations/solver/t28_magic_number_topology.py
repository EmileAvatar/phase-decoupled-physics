#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t28_magic_number_topology.py -- TODO_04 T28 (+ T40 conceptual overlap), Part 137
=======================================================================
Tests whether the nuclear magic-number sequence (2,8,20,28,50,82,126,184)
is reproducible from a PDTP Z_3/closed-vortex-network counting rule (T28
Key Question 3, T40 Key Questions 1-2), and whether PDTP's established
vortex/Y-junction/Hopf-link energy scale (Part 37/106, GeV) can plausibly
supply the observed ~1-2 MeV nuclear shell binding gap (T28 Key Question 1,
T40 Key Question 4).

Established facts used here (cited, not re-derived):
- Nuclear magic numbers 2,8,20,28,50,82,126: Mayer, M.G. (1949), Phys. Rev.
  75, 1969; Haxel, Jensen, Suess (1949), Phys. Rev. 75, 1766 (spin-orbit
  shell model). 184 is the predicted (not yet confirmed) next spherical
  magic number -- Wikipedia "Magic number (physics)", verified 2026-08-30.
- Y-junction baryon energy E_Y = 3*sigma*L, Hopf-link baryon energy
  E_H = 6*pi*sigma*R, sigma = 0.18 GeV^2: Part 37, Part 106
  (hopf_link_baryon.md Sec 5.1, Eq 106.4).
- Centered icosahedral / cuboctahedral (FCC shell) numbers 1,13,55,147,
  309,561,923: Wikipedia "Centered icosahedral number", verified 2026-08-30.

PDTP Original: none of the candidate formulas below are new physics --
this script tests whether ESTABLISHED counting sequences (3D HO shells,
FCC/cuboctahedral shells, tetrahedral numbers) coincide with the REAL
nuclear magic numbers, and separately checks the PDTP vortex energy scale
against the target nuclear binding scale. The comparison/interpretation
of these results as evidence for-or-against a PDTP mechanism is original.

Output: DATA only. Interpretation in docs/research/magic_number_topology.md.
"""

import math

REAL_MAGIC_NUMBERS = [2, 8, 20, 28, 50, 82, 126, 184]  # 184 = predicted, not confirmed


def candidate_3d_ho_shells(n_shells):
    """Cumulative degeneracy of a 3D isotropic harmonic oscillator, WITH
    spin (factor 2): degeneracy of shell N (N=0,1,2,...) = (N+1)(N+2).
    Source: standard nuclear shell model (pre-spin-orbit), textbook result
    -- e.g. Krane, "Introductory Nuclear Physics" (1988), Ch. 5."""
    cumulative = []
    total = 0
    for N in range(n_shells):
        degeneracy = (N + 1) * (N + 2)
        total += degeneracy
        cumulative.append(total)
    return cumulative


def candidate_cuboctahedral_fcc_shells(n_shells):
    """Centered icosahedral/cuboctahedral numbers (identical for FCC close
    packing): C(0)=1, C(n) = C(n-1) + 10n^2+2 for n>=1 (standard closed
    form: (2n+1)(5n^2+5n+3)/3). Source: Wikipedia "Centered icosahedral
    number", verified 2026-08-30."""
    seq = []
    for n in range(n_shells):
        c = (2 * n + 1) * (5 * n**2 + 5 * n + 3) // 3
        seq.append(c)
    return seq


def candidate_tetrahedral_numbers(n_max):
    """Tetrahedral numbers T_n = n(n+1)(n+2)/6 -- the natural "closed
    Z_3-arm packing" counting sequence (each new shell adds a triangular
    layer). Source: standard combinatorics (figurate numbers)."""
    return [n * (n + 1) * (n + 2) // 6 for n in range(1, n_max + 1)]


def check_divisibility_pattern(numbers, divisor):
    """RECHECK-compliant: computes actual consecutive differences and
    tests divisibility -- does not assert the answer."""
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    divisible = [d % divisor == 0 for d in diffs]
    return {'diffs': diffs, 'divisor': divisor, 'all_divisible': all(divisible),
            'divisible_pattern': divisible}


def compare_sequence(candidate, real, label):
    """Computed set-intersection comparison -- how many of the 7 confirmed
    real magic numbers (excluding the unconfirmed 184) appear anywhere in
    the candidate sequence, at ANY position (generous test)."""
    confirmed_real = real[:7]  # 2,8,20,28,50,82,126 (184 excluded, unconfirmed)
    candidate_set = set(candidate)
    matches = [n for n in confirmed_real if n in candidate_set]
    return {
        'label': label,
        'candidate_sequence': candidate,
        'confirmed_real_magic_numbers': confirmed_real,
        'matches': matches,
        'n_matches': len(matches),
        'match_fraction': len(matches) / len(confirmed_real),
        'exact_full_sequence_match': matches == confirmed_real,
    }


def scale_mismatch_check():
    """Compare PDTP's established vortex-baryon energy scale (Part 37/106)
    against the target nuclear shell-binding scale (T28/T40's own stated
    targets)."""
    sigma = 0.18  # GeV^2, Part 37/38
    L_fm = 1.0  # fm, typical baryon size, Part 106 Sec 5.1
    R_fm = 1.0  # fm, typical loop radius, Part 106 Sec 5.1
    hbar_c_gev_fm = 0.197  # GeV*fm

    E_Y_gev = 3 * sigma * (L_fm / hbar_c_gev_fm)
    E_H_gev = 6 * math.pi * sigma * (R_fm / hbar_c_gev_fm)

    typical_shell_gap_mev = 1.5  # MeV, midpoint of T28's stated "~1-2 MeV"
    t40_target_mev = 11.0  # MeV, midpoint of T40's stated "~8-14 MeV" at Mc-299

    E_Y_mev = E_Y_gev * 1000.0
    E_H_mev = E_H_gev * 1000.0

    return {
        'E_Y_GeV': E_Y_gev, 'E_H_GeV': E_H_gev,
        'E_Y_MeV': E_Y_mev, 'E_H_MeV': E_H_mev,
        'typical_shell_gap_MeV': typical_shell_gap_mev,
        't40_target_MeV': t40_target_mev,
        'ratio_E_Y_to_shell_gap': E_Y_mev / typical_shell_gap_mev,
        'ratio_E_H_to_shell_gap': E_H_mev / typical_shell_gap_mev,
        'ratio_E_Y_to_t40_target': E_Y_mev / t40_target_mev,
        'ratio_E_H_to_t40_target': E_H_mev / t40_target_mev,
    }


def main():
    print("=" * 78)
    print("T28/T40 (Part 137): Magic Numbers vs PDTP Z_3 Topology")
    print("=" * 78)
    print(f"\nReal magic numbers (confirmed 2-126, predicted 184): {REAL_MAGIC_NUMBERS}")

    ho = candidate_3d_ho_shells(8)
    r1 = compare_sequence(ho, REAL_MAGIC_NUMBERS, "3D harmonic oscillator (pre-spin-orbit)")
    print(f"\n[1] {r1['label']}: {r1['candidate_sequence']}")
    print(f"    Matches: {r1['matches']} ({r1['n_matches']}/7); exact full match: {r1['exact_full_sequence_match']}")

    fcc = candidate_cuboctahedral_fcc_shells(8)
    r2 = compare_sequence(fcc, REAL_MAGIC_NUMBERS, "Cuboctahedral/FCC shells (Part 54's own lattice type)")
    print(f"\n[2] {r2['label']}: {r2['candidate_sequence']}")
    print(f"    Matches: {r2['matches']} ({r2['n_matches']}/7); exact full match: {r2['exact_full_sequence_match']}")

    tet = candidate_tetrahedral_numbers(12)
    r3 = compare_sequence(tet, REAL_MAGIC_NUMBERS, "Tetrahedral numbers (Z_3-arm layer counting)")
    print(f"\n[3] {r3['label']}: {r3['candidate_sequence']}")
    print(f"    Matches: {r3['matches']} ({r3['n_matches']}/7); exact full match: {r3['exact_full_sequence_match']}")

    r4 = check_divisibility_pattern(REAL_MAGIC_NUMBERS[:7], 3)
    print(f"\n[4] Consecutive differences of real magic numbers: {r4['diffs']}")
    print(f"    All divisible by 3: {r4['all_divisible']} (pattern: {r4['divisible_pattern']})")

    r5 = check_divisibility_pattern(REAL_MAGIC_NUMBERS[:7], 6)
    print(f"    All divisible by 6: {r5['all_divisible']} (pattern: {r5['divisible_pattern']})")

    r6 = scale_mismatch_check()
    print(f"\n[5] PDTP vortex-baryon energy scale (Part 37/106) vs nuclear shell target:")
    print(f"    E_Y (Y-junction) = {r6['E_Y_GeV']:.3f} GeV = {r6['E_Y_MeV']:.0f} MeV")
    print(f"    E_H (Hopf-link)  = {r6['E_H_GeV']:.3f} GeV = {r6['E_H_MeV']:.0f} MeV")
    print(f"    Target: typical shell gap ~{r6['typical_shell_gap_MeV']} MeV, T40's Mc-299 target ~{r6['t40_target_MeV']} MeV")
    print(f"    E_Y / typical shell gap = {r6['ratio_E_Y_to_shell_gap']:.0f}x too large")
    print(f"    E_H / typical shell gap = {r6['ratio_E_H_to_shell_gap']:.0f}x too large")
    print(f"    E_Y / T40 target        = {r6['ratio_E_Y_to_t40_target']:.0f}x too large")
    print(f"    E_H / T40 target        = {r6['ratio_E_H_to_t40_target']:.0f}x too large")

    print("\n" + "=" * 78)
    print("Summary: no candidate closed-network counting sequence reproduces the")
    print("real magic numbers past the first 2-3 entries; consecutive differences")
    print("are NOT uniformly divisible by 3 (fails at the 3rd gap); PDTP's own")
    print("vortex-baryon energy scale exceeds the nuclear shell target by 2-3")
    print("orders of magnitude with no established suppression mechanism.")
    print("Full interpretation in docs/research/magic_number_topology.md.")
    print("=" * 78)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moire_quick_checks_m3_m4.py -- TODO_04 M3/M4 quick checks
=======================================================================
Continues the M1/M2 quick-check series (simulations/solver/outputs/
moire_quick_checks.txt, 2026-04-04): 10-minute numerical sanity checks
on the Wolfram moire/Pythagorean-lock-in speculation, NOT full Parts.
Per the TODO_04 M1-M4 note: "run the simple numerical checks... to see
if the moire angle hypothesis survives first contact with numbers."
M1 (alpha_EM) and M2 (Weinberg angle) both came back NEGATIVE/INCONCLUSIVE
(no small-integer lock-in). This continues with M3 and M4.

M3: does the moire band-spacing formula lambda_moire = (1/2)*csc(theta/2)*a
reproduce Part 89's evanescent depths at the condensate boundaries?

M4: does quark winding n=73 correspond to a genuinely SMALL Pythagorean
generator pair {r,s} (u=r^2-s^2=n, v=2rs), or is the pair already found
in the TODO note (37,36) a mathematical inevitability that says nothing
about the physics?

PDTP Original: none of this is a new physics claim -- it is a check of
whether an existing, previously untested speculation (Wolfram's moire
band-spacing/Pythagorean-lock-in framing, TODO_03 G1) survives contact
with PDTP's own already-established numbers. Both established formulas
used (lambda_moire, evanescent depth, Compton wavelength) are cited to
their PDTP sources (Part 89, Part 96) or to Wolfram (A New Kind of
Science, moire pattern chapter, cited in TODO_03/TODO_04).

Output: DATA only. Verdict discussion in TODO_04.md M3/M4 entries
(no dedicated research doc -- matching the M1/M2 precedent, which also
stayed TODO-only).
"""

import sympy as sp
import itertools

# ===========================================================================
# CONSTANTS
# ===========================================================================
HBAR_C_MEV_FM = 197.3269804   # MeV*fm (hbar*c, exact-ish CODATA combination)
LAMBDA_QCD_MEV = 200.0        # MeV (Part 89's own value, m_gap for B1)
M_W_MEV = 80.4e3               # MeV (m_gap for B2)


# ===========================================================================
# M3: moire band spacing vs evanescent depth
# ===========================================================================
def m3_band_spacing_check():
    """
    Part 89 (condensate_layer_optics.md Eq 89.13-89.15) and Part 96
    (same doc, Eq 96.1 table, "Starting point: Condensate lattice spacing
    = Compton wavelength of gap mass") both use the IDENTICAL formula
    a = lambda_evan = hbar*c/E_gap for the condensate lattice spacing --
    they are not independently derived quantities, they are the same
    formula given two different names in two different sections. This
    must be checked FIRST, because it means a = lambda_evan is forced
    by definition, not a result to be tested.
    """
    a_B1_fm = HBAR_C_MEV_FM / LAMBDA_QCD_MEV     # Part 96's own lattice-spacing formula
    lambda_evan_B1_fm = HBAR_C_MEV_FM / LAMBDA_QCD_MEV  # Part 89's own evanescent-depth formula
    a_equals_lambda_evan_B1 = abs(a_B1_fm - lambda_evan_B1_fm) < 1e-12

    a_B2_fm = HBAR_C_MEV_FM / M_W_MEV
    lambda_evan_B2_fm = HBAR_C_MEV_FM / M_W_MEV
    a_equals_lambda_evan_B2 = abs(a_B2_fm - lambda_evan_B2_fm) < 1e-12

    # Solve lambda_moire = (1/2)*csc(theta/2)*a = a for theta, symbolically,
    # WITHOUT substituting a numeric value for a -- to show the result does
    # not depend on which boundary (i.e. which value of a) is used.
    theta, a_sym = sp.symbols('theta a', positive=True)
    lambda_moire_expr = sp.Rational(1, 2) * (1 / sp.sin(theta / 2)) * a_sym
    equation = sp.Eq(lambda_moire_expr, a_sym)
    # a cancels algebraically -- solve the theta-only equation this reduces to
    reduced_equation = sp.Eq(sp.Rational(1, 2) / sp.sin(theta / 2), 1)
    theta_solutions = sp.solve(reduced_equation, theta)
    theta_deg_solutions = [sp.deg(s).evalf() for s in theta_solutions if s.is_real]

    # Confirm the reduction (a cancels) is legitimate: substitute a generic
    # symbol and check the "a" dependence truly drops out of the SOLVED theta
    a_dependence_check = sp.simplify(sp.solve(equation, theta)[0] -
                                      sp.solve(reduced_equation, theta)[0])

    return {
        'a_B1_fm': a_B1_fm,
        'lambda_evan_B1_fm': lambda_evan_B1_fm,
        'a_equals_lambda_evan_B1': a_equals_lambda_evan_B1,
        'a_B2_fm': a_B2_fm,
        'lambda_evan_B2_fm': lambda_evan_B2_fm,
        'a_equals_lambda_evan_B2': a_equals_lambda_evan_B2,
        'theta_solutions_rad': theta_solutions,
        'theta_deg_solutions': theta_deg_solutions,
        'a_dependence_check_residual': a_dependence_check,   # expect 0 -- theta independent of a
        'part121_su3_angle_deg': 60.0,   # Part 121/T10, tan(theta)=sqrt(3), independently derived
    }


# ===========================================================================
# M4: quark winding n=73 vs Pythagorean generator pair
# ===========================================================================
def m4_winding_pythagorean_check():
    """
    Check whether n=73 = r^2 - s^2 for a genuinely SMALL {r,s} pair (the
    TODO note's own standard -- "smallest lattice vector"), or whether the
    (37,36) pair it already found is a mathematical inevitability for any
    odd n, carrying no information about the physics.

    General claim to verify: for ANY odd N, (r,s) = ((N+1)/2, (N-1)/2)
    satisfies r^2-s^2=N and gcd(r,s)=1 automatically (SymPy, symbolic, for
    general odd N -- not just checked at N=73).
    """
    N = sp.symbols('N', positive=True, odd=True)
    r_generic = (N + 1) / 2
    s_generic = (N - 1) / 2
    identity_residual = sp.simplify(r_generic**2 - s_generic**2 - N)   # expect 0, symbolic, general odd N

    # gcd(r,s) = gcd(s+1, s) = 1 always, since consecutive integers are coprime
    # (checked structurally: r_generic - s_generic = 1 identically)
    r_minus_s = sp.simplify(r_generic - s_generic)

    # Specific case N=73
    n_val = 73
    is_prime = sp.isprime(n_val)
    r73, s73 = (n_val + 1) // 2, (n_val - 1) // 2
    check73 = r73**2 - s73**2 == n_val
    gcd73 = sp.gcd(r73, s73)

    # Brute-force search: are there ANY OTHER (r,s) pairs with 0 < s < r <= 200
    # giving r^2 - s^2 = 73? (Exhaustive over a generous range, not just "small")
    other_pairs = []
    for r in range(2, 201):
        for s in range(1, r):
            if r * r - s * s == n_val:
                other_pairs.append((r, s))

    v73 = 2 * r73 * s73
    gcd_uv73 = sp.gcd(n_val, v73)

    return {
        'identity_residual_general_odd_N': identity_residual,   # expect 0
        'r_minus_s_general': r_minus_s,                          # expect 1 (forces gcd=1)
        'n73_is_prime': is_prime,
        'r73': r73, 's73': s73,
        'check73_valid': check73,
        'gcd73': int(gcd73),
        'all_pairs_found_up_to_200': other_pairs,   # should be exactly [(37,36)] since 73 is prime
        'unique_pair': len(other_pairs) == 1,
        'v73': v73,
        'gcd_uv73': int(gcd_uv73),
        'pair_is_small': max(r73, s73) <= 12,   # M1/M2's own "small" ballpark (their smallest hits were ~2-30)
    }


# ===========================================================================
# SUDOKU-STYLE SANITY CHECKS (lightweight, matching M1/M2's own scope)
# ===========================================================================
def sanity_checks():
    results = []

    r3 = m3_band_spacing_check()
    results.append(('M3-S1: a(B1) equals lambda_evan(B1) exactly (both = hbar*c/Lambda_QCD, same formula)',
                     r3['a_equals_lambda_evan_B1']))
    results.append(('M3-S2: a(B2) equals lambda_evan(B2) exactly (both = hbar*c/m_W, same formula)',
                     r3['a_equals_lambda_evan_B2']))
    results.append(('M3-S3: solving lambda_moire=a for theta gives theta=60 deg (SymPy, exact)',
                     any(abs(float(d) - 60.0) < 1e-9 for d in r3['theta_deg_solutions'])))
    results.append(('M3-S4: theta solution is independent of the numeric value of a (residual=0)',
                     sp.simplify(r3['a_dependence_check_residual']) == 0))

    r4 = m4_winding_pythagorean_check()
    results.append(('M4-S1: r^2-s^2=N identity holds symbolically for GENERAL odd N (not just N=73)',
                     sp.simplify(r4['identity_residual_general_odd_N']) == 0))
    results.append(('M4-S2: r-s=1 identically (forces gcd(r,s)=1 for ANY odd N -- not special to 73)',
                     sp.simplify(r4['r_minus_s_general']) == 1))
    results.append(('M4-S3: 73 is prime (confirmed, not assumed)', r4['n73_is_prime']))
    results.append(('M4-S4: (37,36) is the UNIQUE integer pair for n=73 up to r=200 (prime -> forced)',
                     r4['unique_pair']))
    results.append(('M4-S5: the unique pair is NOT small by M1/M2\'s own standard (max(r,s) > 12)',
                     not r4['pair_is_small']))

    return results


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("M3/M4 Quick Checks -- Moire Band Spacing and Vortex Winding")
    print("=" * 78)

    print("\n--- M3: band spacing vs evanescent depth ---")
    r3 = m3_band_spacing_check()
    print(f"a(B1, C1/C2 boundary)      = {r3['a_B1_fm']:.4f} fm")
    print(f"lambda_evan(B1, Part 89)   = {r3['lambda_evan_B1_fm']:.4f} fm")
    print(f"a == lambda_evan(B1)?      = {r3['a_equals_lambda_evan_B1']}  (TRUE BY CONSTRUCTION, same formula)")
    print(f"a(B2, C2/C3 boundary)      = {r3['a_B2_fm']:.6f} fm")
    print(f"lambda_evan(B2, Part 89)   = {r3['lambda_evan_B2_fm']:.6f} fm")
    print(f"a == lambda_evan(B2)?      = {r3['a_equals_lambda_evan_B2']}  (TRUE BY CONSTRUCTION, same formula)")
    print(f"Solving lambda_moire=a for theta: {r3['theta_deg_solutions']} degrees")
    print(f"theta-independent-of-a residual: {r3['a_dependence_check_residual']}")
    print(f"Compare: Part 121's independently-derived SU(3) critical angle = {r3['part121_su3_angle_deg']} deg")

    print("\n--- M4: quark winding n=73 vs Pythagorean generator pair ---")
    r4 = m4_winding_pythagorean_check()
    print(f"General odd-N identity residual: {r4['identity_residual_general_odd_N']}")
    print(f"r-s (general): {r4['r_minus_s_general']}")
    print(f"73 is prime: {r4['n73_is_prime']}")
    print(f"(r,s) = ({r4['r73']}, {r4['s73']}), valid: {r4['check73_valid']}, gcd(r,s)={r4['gcd73']}")
    print(f"All (r,s) pairs found for n=73, r up to 200: {r4['all_pairs_found_up_to_200']}")
    print(f"Unique pair (forced by 73 being prime): {r4['unique_pair']}")
    print(f"v = 2rs = {r4['v73']}, gcd(u,v) = {r4['gcd_uv73']}")
    print(f"Is the pair 'small' (max<=12)?: {r4['pair_is_small']}")

    print("\n" + "=" * 78)
    print("SANITY CHECKS")
    print("=" * 78)
    checks = sanity_checks()
    n_pass = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    print(f"\nSCORE: {n_pass}/{len(checks)} PASS")


if __name__ == '__main__':
    main()

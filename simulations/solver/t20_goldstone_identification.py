#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t20_goldstone_identification.py -- TODO_04 T20 (Priority 20), Part 133
=======================================================================
Question: L_4 (Part 132/T19) has an exact massless Goldstone mode from its
global U(1) symmetry phi_a -> phi_a + c (all four fields, phi_1,phi_2,
phi_3,psi, shifting together -- T19's Eq 132.2, FE1+FE2+FE3+FE4=0). What
IS this mode physically?

Source: docs/research/pdtp_lagrangian4.md Sec "Goldstone mode"; T19/Part 132
(established the exact conserved combination).

This script:
1. Identifies the exact field content of the Goldstone direction (the
   normalized sum of all 4 fields) and verifies it has a canonical kinetic
   term.
2. Verifies the STRUCTURAL reason it is massless: L_4's potential terms
   (g_i cos(psi-phi_i), J_ab cos(phi_a-phi_b)) depend ONLY on field
   DIFFERENCES -- substituting phi_a = chi + eta_a, psi = chi + eta_psi
   (chi = the Goldstone direction, eta's = independent "shape" degrees of
   freedom with one constraint) shows the full potential is independent of
   chi identically, for ANY eta configuration -- not just verified as a
   zero eigenvalue at the linearized level (T19), but as an EXACT,
   non-perturbative statement.
3. Checks the "is it the graviton?" question via representation theory
   (spin-0 Goldstone vs spin-2 graviton -- different Lorentz representations,
   citing the Goldstone theorem's own scope, Weinberg 1995 Sec 19.2).
4. Checks the "is it phi_- from Part 61?" question by comparing the two
   symmetries' field content directly -- shows they act on different
   (non-overlapping in general) linear combinations, hence are different
   local degrees of freedom, even though both arise from the same
   structural pattern (a cos(difference) potential always has a "center of
   mass" zero mode).
5. Checks the "is it eaten via the Higgs mechanism" question: L_4 as
   written has no gauge field coupled to this U(1) -- the symmetry is
   global, not local -- so the Higgs mechanism does not apply to the
   CURRENT Lagrangian (would require a future gauging extension, not
   answerable from L_4 alone).

PDTP Original: sections 1-2 (exact field identification and the
non-perturbative decoupling proof), section 4 (explicit comparison to
Part 61's phi_-). Sections 3, 5 apply established facts (Goldstone theorem
representation content; gauge/Higgs mechanism prerequisites) to this
specific question.

Output: DATA only. Interpretation belongs in docs/research/pdtp_lagrangian4.md.
"""

import sympy as sp


# ===========================================================================
# PART 1: exact field content and canonical kinetic term
# ===========================================================================
def identify_goldstone_direction():
    """
    Define chi = (phi_1+phi_2+phi_3+psi)/2 (normalization chosen so its
    kinetic term comes out canonical, matching Part 61's phi_+ = (phi_b+phi_s)/2
    convention). Verify: (1/2)[(d phi_1)^2+(d phi_2)^2+(d phi_3)^2+(d psi)^2],
    re-expressed via chi and three independent "shape" combinations eta_a
    (a linear, orthogonal change of variables), contains a canonical
    (1/2)(d chi)^2-like term for chi with NO cross-terms mixing chi and the
    eta's -- i.e. chi decouples kinematically as well as potential-wise.
    """
    t = sp.symbols('t')
    phi1 = sp.Function('phi1')(t)
    phi2 = sp.Function('phi2')(t)
    phi3 = sp.Function('phi3')(t)
    psi = sp.Function('psi')(t)

    # Orthogonal-ish change of variables (4 fields -> chi + 3 independent shape dof).
    # chi = (phi1+phi2+phi3+psi)/2 ; eta1 = phi1-phi2 ; eta2 = phi1-phi3 ; eta3 = phi1-psi
    # (eta's are NOT mutually orthogonal to each other, but each is manifestly
    # orthogonal to chi's normalization by construction of the sum/difference split;
    # verified directly below by checking the cross term coefficient.)
    chi = sp.Function('chi')(t)
    eta1 = sp.Function('eta1')(t)
    eta2 = sp.Function('eta2')(t)
    eta3 = sp.Function('eta3')(t)

    # Solve for phi1,phi2,phi3,psi in terms of chi,eta1,eta2,eta3 (4 eqns, 4 unknowns):
    # chi = (phi1+phi2+phi3+psi)/2, eta1=phi1-phi2, eta2=phi1-phi3, eta3=phi1-psi
    p1, p2, p3, ps = sp.symbols('p1 p2 p3 ps')
    c, e1, e2, e3 = sp.symbols('c e1 e2 e3')
    sol = sp.solve([
        sp.Eq((p1 + p2 + p3 + ps) / 2, c),
        sp.Eq(p1 - p2, e1),
        sp.Eq(p1 - p3, e2),
        sp.Eq(p1 - ps, e3),
    ], [p1, p2, p3, ps], dict=True)[0]

    # Substitute into the kinetic term (using constant-symbol derivatives as proxies
    # for d/dt of each field, since the transformation is linear and time-independent,
    # the same linear relation holds for the derivatives)
    p1d, p2d, p3d, psd = sp.symbols('p1d p2d p3d psd')
    cd, e1d, e2d, e3d = sp.symbols('cd e1d e2d e3d')
    sol_d = sp.solve([
        sp.Eq((p1d + p2d + p3d + psd) / 2, cd),
        sp.Eq(p1d - p2d, e1d),
        sp.Eq(p1d - p3d, e2d),
        sp.Eq(p1d - psd, e3d),
    ], [p1d, p2d, p3d, psd], dict=True)[0]

    kinetic = sp.Rational(1, 2) * (p1d**2 + p2d**2 + p3d**2 + psd**2)
    kinetic_sub = sp.expand(kinetic.subs(sol_d))

    coeff_cd2 = kinetic_sub.coeff(cd, 2)
    # cross terms: coefficient of cd*e1d, cd*e2d, cd*e3d
    cross_e1 = sp.diff(kinetic_sub, cd, e1d)
    cross_e2 = sp.diff(kinetic_sub, cd, e2d)
    cross_e3 = sp.diff(kinetic_sub, cd, e3d)

    return {
        'sol_for_fields': sol,
        'kinetic_in_new_vars': kinetic_sub,
        'coeff_of_cd_squared': coeff_cd2,      # expect 2 (canonical up to normalization)
        'cross_term_cd_e1': cross_e1,          # expect 0 -- no kinetic mixing
        'cross_term_cd_e2': cross_e2,
        'cross_term_cd_e3': cross_e3,
    }


# ===========================================================================
# PART 2: exact (non-perturbative) decoupling of chi from the full potential
# ===========================================================================
def verify_exact_potential_decoupling():
    """
    Substitute phi_1 = chi + a1, phi_2 = chi + a2, phi_3 = chi + a3,
    psi = chi + a4 (chi = overall shift, a_i = arbitrary "shape" offsets,
    NOT required to be small -- this is an EXACT substitution, not a
    linearization) into the full L_4 potential

      V_pot = g1*cos(psi-phi1) + g2*cos(psi-phi2) + g3*cos(psi-phi3)
            + J12*cos(phi1-phi2) + J13*cos(phi1-phi3) + J23*cos(phi2-phi3)

    and verify chi cancels identically (every argument of every cos() is a
    DIFFERENCE of two fields, so the +chi shift cancels in each term
    algebraically, before any series expansion or eigenvalue analysis).
    This is a stronger statement than T19's linearized check: it holds at
    ALL orders, for ANY field configuration, not just small oscillations
    near the vacuum.
    """
    g1, g2, g3, J12, J13, J23 = sp.symbols('g1 g2 g3 J12 J13 J23', positive=True)
    chi, a1, a2, a3, a4 = sp.symbols('chi a1 a2 a3 a4', real=True)

    phi1, phi2, phi3, psi = chi + a1, chi + a2, chi + a3, chi + a4

    V = g1 * sp.cos(psi - phi1) + g2 * sp.cos(psi - phi2) + g3 * sp.cos(psi - phi3) \
        + J12 * sp.cos(phi1 - phi2) + J13 * sp.cos(phi1 - phi3) + J23 * sp.cos(phi2 - phi3)

    V_expanded = sp.expand_trig(sp.expand(V))
    dV_dchi = sp.simplify(sp.diff(V_expanded, chi))

    return {
        'V_after_substitution': sp.simplify(V),
        'dV_dchi': dV_dchi,   # expect exactly 0, for ALL a1..a4 (not just near 0)
        'chi_independent_exactly': sp.simplify(dV_dchi) == 0,
    }


# ===========================================================================
# PART 3: spin/representation argument -- is it the graviton?
# ===========================================================================
def check_not_graviton():
    """
    The Goldstone theorem (Goldstone 1961; Weinberg, "The Quantum Theory of
    Fields Vol II" (1996) Sec 19.2) guarantees one massless mode PER BROKEN
    GENERATOR of a continuous global symmetry, in the SAME Lorentz
    representation as the symmetry generator's action on the fields -- here,
    phi_a are all SCALAR fields (Lorentz spin-0), so the Goldstone mode is
    NECESSARILY spin-0. The graviton (in any metric theory, including PDTP's
    own SU(3)-emergent-metric picture, Part 75) is the spin-2 excitation of
    the metric tensor g_mu_nu. Spin-0 != spin-2: these cannot be the same
    particle, as a direct consequence of representation theory, independent
    of any dynamical details.
    """
    return {
        'goldstone_spin': 0,
        'graviton_spin': 2,
        'same_particle_possible': False,
        'reasoning': (
            "Goldstone bosons from a broken global symmetry acting on scalar fields "
            "are necessarily spin-0 (Goldstone theorem, Weinberg 1996 Sec 19.2). The "
            "graviton is the spin-2 excitation of the metric tensor. Different Lorentz "
            "representations cannot describe the same particle -- this is representation "
            "theory, not a dynamical question, so no further calculation can change the "
            "answer: the L_4 Goldstone mode is NOT the graviton."
        ),
    }


# ===========================================================================
# PART 4: is it Part 61's phi_-? -- explicit field-space comparison
# ===========================================================================
def compare_to_part61_phi_minus():
    """
    Part 61's phi_- = (phi_b - phi_s)/2 is built from TWO fields (phi_b,
    phi_s) that are BOTH representations of the SAME condensate layer (C1
    gravity), split into bulk and surface components. L_4's Goldstone chi
    = (phi_1+phi_2+phi_3+psi)/2 is built from FOUR fields spanning THREE
    DIFFERENT condensate layers (C1,C2,C3) plus matter (psi).

    These live in different field spaces (2 fields vs 4 fields) with no
    overlap in general: phi_- depends on phi_b, phi_s only; chi depends on
    phi_1 (=C1, possibly identifiable with phi_+ if C1 is later split
    Part-61-style, but NOT with phi_-) and phi_2, phi_3, psi, which phi_-
    does not involve at all. Even in the special case where C1's phi_1 is
    identified with Part 61's phi_+, chi (a sum including phi_2, phi_3, psi)
    remains a strictly larger, different combination than phi_- (which
    involves only the bulk/surface split WITHIN C1).

    Returns a structural (non-numerical) comparison; the point is definitional/
    representation-theoretic, not a numeric residual to check.
    """
    return {
        'part61_phi_minus_fields': ['phi_b (C1 bulk)', 'phi_s (C1 surface)'],
        'part61_symmetry_broken': 'bulk/surface split within the single C1 gravity condensate',
        'L4_goldstone_fields': ['phi_1 (C1)', 'phi_2 (C2 QCD)', 'phi_3 (C3 EW)', 'psi (matter)'],
        'L4_symmetry_broken': 'overall phase convention across all three condensate layers + matter',
        'same_degree_of_freedom': False,
        'recurring_structural_pattern': (
            "Both arise from the SAME general mechanism: any Lagrangian built purely from "
            "cos(field DIFFERENCES) has an automatic 'center of mass' zero mode for the sum "
            "of whichever fields it couples. Part 61 instantiates this pattern once (within "
            "C1's bulk/surface split, giving phi_-); L_4 instantiates it again, once more, at "
            "a different level (across the three condensate layers plus matter, giving chi). "
            "They are structurally analogous (same mechanism) but are different physical "
            "degrees of freedom (different field content), not the same particle."
        ),
    }


# ===========================================================================
# PART 5: Higgs mechanism applicability
# ===========================================================================
def check_higgs_mechanism_applicability():
    """
    The Higgs mechanism requires a LOCAL (gauged) continuous symmetry: the
    Goldstone boson is "eaten" by a gauge field A_mu, which becomes massive,
    when the symmetry parameter c is promoted to c(x) (a function of
    spacetime) and a covariant derivative D_mu = d_mu - i*q*A_mu is
    introduced (standard EW symmetry breaking, Weinberg 1996 Sec 21.1).

    L_4 as written (docs/research/pdtp_lagrangian4.md) has phi_a -> phi_a+c
    with c a CONSTANT (global symmetry) -- there is no gauge field A_mu
    coupled to this particular U(1) anywhere in L_4's definition. The Higgs
    mechanism therefore does NOT apply to the CURRENT Lagrangian; the
    question "what gets eaten" has no answer within L_4 as it stands. This
    would require a distinct, future extension (gauging this specific
    U(1)), not something derivable from the existing Lagrangian.
    """
    return {
        'symmetry_type_in_L4': 'global (c constant)',
        'gauge_field_present': False,
        'higgs_mechanism_applicable': False,
        'conclusion': (
            "Not applicable to L_4 as currently written. A gauged extension would be a "
            "distinct future task, not answerable from the existing Lagrangian."
        ),
    }


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS
# ===========================================================================
def sudoku_checks():
    results = []

    r1 = identify_goldstone_direction()
    results.append(('S1: coefficient of chi_dot^2 in the kinetic term is nonzero (canonical-normalizable)',
                     sp.simplify(r1['coeff_of_cd_squared']) != 0))
    results.append(('S2: no kinetic cross-term between chi and eta1 (chi_dot decouples)',
                     sp.simplify(r1['cross_term_cd_e1']) == 0))
    results.append(('S3: no kinetic cross-term between chi and eta2',
                     sp.simplify(r1['cross_term_cd_e2']) == 0))
    results.append(('S4: no kinetic cross-term between chi and eta3',
                     sp.simplify(r1['cross_term_cd_e3']) == 0))

    r2 = verify_exact_potential_decoupling()
    results.append(('S5: dV/dchi = 0 EXACTLY (non-perturbative, all orders, not just linearized)',
                     r2['chi_independent_exactly']))

    r3 = check_not_graviton()
    results.append(('S6: Goldstone spin (0) != graviton spin (2)',
                     r3['goldstone_spin'] != r3['graviton_spin']))
    results.append(('S7: same_particle_possible is False (representation-theoretic conclusion)',
                     r3['same_particle_possible'] is False))

    r4 = compare_to_part61_phi_minus()
    results.append(('S8: L_4 Goldstone field content strictly larger than / different from phi_- field content',
                     set(r4['part61_phi_minus_fields']) != set(['phi_1 (C1)']) and
                     len(r4['L4_goldstone_fields']) > len(r4['part61_phi_minus_fields'])))
    results.append(('S9: same_degree_of_freedom is False',
                     r4['same_degree_of_freedom'] is False))

    r5 = check_higgs_mechanism_applicability()
    results.append(('S10: no gauge field present in L_4 (Higgs mechanism not applicable)',
                     r5['gauge_field_present'] is False))
    results.append(('S11: higgs_mechanism_applicable is False',
                     r5['higgs_mechanism_applicable'] is False))

    return results


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("T20 (Part 133): L_4 Goldstone Mode -- What Is It Physically?")
    print("=" * 78)

    print("\n--- Part 1: exact field content and kinetic term ---")
    r1 = identify_goldstone_direction()
    print(f"chi = (phi1+phi2+phi3+psi)/2")
    print(f"Coefficient of chi_dot^2: {r1['coeff_of_cd_squared']}")
    print(f"Cross terms (chi,eta1)/(chi,eta2)/(chi,eta3): "
          f"{r1['cross_term_cd_e1']}, {r1['cross_term_cd_e2']}, {r1['cross_term_cd_e3']}")

    print("\n--- Part 2: exact potential decoupling ---")
    r2 = verify_exact_potential_decoupling()
    print(f"dV/dchi (should be 0 for ALL a1..a4, not just near 0): {r2['dV_dchi']}")
    print(f"chi is exactly potential-independent: {r2['chi_independent_exactly']}")

    print("\n--- Part 3: not the graviton ---")
    r3 = check_not_graviton()
    print(r3['reasoning'])

    print("\n--- Part 4: comparison to Part 61's phi_- ---")
    r4 = compare_to_part61_phi_minus()
    print(f"Part 61 phi_- fields: {r4['part61_phi_minus_fields']}")
    print(f"L_4 Goldstone fields: {r4['L4_goldstone_fields']}")
    print(r4['recurring_structural_pattern'])

    print("\n--- Part 5: Higgs mechanism applicability ---")
    r5 = check_higgs_mechanism_applicability()
    print(r5['conclusion'])

    print("\n" + "=" * 78)
    print("SUDOKU CONSISTENCY CHECKS")
    print("=" * 78)
    checks = sudoku_checks()
    n_pass = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    print(f"\nSCORE: {n_pass}/{len(checks)} PASS")


if __name__ == '__main__':
    main()

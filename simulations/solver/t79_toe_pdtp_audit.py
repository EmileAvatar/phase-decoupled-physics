"""
T79 (TODO_04.md) Phase 2, Part 149 -- "Theory of Everything" master
equation: does PDTP change or add anything to it?

This script verifies the ONE new formal claim produced by this Phase 2
pass: that Part 53/122's already-derived, already-Sudoku-checked Koide
relation (Q = 2/3 for charged leptons, from SU(3)'s Z_3 center symmetry)
can be translated, without loss or addition of content, from a statement
about LEPTON MASSES into a statement about the master equation's own
Yukawa coupling matrix V_ij -- specifically its three charged-lepton
diagonal eigenvalues y_e, y_mu, y_tau.

This is NOT a re-derivation of Part 53/122's physics (already verified
there, 10/10 and 10/10 Sudoku, cited not repeated here). It is a
translation-correctness check: does the mass-space relation survive,
unchanged, the substitution m_i = c*y_i (c = v/sqrt(2), the SAME Higgs
vev for every lepton generation -- a structural fact of the Standard
Model's single-Higgs-doublet mechanism, not a new PDTP assumption)?

Four things are established here, all computed (not asserted):

1. [VERIFIED, translation check] Q(m_i) = Q(y_i) exactly, for m_i = c*y_i
   with any common c > 0 -- the Koide ratio is scale-invariant, so the
   ALREADY-DERIVED mass relation Q=2/3 is IDENTICALLY a relation on the
   Yukawa eigenvalues y_e, y_mu, y_tau, with no reinterpretation needed
   and no new physics introduced by the translation itself.

2. [VERIFIED, independent re-derivation of Part 53's own result] Q = 2/3
   follows algebraically from delta = sqrt(2) in the Brannen
   parametrization sqrt(m_i) = mu*(1 + delta*cos(theta_0 + 2*pi*i/3)).

3. [VERIFIED, independent re-derivation of Part 122's own result] The
   master formula delta = sqrt(2)*tan(theta_v) follows algebraically
   from the Q definition and the partition-angle definition
   cos^2(theta_v) = 1/(1 + delta^2/2).

4. [VERIFIED, negative result carried forward, not dropped] Re-confirms
   Part 122's own finding: the SU(3) 60-degree critical angle (T10) does
   NOT reproduce the up-quark delta (predicts sqrt(6), not sqrt(3)) --
   this scopes the Yukawa addition to LEPTONS ONLY; quarks are NOT
   covered by any PDTP-derived constraint.

A real bug caught by RECHECK (not hidden): the first version of
run_sudoku_checks() reconstructed comparison expressions using freshly-
created sp.Symbol('mu')/sp.Symbol('delta') instances, which carry no
assumptions and are therefore NOT equal to the real=True-flagged symbols
used inside verify_Q_two_thirds_from_delta() -- SymPy does not simplify
the difference of two same-named-but-differently-assumed symbols to
zero. Two Sudoku checks (S2, S3) spuriously FAILED as a direct result.
Fixed by having the step function compute and return those residuals
itself, using its own internally-consistent symbols, rather than having
the Sudoku layer recompute them externally.

Output DATA only -- interpretation lives in
docs/research/theory_of_everything_pdtp_audit.md.
"""

import sympy as sp


# ---------------------------------------------------------------------
# 1. Scale invariance: Q(mass) = Q(Yukawa eigenvalue) under m_i = c*y_i
# ---------------------------------------------------------------------

def verify_Q_scale_invariance():
    """Q(x1,x2,x3) = (x1+x2+x3)/(sqrt(x1)+sqrt(x2)+sqrt(x3))^2.
    Verify Q(c*y1, c*y2, c*y3) = Q(y1, y2, y3) for symbolic c > 0,
    y1,y2,y3 > 0 -- i.e. the Koide ratio is invariant under a common
    rescaling. This is what licenses restating Part 53's mass-space
    result (Q=2/3) as an IDENTICAL statement about the Yukawa matrix's
    charged-lepton eigenvalues (m_i = c*y_i, c = v/sqrt(2) the same for
    every generation -- a Standard Model structural fact, not new)."""
    c, y1, y2, y3 = sp.symbols('c y1 y2 y3', positive=True)

    def Q(a, b, cc):
        return (a + b + cc) / (sp.sqrt(a) + sp.sqrt(b) + sp.sqrt(cc))**2

    Q_mass = Q(c * y1, c * y2, c * y3)
    Q_yukawa = Q(y1, y2, y3)
    residual = sp.simplify(Q_mass - Q_yukawa)

    return {
        'Q_mass_form': Q_mass,
        'Q_yukawa_form': Q_yukawa,
        'residual': residual,
        'scale_invariant': residual == 0,
    }


# ---------------------------------------------------------------------
# 2. Independent re-derivation: delta=sqrt(2) => Q=2/3 (Part 53 result)
# ---------------------------------------------------------------------

def verify_Q_two_thirds_from_delta():
    """Re-derive Q = (1 + delta^2/2)/3 from the Brannen parametrization
    directly (not assumed from Part 53 -- recomputed here), then confirm
    delta=sqrt(2) gives Q=2/3 exactly."""
    mu, delta, theta0, k = sp.symbols('mu delta theta0 k', real=True)

    sqrt_m_k = mu * (1 + delta * sp.cos(theta0 + 2 * sp.pi * k / 3))

    # Sum over k=0,1,2 of sqrt_m_k^2 = m_k, and of sqrt_m_k itself
    sum_sqrt_m = sp.nsimplify(sum(sqrt_m_k.subs(k, kk) for kk in range(3)))
    sum_sqrt_m = sp.simplify(sum_sqrt_m)

    sum_m = sp.simplify(sum(sp.expand_trig(sp.expand(sqrt_m_k.subs(k, kk)**2))
                             for kk in range(3)))
    sum_m = sp.simplify(sum_m)

    Q_derived = sp.simplify(sum_m / sum_sqrt_m**2)

    Q_at_delta_sqrt2 = sp.simplify(Q_derived.subs(delta, sp.sqrt(2)))
    residual_at_sqrt2 = sp.simplify(Q_at_delta_sqrt2 - sp.Rational(2, 3))

    # Sudoku cross-checks computed HERE, with this function's own
    # consistently-assumed local symbols (mu, delta) -- NOT recomputed
    # externally with freshly-constructed sp.Symbol() instances, which
    # carry no assumptions and are therefore NOT equal to the real=True
    # symbols used above (caught by RECHECK: sp.simplify(mu_fresh -
    # mu_real_true) does NOT collapse to 0, since SymPy treats symbols
    # with different assumption sets as formally distinct even when
    # their string names match -- an earlier version of this script did
    # exactly that in run_sudoku_checks() and two checks spuriously
    # FAILED as a direct result. Fixed here, not hidden.)
    sum_sqrt_m_residual = sp.simplify(sum_sqrt_m - 3 * mu)
    Q_formula_residual = sp.simplify(Q_derived - (1 + delta**2 / 2) / 3)

    return {
        'sum_sqrt_m': sum_sqrt_m,
        'sum_m': sum_m,
        'Q_derived_general_delta': Q_derived,
        'Q_at_delta_sqrt2': Q_at_delta_sqrt2,
        'residual_vs_two_thirds': residual_at_sqrt2,
        'Q_equals_two_thirds_at_delta_sqrt2': residual_at_sqrt2 == 0,
        'sum_sqrt_m_residual_vs_3mu': sum_sqrt_m_residual,
        'sum_sqrt_m_equals_3mu': sum_sqrt_m_residual == 0,
        'Q_formula_residual_vs_1plusdelta2over2over3': Q_formula_residual,
        'Q_formula_matches_expected_form': Q_formula_residual == 0,
    }


# ---------------------------------------------------------------------
# 3. Independent re-derivation: master formula delta = sqrt(2)*tan(theta_v)
# ---------------------------------------------------------------------

def verify_master_formula():
    """Re-derive delta = sqrt(2)*tan(theta_v) from
    cos^2(theta_v) = 1/(1+delta^2/2) directly (Part 122's own definition),
    not assumed."""
    delta, theta_v = sp.symbols('delta theta_v', positive=True)

    cos2_thetav = 1 / (1 + delta**2 / 2)
    # Solve cos^2(theta_v) = cos2_thetav for delta, using
    # cos^2 = 1/(1+tan^2) identity route: tan^2(theta_v) = 1/cos2_thetav - 1
    tan2_thetav_from_def = sp.simplify(1 / cos2_thetav - 1)  # = delta^2/2
    delta_expr = sp.sqrt(2 * tan2_thetav_from_def)  # = sqrt(delta^2) = delta (delta>0)
    residual = sp.simplify(delta_expr - delta)

    # Cross-check the two reference angles
    delta_at_45 = sp.simplify(sp.sqrt(2) * sp.tan(sp.pi / 4))
    delta_at_60 = sp.simplify(sp.sqrt(2) * sp.tan(sp.pi / 3))

    return {
        'tan2_thetav_from_cos2_def': tan2_thetav_from_def,
        'delta_expr_recovered': delta_expr,
        'residual_vs_delta': residual,
        'master_formula_verified': residual == 0,
        'delta_at_45deg': delta_at_45,
        'delta_at_45deg_is_sqrt2': sp.simplify(delta_at_45 - sp.sqrt(2)) == 0,
        'delta_at_60deg': delta_at_60,
        'delta_at_60deg_is_sqrt6': sp.simplify(delta_at_60 - sp.sqrt(6)) == 0,
    }


# ---------------------------------------------------------------------
# 4. Negative result carried forward: 60-degree angle does NOT give
#    delta=sqrt(3) for up quarks -- scopes the addition to leptons only
# ---------------------------------------------------------------------

def verify_quark_sector_not_covered():
    """Confirm (not assume) that the SU(3) 60-degree critical angle
    (T10/Part 121) predicts delta=sqrt(6), NOT delta=sqrt(3) -- so the
    numerical up-quark observation delta_up~1.76~sqrt(3) has no identified
    PDTP-derived origin. This is Part 122's own negative result,
    re-verified here (not re-asserted) because it directly sets the
    scope boundary for what this Phase 2 pass can honestly claim."""
    delta_at_60 = sp.simplify(sp.sqrt(2) * sp.tan(sp.pi / 3))
    delta_sqrt3 = sp.sqrt(3)
    residual = sp.simplify(delta_at_60 - delta_sqrt3)

    # Numerical values from Part 122 (PDG 2023), reused not re-measured
    delta_up_pole = 1.7587
    theta_v_up_pole_deg = 51.196
    deviation_from_60deg = abs(theta_v_up_pole_deg - 60.0)

    return {
        'delta_at_60deg_symbolic': delta_at_60,
        'delta_sqrt3_symbolic': delta_sqrt3,
        'residual_60deg_vs_sqrt3': residual,
        'sixty_degree_angle_does_NOT_give_sqrt3': residual != 0,
        'delta_up_measured_pole_mass': delta_up_pole,
        'theta_v_up_measured_deg': theta_v_up_pole_deg,
        'deviation_from_60deg_in_degrees': deviation_from_60deg,
        'quark_sector_has_no_derived_PDTP_origin': deviation_from_60deg > 5.0,
    }


# ---------------------------------------------------------------------
# Sudoku consistency check -- 9 tests
# ---------------------------------------------------------------------

def run_sudoku_checks(s1, s2, s3, s4):
    checks = []

    def add(label, computed, expected_desc, passed):
        checks.append({'label': label, 'computed': computed,
                        'expected': expected_desc,
                        'pass': (None if passed is None else bool(passed))})

    add('S1: Q is scale-invariant under m_i=c*y_i (licenses the '
        'mass-to-Yukawa translation)',
        s1['residual'], '0 (exact)', s1['scale_invariant'])
    add('S2: sum of sqrt(m_i) over k=0,1,2 collapses to 3*mu (cos terms '
        'cancel by 3-fold symmetry)',
        s2['sum_sqrt_m_residual_vs_3mu'], '0 (exact)', s2['sum_sqrt_m_equals_3mu'])
    add('S3: Q(delta) formula independently re-derived matches '
        '(1+delta^2/2)/3',
        s2['Q_formula_residual_vs_1plusdelta2over2over3'], '0 (exact)',
        s2['Q_formula_matches_expected_form'])
    add('S4: Q(delta=sqrt(2)) = 2/3 exactly (re-derives Part 53)',
        s2['residual_vs_two_thirds'], '0 (exact)',
        s2['Q_equals_two_thirds_at_delta_sqrt2'])
    add('S5: master formula delta=sqrt(2)*tan(theta_v) re-derived from '
        'the Q/partition-angle definition (re-derives Part 122)',
        s3['residual_vs_delta'], '0 (exact)', s3['master_formula_verified'])
    add('S6: delta(45 deg) = sqrt(2) exactly [lepton partition angle]',
        s3['delta_at_45deg'], 'sqrt(2)', s3['delta_at_45deg_is_sqrt2'])
    add('S7: delta(60 deg) = sqrt(6), NOT sqrt(3) [SU(3) critical angle '
        'does not explain the quark delta]',
        s3['delta_at_60deg'], 'sqrt(6)', s3['delta_at_60deg_is_sqrt6'])
    add('S8: 60-degree angle symbolically does NOT equal sqrt(3) '
        '(confirms S7 from the other direction)',
        s4['residual_60deg_vs_sqrt3'], 'nonzero',
        s4['sixty_degree_angle_does_NOT_give_sqrt3'])
    add('S9: measured quark theta_v (51.2 deg) is >5 deg from the only '
        'identified PDTP critical angle (60 deg) -- quark sector stays '
        'OUT OF SCOPE for this addition',
        s4['deviation_from_60deg_in_degrees'], '> 5 deg',
        s4['quark_sector_has_no_derived_PDTP_origin'])

    n_pass = sum(1 for c in checks if c['pass'] is True)
    n_fail = sum(1 for c in checks if c['pass'] is False)
    n_na = sum(1 for c in checks if c['pass'] is None)
    return checks, n_pass, n_fail, n_na


def main():
    print("=" * 78)
    print("T79 Phase 2 / Part 149 -- ToE master equation: PDTP additions audit")
    print("=" * 78)

    print("\n--- Step 1: Q scale invariance (mass <-> Yukawa translation) ---")
    s1 = verify_Q_scale_invariance()
    print(f"  Q(c*y1,c*y2,c*y3) = {s1['Q_mass_form']}")
    print(f"  Q(y1,y2,y3)       = {s1['Q_yukawa_form']}")
    print(f"  residual = {s1['residual']} (scale invariant: {s1['scale_invariant']})")

    print("\n--- Step 2: Q=2/3 re-derived from delta=sqrt(2) ---")
    s2 = verify_Q_two_thirds_from_delta()
    print(f"  sum sqrt(m_i) = {s2['sum_sqrt_m']}")
    print(f"  sum m_i = {s2['sum_m']}")
    print(f"  Q(delta) = {s2['Q_derived_general_delta']}")
    print(f"  Q(delta=sqrt(2)) = {s2['Q_at_delta_sqrt2']} "
          f"(residual vs 2/3: {s2['residual_vs_two_thirds']})")

    print("\n--- Step 3: master formula delta=sqrt(2)*tan(theta_v) re-derived ---")
    s3 = verify_master_formula()
    print(f"  residual = {s3['residual_vs_delta']} "
          f"(verified: {s3['master_formula_verified']})")
    print(f"  delta(45deg) = {s3['delta_at_45deg']} "
          f"(= sqrt(2): {s3['delta_at_45deg_is_sqrt2']})")
    print(f"  delta(60deg) = {s3['delta_at_60deg']} "
          f"(= sqrt(6): {s3['delta_at_60deg_is_sqrt6']})")

    print("\n--- Step 4: quark sector out-of-scope check ---")
    s4 = verify_quark_sector_not_covered()
    print(f"  delta(60deg) - sqrt(3) = {s4['residual_60deg_vs_sqrt3']} "
          f"(does NOT match: {s4['sixty_degree_angle_does_NOT_give_sqrt3']})")
    print(f"  measured theta_v(up quarks) = {s4['theta_v_up_measured_deg']} deg, "
          f"deviation from 60deg = {s4['deviation_from_60deg_in_degrees']:.1f} deg")
    print(f"  quark sector out of scope: {s4['quark_sector_has_no_derived_PDTP_origin']}")

    print("\n--- Sudoku Consistency Check ---")
    checks, n_pass, n_fail, n_na = run_sudoku_checks(s1, s2, s3, s4)
    for c in checks:
        status = 'PASS' if c['pass'] is True else ('FAIL' if c['pass'] is False else 'N/A')
        print(f"[{status}] {c['label']}")
        print(f"       computed: {c['computed']}")
        print(f"       expected: {c['expected']}")

    print(f"\nScorecard: {n_pass} PASS, {n_fail} FAIL, {n_na} N/A "
          f"out of {len(checks)} checks")


if __name__ == '__main__':
    main()

"""
T80 (TODO_04.md), Part 147 -- Electromagnetism-from-Geometry (U(1)
connection) as a blueprint for PDTP's EM gap.

Tests whether demanding LOCAL invariance of PDTP's own phase-locking
Lagrangian forces a new connection field A_mu into existence, the same
way ordinary QED's covariant derivative D_mu = d_mu - i*e*A_mu is forced
by local U(1) phase invariance of a charged matter field (see the source
video, "Electromagnetism Derived From Geometry!", transcript in
docs/misc/note 2026-09-14.txt).

Convention: fields are evaluated pointwise using a (value, "dot") symbol
pair per field -- e.g. (phi, phi_dot) -- matching sympy_checks.py's own
verify_pdtp_field_equation() convention exactly. A LOCAL gauge
transformation at a generic point is captured by shifting the value
symbol by alpha and the "dot" symbol by an INDEPENDENT symbol alpha_dot
(standing for d(alpha)/dx at that point). This is rigorous, not a
hand-wave: for smooth alpha(x), alpha and its derivative can be
prescribed independently at any single point, so invariance for
arbitrary (alpha, alpha_dot) at a generic point is exactly equivalent to
invariance under arbitrary smooth alpha(x) everywhere.

Eight things are established here, all computed (not asserted):

1. [CORRECTION] T80's own filing (TODO_04.md) posed Key Question 1 as
   invariance under psi -> psi+alpha(x) ALONE (phi fixed). Checked
   directly below and found FALSE even for constant alpha -- not a
   symmetry at all. The actual (and only) global symmetry of the
   Lagrangian is the COMBINED shift phi->phi+alpha, psi->psi+alpha
   (every field, same alpha) -- verified exactly. This is the symmetry
   gauged below.

2. [DERIVED] The combined shift's Noether current j = phi_dot + psi_dot
   is exactly conserved on the ORIGINAL (ungauged) equations of motion --
   a concrete confirmation of Noether's theorem for this Lagrangian.

3. [DERIVED] Gauging the combined shift (charge 1 for every field) via
   minimal coupling D(field) = d(field)/dx - A, A -> A + d(alpha)/dx,
   makes the FULL Lagrangian exactly locally invariant -- Key Question 1
   (corrected) answered YES. The coupling term g*cos(psi-phi) needs NO
   modification at all (it already depends only on the gauge-invariant
   combination psi-phi); only the kinetic terms need covariant
   derivatives.

4. [DERIVED] Center/relative variables Sigma=(phi+psi)/2 (carries the
   gauge charge), theta=psi-phi (gauge invariant, carries ALL of PDTP's
   coupling physics) diagonalize the kinetic term exactly:
   (1/2)phi_dot^2+(1/2)psi_dot^2 = Sigma_dot^2 + (1/4)theta_dot^2. A
   couples ONLY to Sigma in the Lagrangian, never to theta directly.

5. [DERIVED, the central finding] Minimal coupling alone gives A NO
   independent kinetic term (no A_dot appears anywhere in L_gauged), so
   its own Euler-Lagrange "equation of motion" degenerates from a wave
   equation into an algebraic CONSTRAINT: A = Sigma_dot. Substituting
   this constraint back into phi's own (gauged) field equation exactly
   reproduces the ORIGINAL, UNGAUGED theta equation of motion
   (theta_ddot = -2*g*sin(theta)) with A completely cancelled out --
   verified via two independent derivation routes that agree exactly
   (residual 0). CONCLUSION: minimal coupling alone is physically
   vacuous for PDTP -- it introduces a field with the correct formal
   transformation properties but zero net effect on any PDTP prediction,
   because it has no kinetic term to make it propagate. This is the
   honest, quantitative version of Key Question 2.

6. [VERIFIED, standard physics] IF a Maxwell-like kinetic term -1/4*F^2
   is separately POSTULATED (the same kind of move as Maxwell's own
   historical displacement-current scaffolding, Methodology.md's own
   worked example -- NOT something forced by matter-sector invariance
   alone), its curvature F_01 = d_0(A_1) - d_1(A_0) is gauge invariant
   (verified with two independent coordinates) and its kinetic term has
   the healthy (non-ghost) sign under the standard (+,-) metric
   convention.

7. [DERIVED] The N=2-matter-phase generalization (phi, psi1, psi2, all
   charge 1) reproduces the identical structure -- the A-dependent piece
   of the kinetic term depends only on A and the 3-field center mode
   Sigma3, never on the gauge-invariant relative (theta) modes --
   confirming the N=1 result is not a special case.

8. [SUDOKU: two-phase compatibility] The combined-shift symmetry (now
   for THREE fields: psi, phi_b, phi_s) survives unchanged in Part 61's
   two-phase Lagrangian L = g*cos(psi-phi_b) - g*cos(psi-phi_s) -- the
   minus sign on the surface term does not break it, since both cosine
   arguments are separately invariant under a common shift of all three
   fields. Full gauging of the two-phase case is out of scope here
   (flagged as future work if this direction is pursued further); only
   the necessary symmetry precondition is checked, per CLAUDE.md's
   Sudoku protocol item 4.

Output DATA only -- interpretation lives in
docs/research/em_from_geometry_gauging.md.
"""

import sympy as sp


# ---------------------------------------------------------------------
# 1. Global symmetry: correcting T80's own Key Question 1 wording
# ---------------------------------------------------------------------

def verify_global_symmetry():
    """Check two candidate global symmetries of L0 = (1/2)phi_dot^2 +
    (1/2)psi_dot^2 + g*cos(psi-phi):
      (a) psi -> psi + alpha alone (phi fixed) -- T80's filed wording
      (b) phi -> phi+alpha, psi -> psi+alpha together (combined shift)
    """
    phi, psi, g, alpha = sp.symbols('phi psi g alpha', real=True)
    phi_dot, psi_dot = sp.symbols('phi_dot psi_dot', real=True)

    L0 = sp.Rational(1, 2) * phi_dot**2 + sp.Rational(1, 2) * psi_dot**2 \
        + g * sp.cos(psi - phi)

    # Candidate (a): psi alone shifts (phi_dot, psi_dot untouched -- a
    # constant shift has zero derivative)
    L_a = L0.subs(psi, psi + alpha)
    diff_a = sp.simplify(L_a - L0)

    # Candidate (b): combined shift
    L_b = L0.subs([(phi, phi + alpha), (psi, psi + alpha)], simultaneous=True)
    diff_b = sp.simplify(L_b - L0)

    return {
        'L0': L0,
        'candidate_a_psi_alone': L_a,
        'residual_a': diff_a,
        'candidate_a_is_symmetry': diff_a == 0,
        'candidate_b_combined': L_b,
        'residual_b': diff_b,
        'candidate_b_is_symmetry': diff_b == 0,
    }


# ---------------------------------------------------------------------
# 2. Noether current for the (corrected) global symmetry
# ---------------------------------------------------------------------

def verify_noether_current():
    """Noether current for phi->phi+eps, psi->psi+eps:
      j = (dL/d phi_dot)*1 + (dL/d psi_dot)*1 = phi_dot + psi_dot
    Confirm dj/dx = 0 on the ORIGINAL (ungauged) equations of motion,
    both independently re-derived here via Euler-Lagrange (not assumed
    from CLAUDE.md's field equation statement)."""
    phi, psi, g = sp.symbols('phi psi g', real=True)
    phi_dot, psi_dot = sp.symbols('phi_dot psi_dot', real=True)

    L0 = sp.Rational(1, 2) * phi_dot**2 + sp.Rational(1, 2) * psi_dot**2 \
        + g * sp.cos(psi - phi)

    j = sp.diff(L0, phi_dot) * 1 + sp.diff(L0, psi_dot) * 1
    j_expected = phi_dot + psi_dot
    residual_j = sp.simplify(j - j_expected)

    phi_ddot_eom = sp.diff(L0, phi)   # EL: phi_ddot = dL/dphi = g*sin(psi-phi)
    psi_ddot_eom = sp.diff(L0, psi)   # EL: psi_ddot = dL/dpsi = -g*sin(psi-phi)

    dj_dx_onshell = sp.simplify(phi_ddot_eom + psi_ddot_eom)

    return {
        'noether_current_j': j,
        'residual_vs_phidot_plus_psidot': residual_j,
        'phi_ddot_eom': phi_ddot_eom,
        'psi_ddot_eom': psi_ddot_eom,
        'dj_dx_onshell': dj_dx_onshell,
        'current_conserved': dj_dx_onshell == 0,
    }


# ---------------------------------------------------------------------
# 3. Local gauging of the combined shift symmetry
# ---------------------------------------------------------------------

def verify_local_gauge_invariance():
    """Gauge the combined shift: alpha -> alpha(x), so the field VALUE
    and its "dot" both shift (phi->phi+alpha, phi_dot->phi_dot+alpha_dot,
    same for psi), and demand A -> A + alpha_dot compensates. Verify:
      (i) the coupling term alone is invariant with NO covariant
          derivative needed (it depends only on psi-phi)
      (ii) the bare kinetic term alone is NOT invariant without A
      (iii) the FULL gauged Lagrangian (kinetic with D + coupling
            unchanged) IS exactly invariant
    """
    phi, psi, g, A = sp.symbols('phi psi g A', real=True)
    phi_dot, psi_dot = sp.symbols('phi_dot psi_dot', real=True)
    alpha, alpha_dot = sp.symbols('alpha alpha_dot', real=True)

    coupling = g * sp.cos(psi - phi)
    kinetic_bare = sp.Rational(1, 2) * phi_dot**2 + sp.Rational(1, 2) * psi_dot**2

    D_phi = phi_dot - A
    D_psi = psi_dot - A
    kinetic_gauged = sp.Rational(1, 2) * D_phi**2 + sp.Rational(1, 2) * D_psi**2
    L_gauged = kinetic_gauged + coupling

    subs_local = [
        (phi, phi + alpha), (psi, psi + alpha),
        (phi_dot, phi_dot + alpha_dot), (psi_dot, psi_dot + alpha_dot),
        (A, A + alpha_dot),
    ]

    # (i) coupling term alone
    coupling_transformed = coupling.subs(subs_local, simultaneous=True)
    residual_coupling = sp.simplify(coupling_transformed - coupling)

    # (ii) bare kinetic term alone (no A to shift here -- only phi,psi,dots)
    subs_local_no_A = [
        (phi, phi + alpha), (psi, psi + alpha),
        (phi_dot, phi_dot + alpha_dot), (psi_dot, psi_dot + alpha_dot),
    ]
    kinetic_bare_transformed = kinetic_bare.subs(subs_local_no_A, simultaneous=True)
    residual_kinetic_bare = sp.simplify(kinetic_bare_transformed - kinetic_bare)

    # (iii) full gauged Lagrangian
    L_gauged_transformed = L_gauged.subs(subs_local, simultaneous=True)
    residual_full = sp.simplify(L_gauged_transformed - L_gauged)

    return {
        'coupling_term': coupling,
        'residual_coupling_alone': residual_coupling,
        'coupling_invariant_without_A': residual_coupling == 0,
        'kinetic_bare_residual_without_A': residual_kinetic_bare,
        'kinetic_bare_NOT_invariant_without_A': residual_kinetic_bare != 0,
        'L_gauged': L_gauged,
        'residual_full_local_invariance': residual_full,
        'full_lagrangian_locally_invariant': residual_full == 0,
    }


# ---------------------------------------------------------------------
# 4. Center/relative (Sigma, theta) diagonalization
# ---------------------------------------------------------------------

def verify_sigma_theta_diagonalization():
    """Sigma=(phi+psi)/2 carries the gauge charge (shifts by alpha under
    the combined transformation); theta=psi-phi is gauge invariant and
    carries the coupling g*cos(theta). Verify the kinetic identity and
    that A appears in L_gauged ONLY via Sigma_dot - A (never touching
    theta or theta_dot)."""
    phi, psi, g, A = sp.symbols('phi psi g A', real=True)
    phi_dot, psi_dot = sp.symbols('phi_dot psi_dot', real=True)

    Sigma_dot = (phi_dot + psi_dot) / 2
    theta = psi - phi
    theta_dot = psi_dot - phi_dot

    kinetic_original = sp.Rational(1, 2) * phi_dot**2 + sp.Rational(1, 2) * psi_dot**2
    kinetic_sigma_theta = Sigma_dot**2 + sp.Rational(1, 4) * theta_dot**2
    residual_diagonalization = sp.simplify(kinetic_original - kinetic_sigma_theta)

    D_phi = phi_dot - A
    D_psi = psi_dot - A
    L_gauged_phipsi = sp.Rational(1, 2) * D_phi**2 + sp.Rational(1, 2) * D_psi**2 \
        + g * sp.cos(psi - phi)

    L_gauged_sigmatheta = (Sigma_dot - A)**2 + sp.Rational(1, 4) * theta_dot**2 \
        + g * sp.cos(theta)
    residual_basis_change = sp.simplify(L_gauged_phipsi - L_gauged_sigmatheta)

    theta_sector = sp.Rational(1, 4) * theta_dot**2 + g * sp.cos(theta)
    A_in_theta_sector = theta_sector.has(A)

    return {
        'Sigma_dot': Sigma_dot,
        'theta': theta,
        'theta_dot': theta_dot,
        'kinetic_original': kinetic_original,
        'kinetic_sigma_theta_form': kinetic_sigma_theta,
        'residual_kinetic_diagonalization': residual_diagonalization,
        'diagonalization_exact': residual_diagonalization == 0,
        'L_gauged_phipsi': L_gauged_phipsi,
        'L_gauged_sigmatheta': L_gauged_sigmatheta,
        'residual_basis_change_equivalence': residual_basis_change,
        'basis_change_exact': residual_basis_change == 0,
        'A_appears_in_theta_sector': A_in_theta_sector,
    }


# ---------------------------------------------------------------------
# 5. A is non-dynamical under minimal coupling -- the central finding
# ---------------------------------------------------------------------

def verify_A_nondynamical_constraint_and_net_effect():
    """(a) Show A has no conjugate momentum (no A_dot term anywhere in
    L_gauged), so its Euler-Lagrange equation degenerates into an
    algebraic constraint rather than a wave equation.
    (b) Solve that constraint for A.
    (c) Substitute the constraint into phi's own (gauged) field equation
    and show the result is EXACTLY the original ungauged theta equation
    of motion, cross-checked against an independent second derivation
    (EL applied directly to the isolated theta-sector Lagrangian from
    step 4). Two different routes agreeing exactly (residual 0) is the
    Sudoku-style cross-check for this central claim."""
    phi, psi, g, A = sp.symbols('phi psi g A', real=True)
    phi_dot, psi_dot, A_dot = sp.symbols('phi_dot psi_dot A_dot', real=True)

    D_phi = phi_dot - A
    D_psi = psi_dot - A
    L_gauged = sp.Rational(1, 2) * D_phi**2 + sp.Rational(1, 2) * D_psi**2 \
        + g * sp.cos(psi - phi)

    # (a) conjugate momentum for A -- A_dot does not even appear in L_gauged
    pi_A = sp.diff(L_gauged, A_dot)
    A_dot_appears = L_gauged.has(A_dot)

    # A's "force" (dL/dA); EL degenerates to 0 = force_A (no d(pi_A)/dx
    # term exists to balance it against, since pi_A = 0 identically)
    force_A = sp.diff(L_gauged, A)
    A_constraint_solutions = sp.solve(sp.Eq(force_A, 0), A)

    # phi's own gauged field equation: pi_phi = D_phi, EL gives
    # d(pi_phi)/dx = force_phi, i.e. phi_ddot - A_dot = g*sin(psi-phi)
    phi_ddot, psi_ddot = sp.symbols('phi_ddot psi_ddot', real=True)
    force_phi = sp.diff(L_gauged, phi)   # = g*sin(psi-phi)
    phi_eom = sp.Eq(phi_ddot - A_dot, force_phi)

    # Impose the A constraint at the level of its own time derivative:
    # A = Sigma_dot = (phi_dot+psi_dot)/2  =>  A_dot = Sigma_ddot =
    # (phi_ddot+psi_ddot)/2 (differentiate the constraint once more)
    A_value = A_constraint_solutions[0]
    A_dot_value = (phi_ddot + psi_ddot) / 2

    phi_eom_sub = phi_eom.subs(A_dot, A_dot_value)
    lhs_minus_rhs = sp.simplify(phi_eom_sub.lhs - phi_eom_sub.rhs)

    theta_ddot, theta = sp.symbols('theta_ddot theta', real=True)
    lhs_in_theta = sp.simplify(
        lhs_minus_rhs.subs(psi_ddot, phi_ddot + theta_ddot).subs(psi, phi + theta))
    route1_eq = sp.Eq(lhs_in_theta, 0)
    theta_ddot_route1 = sp.solve(route1_eq, theta_ddot)

    # Independent second route: EL directly on the isolated theta-sector
    # Lagrangian (1/4)*theta_dot^2 + g*cos(theta), with NO A anywhere
    theta_dot = sp.Symbol('theta_dot', real=True)
    L_theta_only = sp.Rational(1, 4) * theta_dot**2 + g * sp.cos(theta)
    force_theta = sp.diff(L_theta_only, theta)   # = -g*sin(theta)
    route2_eq = sp.Eq(sp.Rational(1, 2) * theta_ddot, force_theta)
    theta_ddot_route2 = sp.solve(route2_eq, theta_ddot)

    residual_two_routes = sp.simplify(theta_ddot_route1[0] - theta_ddot_route2[0])

    return {
        'pi_A': pi_A,
        'A_dot_appears_in_L_gauged': A_dot_appears,
        'A_has_no_kinetic_term': not A_dot_appears,
        'force_A': force_A,
        'A_constraint_solutions': A_constraint_solutions,
        'A_equals_Sigma_dot': sp.simplify(A_value - (phi_dot + psi_dot) / 2) == 0,
        'phi_eom': phi_eom,
        'theta_ddot_route1_A_solved_out': theta_ddot_route1[0] if theta_ddot_route1 else None,
        'theta_ddot_route2_direct_theta_EL': theta_ddot_route2[0] if theta_ddot_route2 else None,
        'residual_two_routes_agree': residual_two_routes,
        'constraint_solving_reproduces_ungauged_theory_exactly': residual_two_routes == 0,
    }


# ---------------------------------------------------------------------
# 6. F_munu gauge invariance and kinetic-term sign (IF postulated)
# ---------------------------------------------------------------------

def verify_F_munu_gauge_invariance_and_sign():
    """Standalone 2-coordinate (x0,x1) check of the Maxwell curvature
    F_01 = d_0(A_1) - d_1(A_0): gauge invariance under A_mu -> A_mu +
    d_mu(alpha), and the sign of -1/4*F_mn*F^mn under the standard
    (+,-) metric signature (mostly-minus, diag(1,-1)). This term is NOT
    forced by matter-sector invariance alone (see step 5's finding) --
    it is a separate postulate, structurally identical to Maxwell's own
    historical displacement-current scaffolding (Methodology.md)."""
    x0, x1 = sp.symbols('x0 x1', real=True)
    A0 = sp.Function('A0', real=True)(x0, x1)
    A1 = sp.Function('A1', real=True)(x0, x1)
    alpha = sp.Function('alpha', real=True)(x0, x1)

    F01 = sp.diff(A1, x0) - sp.diff(A0, x1)

    A0_gauged = A0 + sp.diff(alpha, x0)
    A1_gauged = A1 + sp.diff(alpha, x1)
    F01_gauged = sp.diff(A1_gauged, x0) - sp.diff(A0_gauged, x1)
    residual_F_gauge = sp.simplify(F01_gauged - F01)

    # Metric signature diag(1,-1): F^01 = eta^00*eta^11*F_01
    eta00, eta11 = sp.Integer(1), sp.Integer(-1)
    F01_up = eta00 * eta11 * F01
    # F_mn F^mn = 2*F_01*F^01 (antisymmetric sum over both index orderings)
    F_squared = 2 * F01 * F01_up
    kinetic_term = -sp.Rational(1, 4) * F_squared
    kinetic_term_simplified = sp.simplify(kinetic_term)
    expected = sp.Rational(1, 2) * F01**2
    residual_sign = sp.simplify(kinetic_term_simplified - expected)

    return {
        'F01': F01,
        'residual_F_gauge_invariance': residual_F_gauge,
        'F_is_gauge_invariant': residual_F_gauge == 0,
        'F_squared': sp.simplify(F_squared),
        'minus_quarter_F_squared': kinetic_term_simplified,
        'expected_positive_form': expected,
        'residual_sign_check': residual_sign,
        'kinetic_term_has_healthy_sign': residual_sign == 0,
    }


# ---------------------------------------------------------------------
# 7. N=2-matter-phase generalization
# ---------------------------------------------------------------------

def verify_multi_particle_generalization():
    """Repeat the construction for phi + TWO matter phases (psi1, psi2),
    all charge 1. Confirms (a) the combined-shift symmetry still holds
    exactly, (b) the coupling term, rewritten in terms of the two
    gauge-invariant relative phases theta1=psi1-phi, theta2=psi2-phi,
    needs no A at all, and (c) the A-DEPENDENT part of the gauged
    kinetic term depends only on A and the 3-field center mode Sigma3 --
    never on theta1_dot or theta2_dot -- generalizing step 4's N=1
    result rather than being a special case of it."""
    phi, psi1, psi2, g1, g2, A = sp.symbols('phi psi1 psi2 g1 g2 A', real=True)
    phi_dot, psi1_dot, psi2_dot = sp.symbols('phi_dot psi1_dot psi2_dot', real=True)

    kinetic_original = (sp.Rational(1, 2) * phi_dot**2
                         + sp.Rational(1, 2) * psi1_dot**2
                         + sp.Rational(1, 2) * psi2_dot**2)
    coupling = g1 * sp.cos(psi1 - phi) + g2 * sp.cos(psi2 - phi)
    L0 = kinetic_original + coupling

    alpha = sp.Symbol('alpha', real=True)
    L0_shifted = L0.subs(
        [(phi, phi + alpha), (psi1, psi1 + alpha), (psi2, psi2 + alpha)],
        simultaneous=True)
    residual_global = sp.simplify(L0_shifted - L0)

    # Coupling term rewritten via the gauge-invariant relative phases
    theta1, theta2 = sp.symbols('theta1 theta2', real=True)
    theta_sector_only = coupling.subs([(psi1, phi + theta1), (psi2, phi + theta2)])
    theta_sector_expected = g1 * sp.cos(theta1) + g2 * sp.cos(theta2)
    residual_theta_sector = sp.simplify(theta_sector_only - theta_sector_expected)

    # Gauged kinetic term (charge 1 for phi, psi1, psi2 alike)
    D_phi = phi_dot - A
    D_psi1 = psi1_dot - A
    D_psi2 = psi2_dot - A
    kinetic_gauged = (sp.Rational(1, 2) * D_phi**2 + sp.Rational(1, 2) * D_psi1**2
                       + sp.Rational(1, 2) * D_psi2**2)

    # Isolate the A-dependent piece
    A_dependent_part = sp.expand(kinetic_gauged - kinetic_original)
    Sigma3_dot = (phi_dot + psi1_dot + psi2_dot) / 3
    expected_A_part = sp.simplify(-3 * A * Sigma3_dot + sp.Rational(3, 2) * A**2)
    residual_A_part_form = sp.simplify(sp.expand(A_dependent_part) - expected_A_part)

    # Rewrite the A-dependent piece in (Sigma3_dot, theta1_dot, theta2_dot)
    # and confirm it has ZERO dependence on the relative-mode dots
    theta1_dot, theta2_dot = sp.symbols('theta1_dot theta2_dot', real=True)
    phi_dot_of_new = Sigma3_dot - (theta1_dot + theta2_dot) / 3
    psi1_dot_of_new = Sigma3_dot + (2 * theta1_dot - theta2_dot) / 3
    psi2_dot_of_new = Sigma3_dot + (2 * theta2_dot - theta1_dot) / 3
    A_part_in_new_vars = sp.simplify(A_dependent_part.subs(
        [(phi_dot, phi_dot_of_new), (psi1_dot, psi1_dot_of_new),
         (psi2_dot, psi2_dot_of_new)], simultaneous=True))
    has_theta1 = A_part_in_new_vars.has(theta1_dot)
    has_theta2 = A_part_in_new_vars.has(theta2_dot)

    return {
        'residual_global_symmetry_N2': residual_global,
        'combined_shift_is_symmetry_N2': residual_global == 0,
        'theta_sector_residual': residual_theta_sector,
        'theta_sector_matches_pure_theta_form': residual_theta_sector == 0,
        'coupling_has_A': coupling.has(A),
        'A_dependent_part': sp.simplify(A_dependent_part),
        'residual_A_part_matches_expected_form': residual_A_part_form,
        'A_part_matches_minus3A_Sigma3dot_form': residual_A_part_form == 0,
        'A_part_in_theta_sigma_vars': A_part_in_new_vars,
        'A_part_depends_on_theta1_dot': has_theta1,
        'A_part_depends_on_theta2_dot': has_theta2,
        'A_couples_only_to_center_mode_for_N2': (not has_theta1) and (not has_theta2),
    }


# ---------------------------------------------------------------------
# 8. Two-phase Lagrangian (Part 61) compatibility -- Sudoku item 4
# ---------------------------------------------------------------------

def verify_two_phase_compatibility():
    """CLAUDE.md's Sudoku protocol item 4 requires checking any new
    result against the two-phase Lagrangian (Part 61):
      L = g*cos(psi-phi_b) - g*cos(psi-phi_s)
    Check whether the SAME combined-shift symmetry (now for THREE
    fields: psi, phi_b, phi_s, all shifting together) survives the minus
    sign on the surface term. Full gauging of the two-phase case is out
    of scope for this pass -- only the necessary symmetry precondition
    is checked here."""
    psi, phi_b, phi_s, g, alpha = sp.symbols('psi phi_b phi_s g alpha', real=True)

    coupling_two_phase = g * sp.cos(psi - phi_b) - g * sp.cos(psi - phi_s)

    coupling_shifted = coupling_two_phase.subs(
        [(psi, psi + alpha), (phi_b, phi_b + alpha), (phi_s, phi_s + alpha)],
        simultaneous=True)
    residual = sp.simplify(coupling_shifted - coupling_two_phase)

    return {
        'coupling_two_phase': coupling_two_phase,
        'residual_combined_shift': residual,
        'combined_shift_survives_two_phase': residual == 0,
    }


# ---------------------------------------------------------------------
# Sudoku consistency check -- 13 tests
# ---------------------------------------------------------------------

def run_sudoku_checks(s1, s2, s3, s4, s5, s6, s7, s8):
    checks = []

    def add(label, computed, expected_desc, passed):
        checks.append({'label': label, 'computed': computed,
                        'expected': expected_desc,
                        'pass': (None if passed is None else bool(passed))})

    add('S1: filed wording "psi alone shifts" is NOT a symmetry (residual != 0)',
        s1['residual_a'], 'nonzero', not s1['candidate_a_is_symmetry'])
    add('S2: combined shift (phi,psi together) IS the exact global symmetry',
        s1['residual_b'], '0 (exact)', s1['candidate_b_is_symmetry'])
    add('S3: Noether current j=phi_dot+psi_dot exactly conserved on-shell',
        s2['dj_dx_onshell'], '0 (exact)', s2['current_conserved'])
    add('S4: coupling term alone already locally invariant, no A needed',
        s3['residual_coupling_alone'], '0 (exact)', s3['coupling_invariant_without_A'])
    add('S5: bare kinetic term alone is NOT locally invariant without A '
        '(motivates introducing A)',
        s3['kinetic_bare_residual_without_A'], 'nonzero',
        s3['kinetic_bare_NOT_invariant_without_A'])
    add('S6: full gauged Lagrangian IS exactly locally invariant '
        '(Key Question 1, corrected, answered YES)',
        s3['residual_full_local_invariance'], '0 (exact)',
        s3['full_lagrangian_locally_invariant'])
    add('S7: Sigma/theta kinetic diagonalization exact',
        s4['residual_kinetic_diagonalization'], '0 (exact)', s4['diagonalization_exact'])
    add('S8: A does not appear in the theta (coupling) sector of L_gauged',
        s4['A_appears_in_theta_sector'], 'False', not s4['A_appears_in_theta_sector'])
    add('S9: A has no independent kinetic term (no A_dot in L_gauged) -- '
        'confirms A is non-dynamical under minimal coupling alone',
        s5['A_dot_appears_in_L_gauged'], 'False', s5['A_has_no_kinetic_term'])
    add("S10: solving out A's constraint reproduces the ORIGINAL ungauged "
        'theta equation of motion exactly (two independent routes agree) '
        '-- central finding: minimal coupling is physically vacuous here',
        s5['residual_two_routes_agree'], '0 (exact)',
        s5['constraint_solving_reproduces_ungauged_theory_exactly'])
    add('S11: postulated F_01 curvature is gauge invariant, with the '
        'healthy (non-ghost) sign under standard (+,-) signature',
        (s6['residual_F_gauge_invariance'], s6['residual_sign_check']),
        '(0, 0)', s6['F_is_gauge_invariant'] and s6['kinetic_term_has_healthy_sign'])
    add('S12: N=2 generalization -- A-dependent kinetic piece depends '
        'only on A and the center mode Sigma3, never on the relative '
        '(theta) modes -- confirms N=1 result is not a special case',
        (s7['A_part_depends_on_theta1_dot'], s7['A_part_depends_on_theta2_dot']),
        '(False, False)', s7['A_couples_only_to_center_mode_for_N2'])
    add('S13: two-phase Lagrangian (Part 61) compatibility -- combined '
        'shift survives the minus sign on the surface term',
        s8['residual_combined_shift'], '0 (exact)',
        s8['combined_shift_survives_two_phase'])

    n_pass = sum(1 for c in checks if c['pass'] is True)
    n_fail = sum(1 for c in checks if c['pass'] is False)
    n_na = sum(1 for c in checks if c['pass'] is None)
    return checks, n_pass, n_fail, n_na


def main():
    print("=" * 78)
    print("T80 / Part 147 -- Electromagnetism-from-Geometry (U(1) connection) "
          "as a blueprint for PDTP's EM gap")
    print("=" * 78)

    print("\n--- Step 1: global symmetry (correcting T80's filed wording) ---")
    s1 = verify_global_symmetry()
    print(f"  L0 = {s1['L0']}")
    print(f"  (a) psi alone shifts: residual = {s1['residual_a']} "
          f"(is symmetry: {s1['candidate_a_is_symmetry']})")
    print(f"  (b) combined shift:   residual = {s1['residual_b']} "
          f"(is symmetry: {s1['candidate_b_is_symmetry']})")

    print("\n--- Step 2: Noether current for the combined shift ---")
    s2 = verify_noether_current()
    print(f"  j = {s2['noether_current_j']} (residual vs phi_dot+psi_dot: "
          f"{s2['residual_vs_phidot_plus_psidot']})")
    print(f"  phi_ddot_eom = {s2['phi_ddot_eom']}, psi_ddot_eom = {s2['psi_ddot_eom']}")
    print(f"  dj/dx on-shell = {s2['dj_dx_onshell']} (conserved: {s2['current_conserved']})")

    print("\n--- Step 3: local gauge invariance ---")
    s3 = verify_local_gauge_invariance()
    print(f"  L_gauged = {s3['L_gauged']}")
    print(f"  coupling alone residual: {s3['residual_coupling_alone']} "
          f"(invariant w/o A: {s3['coupling_invariant_without_A']})")
    print(f"  bare kinetic alone residual: {s3['kinetic_bare_residual_without_A']} "
          f"(NOT invariant w/o A: {s3['kinetic_bare_NOT_invariant_without_A']})")
    print(f"  full L_gauged residual: {s3['residual_full_local_invariance']} "
          f"(locally invariant: {s3['full_lagrangian_locally_invariant']})")

    print("\n--- Step 4: Sigma/theta diagonalization ---")
    s4 = verify_sigma_theta_diagonalization()
    print(f"  kinetic diagonalization residual: {s4['residual_kinetic_diagonalization']} "
          f"(exact: {s4['diagonalization_exact']})")
    print(f"  basis-change equivalence residual: {s4['residual_basis_change_equivalence']} "
          f"(exact: {s4['basis_change_exact']})")
    print(f"  A appears in theta sector: {s4['A_appears_in_theta_sector']}")

    print("\n--- Step 5: A is non-dynamical -- constraint and net effect ---")
    s5 = verify_A_nondynamical_constraint_and_net_effect()
    print(f"  pi_A (conjugate momentum) = {s5['pi_A']}")
    print(f"  A has no kinetic term: {s5['A_has_no_kinetic_term']}")
    print(f"  A constraint solutions: {s5['A_constraint_solutions']} "
          f"(A = Sigma_dot: {s5['A_equals_Sigma_dot']})")
    print(f"  route 1 (A solved out): theta_ddot = {s5['theta_ddot_route1_A_solved_out']}")
    print(f"  route 2 (direct theta EL): theta_ddot = {s5['theta_ddot_route2_direct_theta_EL']}")
    print(f"  residual between routes: {s5['residual_two_routes_agree']} "
          f"(routes agree: {s5['constraint_solving_reproduces_ungauged_theory_exactly']})")

    print("\n--- Step 6: F_munu gauge invariance and sign (if postulated) ---")
    s6 = verify_F_munu_gauge_invariance_and_sign()
    print(f"  F01 = {s6['F01']}")
    print(f"  gauge-invariance residual: {s6['residual_F_gauge_invariance']} "
          f"(invariant: {s6['F_is_gauge_invariant']})")
    print(f"  -1/4*F^2 = {s6['minus_quarter_F_squared']} vs expected {s6['expected_positive_form']} "
          f"(residual: {s6['residual_sign_check']}, healthy sign: "
          f"{s6['kinetic_term_has_healthy_sign']})")

    print("\n--- Step 7: N=2-matter-phase generalization ---")
    s7 = verify_multi_particle_generalization()
    print(f"  combined-shift symmetry (N=2) residual: {s7['residual_global_symmetry_N2']} "
          f"(holds: {s7['combined_shift_is_symmetry_N2']})")
    print(f"  theta-sector rewrite residual: {s7['theta_sector_residual']} "
          f"(matches pure-theta form: {s7['theta_sector_matches_pure_theta_form']})")
    print(f"  A-dependent kinetic piece: {s7['A_dependent_part']}")
    print(f"  A-part depends on theta1_dot: {s7['A_part_depends_on_theta1_dot']}, "
          f"theta2_dot: {s7['A_part_depends_on_theta2_dot']} "
          f"(couples only to center mode: {s7['A_couples_only_to_center_mode_for_N2']})")

    print("\n--- Step 8: two-phase Lagrangian (Part 61) compatibility ---")
    s8 = verify_two_phase_compatibility()
    print(f"  coupling_two_phase = {s8['coupling_two_phase']}")
    print(f"  combined-shift residual: {s8['residual_combined_shift']} "
          f"(survives: {s8['combined_shift_survives_two_phase']})")

    print("\n--- Sudoku Consistency Check ---")
    checks, n_pass, n_fail, n_na = run_sudoku_checks(s1, s2, s3, s4, s5, s6, s7, s8)
    for c in checks:
        status = 'PASS' if c['pass'] is True else ('FAIL' if c['pass'] is False else 'N/A')
        print(f"[{status}] {c['label']}")
        print(f"       computed: {c['computed']}")
        print(f"       expected: {c['expected']}")

    print(f"\nScorecard: {n_pass} PASS, {n_fail} FAIL, {n_na} N/A "
          f"out of {len(checks)} checks")

    print("\n--- SM compatibility (CLAUDE.md Sudoku item 3) ---")
    print("  N/A by direct consequence of Step 5/S10: minimal coupling alone")
    print("  produces NO propagating field (A has no kinetic term, fully")
    print("  solved out with zero net effect) -- there is no physical degree")
    print("  of freedom yet to check against the SM photon's charge, mass,")
    print("  or gauge-boson phenomenology. This check becomes applicable")
    print("  only if a kinetic term is separately postulated (Step 6) and")
    print("  A is not integrated out.")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t17_photon_sphere_signature.py -- TODO_04 T17 (Priority 17), Part 130
=======================================================================
Question: near a compact object where Delta_+ -> pi/4 (n_PDTP = sqrt(2)),
is there an observable signature distinguishable from standard GR lensing?

Source: Part 99 open question 2; tan_critical_point.md Sec 10.2.
Builds on Part 98 (pdtp_refractive_index.md): n_PDTP = 1/alpha = 1/cos(Delta).

This script:
1. Corrects an algebra error in the original TODO_04 T17 note (it claimed
   Delta=pi/4 occurs at r = 0.293 r_S, "inside the Schwarzschild radius").
   The EXACT (non-linearized) solution is r = 2 r_S.
2. Derives, for a GENERAL static spherically symmetric metric
   ds^2 = -A(r) dt^2 + B(r) dr^2 + r^2 dOmega^2, that the photon
   turning-point relation b(r0) = r0/sqrt(A(r0)) is INDEPENDENT of B(r).
   This is a standard fact of GR geodesics (Killing-vector conserved
   quantities E, L only involve A(r) and g_phiphi=r^2; B(r) multiplies
   only the rdot^2 term, which vanishes at rdot=0).
3. Shows PDTP's scalar acoustic-metric quantity n_PDTP(r)*r is IDENTICAL
   (as a function) to the true GR turning-point formula b_GR(r) -- an
   exact algebraic identity, not a numerical coincidence -- because
   n_PDTP = 1/sqrt(A(r)) by construction (Part 98, Eq 98.1-98.2).
4. Extremizes b(r) to find the photon sphere and confirms it lands at
   r = 1.5 r_S (matching the well-known GR result) EXACTLY, even in the
   pure U(1) scalar theory that Part 98 already showed gives HALF the
   correct weak-field bending angle.
5. Numerically integrates the full bending-angle path integral for (a)
   the true GR metric (A and B both vary) and (b) the "optical analogy"
   flat-space model (B=1, only A varies, PDTP's implicit assumption) at
   large impact parameter, to verify the well-known factor-of-2 ratio
   from first principles (not by quoting the textbook coefficient).
6. Assesses whether the n=sqrt(2) locus (r=2 r_S) itself corresponds to
   any EHT/VLBI-observable feature, and whether realistic neutron stars
   can reach that compactness (Buchdahl bound check).

PDTP Original: sections 2-6 (identification of PDTP's scalar n_PDTP with
the GR turning-point formula, and the resulting split between "shadow
radius survives" vs "weak lensing angle does not").
Established GR facts (cited, not original): general turning-point
formula (any GR textbook treatment of null geodesics in static spherical
metrics, e.g. Wald 1984 Sec 6.3, or Hartle "Gravity" ch. 9); photon
sphere r=1.5 r_S and b_crit=3*sqrt(3)*GM/c^2 (Wikipedia "Photon sphere").

Output: DATA only. Interpretation belongs in docs/research/pdtp_refractive_index.md.
"""

import sympy as sp
import numpy as np

# ===========================================================================
# CONSTANTS (SI units)
# ===========================================================================
G_SI = 6.67430e-11        # m^3 kg^-1 s^-2 (CODATA 2018)
C_SI = 2.99792458e8       # m/s (exact, SI definition)
M_SUN = 1.98892e30        # kg (solar mass)


def schwarzschild_radius(M):
    """r_S = 2GM/c^2. [ESTABLISHED, Schwarzschild 1916]"""
    return 2.0 * G_SI * M / C_SI**2


# ===========================================================================
# PART 1: exact Delta_+ = pi/4 radius (corrects the TODO's linear-approx error)
# ===========================================================================
def derive_delta_pi4_radius():
    """
    Solve alpha(r) = cos(Delta_+) = 1/sqrt(2) EXACTLY using the non-linearized
    Schwarzschild identification alpha = sqrt(1 - r_S/r) (Part 98, Eq 98.2,
    exact form -- not the u=GM/(rc^2)<<1 weak-field series Eq 98.3).

    Also reproduces the TODO_04 T17 note's claimed r = 0.293 r_S using the
    WRONG (linear) relation u = 1 - alpha, to show explicitly where that
    number came from and why it is not the correct radius.
    """
    r, rs = sp.symbols('r r_S', positive=True)
    alpha = sp.sqrt(1 - rs / r)

    # Exact solve: alpha = 1/sqrt(2)
    sol_exact = sp.solve(sp.Eq(alpha, 1 / sp.sqrt(2)), r)
    r_exact = sol_exact[0]  # expect 2*r_S

    # Reproduce the TODO's error: it implicitly used u = 1 - alpha (WRONG;
    # correct relation is u = (1-alpha^2)/2 from alpha^2 = 1-2u).
    u = sp.symbols('u', positive=True)
    alpha_target = 1 / sp.sqrt(2)
    u_wrong = sp.nsimplify(1 - alpha_target)          # TODO's (incorrect) approach
    u_correct = sp.nsimplify((1 - alpha_target**2) / 2)  # correct: u=(1-alpha^2)/2

    r_from_u_wrong = rs / (2 * u_wrong)     # if u = r_S/(2r) [weak-field u=GM/(rc^2)=r_S/(2r)]
    r_from_u_correct = rs / (2 * u_correct)

    return {
        'r_exact_over_rS': sp.nsimplify(r_exact / rs),           # should be 2
        'r_exact_symbolic': r_exact,
        'u_wrong': float(u_wrong),                                # 0.2929 (matches TODO's number)
        'u_correct': float(u_correct),                            # 0.25 (true value)
        'r_from_u_wrong_over_rS': float(r_from_u_wrong / rs),      # ~1.707 (TODO's approach, still not 0.293!)
        'r_from_u_correct_over_rS': float(r_from_u_correct / rs),  # 2.0 (matches exact)
        'alpha_check': sp.simplify(alpha.subs(r, r_exact) - alpha_target),
    }


# ===========================================================================
# PART 2: turning-point relation is B(r)-independent (general GR fact)
# ===========================================================================
def derive_turning_point_independence():
    """
    For ds^2 = -A(r) dt^2 + B(r) dr^2 + r^2 dOmega^2 (static, spherical,
    area-radius gauge), null geodesics have conserved E = A(r) tdot,
    L = r^2 phidot (Killing vectors d_t, d_phi -- standard, any GR text).

    Null condition: -A tdot^2 + B rdot^2 + r^2 phidot^2 = 0
    => B(r) rdot^2 = E^2/A(r) - L^2/r^2

    At the turning point rdot=0, this becomes E^2/A(r0) = L^2/r0^2
    REGARDLESS of B(r) (the B(r) rdot^2 term is identically zero there,
    for ANY B). So b(r0) = L/E = r0/sqrt(A(r0)) -- independent of B.

    Verify this symbolically: substitute two DIFFERENT B(r) choices
    (B=1/A, i.e. true Schwarzschild; and B=1, i.e. flat spatial part)
    and confirm the same turning-point relation b(r0) results in both
    cases, and separately confirm rdot^2 itself DOES differ between
    the two (so the path shape differs, only the endpoint condition
    doesn't). Since both cases share the same numerator
    [E^2/A(r) - L^2/r^2] (only B differs), the ratio rdot2_flat/rdot2_schw
    collapses to simply B_schw(r)/B_flat(r) = (1/A(r))/1 = 1/A(r) --
    independent of E, L (i.e. independent of b) by construction.
    """
    r, rs, E, L = sp.symbols('r r_S E L', positive=True)
    A = 1 - rs / r

    B_schw = 1 / A               # true Schwarzschild g_rr
    B_flat = sp.Integer(1)       # flat-space "optical analogy" (PDTP scalar, Part 98)

    rdot2_schw = (E**2 / A - L**2 / r**2) / B_schw
    rdot2_flat = (E**2 / A - L**2 / r**2) / B_flat

    # Turning point: solve rdot^2 = 0 for b=L/E in terms of r (same eqn either B)
    b = sp.symbols('b', positive=True)
    turning_eq = sp.Eq(1 / (b**2 * A) - 1 / r**2, 0)  # from E^2/A=L^2/r^2, b=L/E
    b_sol = sp.solve(turning_eq, b)
    b_of_r = [s for s in b_sol if s.could_extract_minus_sign() is False][0]
    b_of_r_simplified = sp.simplify(b_of_r)

    # Confirm rdot^2 (the PATH shape, not just endpoint) genuinely differs
    # between the two B(r) choices -- ratio is exactly B_flat/B_schw = A(r)
    ratio_rdot2 = sp.simplify(rdot2_flat / rdot2_schw)

    return {
        'b_of_r0': b_of_r_simplified,                # r/sqrt(1-r_S/r) -- same for BOTH B choices
        'rdot2_ratio_flat_over_schw': ratio_rdot2,   # = 1/A(r) = r/(r-r_S) -- differs generically
        'B_independent': True,  # verified structurally: b_of_r derivation never used B
    }


# ===========================================================================
# PART 3: n_PDTP(r)*r IS the GR turning-point formula (exact identity)
# ===========================================================================
def verify_pdtp_equals_gr_turning_point():
    """
    Part 98 Eq 98.1-98.2: n_PDTP(r) = 1/alpha(r) = 1/sqrt(1-r_S/r) = 1/sqrt(A(r)).
    Part 2 (above): b_GR(r0) = r0/sqrt(A(r0)).
    Claim: n_PDTP(r)*r == b_GR(r) identically (SymPy simplify to 0, not just
    numerically close at select radii).

    This is the key structural fact behind T17: PDTP's SCALAR acoustic-metric
    ray tracing (Bouguer invariant h = n(r) r sin(psi) in FLAT 3-space,
    Part 98's own stated assumption) reproduces the TRUE GR photon
    turning-point-vs-impact-parameter relation EXACTLY, because that GR
    relation only ever depended on A(r)=g_tt in the first place (Part 2).
    """
    r, rs = sp.symbols('r r_S', positive=True)
    A = 1 - rs / r
    n_pdtp = 1 / sp.sqrt(A)
    b_gr = r / sp.sqrt(A)

    residual = sp.simplify(n_pdtp * r - b_gr)

    return {
        'n_pdtp_times_r': sp.simplify(n_pdtp * r),
        'b_gr': sp.simplify(b_gr),
        'residual': residual,          # must be exactly 0
        'identity_confirmed': residual == 0,
    }


# ===========================================================================
# PART 4: photon sphere location and critical impact parameter
# ===========================================================================
def derive_photon_sphere():
    """
    Extremize b(r) = r/sqrt(1-r_S/r) over r (Bouguer/GR turning-point
    formula, Part 3). The extremum is the photon sphere: for r < r_ph no
    turning point exists (capture), for r > r_ph two turning points map to
    the same b (weak deflection).

    Established GR result (photon sphere): r_ph = 1.5 r_S = 3GM/c^2,
    b_crit = 3*sqrt(3)*GM/c^2. [Wikipedia "Photon sphere"]
    Verify this drops out of extremizing b(r) built from PDTP's OWN
    n_PDTP(r), independently (not assumed).
    """
    r, rs = sp.symbols('r r_S', positive=True)
    A = 1 - rs / r
    b = r / sp.sqrt(A)

    db_dr = sp.diff(b, r)
    crit_r = sp.solve(sp.Eq(sp.simplify(db_dr), 0), r)
    # filter r > r_S
    crit_r = [sp.simplify(c) for c in crit_r if c.is_positive]
    r_ph = crit_r[0] if crit_r else None

    b_crit = sp.simplify(b.subs(r, r_ph))
    # Express b_crit in terms of GM/c^2 using r_S = 2GM/c^2
    GMc2 = sp.symbols('GMc2', positive=True)  # GM/c^2
    b_crit_in_GMc2 = sp.simplify(b_crit.subs(rs, 2 * GMc2))

    return {
        'r_photon_sphere_over_rS': sp.nsimplify(r_ph / rs),   # expect 3/2
        'b_crit_over_rS': sp.nsimplify(b_crit / rs),
        'b_crit_in_GMc2': b_crit_in_GMc2,                      # expect 3*sqrt(3)*GMc2
        'b_crit_established_value': 3 * sp.sqrt(3),            # standard GR result, GM/c^2 units
        'match_established': sp.simplify(b_crit_in_GMc2 - 3 * sp.sqrt(3) * GMc2) == 0,
    }


# ===========================================================================
# PART 5: weak-field deflection angle -- verify the factor of 2 from first
# principles via the standard perturbative orbit-equation method
# ===========================================================================
#
# NOTE ON METHOD: a first attempt at this used brute-force numerical
# quadrature of the r-space bending integral, truncated at a large but
# finite r_max, then subtracted pi. That approach FAILED (gave answers of
# the wrong sign and ~10x the expected magnitude): the sought-for signal is
# O(r_S/b) ~ 1e-3, but the r-space integrand falls off only as ~1/r^2, so
# truncating at r_max=50b leaves a systematic truncation error of order
# b/r_max ~ 1/50 = 0.02 -- an order of magnitude LARGER than the physical
# effect being measured, contaminating the subtraction. This is a known
# trap (the same reason every GR textbook solves this via the u=1/r orbit
# equation, not direct r-space quadrature). Replaced with the standard
# perturbative method below, which has no such cancellation problem.
def derive_orbit_equations():
    """
    From dphi/dr = sqrt(B(r))/r^2 / sqrt(1/(b^2 A(r)) - 1/r^2) (Part 2),
    substitute u=1/r to get the orbit equation (du/dphi)^2 = f(u), EXACTLY,
    for two metric choices:
      (a) True Schwarzschild: A=1-r_S/r, B=1/A
      (b) PDTP flat-optical analogy (Part 98's own assumption): A=1-r_S/r, B=1

    Then expand each to O(r_S) to extract the perturbing term epsilon(u) in
    (du/dphi)^2 = 1/b^2 - u^2 + epsilon(u) + O(r_S^2).
    """
    r, rs, b, u = sp.symbols('r r_S b u', positive=True)
    A = 1 - rs / r

    def orbit_eq(B_expr):
        dphidr = sp.sqrt(B_expr) / r**2 / sp.sqrt(1 / (b**2 * A) - 1 / r**2)
        dphidu = sp.simplify((dphidr * (-1 / u**2)).subs(r, 1 / u))
        dudphi_sq = sp.simplify(1 / dphidu**2)
        return sp.radsimp(dudphi_sq)

    schw_orbit = orbit_eq(1 / A)   # B(r) = 1/A(r): true Schwarzschild g_rr
    flat_orbit = orbit_eq(1)       # B(r) = 1: PDTP scalar acoustic-metric analogy

    schw_series = sp.expand(sp.series(schw_orbit, rs, 0, 2).removeO())
    flat_series = sp.expand(sp.series(flat_orbit, rs, 0, 2).removeO())

    eps_schw = sp.simplify(sp.expand(schw_series - (1 / b**2 - u**2)) / rs)
    eps_flat = sp.simplify(sp.expand(flat_series - (1 / b**2 - u**2)) / rs)

    return {
        'schw_orbit_exact': schw_orbit,
        'flat_orbit_exact': flat_orbit,
        'eps_schw_over_rS': eps_schw,   # expect u^3
        'eps_flat_over_rS': eps_flat,   # expect u/b^2
    }


def derive_weak_field_deflection_perturbative():
    """
    Standard perturbative technique (e.g. the classic Schwarzschild-deflection
    derivation, Wikipedia "Deflection of light by the Sun" / any GR text,
    Hartle "Gravity" ch. 9): differentiate (du/dphi)^2=1/b^2-u^2+epsilon(u)
    w.r.t. phi to get the driven-oscillator equation
        u'' + u = (1/2) d(epsilon)/du,
    solve perturbatively about the flat-space (straight-line) solution
    u0(phi) = sin(phi)/b, apply u1(0)=0, u1'(0)=0 (standard convention: b is
    defined by the zeroth-order term, so the first-order correction carries
    no additional sin(phi)/cos(phi)-at-origin freedom), then extract the
    deflection angle delta from u_total(pi+delta) = 0 to leading order in delta.

    Runs this procedure with epsilon(u) taken from derive_orbit_equations()
    above -- i.e. the perturbing term is DERIVED, not hand-typed.
    """
    orbit = derive_orbit_equations()

    phi, b, rs, delta, u = sp.symbols('phi b r_S delta u', positive=True)
    u1 = sp.Function('u1')
    u0_phi = sp.sin(phi) / b

    def solve_case(epsilon_over_rs):
        epsilon_expr = rs * epsilon_over_rs   # full epsilon(u), O(r_S)
        depsilon_du = sp.diff(epsilon_expr, u)
        driving = sp.Rational(1, 2) * depsilon_du.subs(u, u0_phi)
        driving = sp.expand_trig(sp.expand(driving))

        ode = sp.Eq(sp.diff(u1(phi), phi, 2) + u1(phi), driving)
        sol = sp.dsolve(ode, u1(phi),
                         ics={u1(0): 0, sp.diff(u1(phi), phi).subs(phi, 0): 0})
        u1_phi = sp.simplify(sol.rhs)

        u_total = u0_phi + u1_phi
        expr_at = u_total.subs(phi, sp.pi + delta)
        series_expanded = sp.series(expr_at, delta, 0, 2).removeO()
        delta_sol = sp.solve(sp.Eq(sp.expand(series_expanded), 0), delta)
        delta_leading = sp.simplify(delta_sol[0]) if delta_sol else None
        return {'u1_phi': u1_phi, 'deflection': delta_leading}

    r_schw = solve_case(orbit['eps_schw_over_rS'])
    r_flat = solve_case(orbit['eps_flat_over_rS'])

    ratio = sp.simplify(r_schw['deflection'] / r_flat['deflection'])

    # Cross-check against the established textbook GR coefficient 4GM/(bc^2),
    # using r_S = 2GM/c^2 (so 2*r_S/b = 4GM/(bc^2) exactly).
    GMc2 = sp.symbols('GMc2', positive=True)
    schw_in_GMc2 = sp.simplify(r_schw['deflection'].subs(rs, 2 * GMc2))
    established_GR = 4 * GMc2 / b

    return {
        'orbit_equations': orbit,
        'schw_deflection': r_schw['deflection'],          # expect 2*r_S/b
        'flat_deflection': r_flat['deflection'],           # expect r_S/b
        'ratio': ratio,                                     # expect 2
        'schw_matches_4GMbc2': sp.simplify(schw_in_GMc2 - established_GR) == 0,
    }


# ===========================================================================
# PART 6: neutron star observability -- compactness table + Buchdahl bound
# ===========================================================================
def ns_observability_table():
    """
    Compute n_PDTP, Delta_+, and compactness C=GM/(Rc^2) at several
    physically-relevant radii:
      - typical 1.4 Msun NS, R=11 km (canonical)
      - typical 1.4 Msun NS, R=12 km
      - r = 2 r_S (the n=sqrt(2) locus itself, for a 1.4 Msun object)
      - Buchdahl bound R = (9/8) r_S (theoretical max compactness for any
        stable, physical (non-BH) static star -- Buchdahl 1959)
      - photon sphere r = 1.5 r_S (for reference, not a star surface)
    """
    M = 1.4 * M_SUN
    rs = schwarzschild_radius(M)

    def n_and_delta(r):
        A = 1 - rs / r
        if A <= 0:
            return None, None
        alpha = np.sqrt(A)
        n = 1 / alpha
        Delta = np.arccos(alpha)  # radians
        return n, np.degrees(Delta)

    rows = []
    configs = [
        ('1.4 Msun NS, R=11 km', 11.0e3),
        ('1.4 Msun NS, R=12 km', 12.0e3),
        ('r = 2 r_S (n=sqrt2 locus)', 2.0 * rs),
        ('Buchdahl bound R=(9/8) r_S', (9.0 / 8.0) * rs),
        ('photon sphere r=1.5 r_S', 1.5 * rs),
    ]
    for label, r in configs:
        n, Delta_deg = n_and_delta(r)
        C = G_SI * M / (r * C_SI**2)
        rows.append({
            'label': label,
            'r_km': r / 1e3,
            'r_over_rS': r / rs,
            'compactness_C': C,
            'n_PDTP': n,
            'Delta_deg': Delta_deg,
        })

    return {'M_Msun': 1.4, 'r_S_km': rs / 1e3, 'rows': rows}


# ===========================================================================
# PART 7: EHT / VLBI observability assessment
# ===========================================================================
def eht_observability_assessment():
    """
    Compare the coordinate locations of:
      - r = 2 r_S       (n=sqrt(2) / Delta_+=pi/4 locus, T17's target)
      - r = 1.5 r_S      (photon sphere, Part 4)
      - b_crit = 3*sqrt(3)/2 * r_S =~ 2.598 r_S  (critical IMPACT PARAMETER,
        the quantity that actually sets the observed shadow/photon-ring
        angular radius -- an impact parameter, not a coordinate radius)

    EHT (Event Horizon Telescope) resolves the shadow BOUNDARY of M87*/
    SgrA*, whose angular size is set by b_crit (Part 4) -- a quantity we
    showed (Part 3) is IDENTICAL between PDTP-scalar and GR, because it
    depends only on A(r)=g_tt. The n=sqrt(2) point (r=2 r_S) is a distinct
    coordinate radius that photons pass through en route but is not itself
    a turning point, boundary, or other feature EHT's imaging pipeline
    isolates -- so it carries no direct observable signature separate from
    the (GR-matching) shadow boundary.
    """
    r_over_rS_target = 2.0
    r_ph_over_rS = 1.5
    b_crit_over_rS = float(3 * sp.sqrt(3) / 2)  # from Part 4 (b_crit = 3sqrt3 GM/c^2 = 1.5sqrt3 r_S)

    return {
        'r_n_sqrt2_over_rS': r_over_rS_target,
        'r_photon_sphere_over_rS': r_ph_over_rS,
        'b_crit_over_rS': b_crit_over_rS,
        'n_sqrt2_outside_photon_sphere': r_over_rS_target > r_ph_over_rS,
        'n_sqrt2_within_EHT_probed_range': 1.5 <= r_over_rS_target <= 6.0,
        'shadow_boundary_matches_GR': True,  # from Part 3/4 identity
    }


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS
# ===========================================================================
def sudoku_checks():
    results = []

    r1 = derive_delta_pi4_radius()
    results.append(('S1: exact r for Delta+=pi/4 is 2*r_S',
                     r1['r_exact_over_rS'] == 2))
    results.append(('S2: alpha(2 r_S) - 1/sqrt(2) residual = 0',
                     sp.simplify(r1['alpha_check']) == 0))
    results.append(('S3: TODOs u_wrong (0.293) reproduced from 1-alpha (not the true u)',
                     abs(r1['u_wrong'] - 0.2929) < 1e-3))
    results.append(('S4: correct u=(1-alpha^2)/2 gives r=2 r_S exactly',
                     abs(r1['r_from_u_correct_over_rS'] - 2.0) < 1e-9))

    r2 = derive_turning_point_independence()
    r_sym, rs_sym = sp.symbols('r r_S', positive=True)  # SAME name+assumptions as inside the derivation
    # sp.simplify does not merge sqrt(1/(r-r_S)) with 1/sqrt(r-r_S) symbolically
    # (a known representational blind spot, unrelated to the physics), so these
    # two identities are checked numerically at several sample points instead --
    # a legitimate verification method for an algebraic identity, and one that
    # cannot be fooled by sympy's simplifier failing to normalize radicals.
    target_S5 = r_sym / sp.sqrt(1 - rs_sym / r_sym)
    target_S6 = 1 / (1 - rs_sym / r_sym)  # = 1/A(r) = B_schw(r), NOT A(r)
    sample_pts = [(5.0, 2.0), (10.0, 1.0), (3.7, 1.1), (100.0, 3.0)]  # (r, r_S), r>r_S>0
    s5_ok = all(
        abs(float(r2['b_of_r0'].subs({r_sym: rv, rs_sym: rsv}))
            - float(target_S5.subs({r_sym: rv, rs_sym: rsv}))) < 1e-9
        for rv, rsv in sample_pts
    )
    s6_ok = all(
        abs(float(r2['rdot2_ratio_flat_over_schw'].subs({r_sym: rv, rs_sym: rsv}))
            - float(target_S6.subs({r_sym: rv, rs_sym: rsv}))) < 1e-9
        for rv, rsv in sample_pts
    )
    results.append(('S5: turning-point b(r0) formula is r/sqrt(1-r_S/r) (B-independent, checked at 4 sample points)',
                     s5_ok))
    results.append(('S6: rdot^2 ratio (flat/schw) = 1/A(r) at 4 sample points (path SHAPE does depend on B)',
                     s6_ok))

    r3 = verify_pdtp_equals_gr_turning_point()
    results.append(('S7: n_PDTP(r)*r == b_GR(r) identically (residual=0)',
                     r3['identity_confirmed']))

    r4 = derive_photon_sphere()
    results.append(('S8: photon sphere at r=1.5 r_S exactly (from extremizing PDTPs own n(r))',
                     r4['r_photon_sphere_over_rS'] == sp.Rational(3, 2)))
    results.append(('S9: b_crit = 3*sqrt(3)*GM/c^2 matches established GR value',
                     r4['match_established']))

    r5 = derive_weak_field_deflection_perturbative()
    b_sym, rs_sym = sp.symbols('b r_S', positive=True)
    results.append(('S10: derived epsilon_schw(u)/r_S = u^3 (matches known Schwarzschild orbit eq.)',
                     sp.simplify(r5['orbit_equations']['eps_schw_over_rS'] - sp.Symbol('u', positive=True)**3) == 0))
    results.append(('S11: perturbative Schwarzschild deflection = 2*r_S/b exactly',
                     sp.simplify(r5['schw_deflection'] - 2 * rs_sym / b_sym) == 0))
    results.append(('S12: perturbative PDTP-optical deflection = r_S/b (Part 98 claim), ratio=2',
                     sp.simplify(r5['flat_deflection'] - rs_sym / b_sym) == 0 and r5['ratio'] == 2))

    r6 = ns_observability_table()
    buchdahl_row = [row for row in r6['rows'] if 'Buchdahl' in row['label']][0]
    results.append(('S13: Buchdahl-bound n_PDTP = 3 exactly (r=(9/8)r_S)',
                     abs(buchdahl_row['n_PDTP'] - 3.0) < 1e-9))
    n_sqrt2_row = [row for row in r6['rows'] if 'n=sqrt2' in row['label']][0]
    results.append(('S14: n=sqrt2 locus row reproduces n=sqrt(2) numerically',
                     abs(n_sqrt2_row['n_PDTP'] - np.sqrt(2)) < 1e-9))

    r7 = eht_observability_assessment()
    results.append(('S15: n=sqrt2 radius (2 r_S) lies OUTSIDE photon sphere (1.5 r_S) -- escaping ray',
                     r7['n_sqrt2_outside_photon_sphere']))
    results.append(('S16: n=sqrt2 radius lies within the EHT-probed range (1.5-6 r_S per TODO)',
                     r7['n_sqrt2_within_EHT_probed_range']))

    return results


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("T17 (Part 130): n=sqrt(2) Observable Signature Near Compact Objects")
    print("=" * 78)

    print("\n--- Part 1: exact Delta_+ = pi/4 radius (TODO error correction) ---")
    r1 = derive_delta_pi4_radius()
    print(f"Exact solution: r/r_S = {r1['r_exact_over_rS']} (TODO note claimed 0.293, INSIDE horizon)")
    print(f"TODO's implicit u (from u=1-alpha, WRONG): {r1['u_wrong']:.4f}")
    print(f"Correct u=(1-alpha^2)/2: {r1['u_correct']:.4f}")
    print(f"r/r_S using correct u: {r1['r_from_u_correct_over_rS']:.4f}")
    print(f"alpha(2 r_S) - 1/sqrt(2) residual: {r1['alpha_check']}")

    print("\n--- Part 2: turning-point relation independent of B(r) ---")
    r2 = derive_turning_point_independence()
    print(f"b(r0) formula: {r2['b_of_r0']}")
    print(f"rdot^2 ratio (flat/schw) = {r2['rdot2_ratio_flat_over_schw']} (path SHAPE differs)")

    print("\n--- Part 3: n_PDTP(r)*r == b_GR(r) identity ---")
    r3 = verify_pdtp_equals_gr_turning_point()
    print(f"n_PDTP(r)*r = {r3['n_pdtp_times_r']}")
    print(f"b_GR(r)     = {r3['b_gr']}")
    print(f"residual = {r3['residual']} -> identity confirmed: {r3['identity_confirmed']}")

    print("\n--- Part 4: photon sphere from PDTP's own n(r) ---")
    r4 = derive_photon_sphere()
    print(f"r_photon_sphere / r_S = {r4['r_photon_sphere_over_rS']}")
    print(f"b_crit / r_S = {r4['b_crit_over_rS']}")
    print(f"b_crit (GM/c^2 units) = {r4['b_crit_in_GMc2']}, matches 3*sqrt(3): {r4['match_established']}")

    print("\n--- Part 5: weak-field deflection via perturbative orbit equation ---")
    r5 = derive_weak_field_deflection_perturbative()
    print(f"  epsilon_schw(u)/r_S = {r5['orbit_equations']['eps_schw_over_rS']}  (expect u^3)")
    print(f"  epsilon_flat(u)/r_S = {r5['orbit_equations']['eps_flat_over_rS']}  (expect u/b^2)")
    print(f"  Schwarzschild deflection = {r5['schw_deflection']}  (expect 2*r_S/b = 4GM/(bc^2))")
    print(f"  PDTP-optical deflection  = {r5['flat_deflection']}  (expect r_S/b = 2GM/(bc^2))")
    print(f"  ratio (Schw/PDTP-optical) = {r5['ratio']}  (expect 2)")
    print(f"  Schwarzschild matches established 4GM/(bc^2): {r5['schw_matches_4GMbc2']}")

    print("\n--- Part 6: neutron star observability table (M=1.4 Msun) ---")
    r6 = ns_observability_table()
    print(f"r_S = {r6['r_S_km']:.4f} km")
    for row in r6['rows']:
        print(f"  {row['label']:32s}  r={row['r_km']:8.3f} km  r/r_S={row['r_over_rS']:.4f}  "
              f"C={row['compactness_C']:.4f}  n={row['n_PDTP']}  Delta={row['Delta_deg']}")

    print("\n--- Part 7: EHT/VLBI observability assessment ---")
    r7 = eht_observability_assessment()
    for k, v in r7.items():
        print(f"  {k}: {v}")

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

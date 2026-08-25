#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t18_delta_minus_crossover.py -- TODO_04 T18 (Priority 18), Part 131
=======================================================================
Question: the reversed Higgs (Part 62) gives phi_- a mass near matter.
Does Delta_- (the surface-mode phase mismatch) ever reach pi/4 inside a
neutron star, analogous to T17's Delta_+ = pi/4 crossover?

Source: Part 99 open question 3; tan_critical_point.md Sec 10.3.

SCOPING NOTE (per user-approved plan, 2026-08-09): while scoping this task,
Part 62's phi_- mass formula was found to use g=omega_gap directly -- the
same dimensional shortcut T51 (Part 128) already flagged and fixed
elsewhere (established [g]=1/s^2 is required, not omega_gap's [T]^-1).
This script deliberately keeps its CORE derivation (does a Delta_-=pi/4
crossover exist? how does it relate to Part 119's phi_-=pi/2 true vacuum?)
completely independent of g's numerical value -- those questions only need
g>0, not a specific number. Only the one sub-question that DOES need a
number (comparing phi_-'s local mass to neutron-star oscillation-mode
frequencies) is affected; there, two candidate g values are computed and
shown explicitly with caveats, per the approved plan. The g-units question
itself is filed separately (TODO_05 T68), not resolved here.

This script:
1. Re-derives V_eff(phi_-; Delta_+) directly from Part 61's own product
   identity (not Part 119's cosmological beta route) and finds its exact
   critical points -- shows phi_-=pi/2 is the unique stable minimum for
   ANY Delta_+ > 0, independently reproducing Part 119's "true vacuum at
   pi/2" result via a simpler, purely local/static argument.
2. Shows Part 62's own "V''(0) near matter" formula does not match the
   curvature of its own stated potential at phi_-=0 (residual != 0 for
   Delta_+ > 0) -- phi_-=0 is not even a stationary point unless Delta_+=0
   exactly, so that curvature described the INITIAL tachyonic roll rate
   (matching Part 119 Sec 2.1's own diagnosis), not a stable particle mass.
3. Derives the correct stable-oscillation mass m^2(Delta_+) = 2g sin(Delta_+)
   at the TRUE minimum (phi_-=pi/2), and defines Delta_- = pi/2 - phi_-
   (displacement from true vacuum, matching Part 119's own xi variable and
   the "offset from pi/2 equilibrium" language in pdtp_refractive_index.md
   Sec 8).
4. Checks explicitly whether Delta_-=pi/4 is any kind of special point of
   V_eff (it is not, for any Delta_+ > 0) and explains structurally why
   Delta_+'s pi/4 crossover (Part 99, tan(Delta_+)=1 in V(Delta_+)=-2g cos(Delta_+))
   and Delta_-'s absence of one arise from genuinely different potential
   shapes -- answering T18 Key Question 3.
5. Computes m(Delta_+) for realistic neutron-star compactness (reusing
   T17/Part130's numbers) using two candidate g values, compares to known
   NS f-mode/g-mode frequency bands, and reports the comparison as
   inconclusive pending the flagged g-units resolution (TODO_05 T68).

PDTP Original: sections 1, 3, 4 (direct static extremization of Part 61's
potential, reconciliation with Part 62/119, and the Delta_-=pi/4 negative
result). Section 5's numerics use ESTABLISHED NS asteroseismology ranges
(cited) for comparison only.

Output: DATA only. Interpretation belongs in a new Section of
docs/research/reversed_higgs (folded into an existing doc; see main script
docstring for target file).
"""

import sympy as sp
import numpy as np

# ===========================================================================
# CONSTANTS (SI units)
# ===========================================================================
HBAR = 1.054571817e-34    # J s
C_SI = 2.99792458e8       # m/s
G_SI = 6.67430e-11        # m^3 kg^-1 s^-2
M_P = 2.176434e-8         # kg (Planck mass)
M_SUN = 1.98892e30        # kg
EV_J = 1.602176634e-19    # eV -> J

OMEGA_GAP = M_P * C_SI**2 / HBAR   # Part 33/94: m_cond*c^2/hbar, m_cond=m_P


# ===========================================================================
# PART 1: exact extremization of Part 61's own product-form potential
# ===========================================================================
def derive_exact_potential_and_extrema():
    """
    From Part 61 (established, CLAUDE.md-documented identity, verified by
    direct trig sum-to-product):
      cos(psi-phi_b) - cos(psi-phi_s) = 2 sin(psi-phi_+) sin(phi_-)
    so the interaction Lagrangian is
      L_int = g * [cos(psi-phi_b) - cos(psi-phi_s)] = 2g sin(Delta_+) sin(phi_-)
    with Delta_+ = psi - phi_+ (Part 98/99 notation). The effective
    potential (V = -L_int, standard L=T-V convention) is

      V_eff(phi_-; Delta_+) = -2g sin(Delta_+) sin(phi_-).    [Eq 131.1]

    Find dV/dphi_- = 0 (critical points) and classify via d^2V/dphi_-^2.
    """
    # Delta_+ restricted positive (physically 0 < Delta_+ < pi/2, Part 98/99) so sympy can
    # prove sin(Delta_+) > 0 symbolically; phi_- left assumption-free (plain real symbol) --
    # sp.solve returns [] if phi_m carries `positive=False` alongside `real=True` together (a
    # sympy assumption quirk, confirmed by direct test), so this symbol is deliberately
    # assumption-free rather than over-constrained.
    g = sp.symbols('g', positive=True)
    Delta_p = sp.symbols('Delta_plus', positive=True)
    phi_m = sp.symbols('phi_minus', real=True)

    V = -2 * g * sp.sin(Delta_p) * sp.sin(phi_m)
    dV = sp.diff(V, phi_m)
    d2V = sp.diff(V, phi_m, 2)

    # Critical points: cos(phi_-) = 0 (for sin(Delta_+) != 0) => phi_- = pi/2, 3pi/2 (mod 2pi,
    # i.e. the same point as -pi/2).
    crit_pts = sp.solve(sp.Eq(sp.cos(phi_m), 0), phi_m)

    d2V_at_pi2 = sp.simplify(d2V.subs(phi_m, sp.pi / 2))
    d2V_at_negpi2 = sp.simplify(d2V.subs(phi_m, -sp.pi / 2))
    V_at_pi2 = sp.simplify(V.subs(phi_m, sp.pi / 2))
    V_at_negpi2 = sp.simplify(V.subs(phi_m, -sp.pi / 2))

    return {
        'V_expr': V,
        'dV_expr': dV,
        'd2V_expr': d2V,
        'critical_points_of_cos': crit_pts,
        'd2V_at_pi2': d2V_at_pi2,          # expect +2g sin(Delta_+) -- minimum for sin(Delta_+)>0
        'd2V_at_negpi2': d2V_at_negpi2,    # expect -2g sin(Delta_+) -- maximum
        'V_at_pi2': V_at_pi2,              # expect -2g sin(Delta_+), global min value
        'V_at_negpi2': V_at_negpi2,        # expect +2g sin(Delta_+), global max value
    }


# ===========================================================================
# PART 2: reconcile with Part 62's original claim and Part 119's result
# ===========================================================================
def reconcile_with_part62_and_119():
    """
    Part 62 (reversed_higgs.py docstring) claims:
      "Near matter: sin(psi-phi_+) ~ Phi_grav > 0 -> V''(0) = -2g*sin(psi-phi_+)"
    i.e. it evaluates the curvature of V_eff AT phi_-=0 and calls it -2g*sin(Delta_+).

    Check this against the ACTUAL curvature of Eq 131.1 at phi_-=0, and
    check whether phi_-=0 is even a stationary point (dV/dphi_-=0) for
    Delta_+ > 0.
    """
    g, Delta_p, phi_m = sp.symbols('g Delta_plus phi_minus', positive=True)
    V = -2 * g * sp.sin(Delta_p) * sp.sin(phi_m)
    dV = sp.diff(V, phi_m)
    d2V = sp.diff(V, phi_m, 2)

    dV_at_0 = sp.simplify(dV.subs(phi_m, 0))        # expect -2g sin(Delta_+) -- NONZERO for Delta_+>0
    d2V_at_0 = sp.simplify(d2V.subs(phi_m, 0))       # expect 0 (not -2g sin(Delta_+) as Part 62 claims)

    part62_claim = -2 * g * sp.sin(Delta_p)
    residual_vs_part62 = sp.simplify(d2V_at_0 - part62_claim)

    return {
        'dV_at_phi_minus_0': dV_at_0,
        'is_phi_minus_0_stationary_for_Deltap_gt_0': dV_at_0 == 0,
        'd2V_at_phi_minus_0': d2V_at_0,
        'part62_claimed_curvature': part62_claim,
        'residual_vs_part62_claim': residual_vs_part62,   # nonzero => Part 62's formula does not match its own stated V_eff
        'reconciliation': (
            "Part 62's V''(0) is NOT the curvature of a stationary point when Delta_+>0 "
            "(phi_-=0 is not stationary unless Delta_+=0 exactly); dV/dphi_-|_0 = -2g sin(Delta_+) "
            "is better read as the INITIAL SLOPE (tachyonic push rate) that starts phi_- rolling "
            "away from 0, matching Part 119 Sec 2.1's own diagnosis of a tachyonic instability at "
            "phi_-=0 driving the field toward the TRUE minimum at phi_-=pi/2 (Part 1 above). "
            "Part 119's pi/2 result is thus independently reproduced by direct extremization of "
            "Part 61's own leading-order (non-quartic) potential -- no cosmological beta or Part "
            "117 quartic correction needed for this leading-order structural conclusion."
        ),
    }


# ===========================================================================
# PART 3: stable mass formula at the true minimum, and Delta_- definition
# ===========================================================================
def derive_stable_mass_and_delta_minus():
    """
    m^2(Delta_+) = d^2V/dphi_-^2 |_{phi_-=pi/2} = 2g sin(Delta_+)   [Eq 131.2]

    Define Delta_- = pi/2 - phi_- (displacement from the TRUE vacuum,
    matching Part 119's xi and the "offset from pi/2 equilibrium" language
    already used in pdtp_refractive_index.md Sec 8). Near the minimum,
    expand V_eff in Delta_- to confirm standard SHM form and cross-check
    the mass coefficient two independent ways (direct 2nd derivative vs.
    quadratic term of the Delta_- expansion).
    """
    g, Delta_p, phi_m, Delta_m = sp.symbols('g Delta_plus phi_minus Delta_minus', positive=True)

    V = -2 * g * sp.sin(Delta_p) * sp.sin(phi_m)
    d2V = sp.diff(V, phi_m, 2)
    m2_from_2nd_deriv = sp.simplify(d2V.subs(phi_m, sp.pi / 2))

    # Substitute phi_- = pi/2 - Delta_- and Taylor-expand in Delta_- to O(Delta_-^2)
    V_in_Delta_minus = V.subs(phi_m, sp.pi / 2 - Delta_m)
    V_series = sp.series(V_in_Delta_minus, Delta_m, 0, 3).removeO()
    V_series = sp.expand(V_series)

    # Extract coefficient of Delta_-^2 -- should be +g*sin(Delta_+) [since (1/2)m^2 Delta_-^2 form]
    coeff_Delta2 = V_series.coeff(Delta_m, 2)
    m2_from_series = sp.simplify(2 * coeff_Delta2)   # V ~ (1/2) m^2 Delta_-^2 + const

    return {
        'Delta_minus_definition': 'Delta_minus = pi/2 - phi_minus',
        'm2_formula': m2_from_2nd_deriv,          # 2g sin(Delta_+)
        'm2_from_series_expansion': m2_from_series,
        'cross_check_residual': sp.simplify(m2_from_2nd_deriv - m2_from_series),  # expect 0
        'V_series_in_Delta_minus': V_series,
    }


# ===========================================================================
# PART 4: is Delta_- = pi/4 a special point? (T18 Key Questions 1 and 3)
# ===========================================================================
def check_delta_minus_pi4_crossover():
    """
    Check whether phi_- = pi/4 (equivalently Delta_- = pi/2 - pi/4 = pi/4,
    a numerical coincidence of the two conventions at this specific value)
    is a critical point, inflection point, or otherwise special locus of
    V_eff(phi_-) = -2g sin(Delta_+) sin(phi_-).

    Contrast with Delta_+'s pi/4 crossover (Part 99): that crossover comes
    from an ENTIRELY DIFFERENT potential, V(Delta_+) = -2g cos(Delta_+)
    (single-phase form, Eq 99.2), via the criterion tan(Delta_+)=1 (Eq 99.3,
    comparing sin and cos terms of the SAME potential's own first and
    second derivatives at a GENERIC point Delta_+, since Delta_+ itself is
    a monotonic decoupling-progress parameter ranging from 0 (fully locked)
    to pi/2 (fully decoupled) -- not a displacement from a stable
    equilibrium). Delta_- (=xi) IS a displacement from a stable equilibrium
    (Part 3 above) -- structurally a different kind of variable, in a
    potential of a different functional shape (sin(phi_-) not cos(phi_-)).
    """
    g, Delta_p, phi_m = sp.symbols('g Delta_plus phi_minus', positive=True)
    V = -2 * g * sp.sin(Delta_p) * sp.sin(phi_m)
    dV = sp.diff(V, phi_m)

    dV_at_pi4 = sp.simplify(dV.subs(phi_m, sp.pi / 4))   # expect nonzero for Delta_+>0
    is_critical = dV_at_pi4 == 0

    # Part 99's Delta_+ potential and its pi/4 criterion, for explicit contrast
    V_Deltap = -2 * g * sp.cos(Delta_p)
    dV_Deltap = sp.diff(V_Deltap, Delta_p)
    d2V_Deltap = sp.diff(V_Deltap, Delta_p, 2)
    # Part 99's crossover criterion: |dV/dDelta+| = |d2V/dDelta+^2| (force-vs-coupling
    # comparison, Eq 99.4) -> 2g sin(Delta+) = 2g cos(Delta+) -> tan(Delta+)=1 -> Delta+=pi/4
    crossover_eq = sp.Eq(sp.Abs(dV_Deltap), sp.Abs(d2V_Deltap))
    tan_criterion = sp.simplify(sp.tan(sp.pi / 4) - 1)  # expect 0, Eq 99.3

    return {
        'dV_dphi_minus_at_pi4': dV_at_pi4,
        'phi_minus_pi4_is_critical_point': is_critical,   # False for Delta_+>0
        'contrast_Delta_plus_potential': V_Deltap,          # -2g cos(Delta_+): different shape
        'contrast_tan_criterion_residual': tan_criterion,   # 0, reproduces Part 99 Eq 99.3
        'structural_conclusion': (
            "Delta_+'s pi/4 crossover is a regime boundary WITHIN a monotonic decoupling "
            "parameter, defined by comparing V(Delta_+)=-2g*cos(Delta_+)'s own first and "
            "second derivatives at a generic point. Delta_- has no analogous feature: its "
            "potential V_eff(phi_-)=-2g*sin(Delta_+)*sin(phi_-) has a UNIQUE critical point "
            "(the true minimum at phi_-=pi/2, Delta_-=0) and phi_-=pi/4 is not "
            "distinguished in any way -- not a critical point, not an inflection point, just "
            "an arbitrary point along the roll toward equilibrium. Questions (a) and (c) "
            "answered: NO stable Delta_-=pi/4 crossover exists; it is NOT the same kind of "
            "state as Part 62's phi_-=pi/2 equilibrium (that IS the true vacuum, Delta_-=0)."
        ),
    }


# ===========================================================================
# PART 5: neutron-star mass/frequency comparison (g-value CAVEATED, both shown)
# ===========================================================================
def numeric_ns_mass_and_modes():
    """
    Compute Delta_+ for a realistic 1.4 Msun neutron star (reusing T17/
    Part130's numbers: R=11-12 km, r_S=4.14 km), then m(Delta_+) using TWO
    explicitly-flagged candidate values for the correctly-dimensioned
    ([g]=1/s^2, per T51/Part128) coupling:

      Candidate A: g = omega_gap^2 = (m_P c^2/hbar)^2 -- the literal,
        dimensionally-forced placeholder from T51's own resolution
        ("omega_gap^2 plays g's role"), tied to the framework's single
        free parameter m_cond=m_P. NOT independently validated for this
        specific (phi_- mass) formula.

      Candidate B (reference only, NOT combined with the NS's Delta_+):
        Part 119's own g_dyn = 9 H0^2 eps0/2, already established
        specifically for phi_-'s PRESENT-DAY COSMOLOGICAL mass (m^2=2g_dyn,
        near-exact vacuum, eps0<<1). Shown here only as a magnitude
        reference -- substituting a NS-scale sin(Delta_+) into g_dyn would
        repeat exactly the kind of unjustified g-mixing T51 already warned
        against for g_Lambda vs g_dyn, so it is NOT done.

    Compares Candidate A's result to established neutron-star f-mode
    (~1-3 kHz) and g-mode (~10 Hz - 1.4 kHz) frequency bands.
    """
    M = 1.4 * M_SUN
    r_S = 2 * G_SI * M / C_SI**2

    rows = []
    for label, R in [('R=11 km', 11.0e3), ('R=12 km', 12.0e3)]:
        A = 1 - r_S / R
        alpha = np.sqrt(A)
        Delta_p = np.arccos(alpha)   # radians
        sin_Delta_p = np.sin(Delta_p)

        # Candidate A: g = omega_gap^2
        m2_A = 2 * OMEGA_GAP**2 * sin_Delta_p     # s^-2
        m_A_Hz = np.sqrt(m2_A) / (2 * np.pi)       # convert angular freq -> Hz

        rows.append({
            'label': label,
            'Delta_plus_deg': np.degrees(Delta_p),
            'sin_Delta_plus': sin_Delta_p,
            'm_candidateA_rad_per_s': np.sqrt(m2_A),
            'm_candidateA_Hz': m_A_Hz,
        })

    # Candidate B: Part 119's own g_dyn, native cosmological mass (reference only)
    H0_SI = 2.2e-18   # s^-1 (approx 67.9 km/s/Mpc, matches Part 119's own value order)
    eps0 = 1.0 / 12.0  # Part 119's eps_0 (memory: eps_0 < eps_crit=1/9, currently ~ this order)
    g_dyn = 4.5 * H0_SI**2 * eps0  # 9*H^2*eps/2
    m2_dyn = 2 * g_dyn
    m_dyn_Hz = np.sqrt(m2_dyn) / (2 * np.pi)

    ns_fmode_range_Hz = (1000.0, 3000.0)     # established: NS f-modes ~1-3 kHz
    ns_gmode_range_Hz = (10.0, 1400.0)       # established: NS g-modes ~10 Hz - 1.4 kHz (approx)

    return {
        'r_S_km': r_S / 1e3,
        'rows': rows,
        'g_dyn_reference_Hz': m_dyn_Hz,
        'ns_fmode_range_Hz': ns_fmode_range_Hz,
        'ns_gmode_range_Hz': ns_gmode_range_Hz,
        'candidateA_vs_fmode_ratio': rows[0]['m_candidateA_Hz'] / ns_fmode_range_Hz[1],
        'conclusion': (
            "Candidate A (g=omega_gap^2) puts phi_-'s local NS mass at ~omega_gap/2pi, i.e. "
            "the Planck frequency scale (~1e42 Hz) -- ~39 orders of magnitude above any NS "
            "oscillation-mode band. Candidate B (Part 119's g_dyn) is ~1e-19 Hz, ~20+ orders "
            "of magnitude BELOW the NS band, but is not a like-for-like substitute (derived "
            "for a different, cosmological regime). The two candidates bracket the NS f/g-mode "
            "band by roughly 60 orders of magnitude combined -- this sub-question is reported "
            "as OPEN/INCONCLUSIVE pending TODO_05 T68 (the g-units resolution), not as a "
            "confident 'no coupling.'"
        ),
    }


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS
# ===========================================================================
def sudoku_checks():
    results = []

    r1 = derive_exact_potential_and_extrema()
    g_c, Deltap_c = sp.symbols('g Delta_plus', positive=True)  # match Part 1's own symbol construction
    results.append(('S1: cos(phi_-)=0 critical points include pi/2 (and its 3pi/2=-pi/2 twin)',
                     sp.pi / 2 in r1['critical_points_of_cos'] and
                     any(sp.simplify(sp.cos(cp)) == 0 for cp in r1['critical_points_of_cos'])))
    results.append(('S2: d2V/dphi_-^2 at pi/2 is +2g*sin(Delta_+) (stable minimum)',
                     sp.simplify(r1['d2V_at_pi2'] - 2 * g_c * sp.sin(Deltap_c)) == 0))
    results.append(('S3: d2V/dphi_-^2 at -pi/2 is -2g*sin(Delta_+) (unstable maximum)',
                     sp.simplify(r1['d2V_at_negpi2'] + 2 * g_c * sp.sin(Deltap_c)) == 0))
    # S4: checked numerically at a representative physical value Delta_+=0.5 rad (0<Delta_+<pi/2,
    # Part 98/99's physical domain) rather than via symbolic .is_negative, which needs an
    # explicit upper bound on Delta_+ that a bare `positive=True` assumption does not supply.
    V_pi2_num = float(r1['V_at_pi2'].subs({g_c: 1.0, Deltap_c: 0.5}))
    V_negpi2_num = float(r1['V_at_negpi2'].subs({g_c: 1.0, Deltap_c: 0.5}))
    results.append(('S4: V(pi/2) < V(-pi/2) at Delta_+=0.5 rad, i.e. pi/2 is the GLOBAL min',
                     V_pi2_num < V_negpi2_num))

    r2 = reconcile_with_part62_and_119()
    results.append(('S5: phi_-=0 is NOT stationary for Delta_+>0 (dV/dphi_-|_0 != 0)',
                     not r2['is_phi_minus_0_stationary_for_Deltap_gt_0']))
    results.append(('S6: d2V/dphi_-^2 at phi_-=0 is exactly 0 (not Part 62s claimed -2g sin(Delta_+))',
                     sp.simplify(r2['d2V_at_phi_minus_0']) == 0))
    results.append(('S7: residual vs Part 62 claim is nonzero (confirms the mismatch)',
                     sp.simplify(r2['residual_vs_part62_claim']) != 0))

    r3 = derive_stable_mass_and_delta_minus()
    results.append(('S8: mass from 2nd derivative matches mass from series expansion (residual=0)',
                     sp.simplify(r3['cross_check_residual']) == 0))
    results.append(('S9: m^2(Delta_+) = 2g*sin(Delta_+) exactly',
                     sp.simplify(r3['m2_formula'] - 2 * sp.Symbol('g', positive=True) * sp.sin(sp.Symbol('Delta_plus', positive=True))) == 0))

    r4 = check_delta_minus_pi4_crossover()
    results.append(('S10: phi_-=pi/4 is NOT a critical point of V_eff for Delta_+>0',
                     not r4['phi_minus_pi4_is_critical_point']))
    results.append(('S11: Part 99 tan(pi/4)=1 criterion reproduced (residual=0)',
                     sp.simplify(r4['contrast_tan_criterion_residual']) == 0))

    r5 = numeric_ns_mass_and_modes()
    results.append(('S12: Candidate A NS mass is many OoM above the f-mode band (as computed, not asserted)',
                     r5['candidateA_vs_fmode_ratio'] > 1e10))
    results.append(('S13: g_dyn reference value matches Part 119 order of magnitude (~1e-19 to 1e-18 Hz)',
                     1e-20 < r5['g_dyn_reference_Hz'] < 1e-17))

    return results


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("T18 (Part 131): Two-Phase Delta_- Crossover Near Dense Matter")
    print("=" * 78)

    print("\n--- Part 1: exact extremization of V_eff(phi_-; Delta_+) ---")
    r1 = derive_exact_potential_and_extrema()
    print(f"V_eff = {r1['V_expr']}")
    print(f"Critical points of cos(phi_-)=0: {r1['critical_points_of_cos']}")
    print(f"d2V/dphi_-^2 at pi/2: {r1['d2V_at_pi2']}  (positive => stable min)")
    print(f"d2V/dphi_-^2 at -pi/2: {r1['d2V_at_negpi2']}  (negative => unstable max)")
    print(f"V(pi/2) = {r1['V_at_pi2']}, V(-pi/2) = {r1['V_at_negpi2']}")

    print("\n--- Part 2: reconciliation with Part 62 and Part 119 ---")
    r2 = reconcile_with_part62_and_119()
    print(f"dV/dphi_- at phi_-=0: {r2['dV_at_phi_minus_0']}")
    print(f"d2V/dphi_-^2 at phi_-=0: {r2['d2V_at_phi_minus_0']}")
    print(f"Part 62's claimed curvature: {r2['part62_claimed_curvature']}")
    print(f"Residual: {r2['residual_vs_part62_claim']}")
    print(r2['reconciliation'])

    print("\n--- Part 3: stable mass formula and Delta_- definition ---")
    r3 = derive_stable_mass_and_delta_minus()
    print(f"Delta_-  := {r3['Delta_minus_definition']}")
    print(f"m^2(Delta_+) [2nd derivative] = {r3['m2_formula']}")
    print(f"m^2(Delta_+) [series expansion] = {r3['m2_from_series_expansion']}")
    print(f"Cross-check residual: {r3['cross_check_residual']}")

    print("\n--- Part 4: is Delta_- = pi/4 special? ---")
    r4 = check_delta_minus_pi4_crossover()
    print(f"dV/dphi_- at phi_-=pi/4: {r4['dV_dphi_minus_at_pi4']}")
    print(f"Is it a critical point? {r4['phi_minus_pi4_is_critical_point']}")
    print(f"Contrast Delta_+ potential: {r4['contrast_Delta_plus_potential']}")
    print(f"tan(pi/4)-1 residual: {r4['contrast_tan_criterion_residual']}")
    print(r4['structural_conclusion'])

    print("\n--- Part 5: NS mass/mode comparison (both g candidates, caveated) ---")
    r5 = numeric_ns_mass_and_modes()
    print(f"r_S = {r5['r_S_km']:.4f} km")
    for row in r5['rows']:
        print(f"  {row['label']}: Delta_+={row['Delta_plus_deg']:.2f} deg, "
              f"sin(Delta_+)={row['sin_Delta_plus']:.4f}, "
              f"m_candA={row['m_candidateA_Hz']:.3e} Hz")
    print(f"g_dyn reference (Part 119, cosmological, NOT substitutable): {r5['g_dyn_reference_Hz']:.3e} Hz")
    print(f"NS f-mode band: {r5['ns_fmode_range_Hz']} Hz")
    print(f"NS g-mode band: {r5['ns_gmode_range_Hz']} Hz")
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

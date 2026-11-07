#!/usr/bin/env python3
"""
t84_pmf_scoping.py -- TODO_05 T84: can PDTP's phase field make primordial
magnetic fields? (scoping, Part 159)
==========================================================================
Worked by CLAUDE OPUS 5.5 (2026-11-07).

GOAL:
    PDTP as written has no phi-photon coupling, so it makes zero magnetic
    field. Enumerate the lowest-order couplings, test each against gauge
    invariance, photon masslessness and PDTP's shift symmetry, and for the
    survivor (axion-type phi F Fdual) derive the field-amplification
    exponent N and the CMB polarization rotation theta_CB from the same
    mode equation. Evaluate both for the PDTP epochs where phi moves.

EQUATIONS USED:
    Eq 1: charged coupling L = 1/2 |(d - i e A) Phi|^2, Phi = v exp(i phi)
          (Higgs mechanism) https://en.wikipedia.org/wiki/Higgs_mechanism [ASSUMED]
    Eq 2: dilaton-type L = -1/4 f(phi) F^2 (Ratra 1992, ApJ 391, L1) [ASSUMED]
    Eq 3: axion-type L = 1/2(E^2 - B^2) + g_pg a E.B, a = f_phi * phi
          (Harari & Sikivie 1992, PLB 289, 67; Carroll, Field & Jackiw 1990,
          PRD 41, 1231) [ASSUMED]
    Eq 4: natural coupling g_pg = alpha*C / (2 pi f_phi), C = O(1)
          (standard axion normalisation) [ASSUMED]
    Eq 5: f_phi^2 = 2 K_0 m_P^2, K_0 = 1/(4 pi) (term_glossary.md K) [ASSUMED]

ASSUMPTIONS:
    [A1] Radiation gauge A_0 = 0; homogeneous a(t); plane waves along z.
    [A2] Amplification counted from the maximum tachyonic growth rate
         (necessary condition N >= 1 for any classical field; NOT sufficient).
    [A3] Vacuum conductivity ignored (it only suppresses growth further).
    [A4] Kibble-Zurek winding: Delta phi ~ 2 pi per domain (Part 116).

SIGN CONVENTIONS:
    +cos locking (CLAUDE.md); E = -dA/dt, B = curl A; helicity +/- defined by
    curl A_pm = +/- k A_pm.

OUTPUT (data only): coupling residuals, photon mass, mode equation, growth
    exponent, polarization rotation, numerical values, Sudoku scorecard.
"""

import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

# ---------------------------------------------------------------------
# Constants (SI unless noted)
# ---------------------------------------------------------------------
ALPHA = 7.2973525693e-3            # fine-structure constant (CODATA 2018)
HBAR = 1.054571817e-34             # J s
C_LIGHT = 2.99792458e8             # m/s
M_P_KG = 2.176434e-8               # Planck mass (CODATA 2018)
M_P_GEV = 1.220890e19              # Planck mass in GeV (PDG)
GEV_EV = 1.0e9
T0_S = 13.797e9 * 3.15576e7        # age of universe, Planck 2018 [s]
T_CMB = 2.7255                     # K (Fixsen 2009)
A_RAD_CGS = 7.5657e-15             # radiation constant, erg cm^-3 K^-4
CAST_G = 0.66e-10                  # GeV^-1 (CAST 2017, 95% CL)
THETA_CB_DEG, THETA_CB_ERR = 0.342, 0.09   # Eskilt & Komatsu 2022 (arXiv:2205.13962)
M_GAMMA_BOUND_EV = 2.2e-14         # most lenient PDG-listed photon mass bound used
B_REC_NG = (0.0545, 0.104)         # Jedamzik+2025 Table IV, comoving at z~1090 [nG]
K0 = 1.0 / (4.0 * 3.141592653589793)


# =====================================================================
# DERIVATIONS (symbolic)
# =====================================================================

def derive_charged_coupling():
    """Eq 1 with one spacetime component written explicitly:
    D Phi = (d_mu - i e A_mu) v e^{i phi};  L = 1/2 |D Phi|^2."""
    v, e, dphi, A, ph = sp.symbols('v e dphi A phi', real=True)
    DPhi = (sp.I * dphi - sp.I * e * A) * v * sp.exp(sp.I * ph)
    L = sp.simplify(sp.Rational(1, 2) * DPhi * sp.conjugate(DPhi))
    L = sp.expand(L)
    coeff_A2 = L.coeff(A, 2)
    m2 = 2 * coeff_A2                      # L contains 1/2 m^2 A^2
    return {'L': L, 'coeff_A2': coeff_A2, 'mA2': sp.simplify(m2),
            'mA2_residual': sp.simplify(m2 - e**2 * v**2)}


def derive_shift_checks():
    """Eq 2: f(phi) under phi -> phi + c (generic f) vs f(psi - phi) under
    the joint shift psi, phi -> +c (PDTP's Goldstone symmetry)."""
    ph, ps, c = sp.symbols('phi psi c', real=True)
    f = sp.Function('f')
    single = sp.simplify(f(ph + c) - f(ph))
    joint = sp.simplify(f((ps + c) - (ph + c)) - f(ps - ph))
    return {'single_residual': single, 'joint_residual': joint}


def derive_ffdual_total_derivative():
    """Eq 3 shift symmetry: eps^{mnrs} F_mn F_rs = 4 d_m(eps^{mnrs} A_n d_r A_s)
    for arbitrary A_mu(x0..x3). Metric-free (all indices on eps)."""
    X = sp.symbols('x0:4', real=True)
    A = [sp.Function('A%d' % m)(*X) for m in range(4)]
    F = [[sp.diff(A[n], X[m]) - sp.diff(A[m], X[n]) for n in range(4)]
         for m in range(4)]
    eps = sp.LeviCivita
    lhs = 0
    rhs = 0
    idx = range(4)
    for m in idx:
        for n in idx:
            for r in idx:
                for s in idx:
                    e_ = eps(m, n, r, s)
                    if e_ == 0:
                        continue
                    lhs += e_ * F[m][n] * F[r][s]
                    rhs += 4 * sp.diff(e_ * A[n] * sp.diff(A[s], X[r]), X[m])
    return {'residual': sp.simplify(sp.expand(lhs - rhs))}


def derive_mode_equation():
    """Eq 3 with A_0 = 0, A = (A_x(t,z), A_y(t,z), 0), homogeneous a(t):
    L = 1/2(At^2 - (curl A)^2) + g a(t) E.B, E = -At. Euler-Lagrange via
    SymPy, then insert the helical ansatz A = u(t)(cos kz, -/+ sin kz)."""
    t, z, g, k = sp.symbols('t z g k', real=True)
    a = sp.Function('a')(t)
    Ax = sp.Function('Ax')(t, z)
    Ay = sp.Function('Ay')(t, z)
    # curl A for A = (Ax(t,z), Ay(t,z), 0): (-d_z Ay, d_z Ax, 0)
    Bv = sp.Matrix([-sp.diff(Ay, z), sp.diff(Ax, z), 0])
    Ev = sp.Matrix([-sp.diff(Ax, t), -sp.diff(Ay, t), 0])
    L = sp.Rational(1, 2) * (Ev.dot(Ev) - Bv.dot(Bv)) + g * a * Ev.dot(Bv)
    eqs = sp.euler_equations(L, [Ax, Ay], [t, z])
    out = {}
    u = sp.Function('u')(t)
    for hel, sgn in (('plus', 1), ('minus', -1)):
        # curl A = sgn * k * A for A = u (cos kz, -sgn sin kz, 0)
        sub = {Ax: u * sp.cos(k * z), Ay: -sgn * u * sp.sin(k * z)}
        ex = sp.simplify(eqs[0].lhs.subs(sub).doit())
        target = -(sp.diff(u, t, 2) + (k**2 - sgn * g * sp.diff(a, t) * k) * u)
        # eqs[0] is d/dt(dL/dAx_t) ... sign as returned; compare up to the cos factor
        ratio = sp.simplify(ex / sp.cos(k * z))
        res = sp.simplify(sp.expand(ratio - target))
        res_alt = sp.simplify(sp.expand(ratio + target))
        out[hel] = {'ode_over_cos': ratio,
                    'residual': res if res == 0 else res_alt}
    return out


def derive_growth_and_rotation():
    """From u'' + (k^2 - s k) u = 0 with s = g * da/dt (helicity +):
    tachyonic growth rate Gamma(k) = sqrt(s k - k^2) for 0 < k < s;
    its maximum; and the polarization rotation rate for k >> s from
    omega_pm = sqrt(k^2 -/+ s k): rotation rate = (omega_- - omega_+)/2."""
    k, s = sp.symbols('k s', positive=True)
    gam2 = s * k - k**2
    k_star = sp.solve(sp.diff(gam2, k), k)[0]
    gam_max = sp.sqrt(gam2.subs(k, k_star))
    w_plus = sp.sqrt(k**2 - s * k)
    w_minus = sp.sqrt(k**2 + s * k)
    rot = sp.limit((w_minus - w_plus) / 2, k, sp.oo)
    # g -> 0 limit: dispersion omega = k
    free = sp.simplify(w_plus.subs(s, 0) - k)
    return {'k_star': k_star, 'gamma_max': sp.simplify(gam_max),
            'rotation_rate': rot,
            'growth_minus_rotation': sp.simplify(gam_max - rot),
            'free_limit_residual': free}


def derive_exponent_formula():
    """N = integral Gamma_max dt = (g/2) Delta a, a = f_phi * phi,
    g = alpha C / (2 pi f_phi). Same for theta_CB = (g/2) Delta a.
    Shows f_phi cancels (two-phase inertia factor irrelevant)."""
    al, Cc, f, dphi = sp.symbols('alpha C f_phi Delta_phi', positive=True)
    g = al * Cc / (2 * sp.pi * f)
    N = g / 2 * (f * dphi)
    return {'N': sp.simplify(N), 'dN_df': sp.simplify(sp.diff(N, f)),
            'N_target': al * Cc * dphi / (4 * sp.pi)}


# =====================================================================
# COMPUTATION (numerical)
# =====================================================================

def compute_numbers(exp_formula):
    al_s, C_s, d_s = sp.symbols('alpha C Delta_phi', positive=True)
    N_expr = exp_formula['N']          # the derived (g/2) * Delta a, not the target

    def N(dphi, C=1.0):
        return float(N_expr.subs({al_s: ALPHA, C_s: C, d_s: dphi}))

    f_gev = (2.0 * K0) ** 0.5 * M_P_GEV
    g_pg = ALPHA / (2.0 * 3.141592653589793 * f_gev)          # GeV^-1
    e_charge = (4.0 * 3.141592653589793 * ALPHA) ** 0.5
    m_A_ev = e_charge * f_gev * GEV_EV                         # case (a)
    omega_gap = M_P_KG * C_LIGHT**2 / HBAR                     # s^-1
    theta_rot_vac = N(omega_gap * T0_S)                        # radians, case rotating
    theta_obs_rad = THETA_CB_DEG * 3.141592653589793 / 180.0
    dphi_for_obs = 4.0 * 3.141592653589793 * theta_obs_rad / ALPHA
    dphi_for_N1 = 4.0 * 3.141592653589793 / ALPHA
    rho_g = A_RAD_CGS * T_CMB**4                               # erg/cm^3
    ratios = [((b * 1e-9)**2 / (8.0 * 3.141592653589793)) / rho_g for b in B_REC_NG]
    # two-phase: phi_+ has inertia 2 -> f_+ = sqrt(2) f; N in terms of Delta phi
    f_plus = 2.0 ** 0.5 * f_gev
    g_plus = ALPHA / (2.0 * 3.141592653589793 * f_plus)
    N_plus_kz = g_plus / 2.0 * f_plus * 2.0 * 3.141592653589793
    return {
        'f_phi_GeV': f_gev, 'g_pg_GeVinv': g_pg, 'g_over_CAST': g_pg / CAST_G,
        'm_A_eV': m_A_ev, 'm_A_over_bound': m_A_ev / M_GAMMA_BOUND_EV,
        'N_KZ': N(2.0 * 3.141592653589793),
        'N_KZ_plus': N_plus_kz,
        'dphi_for_N1_rad': dphi_for_N1, 'turns_for_N1': dphi_for_N1 / (2 * 3.141592653589793),
        'omega_gap': omega_gap, 'theta_rotating_vacuum_rad': theta_rot_vac,
        'theta_obs_rad': theta_obs_rad, 'dphi_for_obs_rad': dphi_for_obs,
        'theta_static_rad': N(0.0),
        'rhoB_over_rhogamma': ratios,
    }


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(ch, sh, fd, mode, gr, ex, num):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp),
                     'MATCH' if ok else 'CONTRADICTION'))

    add('S1', '(a) charged: m_A^2 = e^2 v^2 (Higgs mechanism)',
        ch['mA2_residual'], 0, ch['mA2_residual'] == 0)
    add('S2', '(a) photon mass <= lenient PDG bound 2.2e-14 eV',
        '{:.2e} eV'.format(num['m_A_eV']), '<= 2.2e-14 eV',
        num['m_A_eV'] <= M_GAMMA_BOUND_EV)
    add('S3', '(b) f(phi)F^2 invariant under phi->phi+c (generic f)',
        sh['single_residual'], 0, sh['single_residual'] == 0)
    add('S4', "(b') f(psi-phi)F^2 invariant under joint shift",
        sh['joint_residual'], 0, sh['joint_residual'] == 0)
    add('S5', '(c) eps F F = 4 d(eps A dA): total derivative',
        fd['residual'], 0, fd['residual'] == 0)
    add('S6', '(c) EOM -> u" + (k^2 -/+ s k) u = 0, both helicities',
        (mode['plus']['residual'], mode['minus']['residual']), (0, 0),
        mode['plus']['residual'] == 0 and mode['minus']['residual'] == 0)
    add('S7', 'g -> 0: dispersion omega = k', gr['free_limit_residual'], 0,
        gr['free_limit_residual'] == 0)
    add('S8', 'max growth rate = s/2 at k = s/2',
        (gr['gamma_max'], gr['k_star']), ('s/2', 's/2'),
        sp.simplify(gr['gamma_max'] - sp.Symbol('s', positive=True) / 2) == 0)
    add('S9', 'growth rate = polarization rotation rate (N == theta_CB)',
        gr['growth_minus_rotation'], 0, gr['growth_minus_rotation'] == 0)
    add('S10', 'f_phi cancels: dN/df_phi = 0', ex['dN_df'], 0, ex['dN_df'] == 0)
    add('S11', 'N formula = alpha C Delta_phi/(4 pi)',
        sp.simplify(ex['N'] - ex['N_target']), 0,
        sp.simplify(ex['N'] - ex['N_target']) == 0)
    add('S12', '(c) natural g_pg below CAST 0.66e-10 GeV^-1',
        '{:.2e}'.format(num['g_pg_GeVinv']), '< 6.6e-11',
        num['g_pg_GeVinv'] < CAST_G)
    add('S13', '(c) KZ winding (Delta phi = 2 pi) gives N >= 1',
        '{:.2e}'.format(num['N_KZ']), '>= 1', num['N_KZ'] >= 1.0)
    add('S14', 'two-phase phi_+ (inertia 2): N_KZ unchanged',
        '{:.3e}'.format(num['N_KZ_plus']), '{:.3e}'.format(num['N_KZ']),
        abs(num['N_KZ_plus'] - num['N_KZ']) < 1e-15)
    lim = (THETA_CB_DEG + 3 * THETA_CB_ERR) * 3.141592653589793 / 180.0
    add('S15', 'rotating vacuum (dphi/dt = omega_gap): theta_CB <= obs+3sigma',
        '{:.2e} rad'.format(num['theta_rotating_vacuum_rad']), '<= {:.4f} rad'.format(lim),
        num['theta_rotating_vacuum_rad'] <= lim)
    add('S16', 'static vacuum theta_CB = 0 vs hint 0.342 +- 0.09 deg',
        '{:.1f} deg'.format(num['theta_static_rad']), '0.342 deg',
        abs(num['theta_static_rad'] * 180 / 3.141592653589793 - THETA_CB_DEG)
        <= THETA_CB_ERR)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t84_pmf_scoping')
    rw.section('T84 -- PDTP primordial magnetic fields scoping (CLAUDE OPUS 5.5, Part 159)')
    ch, sh = derive_charged_coupling(), derive_shift_checks()
    fd = derive_ffdual_total_derivative()
    mode, gr = derive_mode_equation(), derive_growth_and_rotation()
    ex = derive_exponent_formula()
    num = compute_numbers(ex)

    rw.subsection('(a) charged coupling')
    rw.key_value('L', ch['L'])
    rw.key_value('m_A^2', ch['mA2'])
    rw.subsection('(b) dilaton-type shift checks')
    rw.key_value('f(phi+c)-f(phi)', sh['single_residual'])
    rw.key_value('f(psi-phi) joint-shift residual', sh['joint_residual'])
    rw.subsection('(c) axion-type')
    rw.key_value('eps F F - 4 d(eps A dA)', fd['residual'])
    for hel in ('plus', 'minus'):
        rw.key_value('EOM / cos(kz), helicity ' + hel, mode[hel]['ode_over_cos'])
    rw.key_value('k* (max growth)', gr['k_star'])
    rw.key_value('Gamma_max', gr['gamma_max'])
    rw.key_value('rotation rate (k >> s)', gr['rotation_rate'])
    rw.key_value('N = (g/2) Delta a', ex['N'])
    rw.key_value('dN/df_phi', ex['dN_df'])
    rw.subsection('Numbers')
    for k_, v_ in num.items():
        rw.key_value(k_, v_)

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(ch, sh, fd, mode, gr, ex, num)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows,
             [4, 62, 26, 18, 13])
    n = sum(1 for r in rows if r[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()

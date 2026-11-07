#!/usr/bin/env python3
"""
t87_turing_scales.py -- TODO_05 T87: Turing (reaction-diffusion) checks for
PDTP and a scan of candidate "ticking" frequencies (exploratory, not a Part)
==========================================================================
Worked by CLAUDE OPUS 5.5 (2026-11-07).

GOAL:
    (1) Re-derive Turing's linear instability conditions and the worked
        example (critical diffusion ratio, pattern wavenumber).
    (2) Re-derive the linearised PDTP two-substance matrix (spacetime phi,
        matter psi) and show it has no growing mode (symmetric coupling).
    (3) IF a Turing-type band existed with expansion overdamping
        D_eff = c^2/(3H) and a reaction rate omega_r, its spacing would be
        l_T = sqrt(D_eff/omega_r). Evaluate l_T for candidate frequencies:
        Planck (omega_P = omega_gap), cosmological constant (H_Lambda),
        dark-energy scale (E_Lambda/hbar), matter Compton frequencies, QCD.
    (4) Verify the identity E_Lambda = hbar*sqrt(omega_P*H_Lambda)*(3/(8 pi))^(1/4).

EQUATIONS USED:
    Eq 1: du/dt = f + D_u lap u, dv/dt = g + D_v lap v (Turing 1952, eq 7.1) [ASSUMED]
    Eq 2: growth <=> det(J - k^2 D) < 0 (2x2 stability) [ASSUMED, standard]
    Eq 3: PDTP linearised: phi_tt = c^2 lap phi + g (psi - phi),
          psi_tt = c_p^2 lap psi - g (psi - phi) (CLAUDE.md, small offset) [ASSUMED]
    Eq 4: rho_Lambda c^2 = Lambda c^4 / (8 pi G), G = hbar c / m_P^2 [ASSUMED]
    Eq 5: H_Lambda = c sqrt(Lambda/3); omega_P = m_P c^2 / hbar;
          omega_Compton = m c^2 / hbar [ASSUMED, definitions]
    Eq 6: overdamped expansion: 3 H phi_t ~ c^2 lap phi + ... => D_eff = c^2/(3H)
          [SPECULATIVE regime, T87 note sec 6]

ASSUMPTIONS:
    [A1] l_T = sqrt(D_eff/omega_r) is a dimensional estimate of a Turing
         spacing (Turing 1952 sec 8 "chemical wave-length"); it is NOT a
         derivation that PDTP has such a band (sec 4 of the note shows plain
         PDTP does not).
    [A2] Present-day H0 used for D_eff (late universe).

OUTPUT (data only): Turing threshold, PDTP matrix invariants, frequency
    table, length table, identity residual, Sudoku scorecard.
"""

import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

# Constants (SI; CODATA 2018 / Planck 2018)
HBAR = 1.054571817e-34
C = 2.99792458e8
G_N = 6.67430e-11
M_P = 2.176434e-8                       # Planck mass, kg
EV = 1.602176634e-19
# Planck 2018 TT,TE,EE+lowE+lensing+BAO (the set behind the quoted Lambda;
# first run used Planck-only 67.4/0.685 and S10 failed by 1.3% -- parameter-set
# mismatch, not physics)
H0 = 67.66e3 / 3.0856775814913673e22    # s^-1
OMEGA_L = 0.6889
LAMBDA_LIT = 1.1056e-52                 # m^-2 (Planck 2018 + BAO, as quoted)
M_E = 9.1093837015e-31
M_PR = 1.67262192369e-27
M_QCD_MEV = 367.0                       # PDTP m_cond_QCD (Part 37)
L_EOTWASH = 52e-6                       # m, Lee et al. 2020 shortest separation


# =====================================================================
# DERIVATIONS
# =====================================================================

def derive_turing_example():
    """Turing 2x2 with f_u=1, f_v=-1, g_u=2, g_v=-3/2, D=diag(1, d)."""
    k, d, q = sp.symbols('k d q', positive=True)
    J = sp.Matrix([[1, -1], [2, sp.Rational(-3, 2)]])
    h = sp.expand((J - q * sp.diag(1, d)).det())
    qc = sp.solve(sp.diff(h, q), q)[0]
    roots = sp.solve(sp.simplify(h.subs(q, qc)), d)
    d_c = max(r for r in roots if (2 * r - 3) > 0)   # k_c^2 > 0 requires d > 3/2
    return {'trJ': J.trace(), 'detJ': J.det(), 'h': h, 'qc': sp.simplify(qc),
            'd_c': d_c, 'qc_at6': qc.subs(d, 6),
            'hmin_at6': sp.simplify(h.subs(q, qc).subs(d, 6)),
            'bc': J[0, 1] * J[1, 0]}


def derive_pdtp_matrix():
    """Linearised PDTP two-substance matrix M_k (lambda^2 = eigenvalue)."""
    k, g, c, cp = sp.symbols('k g c c_p', positive=True)
    M = sp.Matrix([[-c**2 * k**2 - g, g], [g, -cp**2 * k**2 - g]])
    det = sp.factor(sp.expand(M.det()))
    ev0 = sorted(sp.simplify(m.subs(k, 0)) for m in M.eigenvals())
    # Turing notation a=M00, b=M01, c=M10, d=M11 at k=0
    a, b, cc, dd = (M[0, 0].subs(k, 0), M[0, 1], M[1, 0], M[1, 1].subs(k, 0))
    return {'symmetric': M == M.T, 'trace': sp.simplify(M.trace()), 'det': det,
            'eig_k0': ev0, 'bc_minus_ad': sp.simplify(b * cc - a * dd),
            'bc': sp.simplify(b * cc)}


def derive_lambda_identity():
    """E_Lambda^4 = (hbar c)^3 rho_Lambda c^2 with rho_L c^2 = Lambda c^4/(8 pi G),
    G = hbar c/m_P^2. Show E_Lambda/hbar = sqrt(omega_P H_Lambda) (3/(8 pi))^(1/4)."""
    hb, c, mP, Lam = sp.symbols('hbar c m_P Lambda', positive=True)
    G = hb * c / mP**2
    E4 = (hb * c)**3 * Lam * c**4 / (8 * sp.pi * G)
    E = E4**sp.Rational(1, 4)
    wP = mP * c**2 / hb
    HL = c * sp.sqrt(Lam / 3)
    target = hb * sp.sqrt(wP * HL) * (sp.Rational(3, 8) / sp.pi)**sp.Rational(1, 4)
    return {'E_Lambda': sp.simplify(E), 'residual': sp.simplify(E / target - 1)}


def derive_turing_length():
    """l_T = sqrt(D_eff/omega), D_eff = c^2/(3H). With omega = omega_P = c/l_P and
    R_H = c/H: l_T = sqrt(l_P R_H / 3)."""
    c, H, lP = sp.symbols('c H l_P', positive=True)
    wP = c / lP
    lT = sp.sqrt((c**2 / (3 * H)) / wP)
    return {'l_T': sp.simplify(lT),
            'residual': sp.simplify(lT - sp.sqrt(lP * (c / H) / 3))}


# =====================================================================
# COMPUTATION
# =====================================================================

def compute_tables():
    Lam = 3 * OMEGA_L * H0**2 / C**2
    wP = M_P * C**2 / HBAR
    HL = C * (Lam / 3) ** 0.5
    rho_c2 = Lam * C**4 / (8 * 3.141592653589793 * G_N)
    E_L = ((HBAR * C) ** 3 * rho_c2) ** 0.25
    freqs = {
        'Planck omega_P (= omega_gap)': wP,
        'dark-energy E_Lambda/hbar': E_L / HBAR,
        'QCD m_cond_QCD c^2/hbar (367 MeV)': M_QCD_MEV * 1e6 * EV / HBAR,
        'proton Compton m_p c^2/hbar': M_PR * C**2 / HBAR,
        'electron Compton m_e c^2/hbar': M_E * C**2 / HBAR,
        'Hubble H0': H0,
        'cosmological constant H_Lambda': HL,
    }
    D_eff = C**2 / (3 * H0)
    lengths = {name: (D_eff / w) ** 0.5 for name, w in freqs.items()}
    return {'Lambda': Lam, 'Lambda_ratio_lit': Lam / LAMBDA_LIT, 'omega_P': wP,
            'H_Lambda': HL, 'E_Lambda_meV': E_L / EV * 1e3,
            'l_Lambda_um': HBAR * C / E_L * 1e6, 'D_eff': D_eff,
            'freqs': freqs, 'lengths': lengths,
            'l_P': HBAR / (M_P * C), 'R_H': C / H0}


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(te, pm, li, tl, tab):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    add('S1', 'Turing example stable at k=0 (trJ<0, detJ>0)',
        (te['trJ'], te['detJ']), '(<0, >0)', te['trJ'] < 0 and te['detJ'] > 0)
    add('S2', 'Turing example critical ratio d_c = 9/2', te['d_c'], '9/2',
        te['d_c'] == sp.Rational(9, 2))
    add('S3', 'At d=6: min det J_k < 0 (pattern grows)', te['hmin_at6'], '< 0',
        te['hmin_at6'] < 0)
    add('S4', 'Turing case (d) needs bc < 0 (Turing eq 9.4): example', te['bc'], '< 0',
        te['bc'] < 0)
    add('S5', 'PDTP matrix symmetric (single Lagrangian)', pm['symmetric'], True,
        pm['symmetric'] is True)
    add('S6', 'PDTP: bc - ad = 0 (on Turing case-(a) boundary)', pm['bc_minus_ad'], 0,
        pm['bc_minus_ad'] == 0)
    add('S7', 'PDTP eigenvalues at k=0 = {-2g, 0} (Goldstone)', pm['eig_k0'],
        '[-2*g, 0]', len(pm['eig_k0']) == 2 and pm['eig_k0'][1] == 0)
    add('S8', 'E_Lambda = hbar sqrt(omega_P H_Lambda)(3/8pi)^(1/4) residual',
        li['residual'], 0, li['residual'] == 0)
    add('S9', 'l_T(omega_P) = sqrt(l_P R_H / 3) residual', tl['residual'], 0,
        tl['residual'] == 0)
    add('S10', 'Lambda from (H0, Omega_L) vs Planck 1.1056e-52 m^-2 (1%)',
        '{:.4f}'.format(tab['Lambda_ratio_lit']), 1.0,
        abs(tab['Lambda_ratio_lit'] - 1) < 0.01)
    add('S11', 'E_Lambda in the quoted ~2.2-2.3 meV range',
        '{:.3f} meV'.format(tab['E_Lambda_meV']), '2.2-2.3 meV',
        2.2 <= tab['E_Lambda_meV'] <= 2.3)
    lT = tab['lengths']['Planck omega_P (= omega_gap)']
    ratio = lT / (tab['l_Lambda_um'] * 1e-6)
    add('S12', 'l_T(Planck) / l_Lambda within one order of magnitude',
        '{:.3f}'.format(ratio), '0.1-10', 0.1 <= ratio <= 10)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t87_turing_scales')
    rw.section('T87 -- Turing checks + candidate ticking frequencies (CLAUDE OPUS 5.5)')
    te, pm = derive_turing_example(), derive_pdtp_matrix()
    li, tl = derive_lambda_identity(), derive_turing_length()
    tab = compute_tables()

    rw.subsection('Turing example')
    for k_ in ('trJ', 'detJ', 'h', 'qc', 'd_c', 'qc_at6', 'hmin_at6', 'bc'):
        rw.key_value(k_, te[k_])
    rw.subsection('PDTP two-substance matrix')
    for k_ in ('symmetric', 'trace', 'det', 'eig_k0', 'bc', 'bc_minus_ad'):
        rw.key_value(k_, pm[k_])
    rw.subsection('Identities')
    rw.key_value('E_Lambda', li['E_Lambda'])
    rw.key_value('l_T(omega_P)', tl['l_T'])
    rw.subsection('Scales')
    for k_ in ('Lambda', 'Lambda_ratio_lit', 'omega_P', 'H_Lambda', 'E_Lambda_meV',
               'l_Lambda_um', 'D_eff', 'l_P', 'R_H'):
        rw.key_value(k_, tab[k_])
    rows_t = [(n, '{:.3e}'.format(w), '{:.3e}'.format(tab['lengths'][n]))
              for n, w in tab['freqs'].items()]
    rw.table(['frequency', 'omega [s^-1]', 'l_T = sqrt(D_eff/omega) [m]'], rows_t,
             [36, 14, 28])
    rw.key_value('Eot-Wash shortest tested separation [m]', L_EOTWASH)

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(te, pm, li, tl, tab)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows, [4, 58, 22, 12, 13])
    n = sum(1 for r in rows if r[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()

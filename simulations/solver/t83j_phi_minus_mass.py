#!/usr/bin/env python3
"""
t83j_phi_minus_mass.py -- T83 sub-task 83j: reversed-Higgs mass of phi_-
=========================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-09-28). Part 157.

GOAL:
    Part 62 gives the phi_- mass near matter as m^2 = V''(pi/2) = 2 g Phi,
    Phi = sin(psi - phi_+). The phi_- kinetic term is phi_-_dot^2 (inertia
    2), so the physical mass is V''/2. Verify, test the consequences:
      - E_gap (Part 80), neutron-star and Earth values (Parts 89/94),
      - Part 119: is m/H = 3 sqrt(eps) affected? (slow-roll, inertia I)
      - Part 117: phi_+ gradient stiffness and lambda_4,
    and keep the correct neighbours untouched (single-phase breathing gap
    omega^2 = 2g; phi_- potential amplitude 2 g Phi).

EQUATIONS USED:
    Eq 1: L = 1/2 psi_t^2 + phi_+t^2 + phi_-t^2 - (gradients)
              + 2 g sin(psi - phi_+) sin(phi_-)            (Part 61) [ASSUMED]
    Eq 2: small oscillations: m^2 = V''/I for L = 1/2 I q_t^2 - V(q)
          Source: Goldstein, Classical Mechanics, Sec 6.2
    Eq 3: slow roll: 3 H q_t = -V'(q)/I (overdamped, q_tt neglected);
          eps := K/V with K = 1/2 I q_t^2.
          Source: https://en.wikipedia.org/wiki/Inflaton (slow-roll)
    Eq 4: Gaussian integration of a quadratic mode: V_min = V_0 - J^2/(2M)
          Source: Peskin & Schroeder, Ch. 11 (tree-level matching)

ASSUMPTIONS:
    [A1] Phi = sin(psi - phi_+) treated as a fixed background (Part 62).
    [A2] Harmonic (quadratic) limit for slow roll.
    [A3] Part 117 setup: eta = phi_+ fluctuation of wavenumber kbar; the
         phi_+ gradient term (d phi_+)^2 (coefficient 1) gives kbar^2 eta^2.

OUTPUT (data only): mass ratios, slow-roll invariance, lambda_4 ratios,
    numeric rescalings, Sudoku scorecard.
"""

import os
import sys
import math
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

g, Phi, H, I, kb2 = sp.symbols('g Phi H I kbar2', positive=True)
pm, th, pp, psi, eta, beta, x = sp.symbols('phi_m Theta phi_p psi eta beta x', real=True)


# =====================================================================
# DERIVATIONS
# =====================================================================

def derive_mass():
    """m^2 at phi_- = pi/2 for inertia 2 (correct) and 1 (Part 62)."""
    V = -2 * g * Phi * sp.sin(pm)
    Vpp = sp.diff(V, pm, 2).subs(pm, sp.pi / 2)
    m2_correct = sp.simplify(Vpp / 2)
    m2_part62 = sp.simplify(Vpp / 1)
    # canonical field phi_c = sqrt(2) phi_- -> kinetic 1/2 phi_c_t^2
    pc = sp.Symbol('phi_c', real=True)
    Vc = V.subs(pm, pc / sp.sqrt(2))
    m2_canon = sp.simplify(sp.diff(Vc, pc, 2).subs(pc, sp.sqrt(2) * sp.pi / 2))
    return {'Vpp': Vpp, 'm2_correct': m2_correct, 'm2_part62': m2_part62,
            'm2_canonical': m2_canon}


def derive_vacuum_eigen():
    """Full linear dynamics at Theta = phi_- = pi/2 with inertias (1,2,2):
    phi_- eigenvalue (Phi = sin Theta = 1). Independent of derive_mass."""
    L_int = 2 * g * sp.sin(psi - pp) * sp.sin(pm)
    a_m = sp.diff(L_int, pm) / 2
    a_m = a_m.subs(psi, th + pp)
    coeff = sp.diff(a_m, pm).subs({th: sp.pi / 2, pm: sp.pi / 2})
    return {'phi_m_eig': sp.simplify(coeff)}


def derive_slow_roll():
    """eps = K/V for V = 1/2 I m^2 q^2, K = 1/2 I q_t^2, 3 H q_t = -V'/I.
    Returns eps in terms of m, H -- inertia should cancel."""
    q, m = sp.symbols('q m', positive=True)
    V = sp.Rational(1, 2) * I * m**2 * q**2
    qdot = -sp.diff(V, q) / I / (3 * H)
    K = sp.Rational(1, 2) * I * qdot**2
    eps = sp.simplify(K / V)
    # eps declared positive so solve returns the physical (positive) root
    # (RECHECK fix: first run returned -3 sqrt(eps) from an undeclared symbol)
    m_over_H = sp.simplify(sp.solve(sp.Eq(sp.Symbol('eps', positive=True), eps), m)[0] / H)
    return {'eps': eps, 'm_over_H': m_over_H}


def derive_part117(stiffness_coeff):
    """V_ind = -J^2/(2M), M = stiffness_coeff * kbar2 (gradient-dominated).
    Part 117 used (1/2) kbar2 eta^2 -> M = kbar2 (coeff 1); correct
    (d phi_+)^2 gives kbar2 eta^2 -> M = 2 kbar2 (coeff 2)."""
    V_exact = -2 * g * sp.sin(sp.pi / 2 - beta + eta) * sp.sin(pm)
    V_ser = sp.expand(sp.series(V_exact, eta, 0, 3).removeO())
    J = -V_ser.coeff(eta, 1)
    V_ind = -J**2 / (2 * stiffness_coeff * kb2)
    c4 = sp.expand(sp.series(V_ind, pm, 0, 6).removeO()).coeff(pm, 4)
    return {'V_ind': sp.simplify(V_ind), 'lambda4': sp.simplify(c4)}


# =====================================================================
# COMPUTATION
# =====================================================================

def compute_rescalings(m2_ratio):
    """Every quantity proportional to m (or E_gap, omega) scales by
    sqrt(m2_ratio); applied to the published headline values (inputs)."""
    s = math.sqrt(float(m2_ratio))
    published = {'NS phi_- mass [TeV] (Part 89)': 566.0,
                 'Earth omega_phi [GeV] (Eq 94.10)': 31.7}
    return {k: (v, v * s) for k, v in published.items()}, s


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(ms, vac, sr, p117_old, p117_new, resc, s):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    add('S1', 'm^2 = V\'\'/I_- (I_- = 2) vs Part 62 2 g Phi', ms['m2_correct'],
        2 * g * Phi, sp.simplify(ms['m2_correct'] - 2 * g * Phi) == 0)
    add('S2', 'Canonical field phi_c = sqrt2 phi_- gives same m^2', ms['m2_canonical'],
        ms['m2_correct'], sp.simplify(ms['m2_canonical'] - ms['m2_correct']) == 0)
    eig = vac['phi_m_eig']
    add('S3', 'Vacuum eigenvalue (Part 154 route) = -m^2 at Phi=1', eig,
        -ms['m2_correct'].subs(Phi, 1), sp.simplify(eig + ms['m2_correct'].subs(Phi, 1)) == 0)
    add('S4', 'Part 62 value reproduced with inertia 1', ms['m2_part62'], 2 * g * Phi,
        sp.simplify(ms['m2_part62'] - 2 * g * Phi) == 0)
    ratio = sp.simplify(ms['m2_correct'] / ms['m2_part62'])
    add('S5', 'm^2 ratio new/old', ratio, sp.Rational(1, 2), ratio == sp.Rational(1, 2))
    add('S6', 'slow roll eps = m^2/(9H^2), inertia-free', sr['eps'],
        'm**2/(9*H**2)', sp.simplify(sr['eps'] - sp.Symbol('m', positive=True)**2 / (9 * H**2)) == 0
        and not sr['eps'].has(I))
    add('S7', 'm/H = 3 sqrt(eps) (Part 119 Eq 119.1) invariant', sr['m_over_H'],
        '3*sqrt(eps)', sp.simplify(sr['m_over_H'] - 3 * sp.sqrt(sp.Symbol('eps', positive=True))) == 0)
    g_dyn_ratio = sp.simplify(1 / ratio)       # m fixed by data: g = m^2 / (m^2/g)
    add('S8', 'Inferred g_dyn new/old at fixed m', g_dyn_ratio, 2, g_dyn_ratio == 2)
    l_ratio = sp.simplify(p117_new['lambda4'] / p117_old['lambda4'])
    add('S9', 'Part 117 lambda_4 new/old (same kbar2)', l_ratio, sp.Rational(1, 2),
        l_ratio == sp.Rational(1, 2))
    l_old_gap = sp.simplify(p117_old['lambda4'].subs(kb2, 2 * g) / g)
    l_new_gap = sp.simplify(p117_new['lambda4'].subs(kb2, ms['m2_correct'].subs(Phi, 1)) / g)
    add('S10', 'lambda_4/g at natural gap (old kbar2=2g vs new kbar2=g)',
        l_new_gap, l_old_gap, sp.simplify(l_new_gap - l_old_gap) == 0)
    add('S11', 'Mass/energy rescaling factor sqrt(1/2)', '{:.6f}'.format(s),
        '{:.6f}'.format(1 / math.sqrt(2)), abs(s - 1 / math.sqrt(2)) < 1e-12)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83j_phi_minus_mass')
    rw.section('T83j -- phi_- (reversed Higgs) mass (CLAUDE OPUS 5.5, Part 157)')
    ms = derive_mass()
    vac = derive_vacuum_eigen()
    sr = derive_slow_roll()
    p117_old, p117_new = derive_part117(1), derive_part117(2)
    ratio = sp.simplify(ms['m2_correct'] / ms['m2_part62'])
    resc, s = compute_rescalings(ratio)

    rw.subsection('phi_- mass at phi_- = pi/2')
    for k in ('Vpp', 'm2_correct', 'm2_part62', 'm2_canonical'):
        rw.key_value(k, ms[k])
    rw.key_value('vacuum phi_- eigenvalue (inertias 1,2,2)', vac['phi_m_eig'])
    rw.subsection('Slow roll (inertia I symbolic)')
    rw.key_value('eps = K/V', sr['eps'])
    rw.key_value('m/H', sr['m_over_H'])
    rw.subsection('Part 117 induced potential')
    rw.key_value('old (M = kbar2): lambda_4', p117_old['lambda4'])
    rw.key_value('new (M = 2 kbar2): lambda_4', p117_new['lambda4'])
    rw.subsection('Rescaled headline values (factor {:.6f})'.format(s))
    rw.table(['quantity', 'published', 'corrected'],
             [[k, '{:.4g}'.format(a), '{:.4g}'.format(b)] for k, (a, b) in resc.items()],
             [34, 12, 12])

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(ms, vac, sr, p117_old, p117_new, resc, s)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows, [4, 56, 34, 22, 13])
    n = sum(1 for r in rows if r[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
t88_concordance_scan.py -- TODO_05 T88: concordance (brute-force parameter)
scan of PDTP's single frequency knob, with plot and null test
===========================================================================
Worked by CLAUDE OPUS 5.5 (2026-11-07).

GOAL:
    Sweep PDTP's one free scale -- the condensate frequency
    omega = m_cond c^2 / hbar -- over 70 decades. For each existing PDTP
    prediction, compute log10(predicted / measured). A prediction "works"
    where its curve crosses zero; CONCORDANCE = independent curves crossing
    at the same omega. Observable list FROZEN before the first run
    (look-elsewhere protection):

      O1  G = hbar c / m_cond^2                       (Part 33)   CODATA G
      O2  E_Lambda from rho_Lambda with G(omega)       (T87 6b)    2.25 meV
          -- BUILT-IN duplicate of O1 (control: what a fake match looks like)
      O3  Lambda = 3 Omega_L (H0/omega)^2 (omega/c)^2 (Part 123) Planck Lambda
          -- omega cancels (Part 115 no-go): expected flat
      O4  sigma_QCD = C2_fund (hbar omega)^2           (Part 37)   0.18 GeV^2
      O5  dH0/H0 = (a0 / r_s)^2, a0 = c/omega         (Part 88/155) 0.084
      O6  Turing spacing l_T = sqrt(c^2/(3 H0 omega))  (T87)  one-sided:
          l_T <= 38.6 um (Lee et al. 2020, 95% CL Yukawa range) -- conditional

EQUATIONS USED: as listed above, with
    m_cond = hbar omega / c^2;  a0 = hbar/(m_cond c) = c/omega;
    rho_Lambda c^2 = Lambda c^4/(8 pi G);  E^4 = (hbar c)^3 rho c^2.
    Sources: CODATA 2018; Planck 2018 (+BAO set, H0 = 67.66, Omega_L = 0.6889);
    PDG sigma = 0.18 GeV^2 (as used in Part 37); Riess+2022 / Planck for
    the 8.4% tension; Lee et al. 2020 PRL 124, 101101.

ASSUMPTIONS:
    [A1] Each prediction is taken exactly as its Part states it; no new physics.
    [A2] "Match" = crossing of log ratio = 0; "concordance" = crossings of
         INDEPENDENT observables within 1 decade of each other.
    [A3] Null test: targets replaced by log-uniform random values within
         +/-10 decades of the real ones; same power-law slopes.

OUTPUT (data only): crossing frequencies, slopes, spreads, null-test
    probability, PNG plot, Sudoku scorecard.
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

HBAR, C, G_N = 1.054571817e-34, 2.99792458e8, 6.67430e-11
EV = 1.602176634e-19
GEV = 1e9 * EV
H0 = 67.66e3 / 3.0856775814913673e22
OMEGA_L = 0.6889
LAMBDA_OBS = 1.1056e-52                  # m^-2
SIGMA_QCD = 0.18                         # GeV^2
C2_FUND = 4.0 / 3.0
R_S = 4.539e24                           # m (147.09 Mpc, Part 88)
TENSION = 0.084                          # dH0/H0 needed (Part 88)
L_YUK = 38.6e-6                          # m, Lee et al. 2020 95% CL
M_P = 2.176434e-8
OMEGA_P = M_P * C**2 / HBAR

LOGW = np.linspace(-20.0, 50.0, 70001)   # log10(omega / s^-1)


# =====================================================================
# COMPUTE: predictions vs omega
# =====================================================================

def compute_predictions(logw):
    w = 10.0 ** logw
    m = HBAR * w / C**2
    G_pred = HBAR * C / m**2
    rho_pred = LAMBDA_OBS * C**4 / (8 * np.pi * G_pred)
    E_pred = ((HBAR * C) ** 3 * rho_pred) ** 0.25
    rho_meas = LAMBDA_OBS * C**4 / (8 * np.pi * G_N)
    E_meas = ((HBAR * C) ** 3 * rho_meas) ** 0.25
    Lam_pred = 3 * OMEGA_L * (H0 / w) ** 2 * (w / C) ** 2
    sigma_pred = C2_FUND * (HBAR * w / GEV) ** 2
    dH_pred = ((C / w) / R_S) ** 2
    lT = np.sqrt(C**2 / (3 * H0 * w))
    return {
        'O1 G (Part 33)': np.log10(G_pred / G_N),
        'O2 E_Lambda via G (built-in)': np.log10(E_pred / E_meas),
        'O3 Lambda (Part 123)': np.log10(Lam_pred / LAMBDA_OBS),
        'O4 QCD sigma (Part 37)': np.log10(sigma_pred / SIGMA_QCD),
        'O5 Hubble shift (Part 88)': np.log10(dH_pred / TENSION),
    }, np.log10(lT / L_YUK)


def compute_crossing(logw, y):
    """Zero crossing by linear interpolation; None if no sign change."""
    s = np.sign(y)
    idx = np.where(np.diff(s) != 0)[0]
    if len(idx) == 0:
        return None
    i = idx[0]
    return logw[i] - y[i] * (logw[i + 1] - logw[i]) / (y[i + 1] - y[i])


def compute_slope(logw, y):
    return float(np.polyfit(logw, y, 1)[0])


def compute_null_test(n_obs=3, width=1.0, span=None, n=400000, seed=88):
    """Chance concordance: place n_obs crossings uniformly at random over the
    scanned range (span decades); return the fraction whose spread is
    <= width decades (Monte Carlo) and the exact value for comparison,
    P = n (w/L)^(n-1) - (n-1) (w/L)^n  (order-statistics range of n uniforms).
    (First version shifted targets around the CURRENT crossings and returned
    0 -- not a calibration; replaced, 2026-11-07.)"""
    if span is None:
        span = LOGW[-1] - LOGW[0]
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, span, (n, n_obs))
    p_mc = float(np.mean(x.max(axis=1) - x.min(axis=1) <= width))
    r = width / span
    p_exact = n_obs * r ** (n_obs - 1) - (n_obs - 1) * r ** n_obs
    return p_mc, p_exact


def compute_plot(logw, preds, lt_ratio, crossings, path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(11, 6.5))
    styles = {'O1': ('-', 2.2), 'O2': (':', 2.2), 'O3': ('--', 1.8),
              'O4': ('-', 1.8), 'O5': ('-', 1.8)}
    for name, y in preds.items():
        ls, lw = styles[name[:2]]
        ax.plot(logw, y, ls, lw=lw, label=name)
    ax.axhline(0.0, color='k', lw=0.8)
    excl = lt_ratio > 0
    ax.fill_between(logw, -200, 200, where=excl, color='grey', alpha=0.12,
                    label='O6 excluded if a Turing band existed (l_T > 38.6 um)')
    for name, xc in crossings.items():
        if xc is not None:
            ax.axvline(xc, color='grey', lw=0.5, ls='--')
    ax.axvline(np.log10(OMEGA_P), color='k', lw=0.6, ls='-.')
    ax.text(np.log10(OMEGA_P) + 0.4, 60, 'Planck\nomega_gap', fontsize=8)
    ax.set_xlim(logw[0], logw[-1])
    ax.set_ylim(-150, 150)
    ax.set_xlabel('log10( knob frequency omega = m_cond c^2 / hbar  [s^-1] )')
    ax.set_ylabel('log10( PDTP prediction / measured value )')
    ax.set_title('T88 concordance scan: PDTP single knob (zero line = match)')
    ax.legend(fontsize=8, loc='lower left')
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(cr, sl, flat, delta_at_P, lt_at_P, p_null, p_exact):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    xP = np.log10(OMEGA_P)
    add('S1', 'O1 G crosses zero at omega_P (Planck), within 1%',
        '{:.4f}'.format(10 ** (cr['O1'] - xP)), 1.0, abs(10 ** (cr['O1'] - xP) - 1) < 0.01)
    add('S2', 'O2 crossing == O1 crossing (built-in duplicate flagged)',
        '{:.2e} dec'.format(abs(cr['O2'] - cr['O1'])), '< 1e-6 dec',
        abs(cr['O2'] - cr['O1']) < 1e-6)
    add('S3', 'O3 flat: slope d log ratio / d log omega = 0 (Part 115)',
        '{:.1e}'.format(sl['O3']), 0, abs(sl['O3']) < 1e-9)
    add('S4', 'O3 level: Lambda formula / Lambda_obs = 1 (1%)',
        '{:.4f}'.format(10 ** flat), 1.0, abs(10 ** flat - 1) < 0.01)
    m4 = HBAR * 10 ** cr['O4'] / GEV * 1e3      # MeV
    add('S5', 'O4 crossing gives m_cond_QCD = 367 MeV (Part 37), 1%',
        '{:.1f} MeV'.format(m4), '367 MeV', abs(m4 / 367.0 - 1) < 0.01)
    add('S6', 'O5 at omega_P reproduces Part 88 (l_P/r_s)^2 = 1.27e-119 (1%)',
        '{:.3e}'.format(delta_at_P), '1.27e-119', abs(delta_at_P / 1.27e-119 - 1) < 0.01)
    add('S7', 'slopes O1/O4/O5 = -2/+2/-2 (power laws)',
        '{:.3f}/{:.3f}/{:.3f}'.format(sl['O1'], sl['O4'], sl['O5']), '-2/2/-2',
        all(abs(a - b) < 1e-6 for a, b in ((sl['O1'], -2), (sl['O4'], 2), (sl['O5'], -2))))
    add('S8', 'CONCORDANCE O4 vs O1 within 1 decade',
        '{:.1f} dec'.format(abs(cr['O4'] - cr['O1'])), '<= 1', abs(cr['O4'] - cr['O1']) <= 1)
    add('S9', 'CONCORDANCE O5 vs O1 within 1 decade',
        '{:.1f} dec'.format(abs(cr['O5'] - cr['O1'])), '<= 1', abs(cr['O5'] - cr['O1']) <= 1)
    add('S10', 'O6 at omega_P allowed: l_T <= 38.6 um',
        '{:.1f} um'.format(lt_at_P * 1e6), '<= 38.6 um', lt_at_P <= L_YUK)
    add('S11', 'Null test MC = exact range formula (within 10%)',
        '{:.2e} vs {:.2e}'.format(p_null, p_exact), 'equal',
        abs(p_null / p_exact - 1) < 0.10)
    add('S12', 'Chance 3-way concordance in 70 decades < 1% (a real one would be significant)',
        '{:.2e}'.format(p_exact), '< 0.01', p_exact < 0.01)
    return rows


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    rw = ReportWriter(os.path.join(here, 'outputs'), label='t88_concordance_scan')
    rw.section('T88 -- PDTP concordance scan, single knob (CLAUDE OPUS 5.5)')
    preds, lt_ratio = compute_predictions(LOGW)
    cr, sl = {}, {}
    for name, y in preds.items():
        cr[name[:2]] = compute_crossing(LOGW, y)
        sl[name[:2]] = compute_slope(LOGW, y)
    flat = float(np.mean(preds['O3 Lambda (Part 123)']))
    xP = np.log10(OMEGA_P)
    delta_at_P = ((C / OMEGA_P) / R_S) ** 2
    lt_at_P = np.sqrt(C**2 / (3 * H0 * OMEGA_P))
    lt_cross = compute_crossing(LOGW, lt_ratio)
    p_null, p_exact = compute_null_test()

    rw.subsection('Crossings (log10 omega where prediction = measured)')
    for k in ('O1', 'O2', 'O3', 'O4', 'O5'):
        rw.key_value(k + ' crossing', cr[k])
        rw.key_value(k + ' slope', sl[k])
    rw.key_value('O3 constant log ratio', flat)
    rw.key_value('log10 omega_P', xP)
    rw.key_value('O6 boundary (l_T = 38.6 um) at log10 omega', lt_cross)
    rw.key_value('l_T at omega_P [m]', lt_at_P)
    rw.key_value('O5 at omega_P', delta_at_P)
    rw.key_value('spread of independent crossings O1,O4,O5 [decades]',
                 max(cr['O1'], cr['O4'], cr['O5']) - min(cr['O1'], cr['O4'], cr['O5']))
    rw.key_value('null-test chance 3-way concordance (MC)', p_null)
    rw.key_value('null-test chance 3-way concordance (exact)', p_exact)

    img = os.path.join(here, '..', '..', 'assets', 'images', 't88_concordance_scan.png')
    compute_plot(LOGW, preds, lt_ratio, {k: cr[k] for k in ('O1', 'O4', 'O5')},
                 os.path.normpath(img))
    rw.key_value('plot', os.path.normpath(img))

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(cr, sl, flat, delta_at_P, lt_at_P, p_null, p_exact)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows, [4, 58, 20, 12, 13])
    n = sum(1 for r in rows if r[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()

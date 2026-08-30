#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t25_string_theory_comparison.py -- TODO_04 T25, Part 134
=======================================================================
String theory vs PDTP comparison (TODO_04 T25). Per T25's own effort
estimate ("Medium, mostly literature review + comparison tables"), this
is NOT a heavy Sudoku-verification investigation like T17-T20 -- it is
a literature comparison with ONE genuinely quantitative piece (Key
Question 2: does the Regge-slope relation constrain PDTP's m_cond?).
This script computes that one piece; the rest of T25 is comparison-table
material written directly into the research doc.

Established facts used here (cited to their sources in the doc, not
re-derived): string tension T = 1/(2*pi*alpha') (Wikipedia, Bosonic
string theory); PDTP's own sigma_SU(3) = 0.173 GeV^2 (Part 38) and
m_cond_QCD = 367 MeV (Part 37, su3_condensate_extension.md Sec 11.1,
m_cond_QCD = sqrt(sigma/(4/3)) using the real QCD lattice sigma=0.18 GeV^2
and Part 37's own Casimir factor); m_cond (gravity layer) = m_Planck
(Part 33/35).

PDTP Original: none -- this is a structural comparison of two
already-established PDTP numbers (m_cond_QCD, m_cond=m_Planck), checking
whether a string-theory relation (Regge slope) bridges them. It does not.

Output: DATA only. Interpretation in docs/research/string_theory_comparison.md.
"""

import math

# ===========================================================================
# CONSTANTS
# ===========================================================================
HBAR_C_GEV_FM = 0.1973269804   # GeV*fm
M_PLANCK_GEV = 1.220890e19     # GeV (Part 33's m_cond for the gravity layer)


def regge_slope_from_sigma(sigma_gev2):
    """alpha' = 1/(2*pi*sigma). Source: Wikipedia, Bosonic string theory,
    T = 1/(2*pi*alpha') solved for alpha'."""
    return 1.0 / (2 * math.pi * sigma_gev2)


def string_length_fm(alpha_prime_gev_minus2):
    """String length scale ell_s = sqrt(alpha'), converted to fm via hbar*c."""
    ell_s_gev_inv = math.sqrt(alpha_prime_gev_minus2)
    return ell_s_gev_inv * HBAR_C_GEV_FM


def main():
    print("=" * 78)
    print("T25 (Part 134): Regge Slope vs PDTP's m_cond -- Quantitative Check")
    print("=" * 78)

    sigma_SU3 = 0.173   # GeV^2, Part 38's own predicted SU(3) string tension
    alpha_prime = regge_slope_from_sigma(sigma_SU3)
    ell_s = string_length_fm(alpha_prime)

    print(f"\nPDTP sigma_SU(3) [Part 38]      = {sigma_SU3} GeV^2")
    print(f"alpha' = 1/(2*pi*sigma)          = {alpha_prime:.4f} GeV^-2")
    print(f"String length ell_s = sqrt(alpha') = {math.sqrt(alpha_prime):.4f} GeV^-1")
    print(f"ell_s in fm (via hbar*c)          = {ell_s:.4f} fm")

    lambda_evan_B1_fm = HBAR_C_GEV_FM / 0.200   # Part 89's own evanescent depth, cited for scale comparison
    print(f"\nCompare: Part 89's own lambda_evan(B1) = hbar*c/Lambda_QCD = {lambda_evan_B1_fm:.4f} fm")
    print(f"Ratio ell_s / lambda_evan(B1)     = {ell_s / lambda_evan_B1_fm:.4f}  (same order of magnitude, QCD confinement scale)")

    m_cond_QCD_GeV = 0.367   # Part 37's own value, su3_condensate_extension.md Sec 11.1
    m_cond_gravity_GeV = M_PLANCK_GEV

    ratio = m_cond_gravity_GeV / m_cond_QCD_GeV
    print(f"\nm_cond (gravity layer, Part 33/35) = {m_cond_gravity_GeV:.4e} GeV (= m_Planck)")
    print(f"m_cond_QCD (Part 37, from sigma)    = {m_cond_QCD_GeV} GeV")
    print(f"Ratio m_cond / m_cond_QCD            = {ratio:.4e}")
    print(f"\nStructural conclusion: sigma_SU(3) and alpha' both belong to the QCD")
    print(f"condensate layer (tied to m_cond_QCD via Part 37's own Casimir-factor")
    print(f"formula, sqrt(sigma/(4/3))), NOT to the gravity layer's m_cond=m_Planck.")
    print(f"Nothing in the current framework connects these two layers' condensate")
    print(f"masses -- the {ratio:.1e}-fold gap between them is exactly the un-derived")
    print(f"free-parameter gap the project already tracks (A1/T48/T49), not something")
    print(f"the Regge-slope relation can close, because it never involves m_cond_QCD")
    print(f"and m_cond=m_Planck in the same formula to begin with.")


if __name__ == '__main__':
    main()

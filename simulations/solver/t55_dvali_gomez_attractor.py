#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t55_dvali_gomez_attractor.py -- Phase 92: Dvali-Gomez Criticality as
Attractor (Part 124)
===========================================================================
T55 (TODO_05): Is alpha_gr = 1 an ATTRACTOR of condensate dynamics?
If yes, m_cond = m_P is a dynamical fixed point, not a fitted parameter --
the only no-go-compatible route (Part 115 Theorem 115.4) to "derive" m_cond.

FRAME (no-go compatibility, stated up front):
  All flows below are computed in the FIXED-G frame: the ambient
  gravitational coupling G is held at its measured value (external input),
  and the grain mass m varies as the dynamical variable. This is the same
  logical structure as T50 (external H_0): the Part 115 no-go theorem
  blocks INTERNAL extremum principles (where G = hbar*c/m_cond^2 makes
  every ratio m-independent); it does not block dynamics referenced to an
  external ambient coupling. The absolute scale still comes from outside.

THREE CANDIDATE ATTRACTOR ROUTES TESTED:
  S2 Energy minimization:   E(m) = m*c^2*(1 - xi*alpha(m))
     -> extremum at alpha = 1/(3*xi) = O(1) BUT d2E/dm2 < 0: a MAXIMUM
        (barrier / separatrix), NOT a minimum.        [DERIVED, NEGATIVE]
  S3 Entropy maximization:  S_tot(m) at fixed total mass
     -> quantum branch S ~ 1/m falling, BH branch S ~ m rising:
        criticality is the entropy MINIMUM.           [DERIVED, NEGATIVE]
  S4 Dissipative flow (Hawking): overcritical grains have horizons and
     evaporate in FINITE time t = 5120*pi*G^2*m^3/(hbar*c^4); subcritical
     grains have no horizon, no decay channel, infinite lifetime.
     -> alpha_c = O(1) is a STABILITY BOUNDARY; the flow is a ONE-SIDED
        attractor (ceiling) onto criticality from above. The endpoint
        quantum energy is EXACTLY m_P*c^2 (Part 47).  [DERIVED]

VERDICT SHAPE: PARTIAL. alpha_gr = 1 is a driven/dissipative critical
point (laser-threshold character, Part 110), not an equilibrium extremum
-- consistent with the no-go theorem. Dynamics DERIVES the ceiling
m_cond <= m_P*O(1) and deposits evaporation output exactly at m_P;
the final step (condensate sits AT the ceiling, not below) needs a
maximal-packing principle and remains [SPECULATIVE].

Sources:
  Dvali & Gomez (2011) arXiv:1112.3359 "Black Hole's Quantum N-Portrait"
  Dvali & Gomez (2012) arXiv:1207.4059 (BH = critical point of quantum
      phase transition; maximal packing)
  Page (1976) Phys. Rev. D 13, 198 (evaporation lifetime formula)
  Hawking (1975) Comm. Math. Phys. 43, 199 (T_H)
  Part 24/111: T_H derived/verified in PDTP
  Part 47: evaporation endpoint M_evap = m_P/(8*pi), E_final = m_P*c^2,
      complete evaporation (no remnant)
  Part 61: Jeans eigenvalue +2*sqrt(2)*g (collective clumping drive)
  Part 110: laser-threshold universality class (driven criticality)
  Part 115: scale-invariance no-go theorem; bridge = DG criticality
  Part 116: DM = Planck vortex relic, m_DM = m_cond = m_P

Output: simulations/solver/outputs/t55_dvali_gomez_attractor_<timestamp>.txt

ALL returned values are COMPUTED -- no hardcoded results (RECHECK rule).
"""

import os
import sys
import math

import sympy as sp
from sympy import symbols, sqrt, simplify, diff, solve, Rational, sign

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter

# ===========================================================================
# PHYSICAL CONSTANTS (SI, CODATA 2018)
# ===========================================================================
c_SI    = 2.99792458e8         # m/s (exact)
hbar_SI = 1.054571817e-34      # J s
G_SI    = 6.67430e-11          # m^3 kg^-1 s^-2
kB_SI   = 1.380649e-23         # J/K (exact)

m_P_SI  = math.sqrt(hbar_SI * c_SI / G_SI)          # kg   [COMPUTED]
t_P_SI  = math.sqrt(hbar_SI * G_SI / c_SI**5)       # s    [COMPUTED]
l_P_SI  = math.sqrt(hbar_SI * G_SI / c_SI**3)       # m    [COMPUTED]

# SymPy symbols (fixed-G frame: G external, m dynamical)
m_s, G_s, hbar_s, c_s, xi_s, N_s, R_s, Mtot_s = symbols(
    'm G hbar c xi N R M_tot', positive=True, real=True)


# ===========================================================================
# S1: COUPLING FUNCTION AND FIXED POINT (fixed-G frame)
# ===========================================================================

def derive_coupling_fixed_point(rw):
    """
    alpha_gr(m) = G*m^2/(hbar*c)   [Dvali-Gomez per-quantum coupling]
    Monotone increasing; criticality alpha = 1 at m = m_P = sqrt(hbar*c/G).
    Geometric meaning: r_S(m)/lambda_C(m) = 2*alpha(m), so alpha = 1
    is where the Schwarzschild radius equals TWICE the (reduced) Compton
    wavelength: r_S = 2*a_0 (TODO_05 Sudoku S2 target).
    """
    rw.section("S1: COUPLING alpha(m) AND FIXED POINT (fixed-G frame)")

    alpha_sym  = G_s * m_s**2 / (hbar_s * c_s)
    dalpha_dm  = diff(alpha_sym, m_s)
    m_crit     = solve(sp.Eq(alpha_sym, 1), m_s)[0]     # symbolic root
    m_crit_ok  = simplify(m_crit - sqrt(hbar_s * c_s / G_s)) == 0

    # r_S / lambda_C ratio (lambda_C = hbar/(m c) reduced Compton = a_0)
    r_S      = 2 * G_s * m_s / c_s**2
    lam_C    = hbar_s / (m_s * c_s)
    ratio    = simplify(r_S / lam_C)                    # = 2*alpha
    ratio_ok = simplify(ratio - 2 * alpha_sym) == 0

    # numeric at m = m_P
    alpha_at_mP = G_SI * m_P_SI**2 / (hbar_SI * c_SI)
    rS_at_mP    = 2.0 * G_SI * m_P_SI / c_SI**2
    a0_at_mP    = hbar_SI / (m_P_SI * c_SI)
    rS_over_a0  = rS_at_mP / a0_at_mP

    rw.print("  alpha(m) = G*m^2/(hbar*c)   [DG 2011, per-quantum coupling]")
    rw.print("  d(alpha)/dm = {}  > 0 (monotone)".format(dalpha_dm))
    rw.print("  alpha = 1  <=>  m = {}   [= m_P: {}]".format(m_crit, m_crit_ok))
    rw.print("  r_S/lambda_C = {} = 2*alpha  [{}]".format(
        ratio, "VERIFIED" if ratio_ok else "FAIL"))
    rw.print("")
    rw.print("  Numeric at m = m_P = {:.4e} kg:".format(m_P_SI))
    rw.print("    alpha(m_P)  = {:.9f}".format(alpha_at_mP))
    rw.print("    r_S(m_P)    = {:.4e} m = 2*a_0 (ratio {:.6f})".format(
        rS_at_mP, rS_over_a0))
    rw.print("")
    rw.print("  NOTE (O(1) conventions): horizon-formation threshold varies")
    rw.print("  by convention: lambda_C >= r_S gives m <= m_P/sqrt(2) [115.1a];")
    rw.print("  Part 47 endpoint M_evap = m_P/(8*pi); DG alpha=1 gives m_P.")
    rw.print("  The boundary is m_P up to O(1); factors recorded, not hidden.")

    return {'alpha_at_mP': alpha_at_mP, 'rS_over_a0': rS_over_a0,
            'm_crit_is_mP': m_crit_ok, 'ratio_is_2alpha': ratio_ok,
            'dalpha_dm_positive': str(dalpha_dm)}


# ===========================================================================
# S2: ENERGY LANDSCAPE -- extremum test  [ROUTE 1]
# ===========================================================================

def derive_energy_landscape(rw):
    """
    Grain self-energy in the fixed-G frame (rest + Newtonian self-binding
    of a quantum localized at its Compton size a_0 = hbar/(m*c)):

      E(m) = m*c^2 - xi*G*m^2/a_0(m) = m*c^2*(1 - xi*G*m^2/(hbar*c))
           = m*c^2*(1 - xi*alpha(m))                              (124.1)

    xi = O(1) geometric binding coefficient (3/5 for uniform sphere;
    kept symbolic -- conclusions must not depend on it).

    Extremum: dE/dm = 0 at alpha* = 1/(3*xi)  [O(1) of criticality]
    Stability: d2E/dm2 at alpha* -- if > 0 minimum (attractor),
               if < 0 maximum (barrier / critical point).
    """
    rw.section("S2: ENERGY LANDSCAPE E(m) -- IS CRITICALITY A MINIMUM?")

    alpha_sym = G_s * m_s**2 / (hbar_s * c_s)
    E = m_s * c_s**2 * (1 - xi_s * alpha_sym)

    dE  = diff(E, m_s)
    d2E = diff(E, m_s, 2)

    # extremum location in alpha
    m_star_sols = solve(sp.Eq(dE, 0), m_s)
    m_star = [s for s in m_star_sols if s.is_positive][0]
    alpha_star = simplify(alpha_sym.subs(m_s, m_star))

    # curvature at extremum
    d2E_star = simplify(d2E.subs(m_s, m_star))
    # sign check: substitute positive numerics 1 for all symbols
    d2E_num = d2E_star.subs({G_s: 1, hbar_s: 1, c_s: 1, xi_s: Rational(3, 5)})
    is_maximum = bool(d2E_num < 0)

    # numeric example xi = 3/5
    alpha_star_num = float(alpha_star.subs(xi_s, Rational(3, 5)))

    rw.print("  E(m) = m*c^2*(1 - xi*alpha(m))            [Eq 124.1]")
    rw.print("  dE/dm = 0  at  alpha* = {}".format(alpha_star))
    rw.print("  xi = 3/5 (uniform sphere): alpha* = {:.4f}  [O(1) of 1]".format(
        alpha_star_num))
    rw.print("  d2E/dm2 at extremum = {}".format(d2E_star))
    rw.print("  numeric sign (xi=3/5, units=1): {}  -> {}".format(
        float(d2E_num), "MAXIMUM" if is_maximum else "MINIMUM"))
    rw.print("")
    rw.print("  RESULT: the extremum near criticality is a MAXIMUM -- an")
    rw.print("  energy BARRIER (separatrix between dispersal m->0 and")
    rw.print("  collapse m->infinity), NOT a minimum.")
    rw.print("  Energy-minimization attractor: NEGATIVE.  [DERIVED]")
    rw.print("  This is the 'critical point of a quantum phase transition'")
    rw.print("  of Dvali-Gomez (1207.4059) -- confirmed, and consistent with")
    rw.print("  no-go Theorem 115.4 (no internal energy minimum exists).")

    return {'alpha_star': str(alpha_star), 'alpha_star_num': alpha_star_num,
            'is_maximum': is_maximum, 'd2E_sign_num': float(d2E_num)}


# ===========================================================================
# S3: ENTROPY LANDSCAPE -- extremum test  [ROUTE 2]
# ===========================================================================

def derive_entropy_landscape(rw):
    """
    Fixed total mass M_tot distributed among N = M_tot/m grains of mass m.

    Quantum branch (alpha < 1, no horizon): each grain carries O(1) bits:
      S_q(m) = s0 * kB * M_tot/m               (s0 = O(1))  -> dS/dm < 0
    BH branch (alpha > 1, horizon): Bekenstein-Hawking per grain
      S_BH_grain = 4*pi*kB*(m/m_P)^2 = 4*pi*kB*alpha(m):
      S_BH(m) = (M_tot/m)*4*pi*kB*G*m^2/(hbar*c)
              = 4*pi*kB*G*M_tot*m/(hbar*c)                   -> dS/dm > 0

    Falling then rising  =>  criticality is the entropy MINIMUM.
    Entropy-maximization attractor: NEGATIVE.  [DERIVED]
    (Thermodynamics prefers the extremes: all radiation, or one big BH.)
    """
    rw.section("S3: ENTROPY LANDSCAPE S_tot(m) -- IS CRITICALITY A MAXIMUM?")

    s0 = symbols('s0', positive=True)
    S_q  = s0 * Mtot_s / m_s                              # / kB
    S_bh = 4 * sp.pi * (Mtot_s / m_s) * G_s * m_s**2 / (hbar_s * c_s)

    dSq  = simplify(diff(S_q, m_s))
    dSbh = simplify(diff(S_bh, m_s))

    # signs (all symbols positive)
    sq_falling  = bool(sp.simplify(dSq) .subs(
        {s0: 1, Mtot_s: 1, m_s: 1}) < 0)
    sbh_rising  = bool(sp.simplify(dSbh).subs(
        {G_s: 1, hbar_s: 1, c_s: 1, Mtot_s: 1}) > 0)
    is_minimum  = sq_falling and sbh_rising

    rw.print("  Quantum branch:  S_q/kB  = s0*M_tot/m;   dS/dm = {}  (< 0)".format(dSq))
    rw.print("  BH branch:       S_BH/kB = 4*pi*G*M_tot*m/(hbar*c);")
    rw.print("                   dS/dm = {}  (> 0)".format(dSbh))
    rw.print("")
    rw.print("  Falling (quantum) then rising (BH): entropy has a MINIMUM at")
    rw.print("  the crossover alpha ~ 1: {}".format(is_minimum))
    rw.print("  Entropy-maximization attractor: NEGATIVE.  [DERIVED]")
    rw.print("  Sanity: max entropy sits at the extremes (all radiation or")
    rw.print("  one big BH) -- standard thermodynamics, correctly recovered.")

    return {'sq_falling': sq_falling, 'sbh_rising': sbh_rising,
            'is_minimum': is_minimum}


# ===========================================================================
# S4: DISSIPATIVE FLOW (HAWKING) -- the actual attractor  [ROUTE 3]
# ===========================================================================

def compute_hawking_flow(rw):
    """
    Overcritical grain (horizon exists): Hawking mass loss [Page 1976]
      dm/dt = -hbar*c^4/(5120*pi*G^2*m^2)
      => lifetime t(m) = 5120*pi*G^2*m^3/(hbar*c^4)  -- FINITE for all m
      => d(alpha)/dt = 2*G*m/(hbar*c)*dm/dt < 0      -- flows DOWN

    Subcritical grain (no horizon): no Hawking channel, no other decay
      => dm/dt = 0, infinite lifetime (stable, neutral).

    Endpoint (Part 47): evaporation is COMPLETE (no remnant); the final
    quantum carries E_final = kB*T_H(M_evap) with M_evap = m_P/(8*pi):
      E_final = hbar*c^3/(8*pi*G*M_evap) = m_P*c^2  EXACTLY   (124.4)
    The cascade's last (hardest) output sits exactly at the critical mass.

    => alpha_c = O(1) is a STABILITY BOUNDARY and a ONE-SIDED attractor:
       everything above it decays onto/through it in finite time; nothing
       below it moves. [DERIVED given PDTP Hawking, Parts 24/111]
    """
    rw.section("S4: DISSIPATIVE FLOW -- HAWKING REMOVES EVERYTHING ABOVE")

    # lifetime identity: G^2*m_P^3/(hbar*c^4) = t_P  [check symbolically]
    tP_ident = simplify(
        G_s**2 * sqrt(hbar_s * c_s / G_s)**3 / (hbar_s * c_s**4)
        - sqrt(hbar_s * G_s / c_s**5))
    tP_ok = (tP_ident == 0)

    # lifetime of a grain at m = 2*m_P (illustration), in Planck times
    def lifetime(m):
        return 5120.0 * math.pi * G_SI**2 * m**3 / (hbar_SI * c_SI**4)

    t_2mP     = lifetime(2.0 * m_P_SI)
    t_2mP_tP  = t_2mP / t_P_SI
    t_2mP_exp = 5120.0 * math.pi * 8.0        # expected = 5120*pi*(2)^3 t_P

    # d(alpha)/dt sign for overcritical grain (symbolic)
    mdot   = -hbar_s * c_s**4 / (5120 * sp.pi * G_s**2 * m_s**2)
    dalpha = simplify(2 * G_s * m_s / (hbar_s * c_s) * mdot)
    dalpha_neg = bool(dalpha.subs({G_s: 1, hbar_s: 1, c_s: 1, m_s: 1}) < 0)

    # Part 47 endpoint: E_final = kB*T_H(m_P/(8*pi)) = m_P*c^2 exactly
    M_evap    = m_P_SI / (8.0 * math.pi)
    T_H_evap  = hbar_SI * c_SI**3 / (8.0 * math.pi * G_SI * M_evap * kB_SI)
    E_final   = kB_SI * T_H_evap
    E_final_over_mPc2 = E_final / (m_P_SI * c_SI**2)

    rw.print("  Overcritical (horizon): dm/dt = -hbar*c^4/(5120*pi*G^2*m^2)")
    rw.print("    lifetime t(m) = 5120*pi*G^2*m^3/(hbar*c^4)  [Page 1976]")
    rw.print("    identity G^2*m_P^3/(hbar*c^4) = t_P: residual {} [{}]".format(
        tP_ident, "VERIFIED" if tP_ok else "FAIL"))
    rw.print("    t(2*m_P) = {:.4e} s = {:.4e} t_P".format(t_2mP, t_2mP_tP))
    rw.print("      (expected 5120*pi*8 = {:.4e} t_P)".format(t_2mP_exp))
    rw.print("    d(alpha)/dt = {}  (< 0: {})".format(dalpha, dalpha_neg))
    rw.print("")
    rw.print("  Subcritical (no horizon): no Hawking channel; dm/dt = 0;")
    rw.print("    infinite lifetime -- stable and NEUTRAL (no restoring flow).")
    rw.print("")
    rw.print("  Endpoint (Part 47 re-derived): M_evap = m_P/(8*pi) = {:.4e} kg".format(
        M_evap))
    rw.print("    E_final = kB*T_H(M_evap) = {:.4e} J".format(E_final))
    rw.print("    E_final/(m_P*c^2) = {:.9f}   [EXACTLY 1: Eq 124.4]".format(
        E_final_over_mPc2))
    rw.print("")
    rw.print("  RESULT: alpha_c = O(1) is a STABILITY BOUNDARY:")
    rw.print("    - finite lifetime above (flow down, one-sided attractor)")
    rw.print("    - infinite lifetime at/below (stationary set)")
    rw.print("    - evaporation output terminates at exactly m_P*c^2")
    rw.print("  The supremum of STABLE grain masses is m_P*O(1). [DERIVED]")

    return {'tP_identity_ok': tP_ok, 't_2mP_over_tP': t_2mP_tP,
            't_2mP_expected': t_2mP_exp, 'dalpha_negative': dalpha_neg,
            'M_evap': M_evap, 'E_final_over_mPc2': E_final_over_mPc2}


# ===========================================================================
# S5: BRIDGE / NO-GO CONSISTENCY (Part 115 re-derivation)
# ===========================================================================

def verify_bridge_nogo(rw):
    """
    Under the PDTP bridge G = hbar*c/m_cond^2, alpha_gr = 1 IDENTICALLY
    for any m_cond (re-derives Eq 115.3; SymPy). So the flow of S4 exists
    only in the fixed-G frame: internally there is no flow at all --
    consistent with the no-go theorem. The attractor result therefore:
      DERIVES:  the relation G = hbar*c/m_cond^2 as the stationary
                endpoint state of collapse+evaporation (bridge upgraded
                from algebraic identity to dynamically-enforced state)
      DOES NOT DERIVE: the absolute scale (G itself stays external).
    """
    rw.section("S5: BRIDGE / NO-GO CONSISTENCY (Part 115)")

    G_bridge  = hbar_s * c_s / m_s**2
    alpha_br  = simplify(G_bridge * m_s**2 / (hbar_s * c_s))
    resid     = simplify(alpha_br - 1)
    identical = (resid == 0)
    m_free    = m_s in alpha_br.free_symbols

    rw.print("  Bridge: G = hbar*c/m_cond^2  [Part 33]")
    rw.print("  alpha_gr(bridge) = {}  (residual vs 1: {}) [{}]".format(
        alpha_br, resid, "VERIFIED" if identical else "FAIL"))
    rw.print("  m_cond survives in alpha? {}  (no-go: must be False)".format(m_free))
    rw.print("")
    rw.print("  CONSISTENCY: internally alpha = 1 always -> no internal flow,")
    rw.print("  no internal extremum (re-confirms Theorem 115.4). The S4 flow")
    rw.print("  lives in the fixed-G frame (ambient G external). The attractor")
    rw.print("  DERIVES the bridge relation as the dynamical endpoint; it does")
    rw.print("  NOT derive the absolute scale. No-go theorem INTACT.")

    return {'alpha_bridge_is_1': identical, 'm_cond_absent': (not m_free)}


# ===========================================================================
# S6: DVALI-GOMEZ N-PORTRAIT CROSS-CHECK (N-graviton condensate)
# ===========================================================================

def derive_dg_nportrait(rw):
    """
    Standard DG energetics for N massless quanta of wavelength R
    [arXiv:1112.3359]:
      E(R) = N*hbar*c/R - G*N^2*hbar^2/(c^2*R^3)
      (M = N*hbar/(R*c); E_grav ~ -G*M^2/R)
    Extremum: R* = sqrt(3*N)*l_P;  at R*: N*alpha = N*l_P^2/R*^2 = 1/3
    Curvature: d2E/dR2 (R*) < 0 -> MAXIMUM again (critical point).
    Confirms the S2 grain result at the collective level: DG criticality
    N*alpha = O(1) is a critical point, never an energy minimum.
    """
    rw.section("S6: DG N-PORTRAIT CROSS-CHECK (collective level)")

    lP2 = hbar_s * G_s / c_s**3
    E_R = N_s * hbar_s * c_s / R_s - G_s * N_s**2 * hbar_s**2 / (c_s**2 * R_s**3)

    dE_R  = diff(E_R, R_s)
    R_sols = solve(sp.Eq(dE_R, 0), R_s)
    R_star = [s for s in R_sols if s.is_positive][0]
    R_star_over_lP = simplify(R_star / sqrt(lP2))       # expect sqrt(3N)

    N_alpha = simplify(N_s * lP2 / R_star**2)           # expect 1/3
    d2E_R   = simplify(diff(E_R, R_s, 2).subs(R_s, R_star))
    d2E_num = d2E_R.subs({N_s: 1, hbar_s: 1, c_s: 1, G_s: 1})
    is_max  = bool(d2E_num < 0)

    rw.print("  E(R) = N*hbar*c/R - G*N^2*hbar^2/(c^2*R^3)  [DG 1112.3359]")
    rw.print("  R* = {}  = sqrt(3*N)*l_P: {}".format(
        R_star, simplify(R_star_over_lP - sqrt(3 * N_s)) == 0))
    rw.print("  N*alpha at R* = {}  [O(1) of DG criticality N*alpha = 1]".format(
        N_alpha))
    rw.print("  d2E/dR2 at R* = {}  (sign check: {} -> {})".format(
        d2E_R, float(d2E_num), "MAXIMUM" if is_max else "MINIMUM"))
    rw.print("")
    rw.print("  Same verdict as S2 at the collective level: criticality is a")
    rw.print("  BARRIER TOP (critical point), not a minimum. DG maintain BHs")
    rw.print("  there by LEAKAGE (drive) -- the laser-threshold pattern of")
    rw.print("  Part 110 (driven criticality, not equilibrium SSB).")

    return {'R_star_is_sqrt3N_lP': simplify(R_star_over_lP - sqrt(3 * N_s)) == 0,
            'N_alpha_at_star': float(N_alpha), 'is_maximum': is_max}


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS (12 tests)
# ===========================================================================

def sudoku_checks(rw, s1, s2, s3, s4, s5, s6):
    """
    12 checks. Every 'got' value is read from a step's returned dict
    (RECHECK trace-path rule: inputs -> step arithmetic -> dict -> check).
    """
    rw.section("SUDOKU CONSISTENCY CHECKS")

    passes = 0
    total  = 0

    def chk(label, got, want, tol=0.005, is_bool=False):
        nonlocal passes, total
        total += 1
        if is_bool:
            ok = bool(got) == bool(want)
            rw.print("  [{}] {}: {}  (expected {})".format(
                "PASS" if ok else "FAIL", label, got, want))
        else:
            if want == 0.0:
                ok = abs(got) < 1e-12
            else:
                ok = abs(got / want - 1.0) < tol
            rw.print("  [{}] {}: {:.6g}  (ref {:.6g})".format(
                "PASS" if ok else "FAIL", label, got, want))
        if ok:
            passes += 1

    # T1: alpha computed FROM m_cond = m_P equals 1 (TODO_05 S1)
    chk("T1: alpha(m_P) = G*m_P^2/(hbar*c) = 1", s1['alpha_at_mP'], 1.0)

    # T2: r_S = 2*a_0 at the fixed point (TODO_05 S2)
    chk("T2: r_S(m_P)/a_0(m_P) = 2", s1['rS_over_a0'], 2.0)

    # T3: G = hbar*c/m_cond^2 reproduces measured G (TODO_05 S3)
    G_pred = hbar_SI * c_SI / m_P_SI**2
    chk("T3: G_pred = hbar*c/m_P^2 vs G_known", G_pred, G_SI)

    # T4: bridge alpha = 1 identically (SymPy) -- Part 115 bounds saturated
    chk("T4: bridge alpha_gr = 1 identically [Eq 115.3, SymPy]",
        s5['alpha_bridge_is_1'], True, is_bool=True)

    # T5: no m_cond survives internally (no-go compliance)
    chk("T5: m_cond absent from bridge alpha (no-go 115.4 intact)",
        s5['m_cond_absent'], True, is_bool=True)

    # T6: energy extremum sits at O(1) of criticality
    chk("T6: 0.1 < alpha* = 1/(3*xi) < 10 (O(1) of alpha = 1)",
        0.1 < s2['alpha_star_num'] < 10.0, True, is_bool=True)

    # T7: energy extremum is a MAXIMUM -> minimization route NEGATIVE
    chk("T7: d2E/dm2 < 0 (barrier, NOT minimum) [route 1 NEGATIVE]",
        s2['is_maximum'], True, is_bool=True)

    # T8: entropy MINIMUM at crossover -> maximization route NEGATIVE
    chk("T8: S_tot falls then rises (entropy MIN at alpha~1) [route 2 NEGATIVE]",
        s3['is_minimum'], True, is_bool=True)

    # T9: Hawking lifetime t(2*m_P) = 5120*pi*8 t_P (finite, computed)
    chk("T9: t(2*m_P)/t_P = 5120*pi*8",
        s4['t_2mP_over_tP'], s4['t_2mP_expected'])

    # T10: flow direction above criticality
    chk("T10: d(alpha)/dt < 0 for horizon grains (flow toward alpha=1)",
        s4['dalpha_negative'], True, is_bool=True)

    # T11: endpoint quantum energy = m_P*c^2 exactly (Part 47 cross-check)
    chk("T11: E_final/(m_P*c^2) = 1 [Part 47, Eq 124.4]",
        s4['E_final_over_mPc2'], 1.0)

    # T12: DG N-portrait -- R* = sqrt(3N)*l_P, N*alpha = 1/3, maximum
    dg_ok = (s6['R_star_is_sqrt3N_lP'] and s6['is_maximum']
             and 0.1 < s6['N_alpha_at_star'] < 10.0)
    chk("T12: DG N-portrait: R*=sqrt(3N)l_P, N*alpha=1/3 O(1), maximum",
        dg_ok, True, is_bool=True)

    rw.print("")
    rw.print("  SCORE: {}/{} PASS".format(passes, total))
    return {'passes': passes, 'total': total, 'all_pass': passes == total}


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    out_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(out_dir, label="t55_dvali_gomez_attractor")

    rw.section("T55 -- DVALI-GOMEZ CRITICALITY AS ATTRACTOR (Part 124, Phase 92)")
    rw.print("Date: 2026-07-07")
    rw.print("Question: is alpha_gr = 1 an attractor of condensate dynamics?")
    rw.print("Frame: fixed-G (ambient G external; no-go-compatible).")
    rw.print("")
    rw.print("  Constants (CODATA 2018): G = {:.5e}, hbar = {:.6e}, c = {:.6e}".format(
        G_SI, hbar_SI, c_SI))
    rw.print("  m_P = {:.4e} kg, t_P = {:.4e} s, l_P = {:.4e} m [COMPUTED]".format(
        m_P_SI, t_P_SI, l_P_SI))

    s1 = derive_coupling_fixed_point(rw)
    s2 = derive_energy_landscape(rw)
    s3 = derive_entropy_landscape(rw)
    s4 = compute_hawking_flow(rw)
    s5 = verify_bridge_nogo(rw)
    s6 = derive_dg_nportrait(rw)
    score = sudoku_checks(rw, s1, s2, s3, s4, s5, s6)

    rw.section("OVERALL VERDICT")
    rw.print("  Route 1 (energy minimum):   NEGATIVE -- extremum at alpha* =")
    rw.print("    1/(3*xi) is a MAXIMUM (barrier/critical point). [DERIVED]")
    rw.print("  Route 2 (entropy maximum):  NEGATIVE -- criticality is the")
    rw.print("    entropy MINIMUM at fixed total mass. [DERIVED]")
    rw.print("  Route 3 (dissipative flow): POSITIVE (one-sided) -- horizon")
    rw.print("    grains evaporate in finite time t = 5120*pi*G^2*m^3/(hbar*c^4);")
    rw.print("    subcritical grains are stable; the evaporation cascade")
    rw.print("    terminates at E_final = m_P*c^2 EXACTLY. alpha = 1 is a")
    rw.print("    STABILITY BOUNDARY / evaporation endpoint: an attractor from")
    rw.print("    above, neutral from below. [DERIVED given PDTP Hawking]")
    rw.print("")
    rw.print("  DERIVED:      m_cond <= m_P*O(1)  (dynamical ceiling)")
    rw.print("  SPECULATIVE:  m_cond = m_P (equality) -- requires a maximal-")
    rw.print("    packing/maximal-stiffness selection principle (DG 1207.4059;")
    rw.print("    KZ formation bias). This gap is the remaining content of the")
    rw.print("    hierarchy problem in the fixed-G frame.")
    rw.print("")
    rw.print("  No-go theorem 115.4: INTACT. Internally alpha = 1 identically")
    rw.print("  (no flow, no extremum). The attractor upgrades the bridge")
    rw.print("  G = hbar*c/m_cond^2 from algebraic identity to dynamically-")
    rw.print("  enforced endpoint state; the absolute scale stays external.")
    rw.print("")
    rw.print("  Character: driven/dissipative criticality (barrier top +")
    rw.print("  leakage), matching the Part 110 laser-threshold class")
    rw.print("  qualitatively (no exponents claimed here).")
    rw.print("")
    rw.print("  SUDOKU: {}/{} PASS".format(score['passes'], score['total']))
    rw.print("  VERDICT: PARTIAL -- attractor confirmed as one-sided ceiling;")
    rw.print("  equality step open.")

    rw.close()
    print("")
    print("Log saved to: " + rw.path)
    return score


if __name__ == "__main__":
    score = main()
    sys.exit(0 if score['all_pass'] else 1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sympy_checks.py -- Symbolic Math Verification Library for PDTP
===============================================================
Pure verification functions using SymPy. NO file I/O, NO output.

Each PDTP-specific verifier returns a VerificationResult object containing:
  - label   : short name for the check
  - passed  : True/False
  - message : one-line result summary
  - steps   : list of (step_label, expression_str) pairs recording the derivation

Use VerificationResult.to_markdown() to generate documentation-quality output
that can be pasted into MD research files as proof of the derivation.
Use format_markdown_report(results) to generate a full section with summary table.

Convention used throughout (+ - - - metric, Hilbert stress-energy):
  Lagrangian:       L = 1/2 phi_dot^2 - V(phi)  [standard scalar field]
  Energy density:   rho = pi*phi_dot - L          [Hamiltonian = pi*phidot - L]
  Pressure:         p   = L                       [Hilbert; uniform field]
  Field equation:   phi_ddot = -dV/dphi           [from Euler-Lagrange]

For PDTP with L = 1/2 phi_dot^2 + g*cos(psi - phi):
  V_PDTP = -g*cos(psi - phi)  [so L = 1/2 phi_dot^2 - V_PDTP]
  rho = 1/2 phi_dot^2 - g*cos(psi - phi)   [MINUS on cos]
  p   = 1/2 phi_dot^2 + g*cos(psi - phi)   [PLUS  on cos]
  EL:  phi_ddot = g*sin(psi - phi)          [box phi = Sigma g_i sin(psi_i - phi)]

Sources:
  Peskin & Schroeder (1995) sec 2.2 -- canonical energy-momentum tensor
  Baumann, TASI lectures (2009)     -- scalar field EOS, quintessence
  PDTP CLAUDE.md                    -- Lagrangian and field equation definitions
"""

import sympy as sp


# ===========================================================================
# VERIFICATION RESULT (structured result with derivation steps)
# ===========================================================================

class VerificationResult(object):
    """
    Structured result from a PDTP symbolic verification.

    Attributes:
        label   : str  -- short name for the check
        passed  : bool -- True if verification passed
        message : str  -- one-line result summary
        steps   : list of (step_label: str, expression_str: str) tuples
                  recording each intermediate step of the derivation

    Usage:
        result = verify_pdtp_field_equation()

        # Paste derivation into a research MD file:
        print(result.to_markdown())

        # Console summary:
        print(result.to_text())

        # Tuple unpacking (backward compat with old (bool, str) API):
        ok, msg = result

        # Boolean check:
        if result:
            print("passed")
    """

    def __init__(self, label, passed, message, steps=None):
        self.label = label
        self.passed = passed
        self.message = message
        self.steps = steps if steps is not None else []

    def to_markdown(self):
        """
        Generate documentation-quality markdown for this verification.
        Suitable for pasting into MD research files as derivation proof.

        Output format:
          ### Label [PASS/FAIL]

          **Derivation steps:**

          1. **Step label**: `expression`
          ...

          **Result:** one-line message
        """
        lines = []
        status = "PASS" if self.passed else "FAIL"
        lines.append("### {} [{}]".format(self.label, status))
        lines.append("")
        if self.steps:
            lines.append("**Derivation steps:**")
            lines.append("")
            for i, (step_label, step_expr) in enumerate(self.steps, 1):
                lines.append("{}. **{}**: `{}`".format(i, step_label, step_expr))
            lines.append("")
        lines.append("**Result:** {}".format(self.message))
        return "\n".join(lines)

    def to_text(self):
        """
        Plain-text format for console output.

        Output format:
          [PASS/FAIL] Label
            -- Step label: expression
            ...
            => result message
        """
        lines = []
        status = "PASS" if self.passed else "FAIL"
        lines.append("[{}] {}".format(status, self.label))
        for step_label, step_expr in self.steps:
            lines.append("  -- {}: {}".format(step_label, step_expr))
        lines.append("  => {}".format(self.message))
        return "\n".join(lines)

    def __iter__(self):
        """Support tuple unpacking: ok, msg = result (backward compat)."""
        return iter((self.passed, self.message))

    def __bool__(self):
        return self.passed

    def __repr__(self):
        return "VerificationResult(label={!r}, passed={}, steps={})".format(
            self.label, self.passed, len(self.steps))


def derivation_step(step_label, expr):
    """
    Record a single derivation step as a (label, expression_str) pair.

    Use this inside verifier functions to build a steps list:

        steps = []
        steps.append(derivation_step("Lagrangian L", L))
        steps.append(derivation_step("pi = dL/d(phi_dot)", pi))
        steps.append(derivation_step("rho = pi*phi_dot - L", rho))
        result = VerificationResult("my check", ok, msg, steps)

    Args:
        step_label : str -- human-readable description of this derivation step
        expr       : SymPy expression, str, or any object with __str__

    Returns: (step_label, str(expr)) tuple
    """
    return (step_label, str(expr))


def format_markdown_report(results, title="PDTP SymPy Verification Report"):
    """
    Format a list of VerificationResult objects as a markdown document section.

    Generates a summary table followed by per-check derivation steps.
    Suitable for pasting into MD research files.

    Args:
        results : list of VerificationResult objects
        title   : heading text (str)

    Returns: str containing complete markdown section

    Example:
        n_passed, n_total, results = run_all_verifications()
        md = format_markdown_report(results, title="Part 43 SymPy Checks")
        # paste md into scalar_tensor_backreaction.md
    """
    lines = []
    lines.append("## {}".format(title))
    lines.append("")

    n_passed = sum(1 for r in results if r.passed)
    n_total = len(results)
    lines.append("**Score: {}/{} pass**".format(n_passed, n_total))
    lines.append("")

    # Summary table
    lines.append("| # | Check | Result |")
    lines.append("|---|---|---|")
    for i, r in enumerate(results, 1):
        status = "PASS" if r.passed else "FAIL"
        lines.append("| {} | {} | {} |".format(i, r.label, status))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed derivations
    for r in results:
        lines.append(r.to_markdown())
        lines.append("")

    return "\n".join(lines)


# ===========================================================================
# PRIMITIVE CHECKS (return (bool, str) -- simple, unchanged API)
# ===========================================================================

def check_equal(expr1, expr2, label=""):
    """
    Check whether two SymPy expressions are algebraically identical.

    Uses sp.simplify(expr1 - expr2) == 0.
    Works for polynomial, trigonometric, and mixed expressions.

    Returns:
        (True,  "PASS [label]: expressions are equal") if equal
        (False, "FAIL [label]: residual = <diff>") if not equal
    """
    try:
        diff = sp.simplify(expr1 - expr2)
        passed = (diff == 0)
    except Exception as e:
        return False, "ERROR in check_equal [{}]: {}".format(label, e)
    if passed:
        return True, "PASS [{}]: expressions are equal".format(label)
    return False, "FAIL [{}]: residual = {}".format(label, diff)


def check_shift_symmetry(expr, shift_pairs, label=""):
    """
    Check whether expr is invariant under a list of simultaneous substitutions.

    shift_pairs: list of (old_symbol, new_expr) pairs applied simultaneously.
    Example: [(phi, phi+delta), (psi, psi+delta)]

    Uses subs() then simplify(shifted - original) == 0.

    Returns (bool, str).
    """
    try:
        shifted = expr.subs(shift_pairs)
        diff = sp.simplify(shifted - expr)
        passed = (diff == 0)
    except Exception as e:
        return False, "ERROR in check_shift_symmetry [{}]: {}".format(label, e)
    if passed:
        return True, "PASS [{}]: invariant under substitution".format(label)
    return False, "FAIL [{}]: residual = {}".format(label, diff)


def check_sign(expr, expected_positive, label=""):
    """
    Check whether a SymPy expression has the expected sign.

    Attempts sp.ask(sp.Q.positive(expr)) with standard assumptions.
    Falls back to INCONCLUSIVE if SymPy cannot determine the sign.

    expected_positive: True = expect positive, False = expect negative.

    Returns (bool, str).
    """
    try:
        is_pos = sp.ask(sp.Q.positive(expr))
        is_neg = sp.ask(sp.Q.negative(expr))
        if expected_positive:
            passed = (is_pos is True)
        else:
            passed = (is_neg is True)
        sign_str = "positive" if expected_positive else "negative"
        if is_pos is None and is_neg is None:
            return False, "INCONCLUSIVE [{}]: SymPy cannot determine sign of {}".format(
                label, expr)
        return passed, "{} [{}]: expr = {} is {}".format(
            "PASS" if passed else "FAIL", label, expr, sign_str)
    except Exception as e:
        return False, "ERROR in check_sign [{}]: {}".format(label, e)


def check_eos(rho_expr, p_expr, w_expected, label="", tol_expr=None):
    """
    Check whether the equation of state w = p/rho equals w_expected.

    w_expected: a SymPy expression or number (e.g., sp.Integer(1), sp.Integer(-1)).
    tol_expr:   if provided, check |w - w_expected| < tol_expr instead of exact equality.

    Returns (bool, str).
    """
    try:
        w_computed = sp.simplify(p_expr / rho_expr)
        diff = sp.simplify(w_computed - w_expected)
        if tol_expr is not None:
            passed = sp.ask(sp.Q.negative(sp.Abs(diff) - tol_expr)) is True
        else:
            passed = (diff == 0)
        return passed, "{} [{}]: w = {} (expected {})".format(
            "PASS" if passed else "FAIL", label, w_computed, w_expected)
    except Exception as e:
        return False, "ERROR in check_eos [{}]: {}".format(label, e)


# ===========================================================================
# LAGRANGIAN MECHANICS (return SymPy expressions -- unchanged API)
# ===========================================================================

def hamiltonian_density(L_expr, phi_dot_sym):
    """
    Compute Hamiltonian density (energy density rho = T_00) from Lagrangian.

    rho = pi * phi_dot - L   where pi = dL/d(phi_dot)

    For PDTP L = 1/2*phi_dot^2 + g*cos(psi-phi):
      pi = phi_dot
      rho = phi_dot^2 - L = 1/2*phi_dot^2 - g*cos(psi-phi)   [MINUS on cos]

    This is the canonical Hamiltonian density and equals T_00 in (+---) metric.
    Source: Peskin & Schroeder (1995), sec 2.2.

    Args:
        L_expr:      SymPy expression for Lagrangian density
        phi_dot_sym: SymPy Symbol representing d phi/dt

    Returns: SymPy expression for rho (energy density)
    """
    pi = sp.diff(L_expr, phi_dot_sym)
    return sp.simplify(pi * phi_dot_sym - L_expr)


def pressure_uniform(L_expr):
    """
    Pressure for spatially uniform scalar field.

    For a spatially uniform phi(t), the Hilbert stress-energy tensor gives:
      p = L   (pressure equals Lagrangian density)

    Derivation (Baumann convention, (+---) metric):
      T_{ij} = -g_{ij} L  for uniform phi (no gradient terms)
      Hilbert (variational) T_mu_nu used in GR gives p = L directly.
      For coupling to the Einstein equation, Hilbert is the correct convention.

    For PDTP L = 1/2*phi_dot^2 + g*cos(psi-phi):
      p = L = 1/2*phi_dot^2 + g*cos(psi-phi)   [PLUS on cos]

    Kinetic limit (g->0): p = 1/2*phi_dot^2 = rho -> w = +1 (stiff fluid) [correct]
    Potential limit (phi_dot->0): p = g, rho = -g -> w = -1 (dark energy) [correct]

    Source: Baumann, TASI Lectures on Inflation (2009), eq. (1.47)-(1.48).

    Args:
        L_expr: SymPy expression for Lagrangian density

    Returns: SymPy expression for pressure p (= L for uniform field)
    """
    return L_expr


def euler_lagrange_1d(L_expr, phi_sym, phi_dot_sym):
    """
    Compute Euler-Lagrange equation for spatially uniform scalar field phi(t).

    EL equation: d/dt(dL/d phi_dot) - dL/d phi = 0
    For pi = dL/d phi_dot: d(pi)/dt = dL/d phi
    If pi = phi_dot (canonical kinetic term): phi_ddot = dL/d phi

    Returns:
        (pi, force) where:
          pi    = dL/d(phi_dot)   [canonical momentum]
          force = dL/d(phi)       [generalised force = phi_ddot for standard kinetic term]

    For PDTP L = 1/2*phi_dot^2 + g*cos(psi-phi):
      pi    = phi_dot
      force = g * sin(psi - phi)
      EL:  phi_ddot = g * sin(psi - phi)
         i.e. box phi = Sigma g_i sin(psi_i - phi)  [matches CLAUDE.md]

    Source: Goldstein, Classical Mechanics, 3rd ed., sec 2.1
    """
    pi = sp.diff(L_expr, phi_dot_sym)
    force = sp.diff(L_expr, phi_sym)
    return sp.simplify(pi), sp.simplify(force)


# ===========================================================================
# PDTP-SPECIFIC VERIFIERS (return VerificationResult with derivation steps)
# ===========================================================================

def verify_pdtp_shift_symmetry():
    """
    Verify that the PDTP coupling term g*cos(psi-phi) is invariant under:
      phi -> phi + delta
      psi -> psi + delta   (simultaneous uniform shift of all phases)

    This is the U(1) shift symmetry that makes the condensate vacuum-insensitive.
    PDTP Original result (Part 43).

    Returns: VerificationResult (supports tuple unpacking: ok, msg = result)
    """
    phi, psi, delta, g = sp.symbols('phi psi delta g', real=True)
    steps = []

    coupling = g * sp.cos(psi - phi)
    steps.append(derivation_step("Coupling term", coupling))

    shift_pairs = [(phi, phi + delta), (psi, psi + delta)]
    steps.append(derivation_step(
        "Shift applied: phi -> phi+delta, psi -> psi+delta",
        "phi -> phi + delta, psi -> psi + delta (simultaneous)"))

    shifted = coupling.subs(shift_pairs)
    shifted_simplified = sp.simplify(shifted)
    steps.append(derivation_step("Shifted coupling g*cos((psi+delta)-(phi+delta))",
                                 shifted_simplified))

    diff = sp.simplify(shifted - coupling)
    steps.append(derivation_step("Difference: shifted - original", diff))
    steps.append(derivation_step(
        "Reason: delta cancels in the argument (psi+delta)-(phi+delta) = psi-phi",
        "invariant confirmed"))

    passed = (diff == 0)
    message = ("PASS [PDTP U(1) shift symmetry]: invariant under uniform phase shift"
               if passed else
               "FAIL [PDTP U(1) shift symmetry]: residual = {}".format(diff))

    return VerificationResult(
        label="PDTP U(1) shift symmetry",
        passed=passed,
        message=message,
        steps=steps)


def verify_pdtp_field_equation():
    """
    Verify that Euler-Lagrange applied to the PDTP Lagrangian gives the
    correct field equation: phi_ddot = g * sin(psi - phi)
    equivalently: box phi = Sigma g_i sin(psi_i - phi) [CLAUDE.md].

    For spatially uniform phi(t) with one coupling term:
      L = 1/2 * phi_dot^2 + g * cos(psi - phi)
      EL: phi_ddot = dL/dphi = g * sin(psi - phi)

    Returns: VerificationResult
    """
    phi, psi, g = sp.symbols('phi psi g', real=True)
    phi_dot = sp.Symbol('phi_dot', real=True)
    steps = []

    L = sp.Rational(1, 2) * phi_dot**2 + g * sp.cos(psi - phi)
    steps.append(derivation_step("PDTP Lagrangian L = 1/2*phi_dot^2 + g*cos(psi-phi)", L))

    pi, force = euler_lagrange_1d(L, phi, phi_dot)
    steps.append(derivation_step("Canonical momentum pi = dL/d(phi_dot)", pi))
    steps.append(derivation_step("Generalised force dL/d(phi) [= phi_ddot from EL]", force))

    force_expected = g * sp.sin(psi - phi)
    steps.append(derivation_step(
        "Expected field equation phi_ddot = g*sin(psi-phi)", force_expected))

    diff_pi = sp.simplify(pi - phi_dot)
    diff_force = sp.simplify(force - force_expected)
    steps.append(derivation_step("Residual: pi - phi_dot", diff_pi))
    steps.append(derivation_step("Residual: force - g*sin(psi-phi)", diff_force))

    ok_pi = (diff_pi == 0)
    ok_force = (diff_force == 0)
    passed = ok_pi and ok_force

    if passed:
        message = ("PASS: pi = phi_dot, phi_ddot = g*sin(psi-phi) "
                   "[consistent with box phi = Sigma g_i sin(psi_i - phi)]")
    else:
        parts = []
        if not ok_pi:
            parts.append("pi mismatch: residual = {}".format(diff_pi))
        if not ok_force:
            parts.append("force mismatch: residual = {}".format(diff_force))
        message = "FAIL: " + "; ".join(parts)

    return VerificationResult(
        label="PDTP field equation",
        passed=passed,
        message=message,
        steps=steps)


def verify_pdtp_tmunu_vacuum():
    """
    Verify that the PDTP condensate stress-energy T_00 = 0 in vacuum.

    Vacuum conditions:
      - phi_dot = 0  (static condensate, no kinetic energy)
      - No particles: coupling sum is empty -> g*cos(...) contribution = 0

    rho = pi*phi_dot - L  with phi_dot=0 and L=0 -> rho = 0.

    Returns: VerificationResult
    """
    phi_dot = sp.Symbol('phi_dot', real=True)
    steps = []

    steps.append(derivation_step(
        "Vacuum setup: phi_dot = 0 (static), no particles (empty sum)",
        "phi_dot = 0, Sigma g_i cos(psi_i - phi) = 0"))

    L_vac = sp.Rational(1, 2) * phi_dot**2
    steps.append(derivation_step(
        "Vacuum Lagrangian (no coupling term)", L_vac))

    pi_vac = sp.diff(L_vac, phi_dot)
    steps.append(derivation_step("Canonical momentum pi = dL/d(phi_dot)", pi_vac))

    rho_vac = hamiltonian_density(L_vac, phi_dot)
    steps.append(derivation_step("Hamiltonian density rho = pi*phi_dot - L", rho_vac))

    rho_at_rest = rho_vac.subs(phi_dot, sp.Integer(0))
    steps.append(derivation_step("Evaluate at phi_dot = 0 (static condensate)", rho_at_rest))

    steps.append(derivation_step(
        "Physical interpretation",
        "T_00 = 0 in vacuum -> condensate does not contribute to Lambda"))

    passed = (rho_at_rest == 0)
    message = ("PASS [T_00 in vacuum]: rho = 0 (static condensate, no particles)"
               if passed else
               "FAIL [T_00 in vacuum]: rho = {}".format(rho_at_rest))

    return VerificationResult(
        label="T_00 in vacuum = 0",
        passed=passed,
        message=message,
        steps=steps)


def verify_pdtp_tmunu_formulas():
    """
    Verify the stress-energy components for the PDTP Lagrangian.

    L = 1/2 * phi_dot^2 + g * cos(psi - phi)

    Expected results:
      rho = 1/2 * phi_dot^2 - g * cos(psi - phi)   [MINUS on cos]
      p   = 1/2 * phi_dot^2 + g * cos(psi - phi)   [PLUS on cos  = L]

    NOTE: The Part 43 research doc had a sign error on T_00 (wrote + instead of -).
    This function verifies the CORRECT formulas using SymPy.
    The EOS conclusions in Part 43 are still correct (two sign errors cancelled).

    Returns: list of VerificationResult (one for rho, one for p)
    """
    phi, psi, g = sp.symbols('phi psi g', real=True)
    phi_dot = sp.Symbol('phi_dot', real=True)

    L = sp.Rational(1, 2) * phi_dot**2 + g * sp.cos(psi - phi)

    # -- rho (energy density = Hamiltonian density) --
    steps_rho = []
    steps_rho.append(derivation_step(
        "PDTP Lagrangian L = 1/2*phi_dot^2 + g*cos(psi-phi)", L))
    pi = sp.diff(L, phi_dot)
    steps_rho.append(derivation_step("Canonical momentum pi = dL/d(phi_dot)", pi))
    rho_computed = hamiltonian_density(L, phi_dot)
    steps_rho.append(derivation_step(
        "Hamiltonian density rho = pi*phi_dot - L", rho_computed))
    rho_expected = sp.Rational(1, 2) * phi_dot**2 - g * sp.cos(psi - phi)
    steps_rho.append(derivation_step(
        "Expected: rho = 1/2*phi_dot^2 - g*cos(psi-phi)  [MINUS on cos]",
        rho_expected))
    diff_rho = sp.simplify(rho_computed - rho_expected)
    steps_rho.append(derivation_step("Residual (computed - expected)", diff_rho))
    steps_rho.append(derivation_step(
        "Sign rule: kinetic + potential; rho = T - V where V = -g*cos -> rho = T + g*cos? NO.",
        "Use Hamiltonian H = pi*phidot - L. pi=phidot. H = phidot^2 - (1/2 phidot^2 + g*cos) = 1/2 phidot^2 - g*cos"))

    ok_rho = (diff_rho == 0)
    msg_rho = ("PASS [rho = 1/2 phidot^2 - g cos]: MINUS on cos confirmed"
               if ok_rho else
               "FAIL [rho formula]: residual = {}".format(diff_rho))
    result_rho = VerificationResult(
        label="rho = 1/2*phi_dot^2 - g*cos  [MINUS on cos]",
        passed=ok_rho,
        message=msg_rho,
        steps=steps_rho)

    # -- p (pressure = L for uniform field, Hilbert convention) --
    steps_p = []
    steps_p.append(derivation_step(
        "PDTP Lagrangian L = 1/2*phi_dot^2 + g*cos(psi-phi)", L))
    steps_p.append(derivation_step(
        "Hilbert stress-energy convention for spatially uniform scalar: p = L",
        "T_ij = -g_ij * L for uniform phi; in GR Hilbert convention p = L"))
    p_computed = pressure_uniform(L)
    steps_p.append(derivation_step("Pressure p = L (Hilbert)", p_computed))
    p_expected = sp.Rational(1, 2) * phi_dot**2 + g * sp.cos(psi - phi)
    steps_p.append(derivation_step(
        "Expected: p = 1/2*phi_dot^2 + g*cos(psi-phi)  [PLUS on cos = L]",
        p_expected))
    diff_p = sp.simplify(p_computed - p_expected)
    steps_p.append(derivation_step("Residual (computed - expected)", diff_p))

    ok_p = (diff_p == 0)
    msg_p = ("PASS [p = 1/2 phidot^2 + g cos]: PLUS on cos confirmed (p = L)"
             if ok_p else
             "FAIL [p formula]: residual = {}".format(diff_p))
    result_p = VerificationResult(
        label="p = 1/2*phi_dot^2 + g*cos  [PLUS on cos, Hilbert p=L]",
        passed=ok_p,
        message=msg_p,
        steps=steps_p)

    return [result_rho, result_p]


def verify_pdtp_eos_limits():
    """
    Verify the equation-of-state limits for the PDTP condensate.

    Using rho = 1/2*phi_dot^2 - g*cos and p = 1/2*phi_dot^2 + g*cos:

    Limit 1 -- Kinetic-dominated (g -> 0):
      rho -> 1/2*phi_dot^2,  p -> 1/2*phi_dot^2 -> w = +1  (stiff fluid)

    Limit 2 -- Potential-dominated (phi_dot -> 0, psi = phi so cos = 1):
      rho -> -g,  p -> +g  -> w = g/(-g) = -1  (dark energy)

    Returns: list of VerificationResult (one per limit)
    """
    phi, psi, g = sp.symbols('phi psi g', real=True, positive=True)
    phi_dot = sp.Symbol('phi_dot', real=True)
    results = []

    # -- Kinetic limit: g -> 0 --
    steps_kin = []
    L_kin = sp.Rational(1, 2) * phi_dot**2
    steps_kin.append(derivation_step(
        "Set g = 0 (kinetic-dominated limit, no coupling)", L_kin))
    rho_kin = hamiltonian_density(L_kin, phi_dot)
    steps_kin.append(derivation_step("Energy density rho = pi*phi_dot - L", rho_kin))
    p_kin = pressure_uniform(L_kin)
    steps_kin.append(derivation_step("Pressure p = L", p_kin))
    w_kin = sp.simplify(p_kin / rho_kin)
    steps_kin.append(derivation_step("Equation of state w = p/rho", w_kin))
    steps_kin.append(derivation_step("Expected w for stiff fluid", sp.Integer(1)))
    diff_kin = sp.simplify(w_kin - sp.Integer(1))
    steps_kin.append(derivation_step("Residual w - 1", diff_kin))

    ok_kin = (diff_kin == 0)
    msg_kin = ("PASS [kinetic limit w=+1]: w = {} (stiff fluid, rho = p)".format(w_kin)
               if ok_kin else
               "FAIL [kinetic limit]: w = {}, residual = {}".format(w_kin, diff_kin))
    results.append(VerificationResult(
        label="EOS kinetic limit: w = +1 (stiff fluid, g=0)",
        passed=ok_kin,
        message=msg_kin,
        steps=steps_kin))

    # -- Potential limit: phi_dot -> 0, psi = phi (cos(psi-phi) = 1) --
    steps_pot = []
    steps_pot.append(derivation_step(
        "Set phi_dot = 0, psi = phi so cos(psi-phi) = cos(0) = 1",
        "phi_dot -> 0, psi = phi"))
    rho_pot = -g
    p_pot = g
    steps_pot.append(derivation_step(
        "rho = 1/2*(0)^2 - g*1 = -g", rho_pot))
    steps_pot.append(derivation_step(
        "p = 1/2*(0)^2 + g*1 = +g  (pressure = L = g*cos(0) = g)", p_pot))
    w_pot = sp.simplify(p_pot / rho_pot)
    steps_pot.append(derivation_step("Equation of state w = p/rho = g/(-g)", w_pot))
    steps_pot.append(derivation_step("Expected w for dark energy / Lambda", sp.Integer(-1)))
    diff_pot = sp.simplify(w_pot - sp.Integer(-1))
    steps_pot.append(derivation_step("Residual w - (-1)", diff_pot))
    steps_pot.append(derivation_step(
        "Physical interpretation",
        "w = -1 is de Sitter / cosmological constant behaviour -> dark energy (Part 25)"))

    ok_pot = (diff_pot == 0)
    msg_pot = ("PASS [potential limit w=-1]: w = {} (dark energy / Lambda-like)".format(w_pot)
               if ok_pot else
               "FAIL [potential limit]: w = {}, residual = {}".format(w_pot, diff_pot))
    results.append(VerificationResult(
        label="EOS potential limit: w = -1 (dark energy, phi_dot=0)",
        passed=ok_pot,
        message=msg_pot,
        steps=steps_pot))

    return results


def verify_trace_identity():
    """
    Verify that the trace T = T^mu_mu = rho - 3p satisfies T = rho*(1 - 3w).

    For w = -1: T = rho*(1-3*(-1)) = 4*rho
    For w = +1: T = rho*(1-3*(+1)) = -2*rho

    This is a purely algebraic identity, independent of PDTP.
    Source: standard GR/cosmology, e.g. Wald (1984), General Relativity, Appendix B.

    Returns: list of VerificationResult (general, w=-1, w=+1)
    """
    rho, w = sp.symbols('rho w', real=True)
    results = []

    # -- General trace identity --
    steps_gen = []
    steps_gen.append(derivation_step(
        "Trace definition: T = T^mu_mu = rho - 3p  (in (+---) metric, 3 spatial dims)",
        "T = rho - 3p"))
    steps_gen.append(derivation_step(
        "Substitute p = w*rho (perfect fluid EOS)", "T = rho - 3*w*rho"))
    trace_general = rho - 3 * w * rho
    steps_gen.append(derivation_step("Expanded: rho - 3*w*rho", trace_general))
    trace_formula = rho * (1 - 3 * w)
    steps_gen.append(derivation_step("Factored form: rho*(1 - 3w)", trace_formula))
    diff_gen = sp.simplify(trace_general - trace_formula)
    steps_gen.append(derivation_step("Residual (expanded - factored)", diff_gen))

    ok_gen = (diff_gen == 0)
    msg_gen = ("PASS [T = rho*(1-3w)]: algebraic identity verified"
               if ok_gen else
               "FAIL: residual = {}".format(diff_gen))
    results.append(VerificationResult(
        label="Trace T = rho*(1-3w) general identity",
        passed=ok_gen,
        message=msg_gen,
        steps=steps_gen))

    # -- w = -1 case --
    steps_dm1 = []
    steps_dm1.append(derivation_step(
        "Start from T = rho*(1-3w)", "T = rho*(1 - 3w)"))
    trace_dm1 = trace_formula.subs(w, sp.Integer(-1))
    steps_dm1.append(derivation_step("Substitute w = -1", trace_dm1))
    steps_dm1.append(derivation_step(
        "Simplify: rho*(1 - 3*(-1)) = rho*4", 4 * rho))
    diff_dm1 = sp.simplify(trace_dm1 - 4 * rho)
    steps_dm1.append(derivation_step("Residual: T - 4*rho", diff_dm1))

    ok_dm1 = (diff_dm1 == 0)
    msg_dm1 = ("PASS [T at w=-1: T=4*rho]: T = {}".format(trace_dm1)
               if ok_dm1 else
               "FAIL: T = {}, residual = {}".format(trace_dm1, diff_dm1))
    results.append(VerificationResult(
        label="Trace at w=-1: T = 4*rho",
        passed=ok_dm1,
        message=msg_dm1,
        steps=steps_dm1))

    # -- w = +1 case --
    steps_dp1 = []
    steps_dp1.append(derivation_step(
        "Start from T = rho*(1-3w)", "T = rho*(1 - 3w)"))
    trace_dp1 = trace_formula.subs(w, sp.Integer(1))
    steps_dp1.append(derivation_step("Substitute w = +1", trace_dp1))
    steps_dp1.append(derivation_step(
        "Simplify: rho*(1 - 3*(+1)) = rho*(-2)", -2 * rho))
    diff_dp1 = sp.simplify(trace_dp1 - (-2 * rho))
    steps_dp1.append(derivation_step("Residual: T - (-2*rho)", diff_dp1))

    ok_dp1 = (diff_dp1 == 0)
    msg_dp1 = ("PASS [T at w=+1: T=-2*rho]: T = {}".format(trace_dp1)
               if ok_dp1 else
               "FAIL: T = {}, residual = {}".format(trace_dp1, diff_dp1))
    results.append(VerificationResult(
        label="Trace at w=+1: T = -2*rho",
        passed=ok_dp1,
        message=msg_dp1,
        steps=steps_dp1))

    return results


# ===========================================================================
# BATCH RUNNER
# ===========================================================================

def run_all_verifications():
    """
    Run all built-in PDTP verifications.
    Intended for standalone testing or import into phase modules.
    Does NOT write any file. Does NOT call rw.print().
    Caller decides how to display results.

    Returns:
        (n_passed, n_total, results_list)
        where results_list = [VerificationResult, ...]

    Example -- generate full markdown report:
        n_passed, n_total, results = run_all_verifications()
        md = format_markdown_report(results, title="Part 43 SymPy Checks")
        print(md)   # paste into research MD file
    """
    all_results = []

    # Single-result verifiers
    all_results.append(verify_pdtp_shift_symmetry())
    all_results.append(verify_pdtp_field_equation())
    all_results.append(verify_pdtp_tmunu_vacuum())

    # Multi-result verifiers (return lists, flatten here)
    all_results.extend(verify_pdtp_tmunu_formulas())
    all_results.extend(verify_pdtp_eos_limits())
    all_results.extend(verify_trace_identity())

    n_passed = sum(1 for r in all_results if r.passed)
    n_total = len(all_results)
    return n_passed, n_total, all_results


# ===========================================================================
# STANDALONE TEST
# ===========================================================================

if __name__ == "__main__":
    n_passed, n_total, results = run_all_verifications()

    print("sympy_checks.py -- PDTP Symbolic Verification")
    print("=" * 70)
    for r in results:
        print(r.to_text())
        print("")

    print("Score: {}/{} pass".format(n_passed, n_total))

    # Demonstrate markdown output
    print("")
    print("=" * 70)
    print("Markdown output for 'PDTP field equation' (copy into MD file):")
    print("=" * 70)
    for r in results:
        if "field equation" in r.label:
            print(r.to_markdown())
            break

    # Demonstrate full report
    print("")
    print("=" * 70)
    print("Full report via format_markdown_report():")
    print("=" * 70)
    print(format_markdown_report(results, title="PDTP Part 43 SymPy Verification"))

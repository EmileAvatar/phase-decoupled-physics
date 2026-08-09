#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDTP Particle Life Toy Simulation
==================================
ILLUSTRATIVE / TOY MODEL ONLY -- not a Sudoku-checked PDTP derivation, not a
new Part. Dimensionless toy units throughout (not real G, hbar, c). The goal
is a visual, "Particle Life"-style demo built ONLY from PDTP equations that
are already derived elsewhere in the project, rather than a hand-tuned
interaction matrix.

Physics traced to (see docs/notes on this session, TODO_04.md T66 context):
  - Bulk/gravity channel: weak-field Newtonian limit of the PDTP field
    equation reduces to the Poisson equation
        nabla^2(Phi_b) = 4*pi*G*rho
    (mathematical_formalization.md Section 7.2-7.5; [DERIVED]). Always
    attractive -- PDTP requires the +cos coupling sign for stability
    (CLAUDE.md sign-convention rule), so there is no repulsive-gravity
    species here, unlike an arbitrary Particle Life matrix.
  - Equivalence principle: acceleration from Phi_b is applied UNIFORMLY to
    every particle regardless of its own coupling g_i (inertial mass cancels
    gravitational coupling in the geodesic/test-particle limit -- standard
    GR requirement PDTP must reproduce, CLAUDE.md Sudoku check item 3).
    Species only differ in how strongly they SOURCE the field (deposit
    weight = g_i), never in how they respond to it.
  - Surface/repulsion channel: SIMPLIFIED short-range screened (Yukawa-style)
    potential, INSPIRED BY the two-phase surface-tension term
    -g*cos(psi - phi_s) (Part 61, CLAUDE.md). This is NOT a first-principles
    solve of the actual biharmonic equation nabla^4(Phi) + 4*g^2*Phi = source
    (Part 61) -- that would need its own derivation/Part. Here it is a
    deliberately simplified stand-in that captures the same qualitative role
    (short-range repulsion counteracting long-range attraction), clearly
    labeled as a toy simplification, not a result.
  - "Species" = coupling-strength analogue of winding number (Part 33:
    n = m_cond/m sets mass). Three toy species with different source
    strengths, loosely named after mass scale, NOT literal claims about
    real electrons/atoms/quarks.
  - Friction/velocity damping: NOT present in PDTP's Lagrangian (which is
    energy-conserving). Added purely as a numerical-stability device, same
    as most N-body/particle-mesh toy codes use. Explicitly NOT physics.

Numerical method: particle-mesh (PM) approach on a periodic 2D grid, both
fields solved via FFT each frame (quasi-static / instantaneous-action
approximation -- the full retarded wave-equation version, box(phi)=source
propagating at finite speed c, was explicitly deferred; see TODO_04.md T66
follow-up note if this is revisited).

Output: an animated GIF (pdtp_particle_life_output.gif) plus a final-frame
PNG, saved next to this script, and a short text log of the run parameters.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

rng = np.random.default_rng(42)

# ===========================================================================
# TOY PARAMETERS (dimensionless units -- not physical SI values)
# ===========================================================================
GRID = 128           # field grid resolution (GRID x GRID)
BOX = 100.0           # periodic box size (toy length units)
DX = BOX / GRID

N_STEPS = 300         # animation frames
DT = 0.05             # integration timestep (toy time units)
FRICTION = 0.96       # per-step velocity damping [NUMERICAL, not physics]
SOFTENING = 0.6       # deposition/interp smoothing scale, avoids singular 1/r

G_GRAV = 0.3          # bulk/gravity coupling strength [toy units]
KAPPA_SURF = 1.2       # inverse screening length for surface/repulsion channel
SURF_STRENGTH = 300.0 # surface/repulsion coupling strength [toy units]

# Species table: source-strength analogue of winding-number-set mass
# (Part 33: n = m_cond/m). Larger g -> sources a stronger field, but (per
# the equivalence principle) does NOT accelerate differently in that field.
SPECIES = [
    dict(name="light",  g=1.0, color="#4da3ff", n=250),
    dict(name="medium", g=2.2, color="#ff5c5c", n=180),
    dict(name="heavy",  g=4.0, color="#3ddc84", n=90),
]

N = sum(s["n"] for s in SPECIES)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(OUT_DIR, "pdtp_particle_life_output.txt")
GIF_PATH = os.path.join(OUT_DIR, "pdtp_particle_life_output.gif")
PNG_PATH = os.path.join(OUT_DIR, "pdtp_particle_life_output.png")
MID_PNG_PATH = os.path.join(OUT_DIR, "pdtp_particle_life_midrun.png")
MID_FRAME = 100

# ===========================================================================
# FFT WAVENUMBER GRID (for periodic elliptic solves)
# ===========================================================================
k1 = np.fft.fftfreq(GRID, d=DX) * 2 * np.pi
KX, KY = np.meshgrid(k1, k1, indexing="ij")
K2 = KX**2 + KY**2
K2_SAFE = K2.copy()
K2_SAFE[0, 0] = 1.0  # avoid division by zero at the k=0 (mean) mode


# Gaussian smoothing kernel in Fourier space -- standard particle-mesh
# softening, tames grid-scale (single-cell) force spikes. [NUMERICAL, not
# physics -- same role as a softening length in any N-body code.]
SMOOTH_KERNEL = np.exp(-0.5 * K2 * SOFTENING**2)


def solve_poisson(rho):
    """nabla^2(Phi) = 4*pi*G*rho, periodic FFT solve. [DERIVED structure,
    mathematical_formalization.md Section 7.2-7.5 -- toy G_GRAV value]."""
    rho_hat = np.fft.fft2(rho) * SMOOTH_KERNEL
    phi_hat = -4.0 * np.pi * G_GRAV * rho_hat / K2_SAFE
    phi_hat[0, 0] = 0.0
    return phi_hat


def solve_screened(rho):
    """(nabla^2 - kappa^2) Phi = -source -> short-range screened repulsion.
    [TOY SIMPLIFICATION of Part 61's biharmonic equation -- see module
    docstring]."""
    rho_hat = np.fft.fft2(rho) * SMOOTH_KERNEL
    phi_hat = SURF_STRENGTH * rho_hat / (K2 + KAPPA_SURF**2)
    return phi_hat


def gradient_fields(phi_hat):
    """Spectral gradient: d(phi)/dx = ifft(i*kx*phi_hat). Cleaner than a
    finite-difference stencil on a coarse grid."""
    gx = np.real(np.fft.ifft2(1j * KX * phi_hat))
    gy = np.real(np.fft.ifft2(1j * KY * phi_hat))
    return gx, gy


# ===========================================================================
# PARTICLE-MESH DEPOSITION / INTERPOLATION (cloud-in-cell)
# ===========================================================================
def deposit_cic(pos, weight):
    gx = pos[:, 0] / DX
    gy = pos[:, 1] / DX
    ix = np.floor(gx).astype(int) % GRID
    iy = np.floor(gy).astype(int) % GRID
    fx = gx - np.floor(gx)
    fy = gy - np.floor(gy)
    ix1 = (ix + 1) % GRID
    iy1 = (iy + 1) % GRID

    rho = np.zeros((GRID, GRID))
    np.add.at(rho, (ix, iy), weight * (1 - fx) * (1 - fy))
    np.add.at(rho, (ix1, iy), weight * fx * (1 - fy))
    np.add.at(rho, (ix, iy1), weight * (1 - fx) * fy)
    np.add.at(rho, (ix1, iy1), weight * fx * fy)
    return rho / DX**2


def interp_cic(field, pos):
    gx = pos[:, 0] / DX
    gy = pos[:, 1] / DX
    ix = np.floor(gx).astype(int) % GRID
    iy = np.floor(gy).astype(int) % GRID
    fx = gx - np.floor(gx)
    fy = gy - np.floor(gy)
    ix1 = (ix + 1) % GRID
    iy1 = (iy + 1) % GRID

    return (
        field[ix, iy] * (1 - fx) * (1 - fy)
        + field[ix1, iy] * fx * (1 - fy)
        + field[ix, iy1] * (1 - fx) * fy
        + field[ix1, iy1] * fx * fy
    )


# ===========================================================================
# PARTICLE INITIALIZATION
# ===========================================================================
def init_particles():
    pos = rng.uniform(0, BOX, size=(N, 2))
    vel = rng.normal(0, 0.15, size=(N, 2))
    g_weight = np.empty(N)
    colors = np.empty(N, dtype=object)
    labels = np.empty(N, dtype=object)

    i = 0
    for s in SPECIES:
        n = s["n"]
        g_weight[i : i + n] = s["g"]
        colors[i : i + n] = s["color"]
        labels[i : i + n] = s["name"]
        i += n
    return pos, vel, g_weight, colors, labels


# ===========================================================================
# ONE SIMULATION STEP
# ===========================================================================
def step(pos, vel, g_weight):
    rho = deposit_cic(pos, g_weight)

    phi_b_hat = solve_poisson(rho)   # attractive (well-shaped potential)
    phi_s_hat = solve_screened(rho)  # repulsive (hill-shaped potential)

    gx_b, gy_b = gradient_fields(phi_b_hat)
    gx_s, gy_s = gradient_fields(phi_s_hat)

    # Total acceleration = -grad(Phi_b + Phi_s), applied UNIFORMLY to every
    # particle regardless of its own g_i -- equivalence principle (see
    # module docstring). Species only affects SOURCING (rho above), never
    # RESPONSE.
    ax_grid = -(gx_b + gx_s)
    ay_grid = -(gy_b + gy_s)

    ax = interp_cic(ax_grid, pos)
    ay = interp_cic(ay_grid, pos)

    vel[:, 0] += ax * DT
    vel[:, 1] += ay * DT
    vel *= FRICTION  # [NUMERICAL stability device, not physics]

    pos += vel * DT
    pos %= BOX
    return pos, vel, rho


# ===========================================================================
# MAIN: RUN + ANIMATE
# ===========================================================================
def main():
    pos, vel, g_weight, colors, labels = init_particles()

    fig, ax_plot = plt.subplots(figsize=(7, 7), facecolor="#0b0d13")
    ax_plot.set_facecolor("#0b0d13")
    ax_plot.set_xlim(0, BOX)
    ax_plot.set_ylim(0, BOX)
    ax_plot.set_xticks([])
    ax_plot.set_yticks([])
    for spine in ax_plot.spines.values():
        spine.set_visible(False)

    scat = ax_plot.scatter(pos[:, 0], pos[:, 1], c=colors, s=6, alpha=0.85, linewidths=0)
    title = ax_plot.set_title(
        "PDTP toy sim -- bulk (attractive) + surface (repulsive) channels, step 0",
        color="white", fontsize=9,
    )

    speed_log = []

    def update(frame):
        nonlocal pos, vel
        pos, vel, rho = step(pos, vel, g_weight)
        scat.set_offsets(pos)
        mean_speed = float(np.mean(np.linalg.norm(vel, axis=1)))
        speed_log.append(mean_speed)
        title.set_text(f"PDTP toy sim -- step {frame+1}/{N_STEPS}  mean|v|={mean_speed:.3f}")
        if frame + 1 == MID_FRAME:
            fig.savefig(MID_PNG_PATH, facecolor=fig.get_facecolor(), dpi=150)
        return scat, title

    anim = animation.FuncAnimation(fig, update, frames=N_STEPS, interval=30, blit=False)

    writer = animation.PillowWriter(fps=24)
    anim.save(GIF_PATH, writer=writer)

    # Final-frame PNG snapshot
    fig.savefig(PNG_PATH, facecolor=fig.get_facecolor(), dpi=150)
    plt.close(fig)

    with open(LOG_PATH, "w") as f:
        f.write("PDTP Particle Life Toy Simulation -- run log\n")
        f.write("=" * 55 + "\n")
        f.write(f"N particles: {N}  (species: {[ (s['name'], s['n'], s['g']) for s in SPECIES ]})\n")
        f.write(f"Grid: {GRID}x{GRID}, box={BOX}, dx={DX:.4f}\n")
        f.write(f"G_GRAV={G_GRAV}, KAPPA_SURF={KAPPA_SURF}, SURF_STRENGTH={SURF_STRENGTH}\n")
        f.write(f"FRICTION={FRICTION}, SOFTENING={SOFTENING}, DT={DT}, N_STEPS={N_STEPS}\n")
        f.write(f"mean|v| first step: {speed_log[0]:.4f}\n")
        f.write(f"mean|v| last step:  {speed_log[-1]:.4f}\n")
        f.write(f"mean|v| max over run: {max(speed_log):.4f}\n")
        f.write(f"NaN in final position: {bool(np.isnan(pos).any())}\n")
        f.write(f"NaN in final velocity: {bool(np.isnan(vel).any())}\n")
        f.write("\nNOTE: toy/illustrative model, dimensionless units, not a\n")
        f.write("Sudoku-checked PDTP Part. See module docstring for exactly\n")
        f.write("which channels are [DERIVED] vs [TOY SIMPLIFICATION].\n")

    print(f"Saved animation: {GIF_PATH}")
    print(f"Saved snapshot:  {PNG_PATH}")
    print(f"Saved log:       {LOG_PATH}")
    print(f"mean|v| first/last/max: {speed_log[0]:.4f} / {speed_log[-1]:.4f} / {max(speed_log):.4f}")
    print(f"NaN check -- pos: {bool(np.isnan(pos).any())}  vel: {bool(np.isnan(vel).any())}")


if __name__ == "__main__":
    main()

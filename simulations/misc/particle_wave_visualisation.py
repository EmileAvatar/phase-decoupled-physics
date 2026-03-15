#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDTP Particle Wave Visualisation
=================================
Visualises quarks and leptons as PDTP phase waves.

In PDTP, every particle IS a wave -- a phase distortion in the spacetime condensate.
Key relationships:
  - Compton frequency:  omega = mc^2 / hbar  (heavier = faster oscillation)
  - Compton wavelength: lambda = hbar / (mc)  (heavier = shorter wavelength)
  - Wave amplitude:     A ~ sqrt(m)           (from Koide/energy analysis)

Three plots:
  1. Individual wave panels for each particle (the "particle zoo")
  2. All particles overlaid on the same scale (comparison view)
  3. Mass-frequency spectrum (log-scale bar chart)

Sources:
  - Particle masses: PDG 2024 (Particle Data Group)
  - Compton wavelength: https://en.wikipedia.org/wiki/Compton_wavelength
  - Koide formula: https://en.wikipedia.org/wiki/Koide_formula
  - PDTP mass interpretation: efv_microphysics.md Section 3
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# ===========================================================================
# CONSTANTS
# ===========================================================================
hbar = 1.054571817e-34   # J*s
c = 2.99792458e8         # m/s
eV = 1.602176634e-19     # J per eV
MeV = 1e6 * eV           # J per MeV

# ===========================================================================
# PARTICLE DATA (PDG 2024 values)
# Source: https://en.wikipedia.org/wiki/Standard_Model
# ===========================================================================

# Each particle: (name, symbol, mass_MeV, charge, type, generation, color)
particles = [
    # Leptons (charged)
    ("Electron",  "e",    0.511,      -1, "lepton", 1, "#2196F3"),  # blue
    ("Muon",      "mu",   105.658,    -1, "lepton", 2, "#4CAF50"),  # green
    ("Tau",       "tau",  1776.86,    -1, "lepton", 3, "#F44336"),  # red

    # Quarks (up-type: charge +2/3)
    ("Up",        "u",    2.16,     2/3,  "quark",  1, "#64B5F6"),  # light blue
    ("Charm",     "c",    1270.0,   2/3,  "quark",  2, "#81C784"),  # light green
    ("Top",       "t",    172570.0, 2/3,  "quark",  3, "#E57373"),  # light red

    # Quarks (down-type: charge -1/3)
    ("Down",      "d",    4.70,     -1/3, "quark",  1, "#1565C0"),  # dark blue
    ("Strange",   "s",    93.5,     -1/3, "quark",  2, "#2E7D32"),  # dark green
    ("Bottom",    "b",    4180.0,   -1/3, "quark",  3, "#C62828"),  # dark red
]

# Separate into groups for clarity
leptons = [p for p in particles if p[4] == "lepton"]
quarks_up = [p for p in particles if p[4] == "quark" and p[3] > 0]
quarks_down = [p for p in particles if p[4] == "quark" and p[3] < 0]

# ===========================================================================
# COMPUTE WAVE PROPERTIES
# ===========================================================================
def compute_wave_props(mass_MeV):
    """Compute Compton wavelength, frequency, and relative amplitude."""
    m_kg = mass_MeV * MeV / c**2
    lambda_C = hbar / (m_kg * c)         # Compton wavelength (m)
    omega = m_kg * c**2 / hbar           # Compton frequency (rad/s)
    freq = omega / (2 * np.pi)           # frequency (Hz)
    return lambda_C, omega, freq

# Electron as reference
m_e_MeV = 0.511
lambda_e, omega_e, freq_e = compute_wave_props(m_e_MeV)

# Output directory
output_dir = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# PLOT 1: INDIVIDUAL WAVE PANELS ("Particle Zoo")
# Each particle shown at its OWN scale (3 of its own wavelengths)
# so you can see the wave shape clearly
# ===========================================================================
print("Generating Plot 1: Individual particle wave panels...")

fig = plt.figure(figsize=(18, 14))
fig.suptitle("PDTP Particle Wave Zoo\n"
             "Each particle shown at its own wavelength scale (3 Compton wavelengths each)\n"
             "Amplitude = sqrt(m/m_e) -- heavier particles have taller waves",
             fontsize=13, fontweight='bold', y=0.98)

# 3 rows x 3 columns
gs = gridspec.GridSpec(3, 3, hspace=0.5, wspace=0.3,
                       left=0.06, right=0.96, top=0.88, bottom=0.06)

# Order: electron, muon, tau (row 1), u, c, t (row 2), d, s, b (row 3)
plot_order = [
    leptons[0], leptons[1], leptons[2],      # e, mu, tau
    quarks_up[0], quarks_up[1], quarks_up[2],  # u, c, t
    quarks_down[0], quarks_down[1], quarks_down[2],  # d, s, b
]

row_labels = ["Charged Leptons", "Up-type Quarks (+2/3)", "Down-type Quarks (-1/3)"]

for idx, pdata in enumerate(plot_order):
    name, sym, mass, charge, ptype, gen, color = pdata
    lam_C, omega, freq = compute_wave_props(mass)

    row = idx // 3
    col = idx % 3

    ax = fig.add_subplot(gs[row, col])

    # X range: 3 of THIS PARTICLE's Compton wavelengths (so wave is visible)
    x_range = 3 * lam_C
    x = np.linspace(0, x_range, 2000)

    # Wave: amplitude ~ sqrt(m/m_e), wavelength = Compton wavelength
    amplitude = np.sqrt(mass / m_e_MeV)
    k = 2 * np.pi / lam_C
    psi = amplitude * np.sin(k * x)

    # Line style: dashed for quarks (confined), solid for leptons (free)
    ls = '--' if ptype == "quark" else '-'
    lw = 1.8

    ax.plot(x / lam_C, psi, color=color, linestyle=ls, linewidth=lw)
    ax.axhline(y=0, color='gray', linewidth=0.3)

    # Labels
    charge_str = "{:+.0f}".format(charge) if charge == int(charge) else "{:+.2f}".format(charge)
    ax.set_title("{} ({})\n"
                 "m = {:.3g} MeV, Q = {}e\n"
                 "lambda_C = {:.2e} m, f = {:.2e} Hz".format(
                     name, sym, mass, charge_str, lam_C, freq),
                 fontsize=9, pad=3)

    ax.set_xlabel("x / lambda_C ({})".format(sym), fontsize=8)
    if col == 0:
        ax.set_ylabel("psi (units of sqrt(m_e))", fontsize=8)

    ylim = amplitude * 1.3
    ax.set_ylim(-ylim, ylim)
    ax.tick_params(labelsize=7)

    # Amplitude annotation
    ax.annotate("A = {:.1f}".format(amplitude), xy=(0.02, 0.92),
                xycoords='axes fraction', fontsize=8, color=color,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=color, alpha=0.8))

    # Add row label on the left
    if col == 0:
        ax.annotate(row_labels[row], xy=(-0.25, 0.5),
                    xycoords='axes fraction', fontsize=10,
                    fontweight='bold', rotation=90,
                    ha='center', va='center')

plot1_path = os.path.join(output_dir, "particle_waves_zoo.png")
plt.savefig(plot1_path, dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: {}".format(plot1_path))

# ===========================================================================
# PLOT 2: ALL PARTICLES ON SAME SCALE (Comparison View)
# Use NORMALIZED x-axis (each particle's own wavelength = 1 cycle)
# so all waves are visible and comparable
# ===========================================================================
print("Generating Plot 2: Comparison view (normalized wavelength)...")

fig, axes = plt.subplots(3, 1, figsize=(16, 13))
fig.suptitle("PDTP Particle Waves: Side-by-Side Comparison\n"
             "All waves shown over 3 of their own wavelengths -- amplitude shows mass\n"
             "Heavier = taller wave (amplitude = sqrt(m/m_e))",
             fontsize=13, fontweight='bold', y=0.99)

groups = [
    ("Charged Leptons (free-propagating waves)", leptons),
    ("Up-type Quarks  Q = +2/3 (confined waves)", quarks_up),
    ("Down-type Quarks  Q = -1/3 (confined waves)", quarks_down),
]

# Normalised x: 0 to 3 wavelengths (same for all particles)
x_norm = np.linspace(0, 3, 2000)

for ax_idx, (group_label, group) in enumerate(groups):
    ax = axes[ax_idx]

    max_amp = 0
    for pdata in group:
        name, sym, mass, charge, ptype, gen, color = pdata
        lam_C, omega, freq = compute_wave_props(mass)

        # Amplitude ~ sqrt(m/m_e), normalised wavelength
        amplitude = np.sqrt(mass / m_e_MeV)
        psi = amplitude * np.sin(2 * np.pi * x_norm)

        ls = '--' if ptype == "quark" else '-'
        lw = 2.0

        label = "{} ({}): m = {:.3g} MeV, A = {:.1f}".format(
            name, sym, mass, amplitude)
        ax.plot(x_norm, psi, color=color, linestyle=ls,
                linewidth=lw, label=label, alpha=0.85)

        max_amp = max(max_amp, amplitude)

    ax.axhline(y=0, color='gray', linewidth=0.3)
    ax.set_ylabel("psi (units of sqrt(m_e))", fontsize=10)
    ax.set_title(group_label, fontsize=11, fontweight='bold', pad=5)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)

    ylim = max_amp * 1.3
    ax.set_ylim(-ylim, ylim)
    ax.tick_params(labelsize=9)
    ax.set_xlim(0, 3)

axes[-1].set_xlabel("Phase cycles (each particle at its own Compton wavelength)",
                    fontsize=11)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plot2_path = os.path.join(output_dir, "particle_waves_comparison.png")
plt.savefig(plot2_path, dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: {}".format(plot2_path))

# ===========================================================================
# PLOT 3: MASS-FREQUENCY SPECTRUM
# ===========================================================================
print("Generating Plot 3: Mass-frequency spectrum...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle("PDTP Particle Spectrum: Mass, Frequency, and Wavelength\n"
             "Every particle has a unique Compton frequency = its 'note' in the spacetime condensate",
             fontsize=13, fontweight='bold', y=0.98)

# Left panel: Mass vs Compton frequency
names = []
masses = []
freqs = []
wavelengths = []
colors = []
hatches = []

for pdata in particles:
    name, sym, mass, charge, ptype, gen, color = pdata
    lam_C, omega, freq = compute_wave_props(mass)
    names.append(f"{name}\n({sym})")
    masses.append(mass)
    freqs.append(freq)
    wavelengths.append(lam_C)
    colors.append(color)
    hatches.append('//' if ptype == "quark" else '')

# Sort by mass
sort_idx = np.argsort(masses)
names = [names[i] for i in sort_idx]
masses = [masses[i] for i in sort_idx]
freqs = [freqs[i] for i in sort_idx]
wavelengths = [wavelengths[i] for i in sort_idx]
colors = [colors[i] for i in sort_idx]
hatches = [hatches[i] for i in sort_idx]

y_pos = np.arange(len(names))

# Frequency bar chart
bars1 = ax1.barh(y_pos, freqs, color=colors, edgecolor='black', linewidth=0.5)
for bar, h in zip(bars1, hatches):
    bar.set_hatch(h)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(names, fontsize=9)
ax1.set_xscale('log')
ax1.set_xlabel("Compton Frequency (Hz)", fontsize=11)
ax1.set_title("Compton Frequency\n(heavier = faster oscillation)", fontsize=11)
ax1.tick_params(labelsize=9)

# Add mass labels on bars
for i, (mass, freq) in enumerate(zip(masses, freqs)):
    ax1.text(freq * 1.5, i, f" {mass:.3g} MeV",
             va='center', fontsize=8, color='black')

# Wavelength bar chart
bars2 = ax2.barh(y_pos, wavelengths, color=colors, edgecolor='black', linewidth=0.5)
for bar, h in zip(bars2, hatches):
    bar.set_hatch(h)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(names, fontsize=9)
ax2.set_xscale('log')
ax2.set_xlabel("Compton Wavelength (m)", fontsize=11)
ax2.set_title("Compton Wavelength\n(heavier = shorter wavelength)", fontsize=11)
ax2.tick_params(labelsize=9)
ax2.invert_xaxis()  # Shorter wavelength on the right (heavier particles)

# Add legend for quark vs lepton
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='lightgray', edgecolor='black', label='Lepton (free wave)'),
    Patch(facecolor='lightgray', edgecolor='black', hatch='//', label='Quark (confined wave)'),
]
ax2.legend(handles=legend_elements, loc='lower right', fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plot3_path = os.path.join(output_dir, "particle_spectrum.png")
plt.savefig(plot3_path, dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: {}".format(plot3_path))

# ===========================================================================
# SUMMARY TABLE
# ===========================================================================
print()
print("=" * 90)
print("PDTP PARTICLE WAVE PROPERTIES")
print("=" * 90)
print()
print("  In PDTP, each particle is a phase wave in the spacetime condensate.")
print("  Heavier particles oscillate faster (higher frequency) and have")
print("  shorter wavelength. The wave amplitude goes as sqrt(mass).")
print()
print("  {:>10} {:>6} {:>12} {:>14} {:>14} {:>14}".format(
    "Particle", "Sym", "Mass (MeV)", "Freq (Hz)", "Lambda_C (m)", "Amp/Amp_e"))
print("  {:>10} {:>6} {:>12} {:>14} {:>14} {:>14}".format(
    "--------", "---", "----------", "---------", "-----------", "--------"))

for pdata in sorted(particles, key=lambda p: p[2]):
    name, sym, mass, charge, ptype, gen, color = pdata
    lam_C, omega, freq = compute_wave_props(mass)
    amp_ratio = np.sqrt(mass / m_e_MeV)
    confined = " [confined]" if ptype == "quark" else ""
    print("  {:>10} {:>6} {:>12.3g} {:>14.4e} {:>14.4e} {:>14.2f}{}".format(
        name, sym, mass, freq, lam_C, amp_ratio, confined))

print()
print("  Key observations:")
print("    - Electron has the longest wavelength (3.86e-13 m) and amplitude = 1")
print("    - Top quark oscillates ~338,000x faster than electron")
print("    - Top quark wavelength is ~338,000x shorter than electron")
print("    - Top quark amplitude is ~581x larger than electron (sqrt ratio)")
print("    - Quarks (hatched bars) are confined -- they cannot propagate freely")
print("    - Leptons (solid bars) are free-propagating waves")
print()
print("  All plots saved to: {}".format(output_dir))
print()

# Simulation: Temporal Dispersion of First Inter-Arrival Time with Average IAT Plot

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
import sys
import os

sys.path.append("../1_star_formation")
from star_formation import star_formation_rate

# Simulation parameters
n_simulations = 1000  # number of universe simulations
mu_e = 13000  # mean time of emergence (Myr)
sigma_e = 1500  # standard deviation for emergence time (Myr)

# Different civilization counts to try
n_civ_values = [10, 100, 1000, 10000, 50000, 100000]

# Create figures
fig1, axs = plt.subplots(2, 3, figsize=(18, 12))
axs = axs.flatten()

fig2, ax_avg = plt.subplots(figsize=(12, 8))

# Track statistics for each n_civ
stats = {}
all_iat_times = []
avg_iats = []

# First pass to collect all IAT times for determining common x-axis range
for N_civ in n_civ_values:
    iat1_times = []

    for _ in range(n_simulations):
        civilization_times = np.random.normal(mu_e, sigma_e, size=N_civ)
        civilization_times = civilization_times[civilization_times > 0]

        if len(civilization_times) >= 2:
            sorted_times = np.sort(civilization_times)
            iat1 = sorted_times[1] - sorted_times[0]
            iat1_times.append(iat1)

    all_iat_times.extend(iat1_times)
    stats[N_civ] = {
        "times": iat1_times,
        "mean": np.mean(iat1_times),
        "std": np.std(iat1_times),
        "min": np.min(iat1_times),
        "max": np.max(iat1_times),
    }

    # Add to average IAT data for second plot
    avg_iats.append((N_civ, stats[N_civ]["mean"]))

# Determine common x-axis range
min_iat = min(all_iat_times)
max_iat = max(all_iat_times)
bins = np.linspace(min_iat, max_iat, 51)  # 51 points = 50 bins

# Second pass to plot with consistent scales
for i, N_civ in enumerate(n_civ_values):
    if i < len(axs):  # Make sure we don't exceed the number of subplots
        iat1_times = stats[N_civ]["times"]

        # Plot histogram on the corresponding subplot
        axs[i].hist(iat1_times, bins=bins, edgecolor="black")
        axs[i].set_xlabel("Inter-Arrival Time (IAT₁) (Myr)")
        axs[i].set_ylabel("Frequency")
        axs[i].set_title(f"IAT₁ Distribution with n_civ = {N_civ}")
        axs[i].set_xlim(min_iat, max_iat)
        axs[i].grid(True)

        # Add IAT statistics as text annotation
        stats_text = f"Mean: {stats[N_civ]['mean']:.2f} Myr\nStd Dev: {stats[N_civ]['std']:.2f} Myr"
        axs[i].text(
            0.95,
            0.95,
            stats_text,
            transform=axs[i].transAxes,
            verticalalignment="top",
            horizontalalignment="right",
            bbox=dict(facecolor="white", alpha=0.8, edgecolor="gray"),
        )

# Plot average IAT vs number of civilizations
n_civs, avg_iat_values = zip(*avg_iats)
ax_avg.plot(n_civs, avg_iat_values, "o-", linewidth=2, markersize=10)
ax_avg.set_xscale("log")
ax_avg.set_xlabel("Number of Civilizations (log scale)")
ax_avg.set_ylabel("Average IAT₁ (Myr)")
ax_avg.set_title("Average First Inter-Arrival Time vs Number of Civilizations")
ax_avg.grid(True)

# Add data points labels
for n_civ, avg in zip(n_civs, avg_iat_values):
    ax_avg.annotate(
        f"{avg:.1f}",
        (n_civ, avg),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

plt.tight_layout()
fig1.savefig("inter_arrival_times_comparison.png", dpi=300, bbox_inches="tight")
fig2.savefig("average_iat_vs_nciv.png", dpi=300, bbox_inches="tight")
plt.close("all")

# Print statistics for each n_civ
for N_civ, stat in stats.items():
    print(f"\nStatistics for n_civ = {N_civ}:")
    print(f"  Mean IAT₁: {stat['mean']:.2f} Myr")
    print(f"  Std Dev IAT₁: {stat['std']:.2f} Myr")
    print(f"  Min IAT₁: {stat['min']:.2f} Myr")
    print(f"  Max IAT₁: {stat['max']:.2f} Myr")

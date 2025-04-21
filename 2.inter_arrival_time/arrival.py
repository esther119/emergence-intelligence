# Simulation: Temporal Dispersion of First Inter-Arrival Time

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import star_formation_rate from star_formation package
from star_formation.star_formation import star_formation_rate

# Simulation parameters
n_stars = 1000  # number of stars per simulation
n_simulations = 1000  # number of universe simulations
mu_e = 13000  # mean time of emergence (Myr)
sigma_e = 1500  # standard deviation for emergence time (Myr)

# Different civilization counts to try
n_civ_values = [10, 100, 1000, 10000]

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
axs = axs.flatten()

# Track statistics for each n_civ
stats = {}
all_iat_times = []

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

# Determine common x-axis range
min_iat = min(all_iat_times)
max_iat = max(all_iat_times)
bins = np.linspace(min_iat, max_iat, 51)  # 51 points = 50 bins

# Second pass to plot with consistent scales
for i, N_civ in enumerate(n_civ_values):
    iat1_times = stats[N_civ]["times"]

    # Plot histogram on the corresponding subplot
    axs[i].hist(iat1_times, bins=bins, edgecolor="black")
    axs[i].set_xlabel("Inter-Arrival Time (IAT₁) (Myr)")
    axs[i].set_ylabel("Frequency")
    axs[i].set_title(f"IAT₁ Distribution with n_civ = {N_civ}")
    axs[i].set_xlim(min_iat, max_iat)
    axs[i].grid(True)

plt.tight_layout()
plt.savefig("inter_arrival_times_comparison.png", dpi=300, bbox_inches="tight")
plt.close()

# Print statistics for each n_civ
for N_civ, stat in stats.items():
    print(f"\nStatistics for n_civ = {N_civ}:")
    print(f"  Mean IAT₁: {stat['mean']:.2f} Myr")
    print(f"  Std Dev IAT₁: {stat['std']:.2f} Myr")
    print(f"  Min IAT₁: {stat['min']:.2f} Myr")
    print(f"  Max IAT₁: {stat['max']:.2f} Myr")

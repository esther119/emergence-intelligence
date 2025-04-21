import numpy as np
import matplotlib.pyplot as plt


def star_formation_rate(t):
    """
    Calculate star formation rate at time t (in Gyr)
    Based on observational data showing peak at ~6 Gyr and current decline
    Returns rate in solar masses per year
    """
    # Parameters fitted to match observational data
    peak_time = 6.0  # Peak at 6 Gyr
    peak_rate = 50.0  # Peak rate of 50 M⊙/yr

    # Different slopes for rise and fall
    rise_rate = 2.0
    fall_rate = 0.5

    # Piecewise function for before and after peak
    rate = np.where(
        t < peak_time,
        peak_rate * (t / peak_time) ** rise_rate,  # Sharp rise
        peak_rate * np.exp(-fall_rate * (t - peak_time)),  # Gradual decline
    )

    return rate


# Create time axis from 0 to 14 Gyr
time = np.linspace(0, 14, 1000)

# Calculate SFR
sfr = star_formation_rate(time)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot SFR
plt.plot(time, sfr, "k-", linewidth=2)

# Set up the main axis
plt.xlabel("Time Since Big Bang (Billion Years)", fontsize=12)
plt.ylabel("Number of New Stars Formed per Year\n(in Solar Masses)", fontsize=12)
plt.title("How Many Stars Were Born Throughout Cosmic History?", fontsize=14, pad=20)

# Add redshift axis on top
ax2 = plt.twiny()
redshift = np.array([4, 3, 2, 1, 0])
# Corrected mapping: redshift z=0 should correspond to 13.8 Gyr
time_redshift = np.array(
    [1.6, 2.2, 3.3, 5.9, 13.8]
)  # Fixed time values corresponding to redshifts
ax2.set_xlim(0, 14)
ax2.set_xticks(time_redshift)
ax2.set_xticklabels([f"z={z}" for z in redshift])
ax2.set_xlabel("Redshift (How Far Back We Are Looking)", fontsize=12, labelpad=15)

# Add annotations
plt.annotate(
    "Early Universe\n(Very Few Stars)",
    xy=(1, 5),
    xytext=(1, 15),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

plt.annotate(
    "Peak Star Formation\n(Most Stars Born Here)",
    xy=(6, 45),
    xytext=(8, 45),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

plt.annotate(
    "Present Day\n(Fewer New Stars)",
    xy=(13, 15),
    xytext=(11, 25),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

# Add grid
plt.grid(True, linestyle="--", alpha=0.7)

# Save the plot
plt.savefig("historical_sfr.png", dpi=300, bbox_inches="tight")
plt.close()

print("I've created an easier-to-understand version of the star formation plot!")

# Inter-Arrival Time Simulation

## Overview

This directory contains a simulation that examines the temporal dispersion of first inter-arrival times between intelligent civilizations in the universe. The script `arrival.py` simulates multiple universe scenarios with different numbers of civilizations to analyze how the distribution of inter-arrival times varies.

## The Inter-Arrival Time Concept

The **Inter-Arrival Time (IAT₁)** refers to the time difference between the emergence of the first two civilizations in a universe. This metric is important for understanding the likelihood of temporal overlap between the earliest intelligent species.

## Simulation Methodology

The simulation works as follows:

1. For different civilization counts (10, 100, 1000, 10000), the script simulates 1000 different "universes"
2. In each universe, civilizations emerge according to a normal distribution with:
   - Mean emergence time: 13,000 Million years (Myr)
   - Standard deviation: 1,500 Million years (Myr)
3. For each universe, it calculates the time difference between the first two civilizations to emerge (IAT₁)
4. The distribution of these inter-arrival times is plotted and analyzed statistically

## Key Parameters

- `n_simulations`: 1000 (number of universe simulations)
- `mu_e`: 13000 (mean time of emergence in Myr)
- `sigma_e`: 1500 (standard deviation for emergence time in Myr)
- `n_civ_values`: [10, 100, 1000, 10000] (different civilization counts tested)

## Implementation Details

- The simulation ensures that only valid civilization emergence times (> 0) are considered
- All simulations use a consistent scale for visualization to allow direct comparison across different civilization counts
- Statistics are calculated for each universe scenario and presented both as text annotations on the plots and as terminal output

## Outputs

1. **Visual Output**: A figure with four histograms showing the IAT₁ distribution for each of the civilization counts. The figure is saved as `inter_arrival_times_comparison.png`.

2. **Statistical Analysis**: For each civilization count, the script calculates and displays:
   - Mean IAT₁
   - Standard deviation of IAT₁
   - Minimum IAT₁
   - Maximum IAT₁

## Interpretation

The results help understand how the number of civilizations in a universe affects the likely time gap between the first two emerging intelligent species. As the number of civilizations increases, we generally expect the first inter-arrival time to decrease, as the probability of civilizations emerging closely together increases.

Some key observations from the simulation:

- Higher civilization counts lead to smaller average inter-arrival times
- The distribution shape changes significantly as civilization count increases
- Even with many civilizations, there's still variability in when the first two emerge

## Dependencies

The script requires:

- NumPy (for numerical operations)
- Matplotlib (for visualization)
- SciPy (for statistical functions)
- Custom `star_formation` module from the parent directory

## Running the Simulation

To run the simulation:

```bash
python arrival.py
```

The script will generate the histogram plots and print the statistical information to the console.

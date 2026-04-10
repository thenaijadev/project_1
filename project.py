"""
Simple solution for the Random Variable Generation lab (Group 4).

What this script does:
1) Uses seed = 4 (group number).
2) Generates random values for required distributions.
3) Uses n = 10, 100, 1000, 10000.
4) Saves histogram images in ./histograms.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Non-interactive backend (works in most environments).
matplotlib.use("Agg")


def save_histogram(data, title, filename):
    """Plot and save one histogram."""
    plt.figure(figsize=(7, 4.5))
    plt.hist(data, bins=30, edgecolor="black", alpha=0.8)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(filename, dpi=140)
    plt.close()


def main():
    # Step 1: Set up folder and random generator.
    out_dir = Path("histograms")
    out_dir.mkdir(exist_ok=True)
    rng = np.random.default_rng(4)  # group number = 4

    # Step 2: Define sample sizes.
    sample_sizes = [10, 100, 1000, 10000]

    # Step 3: For each n, generate each distribution and save histogram.
    for n in sample_sizes:
        # Uniform integer in [30, 50]
        u_int = rng.integers(30, 51, size=n)
        save_histogram(u_int, f"Uniform Int [30,50], n={n}", out_dir / f"uniform_int_{n}.png")

        # Uniform real in [3.0, 5.0)
        u_real = rng.uniform(3.0, 5.0, size=n)
        save_histogram(u_real, f"Uniform Real [3.0,5.0), n={n}", out_dir / f"uniform_real_{n}.png")

        # Normal with mean=0 and std=1.25
        normal = rng.normal(loc=0.0, scale=1.25, size=n)
        save_histogram(normal, f"Normal (0,1.25), n={n}", out_dir / f"normal_{n}.png")

        # Exponential with mean=8 (scale=8)
        expo = rng.exponential(scale=8.0, size=n)
        save_histogram(expo, f"Exponential mean=8, n={n}", out_dir / f"exponential_{n}.png")

        # Other distribution for Group 4: Gamma
        # (Using shape=2.0, scale=2.0 as a simple default)
        gamma = rng.gamma(shape=2.0, scale=2.0, size=n)
        save_histogram(gamma, f"Gamma (k=2, theta=2), n={n}", out_dir / f"gamma_{n}.png")

        print(f"Finished n={n}")

    print(f"All histograms saved in: {out_dir.resolve()}")


if __name__ == "__main__":
    main()

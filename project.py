from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


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

    out_dir = Path("histograms")
    out_dir.mkdir(exist_ok=True)
    rng = np.random.default_rng(4)  


    sample_sizes = [10, 100, 1000, 10000]


    gamma_shape = 2.0
    gamma_scale = 2.0

    for n in sample_sizes:
        u_int = rng.integers(30, 51, size=n)
        save_histogram(u_int, f"Uniform Int [30,50], n={n}", out_dir / f"uniform_int_{n}.png")

        u_real = rng.uniform(3.0, 5.0, size=n)
        save_histogram(u_real, f"Uniform Real [3.0,5.0), n={n}", out_dir / f"uniform_real_{n}.png")

        normal = rng.normal(loc=0.0, scale=1.25, size=n)
        save_histogram(normal, f"Normal (0,1.25), n={n}", out_dir / f"normal_{n}.png")

        expo = rng.exponential(scale=8.0, size=n)
        save_histogram(expo, f"Exponential mean=8, n={n}", out_dir / f"exponential_{n}.png")

        gamma = rng.gamma(shape=gamma_shape, scale=gamma_scale, size=n)
        save_histogram(
            gamma,
            f"Gamma (k={gamma_shape}, theta={gamma_scale}), n={n}",
            out_dir / f"gamma_{n}.png",
        )

        print(f"Finished n={n}")

    print(f"All histograms saved in: {out_dir.resolve()}")


if __name__ == "__main__":
    main()

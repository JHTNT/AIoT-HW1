from __future__ import annotations

import numpy as np


def generate_linear_data(
    a: float = 2.0,
    b: float = 0.5,
    n_points: int = 100,
    noise_std: float = 1.0,
    seed: int | None = 42,
):
    """Generate synthetic linear data: y = a*x + b + noise.

    Returns
    -------
    x : np.ndarray, shape (n_points,)
    y : np.ndarray, shape (n_points,)
    """
    rng = np.random.default_rng(seed)
    x = rng.uniform(-5, 5, size=n_points)
    noise = rng.normal(0.0, noise_std, size=n_points)
    y = a * x + b + noise
    return x, y

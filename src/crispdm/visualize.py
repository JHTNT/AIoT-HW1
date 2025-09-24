from __future__ import annotations

import io
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np


def plot_data_and_fit(
    x: np.ndarray,
    y: np.ndarray,
    a_hat: Optional[float] = None,
    b_hat: Optional[float] = None,
):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x, y, alpha=0.6, label="data")
    if a_hat is not None and b_hat is not None:
        xs = np.linspace(np.min(x), np.max(x), 200)
        ys = a_hat * xs + b_hat
        ax.plot(xs, ys, color="red", label=f"fit: y={a_hat:.3f}x+{b_hat:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    return fig

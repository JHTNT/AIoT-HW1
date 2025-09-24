from __future__ import annotations

import numpy as np


def fit_linear_regression(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """Fit y ≈ a*x + b using closed-form least squares.

    Returns (a_hat, b_hat).
    """
    x = np.asarray(x)
    y = np.asarray(y)
    X = np.column_stack([x, np.ones_like(x)])
    # theta = (X^T X)^-1 X^T y
    theta, *_ = np.linalg.lstsq(X, y, rcond=None)
    a_hat, b_hat = float(theta[0]), float(theta[1])
    return a_hat, b_hat


def predict(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return a * np.asarray(x) + b

"""CRISP-DM utilities for simple linear regression demo.

Modules:
- data: synthetic data generation
- model: fit linear regression (closed-form and sklearn-like)
- evaluate: metrics like MSE, R2
- visualize: plotting helpers for Streamlit
"""

from .data import generate_linear_data
from .evaluate import mean_squared_error, r2_score
from .model import fit_linear_regression, predict
from .visualize import plot_data_and_fit

__all__ = [
    "generate_linear_data",
    "fit_linear_regression",
    "predict",
    "mean_squared_error",
    "r2_score",
    "plot_data_and_fit",
]

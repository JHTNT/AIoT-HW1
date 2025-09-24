from __future__ import annotations

import os
import sys

import numpy as np
import streamlit as st

# Ensure we can import from ./src
_ROOT = os.path.dirname(__file__)
_SRC = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
	sys.path.insert(0, _SRC)

from crispdm import (
    fit_linear_regression,
    generate_linear_data,
    mean_squared_error,
    plot_data_and_fit,
    predict,
    r2_score,
)

st.set_page_config(page_title="CRISP-DM: Simple Linear Regression", layout="centered")
st.title("CRISP-DM: 簡單線性回歸 Demo")
st.caption("可調整 a、雜訊與資料筆數；並依 CRISP-DM 步驟展示")


with st.sidebar:
	st.header("參數設定")
	# 預設狀態初始化（供按鈕隨機化與控制項同步）
	st.session_state.setdefault("a_true", 2.0)
	st.session_state.setdefault("n_points", 200)
	st.session_state.setdefault("noise_std", 1.0)
	st.session_state.setdefault("seed", 42)

	# 隨機設定參數按鈕
	if st.button("隨機設定參數"):
		_rng = np.random.default_rng()
		st.session_state["a_true"] = float(_rng.uniform(-10.0, 10.0))
		st.session_state["n_points"] = int(_rng.integers(1, 201) * 10)  # 10~2000, step 10
		st.session_state["noise_std"] = float(_rng.uniform(0.0, 5.0))
		st.session_state["seed"] = int(_rng.integers(0, 10000))

	# 僅提供 a 的控制項；b 固定為常數（例如 0.5）
	a_true = st.slider(
		"真實斜率 a",
		min_value=-10.0,
		max_value=10.0,
		value=float(st.session_state.get("a_true", 2.0)),
		step=0.1,
		key="a_true",
	)
	b_true = 0.5
	n_points = st.slider(
		"資料筆數",
		min_value=10,
		max_value=2000,
		value=int(st.session_state.get("n_points", 200)),
		step=10,
		key="n_points",
	)
	noise_std = st.slider(
		"雜訊標準差",
		min_value=0.0,
		max_value=5.0,
		value=float(st.session_state.get("noise_std", 1.0)),
		step=0.1,
		key="noise_std",
	)
	seed = st.number_input(
		"隨機種子",
		value=int(st.session_state.get("seed", 42)),
		key="seed",
	)


st.subheader("1. Business Understanding / 業務理解")
st.write(
	"本示例目標：在可控制資料生成條件下，利用線性回歸學得 y≈a·x+b 的參數，以理解模型如何受資料與雜訊影響。"
)

st.subheader("2. Data Understanding / 資料理解")
x, y = generate_linear_data(a=a_true, b=b_true, n_points=int(n_points), noise_std=float(noise_std), seed=int(seed))
st.write(f"生成 {len(x)} 筆資料，x 範圍：[{np.min(x):.2f}, {np.max(x):.2f}]，雜訊標準差：{noise_std}")
fig0 = plot_data_and_fit(x, y)
st.pyplot(fig0)

st.subheader("3. Data Preparation / 資料準備")
st.write("本例資料已為數值型，僅需確認形狀、是否含缺失等；此處略。")

st.subheader("4. Modeling / 建模")
a_hat, b_hat = fit_linear_regression(x, y)
st.write(f"估計參數：a_hat={a_hat:.4f}, b_hat={b_hat:.4f}")
fig1 = plot_data_and_fit(x, y, a_hat, b_hat)
st.pyplot(fig1)

st.subheader("5. Evaluation / 評估")
y_pred = predict(x, a_hat, b_hat)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
st.metric("MSE", f"{mse:.4f}")
st.metric("R^2", f"{r2:.4f}")

# CRISP-DM 線性回歸 Demo（Streamlit）

此專案示範以 CRISP-DM 流程解決簡單線性回歸問題，並提供可互動的 Streamlit 介面：你可調整資料生成與訓練參數，即時觀察擬合直線與評估指標。內容包含一頁式的 CRISP-DM 對照、數學原理、模組 API、部署與常見問題；自動化產生與修訂過程請見 `log.md`。

Demo link: <https://aiot-hw1-cnnkxquzng72buddknqshp.streamlit.app/>

## 亮點

- 一頁式 CRISP-DM 對照（Business → Data → Preparation → Modeling → Evaluation → Deployment）
- 即時互動：可調 a、b、雜訊標準差、資料點數、隨機種子
- 指標：MSE 與 R²；圖形：散點與擬合直線
- 快速部署：本機、Docker、Streamlit Community Cloud

## 專案結構

```
app.py                 # Streamlit 入口
src/
  crispdm/
    data.py            # 合成資料生成（y = a·x + b + N(0, σ)）
    model.py           # 線性回歸閉式解與預測
    evaluate.py        # 指標：MSE、R^2
    visualize.py       # 視覺化（散點與擬合線）
    __init__.py
requirements.txt
Dockerfile
log.md                 # 自動化產生與調整的完整紀錄
```

## CRISP-DM 一頁式對照

### 1. Business Understanding（業務理解）

- 目標：在可控條件下重建 y ≈ a·x + b 之參數，理解雜訊與資料量對擬合的影響。
- 成功衡量：R² 越高、MSE 越低越好；視覺上擬合線貼近散點分佈。

### 2. Data Understanding（資料理解）

- `generate_linear_data(a, b, n_points, noise_std, seed)` 合成數據，x ~ U[-5, 5]，y = a·x + b + ε，其中 ε ~ N(0, noise_std)。
- UI 顯示資料筆數、x 範圍；以散點圖檢視資料分佈與雜訊程度。

### 3. Data Preparation（資料準備）

- 本例為乾淨的數值資料；實務上可加入缺值處理、常態化、異常值偵測等。

### 4. Modeling（建模）

- `fit_linear_regression(x, y)` 使用最小二乘閉式解（見下方數學原理），並提供 `predict(x, a, b)` 產生預測。

### 5. Evaluation（評估）

- 指標：`mean_squared_error(y_true, y_pred)`、`r2_score(y_true, y_pred)`；R² 在變異趨近 0 時以 1.0 處理邊界情況。

### 6. Deployment（部署）

- 本機、Docker 或 Streamlit Community Cloud；見下方指引。

## 數學原理（最小二乘閉式解）

對單變量線性回歸 y ≈ a·x + b，令設計矩陣 X = [x, 1]，參數 θ = [a, b]^T。最小化平方誤差：

min_θ ||Xθ − y||²，其閉式解為 θ̂ = (XᵀX)⁻¹ Xᵀ y。

在程式中以 `np.linalg.lstsq(X, y, rcond=None)` 求得 θ̂，再拆解為 a_hat 與 b_hat。

## 模組 API（src/crispdm）

- data.generate_linear_data(a: float, b: float, n_points: int, noise_std: float, seed: int) -> tuple[np.ndarray, np.ndarray]
- model.fit_linear_regression(x: np.ndarray, y: np.ndarray) -> tuple[float, float]
- model.predict(x: np.ndarray, a: float, b: float) -> np.ndarray
- evaluate.mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float
- evaluate.r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float
- visualize.plot_data_and_fit(x: np.ndarray, y: np.ndarray, a_hat: float | None = None, b_hat: float | None = None) -> matplotlib.figure.Figure

## 參數建議與範圍

- a（斜率）：[-10, 10]；數值過大時，若資料點少或雜訊大，R² 可能下降。
- b（截距）：[-10, 10]；平移直線位置。
- noise_std（雜訊標準差）：[0, 5]；越大代表觀測波動越大，擬合難度提高。
- n_points（資料點數）：[10, 2000]；一般資料點越多，擬合越穩定（R² 上升）。
- seed（隨機種子）：固定可重現；多試幾個種子可觀察穩定度。

## 本機快速開始（Windows Bash 相容）

```bash
python -m venv .venv
source .venv/Scripts/activate  # 若使用 Git Bash
# PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

啟動後造訪 <http://localhost:8501>。

## Docker 部署

```bash
docker build -t crispdm-lr .
docker run --rm -p 8501:8501 crispdm-lr
```

瀏覽器造訪 <http://localhost:8501>。

## 部署到 Streamlit Community Cloud（取得公開連結）

1. 將專案推到 GitHub（至少包含 `app.py` 與 `requirements.txt`）。
2. 前往 <https://share.streamlit.io/> 或 <https://streamlit.io/cloud> 登入。
3. New app → 選擇 Repo 與分支 → Main file path 輸入 `app.py`。
4. Deploy 後頁面即顯示可分享的公開 URL。

## 常見問題（FAQ）

- Windows 如何啟用虛擬環境？
  - 在 Bash 用 `source .venv/Scripts/activate`；PowerShell 則為 `.venv\Scripts\Activate.ps1`。
- 為何 R² 有時很低？
  - 可能因雜訊偏大或資料點偏少；可嘗試增大 `n_points` 或降低 `noise_std`。
- 圖沒有顯示？
  - Docker 或遠端環境需等依賴安裝完成；本專案使用 `matplotlib` Agg 後端，無需系統 GUI。

## 產生過程紀錄

請見根目錄的 `log.md`，內含從初始化、程式撰寫、驗證到部署說明的完整步驟與修訂紀錄。

## 後續延伸

- 殘差圖、信賴區間與參數不確定性
- 訓練/測試切分、交叉驗證與多種隨機種子重複實驗
- Flask 版本與 API 化（上傳資料、回傳模型與指標）
- 匯出結果（CSV/PNG）與參數設定（JSON）


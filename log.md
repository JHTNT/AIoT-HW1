## 1. 建立與驗證開發環境

### 1.1 建立虛擬環境（Windows Bash）

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 1.2 安裝相依套件

```bash
pip install -r requirements.txt
```

### 1.3 匯入關鍵套件快速驗證

```bash
python - << 'PY'
import importlib
for m in ['numpy','streamlit']:
   mod = importlib.import_module(m)
   print(m, 'OK', getattr(mod,'__version__',''))
PY
```

- 預期輸出（實際）：
  - numpy OK 2.3.3
  - streamlit OK 1.50.0

## 2. 建立專案骨架與 CRISP-DM 模組

### 2.1 建立目錄與模組

- `src/crispdm/__init__.py`（統一導出 API）
- `src/crispdm/data.py`（`generate_linear_data` 合成 y=a·x+b+噪聲）
- `src/crispdm/model.py`（`fit_linear_regression` 最小二乘閉式解；`predict`）
- `src/crispdm/evaluate.py`（`mean_squared_error`、`r2_score`）
- `src/crispdm/visualize.py`（`plot_data_and_fit` 畫散點與擬合線）
- `src/utils.py`（預留工具）

### 2.2 模組功能煙霧測試

```bash
python - << 'PY'
import os, sys
sys.path.insert(0, os.path.join(os.getcwd(),'src'))
from crispdm import generate_linear_data, fit_linear_regression
x,y = generate_linear_data(a=3.0,b=1.0,n_points=50,noise_std=0.5,seed=7)
a,b = fit_linear_regression(x,y)
print('fit', round(a,3), round(b,3))
PY
```

- 預期：`fit` 係數接近真值（實際：`fit 2.979 1.013`）

## 3. 實作 Streamlit 應用（app.py）

### 3.1 Sidebar 可調參數

- a、b、n_points、noise_std、seed

### 3.2 依 CRISP-DM 區塊顯示

- Business Understanding → 目標說明
- Data Understanding → 散點圖與資料訊息
- Data Preparation → 簡述處理重點
- Modeling → 最小二乘擬合 a_hat、b_hat
- Evaluation → MSE、R² 指標
- Deployment → 部署說明

### 3.3 啟動煙霧測試（headless）

```bash
streamlit run app.py --server.headless true --server.port 8888 --server.address 127.0.0.1
```

- 預期：終端顯示可存取 URL（實際：`http://127.0.0.1:8888`）

## 4. 文件與部署設定

- requirements.txt：streamlit、numpy、pandas、matplotlib
- Dockerfile：基於 `python:3.11-slim`，安裝需求並以 `streamlit run app.py` 啟動
- README.md：增補特色、CRISP-DM 對照、快速開始、Docker、Streamlit Cloud、Troubleshooting、延伸方向
- .gitignore：忽略虛擬環境與編輯器檔案
- pyproject.toml：基本專案描述（非必要）

## 5. 再次執行驗證

### 5.1 Streamlit 第二次煙霧測試

```bash
streamlit run app.py --server.headless true --server.port 8890 --server.address 127.0.0.1
```

- 預期：終端顯示可存取 URL（實際：`http://127.0.0.1:8890`）

## 6. 版本控制與部署（GitHub → Streamlit Cloud）

### 6.1 設定遠端與推送（已設定 remote）

```bash
git remote add origin https://github.com/JHTNT/AIoT-HW1.git
git add .
git commit -m "init: CRISP-DM Streamlit app with docs and deployment"
git push -u origin main
```

### 6.2 Streamlit Community Cloud 部署

- 前往 <https://share.streamlit.io/>（或 <https://streamlit.io/cloud>）登入
- New app → 選擇 `JHTNT/AIoT-HW1` 與分支 `main`
- Main file path 輸入 `app.py`
- 按 Deploy，完成後取得公開連結

## 7. 使用者在本次對話中的手動調整與再驗證

- 使用者手動編輯檔案：
  - app.py
  - src/crispdm/__init__.py
  - src/crispdm/model.py
  - src/crispdm/data.py
  - src/crispdm/evaluate.py
  - src/crispdm/visualize.py
  - src/utils.py

- 再驗證：
  - 模組擬合結果合理（係數接近真值）
  - Streamlit headless 啟動成功並顯示 URL

## 8. 後續可強化項目（非必須）

- 增加殘差圖、信賴區間與參數不確定性視覺化
- 訓練/測試切分與多次重複實驗
- 提供資料下載與參數設定匯出
- 加入 Flask 版本與 CI（GitHub Actions）進行基本匯入/啟動檢查

---


以上步驟可與 `README.md` 內容互相對照；若只需要快速部署到 Streamlit Cloud，請直接參考第 6 節。

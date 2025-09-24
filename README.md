# CRISP-DM 線性回歸 Demo

此專案示範以 CRISP-DM 流程解決簡單線性回歸問題，並提供 Streamlit 介面讓使用者可調整參數：

- 斜率 a（ax + b）
- 截距 b
- 雜訊標準差
- 資料點數

## 專案結構

```
app.py                 # Streamlit 入口
src/
  crispdm/
    data.py            # 資料生成
    model.py           # 線性回歸訓練與預測
    evaluate.py        # MSE、R^2 等指標
    visualize.py       # 繪圖
    __init__.py
requirements.txt
Dockerfile
```

## 快速開始（本機）

```bash
python -m venv .venv
source .venv/bin/activate  # Windows Bash: source .venv/Scripts/activate
pip install -r requirements.txt
streamlit run app.py
```

## Docker 部署

```bash
docker build -t crispdm-lr .
docker run --rm -p 8501:8501 crispdm-lr
```

開啟瀏覽器訪問 <http://localhost:8501>

## 部署到 Streamlit Community Cloud（取得可分享連結）

1. 將此專案推送到 GitHub（需包含 `app.py`、`requirements.txt`）。
2. 前往 <https://share.streamlit.io/> 登入（或 <https://streamlit.io/cloud>）。
3. 點選 New app，選擇你的 GitHub repo 與分支，Main file path 填入 `app.py`。
4. 點 Deploy，完成後頁面上會顯示你的公開連結，複製即可分享。

## CRISP-DM 步驟紀錄

- docs/CRISPDM-01-business_understanding.md
- docs/CRISPDM-02-data_understanding.md
- docs/CRISPDM-03-data_preparation.md
- docs/CRISPDM-04-modeling.md
- docs/CRISPDM-05-evaluation.md
- docs/CRISPDM-06-deployment.md

每個檔案對應本專案中該階段的活動與關鍵決策紀錄。


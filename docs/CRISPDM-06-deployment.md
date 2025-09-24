# 6. Deployment / 部署

- 介面：Streamlit。
- 本機：`streamlit run app.py`。
- 容器：使用 Dockerfile，對外 8501 埠。

## 部署到 Streamlit Community Cloud

1. 建立 Git 儲存庫並推送到 GitHub（專案根目錄需要包含 `app.py` 與 `requirements.txt`）。
2. 前往 <https://share.streamlit.io/> 登入（或 <https://streamlit.io/cloud>）。
3. 選擇「New app」，挑選你的 GitHub repo、分支，`Main file path` 輸入 `app.py`。
4. 點 Deploy。首次部署會安裝相依套件並啟動應用。
5. 完成後會產生一個公開連結，可直接分享存取。

可選：若需要秘密金鑰等設定，於雲端後台設定 Secrets（本專案不需要）。

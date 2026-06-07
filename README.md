# Chrome Glic 通用版更新與 AI 人機協作專案 (Chrome Glic Patcher)

本專案是針對 Google Chrome 的最新 AI 助手 **Glic (Gemini Live in Chrome)** 所開發的地區判定修正工具。

專案網頁展示與說明：👉 [https://falo-taiwan.github.io/gemini_chrome/](https://falo-taiwan.github.io/gemini_chrome/)

---

## 📂 檔案與目錄結構

* **[index.html](index.html)**：首頁說明網頁，包含最新通用版說明、原理解析與 AI Agent 協作交接指南。
* **[patch_glic.py](patch_glic.py)**：通用 Python 核心修正腳本，會自動判定 OS 平台並修正 Chrome 系統設定檔。
* **[patch_glic.command](patch_glic.command)**：macOS 專用雙擊啟動檔。
* **[patch_glic.bat](patch_glic.bat)**：Windows 專用雙擊啟動檔。
* **[history/](history/)**：歷史版本歸檔目錄。
  * **[20260422/](history/20260422/)**：專案啟動時的首版（macOS 專用）排查研究說明檔案。

---

## 💡 更新緣由與文件目的

原本的專案為特定的 macOS 設定排查；本次更新改用通用概念設計，解耦路徑依賴。
當使用者環境無法執行腳本時（例如無 Python 環境、權限不足），腳本可輸出診斷報告並將意圖委託給本機環境的 **AI Agent** 協助完成檔案修正，體現人機協同設計。

# Chrome Glic 通用版更新與 AI 人機協作說明 (Chrome Glic Patcher Update Folder)

這個資料夾包含了 Chrome Glic 顯示判定修正的**跨平台通用版腳本**與**AI 協同處理說明文件**。

---

## 📂 檔案清單

1. **[index.html](index.html)**：部署於 GitHub Pages 的線上說明網頁，包含原理解析與使用說明。
2. **[patch_glic.py](patch_glic.py)**：通用 Python 核心修正腳本，會自動探測作業系統與路徑，更新 Chrome 設定檔。
3. **[patch_glic.command](patch_glic.command)**：Mac 專用雙擊啟動檔。
4. **[patch_glic.bat](patch_glic.bat)**：Windows 專用雙擊啟動檔。

---

## 💡 更新緣由與文件目的

原本的專案為特定的 macOS 設定排查；本次更新改用通用概念設計，解耦路徑依賴。
當使用者環境無法執行腳本時（例如無 Python 環境、權限不足），腳本可輸出診斷報告並將意圖委託給本機環境的 **AI Agent** 協助完成檔案修正，體現人機協同設計。

詳細原理解釋與使用步驟請參考 [update/index.html](index.html) 或線上網址：`https://falo-taiwan.github.io/gemini_chrome/update/`。

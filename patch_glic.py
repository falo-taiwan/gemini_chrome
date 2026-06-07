# ==============================================================================
#  Copyright (c) Falo x Force Cheng 2026/6/6. All rights reserved.
#  
#  Description: 
#    Chrome 內建 Gemini 智慧側邊欄 (Gemini in Chrome) 地區判定修正工具核心。
#    此腳本自動偵測系統平台 (macOS/Windows) 並修改 Chrome 的 Local State 設定檔。
#    當執行失敗時，會自動在同目錄下生成 gemini_chrome_diagnostics.json 供 AI Agent 解析。
# ==============================================================================

import json
import os
import sys
import subprocess
import time

def write_diagnostics(error_type, path):
    diag = {
        "status": "failed",
        "error_type": error_type,
        "os_detected": sys.platform,
        "expected_local_state_path": path,
        "required_patch": {
            "variations_country": "us",
            "variations_permanent_consistency_country": ["current_version", "us"],
            "glic.is_glic_eligible": True
        }
    }
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
    diag_path = os.path.join(script_dir, 'gemini_chrome_diagnostics.json')
    try:
        with open(diag_path, 'w', encoding='utf-8') as f:
            json.dump(diag, f, ensure_ascii=False, indent=2)
        print(f"已自動生成診斷檔案：{diag_path}，您可以將此檔案上傳給您的 AI Agent 協助修復。")
    except Exception as e:
        print(f"寫入診斷檔案失敗：{e}")

def close_chrome():
    print("正在關閉 Google Chrome...")
    if sys.platform == 'darwin':
        subprocess.run(['osascript', '-e', 'quit app "Google Chrome"'], capture_output=True)
    elif sys.platform == 'win32':
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], capture_output=True)
    time.sleep(2)

def open_chrome():
    print("正在重啟 Google Chrome...")
    if sys.platform == 'darwin':
        subprocess.run(['open', '-a', 'Google Chrome'])
    elif sys.platform == 'win32':
        subprocess.run('start chrome', shell=True)

def apply_patch():
    home = os.path.expanduser('~')
    if sys.platform == 'darwin':
        path = os.path.join(home, 'Library/Application Support/Google/Chrome/Local State')
    elif sys.platform == 'win32':
        path = os.path.join(home, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Local State')
    else:
        print(f"不支援的作業系統：{sys.platform}")
        write_diagnostics("UNSUPPORTED_OS", "")
        return False

    if not os.path.exists(path):
        print(f"找不到 Chrome 設定檔：{path}")
        write_diagnostics("LOCAL_STATE_NOT_FOUND", path)
        return False

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print("原始設定：")
        print("  variations_country:", data.get('variations_country'))
        print("  variations_permanent_consistency_country:", data.get('variations_permanent_consistency_country'))

        # 修改地區設定為美國 (US)
        data['variations_country'] = 'us'

        v_p_c_c = data.get('variations_permanent_consistency_country')
        if isinstance(v_p_c_c, list):
            data['variations_permanent_consistency_country'] = [x if x != 'tw' else 'us' for x in v_p_c_c]
            if data['variations_permanent_consistency_country'] and data['variations_permanent_consistency_country'][-1] != 'us':
                data['variations_permanent_consistency_country'][-1] = 'us'
        else:
            data['variations_permanent_consistency_country'] = 'us'

        # 強制開啟 glic (Chrome Gemini 側邊欄內部代號) 相關欄位
        if 'glic' not in data:
            data['glic'] = {}
        data['glic']['is_glic_eligible'] = True
        data['glic']['launcher_enabled'] = True

        # 啟用所有 profile 的 glic 權限
        profile = data.get('profile', {})
        info_cache = profile.get('info_cache', {})
        for name, p_data in info_cache.items():
            p_data['is_glic_eligible'] = True

        print("\n修改後設定：")
        print("  variations_country:", data.get('variations_country'))
        print("  variations_permanent_consistency_country:", data.get('variations_permanent_consistency_country'))

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print("\n地區修正成功！")
        return True
    except Exception as e:
        print(f"修復過程中發生錯誤：{e}")
        write_diagnostics("PATCH_EXECUTION_ERROR", path)
        return False

if __name__ == '__main__':
    close_chrome()
    if apply_patch():
        open_chrome()
    else:
        print("修正失敗。")
    time.sleep(2)

# ==============================================================================
#  Copyright (c) Falo x Force Cheng 2026/6/6. All rights reserved.
#  
#  Description: 
#    Chrome Glic (Gemini Live in Chrome) Region Bypass Core Python Script.
#    This script automatically detects the host operating system (macOS/Windows)
#    and updates the Chrome 'Local State' config file to override region checks.
# ==============================================================================

import json
import os
import sys
import subprocess
import time

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
        return False

    if not os.path.exists(path):
        print(f"找不到 Chrome 設定檔：{path}")
        return False

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

    # 強制開啟 glic 相關欄位
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

if __name__ == '__main__':
    close_chrome()
    if apply_patch():
        open_chrome()
    else:
        print("修正失敗。")
    time.sleep(2)

import json
import os

# 設定檔案名稱
CONFIG_FILE = "config.json"

# 預設設定值
DEFAULT_CONFIG = {
    "screen": {
        "width": 1920,
        "height": 1080,
        "capture_area": {"top": 100, "left": 100, "width": 1280, "height": 720}
    },
    "yolo": {
        "model_path": "runs/train/exp/weights/best.pt",
        "confidence_threshold": 0.5
    },
    "mouse": {
        "sensitivity": 0.5,  # 瞄準靈敏度
        "method": "arduino"  # 可選 "pynput", "pyautogui", "arduino"
    },
    "arduino": {
        "port": "COM3",
        "baud_rate": 115200
    },
    "hotkeys": {
        "toggle_aimbot": "f1",
        "toggle_autofire": "f2"
    }
}

def load_config():
    """ 載入設定檔，如果不存在則建立預設設定 """
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    """ 儲存設定到 `config.json` """
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

# 測試用
if __name__ == "__main__":
    config = load_config()
    print("目前設定：", config)

    # 測試修改設定
    config["mouse"]["sensitivity"] = 0.7
    save_config(config)
    print("設定已更新！")

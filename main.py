import time
import threading
from capture import capture_screen
from detect import detect_enemy
from config import load_config
from mouse import move_mouse_to_target, auto_fire
from keyboard import register_hotkeys
from ui.main import start_ui
from logger import log_info

# 讀取設定
config = load_config()

# AI 瞄準狀態
aimbot_enabled = False
autofire_enabled = False

def toggle_aimbot():
    """ 切換 Aimbot 狀態 """
    global aimbot_enabled
    aimbot_enabled = not aimbot_enabled
    log_info(f"Aimbot {'啟動' if aimbot_enabled else '關閉'}")

def toggle_autofire():
    """ 切換自動開槍狀態 """
    global autofire_enabled
    autofire_enabled = not autofire_enabled
    log_info(f"自動開槍 {'啟動' if autofire_enabled else '關閉'}")

def aimbot_loop():
    """ AI 瞄準執行緒 """
    while True:
        if aimbot_enabled:
            enemies = detect_enemy()
            if enemies:
                target_x, target_y = enemies[0]  # 鎖定第一個敵人
                move_mouse_to_target(target_x, target_y)
                if autofire_enabled:
                    time.sleep(0.1)  # 避免過快射擊
                    auto_fire()
        time.sleep(0.05)  # 避免過度佔用 CPU

if __name__ == "__main__":
    # 註冊快捷鍵
    register_hotkeys(toggle_aimbot, toggle_autofire)

    # 啟動 AI 瞄準執行緒
    aimbot_thread = threading.Thread(target=aimbot_loop, daemon=True)
    aimbot_thread.start()

    # 啟動 UI
    start_ui()

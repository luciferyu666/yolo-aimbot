import pyautogui
import time
from pynput.mouse import Controller, Button

# 使用 Pynput 控制滑鼠
mouse = Controller()

def move_mouse_to_target(target_x, target_y, screen_w=1920, screen_h=1080, method="pynput"):
    """
    移動滑鼠到敵人頭部位置。

    :param target_x: 目標 X 座標
    :param target_y: 目標 Y 座標
    :param screen_w: 螢幕寬度
    :param screen_h: 螢幕高度
    :param method: 選擇 'pyautogui' 或 'pynput'
    """
    screen_center_x = screen_w / 2
    screen_center_y = screen_h / 2

    # 計算滑鼠應該移動的相對位置
    dx = target_x - screen_center_x
    dy = target_y - screen_center_y

    # 限制最大移動距離，避免太快鎖定
    dx = max(min(dx, 300), -300)
    dy = max(min(dy, 300), -300)

    # 使用 PyAutoGUI
    if method == "pyautogui":
        pyautogui.moveRel(dx * 0.5, dy * 0.5, duration=0.05)  # 調整速度
    # 使用 Pynput
    elif method == "pynput":
        current_x, current_y = mouse.position
        mouse.position = (current_x + dx * 0.5, current_y + dy * 0.5)  # 平滑移動

def auto_fire(method="pynput"):
    """
    自動開槍（點擊滑鼠左鍵）

    :param method: 選擇 'pyautogui' 或 'pynput'
    """
    if method == "pyautogui":
        pyautogui.click()
    elif method == "pynput":
        mouse.click(Button.left, 1)

if __name__ == "__main__":
    # 測試滑鼠移動
    print("3 秒後移動滑鼠到 (960, 540)")
    time.sleep(3)
    move_mouse_to_target(960, 540)

    # 測試開槍
    time.sleep(1)
    print("開槍！")
    auto_fire()

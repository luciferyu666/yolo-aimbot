import pyautogui

def move_mouse_to_target(target_x, target_y, screen_w=1920, screen_h=1080):
    screen_center_x = screen_w / 2
    screen_center_y = screen_h / 2
    
    # 計算滑鼠應該移動的相對位置
    dx = target_x - screen_center_x
    dy = target_y - screen_center_y
    
    # 移動滑鼠（適當調整移動速度）
    pyautogui.moveRel(dx * 0.5, dy * 0.5, duration=0.05)

if __name__ == "__main__":
    move_mouse_to_target(960, 540)  # 測試滑鼠移動


import cv2
import numpy as np
import mss
import time
import pygetwindow as gw
import pyautogui

# 取得遊戲視窗名稱（請改成你的遊戲名稱）
GAME_WINDOW_TITLE = "Your Game Window Title"

def get_game_window():
    """ 取得遊戲視窗的座標範圍 """
    try:
        win = gw.getWindowsWithTitle(GAME_WINDOW_TITLE)[0]  # 取得遊戲視窗
        return {"top": win.top, "left": win.left, "width": win.width, "height": win.height}
    except IndexError:
        print(f"未找到遊戲視窗: {GAME_WINDOW_TITLE}")
        return None

def capture_screen(monitor):
    """ 擷取螢幕畫面並轉為 OpenCV 格式 """
    with mss.mss() as sct:
        screen = sct.grab(monitor)  # 擷取畫面
        img = np.array(screen)  # 轉為 NumPy 陣列
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 轉換為 OpenCV 格式
        return img

if __name__ == "__main__":
    # 取得遊戲視窗範圍
    monitor = get_game_window()
    if not monitor:
        exit(1)

    prev_time = 0

    while True:
        frame = capture_screen(monitor)  # 擷取畫面

        # 計算 FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        # 顯示 FPS
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 顯示畫面
        cv2.imshow("Game Capture", frame)

        # 按 'q' 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

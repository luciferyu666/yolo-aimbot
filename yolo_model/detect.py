from ultralytics import YOLO
import cv2
import mss
import numpy as np

# 載入 YOLOv8 模型
model = YOLO("yolo_model/model.pt")

def capture_screen():
    with mss.mss() as sct:
        screen = sct.grab(sct.monitors[1])  # 擷取主螢幕
        img = np.array(screen)  # 轉為 numpy 陣列
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 轉為 BGR 格式
        return img

def detect_enemy():
    frame = capture_screen()
    results = model(frame)  # YOLO 偵測
    for result in results.xyxy[0]:  # 取得每個偵測結果
        x1, y1, x2, y2, conf, cls = result.tolist()
        if conf > 0.5:  # 信心度門檻
            head_x = (x1 + x2) / 2
            head_y = (y1 + y2) / 2
            return (head_x, head_y)  # 回傳頭部座標
    return None

if __name__ == "__main__":
    print(detect_enemy())

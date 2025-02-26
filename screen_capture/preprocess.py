import cv2
import numpy as np

def preprocess_frame(frame, img_size=640):
    """
    預處理畫面，使其符合 YOLO 模型的輸入格式。

    :param frame: 來自 capture.py 的原始畫面 (NumPy 陣列)
    :param img_size: YOLO 模型需要的輸入大小 (預設 640x640)
    :return: 處理後的影像
    """
    # 轉換 BGR → RGB（YOLOv8 使用 RGB）
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 縮放圖片至 YOLO 模型的輸入大小 (640x640)
    frame = cv2.resize(frame, (img_size, img_size))

    # 正規化影像（將像素值縮放至 0~1）
    frame = frame / 255.0

    # 轉換為 NumPy 陣列，並調整維度為 (1, 3, 640, 640) 以符合 YOLO 輸入格式
    frame = np.expand_dims(frame, axis=0)  # 增加 batch 維度
    frame = np.transpose(frame, (0, 3, 1, 2))  # 轉換通道順序 (HWC → CHW)

    return frame.astype(np.float32)

# 測試用
if __name__ == "__main__":
    test_img = cv2.imread("test.jpg")  # 測試圖片
    processed_img = preprocess_frame(test_img)
    print(f"Processed Image Shape: {processed_img.shape}")  # 輸出應該是 (1, 3, 640, 640)

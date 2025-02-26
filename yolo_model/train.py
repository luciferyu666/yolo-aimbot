from ultralytics import YOLO

# 載入 YOLOv8 模型（如果是第一次訓練，請使用 'yolov8n.pt'）
model = YOLO("yolov8n.pt")  # 可換成 'yolov8s.pt' 或 'yolov8m.pt' 來提升精度

# 訓練模型
model.train(data="dataset/data.yaml", epochs=50, imgsz=640, batch=8, device="cuda")

# 訓練完成後，儲存最佳權重
model.export(format="torchscript")

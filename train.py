from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")
model.train(data="config.yaml", epochs=10, imgsz=640)
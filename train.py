from ultralytics import YOLO

model = YOLO("yolo11l-seg.pt")
model.train(data="config.yaml", epochs=50, imgsz=640)

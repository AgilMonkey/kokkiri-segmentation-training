from ultralytics import YOLO

model = YOLO("yolo11l-seg.pt")
model.train(data="config.yaml", epochs=50, batch=4, imgsz=640)

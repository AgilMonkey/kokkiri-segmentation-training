from ultralytics import YOLO

model = YOLO("yolo11m-seg.pt")
model.train(data="config.yaml", epochs=50, batch=16, imgsz=640)

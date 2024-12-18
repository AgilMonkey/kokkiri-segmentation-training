from ultralytics import YOLO

model = YOLO("yolo11x-seg.pt")
model.train(data="config.yaml", epochs=50, workers=8, batch=4, imgsz=640)

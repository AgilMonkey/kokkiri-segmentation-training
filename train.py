from ultralytics import YOLO

model = YOLO("yolo11x-seg.pt")
model.train(data="config.yaml", epochs=50, workers=4, batch=8, imgsz=640)

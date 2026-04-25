from ultralytics import YOLO

model = YOLO('yolov8s.pt') # to train in yolo, we always have to use a pretrained model

model.train(data = "data.yaml", epochs = 100, imgsz = 640, batch = 8, workers = 4) # workers is how many CPU threads to use to train
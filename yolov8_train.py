from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='./truck_detect.yaml' , epochs=50)
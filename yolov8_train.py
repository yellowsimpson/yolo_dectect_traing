from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='./box_data.yaml' , epochs=100)
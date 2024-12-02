from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(data='./box_data_3.yaml' , epochs=100)
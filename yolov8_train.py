from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(data='./box_data_4.yaml' , epochs=50)
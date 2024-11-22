from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(data='./box_data_2.yaml' , epochs=100)
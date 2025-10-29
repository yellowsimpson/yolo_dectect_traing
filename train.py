from ultralytics import YOLO

model = YOLO('yolo11n.pt')

model.train(
    data='/home/deepet/Desktop/yellowsimpson/github/yolo_dectect_traing/example.yaml',         #yaml 파일 위치 지정
    epochs=100,
    project='/home/deepet/Desktop/yellowsimpson/github/yolo_dectect_traing/run/detect',       # 폴더 저장 위치
    name='train',                                                                              # 서브폴더 이름 (자동 생성됨)
    exist_ok=False                                                                         
)


# yolo_dectect_traing

**커스텀 데이터로 yolo 모델 만드는법**

1. 내가 인식시키고 싶은 커스텀 데이터를 모아야한다.
-> 필요한 데이터를 img_capture.py (화면의 사진을 1초에 한번씩 찍어서 저장해준다.)코드를 이용해서 모아준다.
-> 아래 사이트에서 이미지 라벨링하는 tool를 설치하고 설명에 맞게 labeling을 해준다.
    1. https://github.com/developer0hye/Yolo_Label
    2. https://app.roboflow.com/
    -> 그 후 아래 폴더 구성에 맞게 파일을 배치해준다.
    -> roboflow는 데이터를 만들고 받을때 자동으로 yaml파일과 데이터 구조를 만들어 준다.

```
.
├── test
│   ├── images
│   │   └── fe1f55fa-19ba3600.png
│   └── labels
│       └── fe1f2409-c16ea1ed.txt
├── train
│   ├── images
│   │   └── fe1f55fa-19ba3600.png
│   └── labels
│       └── fe1f2409-c16ea1ed.txt
└── val
    ├── images
    │   └── fe1f55fa-19ba3600.png
    └── labels
        └── fe1f2409-c16ea1ed.txt
```
2. yaml파일을 만든다.
-> yaml_create.py에서 아래와 같이 코드를 수정하고 실행시킨다.
```
import yaml

data = {
    "train" : '/box_data/train/',
        "val" : '/box_data/valid/',
        "test" : '/box_data/test/', 
        "names" : {0 : 'blue_box', 1 : 'red_box', 2 : 'green_box', 3 : 'yellow_box'}}

with open('./box_data.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('./box_data.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)
``` 

3. 경로 설정
-> 생성된 yaml 파일에서 경로를 올바르게 설정해준다.
```
names:
  0: blue_box
  1: red_box
  2: green_box
  3: yellow_box

test: /Users/mac/Desktop/github/yolo_dectect_traing/box_data_7/test
train: /Users/mac/Desktop/github/yolo_dectect_traing/box_data_7/train
val: /Users/mac/Desktop/github/yolo_dectect_traing/box_data_7/val
```

4. 모델 학습
-> yolov8_train.py 파일에서 모델을 학습시키면된다.
```
from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(data='./box_data.yaml' , epochs=50)
```
-> 이때 yaml 파일의 데이터 경로가 다른면 학습이 안되니 주의하자!

yolov8s.pt
숫자8: yolo 모델 8버전으로 학습
s: n(nano), s(small), m(meduium), l(large), xl(xlarge)
.pt: 학습된 모델 확장자


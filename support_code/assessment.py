import cv2
from ultralytics import YOLO

# model = YOLO('yolov8s.pt')
model = YOLO('/Users/mac/Desktop/github/yolo_dectect_traing/runs/detect/train9/weights/best.pt')            # 적용 모델
results = model('/Users/mac/Desktop/github/yolo_dectect_traing/box_data_7/test/images/yellow_image_3.jpg')  # 평가 파일

plots = results[0].plot()
cv2.imshow("plot", plots)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# from ultralytics import YOLO

# # YOLO 모델 로드
# model = YOLO('C:\\Users\\shims\\Desktop\\github\\yolo_dectect_traing\\runs\\detect\\train\\weights\\best.pt')

# # 웹캠 캡처 객체 생성 (0은 기본 웹캠을 의미)
# cap = cv2.VideoCapture(1)

# while True:
#     # 프레임 읽기
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # YOLO 모델 적용
#     results = model(frame)

#     # 결과 플로팅
#     plots = results[0].plot()

#     # 플롯된 이미지 표시
#     cv2.imshow("YOLO Webcam", plots)

#     # 'q' 키를 누르면 종료
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 웹캠 릴리스 및 창 닫기
# cap.release()
# cv2.destroyAllWindows()


import cv2
from ultralytics import YOLO

model = YOLO("/home/shim/ws/camera_ws/best.pt")

cap = cv2.VideoCapture("/dev/video2")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ 카메라에서 프레임을 읽을 수 없습니다.")
        break

    # CPU 강제 + 속도 옵션(해상도/신뢰도 조정)
    results = model.predict(
        source=frame,
        device="cpu",
        imgsz=640,     # 1280→640로 줄이면 많이 빨라짐
        conf=0.4,
        verbose=False
    )

    annotated = results[0].plot()
    cv2.imshow("YOLO11 Real-Time Detection (CPU)", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2

# 외장 카메라 장치 번호 지정
cap = cv2.VideoCapture("/dev/video6")
#/dev/video8 : 2D카메라
#/dev/video6 : depth 카메라


# 프레임 크기 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ 카메라에서 프레임을 읽을 수 없습니다.")
        break

    cv2.imshow("Camera", frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()

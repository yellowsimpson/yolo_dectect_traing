import cv2
import time
import os

# 저장 폴더 설정
save_dir = "/home/shim/github/yolo_dectect_traing/captured_images"
os.makedirs(save_dir, exist_ok=True)

# 카메라 장치 번호 지정 (2D 카메라)
cap = cv2.VideoCapture("/dev/video2")

# 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다. /dev/video2 장치를 확인하세요.")
    exit()

count = 1
print("📸 1초마다 이미지를 캡처합니다. 중단하려면 Ctrl+C 또는 'q'를 누르세요.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ 프레임을 읽을 수 없습니다.")
            break

        # 이미지 저장
        filename = os.path.join(save_dir, f"truck_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ {filename} 저장됨.")

        # 현재 프레임 표시
        cv2.imshow("Camera (/dev/video6)", frame)

        # 'q' 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 사용자에 의해 종료되었습니다.")
            break

        count += 1
        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:
    print("\n🛑 Ctrl+C로 중단됨.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("🔒 카메라 연결 종료 및 창 닫기 완료.")

import os

# 🔧 설정 부분
folder = r"/home/shim/github/yolo_dectect_traing/captured_images_1"  # 파일이 들어 있는 폴더 경로
prefix = "car_detection"       # 새 이름 앞부분
file_extension = ".jpg" # 바꾸고 싶은 확장자 (예: .jpg, .png, .txt)
start_index = 1         # 시작 번호 (001부터 시작하도록)

# -------------------------------
count = start_index

# 폴더 내 파일 목록 정렬 (순서대로 이름 붙이기 위해)
files = sorted(os.listdir(folder))

for filename in files:
    old_path = os.path.join(folder, filename)

    if not os.path.isfile(old_path):
        continue  # 폴더 무시

    name, ext = os.path.splitext(filename)

    # 지정한 확장자만 처리
    if file_extension and ext.lower() != file_extension.lower():
        continue

    # 새 파일 이름 (예: green_001.jpg)
    new_filename = f"{prefix}{count:03d}{file_extension}"
    new_path = os.path.join(folder, new_filename)

    os.rename(old_path, new_path)
    print(f"{filename} → {new_filename}")

    count += 1

print("✅ 모든 파일 이름이 순차적으로 변경되었습니다.")

import os
import shutil
import random

# ======== 경로 설정 ========
# 이미지가 모여 있는 폴더
IMAGES_DIR = "/home/deepet/VSCode/yolo_dectect_traing/dataset/good_data/img"   # <- 수정

# 라벨(.txt)들이 모여 있는 폴더
LABELS_DIR = "/home/deepet/VSCode/yolo_dectect_traing/dataset/good_data/label"   # <- 수정

# YOLO용 최종 데이터셋 루트 폴더
DATASET_ROOT = "/home/deepet/VSCode/yolo_dectect_traing/dataset/box_data_17"   # <- 수정

# ======== 분할 비율 설정 ========
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 랜덤 시드 (결과 재현용)
random.seed(42)

# ======== 출력 폴더 생성 ========
for sub in ["images/train", "images/val", "images/test",
            "labels/train", "labels/val", "labels/test"]:
    os.makedirs(os.path.join(DATASET_ROOT, sub), exist_ok=True)

# 사용할 이미지 확장자들
IMG_EXTS = [".jpg", ".jpeg", ".png", ".bmp"]

# ======== 이미지-라벨 페어 수집 ========
pairs = []

for file_name in os.listdir(IMAGES_DIR):
    name, ext = os.path.splitext(file_name)
    if ext.lower() in IMG_EXTS:
        img_path = os.path.join(IMAGES_DIR, file_name)
        label_path = os.path.join(LABELS_DIR, name + ".txt")
        # 라벨 파일이 존재할 때만 사용
        if os.path.exists(label_path):
            pairs.append((img_path, label_path))
        else:
            print(f"[경고] 라벨 없음, 스킵: {file_name}")

print(f"총 유효한 이미지-라벨 쌍 개수: {len(pairs)}")

# ======== 셔플 후 train/val/test 나누기 ========
random.shuffle(pairs)

n_total = len(pairs)
n_train = int(n_total * train_ratio)
n_val = int(n_total * val_ratio)
# 나머지는 test로
n_test = n_total - n_train - n_val

train_pairs = pairs[:n_train]
val_pairs = pairs[n_train:n_train + n_val]
test_pairs = pairs[n_train + n_val:]

print(f"train: {len(train_pairs)}, val: {len(val_pairs)}, test: {len(test_pairs)}")

# ======== 복사 함수 ========
def copy_pair(pair_list, img_dest_dir, label_dest_dir):
    for img_path, label_path in pair_list:
        img_name = os.path.basename(img_path)
        label_name = os.path.basename(label_path)

        shutil.copy2(img_path, os.path.join(img_dest_dir, img_name))
        shutil.copy2(label_path, os.path.join(label_dest_dir, label_name))

# ======== 실제 복사 진행 ========
copy_pair(train_pairs,
          os.path.join(DATASET_ROOT, "images/train"),
          os.path.join(DATASET_ROOT, "labels/train"))

copy_pair(val_pairs,
          os.path.join(DATASET_ROOT, "images/val"),
          os.path.join(DATASET_ROOT, "labels/val"))

copy_pair(test_pairs,
          os.path.join(DATASET_ROOT, "images/test"),
          os.path.join(DATASET_ROOT, "labels/test"))

print("✅ 완료! YOLO 학습용 train/val/test 폴더 구성이 끝났습니다.")
print(f"데이터셋 루트: {DATASET_ROOT}")

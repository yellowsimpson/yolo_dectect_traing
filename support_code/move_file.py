import os
import shutil

source_folder = r"C:\Users\shims\Desktop\github\iot_project\data_set_1"  #원본 파일 위치치
jpg_folder = r"C:\Users\shims\Desktop\github\iot_project\image_files"    #이미지 파일 이동할 폴더 위치
txt_folder = r"C:\Users\shims\Desktop\github\iot_project\label_files"    #텍스트 파일 이동할 폴더 위치

# 폴더 없으면 생성
os.makedirs(jpg_folder, exist_ok=True)
os.makedirs(txt_folder, exist_ok=True)

# 파일 반복해서 이동
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        if filename.lower().endswith(".jpg"):
            shutil.move(file_path, os.path.join(jpg_folder, filename))
        elif filename.lower().endswith(".txt"):
            shutil.move(file_path, os.path.join(txt_folder, filename))

print("JPG, TXT 파일 분류 완료!")

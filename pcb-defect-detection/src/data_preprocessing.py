
# coding: utf-8

# In[ ]:


# data_preprocessing.ipynb
import os
import cv2
from pathlib import Path

# 경로 설정
processed_data_dir = os.path.join(base_dir, "processed_data")
os.makedirs(processed_data_dir, exist_ok=True)

# 전처리 함수
def preprocess_images(input_dir, output_dir, img_size=(640, 640)):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for img_file in Path(input_dir).glob("*.jpg"):
        img = cv2.imread(str(img_file))
        img_resized = cv2.resize(img, img_size)
        img_normalized = img_resized / 255.0
        output_path = Path(output_dir) / img_file.name
        cv2.imwrite(str(output_path), (img_normalized * 255).astype("uint8"))
        print(f"전처리 완료: {output_path}")

# 실행
preprocess_images(data_dir, processed_data_dir)


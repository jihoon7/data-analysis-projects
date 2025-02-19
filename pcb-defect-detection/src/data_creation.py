
# coding: utf-8

# In[ ]:


# data_creation.ipynb
import os
import json
import random
from PIL import Image, ImageDraw

# 프로젝트 경로 설정
base_dir = "C:/Users/user/Desktop/data-analysis-projects/pcb-defect-detection"
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# 이미지 생성 함수
def create_pcb_image(filename, shapes):
    image = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(image)
    for shape in shapes:
        draw.rectangle(shape["bbox"], outline="red", width=3)
    image.save(filename)

# 데이터 생성
labels = []
for i in range(1, 21):  # 20개의 데이터 생성
    bbox = [random.randint(50, 400) for _ in range(4)]
    bbox.sort()
    shapes = [{"bbox": bbox}]
    filename = os.path.join(data_dir, f"pcb_image_{i}.jpg")
    create_pcb_image(filename, shapes)
    labels.append({"image": filename, "bbox": bbox})

# 레이블 저장
labels_path = os.path.join(data_dir, "pcb_labels.json")
with open(labels_path, "w") as f:
    json.dump(labels, f)

print(f"데이터 생성 완료: {data_dir}")


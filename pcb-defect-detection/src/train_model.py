
# coding: utf-8

# In[ ]:


# train_model.ipynb
from ultralytics import YOLO
import os
from PIL import Image, ImageDraw

# 테스트 데이터 생성 함수
def create_test_images(test_dir, num_images=5):
    os.makedirs(test_dir, exist_ok=True)
    for i in range(1, num_images + 1):
        img = Image.new("RGB", (640, 640), color="white")
        draw = ImageDraw.Draw(img)
        draw.rectangle([50, 50, 200, 200], outline="blue", width=5)
        img_path = os.path.join(test_dir, f"test_image_{i}.jpg")
        img.save(img_path)
        print(f"테스트 이미지 생성 완료: {img_path}")

# 경로 설정
test_data_dir = os.path.join(base_dir, "tests")
create_test_images(test_data_dir, num_images=5)

# 모델 학습
data_yaml_path = os.path.join(processed_data_dir, "pcb_data.yaml")
model_save_dir = os.path.join(base_dir, "models")
os.makedirs(model_save_dir, exist_ok=True)

model = YOLO("yolov8s")
model.train(data=data_yaml_path, epochs=30, imgsz=640, project=model_save_dir, name="pcb_training", save=True)
print(f"모델 학습 완료. 저장 경로: {model_save_dir}")


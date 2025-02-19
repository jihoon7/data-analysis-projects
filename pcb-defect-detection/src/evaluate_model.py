
# coding: utf-8

# In[ ]:


# evaluate_model.ipynb
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
import cv2

# 모델 평가 및 시각화
def evaluate_and_visualize(model, test_data_dir):
    test_images = [os.path.join(test_data_dir, img) for img in os.listdir(test_data_dir) if img.endswith(".jpg")]
    results = model.predict(source=test_images, save=True)
    
    for result in results:
        img = cv2.imread(result.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.axis("off")
        plt.show()

# 실행
model_path = os.path.join(model_save_dir, "pcb_training", "weights", "best.pt")
model = YOLO(model_path)
evaluate_and_visualize(model, test_data_dir)



# coding: utf-8

# In[ ]:


import os
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

def evaluate_model(model, test_data_dir):
    test_images = [os.path.join(test_data_dir, img) for img in os.listdir(test_data_dir) if img.endswith(('.jpg', '.png'))]
    if not test_images:
        raise ValueError(f"테스트 데이터가 없습니다: {test_data_dir}")
    return model.predict(source=test_images, save=True)

def visualize_results(predictions):
    for result in predictions:
        img = cv2.cvtColor(cv2.imread(result.path), cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(8, 8))
        plt.imshow(img)
        plt.axis("off")
        plt.title(f"Predicted: {os.path.basename(result.path)}")
        plt.show()

if __name__ == "__main__":
    base_dir = "C:/Users/user/Desktop/data-analysis-projects/artwork-object-detection"
    test_data_dir = os.path.join(base_dir, "tests")
    model_path = os.path.join(base_dir, "models", "artwork_training", "weights", "best.pt")
    
    model = YOLO(model_path)
    predictions = evaluate_model(model, test_data_dir)
    visualize_results(predictions)


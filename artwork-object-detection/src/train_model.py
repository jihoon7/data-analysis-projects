
# coding: utf-8

# In[ ]:


from ultralytics import YOLO
import os

def train_model(data_yaml_path, model_save_dir, epochs=10):
    model = YOLO("yolov8s")
    model.train(
        data=data_yaml_path,
        epochs=epochs,
        imgsz=640,
        batch=16,
        project=model_save_dir,
        name="artwork_training",
        save=True
    )
    return model

if __name__ == "__main__":
    base_dir = "C:/Users/user/Desktop/data-analysis-projects/artwork-object-detection"
    processed_data_dir = os.path.join(base_dir, "processed_data")
    data_yaml_path = os.path.join(processed_data_dir, "artwork_data.yaml")
    model_save_dir = os.path.join(base_dir, "models")
    os.makedirs(model_save_dir, exist_ok=True)

    train_model(data_yaml_path, model_save_dir, epochs=10)


import os
import json
from PIL import Image, ImageDraw

def create_pcb_data():
    data_dir = "pcb-defect-detection/data"
    os.makedirs(data_dir, exist_ok=True)

    # 이미지 생성
    image = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 150, 150], outline="red", width=3)
    image.save(os.path.join(data_dir, "pcb_1.jpg"))

    # 레이블 데이터 생성
    labels = [{"image": "pcb_1.jpg", "bbox": [50, 50, 150, 150], "label": "defect"}]
    with open(os.path.join(data_dir, "pcb_labels.json"), "w") as f:
        json.dump(labels, f)

if __name__ == "__main__":
    create_pcb_data()
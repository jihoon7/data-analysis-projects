import os
import json
from PIL import Image, ImageDraw

def create_artwork_data():
    data_dir = "artwork-object-detection/data"
    os.makedirs(data_dir, exist_ok=True)

    # 이미지 생성
    image = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 150, 150], outline="blue", width=3)
    draw.ellipse([200, 200, 300, 300], outline="red", width=3)
    image.save(os.path.join(data_dir, "artwork_1.jpg"))

    # 레이블 데이터 생성
    labels = [
        {"image": "artwork_1.jpg", "bbox": [50, 50, 150, 150], "label": "rectangle"},
        {"image": "artwork_1.jpg", "bbox": [200, 200, 300, 300], "label": "circle"}
    ]

    with open(os.path.join(data_dir, "artwork_labels.json"), "w") as f:
        json.dump(labels, f)

if __name__ == "__main__":
    create_artwork_data()
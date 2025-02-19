
# coding: utf-8

# In[ ]:


import json
import os
import random
from PIL import Image, ImageDraw

def create_artwork_image(filename, shapes):
    image = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(image)
    for shape in shapes:
        if shape["label"] == "rectangle":
            draw.rectangle(shape["bbox"], outline="blue", width=3)
        elif shape["label"] == "circle":
            x0, y0, x1, y1 = shape["bbox"]
            draw.ellipse((x0, y0, x1, y1), outline="red", width=3)
    image.save(filename)

def create_random_images(output_dir, num_images=10):
    os.makedirs(output_dir, exist_ok=True)
    for i in range(1, num_images + 1):
        img = Image.new("RGB", (500, 500), color="white")
        draw = ImageDraw.Draw(img)
        for _ in range(random.randint(1, 5)):
            shape_type = random.choice(["rectangle", "circle"])
            x0, y0 = random.randint(50, 400), random.randint(50, 400)
            x1, y1 = x0 + random.randint(50, 100), y0 + random.randint(50, 100)
            if shape_type == "rectangle":
                draw.rectangle([x0, y0, x1, y1], outline="blue", width=3)
            elif shape_type == "circle":
                draw.ellipse([x0, y0, x1, y1], outline="red", width=3)
        img_path = os.path.join(output_dir, f"random_image_{i}.jpg")
        img.save(img_path)
        print(f"랜덤 이미지 생성 완료: {img_path}")

if __name__ == "__main__":
    base_dir = "C:/Users/user/Desktop/data-analysis-projects/artwork-object-detection"
    data_dir = os.path.join(base_dir, "data")
    create_random_images(data_dir, num_images=20)


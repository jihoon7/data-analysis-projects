import os
import pandas as pd

def create_education_data():
    data_dir = "special-education-analysis/data"
    os.makedirs(data_dir, exist_ok=True)

    # 특수교육 데이터 생성
    data = {
        "region": ["Seoul", "Busan", "Incheon"],
        "students": [100, 50, 75],
        "teachers": [10, 5, 7]
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(data_dir, "education_data.csv"), index=False)

if __name__ == "__main__":
    create_education_data()
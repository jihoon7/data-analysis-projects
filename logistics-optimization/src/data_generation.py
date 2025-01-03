import os
import pandas as pd

def create_logistics_data():
    data_dir = "logistics-optimization/data"
    os.makedirs(data_dir, exist_ok=True)

    # 물류 데이터 생성
    data = {
        "node_a": ["A", "A", "B"],
        "node_b": ["B", "C", "C"],
        "distance": [10, 20, 15],
        "cost": [5, 8, 7]
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(data_dir, "logistics_data.csv"), index=False)

if __name__ == "__main__":
    create_logistics_data()
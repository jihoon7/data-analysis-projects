import os
import pandas as pd

def create_customer_data():
    data_dir = "customer-insights-dashboard/data"
    os.makedirs(data_dir, exist_ok=True)

    # 고객 데이터 생성
    data = {
        "customer_id": [1, 2, 3],
        "age": [32, 45, 28],
        "region": ["Seoul", "Busan", "Incheon"],
        "purchase_amount": [250, 300, 150]
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(data_dir, "customer_data.csv"), index=False)

if __name__ == "__main__":
    create_customer_data()

# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# 데이터 로드
file_path = 'C:/Users/user/Desktop/data-analysis-projects/logistics-optimization/data/logistics_data.csv'
df = pd.read_csv(file_path)

# 전처리
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfYear'] = df['Date'].dt.dayofyear
df['WarehouseID'] = df['WarehouseID'].astype('category').cat.codes

# 훈련/테스트 데이터 분할
X = df[['WarehouseID', 'DayOfYear']]
y = df['ProductQuantity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# 평가
y_pred = model.predict(X_test)
print("평균 제곱 오차 (MSE):", mean_squared_error(y_test, y_pred))


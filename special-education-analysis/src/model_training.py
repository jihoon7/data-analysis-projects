
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 데이터 로드
file_path = 'C:/Users/user/Desktop/data-analysis-projects/special-education-analysis/data/special_education_data.csv'
df = pd.read_csv(file_path)

# 전처리
df['SpecialNeeds'] = df['SpecialNeeds'].map({'Yes': 1, 'No': 0})
df = pd.get_dummies(df, columns=['Region', 'Gender'], drop_first=True)

# 훈련/테스트 데이터 분할
X = df.drop('SpecialNeeds', axis=1)
y = df['SpecialNeeds']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 평가
y_pred = model.predict(X_test)
print("정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


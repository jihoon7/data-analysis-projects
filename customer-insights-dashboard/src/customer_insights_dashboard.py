
# coding: utf-8

# In[ ]:


# 데이터 생성
import pandas as pd

# 텍스트 데이터 생성
data = pd.DataFrame({
    "text": [
        "연애 고민이 많아요",
        "이별 후에 힘들어요",
        "새로운 만남을 시작하고 싶어요",
        "현재 연애에 문제가 생겼어요",
        "짝사랑을 하고 있는데 어떻게 고백할까요?"
    ] * 6,
    "label": ["silver", "gold", "black", "silver", "gold"] * 6
})

# 데이터 저장
data.to_csv("C:/Users/user/Desktop/data-analysis-projects/customer-insights-dashboard/data/customer_data.csv", index=False)


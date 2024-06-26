import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 讀取資料
# wget https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv
df = pd.read_csv('house-prices.csv')

# 資料預處理
df = df.dropna()  # 刪除缺失值

# 構建特徵和目標變量
#X = df[['Bedrooms', 'Bathrooms', 'SquareFeet']]
X = df[['Bedrooms', 'Bathrooms', 'SqFt']]
y = df['Price']

# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 訓練模型
model = LinearRegression()
model.fit(X_train, y_train)

# 預測
y_pred = model.predict(X_test)

# 評估模型
mse = mean_squared_error(y_test, y_pred)
print(f"均方誤差：{mse}")

# 顯示預測結果
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

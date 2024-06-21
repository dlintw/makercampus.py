import pandas as pd
import matplotlib.pyplot as plt

# 創建一個銷售數據 DataFrame
data = {
    '月份': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '銷售額': [1000, 1500, 2000, 2500, 3000, 3500]
}
df = pd.DataFrame(data)

# 繪製銷售趨勢圖
plt.plot(df['月份'], df['銷售額'], marker='o')
plt.title('銷售趨勢圖')
plt.xlabel('月份')
plt.ylabel('銷售額')
plt.grid(True)
plt.show()

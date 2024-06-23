import pandas as pd
import matplotlib
# matplotlib.use('Agg')  # no UI backend
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['MingLiU']
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=14)
plt.rc('legend', fontsize=14)

# 創建一個銷售數據 DataFrame
data = {
    '月份': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '銷售額': [1000, 1500, 2000, 2500, 3000, 3500]
}
df = pd.DataFrame(data)

# 繪製銷售趨勢圖
plt.plot(df['月份'].values, df['銷售額'].values, marker='o')
plt.title('銷售趨勢圖')
plt.xlabel('月份')
plt.ylabel('銷售額')
plt.grid(True)
plt.show()
# plt.savefig("output.png")

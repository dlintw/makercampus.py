#!/usr/bin/python3
import yfinance as yf
# https://pypi.org/project/yfinance/ 建議看一下原始文件
# yahoo 授權裏提到: 某些 API 只允許非商業使用，禁止在高流量、商業網站或通過廣告
# 和聯盟鏈接間接盈利的應用中使用這些服務。

# 定義股票代碼
stock_code = "NVDA"  # 替換為你感興趣的股票代碼

# 獲取股票數據
stock = yf.Ticker(stock_code)

# 獲取當前股票價格(收盤價)
current_price = stock.history(period="1d")['Close'].iloc[0]

# 獲取歷史數據（最近一年的數據）
historical_data = stock.history(period="1y")

print(f"當前 {stock_code} 股票價格: {current_price}")
print("最近一年的股票數據:")
print(historical_data)

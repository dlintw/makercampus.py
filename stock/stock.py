#!/usr/bin/python3
import yfinance as yf

# 定义股票代码
stock_code = "NVDA"  # 替换为你感兴趣的股票代码

# 获取股票数据
stock = yf.Ticker(stock_code)

# 获取当前股票价格
current_price = stock.history(period="1d")['Close'].iloc[0]

# 获取历史数据（最近一年的数据）
historical_data = stock.history(period="1y")

print(f"当前 {stock_code} 股票价格: {current_price}")
print("最近一年的股票数据:")
print(historical_data)


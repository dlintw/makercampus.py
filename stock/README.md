# 1. 前言
課程目標, 希望由寫課程的過程, 對相關主題進行初步的實作, 因時間有限,
不排除隨時調整大綱.

# 2. 環境設置
安裝 Anaconda 或其他(eg. 例如: Windows11 + WSL2(Ubuntu 22.04) + VSCode),
無論環境怎樣, 基本上能運作相關 python 套件即可, 建議安裝 ipython3 是一個
強大的交互式 Python shell 便於交互式調試
(如: pandas、numpy、matplotlib、seaborn、yfinance 等）
若要做機器學習部分實作, 需要有對應較快速硬體加速設備
建議的環境是 Ubuntu 22.04 相容(未來有機會使用 mojo 程式語言, 寫類似語法加速)
# 3. 股票數據獲取
## 3.1 使用 yfinance 獲取歷史股票數據
要細看[原始文件](https://pypi.org/project/yfinance/), yahoo 授權裏提到:
某些 API 只允許非商業使用，禁止在高流量、商業網站或通過廣告, 和聯盟鏈接間接盈利
的應用中使用這些服務。另外, yfinance 雖提供全球股市資訊, 但除美股外, 其他正確性
自行驗證。

和一般教學不同, 安裝 yfinance 要加參數
```
pip install -y 'yfinance[nospam,repair]'
```
範例, [股票代號查詢](https://finance.yahoo.com/lookup/)
[API文件](https://github.com/ranaroussi/yfinance/wiki/Ticker#history)
```python
import yfinance as yf
stock_code = "NVDA"  # 替換為你感興趣的股票代碼
# stock_code = "006208.TW"  # 台灣的股票以 .TW 結尾
stock = yf.Ticker(stock_code)
current_price = stock.history(period="1d")['Close'].iloc[0]  # 收盤價
print(f"當前 {stock_code} 股票價格: {current_price}")
print("最近一年的股票數據:")
historical_data = stock.history(period="1y")
print(historical_data)
```
作業: 使用 ipython, 找到某一檔股票, 查
[quick-start](https://pypi.org/project/yfinance/#quick-start)
裡面展示的各項數據, 查還原權值數據

import yfinance as yf
import pandas as pd

# 定義 AAPL 的股票代號
ticker = 'AAPL'

# 使用 yfinance 獲取 TSMC 股票資料
tsmc = yf.Ticker(ticker)

# 獲取 TSMC 的季度財務報告
financials = tsmc.quarterly_financials

# 提取需要的財務數據項目
items_to_extract = ['Total Revenue', 'Gross Profit', 'Research Development',
                    'Operating Expense', 'Operating Income', 'Net Income']

# 創建一個 DataFrame 來存儲這些數據
extracted_data = pd.DataFrame()

# 將這些項目從財務報告中提取出來
for item in items_to_extract:
    if item in financials.index:
        extracted_data[item] = financials.loc[item]

# 將數據轉置，使得日期成為 index
extracted_data = extracted_data.T

# 先將 index 排序，避免 datetime slicing 問題
extracted_data = extracted_data.sort_index(axis=1)

# 只選取從 2020 年到 2024 年的數據
extracted_data = extracted_data.loc[:, '2020-01-01':]

# 將提取的數據存成 Excel 檔案
extracted_data.to_excel('aapl_quarterly_income_statement_2020_2024.xlsx', index=True)

print("已生成文件")

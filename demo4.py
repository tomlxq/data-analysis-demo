#第一部分 课前准备和数据源的获取
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
#获得相关组件的支持 pandas numpy datetime和plt
#获得股票金融数据源，安装常见的一些软件包
# pip install yfinance
pip install fix_yahoo_finance
pip install quandl
pip install datetools
pip install statsmodels -U
pip install tushare
pip install pandas_datareader


# import fix_yahoo_finance as yf
# aap1 = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2021, 3, 1),
# end = datetime.datetime(2022, 1, 1))
# print(aap1.head())
btc = pdr.get_data_yahoo('BTC-USD', start=datetime.datetime(2021, 1, 1), end=datetime.datetime(2021, 12, 30))

btc.head()
btc.reset_index(inplace=True)
btc.columns
btc.columns = ['date', 'high', 'low', 'open', 'close', 'volume', 'aa']
btc.head()
df1 = btc
df1.index = btc.iloc[:, 0]
df1.index = pd.to_datetime(df1.index, format='%Y-%m-%d')
# f1.index = btc.iloc[:, 1:]
print(df1.head())
df1 = df1['2021-01-01', '2021-01-04']
print(df1.head())

#使用duplicated查看所有重复元素行
- first  # 保留第一行重复的值
- last  # 保留最后一行重复的值
- False  # 不保留重复行
df1[df1.index.duplicated()]
df1 = df1.loc[~df1.index.duplicated(keep='first')]
plt.figure(figsize=(12, 6))
plt.
#
# btc.tail()

# eth = pdr.get_data_yahoo('ETH-USD', start=datetime.datetime(2021, 3, 1),end=datetime.datetime(2022, 1, 1))
# print(eth.head())

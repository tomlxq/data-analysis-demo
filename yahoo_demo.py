import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)
df = web.DataReader('XOM', 'yahoo', start, end)
print(df)
import tushare as ts

fi = open('tk', 'r')
akey = ''
for i in fi:
    akey = i
print(akey)
ts.set_token(akey)  # 设置token，只需设置一次
pro = ts.pro_api()  # 初始化接口
# 获取股票基础信息数据，包括股票代码、名称、上市日期，行业、概念等
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)
print(data[data.ts_code == '600519.SH'])

df = pro.daily(ts_code='600519.SH,600759.SH', start_date='20210101', end_date='20210410')
print(df.head(10))
df.to_csv('600519.SH.csv')
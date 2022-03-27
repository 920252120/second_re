import pandas as pd


csv_path = r'C:\Users\LYQ\Desktop\datanalyze\station.csv'
data = pd.read_csv(csv_path, index_col=0, encoding='gbk')
station = '1'
print(data)
print(int(station))

station_name = data.iloc[int(station)][1]
print(station_name)

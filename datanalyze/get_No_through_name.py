import pandas as pd
import os
import re

dir_path = r'C:\Users\LYQ\Desktop\datanalyze\值得挖掘的公司数据\值得挖掘的公司数据'

files = os.listdir(dir_path)

table_path = r'C:\Users\LYQ\Desktop\datanalyze\station.csv'
data_path = r'C:\Users\LYQ\Desktop\datanalyze\2015-2019yearflow\2015-2019tot.csv'

to_path = r'C:\Users\LYQ\Desktop\datanalyze\值得挖掘的公司数据\filtered.csv'

data = pd.read_csv(data_path,index_col=0)
data = data.drop(['Unnamed: 0','0'], axis=1)

table = pd.read_csv(table_path, index_col=0,encoding='gbk')
table1 = table.set_index('theuser')
# print(table.set_index('theuser'))
# print(table['出口南线':'出口南线'])
idx_station=[]
idx_station1=[]

pat = "(.*?)[.]png"
pattern = re.compile(pat)
for name in files:
    matchobj = re.search(pattern, name)
    station = matchobj.group(1)
    idx_station.append(table1[station:station].iloc[0][0])
for i in range(len(idx_station)):
    idx_station1.append(str(idx_station[i]))


# idx_station = pd.Series(idx_station)
# print(type(idx_station1[1]))



data_filtrated = data.loc[:][idx_station1[0:-1]]

def change_name(data_filtrated, table, to_path):
    for col in range(len(data_filtrated.columns)):
        col_name = data_filtrated.columns[col]
        if col_name == 'index':
            continue
        print(col_name)
        col_inplace = table.iloc[int(col_name)-1][1]
        data_filtrated.rename(columns={col_name:col_inplace}, inplace=True)

    data_filtrated.to_csv(to_path)


change_name(data_filtrated, table, to_path)


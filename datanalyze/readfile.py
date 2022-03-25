import pandas as pd
import numpy as np
from datetime import datetime
import re


cp_data_month = []
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
for j in range(100):
    if j== 2:
        continue
    if j == 15:
        continue
    if j == 18:
        continue
    if j == 24:
        continue
    if j == 35:
        continue
    if j == 39:
        continue
    if j == 40:
        continue
    if j == 41:
        continue
    if j == 42:
        continue
    if j == 57:
        continue
    if j == 65:
        continue
    if j == 72:
        continue
    if j == 76:
        continue
    if j == 91:
        continue
    if j == 99:
        continue
    data = []
    list = ['f', 'pl', 't', 'p', 'tot', 'md', 'ye', 'recTime', 'thetime']
    for i in range(0, 10):
        path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\all0-100\\' + str(j + 1) + '\\rw' + str(
            j + 1) + '-2021-' + str(i + 1) + '.csv'
        to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100' + '\\' +  str(j + 1) \
        + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'
        # path = r'C:\Users\lyq92\Desktop\DataAnalyse\all0-100' +'\\'+str(j+1)\
        #         +'\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'
        #
        # to_path = r'C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100' + '\\' + str(j + 1) \
        #      + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'

        df_data = pd.read_csv(path, header=None, sep='\\t', engine='python')  # 读文件
        df_data.columns = list
        df_data = df_data[['tot', 'recTime', 'thetime']]  # 筛选出有用列
        df_data = df_data.sort_values(by='thetime')  # 将索引的值进行排序

        # 正则表达式筛选出需要的列
        # pat = "((?<!01)\s00:01:\d\d)|(01\s00:00:)"
        pat = "(\s00:0[01]:\d\d)|((?<=" + str(month_days[i]) + ')\s23:5[89])'
        mask = df_data['thetime'].str.contains(pat)  # 第一次筛选出00和01分的数据
        df_data = df_data[mask]
        # print(df_data)


        bool1 = []
        k=0
        z=1
        # for z in range(1, month_days[i] + 1):
        # while z < month_days[i]+1:
        #     pat1 = '('+str(z) + "\s00:\d\d:)|(0" + str(i+2)+ '-01\s00:)'
        #     print(pat1)
        #     patten = re.compile(pat1)
        #     if re.search(patten,df_data.iloc[k]['thetime']):
        #         bool1.append(True)
        #         z += 1
        #     else:
        #         bool1.append(False)
        #     k += 1
        while k < len(df_data):
            pat1 = '(' + str(z) + "\s00:\d\d:)|((?<=" + str(month_days[i]) + ')\s(23):5[89])'
            patten = re.compile(pat1)
            matchobj = re.search(patten, df_data.iloc[k]['thetime'])
            if matchobj:
                # print(matchobj.group(3))
                if matchobj.group(3)=="23":
                    bool1.append(True)
                    break
                bool1.append(True)
                z += 1
            else:
                bool1.append(False)
            k += 1

        while len(bool1) < len(df_data):
            bool1.append(False)
        print(df_data[bool1])
        df_data = df_data[bool1]







        # 设置日期为序列的df
        data = str(i+1)+r'/1/2021'
        daily_flow = pd.DataFrame(index=pd.date_range(data, periods=len(df_data)-1))
        print('len='+str(len(df_data)))

        flow = []
        for z in range(len(df_data)-1):
            flow.append(df_data.iloc[z+1]['tot'] - df_data.iloc[z]['tot'])
        flow = np.asarray(flow)
        daily_flow.insert(column=str(j), value=flow, loc=0)
        print(daily_flow)
        print(len(daily_flow))
        daily_flow.to_csv(to_path)








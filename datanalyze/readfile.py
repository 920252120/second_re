import pandas as pd
import numpy as np
from datetime import datetime


cp_data_month = []
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
    for i in range(10):
        # path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\all0-100\\' + str(j + 1) + '\\rw' + str(
        #     j + 1) + '-2021-' + str(i + 1) + '.csv'
        # to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100' + '\\' +  str(j + 1) \
        # + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'
        path = r'C:\Users\lyq92\Desktop\DataAnalyse\all0-100' +'\\'+str(j+1)\
                +'\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'

        to_path = r'C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100' + '\\' + str(j + 1) \
             + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'


        df_data = pd.read_csv(path, header=None, sep='\\t', engine='python')
        df_data.columns = list
        df_data = df_data[['tot', 'recTime', 'thetime']]
        pat = "(00:01:\d\d)|(01\s00:00:)"
        mask = df_data['thetime'].str.contains(pat)
        df_data = df_data[mask]
        data = str(i+1)+r'/1/2021'
        daily_flow = pd.DataFrame(index=pd.date_range(data, periods=len(df_data)-1))
        flow = []
        for z in range(len(df_data)-1):
            flow.append(df_data.iloc[z+1]['tot'] - df_data.iloc[z]['tot'])
        flow = np.asarray(flow)
        daily_flow.insert(column='flow', value=flow, loc=0)
        print(daily_flow)
        daily_flow.to_csv(to_path)





        # df_data.to_csv(to_path)


    #     aa = df_data.values[-1, 4] - df_data.values[0, 4]
    #     if aa < 0:
    #         aa = aa1
    #
    #     data.append(aa)
    #     aa1 = aa
    # cp_data_month.append(data)


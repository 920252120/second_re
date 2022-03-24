import pandas as pd
import numpy as np


cp_data_month = []
for j in range(100):
    if j == 1:
        break
    if j == 2:
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
        path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\all0-100\\' + str(j + 1) + '\\rw' + str(
            j + 1) + '-2021-' + str(i + 1) + '.csv'
        to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100' + '\\' + str(j + 1) \
                  + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'

        df_data = pd.read_csv(path, header=None, sep='\\t', engine='python')
        df_data.columns = list
        df_data = df_data[['tot', 'recTime', 'thetime']]
        df_data = df_data.sort_values(by='recTime')
        pat = "(00:00:\d\d)|((\d{4}-\d\d-01\s((00:00:\d\d)|(00:01:\d\d))))"
        mask = df_data['thetime'].str.contains(pat)
        df_data1 = df_data[mask]
        print(df_data1)


        date = str(i + 1) + '/1' + '/2021'
        long = pd.DataFrame(index=pd.date_range(date, periods=len(df_data1)-1))

        flow = []
        for z in range(len(df_data1) - 1):
            flow.append(df_data1.iloc[z + 1, 0] - df_data1.iloc[z, 0])

        flow = np.asarray(flow)
        long.insert(loc=0, column='flow', value=flow)

        # if i == 0:
        #     result = long
        # else:
        #     pd.concat(result, long)
        #
        long.to_csv(r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\1'+'\\'+str(i)+'.csv')
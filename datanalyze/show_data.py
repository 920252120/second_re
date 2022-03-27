import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font",family='DengXian')
path = r'C:\Users\LYQ\Desktop\datanalyze\test\years\2015-2019tot.csv'

data = pd.read_csv(path, parse_dates=['index'], infer_datetime_format=True)
csv_path = r'C:\Users\LYQ\Desktop\datanalyze\station.csv'
name = pd.read_csv(csv_path, index_col=0, encoding='gbk')



N = 10
x = data['index']

data = data.drop(['Unnamed: 0.1','Unnamed: 0'],axis=1)

length = len(data.columns)


for i in range(1, length):
    fig = plt.figure(figsize=(100, 20))
    ax = fig.add_subplot(1, 1, 1)
    station = data.columns[i]
    data1 = data[station]
    station_name = name.iloc[int(station)-1][1]
    print(station,station_name)

    data1.plot(ax=ax, style='k-')

    ax.set_xticks(range(0, len(x), len(data1) // N))
    ax_xticklabels = list(map(lambda x: str(x)[0:4] + str(x)[5:7] + str(x)[8:10], x))
    ax.set_xticklabels(ax_xticklabels[::len(data1) // N])
    ax.set_xlabel('date', size=30)
    ax.set_ylabel('dailyfolw', size=30)
    ax.set_title(station_name, size=30)
    plt.tick_params(labelsize=23)

    plt.savefig(r'C:\Users\LYQ\Desktop\datanalyze\figs'+'\\'+station_name+'.png')
    plt.close()

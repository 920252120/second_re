import numpy as np
import pandas as pd
import os


# 组合一个路径的函数
def get_path(root_path, folder_path, csv_path):
    path = os.path.join(root_path, folder_path, csv_path)
    return path


names1 = np.array(['station', 'date', 'hour', 'dailyflow', 'tot'])


def daily_flow(from_path, to_path):
    flow = pd.read_csv(from_path, header=None, names=names1)
    # 对数据进行排序，按日期和小时来排序
    flow = flow.sort_values(by=['date', 'hour'])
    # 下面建立以站点为columns和以日期为index的新列表
    data_daily = pd.DataFrame(columns=flow.station.unique(), index=flow.date.unique())

    date_index = data_daily.shape[0]
    station_columns = data_daily.shape[1]
    for j in range(date_index):
        for i in range(station_columns):
            tmp = flow[flow.station == data_daily.columns[i]]  # 先把站点等于列名的数据筛选出来
            data_daily.iloc[j, i] = tmp[tmp.date == data_daily.index[j]].dailyflow.sum()  # ？？？如何通过两列的值来筛选？
    data_daily.to_csv(to_path)


if __name__ == '__main__':
    # 获取一个文件夹内所有文件
    root_path = "C:\\Users\\LYQ\\Desktop\\datanalyze\\test\\2015"  # 文件目录
    to_path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\test\\to_2015'
    # 下面处理一个文件夹内所有的csv
    files = os.listdir(root_path)
    files_num = len(files)

    for i in range(files_num):
        path = os.path.join(root_path, files[i])
        to_path_file = os.path.join(to_path, files[i])
        daily_flow(path, to_path_file)


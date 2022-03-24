"""
根据文件夹和文件后面的后缀来判断年份和月份，然后根据每个文件的一列的长度来规定period，每次读完一个文件要按原索引
进行一个排序，使其按日期的升序来排序。之后用 data.insert(loc=0, column='index', value=pd.data_range('mon/day/year', period=))
插入索引列，再用data.set_index('index')来改变其索引
"""
import os
import numpy as np
import pandas as pd
import re
from datetime import datetime


def getyearmon(pattern_str, string):
    pattern = re.compile(pattern_str)
    matchobj = re.search(pattern, string)
    return matchobj.group(1), matchobj.group(2)



def get_path1(*args):
    result = ''
    for path in args:
        result = os.path.join(result, path)

    return result


# 判断一个文件名是不是我想要的格式
def judge_file(pattern_str, file_name):
    patten = re.compile(pattern_str)
    matchobj = re.search(patten, file_name)
    if matchobj:
        return True
    else:
        return False






if __name__ == '__main__':
    # 获取一个文件夹内所有文件
    root_path = r"C:\Users\LYQ\Desktop\datanalyze\test"  # 文件目录
    todir_path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\test'

    # ？？？这里如何判断是否存在文件夹，若无则创建

    # 下面处理一个文件夹内所有的csv
    # files = os.listdir(root_path)  # 拿到一个文件夹内的所有文件返回到一个数组里
    # files_num = len(files)
    patten_str = r"(\d{4})_([1]?\d)"
    file_patten = r".*.csv$"





    for j in range(2015,2020):
        dir_path = os.path.join(root_path, str(j))  # 拼接一个文件夹的地址
        # dir_path = root_path + '\\' + str(j)

        files = os.listdir(dir_path)  # 拿到一个文件夹内的所有文件返回到一个数组里
        files_num = len(files)

        to_path = os.path.join(todir_path, 'to_'+str(j))
        # to_path = todir_path + '\\' + 'to_' + str(j)
        # print("dir_path: {}, to_path: {}".format(dir_path, to_path))
        break
        for i in range(files_num):
            path = get_path1(dir_path, files[i])  # 这里如何用函数进行代替，学会用多参数函数
            # to_path_file = get_path1(to_path, files[i])

            print(files[i])

            data = pd.read_csv(path, index_col=0)
            data = data.sort_index()  # 将索引进行排序

            year, mon = getyearmon(patten_str, files[i])  # 找到文件名中的月份和年份
            date = mon + '/' + '1' + '/'+ year
            days = data.shape[0]  # 找到一个表里面的天数

            data.insert(loc=0, column='index', value=pd.date_range(date, periods=days))  # 在列表的第一列插入索引
            data.set_index(['index'])

            data.to_csv(to_path+'\\'+files[i], index=False)







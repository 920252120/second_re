import pandas as pd
import os


  #将一个文件夹内的所有csv进行上下合并返回一个df
def concat_csv(path):
    files = os.listdir(path)
    num_files = len(files)
    if num_files == 0:
        return False
    obj_file = os.path.join(path, files[0])

    result = pd.read_csv(obj_file)
    if result is None:
        return None
    print(len(files))


    for i in range(1, num_files):
        print(files[i])
        obj_file = os.path.join(path, files[i])
        file = pd.read_csv(obj_file)
        result = pd.concat([result, file])
    result = result.rename(columns={"Unnamed: 0":"date"})
    print(result)
    return result.sort_values(by="date")


def merge_csv(dir_path, to_path):
    files = os.listdir(dir_path)
    result = pd.read_csv(dir_path + '\\' + files[0], index_col=0,)
    length = len(files)
    for i in range(1, length):
        tmp = pd.read_csv(dir_path + '\\' + files[i], index_col=0)
        result = pd.merge(result, tmp, on='date', how='outer')
    result.to_csv(to_path + '\\' + 'allinone.csv')


if __name__ == '__main__':
      # 合并
    # dir_path = r"C:\Users\LYQ\Desktop\datanalyze\to_all0-100\allinone1"
    # to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\allinone2'
    dir_path = r"C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100\allinone"
    to_path = r'C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100\test'

    merge_csv(dir_path, to_path)



    # 尝试合并1号station
    #   dir_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\1'
    #   to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\allinonetest'
    #   file = concat_csv(dir_path)
    #   file = file.rename({'0':'1'},axis=1)
    #   file.to_csv(to_path + '\\'+ "1.csv")

    # 上下拼接每个station
    # to_path = r'C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100\allinone'
    # for i in range(1, 101):
    #     dir_path = r'C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100' + '\\'+ str(i)
    #     file = concat_csv(dir_path)
    #     if file is False:
    #           continue
    #     file.to_csv(to_path + '\\' + str(i) + ".csv")


    # 转移文件到另一个文件夹中
    # for i in range(100):
    #     path1 = path + '\\' + str(i+1)
    #     file = concat_csv(path1)
    #     if file is False:
    #         continue
    #
    #     file.to_csv(to_path + '\\' + str(i+1)+'tot.csv')




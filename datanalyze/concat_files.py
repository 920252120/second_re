import pandas as pd
import os



def concat_csv(path):
    files = os.listdir(path)
    num_files = len(files)
    obj_file = os.path.join(path, files[0])
    result = pd.read_csv(obj_file)
    print(len(files))


    for i in range(1, num_files):
        print(files[i])
        obj_file = os.path.join(path, files[i])
        file = pd.read_csv(obj_file)
        result = pd.concat([result, file])
    result = result.rename(columns={"Unnamed: 0":"date"})
    print(result)
    return result.sort_values(by="date")

# obj_file0 = os.path.join(path, files[0])
# obj_file1 = os.path.join(path, files[1])
# file0 = pd.read_csv(obj_file0)
# file1 = pd.read_csv(obj_file1)
#
# data1 = pd.concat([file1, file0])
# data1 = data1.sort_values(by='index')
if __name__ == '__main__':
    path = r"C:\Users\lyq92\Desktop\DataAnalyse\to_all0-100\1"
    # for i in range(2016, 2019):
    #     file_path = path + '\\' + str(i) + 'yearflow.csv'
    #     file = concat_csv(file_path)
    #     file = file.sort_values(by='index')
    #     file.to_csv(file_path+'\\' + 'yearflow.csv')
    file = concat_csv(path)
    # file = file.sort_values(by='index')
    file.to_csv(path + '\\'+ '1tot.csv')
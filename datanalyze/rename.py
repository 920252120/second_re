import pandas as pd
import os
import re

path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\allinone'
to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100\allinone2'

files = os.listdir(path)
num_files = len(files)

pat = "(\d+).csv"
patten = re.compile(pat)


for i in range(num_files):

    matchobj = re.search(patten, files[i])
    if matchobj:
        obj_file = os.path.join(path, files[i])

        result = pd.read_csv(obj_file, index_col="date")
        # result = result.rename(columns={"flow": matchobj.group(1)})
        # result = result.drop('Unnamed: 0', axis=1)
        # result.to_csv(path + "\\" + matchobj.group(1)+".csv", index=True,index_label="date")
        result.to_csv(to_path + "\\" +files[i], index=True,index_label="date")


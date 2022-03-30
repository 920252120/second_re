import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


path = r'C:\Users\LYQ\Desktop\datanalyze\stationInfo(1).xml'

pat = r'station\sNo="(\d+)"\stheuser="(.*?)"\sstyle="(.*?)"'
patten = re.compile(pat)

data = pd.DataFrame(columns=['No', 'theuser', 'style'],index=range(1,256))

# data.append({'No':'1',
#              'theuser':'h',
#              'style':'1'}, ignore_index=True)
data.iloc[0]={'No':'1',
              'theuser':'h',
              'style':'1'}

with open(path, encoding='utf-8') as f:
    xml = f.readlines()
    for i in range(1,256):
        matchgroup = re.search(patten, xml[i+1])
        no = matchgroup.group(1)
        theuser = matchgroup.group(2)
        style = matchgroup.group(3)
        data.iloc[i-1] = {'No': no,
                        'theuser': theuser,
                        'style': style}
print(data)
data.to_csv(r'C:\Users\LYQ\Desktop\datanalyze\station.csv')
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

path = r'C:\Users\LYQ\Desktop\datanalyze\test\years\2015-2019tot.csv'

data = pd.read_csv(path, parse_dates=True)

data = data[['index','1']]

# fig = plt.figure(sharey)
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
# ax1.plot(data['1'][:800])
# ax2.plot(data['1'][800:])

fig, axes = plt.subplots(2,1, sharey=True)

props = {
    'title': 'first_800d',
    'xlabel': 'days',
    'ylabel': 'heat'
}
axes[0].set(**props)
axes[1].set(**props)

axes[0].plot(data['1'])
axes[0].set_xlim(['3/1/2015', '7/31/2019'])

# axes[1].plot(data['1'][800:])

plt.show()
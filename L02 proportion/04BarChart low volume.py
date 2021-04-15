import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)

selected = ['TAP', 'ZMS', 'XSV', 'CNQ', 'WYG', 'BTB', 'YGY', 'TSE', 'DZT', 'VSM', 'WGR', 'EFN', 'ATT', 'DTJ', 'NMO', 'BZM', 'VYZ', 'WMB', 'UMU', 'UGJ', 'CFG', 'ENY', 'XML', 'AEI']
print(data[selected].head())

# data[selected].sum().plot.bar(width=0.8, rot=0, figsize=(8, 8))
plt.figure(figsize=(8, 8))
x_pos = np.arange(len(data[selected].columns))
plt.bar(x_pos, data[selected].sum(), align='center')
plt.xticks(x_pos, data[selected].columns)
plt.xlabel('Stores', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Low Volume Customer Visits', fontsize=20)
plt.show()

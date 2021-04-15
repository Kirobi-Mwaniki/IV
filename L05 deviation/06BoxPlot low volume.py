import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())

selected = ['TAP', 'ZMS', 'XSV', 'CNQ', 'WYG', 'BTB', 'YGY', 'TSE', 'DZT', 'VSM', 'WGR', 'EFN', 'ATT', 'DTJ', 'NMO', 'BZM', 'VYZ', 'WMB', 'UMU', 'UGJ', 'CFG', 'ENY', 'XML', 'AEI']

plt.figure(figsize=(8, 8))
# data[selected].boxplot()
plt.boxplot(data[selected].transpose(), labels=selected)
plt.xlabel('Product', fontsize=18)
plt.ylabel('Customer visits per day', fontsize=18)
plt.title('Low volume Customer Visits distributions', fontsize=20)
plt.show()

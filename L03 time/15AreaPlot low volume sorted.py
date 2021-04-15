import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())

# sort the data according to the sum of each column
data = data.reindex(data.sum().sort_values(ascending=False).index, axis=1)
print(data.head())

selected = ['TAP', 'ZMS', 'XSV', 'CNQ', 'WYG', 'BTB', 'YGY', 'TSE', 'DZT', 'VSM', 'WGR', 'EFN', 'ATT', 'DTJ', 'NMO', 'BZM', 'VYZ', 'WMB', 'UMU', 'UGJ', 'CFG', 'ENY', 'XML', 'AEI']

plt.figure(figsize=(8, 8))
# data.plot.area(figsize=(8, 8))
plt.stackplot(data.index, data[selected].transpose())
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Stacked Low Volume Customer Visits', fontsize=20)
plt.legend(selected, loc=2)
plt.show()

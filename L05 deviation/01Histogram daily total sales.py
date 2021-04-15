import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())
print(data.sum(axis=1))

x_min = 2000
x_max = 3500
bin_width = 50
n_bins = int((x_max - x_min) / bin_width)
print(str(n_bins) + ' bins')
bins = [(x_min + x * (x_max - x_min) / n_bins) for x in range(int(n_bins))]
# print(bins)

plt.figure(figsize=(8, 8))
# plt.hist(data.sum(), edgecolor='w')
plt.hist(data.sum(axis=1), bins=bins, edgecolor='w')
plt.title('Daily total sales distribution', fontsize=20)
plt.show()

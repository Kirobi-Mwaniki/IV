import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())

selected = ['ZSD', 'MAJ', 'YYO', 'NGB']

plt.figure(figsize=(8, 8))
# data[selected].boxplot()
plt.boxplot(data[selected].transpose(), labels=selected)
plt.xlabel('Product', fontsize=18)
plt.ylabel('Customer visits per day', fontsize=18)
plt.title('Very low volume Customer Visits distributions', fontsize=20)
plt.show()

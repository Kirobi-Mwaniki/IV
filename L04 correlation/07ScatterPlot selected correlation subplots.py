import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())

selected = ['H', 'M', 'O']

counter = 1
fig = plt.figure(figsize=(8, 8))
fig.suptitle('Customer Visits correlations', fontsize=20, position=(0.5, 1.0))
for i, name_i in enumerate(selected):
    for j in range(i + 1, len(selected)):
        name_j = selected[j]
        sub = fig.add_subplot(2, 2, counter)
        sub.set_title(name_i + ' vs ' + name_j, fontsize=16)
        sub.scatter(data[name_i], data[name_j], s=5)
        counter += 1
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.tight_layout()
plt.show()

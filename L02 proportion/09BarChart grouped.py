import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)

selected = []
columns = data.columns
data['Others'] = [0] * len(data.index)
for name in columns:
    total_sales = data[name].sum()
    if total_sales > 10000:
        selected.append(name)
    else:
        data['Others'] += data[name]
selected.append('Others')
print(data[selected].head())

plt.figure(figsize=(8, 8))
x_pos = np.arange(len(selected))
plt.bar(x_pos, data[selected].sum(), align='center')
plt.xticks(x_pos, selected)
plt.xlabel('Stores', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Total Customer Visits', fontsize=20)
plt.show()

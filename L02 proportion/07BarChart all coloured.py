import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)

colours = []
for name in data.columns:
    total_sales = data[name].sum()
    if total_sales > 300000:
        colour = 'green'
    elif total_sales > 50000:
        colour = 'orange'
    elif total_sales > 10000:
        colour = 'red'
    else:
        colour = 'black'
    colours.append(colour)

plt.figure(figsize=(8, 8))
x_pos = np.arange(len(data.columns))
plt.bar(x_pos, data.sum(), align='center', color=colours)
plt.xticks(x_pos, data.columns)
plt.xlabel('Stores', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Total Customer Visits', fontsize=20)
plt.show()

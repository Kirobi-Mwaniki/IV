import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
print(data.head())

colours = []
for name in data.columns:
    total_sales = data[name].sum()
    colour = ''
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
plt.pie(data.sum(), labels=data.columns, colors=colours)
plt.title('Total Customer Visits', fontsize=20)
plt.legend(loc=2)
plt.show()

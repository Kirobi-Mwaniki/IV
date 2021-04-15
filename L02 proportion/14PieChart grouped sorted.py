import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
print(data.head())

# sort the data according to the sum of each column
data = data.reindex(data.sum().sort_values(ascending=False).index, axis=1)
print(data.head())

explodeList = []
selected = []
columns = data.columns
data['Others'] = [0] * len(data.index)
for name in columns:
    total_sales = data[name].sum()
    if total_sales > 10000:
        selected.append(name)
        explodeList.append(0)
    else:
        data['Others'] += data[name]
selected.append('Others')
explodeList.append(0.05)
print(data[selected].head())

plt.figure(figsize=(8, 8))
plt.pie(data[selected].sum(), labels=selected, autopct='%1.1f%%', startangle=90, explode=explodeList)
plt.title('Total Customer Visits', fontsize=20)
plt.legend(loc=2)
plt.show()

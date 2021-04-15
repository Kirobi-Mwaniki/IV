import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
data.index = pd.to_datetime(data.index)
print(data.head())

selected = ['QSN', 'SGA', 'SMM', 'RAH' ]

data = data[selected]
print(data.head())

data['Average'] = data.mean(axis=1)
print(data.head())

data.plot.line()
plt.show()



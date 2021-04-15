import matplotlib.pyplot as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
data.index = pd.to_datetime(data.index)
print(data.head())

selected = ['QSN', 'SGA', 'SMM', 'RAH' ]
data = data[selected]

data = data.loc[pd.to_datetime('2019-10-01'): pd.to_datetime('2019-12-31')]
print(data.head())

data.plot.line()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
print(data.head())

# data.plot.line(linewidth=0.5, figsize=(8, 8))
plt.figure(figsize=(8, 8))
plt.plot(data, linewidth=0.5)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Customer Visits', fontsize=20)
plt.legend(data.columns, loc=2)
plt.show()

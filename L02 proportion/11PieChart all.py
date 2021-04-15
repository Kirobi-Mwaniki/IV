import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
print(data.head())

plt.figure(figsize=(8, 8))
plt.pie(data.sum(), labels=data.columns)
plt.title('Total Customer Visits', fontsize=20)
plt.legend(loc=2)
plt.show()

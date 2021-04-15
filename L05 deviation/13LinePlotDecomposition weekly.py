import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)

selected = ['H', 'M', 'O']

for name in selected:
    result = seasonal_decompose(data[name], model='multiplicative', freq=7)
    result.plot()
    plt.suptitle('Product ' + name, position=(0.5, 1.0))
    plt.show()

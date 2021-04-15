import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)

period = 7
rolling_average = data.rolling(window=period).mean()

selected = ['OSG', 'PAA', 'NAQ', 'MUY', 'RGS', 'QMD', 'PGL', 'OMV']
print(data[selected].head())

plt.figure(figsize=(8, 8))
plt.plot(data[selected], linewidth=0.5)
plt.gca().set_prop_cycle(None)
plt.plot(rolling_average[selected], linewidth=2)
# plt.ylim(ymin=0)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Customer visits', fontsize=18)
plt.title('Medium Volume Customer Visits\n with 7-day Rolling Average', fontsize=20)
plt.legend(selected, loc=2)
plt.show()

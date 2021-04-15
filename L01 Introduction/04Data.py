import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
data.index = pd.to_datetime(data.index)

print(data)
print(data.head())
print(data.tail())
print(data.describe())
print(data.sum())

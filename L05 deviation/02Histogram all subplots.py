import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)

counter = 1
fig = plt.figure(figsize=(8, 8))
fig.suptitle('Customer Visits distributions', fontsize=20, position=(0.5, 1.0))
for name in data:
    sub = fig.add_subplot(5, 5, counter)
    sub.set_title('Product ' + name, fontsize=10)
    sub.hist(data[name], edgecolor='w')
    counter += 1
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()

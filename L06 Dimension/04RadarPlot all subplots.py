import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
print(data.head())

marketing_data = pd.read_csv('https://tinyurl.com/ChrisCoDV/Stores/MarketingPerProduct.csv', index_col=0)
price_per_unit = pd.read_csv('https://tinyurl.com/ChrisCoDV/Stores/PricePerUnit.csv', index_col=0)
profit_per_unit = pd.read_csv('https://tinyurl.com/ChrisCoDV/Stores/ProfitPerUnit.csv', index_col=0)

summary_data = pd.DataFrame(index=data.columns)
summary_data['Price'] = price_per_unit.values
summary_data['Profit'] = profit_per_unit.values
summary_data['Sales'] = data.sum().values
summary_data['Marketing'] = marketing_data.values
summary_data['Cost'] = summary_data['Price'] - summary_data['Profit']
print(summary_data.head())
print(summary_data.describe())

normalised_data = summary_data / summary_data.max()
print(normalised_data.head())

n_attributes = len(summary_data.columns)
angles = [n / float(n_attributes) * 2 * np.pi for n in range(n_attributes + 1)]
plt.figure(figsize=(8, 8))
counter = 1
for name in normalised_data.index:
    # values = normalised_data.transpose()[name].values.flatten().tolist()
    values = normalised_data.loc[[name]].values.flatten().tolist()
    values += values[:1]
    sub = plt.subplot(5, 5, counter, polar=True)
    sub.plot(angles, values)
    sub.set_ylim(ymax=1.05)
    sub.set_yticks([])
    sub.set_xticks(angles)
    sub.set_xticklabels(normalised_data.columns, fontsize=8)
    sub.set_title(name, fontsize=8, loc='left')
    counter += 1
plt.tight_layout()
plt.show()

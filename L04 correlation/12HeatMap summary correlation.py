import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
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

plt.figure(figsize=(8, 8))
corr = summary_data.corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=200), square=True, annot=True,
                 annot_kws={"size": 8})
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


-------------------------------


#Heatmap code for Summary data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('https://tinyurl.com/ChrisCoNorth/bannerid/DailyCustomers.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)
#print(data.head())

StoreMarketing = pd.read_csv('https://tinyurl.com/ChrisCoNorth/bannerid/StoreMarketing.csv', index_col=0)
StoreOverheads = pd.read_csv('https://tinyurl.com/ChrisCoNorth/bannerid/StoreOverheads.csv', index_col=0)
StoreSize = pd.read_csv('https://tinyurl.com/ChrisCoNorth/bannerid/StoreSize.csv', index_col=0)
StoreStaff = pd.read_csv('https://tinyurl.com/ChrisCoNorth/bannerid/StoreStaff.csv', index_col=0)

summary_data = pd.DataFrame(index=data.columns)
summary_data['Store_Overheads'] = StoreOverheads.values
summary_data['Store_Size'] = StoreSize.values
summary_data['Store_Staff'] = StoreStaff.values
summary_data['Store_Marketing'] = StoreMarketing.values
summary_data['Store_Customers_Visits'] = data.sum().values


plt.figure(figsize=(8, 8))
corr = summary_data.corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=200), square=True, annot=True,
                 annot_kws={"size": 8})
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.title('Heatmap visualizing Summary Data', fontsize=20)
plt.show()
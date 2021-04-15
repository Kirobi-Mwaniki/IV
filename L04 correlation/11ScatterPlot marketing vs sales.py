import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
print(summary_data.describe())

plt.figure(figsize=(8, 8))
plt.scatter(summary_data['Marketing'], summary_data['Sales'])
plt.title('Marketing spend vs Sales', fontsize=20)
plt.xlabel('Marketing spend (£)', fontsize=18)
plt.ylabel('Sales', fontsize=18)
plt.show()


------------------

#summary data code for store marketing vs Customers_Visits(scatterplot)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
#summary_data['Cost'] = summary_data['Price'] - summary_data['Profit']
#print(summary_data.head())
#print(summary_data.describe())

plt.figure(figsize=(8, 8))
plt.scatter(summary_data['Store_Marketing'], summary_data['Store_Customers_Visits'])


#z = np.polyfit(summary_data['Store_Marketing'], summary_data['Store_Customers_Visits'], 1)
#trend = np.poly1d(z)
#plt.plot(summary_data['Store_Customers_Visits'], trend(summary_data['Store_Customers_Visits']))


plt.title('Store_Marketing vs Store_Customers_Visits', fontsize=20)
plt.xlabel('Store_Marketing', fontsize=18)
plt.ylabel('Store_Customers_Visits', fontsize=18)
plt.show()
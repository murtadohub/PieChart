import pandas as pd 
import matplotlib.pyplot as plt
import datetime

#membaca file
dataset = pd.read_csv('data.csv')
#Buat kolom baru yg bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
#Buat kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# dataset.groupby(['order_month','province'])['gmv'].sum().unstack().plot(cmap='Set1')
#membuat data frame
dataset_dki_q4 = dataset[(dataset['province']=='DKI Jakarta') & (dataset['order_month'] >= '2019-10')]
print(dataset_dki_q4.head())
# membuat pie chart
gmv_per_city_dki_q4 = dataset_dki_q4.groupby('city')['gmv'].sum().reset_index()
plt.figure(figsize=(6,6))
plt.pie(gmv_per_city_dki_q4['gmv'], labels = gmv_per_city_dki_q4['city'], autopct='%1.2f%%')
plt.title('GMV Kontribusi Jakarta per Kota - DKI Jakarta di Q4 2019', loc='center', pad=30, fontsize=15, color='blue')
plt.show()


import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
products = pd.read_csv('products.csv', sep=',', encoding='utf-8')
shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
cars = pd.read_csv('cars.csv', sep=',', encoding='utf-8')




# print(orders[4:10]) # lines from 4 to 9 
# print(orders.loc[4:10]) # lines from 4 to 10. loc takes index of the line not from 0
# print(orders.iloc[4:10]) # lines from 4 to 9 

# mask = products['category' == 'Essential oil']
# print(products.loc[mask, 'category':'volume_ml'].head(3)) #filters lines with mask, than columns


# Задача: Вывести заказы 2023 года, где сумма (total) превышает 8000

# print(shop.info())
# order_date, total

# shop["order_date"] = pd.to_datetime(shop["order_date"], errors='coerce')
# # mask = shop.loc[(shop['order_date'] >= '2023-01-01') & (shop['order_date'] <= '2023-12-31') & (shop['total'] > 8000)]

# mask = shop.loc[(shop['order_date'].dt.year==2023) & (shop['total'] > 8000)]
# print(mask['order_id'].count())


# Задача: Вывести строки с 5-й по 14-ю включительно (то есть индексы 5–14) с помощью .iloc[] для customer_id

# print(customers.iloc[5:15]['customer_id'])


# Задача: Найти клиентов, которые не зарегистрировались в 2023 году. Столбцы: customer_id, registration_date.

# shop["registration_date"] = pd.to_datetime(shop["registration_date"], errors='coerce')
# mask = shop.loc[shop['registration_date'].dt.year != 2023]
# print(mask[['customer_id', 'registration_date']].count())


# Задача: Вывести товары с volume_ml == 5.0 из строк с индексами от 20 до 30. Столбцы: product_name, volume_ml.

# lines = products.iloc[20:31]
# filter_vol = lines.loc[lines['volume_ml'] == 5.0]
# print(filter_vol[['product_name', 'volume_ml']])

#Query:
# filter_1 = shop.query('country == "Russia" and category == "Absolute"')['order_id']
# filter_2 = shop.query(' 5 <= index <= 8')[['product_name', 'price']]


# print(shop[['product_name', 'price']].head())
# print(shop[['product_name', 'price']].duplicated().head())
# print(shop[['product_name', 'price']].duplicated().sum()) #false=0, true=1

#Deleting duplicates
# customer = shop.loc[:, 'customer_id':'contanct_information'].drop_duplicates
# print(len(customer))



#Uniqe
# print(shop['category'].sort_values().unique())
# product = shop.loc[:,'product_id':'volume_ml'].drop_duplicates()
# print(product['category'].value_counts(normalize=True))


#Задачв Вывести заказы 2023 года с total > 10 000 через query(). Выведите 10 строк
# shop["order_date"] = pd.to_datetime(shop["order_date"], errors='coerce')
# query_1 = shop.query("order_date.dt.year == 2023 and total > 10000")[['order_id', 'total','order_date']].head(10)
# print(query_1)

#Вывести продукты категории "Absolute" и объёмом 2.5 мл через query() и с drop_duplicates()
# query_2 = shop.query('category == "Absolute" and volume_ml == 2.5')
# print(query_2[['product_name', 'volume_ml', 'category']].drop_duplicates())


#Strings
# product = shop.loc[:, 'product_id':'volume_ml'].drop_duplicates()
# shop['category'] = shop['category'].str.lower().str.strip().str.replace(' ', '_')
# print(shop['category'].unique())


#File cars
# print(cars.dtypes)
# print(cars.head(5))
# print(cars.info())

#2. Изучите уникальные значения в столбцах с названием бренда автомобиля и цвета. 
# Устраните неявные дубликаты и некорректные значения. 
# Например, для колонки brand значения «BMV» и «bmv» – это одно и то же значение.

cars['brand'] = cars['brand'].str.lower().str.strip().replace({'bmv':'bmw'})
cars['color'] = cars['color'].str.lower().str.strip()
# print(cars.count())

# duplicates = cars[cars.duplicated()]
# # print(len(duplicates))
# cars = cars.drop_duplicates()
# print(cars.count())

#4. Определите спрос на бренды автомобилей. Рассчитайте долю покупок каждого бренда среди всех заказов, представленных в данных. 
# Затем для данного бренда определите самую популярную модель.

brand = cars['brand'].value_counts(normalize=True) * 100
# print(brand.round(2))


#5. Определите топ три самых популярных цвета у покупателей.
color = cars['color'].value_counts(normalize=True) * 100
# print(color.head(3))


#6. Создайте переменную filtered_orders. Занесите в нее датафрейм, который содержит только те заказы, 
# в которых бренд автомобиля BMW представлен в холодных тонах.
#Посчитайте количество таких заказов. (Если все шаги до этого выполнены верно, то должно получиться 28 заказов)

cold_colors = ['blue', 'grey']
filtered_orders = cars[(cars['brand'] == 'bmw') & (cars['color'].isin(cold_colors))]
print(len(filtered_orders))
print(filtered_orders.head(28))
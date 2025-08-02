import pandas as pd

print("Домашнее задание № 3")


# Задание 1. Выполните фильтрацию с помощью [ ], .loc[]	и .query().
# Объедините таблицы contacts, customers, orders. Будьте внимательны, не все пользователи
# делали заказы. Отберите все записи о продажах пользователей из европеийских стран
# и России,	совершенных в первые два квартала 2023 года. Оставьте поля order_id
# и total. Определите сумму отобранных продаж.

print('Задача №1')

contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_df = orders.merge(customers, on='customer_id', 
                         how='inner').merge(contacts, on='customer_id', how='inner')
merged_df["order_date"] = pd.to_datetime(merged_df["order_date"], errors='coerce')
desired_countries = ["Italy", "Spain", "UK", "France", "Germany", "Russia"]


filter_1 = merged_df[(merged_df['country'].isin(desired_countries)) 
                     & (merged_df['order_date'] >= "2023-01-01") & (merged_df['order_date'] <= "2023-06-30")]
print(filter_1[['total', 'order_id']])
print(f"Total sum = {filter_1['total'].sum()}")


filter_loc = merged_df.loc[(merged_df['order_date'].dt.year == 2023) & (merged_df['order_date'].dt.month <=6) 
                           & (merged_df['country'].isin(desired_countries))]
print(filter_loc[['total', 'order_id']])
print(f"Total sum = {filter_loc['total'].sum()}")


filter_query = merged_df.query('country in @desired_countries and order_date.dt.year == 2023 and order_date.dt.quarter <= 2')
print(filter_query[['total', 'order_id']])
print(f"Total sum = {filter_query['total'].sum()}")

# Задание 2. Выполните фильтрацию с	помощью	.query().
# Отберите все записи продаж пользователей, прошедших регистрацию начиная с 2022 года
# и совершивших	заказы в 2023 году на сумму	более 30000 руб. Оставьте поля с ФИО и total.	ПодсчитаиS те	количество	таких	продаж.


print('Задача №2')

contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_df_2 = orders.merge(customers, on='customer_id', 
                         how='inner').merge(contacts, on='customer_id', how='inner')
merged_df_2["order_date"] = pd.to_datetime(merged_df_2["order_date"], errors='coerce')
merged_df_2["registration_date"] = pd.to_datetime(merged_df_2["registration_date"], errors='coerce')


query_2 = merged_df_2.query('registration_date.dt.year >= 2022 and order_date.dt.year == 2023 and total > 30000')
print(query_2[['first_name', 'last_name','total']])
print(f"Количество продаж: {len(query_2)}")


# Задание 3. Методом value_counts()	подсчитайте	сколько	заказов	в период 2022-2023 годов 
# было осуществлено пользователями мужского пола и сколько пользователями женского пола.


print('Задача №3')

customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_df_3 = orders.merge(customers, on='customer_id', how='inner')
merged_df_3["order_date"] = pd.to_datetime(merged_df_3["order_date"], errors='coerce')


filter_3 = merged_df_3.query('gender in ["M", "F"] and 2022 <= order_date.dt.year <= 2023')
print(filter_3['gender'].value_counts())

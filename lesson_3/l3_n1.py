import pandas as pd

"""Задание 1. Выполните фильтрацию с помощью [ ], .loc[]	и .query().
Объедините таблицы contacts, customers, orders. Будьте внимательны, не все пользователи
делали заказы. Отберите все записи о продажах пользователей из европеийских стран
и России,	совершенных в первые два квартала 2023 года. Оставьте поля order_id
и total. Определите сумму отобранных продаж."""

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
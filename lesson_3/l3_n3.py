import pandas as pd

"""Задание 3. Методом value_counts()	подсчитайте	сколько	заказов	в период 2022-2023 годов 
было осуществлено пользователями мужского пола и сколько пользователями женского пола."""

customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_df_3 = orders.merge(customers, on='customer_id', how='inner')
merged_df_3["order_date"] = pd.to_datetime(merged_df_3["order_date"], errors='coerce')


filter_3 = merged_df_3.query('gender in ["M", "F"] and 2022 <= order_date.dt.year <= 2023')
print(filter_3['gender'].value_counts())
import pandas as pd
"""Задание 1
Используйте файл group_orders.csv. Посчитайте общее количество заказов в каждом
городе."""

group_orders = pd.read_csv('group_orders.csv')
group_orders_city = group_orders.groupby('city')['order_id'].count().reset_index(name='total_orders')
print(group_orders_city)
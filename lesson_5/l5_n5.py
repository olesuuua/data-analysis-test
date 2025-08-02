import pandas as pd

"""Задание 5: Найдите пользователей, сделавших более 1 заказа, и выведите их имена и
количество заказов."""

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

df = orders.merge(users, on='user_id', how='inner')

mask_group = df.groupby('name')['user_id'].count().reset_index(name='order_count')
print(mask_group[mask_group['order_count'] > 1])
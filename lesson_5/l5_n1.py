import pandas as pd

"""Задание 1: Найдите всех пользователей из региона North, возраст которых младше 30, и
определите общее количество заказов, сделанных ими."""

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

df = orders.merge(users, on='user_id', how='inner')

mask_reg = df.loc[(df['region'] == "North") & (df['age'] < 30)]
print(mask_reg['name'].value_counts().reset_index(name='order_count'))
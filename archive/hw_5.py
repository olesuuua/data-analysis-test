
import pandas as pd

"""Задание 1: Найдите всех пользователей из региона North, возраст которых младше 30, и
определите общее количество заказов, сделанных ими."""

print('Задача №1')
users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

df = orders.merge(users, on='user_id', how='inner')

mask_reg = df.loc[(df['region'] == "North") & (df['age'] < 30)]
print(mask_reg['name'].value_counts().reset_index(name='order_count'))


"""Задание 2: Вывести все заказы на продукт "C" с суммой больше 250. Использовать query и
арифметику"""

print('Задача №2')

orders['total'] = orders['price'] * orders['quantity']
mask_query = orders.query('product == "C" and total > 250')
print(mask_query)


"""Задание 3: Посчитайте, сколько раз каждый продукт заказывался. Используйте
value_counts."""

print('Задача №3')

mask_vc = orders['product'].value_counts().reset_index(name='order_count')
print(mask_vc)


"""Задание 4: Постройте сводную таблицу, где по строкам — region, по столбцам — product, а
значения — общая сумма заказов (цена × количество)."""

print('Задача №4')

df['total'] = df['price'] * df['quantity']
mask_table = df.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(mask_table)


"""Задание 5: Найдите пользователей, сделавших более 1 заказа, и выведите их имена и
количество заказов."""

print('Задача №5')

mask_group = df.groupby('name')['user_id'].count().reset_index(name='order_count')
print(mask_group[mask_group['order_count'] > 1])


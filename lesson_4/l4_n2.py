import pandas as pd
"""Задание 2
Найдите среднюю сумму заказа по каждому городу."""
group_orders = pd.read_csv('group_orders.csv')
group_orders_mean = group_orders.groupby('city')['total'].mean().reset_index(name='mean_total')
print(group_orders_mean)
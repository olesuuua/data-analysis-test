import pandas as pd

"""Задание 5
Выведите топ-3 города с самой высокой средней стоимостью одного заказа (total)."""

group_orders = pd.read_csv('group_orders.csv')
group_orders_mean = group_orders.groupby('city')['total'].mean().reset_index(name='mean_total')
print(group_orders_mean.sort_values('mean_total', ascending=False).head(3))
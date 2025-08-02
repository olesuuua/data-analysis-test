import pandas as pd


"""Задание 3
Определите, какой товар продавался в наибольшем количестве (по сумме quantity)."""

group_orders = pd.read_csv('group_orders.csv')
group_orders_most = group_orders.groupby('product')['quantity'].sum().reset_index(name='sum_quantity')
print(group_orders_most.sort_values('sum_quantity', ascending=False, ignore_index=True).head(1))

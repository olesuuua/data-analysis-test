import pandas as pd

"""Задание 4
Сгруппируйте данные по месяцу заказа и найдите общую выручку в каждом месяце."""

group_orders = pd.read_csv('group_orders.csv')
group_orders['order_month'] = pd.to_datetime(group_orders['order_date'], errors='coerce').dt.strftime('%Y-%m')
group_orders_month = group_orders.groupby('order_month')['total'].sum().reset_index(name='month_total')
print(group_orders_month)
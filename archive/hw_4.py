import pandas as pd
"""Задание 1
Используйте файл group_orders.csv. Посчитайте общее количество заказов в каждом
городе."""

print('Задача №1')
group_orders = pd.read_csv('group_orders.csv')
group_orders_city = group_orders.groupby('city')['order_id'].count().reset_index(name='total_orders')
print(group_orders_city)

"""Задание 2
Найдите среднюю сумму заказа по каждому городу."""

print('Задача №2')
group_orders_mean = group_orders.groupby('city')['total'].mean().reset_index(name='mean_total')
print(group_orders_mean)

"""Задание 3
Определите, какой товар продавался в наибольшем количестве (по сумме quantity)."""

print('Задача №3')
group_orders_most = group_orders.groupby('product')['quantity'].sum().reset_index(name='sum_quantity')
print(group_orders_most.sort_values('sum_quantity', ascending=False, ignore_index=True).head(1))

"""Задание 4
Сгруппируйте данные по месяцу заказа и найдите общую выручку в каждом месяце."""

print('Задача №4')
group_orders['order_month'] = pd.to_datetime(group_orders['order_date'], errors='coerce').dt.strftime('%B')
group_orders_month = group_orders.groupby('order_month')['total'].sum().reset_index(name='month_total')
print(group_orders_month)

"""Задание 5
Выведите топ-3 города с самой высокой средней стоимостью одного заказа (total)."""

print('Задача №5')
print(group_orders_mean.sort_values('mean_total', ascending=False).head(3))
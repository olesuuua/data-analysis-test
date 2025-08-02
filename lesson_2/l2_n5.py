import pandas as pd


"""Задача_5: Выведите заказы клиентов с ID от 10 до 20 включительно, у которых сумма заказа больше 8000.
Покажите order_id, customer_id и сумму."""
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_ord = orders[(orders['customer_id'] >= 10) & (orders['customer_id'] <= 20) & (orders['total'] > 8000)]
print(filter_ord[['order_id', 'customer_id', 'total']])
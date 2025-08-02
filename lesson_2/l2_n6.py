import pandas as pd


"""Задача_6: Выгрузите номера заказов с суммой от 10 000 до 15 000 рублей, сделанных в 2023 году."""
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_id = orders[(orders['total'] > 10000) & (orders['total'] < 15000) & (orders['order_date'] >= '2023-01-01') & (orders['order_date'] <= '2023-12-31')]
print(filter_id[['order_id', 'total', 'order_date']])

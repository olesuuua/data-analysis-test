import pandas as pd



"""Задача_8: Найдите заказы за февраль 2023 года, где сумма заказа > 5000."""
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_feb = orders[(orders['total'] > 5000) & (orders['order_date'] >= '2023-02-01') & (orders['order_date'] <= '2023-02-29')]
print(filter_feb[['order_id', 'total', 'order_date']])
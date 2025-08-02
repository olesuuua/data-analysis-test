import pandas as pd

"""Задача_1: Выгрузите номера всех заказов из файла orders, у которых стоимость заказа находится в диапазоне от 30 тыс. 
до 40 тыс. включительно и при этом заказы выполнены начиная с 1 января 2023 года."""
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_ord = orders[((orders['total']>=30000) & (orders['total']<=40000))]
filter_ord = filter_ord[filter_ord['order_date'] >= '2023-01-01']
print(filter_ord[['order_id']])
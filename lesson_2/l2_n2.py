import pandas as pd

"""Задача_2: Известно, что пользователи из России имеют id с 68 по 88. Отберите заказы пользователей 
из России за 2022 год. Из полученной выборки отобразите
только записи с 5 по 10 включительно и столбцы с номером заказа и суммой заказа"""
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_orders = orders[(orders['customer_id'] >= 68) & (orders['customer_id'] <= 88)]
filter_orders = filter_orders[(filter_orders['order_date'] >= '2022-01-01') &
                               (filter_orders['order_date'] <= '2022-12-31')]
filtr = filter_orders.head(11).tail(6)
print(filtr[['order_id', 'total']])

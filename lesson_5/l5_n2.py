import pandas as pd

"""Задание 2: Вывести все заказы на продукт "C" с суммой больше 250. Использовать query и
арифметику"""

orders = pd.read_csv('orders_new.csv')

orders['total'] = orders['price'] * orders['quantity']
mask_query = orders.query('product == "C" and total > 250')
print(mask_query)
import pandas as pd


"""Задание 3: Посчитайте, сколько раз каждый продукт заказывался. Используйте
value_counts."""
orders = pd.read_csv('orders_new.csv')
mask_vc = orders['product'].value_counts().reset_index(name='order_count')
print(mask_vc)

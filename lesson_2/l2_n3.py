import pandas as pd


"""Задача_3: Отобразите продукты, которые стоят меньше 500 руб. и имеют объём
5.0 мл.Выведите название и цену."""
products = pd.read_csv('products.csv', sep=',', encoding='utf-8')
print(products.head())
filter_prod = products[(products['price'] < 500) & (products['volume_ml'] == 5)]
print(filter_prod [['product_name', 'price']])
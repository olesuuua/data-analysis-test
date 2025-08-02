import pandas as pd

#Один из способов создания дата-фрейма
# data_countries = [["Russia", "Moscow"], ["China", "Pekin"], ]
# data = pd.DataFrame(data_countries, columns=["Countries", "Capitals"])
# print(data)


#Задание: Создайте свой собственный DataFrame из 3-х столбцов и 5 значение
# data_1 = pd.DataFrame({'Имя' : ['Иван', 'Алексей', 'Анна', 'Владимир', 'Петр'],  
#                        'Город' : ['Москва', 'Липецк', 'Воронеж', 'Москва', 'Владикавказ'], 
#                        'Возраст' : [23, 34, 17, 45, 34]})
# print(data_1)


#Задание: Примените к одному из файлов info(), shape(), tail(), sample(), len()
# customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
# print(customers.head(10))
# print('info:') 
# print(customers.info())
# print('shape:')
# print(customers.shape)
# print('tail:')
# print(customers.tail(10))
# print('sample:')
# print(customers.sample(3))
# print('len:')
# print(len(customers))


# Переименовка заголовков таблицы
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# customers_renamed = customers.rename(columns={'customer_id': 'id_klienta'})
# orders_renamed = orders.rename(columns={'customer_id': 'id_zakaza'})


# Задание: Объедините таблицы по customer_id. Объедините таблицы customers и orders, чтобы получить только тех клиентов, которые делали заказы (используйте how='inner').
# customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# merged = customers.merge(orders, on='customer_id', how='inner')
# print(merged)


# Фильтрация возможна по строкам и столбцам
# customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# shop_price = shop[['price.1']]
# shop_price_more_300 = shop[shop['price.1'] > 300]
# print(shop_price_more_300)
# print(orders)
# print(orders[['order_id', 'order_date']].head())
# print(orders.drop(columns=['order_id', 'order_date']).head()) #исключаем
# print(orders[9:19][['order_id', 'order_date']])
# orders["order_date"] = pd.to_datetime(orders["order_date"])


# Задача_1: Выгрузите номера всех заказов из файла orders, у которых стоимость заказа находится в диапазоне от 30 тыс. 
# до 40 тыс. включительно и при этом заказы выполнены начиная с 1 января 2023 года.
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# filter_ord = orders[((orders['total']>=30000) & (orders['total']<=40000))]
# filter_ord = filter_ord[filter_ord['order_date'] > '2023-01-01'] #сравнивает строку без проблем
# print(filter_ord[['order_id']])
# но может не сравнивать и тогда нужно преобразовывать тип данных:
# orders["order_date"] = pd.to_datetime(orders["order_date"], errors='coerce')
# filter_ord = orders[((orders['total']>=30000) & (orders['total']<=40000))]
# filter_ord = filter_ord[filter_ord['order_date'] >= '2023-01-01']
# print(filter_ord[['order_id']])



# Задача_2: Известно, что пользователи из России имеют id с 68 по 88. Отберите заказы пользователей 
# из России за 2022 год. Из полученной выборки отобразите
# только записи с 5 по 10 включительно и столбцы с номером заказа и суммой заказа.
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# filter_orders = orders[(orders['customer_id'] >= 68) & (orders['customer_id'] <= 88)]
# filter_orders = filter_orders[(filter_orders['order_date'] >= '2022-01-01') &
#                                (filter_orders['order_date'] <= '2022-12-31')]
# filtr = filter_orders.head(11).tail(6)
# print(filtr[['order_id', 'total']])


# Задача_3: Отобразите продукты, которые стоят меньше 500 руб. и имеют объём
# 5.0 мл.Выведите название и цену.
# products = pd.read_csv('products.csv', sep=',', encoding='utf-8')
# print(products.head())
# filter_prod = products[(products['price'] < 500) & (products['volume_ml'] == 5)]
# print(filter_prod [['product_name', 'price']])


# Задача_4: Найдите всех клиентов женского пола, которые родились до 1995 года.
# Выведите их customer_id, имя, фамилию и год рождения.
# customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
# print(customers.head())
# filter_cust = customers[(customers['gender'] == 'F') & (customers['birth_date'] < '1995-01-01')]
# print(filter_cust[['customer_id', 'first_name', 'last_name', 'birth_date']])


# Задача_5: Выведите заказы клиентов с ID от 10 до 20 включительно, у которых сумма заказа больше 8000.
# Покажите order_id, customer_id и сумму.
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# filter_ord = orders[(orders['customer_id'] >= 10) & (orders['customer_id'] <= 20) & (orders['total'] > 8000)]
# print(filter_ord[['order_id', 'customer_id', 'total']])


# Задача_6: Выгрузите номера заказов с суммой от 10 000 до 15 000 рублей, сделанных в 2023 году.
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# filter_id = orders[(orders['total'] > 10000) & (orders['total'] < 15000) & (orders['order_date'] >= '2023-01-01') & (orders['order_date'] <= '2023-12-31')]
# print(filter_id[['order_id', 'total', 'order_date']])


# Задача_7: Найдите заказы клиентов, родившихся в 1990 году. Выведите order_id и customer_id
# customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# merged = customers.merge(orders, on='customer_id', how='inner')
# filter_mrg = merged[(merged['birth_date'] >= '1990-01-01') & (merged['birth_date'] <= '1990-12-31')]
# print(filter_mrg[['order_id', 'customer_id']])


# Задача_8: Найдите заказы за февраль 2023 года, где сумма заказа > 5000.
# orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
# filter_feb = orders[(orders['total'] > 5000) & (orders['order_date'] >= '2023-02-01') & (orders['order_date'] <= '2023-02-29')]
# print(filter_feb[['order_id', 'total', 'order_date']])

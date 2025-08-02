import pandas as pd

"""Задача_4: Найдите всех клиентов женского пола, которые родились до 1995 года.
Выведите их customer_id, имя, фамилию и год рождения."""
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
print(customers.head())
filter_cust = customers[(customers['gender'] == 'F') & (customers['birth_date'] < '1995-01-01')]
print(filter_cust[['customer_id', 'first_name', 'last_name', 'birth_date']])

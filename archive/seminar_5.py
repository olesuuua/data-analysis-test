

import pandas as pd

#Сводные таблицы
# df = pd.read_csv('data_final.csv')

# data_pivot = df.pivot_table(index=['category_name', 'subcategory_name']
#                                    columns='source', values='visits', aggfunc='sum')


# data_pivot = df.pivot_table(index=['category_name', 'subcategory_name']
#                                    columns='source', values='visits', aggfunc='sum')

# data_pivot_reset_index = data_pivot.reset_index()

# print(data_pivot_reset_index.head(10))

#с использованием group by и agg

# data_grouped = df.groupby(['category_name', 'subcategory_name', 'source']).agg({'visits':'sum'})

# data_grouped['daily_visits'] = data_grouped['visits']/30

# print(data_grouped.head(10))



# df = pd.read_csv('data_final.csv')
# data_pivot = df.pivot_table(index=['category_name', 'subcategory_name'],
#                                    columns='source', values='visits', aggfunc='sum')

"""Создайте в таблице data_pivot новый столбец 'ratio' и сохраните в нём значение отношения 
органического трафика 'organic' к прямому 'direct'. Выведите первые 10 строк таблицы на экран."""

# data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

# print(data_pivot.head(10))
"""Отсортируйте таблицу по столбцу 'ratio' в порядке убывания. Выведите первые 10 строк.
Отсортированную таблицу сохранять не нужно."""

# print(data_pivot.sort_values(by='ratio', ascending=False).tail(10))

"""вывести последних 10 записей, где direct трафик больше 1000"""

# print(data_pivot[data_pivot['direct'] > 1000].sort_values(by='ratio', ascending=False).tail(10))

"""Задание 1
Создайте сводную таблицу, где:
строки — category_name и subcategory_name,
столбцы — source,
значения — сумма визитов (visits)."""

# df = pd.read_csv('shop_visits.csv')
# print(df.sample(3))
# data_pivot = df.pivot_table(index=['category_name', 'subcategory_name'], columns='source',
#                              values='visits', aggfunc='sum')
# print(data_pivot)

"""сделайте столбец ratio organic к direct"""

# data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']
# print(data_pivot.head(10))

"""избавимся от ads и отсортируем по ratio и direct больше 5000"""
# print(data_pivot[data_pivot['direct'] > 5000].drop(columns=['ads']).sort_values('ratio', ascending=False).head(10))

#Категоризация данных

# df = pd.read_csv('shop.csv')

# df.rename(columns={'phone': 'Телефон', 'address' : 'Адрес'}, inplace=True)
# print(df.info())


# orders = pd.read_csv('orders.csv')
# order_lines = pd.read_csv('order_lines.csv')
# merge = orders.merge(order_lines, on = 'order_id', how = 'left')
# print(merge.head(10))


# df = pd.read_csv('classified_people.csv')

# def classify_person(row):
#     if row['age'] < 18:
#         return "несовершеннослетние"
#     elif row['age'] > 65:
#         return "пенсионер"
#     elif row['gendre'] == "F":
#         return "женщина трудоспособного возраста"
#     else:
#         return "мужчина трудоспособного возраста"

# df['category'] = df.apply(classify_person, axis = 1)
# print(df)

# df = pd.read_csv('age_grouped_data.csv')

# def group(age):
#     if age < 18:
#         return 'до 18'
#     elif 18 < age < 65:
#         return 'от 18 до 65'
#     else:
#         return 'старше 65'
    
# df['age_group1'] = df['age'].apply(group)

# df = pd.read_csv('stats_by_age')
# print(df['age'].value_counts())
# def group(age):

#     if age <= 18:
#         return 'дети'
#     if age <= 64:
#         return 'взрослые'
#     else:
#         return "пенсионеры"
    
# df['age_group1'] = df['age'].apply(group)
# print(df['age_group1'].value_counts())


# def make_full_name(row):
#     """returs full name (firs and last)"""
#     full_name = row['first_name'] + " " + row['last_name']
#     return full_name

# df['full_name'] = df.apply(make_full_name, axis = 1)
# print(df.head(10))

# df = pd.read_csv('support_log.csv')
# print(df.info())
# print(df.head())

"""Сгруппируйте данные по типу события и посчитайте 
количество событий. Сохраните группировку с подсчётом в 
переменной support_log_grouped и выведите её на экран."""

# support_log_grouped = df.groupby(['type_id']).count()
# print(support_log_grouped)

"""Напишите функцию alert_group(messages) , которая оценивает приоритет в
зависимости от количества сообщений. Если параметр не более 300, 
она должна возвращать строку 'средний', если значение параметра от 
301 до 500 включительно, тогда строку 'высокий'. Для более высоких 
значений должна возвращаться строка 'критичный'.
Проверьте, что ваша функция отвечает верно, когда ей передают числа 10, 450, 
1000. Каждое значение выводите на новой строке."""


# def alert_group(messages):
#     if messages <= 300:
#         return 'средний'
#     elif messages <= 500:
#         return 'высокий'
#     else:
#         return 'критичный'

# print(alert_group(10))
# print(alert_group(450))
# print(alert_group(1000))

"""Добавьте к таблице support_log столбец 'alert_group', где хранятся результаты
 применения вашей функции alert_group().
Закомментируйте результаты предыдущего задания. Посмотрите верхние 10 строк 
support_log_grouped: убедитесь, что функция правильно расставила приоритеты."""

# support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group)

# print(support_log_grouped.head(10))

"""Посчитайте количество обращений по каждому приоритету и выведите результат на экран.
 Вывод от прошлых задач при необходимости закомментируйте."""

# print(support_log_grouped.groupby('alert_group')['user_id'].sum())


# support_req = pd.read_csv('support_requests.csv')
"""Сгруппируйте обращения по типу (type_id) и посчитайте количество каждого типа."""
# support_group = support_req.groupby('type_id')['user_id'].count().reset_index(name='count')
# print(support_group)

"""Напишите функцию priority_group(count), которая возвращает:
'низкий', если обращений ≤ 50;
'средний', если от 51 до 100;
'высокий' — если больше 100."""

# def priority_group(messages):
#     if messages <= 50:
#         return 'низкий'
#     elif messages <= 100:
#         return 'средний'
#     else:
#         return 'высокий'
    
"""Добавьте к таблице группировки столбец priority, содержащий категории приоритета."""

# support_group['priority'] = support_group['count'].apply(priority_group)
# print(support_group)

"""сколько всег сообщений приходится на каждый уровень приоритета"""

# support_group_count = support_group.groupby('priority')['count'].sum().reset_index(name='count_2')
# print(support_group_count)

"""отсортировать по кол-ву"""
# print(support_group_count.sort_values('count_2', ascending=False))


#Неупорядоченные коллекции

# grains = {'пшеница', 'рожь', 'овес', 'кукуруза', 
#           'рис', 10, ('ячмень', 'горох'), 'овес'}
# print(grains)

# empty = set()
# print("Empty содержит:", empty)

# vegetables = ['tomato', 'cucumber', 'eggplant']
# vegetables_price = [100, 50, 70, [30, 50]]
# vegetables_set = set(vegetables)
# print(vegetables_set)


# veg_price = {'tomato' : 100, 'cucumber' : 40, 'eggplant' : 30}
# print(set(veg_price))

# To delete object from set :remove/discard/poo
"""если не будет удаляемого элемента при использовании discard код пропустит 
это и продолжит работу в отличии от remove
pop удаляет и возвращает случайный эл-т множества"""

# import time

# num_set = set(range(10 ** 6))

# num_list = list(range(10 ** 6))

# start_time = time.time()
# if 954365 in num_set:
#     print(True)

# print(f'Поиск эл-та множ-ва занял {time.time() - start_time}, сек')

# start_time = time.time()
# if 954365 in num_list:
#     print(True)

# print(f'Поиск эл-та списка занял {time.time() - start_time}, сек')






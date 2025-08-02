import pandas as pd
import plotly.express as px



#Работа с множествами 
# stepan_veg = {'томат', "огурцы", "баклажан", "лук"}
# tania_veg = {'огурцы', 'баклажан', 'кабачок', 'морковь'}

# common_veg = stepan_veg & tania_veg
# print(common_veg)
# print(set.intersection(stepan_veg, tania_veg))


# all_veg = stepan_veg | tania_veg
# print(all_veg)
# print(set.union(stepan_veg, tania_veg))

# only_stepan = stepan_veg - tania_veg
# print(only_stepan)
# print(set.difference(stepan_veg, tania_veg))

# sym_dif = stepan_veg ^ tania_veg
# print(sym_dif)
# print(set.symmetric_difference(stepan_veg, tania_veg))

"""Задача 1
В строках num_string_1 и num_string_2 через пробел указаны числа. 
Напишите программу, которая вычислит и напечатает количество одинаковых 
чисел из этих строк.
num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'"""

# num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
# num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

# list_1 = list(map(int, num_string_1.split()))
# list_2 = list(map(int, num_string_2.split()))

# common_nums = set(list_1) & set(list_2)
# print(len(common_nums))

"""адача 2
В одном огороде растут помидоры, огурцы и морковь, во втором — перец, помидоры и лук.
Допишите программу, которая определит:
Какие овощи растут одновременно и в первом, и во втором огороде.
Какие овощи растут в первом огороде, но не растут во втором.
Какие овощи растут во втором огороде, но не растут в первом.
 
first_garden = {'помидоры', 'огурцы', 'морковь'}
second_garden = {'перец', 'помидоры', 'лук'}"""

# first_garden = {'помидоры', 'огурцы', 'морковь'}
# second_garden = {'перец', 'помидоры', 'лук'}

# both_gardens = first_garden & second_garden
# only_first = first_garden - second_garden
# only_second = set.difference(second_garden, first_garden)
# print(both_gardens, only_first, only_second)


"""Задание 1
Получите общую выручку (цена × количество) по каждой категории и региону."""


# products = pd.read_csv('products_new.csv')
# sales = pd.read_csv('sales.csv')
# print(products.info(), sales.info())
# sales['total'] = sales['quantity'] * sales['price_per_unit']

# print(products.head(6))
# print(sales.head(10))

# merged = sales.merge(products, on='product_id', how='inner')
# print(merged.head(10))

# merged_pivot_reg = merged.pivot_table(index='category', columns='region', values= 'total', aggfunc='sum')
# print(merged_pivot_reg)

"""Сколько штук каждого товара было продано по категориям?"""

# merged_pivot_cat = merged.pivot_table(index='category', columns='product_name', values='quantity', aggfunc='sum')
# print(merged_pivot_cat)

"""Задание 3
Найдите все продажи в категории "Accessories", где сумма покупки превышает 500. используйте loc[] при решении"""

# mask_sum = merged.loc[(merged['category'] == "Accessories") & (merged['total'] > 500)]
# print(mask_sum)


"""Задание 4
Сгруппируйте товары по категориям и посчитайте среднюю цену за единицу товара."""

# merged_group = merged.groupby('category')['price_per_unit'].mean().reset_index()
# print(merged_group)



"""Задание 5
Используя value_counts, определите, сколько раз продавался каждый товар из категории "Electronics"."""

# mask_cat = merged.loc[(merged['category'] == 'Electronics')]
# print(mask_cat['product_name'].value_counts().reset_index(name='sale_count'))





"""Задание 1
Найдите количество клиентов в каждом сегменте."""

# clients = pd.read_csv('clients.csv')
# print(clients.head(10))
# print(clients.info())

# clients_seg = clients.groupby('segment')['client_id'].count().reset_index(name='client_count')
# print(clients_seg)

#using vale_counts
# clients_seg_vc = clients['segment'].value_counts().reset_index(name='client_count')
# clients_seg_vc.columns = ['segment_mew', 'client_count_new']
# print(clients_seg_vc)

"""Задание 2
Отфильтруйте клиентов младше 30 лет и сегмента "A" с помощью .loc."""

# mask_age = clients.loc[(clients['segment'] == 'A') & (clients['age'] < 30)]
# print(mask_age)

"""Задание 3
С помощью query() найдите покупки в категории "Tech", где сумма больше 150."""

# purchases = pd.read_csv('purchases.csv')
# print(purchases.info())
# print(purchases.head(10))

# purchases_query = purchases.query('product_category == "Tech" and amount > 150')
# print(purchases_query)

"""Задание 4
Добавьте колонку age_group (до 30, 30–50, 50+) и выведите сводную таблицу по количеству 
клиентов в этих группах и полу."""


# def age_group(age):
#     if age < 30:
#         return 'до 30'
#     elif age <= 50:
#         return '30-50'
#     else:
#         return '50+'

# clients['age_group'] = clients['age'].apply(age_group)
# print(clients.head())

# clients_table = clients.pivot_table(index='age_group', columns='gender', 
#                                     values='client_id', aggfunc='count')
# print(clients_table)

"""Задание 5
Объедините клиентов и покупки и найдите общую сумму покупок по каждому сегменту."""

# print(clients.head())
# print(purchases.head())
# print(clients.info())
# print(purchases.info())
# merg = purchases.merge(clients, how='inner', on='client_id')
# print(merg.head(10))
# print(merg.groupby('segment')['amount'].sum().reset_index(name='total_amount'))


"""Задание 7
Найдите клиентов, которые совершали более одной покупки. Выведите их имена и количество покупок."""

# clients_num = merg.groupby(['name', 'client_id'])['client_id'].count().reset_index(name='purchase_count')
# clients_num = merg[['name', 'client_id']].value_counts().reset_index(name='purchase_count')
# print(clients_num.loc[clients_num['purchase_count'] > 1])


"""RFM-анализ
время между покупками, частота покупок, сумма покупок. постоянные покупатели несут больше прибылию 20% кличетов - 80% выручки"""


df = pd.read_csv('shop.csv')

df['order_date'] = pd.to_datetime(df['order_date'])
df['order_recency'] = pd.to_datetime('2025-07-28') - pd.to_datetime(df['order_date'].dt.date)
# print(df['order_recency'].head(10))

rfm = df.groupby('customer_id').agg(
    recency = ( "order_recency", lambda x: x.min().days),
    frequence = ('order_id', 'nunique'),
    monetary_value = ('price', 'sum')
    ).reset_index()
# print(rfm.head(5))

rfm['r'] = pd.qcut(rfm['recency'], q = 3, labels=[1, 2, 3])
rfm ['f'] = pd.qcut(rfm['frequence'], q = 3, labels=[1, 2, 3])
# rfm ['f'] = pd.cut(rfm['frequence'], [0,2, 10, 1000], labels=[1, 2, 3])

rfm ['m'] = pd.qcut(rfm['monetary_value'], q = 3, labels=[1, 2, 3])


rfm[['r', 'f', 'm']] = rfm[['r', 'f', 'm']].astype('str')
rfm['rfm_group'] = rfm['r'] + rfm['f'] + rfm['m']
rfm[['r', 'f', 'm']] = rfm[['r', 'f', 'm']].astype('int')
rfm['rfm_sum'] = rfm[['r', 'f', 'm']].sum(axis=1)
# print(rfm.head())
 

rfm_group = rfm.groupby('rfm_group').agg({'customer_id' : 'nunique', 'rfm_sum':'mean'}).reset_index()
# print(rfm_group.sort_values(by= 'customer_id', ascending=False))


fig = px.treemap(rfm_group,
                 path=['rfm_group'],
                 values = 'customer_id',
                 color = 'rfm_sum', 
                 color_continuous_scale = 'Sunset', 
                 title = "RFM segmentation ...")
fig.show()







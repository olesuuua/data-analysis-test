import pandas as pd

# df = pd.read_csv('shop.csv')

"""converting collums together"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)

# print(df['order_date'].dtype)
# print(df['registration_date'].dtype)

"""converting format"""
# date='18-10-59 14.07.25'
# print(pd.to_datetime(date, format = '%H-%M-%S %d.%m.%y'))

"""adding extraction from date"""
# df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
# df['order_day'] = df['order_date'].dt.day_name()
# df['order_year'] = df['order_date'].dt.year
# print(df[['order_day', 'order_year']].head())

# df['month_order'] = pd.to_datetime(df['order_date']).dt.strftime('%Y %B') #b- short month name; A- day name
# print(df['month_order'].head())


"""time intervals"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)
# df['delta'] = df['order_date'] - df['registration_date']
# print(df['delta'].head())

"""Найдите среднюю задержку между регистрацией и заказом"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)
# df['delta'] = df['order_date'] - df['registration_date']
# print(df['delta'].mean())


"""Найдите заказы, сделанные спустя более 100 дней после регистрации"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)
# df['delta'] = df['order_date'] - df['registration_date']
# orders_delta = df[df['delta'] > pd.Timedelta(days=100)]
# print(orders_delta.head())

"""Заказы, оформленные в течение 7 дней после регистрации"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)
# df['delta'] = df['order_date'] - df['registration_date']
# orders_delta = df[df['delta'] == pd.Timedelta(days=7)]
# print(len(orders_delta))


"""Добавьте 30 дней ко всем значениям delta (например, гипотетическая доставка через 30 дней)"""
# df[['order_date', 'registration_date']] = df[['order_date', 'registration_date']].apply(pd.to_datetime)
# df['delta'] = df['order_date'] - df['registration_date']
# df['delivery_date'] = df['delta'] + pd.Timedelta(days=30)
# print(df[['delivery_date', 'delta']])

"""Преобразуй столбцы registration_date и order_date к типу datetime64, и выведи их типы.
Вычисли разницу между датой заказа и регистрацией."""

# df_1 = pd.read_csv('user_orders_solved.csv')
# # print(df_1.head())
# df_1[['order_date', 'registration_date']] = df_1[['order_date', 'registration_date']].apply(pd.to_datetime)
# print(df_1['order_date'].dtype)
# df_1['delta_order'] = df_1['order_date'] - df_1['registration_date']
# print(df_1['delta_order'].head())

"""Выведите день недели когда было сделано боьше всего заказов"""
# df_1['order_date'] = df_1['order_date'].dt.day_name()
# permen =df_1['order_date'].value_counts().idxmax()
# print(permen)

# cars = pd.read_csv('cars.csv')
# print(cars.head())


# group_brand = cars.groupby("brand")["price"].mean()
# cars['brand'] = cars['brand'].str.upper().str.strip().replace({'BMV':'BMW'})

# cars_group = cars.groupby('brand')['price'].mean().reset_index(name="avg_price")
# print(cars_group)



"""Давайте подчистим данные в city и сделаем группировку по городу и населению (total)"""
# city = pd.read_csv('example3_4.csv')
# print(city.info())
# city['city'] = city['city'].str.upper().str.strip().replace({'M?XICO D.F.':'MEXICO D.F.', 'M?NSTER':'MENSTER', 'MONTR?AL':'MONTREAL', 'M?NCHEN':'MUNCHEN', 'SAINT-PETERSBURG':'SAINT PETERSBURG', 'K?LN':'KOLN'})
# print(city['city'].sort_values().unique())
# filter_1 = city.groupby('city').agg({"total": "sum"})
# filter_1 = city.groupby(['city', 'country']).agg({"total": "sum"})
# print(filter_1.head())

"""Сгруппируйте данные по user_id, а колонку genre_name выберите как показатель для сравнения. Результат сохраните в переменной track_grouping.
Затем посчитайте количество композиций, которые слушал каждый пользователь, — методом count(). Результат сохраните в 
переменной track_counting.
Выведите на экран первые 30 строк из track_counting.
"""
# music = pd.read_csv('music_log_upd.csv')
# print(music.info())

# track_grouping = music.groupby('user_id')['genre_name']
# track_counting =  track_grouping.count()
# print(track_counting.head(30))

"""Предположим, что более широкие вкусы характерны для пользователей, которые слушают больше 50 песен. 
Чтобы найти такого пользователя, напишите функцию user_tracks.
Эта функция: 
•	Принимает группировку, сгруппированные данные, как значение для параметра group.
•	Перебирает группы, входящие в эту группировку. В каждой группе два элемента — имя группы с индексом 0 и список значений с индексом 1.
•	Обнаружив первую группу, в которой список (элемент с индексом 1) содержит более 50 значений, 
функция вернёт имя группы (элемент с индексом 0).
Вызовите функцию user_tracks и передайте ей track_grouping. Результат — user_id меломана — сохраните в переменной search_id
 и выведите на экран её значение."""

# music = pd.read_csv('music_log_upd.csv')

# track_grouping = music.groupby('user_id')['genre_name']


# def user_tracks(track_grouping):
#     for el in track_grouping:
#         if len(el[1]) > 50:
#             user = el[0]
#             return user
        
# meloman_id = user_tracks(track_grouping)

# top_artist = (music[music['user_id'] == meloman_id]['artist_name']).value_counts().idxmax()
# print(f"Меломан {meloman_id}")
# print(f"Любимый исполнитель {top_artist}")


"""Посчитайте общее количество заказов в каждом городе."""
# orders = pd.read_csv('group_orders.csv')
# print(orders['city'].unique())
# group_city = orders.groupby('city')['order_id'].count().reset_index(name='total_orders')
# print(group_city)
# print(orders.head(30))

"""среднее по городу сумма заказа"""
# group_city_1 = orders.groupby('city')['total'].mean()
# print(group_city_1)

"""самый продаваемый по кол-ву"""
# group_city_2 = orders.groupby('product')['quantity'].sum().reset_index(name='summ')
# print(group_city_2)

# group_city_3 = group_city_2.sort_values(by='summ', ascending=False).iloc[0]
# print(group_city_3)


"""Сгруппируйте данные по месяцу заказа и найдите общую выручку в каждом месяце."""
# orders = pd.read_csv('group_orders.csv')
# orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')

#orders['order_month'] = orders['order_date'].dt.strftime('%B')

# orders['order_month'] = orders['order_date'].dt.to_period('M')
# month_group = orders.groupby('order_month')['total'].sum().reset_index(name='summ')
# month_group['month_name'] = month_group['order_month'].dt.strftime('%B %Y') #timestamp - data to date - time
# print(month_group[['month_name', 'summ']])


"""Выведите топ-3 города с самой высокой средней стоимостью одного заказа (total)."""
orders = pd.read_csv('group_orders.csv')
# print(orders.head())
group_ord_tot = orders.groupby('city')['total'].mean().reset_index(name='avg_tot').sort_values(by='avg_tot', ascending=False)
print(group_ord_tot.head(3))
"""Разделите строку на фамилии по символу ;, а затем получите вторую фамилию в списке."""
example_str = 'Иванов;Петров;Сидоров;Кузнецов'
second_surname = example_str.split(';')[1]
print(second_surname)
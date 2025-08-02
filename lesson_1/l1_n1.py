"""Удалите лишние символы * и - с начала и конца строки."""
example_str = '***---Добро пожаловать!---***'
clear_str = example_str.strip('*-')
print(clear_str)
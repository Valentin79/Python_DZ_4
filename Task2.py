# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def func(**kwargs):
    result = {}
    for item, value in kwargs.items():
        result[value] = item
    return result


print(func(хлеб=1, молоко=1, яйцо="10шт", картофель=2, пиво="1,5л"))

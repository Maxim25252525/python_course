"""
# Задача 2: Математические операции +1

Программа должна работать с двумя числами, которые вводит пользователь.
Напишите четыре функции, каждая из которых будет выполнять определённую
математическую операцию с этими числами.

1. summarize(a, b): возвращает сумму чисел a и b.
2. subtract(a, b): возвращает разность чисел (из большего числа вычитается
меньшее).
3. multiply(a, b): возвращает произведение чисел a и b.
4. divide(a, b): возвращает частное чисел (большее число делится на меньшее
без округления). Если происходит деление на ноль, функция должна перехватить
исключение через except и вызвать с сообщением: 'Деление на 0 невозможно.'.

Под блоком if __name__ == '__main__': получите пользовательский ввод,
выполните все четыре вышеописанные функции по очереди, передав им нужные
аргументы и распечатав результат вычислений.

> Для того, чтобы понять, какое из чисел больше или меньше можно
воспользоваться функциями max() и min() соответственно.
"""


def summarize(a, b):
    return a + b


def subtract(a, b):
    return max(a, b) - min(a, b)


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return max(a, b) / min(a, b)
    except ZeroDivisionError:
        raise ZeroDivisionError("Деление на 0 невозможно.")


if __name__ == '__main__':
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    print(summarize(first_number, second_number))
    print(subtract(first_number, second_number))
    print(multiply(first_number, second_number))
    print(divide(first_number, second_number))

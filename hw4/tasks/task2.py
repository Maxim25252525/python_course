"""
# Задача 2: Перехват ошибок +1

Напишите программу, которая ожидает пользовательский ввод с клавиатуры двух
чисел и делит первое на второе соответственно при помощи целочисленного
деления.

При попытке деления на 0 нужно перехватить ошибку и вернуть строку
'Деление на 0 невозможно'.

> В блоке except нужно явно указать тип ошибки деления на 0
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
try:
    print(a // b)
except ZeroDivisionError:
    print("Деление на 0 невозможно")

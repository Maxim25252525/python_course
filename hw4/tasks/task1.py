"""
# Задача 1: name is main +1

Современные фильмы делятся на различные категории, самая популярная - 12+
Напишите программу, которая принимает натуральное число - возраст человека
Если возраст больше или равен 12 - программа должна вывести 'Проход разрешен',
иначе 'Проход запрещен'

> При решении нужно использовать тернарный оператор

> Гарантируется, что пользователь вводит натуральные числа
"""
age = int(input())
print("Проход разрешен" if age >= 12 else "Проход запрещен")

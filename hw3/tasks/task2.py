"""
# Задача 2: На чьей стороне ты? +1

Программа должна спрашивать у пользователя: `Какую палочку Twix выберешь ты: `.

Если пользователь вводит `л`, то нужно вывести: `Выбрана левая палочка`.

Если пользователь вводит `п`, то нужно вывести: `Выбрана правая палочка`

Иначе вывести `Палочка не выбрана`.

> Данную задачу нужно дополнительно выложить в github.
"""

twix = input("Какую палочку Twix выберешь ты: ")
if twix == 'л':
    print("Выбрана левая палочка")
elif twix == 'п':
    print("Выбрана правая палочка ")
else:
    print("Палочка не выбрана ")
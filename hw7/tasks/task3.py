"""
# Задача 3: Отчёт о погоде +1

Новый прибор в гидрометцентре каждый час измеряет температуру воздуха и
передаёт данные в виде строки чисел, разделённых пробелами.
Например: 15 15.1 15.2 16 15.5

Напишите функцию 'create_weather_report', которая обрабатывает эти данные:
1. Удаляет повторяющиеся значения температуры.
2. Вычисляет среднюю температуру (на основе всех данных, а не только
уникальных).

Функция должна принимать на вход список с числами.
Функция должна возвращать словарь с ключами:
- unique_degrees - уникальные значения температуры.
- average_temperature - средняя температура.

Под блоком if __name__ == '__main__':
1. Получите от пользователя строку с числами через пробел.
2. Преобразуйте строку в список чисел.
2. Вызовите функцию 'create_weather_report', передав на вход список.
3. Выведите результат работы функции следующим образом:
Отчет о температуре: <уникальные значения через пробел>
Среднее значение температуры: <средняя температура>

Среднее значение температуры при выводе округлите до 2 знаков после запятой.

Добавьте докстринг (описание функции) и аннотацию типов (указание типов
параметров и возвращаемых значений) для функции.

В примере ниже данные в отчете могут располагаться в различном порядке.
Input:
```
20 20 20 20 20.23 20.23 20.54 20.546789 20.71 20.80 21 21 21 21 21
```

Output:
```
Отчет о температуре: 20.71 20.54 20.546789 20.0 20.23 20.8 21.0
Среднее значение температуры: 20.54
```
"""

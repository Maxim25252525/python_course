"""
# Задача 3: Сумма аргументов +2

Напишите функцию 'get_sum', которая принимает произвольное количество
аргументов (чисел или строк, содержащих числа) и возвращает их сумму. Если
аргумент не является числом, он игнорируется.

Если аргумент — строка, содержащая число, она должна быть преобразована в число
и учтена в сумме.

Под блоком if __name__ == '__main__': выполните функцию, передав ей нужные
аргументы, и распечатайте результат вызова функции. В данной задаче ожидать
ввода пользователя не нужно!

Добавьте докстринг (описание функции) и аннотацию типов (указание типов
параметров и возвращаемых значений) для функции.

Напишите тесты для функции, используя параметризацию.

Разберем пример:
Call:
```
get_sum(1, 2, '3', 2.5, '3,5', '1.5', [1, 2, 3], {1: 123, 2: 234}, 'abc 12')
```

Return:
```
13.5
```

1 - число, учитываем
2 - число, учитываем
'3' - строка, преобразуем в число, учитываем
2.5 - число, учитываем
'3,5' - строка, преобразовываем в число, учитываем
'1.5' - строка, преобразовываем в число, учитываем
[1, 2, 3] - список, нельзя преобразовать в число, пропускаем
{1: 123, 2: 234} - словарь, нельзя преобразовать в число, пропускаем
'abc 12' - строка, нельзя преобразовать в число, пропускаем
"""

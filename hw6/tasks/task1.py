"""
# Задача 1: Методы списка +1

Напишите 3 функции, каждая из которых будет выполнять определённые действия со
списком целых чисел.

1. get_central_element(numbers) - возвращает центральный элемент списка.
Если количество элементов в списке четное - возвращает два центральных
элемента в виде кортежа.
2. get_latest_sorted_items(numbers) - возвращает два последних элемента
отсортированного по возрастанию списка, в виде кортежа.
Элементы должны возвращаться в том порядке, в котором они были отсортированы.
3. check_hundred(numbers) - возвращает "YES", если список содержит элементы
100 и -100, иначе возвращает "NO". Этот пункт нужно реализовать с
использованием тернарного оператора.

> Гарантируется, что количество элементов в списке больше одного.

Под блоком if __name__ == '__main__':
1. Получите список от пользователя (каждый элемент списка вводится через пробел
на одной строке)
2. Проинициализируйте переменную numbers - список.
3. Приведите элементы списка к типу int.
4. Выполните функции, передав им нужные аргументы, и распечатайте результат
вызовов функций.

Добавьте докстринги (описание функций) и аннотации типов (указание типов
параметров и возвращаемых значений) для каждой функции.
"""


def get_central_element(numbers: list[int]) -> int | tuple[int, int]:
    """Функция возвращает центральный элемент списка.

    Args:
        numbers: Список целых чисел.

    Returns:
        Центральные элементы в зависимости от длины списка.
    """

    central_index = int(len(numbers) / 2)
    if len(numbers) % 2 == 0:
        return numbers[central_index - 1], numbers[central_index]
    return numbers[central_index]


def get_latest_sorted_items(numbers: list[int]) -> tuple[int, int]:
    """Функция возвращает два последних элемента
    отсортированного по возрастанию списка.

    Args:
        numbers: Список целых чисел.

    Returns:
        Предпоследний и последний элементы списка.
    """

    numbers = sorted(numbers)
    return numbers[-2], numbers[-1]


def check_hundred(numbers: list[int]) -> str:
    """Функция проверяет список на наличие элементов 100 и -100.

    Args:
        numbers: Список целых чисел.

    Returns:
        YES - если список содержит элементы 100 и -100, NO - иначе.
    """

    return "YES" if -100 in numbers and 100 in numbers else "NO"


if __name__ == "__main__":
    my_numbers = list(map(int, input("Введите числа через пробел: ").split()))
    if get_central_element(my_numbers) == tuple:
        print(*get_central_element(my_numbers))
    else:
        print(get_central_element(my_numbers))
    print(*get_latest_sorted_items(my_numbers))
    print(check_hundred(my_numbers))

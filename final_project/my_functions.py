import random
import sys

from final_project.main import coordinates_dict
from my_classes import Shot, Tank, Field


def print_fields(player_field: Field, comp_field: Field):
    # Создание заголовка с буквами, где THSP - символ тонкого пробела.
    letters = "  ".join(list("АБВГДЕЖЗИК"))
    # letters = letters.replace("Д", " Д")
    result = f"    {letters}         {letters}\n"

    # Актуализируем данные на полях.
    player_field.fill_field()
    comp_field.fill_field()

    for index, row_data in enumerate(zip(player_field.data, comp_field.data)):
        row_number = f" {index + 1}"[-2:]  # Номер строки из двух символов.
        # Данные пользовательского поля.
        result += f"{row_number} {' '.join(row_data[0])}"
        # Данные поля компьютера.
        result += " " * 5 + f"{row_number} {' '.join(row_data[1])}\n"
    print(result)


def converted_coords(coords: list) -> list:
    """
    Переводит координаты в индексы.
    Args:
        coords: Список координат танка.

    Returns:
        Список в формате ((кор1, кор2), колонка).
    """
    result = []
    for coord in coords:
        column = coordinates_dict[coord[0].lower()]  # Колонка.
        if len(coord) >= 4:
            coord1 = int(coord[1]) - 1  # Первая координата.
            coord2 = int(coord[3:]) - 1  # Вторая координата.
            result.append(Tank((coord1, coord2), column))
        else:
            cord1 = int(coord[1:]) - 1  # Координата.
            result.append(Tank((cord1, cord1), column))

    return result


def check_tank_coordinate(
    searched_coord: Tank, coordinates: list[Tank]
) -> bool:
    """Проверяет корректность координаты танка на поле.

    Args:
        searched_coord: Координаты искомого танка.
        coordinates: Список координат всех танков на поле.

    Returns:
        True - если координаты танка корректны, False - если нет.
    """
    is_correctly = True
    for coord in coordinates:
        rows, column = coord.rows, coord.column
        if (
            searched_coord.rows == rows
            and searched_coord.column == column
            and coordinates.count(coord) == 1
        ):
            continue
        if (
            searched_coord.rows[0] - 1 <= rows[1]
            and searched_coord.rows[1] + 1 >= rows[0]
        ):
            if (
                searched_coord.column - 1
                <= column
                <= searched_coord.column + 1
            ):
                is_correctly = False
                break

    return is_correctly


def check_tanks_coordinates(coordinates: list) -> bool:
    """Проверяет корректность координат танков на поле.

    Args:
        coordinates: Список координат всех танков на поле.

    Returns:
        True - если координаты танков корректны, False - если нет.
    """
    for coord in coordinates:
        if check_tank_coordinate(coord, tanks):
            return True
        else:
            print("Некорректные координаты танков!")
            return False

    return True


def check_hit(shot: Shot, field: Field, kind: str = "tank") -> tuple:
    """
    Проверяет попадание выстрела в танк или повторное попадание.
    Функция возвращает True в двух случаях:
    1. Если на месте выстрела есть танк.
    2. Если в это место уже стреляли.
    Выбор случая определяется параметром kind.

    Args:
        shot: Выстрел игрока.
        field: Поле с танками или выстрелами.
        kind: Тип списка, в котором ищется выстрел('tank' или 'shot').

    Returns:
        Кортеж, содержащий логический тип и объект танка или выстрела.
        True - если выстрел есть в выбранном списке, False - если нет.
    """
    if kind == "tank":
        arr = field.tanks
        for coord in arr:
            if (
                coord.rows[0] <= shot.row <= coord.rows[1]
                and coord.column == shot.column
            ):
                return True, coord
    elif kind == "shot":
        arr = field.shots
        for coord in arr:
            if coord == shot:
                return True, coord
    else:
        raise ValueError(
            f"Функция 'check_available_shot' не принимает "
            f"значение '{kind}' в качестве аргумента 'kind'."
        )

    return False, None


def tip(field: Field):
    """
    Дает подсказку игроку, если он правильно решил пример.

    Args:
        field: Поле компьютера.
    """
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = a + b
    answer = input(f"Решите пример: {a} + {b} = ")
    if int(answer) == c:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        player_shot = Shot(x, y)

        if check_hit(player_shot, field)[0]:
            while check_hit(player_shot, field)[0]:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                player_shot = Shot(x, y)

        # Трансформация индексов в координату.
        x += 1
        y = coordinates_dict[y]
        field.shots.append(player_shot)
        print(
            "Правильно!",
            f"Ваша подсказка: в клетке {y}{x} нет танка!",
            sep="\n",
        )
    else:
        print("Неправильно!")


def check_exit(cmd):
    """Завершает программу если игрок решил выйти."""
    if cmd == "выход":
        print("Игра окончена!")
        sys.exit()


def conv_cmd(cmd: str) -> str:
    """
    Удаляет лишние пробелы и переводит все буквы в нижний регистр
    из команды игрока.

    Args:
        cmd: Команда игрока.

    Returns:
        Отформатированная команда игрока.
    """
    return cmd.strip().lower()


def create_tanks(tanks_list: list):
    """Создает случайные координаты танков на поле.

    Args:
        tanks_list: Список координат всех танков на поле.
    """
    for _ in range(10):
        x = [random.randint(0, 9) for _ in range(2)]
        coord1 = min(x)  # Первая координата.
        coord2 = max(x)  # Вторая координата.
        column = random.randint(0, 9)  # Колонка.
        tank_coord = Tank(
            (coord1, coord2), column
        )  # Создание координаты танка.
        while (
            not check_tank_coordinate(tank_coord, tanks_list)
            or coord2 - coord1 + 1 > 5
            or tank_coord in tanks_list
        ):
            x = [random.randint(0, 9) for _ in range(2)]
            coord1 = min(x)  # Первая координата.
            coord2 = max(x)  # Вторая координата.
            column = random.randint(0, 9)  # Колонка.
            tank_coord = Tank(
                (coord1, coord2), column
            )  # Создание координаты танка.
        tanks_list.append(tank_coord)


def check_destroyed_tank(field: Field, shot: Shot) -> tuple:
    """
    Проверяет, не уничтожен ли танк при выстреле игрока.

    Args:
        field: Поле игрока или компьютера.
        shot: Выстрел игрока или компьютера.

    Returns:
        Кортеж, содержащий логический тип и объект танка.
        True - если танк был уничтожен. False - если нет.
    """
    if check_hit(shot, field)[0]:
        tank = check_hit(shot, field)[1]
        for row in range(tank.rows[0], tank.rows[1] + 1):
            if field.data[row][shot.column] == "✘":
                continue
            return False, None

        return True, tank
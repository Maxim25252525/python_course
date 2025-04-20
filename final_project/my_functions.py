import random
import sys
import re

from final_project.my_classes import Shot, Tank, User, Computer

coordinates_dict = {
    "а": 0,
    "б": 1,
    "в": 2,
    "г": 3,
    "д": 4,
    "е": 5,
    "ж": 6,
    "з": 7,
    "и": 8,
    "к": 9,
    0: "а",
    1: "б",
    2: "в",
    3: "г",
    4: "д",
    5: "е",
    6: "ж",
    7: "з",
    8: "и",
    9: "к",
}


def print_fields(player_field: User, comp_field: Computer):
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


def converted_coords(coords: list[str]) -> list:
    """
    Переводит координаты в индексы.
    Args:
        coords: Необработанный список координат танка.

    Returns:
        Список в формате ((кор1, кор2), колонка).
    """
    result = []
    english = 'abcdefghijklmnopqrstuvwxyz' # noqa
    pattern = r'^([a-я])(\d+)(?:([a-я])(\d+))?$'
    for coord in coords:
        if re.fullmatch(pattern, coord) is None:
            raise ValueError("Неверный формат координат.")

        match = re.fullmatch(pattern, coord)
        row1 = int(match.group(2)) - 1  # Первая координата.
        row2 = int(match.group(4)) - 1 if match.group(4) else row1  # Вторая координата.
        if row1 > row2:
            row1, row2 = row2, row1
        col1 = match.group(1)
        col2 = match.group(3) if match.group(3) else col1

        if col1 in english or col2 in english:
            raise ValueError("Координаты танка должны быть на русском языке.")
        elif (col1 not in coordinates_dict.values() or
                col2 not in coordinates_dict.values()):
            raise ValueError("Координаты танка должны быть в пределах от 'a' до 'к'.")
        elif col1 != col2:
            raise ValueError("Координаты танка должны быть в одной колонке.")
        elif row1 not in range(10) or row2 not in range(10):
            raise ValueError("Координаты танка должны быть от 1 до 10.")

        col = coordinates_dict[col1]  # Колонка.
        result.append(Tank((row1, row2), col))

    return result


def check_tank_coordinate(
        searched_coord: Tank, coordinates: list[Tank]
) -> (bool, str | Tank):
    """Проверяет корректность координаты танка на поле.

    Args:
        searched_coord: Координаты искомого танка.
        coordinates: Список координат всех танков на поле.

    Returns:
        Кортеж, содержащий логический тип и объект танка.
        Если координаты танка некорректны,
        то вместо объекта танка возвращается строка с ошибкой.
        True - если координаты танка корректны, False - если нет.
    """
    for coord in coordinates:
        rows, column = coord.rows, coord.column
        length = coord.length
        if length > 5:
            error = "Танк не может быть длиннее 5 клеток."
            return False, error

        # Координаты первого танка.
        r1 = searched_coord.rows[0] + 1
        r2 = searched_coord.rows[1] + 1
        c = coordinates_dict[searched_coord.column]
        t1 = (f'{c}{r1}{c}{r2}' if r1 != r2
              else f'{c}{r1}')
        # Координаты второго танка.
        r1 = rows[0] + 1
        r2 = rows[1] + 1
        c = coordinates_dict[column]
        t2 = (f'{c}{r1}{c}{r2}' if r1 != r2
              else f'{c}{r1}')

        if (searched_coord == coord
                and coordinates.count(coord) > 1):
            error = f"Танк {t1} уже есть на поле."
            return False, error
        elif (searched_coord == coord
              and coordinates.count(coord) <= 1):
            continue

        if (searched_coord.rows[0] - 1 <= rows[1]
                and searched_coord.rows[1] + 1 >= rows[0]
                and searched_coord.column - 1
                <= column
                <= searched_coord.column + 1):
            error = f"Танки {t1} и {t2} соприкасаются."
            return False, error

    return True, Tank


def check_tanks_coordinates(coordinates: list,
                            field: User | Computer) -> bool:
    """Проверяет корректность координат танков на поле.

    Args:
        coordinates: Список координат всех танков на поле.
        field: Поле с танками игрока или компьютера.

    Returns:
        True - если координаты танков корректны, False - если нет.
    """
    for coord in coordinates:
        check = check_tank_coordinate(coord, coordinates)
        length = coord.length
        if not check[0]:
            print(check[1])
            return False
        elif field.placement[length] == 0:
            print(f'Превышено количество танков длиной {length}.')
            return False
        field.placement[length] -= 1

    return True


def check_hit(shot: Shot, field: User | Computer, kind: str) -> tuple:
    """
    Проверяет попадание выстрела в танк или повторное попадание.
    Функция возвращает True в двух случаях:
    1. Если на месте выстрела есть танк.
    2. Если в это место уже стреляли.
    Выбор случая определяется параметром kind.

    Args:
        shot: Выстрел игрока или компьютера.
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


def tip(field: Computer):
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

        while check_hit(player_shot, field, "tank")[0]:
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


def create_tanks(tanks_list: list, placement: dict):
    """Создает случайные координаты танков на поле.

    Args:
        tanks_list: Список координат всех танков на поле.
        placement: Словарь с правильными длинами танков.
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
                not check_tank_coordinate(tank_coord, tanks_list)[0]
                or coord2 - coord1 + 1 > 5
                or tank_coord in tanks_list
                or placement[tank_coord.length] == 0
        ):
            x = [random.randint(0, 9) for _ in range(2)]
            coord1 = min(x)  # Первая координата.
            coord2 = max(x)  # Вторая координата.
            column = random.randint(0, 9)  # Колонка.
            tank_coord = Tank(
                (coord1, coord2), column
            )  # Создание координаты танка.
        placement[tank_coord.length] -= 1
        tanks_list.append(tank_coord)


def check_destroyed_tank(field: User | Computer, shot: Shot) -> tuple:
    """
    Проверяет, не уничтожен ли танк при выстреле игрока.

    Args:
        field: Поле игрока или компьютера.
        shot: Выстрел игрока или компьютера.

    Returns:
        Кортеж, содержащий логический тип и объект танка.
        True - если танк был уничтожен. False - если нет.
    """
    if check_hit(shot, field, 'tank')[0]:
        tank = check_hit(shot, field, 'tank')[1]
        for row in range(tank.rows[0], tank.rows[1] + 1):
            if field.data[row][shot.column] == "✘":
                continue
            return False, None

        return True, tank


def check_input(user_input: str | list, kind: str, field: User | Computer) -> bool:
    """
    Проверяет корректность ввода игрока.
    Некорректным вводом считается:
    Если kind = 'shot':
        1. Если игрок стреляет по своей же клетке.
        2. Если такая клетка не входит в диапазон поля.
        3. Если ввод не соответствует шаблону.
    Если kind = 'tank':
        1. Если расположение танков неправильное.
        2. Если ввод не соответствует шаблону.

    Args:
        user_input: Ввод пользователя.
        kind: Флаг, который указывает какую проверку нужно выполнить.
            'shot' - проверка ввода выстрела игрока.
            'tank' - проверка ввода танков игрока.
        field: Поле компьютера или игрока.
        Если kind = 'shot', то field = поле компьютера.
        Если kind = 'tank', то field = поле игрока.

    Returns:
        True - если выстрел корректный, False - если нет.
    """
    if kind == 'shot':
        if user_input == 'подсказка':
            return False
        if field is None:
            raise ValueError("Вы не указали аргумент 'field'")
        if len(user_input) < 2:
            print("Неправильный ввод!")
            return False

        row = user_input[0]
        column = user_input[1:]
        if (row.isalpha()
                and 2 <= len(user_input) <= 3
                and column.isdigit()
                and 1 <= int(column) <= 10
                and row in coordinates_dict):
            user_shot = Shot(int(column) - 1, coordinates_dict[row], )
            if not check_hit(user_shot, field, 'shot')[0]:
                return True
            else:
                print("Вы уже стреляли по этой клетке!")
        else:
            print("Неправильный ввод!")

        return False
    elif kind == 'tank':
        try:
            tanks = converted_coords(user_input)
        except ValueError as ex:  # noqa
            print(ex)
            return False
        return check_tanks_coordinates(tanks, field)

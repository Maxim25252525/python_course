import random
import sys


CELL_DESIGN = {"empty": "▢", "tank": "▣", "miss": "◼", "hit": "✘"}

coordinates_dict = {"а": 0, "б": 1, "в": 2, "г": 3, "д": 4, "е": 5, "ж": 6, "з": 7, "и": 8, "к": 9,
                    0: "а", 1: "б", 2: "в", 3: "г", 4: "д", 5: "е", 6: "ж", 7: "з", 8: "и", 9: "к"}


class Tank:

    def __init__(self, rows: tuple[int, int], column: int):
        self.rows = rows  # Индексы строк, где расположен танк.
        self.column = column  # Индекс столбца, где расположен танк.

    # Метод сравнения объектов
    # Теперь объекты сравниваются по атрибутам.
    def __eq__(self, other):
        if not isinstance(other, Tank):
            return False
        return (self.rows == other.rows and
                self.column == other.column)


class Shot:

    def __init__(self, row: int, column: int):
        self.row = row  # Индекс строки, куда произведен выстрел.
        self.column = column  # Индекс столбца, куда произведен выстрел.
        self.hit: bool = False  # Признак попадания.


class Field:
    """Класс поля.

    Поле представлено в виде списка строк,
    каждая из которых - это список столбцов
    - условных обозначений из CELL_DESIGN.

    Args:
        player: Показывает, пользовательское ли поле.

    Attributes:
        data: Двумерный список, содержащий поле.
        tanks: Список танков.
        shots: Список выстрелов, производимых по инициализированному полю.
        player: Показывает, пользовательское ли поле.
    """

    def __init__(self, player: bool = True):
        # Заполнение пустого поля.
        self.data = [
            [CELL_DESIGN["empty"] for column in range(10)] for row in range(10)
        ]
        # Нужно заполнять только для пользовательского поля.
        self.tanks: list[Tank] = []
        self.shots: list[Shot] = []
        self.player = player

    def fill_field(self):
        """Заполняет поле условными символами."""
        # Расстановка танков на поле.
        if self.player:
            for tank in self.tanks:
                for row in range(tank.rows[0], tank.rows[1] + 1):
                    self.data[row][tank.column] = CELL_DESIGN["tank"]
        # Расстановка выстрелов на поле.
        for shot in self.shots:
            self.data[shot.row][shot.column] = (
                CELL_DESIGN["hit"] if shot.hit else CELL_DESIGN["miss"]
            )


def print_fields(player_field: Field, comp_field: Field):
    # Создание заголовка с буквами, где THSP - символ тонкого пробела.
    letters = "  ".join(list("АБВГДЕЖЗИК"))
    letters = letters.replace("Д", " Д")
    result = f"   {letters}         {letters}\n"

    # Актуализируем данные на полях.
    player_field.fill_field()
    comp_field.fill_field()

    for index, row_data in enumerate(
        zip(player_field.data, comp_field.data)
    ):
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


def check_tank_coordinate(searched_coord: Tank, coordinates: list[Tank]) -> bool:
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
        if (searched_coord.rows == rows and searched_coord.column == column and
                coordinates.count(coord) == 1):
            continue
        if searched_coord.rows[0] - 1 <= rows[1] and searched_coord.rows[1] + 1 >= rows[0]:
            if searched_coord.column - 1 <= column <= searched_coord.column + 1:
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


def check_available_shot(shot: Shot, field: Field, kind: str = 'tank') -> bool:
    """
    Проверяет доступность выстрела.
    Функция возвращает False в двух случаях:
    1. Если на месте выстрела есть танк.
    2. Если в это место уже стреляли.
    Выбор случая определяется параметром kind.

    Args:
        shot: Выстрел игрока.
        field: Поле с танками или выстрелами.
        kind: Тип списка, в котором ищется выстрел('tank' или 'shot').

    Returns:
        True - если в выстрел есть в выбранном списке, False - если нет.
    """
    if kind == 'tank':
        arr = field.tanks
        for coord in arr:
            if (coord.rows[0] <= shot.row <= coord.rows[1] and
                    coord.column == shot.column):
                return True
    elif kind == 'shot':
        arr = field.shots
        for coord in arr:
            if coord == shot:
                return True
    else:
        raise ValueError(f"Функция 'check_available_shot' не принимает "
                         f"значение '{kind}' в качестве аргумента 'kind'.")

    return False


def tip(field: Field):
    """
    Дает подсказку игроку, если он правильно решил пример.

    Args:
        field: Поле компьютера.
    """
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = a + b
    answer = input(f'Решите пример: {a} + {b} = ')
    if int(answer) == c:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        player_shot = Shot(x, y)

        if check_available_shot(player_shot, field):
            while check_available_shot(player_shot, field):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                player_shot = Shot(x, y)

        # Трансформация индексов в координату.
        x = coordinates_dict[x]
        y += 1
        field.shots.append(player_shot)
        print("Правильно!"
              f"Ваша подсказка: в клетке {x}{y} нет танка!", sep="\n")
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
        tank_coord = Tank((coord1, coord2), column)  # Создание координаты танка.
        while (not check_tank_coordinate(tank_coord, tanks_list) or
               coord2 - coord1 + 1 > 5 or tank_coord in tanks_list):
            x = [random.randint(0, 9) for _ in range(2)]
            coord1 = min(x)  # Первая координата.
            coord2 = max(x)  # Вторая координата.
            column = random.randint(0, 9)  # Колонка.
            tank_coord = Tank((coord1, coord2), column)  # Создание координаты танка.
        tanks_list.append(tank_coord)


if __name__ == "__main__":
    print("Привет! Это игра танковый бой!",
          "Если вы хотите ознакомиться с правилами игры, напишите 'помощь'.",
          "Чтобы начать игру, вам нужно написать 'старт'.", sep="\n")

    command = conv_cmd(input("> "))
    # command = 'старт'
    check_exit(command)
    while True:
        match command:
            case "помощь":
                print("Правила игры: ")
                command = conv_cmd(input("> "))
                check_exit(command)

            case "старт":
                # Начало программы, создаем поля для игрока и компьютера.
                # Создаём танки для компьютера.
                print("Игра началась!")
                user_field = Field()
                computer_field = Field()
                tanks = []
                create_tanks(tanks)
                computer_field.tanks = tanks
                print_fields(user_field, computer_field)

                # Создаем танки для игрока.
                command = conv_cmd(input("Введите координаты ваших танков через пробел: "))
                check_exit(command)
                tanks = command.split()
                tanks = converted_coords(tanks)  # конвертируем координаты танков
                while not check_tanks_coordinates(tanks):
                    command = conv_cmd(input("Введите координаты ваших танков через пробел: "))
                    check_exit(command)
                    tanks = command.split()
                    tanks = converted_coords(tanks)
                user_field.tanks = tanks

                # Алгоритм самой игры.

                # TODO:
                #  Глобально, нужно доделать логику самой игры.
                #  То есть добавить возможность производить выстрелы компьютеру
                #  И делать ходы по очереди, пока не закончится игра.
                #  Также нужно добавить всяческие проверки на корректность ввода координат,
                #  причем как танков, так и выстрелов.
                #
                # TODO:
                #  > Если понадобится делать проверку на наличие в клетки выстрела или танка
                #    можно использовать функцию "check_available_shot".
                #  > После каждого ввода пользователя нужно использовать "conv_cmd".
                #  > Также нужно использовать "check_exit", чтобы в случае чего завершать игру.
                #
                # TODO:
                #  Желательно вынести все функции в отдельный файл.
                #  Также нужно разобраться, когда стоит очищать терминал.
                #  Чтобы скрыть танки компьютера нужно добавить False в
                #  computer_field (находиться где-то в начале блока main, после приветствия).

                command = conv_cmd(input("Введите координаты вашего выстрела или воспользуйтесь подсказкой: "))
                check_exit(command)
                if command == "подсказка":
                    tip(computer_field)
                    command = conv_cmd(input("Введите координаты вашего выстрела: "))
                    check_exit(command)

                user_shot = Shot(int(command[1:]) - 1, coordinates_dict[command[0]])
                if computer_field.data[user_shot.row][user_shot.column] == "▣":
                    user_shot.hit = True
                    computer_field.shots.append(user_shot)
                    print_fields(user_field, computer_field)
                    print("Вы попали!")
                else:
                    computer_field.shots.append(user_shot)
                    print_fields(user_field, computer_field)
                    print("Вы промахнулись!")

            case _:
                print("Такой команды нет! Попробуйте еще раз!")
                command = conv_cmd(input("> "))
                check_exit(command)

    # cors = [[(0, 1), 0], [(2, 3), 3], [(0, 1), 4], [(3, 4), 4]]
    # print(check_tank_coordinate([(2, 3), 3], cors))

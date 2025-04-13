CELL_DESIGN = {"empty": "▢", "tank": "▣", "miss": "◼", "hit": "✘"}

coordinates_dict = {"а": 0, "б": 1, "в": 2, "г": 3, "д": 4, "е": 5, "ж": 6, "з": 7, "и": 8, "к": 9}


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
            result.append(((coord1, coord2), column))
        else:
            cord1 = int(coord[1:]) - 1  # Координата.
            result.append(((cord1, cord1), column))

    return result


def check_tank_coordinate(searched_coord: tuple, coordinates: list) -> bool:
    """Проверяет корректность координаты танка на поле.

    Args:
        searched_coord: Координаты искомого танка.
        coordinates: Список координат всех танков на поле.

    Returns:
        True - если координаты танка корректны, False - если нет.
    """
    is_correctly = True
    for coord in coordinates:
        if searched_coord == coord:
            continue
        rows, column = coord[0], coord[1]
        if searched_coord[0][0] - 1 <= rows[1] and searched_coord[0][1] + 1 >= rows[0]:
            if searched_coord[1] - 1 <= column <= searched_coord[1] + 1:
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
            user_field.tanks = [Tank(tank[0], tank[1]) for tank in coordinates]
        else:
            print("Некорректные координаты танков!")
            return False

    return True


def tip() -> str:
    """
    Выводит подсказку для игрока если он правильно решил пример.

    Returns:
        Подсказка игрока.
    """
    ...



class Tank:

    def __init__(self, rows: tuple[int, int], column: int):
        self.rows = rows  # Индексы строк, где расположен танк.
        self.column = column  # Индекс столбца, где расположен танк.


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
    """

    def __init__(self):
        # Заполнение пустого поля.
        self.data = [
            [CELL_DESIGN["empty"] for column in range(10)] for row in range(10)
        ]
        # Нужно заполнять только для пользовательского поля.
        self.tanks: list[Tank] = []
        self.shots: list[Shot] = []

    def fill_field(self):
        """Заполняет поле условными символами."""
        # Расстановка танков на поле.
        for tank in self.tanks:
            for row in tank.rows:
                self.data[row][tank.column] = CELL_DESIGN["tank"]
        # Расстановка выстрелов на поле.
        for shot in self.shots:
            self.data[shot.row][shot.column] = (
                CELL_DESIGN["hit"] if shot.hit else CELL_DESIGN["miss"]
            )


def print_fields(player_field: Field, computer_field: Field):
    # Создание заголовка с буквами, где THSP - символ тонкого пробела.
    letters = "  ".join(list("АБВГДЕЖЗИК"))
    letters = letters.replace("Д", " Д")
    result = f"   {letters}         {letters}\n"

    # Актуализируем данные на полях.
    player_field.fill_field()
    computer_field.fill_field()

    for index, row_data in enumerate(
        zip(player_field.data, computer_field.data)
    ):
        row_number = f" {index + 1}"[-2:]  # Номер строки из двух символов.
        # Данные пользовательского поля.
        result += f"{row_number} {' '.join(row_data[0])}"
        # Данные поля компьютера.
        result += " " * 5 + f"{row_number} {' '.join(row_data[1])}\n"
    print(result)


if __name__ == "__main__":
    # Пример использования функции отрисовки поля.
    # player_field_example = Field()
    # player_field_example.tanks = [Tank((0, 1), 1)]
    #
    # # Создаем выстрел отдельно, чтобы отметить его успешным.
    # successful_shot = Shot(0, 1)
    # successful_shot.hit = True  # Успешное попадание.
    #
    # player_field_example.shots = [successful_shot, Shot(2, 3)]
    #
    # computer_field_example = Field()
    # computer_field_example.shots = [Shot(9, 2), Shot(6, 6)]
    #
    # print_fields(player_field_example, computer_field_example)
    print("Привет! Это игра танковый бой!",
          "Если вы хотите ознакомиться с правилами игры, напишите 'помощь'.",
          "Чтобы начать игру, вам нужно написать 'старт'.", sep="\n")

    command = input("> ").strip()
    while command != "выход":
        match command:
            case "помощь":
                print("Правила игры: ")
                command = input("> ").strip()
            case "старт":
                print("Игра началась!")
                user_field = Field()

                tanks = input("Введите координаты ваших танков через пробел: ").split()
                tanks = converted_coords(tanks)  # конвертируем координаты танков
                while not check_tanks_coordinates(tanks):
                    tanks = input("Введите координаты ваших танков через пробел: ").split()
                    tanks = converted_coords(tanks)

                command = input("Введите координаты вашего выстрела или воспользуйтесь подсказкой: ").strip()
                if command == "подсказка":
                    tip()
            case _:
                print("Такой команды нет! Попробуйте еще раз!")
                command = input("> ").strip()
    # cors = [[(0, 1), 0], [(2, 3), 3], [(0, 1), 4], [(3, 4), 4]]
    # print(check_tank_coordinate([(2, 3), 3], cors))

CELL_DESIGN = {"empty": "▢", "tank": "▣", "miss": "◼", "hit": "✘"}


class Tank:

    def __init__(self, rows: tuple[int, int], column: int):
        self.rows = rows  # Индексы строк, на которых располагается танк.
        self.column = column  # Индекс столбца, на котором располагается танк.


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
    letters = letters.replace("Д", " Д ")
    result = f"   {letters}          {letters}\n"

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
    player_field_example = Field()
    player_field_example.tanks = [Tank((0, 1), 1)]

    # Создаем выстрел отдельно, чтобы отметить его успешным.
    successful_shot = Shot(0, 1)
    successful_shot.hit = True  # Успешное попадание.

    player_field_example.shots = [successful_shot, Shot(2, 3)]

    computer_field_example = Field()
    computer_field_example.shots = [Shot(9, 2), Shot(6, 6)]

    print_fields(player_field_example, computer_field_example)

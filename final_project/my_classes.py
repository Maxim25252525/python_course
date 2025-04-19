CELL_DESIGN = {"empty": "▢", "tank": "▣", "miss": "◼", "hit": "✘"}


class Tank:

    def __init__(self, rows: tuple[int, int], column: int):
        self.rows = rows  # Индексы строк, где расположен танк.
        self.column = column  # Индекс столбца, где расположен танк.
        self.length = 1 + rows[1] - rows[0]  # Длина танка.

    # Метод сравнения объектов
    # Теперь объекты сравниваются по атрибутам.
    def __eq__(self, other):
        if not isinstance(other, Tank):
            return False
        return self.rows == other.rows and self.column == other.column


class Shot:

    def __init__(self, row: int, column: int):
        self.row = row  # Индекс строки, куда произведен выстрел.
        self.column = column  # Индекс столбца, куда произведен выстрел.
        self.hit: bool = False  # Признак попадания.

    def __eq__(self, other):
        if not isinstance(other, Shot):
            return False
        return self.row == other.row and self.column == other.column


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
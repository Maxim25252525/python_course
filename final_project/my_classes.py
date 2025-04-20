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
        placement: Словарь для расстановки танков на поле.
        remembered_shots: Список выстрелов, которые не будут отображаться,
        но будут запомнены.
    """

    def __init__(self):
        # Заполнение пустого поля.
        self.data = [
            [CELL_DESIGN["empty"] for column in range(10)] for row in range(10)
        ]
        self.tanks: list[Tank] = []
        self.shots: list[Shot] = []
        self.placement = {5: 1, 4: 1, 3: 2, 2: 3, 1: 3}
        self.remembered_shots = []


class User(Field):
    """
    Класс пользователя.

    Поле представлено в виде списка строк,
    каждая из которых - это список столбцов
    - условных обозначений из CELL_DESIGN.

    Attributes:
        data: Двумерный список, содержащий поле.
        tanks: Список танков.
        shots: Список выстрелов, производимых по инициализированному полю.
        placement: Словарь для расстановки танков на поле.
        remembered_shots: Список выстрелов, которые не будут отображаться,
        но будут запомнены.
        """
    def fill_field(self):
        """Заполняет поле условными символами."""
        # Расстановка танков на поле.
        for tank in self.tanks:
            for row in range(tank.rows[0], tank.rows[1] + 1):
                self.data[row][tank.column] = CELL_DESIGN["tank"]
        # Расстановка выстрелов на поле.
        for shot in self.shots:
            self.data[shot.row][shot.column] = (
                CELL_DESIGN["hit"] if shot.hit else CELL_DESIGN["miss"]
            )

    def remember_shot(self, shot: Shot, destroyed: bool):
        """
        Запоминает выстрел.

        Args:
            shot: Выстрел.
            destroyed: Признак уничтожения танка.
        """
        if not destroyed:
            row = shot.row
            column = shot.column
            if column == 0:
                if row == 0:
                    pass
                elif row == 9:
                    pass
                else:
                    pass
                shot = Shot(row + 1, column)
                self.remembered_shots.append(shot)
            elif column == 9:
                if row == 0:
                    pass
                elif row == 9:
                    pass
                else:
                    pass
                shot = Shot(row - 1, column)
                self.remembered_shots.append(shot)
            else:
                if row == 0:
                    pass
                elif row == 9:
                    pass
                else:
                    pass
                shots = [Shot(row + 1, column), Shot(row - 1, column)]
                self.remembered_shots += shots
        else:
            pass

        self.shots.append(shot)


class Computer(Field):
    """
    Класс компьютера.

    Поле представлено в виде списка строк,
    каждая из которых - это список столбцов
    - условных обозначений из CELL_DESIGN.

    Attributes:
        data: Двумерный список, содержащий поле.
        tanks: Список танков.
        shots: Список выстрелов, производимых по инициализированному полю.
        placement: Словарь для расстановки танков на поле.
        remembered_shots: Список выстрелов, которые не будут отображаться,
        но будут запомнены.
    """
    def __init__(self, show: bool):
        """
        Инициализирует поле компьютера.

        Args:
            show: Показывает, отображать ли танки
        """
        super().__init__()
        self.show = show

    def fill_field(self):
        """Заполняет поле условными символами."""
        # Расстановка танков на поле.
        if self.show:
            for tank in self.tanks:
                for row in range(tank.rows[0], tank.rows[1] + 1):
                    self.data[row][tank.column] = CELL_DESIGN["tank"]
        # Расстановка выстрелов на поле.
        for shot in self.shots:
            self.data[shot.row][shot.column] = (
                CELL_DESIGN["hit"] if shot.hit else CELL_DESIGN["miss"]
            )

    def remember_shot(self, shot: Shot):
        """
        Запоминает выстрел.

        Args:
            shot: Выстрел.
        """
        self.remembered_shots.append(shot)

import random

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

    def __hash__(self):
        return hash((self.row, self.column))

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
            [CELL_DESIGN["empty"] for _ in range(10)] for _ in range(10)
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
        saved_shot: Отложенный выстрел.
        direction: Показывает, как изменить следующий выстрел
        (сделать больше или меньше).

        """

    def __init__(self):
        super().__init__()
        self.saved_shot: Shot | None = None
        self.direction: str | None = None
        self.remembered_shots = set()

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

    def remember_shot(self, shot: Shot, destroyed: bool,
                      tank: Tank | None = None) -> Shot:
        """
        Запоминает выстрел.

        Args:
            shot: Выстрел.
            destroyed: Признак уничтожения танка.
            tank: Танк.
            (Указывается только при уничтожении танка).

        Returns:
            Следующий выстрел.
        """
        row = shot.row
        column = shot.column

        # Заполняем клетки, в которых точно нет танка.
        if column == 0:
            self.remembered_shots.add(Shot(row, column + 1))
            shot.hit = True
        elif column == 9:
            self.remembered_shots.add(Shot(row, column - 1))
            shot.hit = True
        else:
            self.remembered_shots.add(Shot(row, column - 1))
            self.remembered_shots.add(Shot(row, column + 1))

        if not destroyed:
            # Возвращаем клетку, в который может быть танк.
            if row == 0:
                next_shot = Shot(1, column)
                if next_shot in self.shots:
                    next_shot = self.saved_shot
                self.direction = 'up'
            elif row == 9:
                next_shot = Shot(8, column)
                if next_shot in self.shots:
                    next_shot = self.saved_shot
                self.direction = 'down'
            else:
                if self.direction == 'up':
                    next_shot = Shot(row + 1, column)
                elif self.direction == 'down':
                    next_shot = Shot(row - 1, column)
                else:
                    if self.saved_shot is None:
                        option1 = Shot(row + 1, column)
                        option2 = Shot(row - 1, column)
                        chosen = random.choice([option1, option2])
                        self.saved_shot = option2 if chosen == option1 else option1
                        self.direction = 'up' if chosen == option1 else 'down'
                        next_shot = chosen
                        return next_shot
                    else:
                        next_shot = self.saved_shot
                        if self.direction == 'isup':
                            next_shot.row += 1
                            self.direction = 'up'
                        else:
                            next_shot.row -= 1
                            self.direction = 'down'

        else:
            self.direction = None
            self.saved_shot = None

            # Запомнили клетки снизу и сверху, в которых точно нет танка.
            length = tank.length
            row1 = tank.rows[0]
            row2 = tank.rows[1]
            if row == 0:
                self.remembered_shots.add(Shot(row + length, column))
            elif row == 9:
                self.remembered_shots.add(Shot(row - length, column))
            else:
                self.remembered_shots.add(Shot(row1 - 1, column))
                self.remembered_shots.add(Shot(row2 + 1, column))

            # Запомнили диагональные клетки, в которых точно нет танка.
            d1 = Shot(row1 - 1, column - 1)
            d2 = Shot(row1 - 1, column + 1)
            d3 = Shot(row2 + 1, column - 1)
            d4 = Shot(row2 + 1, column + 1)
            diagonals = [
                lambda x: x in [d1, d2, d3, d4]
                if 0 <= x.row <= 9 and 0 <= x.column <= 9
                else None
            ]
            self.remembered_shots.update(diagonals)

            # Придумали новый выстрел.
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            next_shot = Shot(row, column)
            while (next_shot in self.remembered_shots
                   or next_shot in self.shots):
                row = random.randint(0, 9)
                column = random.randint(0, 9)
                next_shot = Shot(row, column)

        return next_shot


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

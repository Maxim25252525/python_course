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
        saved_shot: Отложенный выстрел.
        direction: Показывает, как изменить следующий выстрел
        (сделать больше или меньше).

        """

    def __init__(self):
        super().__init__()
        self.saved_shot: Shot | None = None
        self.direction: str | None = None

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
        # TODO: Если сохраняется одно число, то оно не сохраняется до
        #  следующего вызова, но сохраняется в main как-то, иначе
        #  первое число сохраняется где-то в main, а второе сохраняется
        #  до следующего вызова.
        if not destroyed:
            row = shot.row
            column = shot.column

            # Заполняем клетки, в которых точно нет танка.
            if column == 0:
                self.remembered_shots.append(Shot(row, column + 1))
            elif column == 9:
                self.remembered_shots.append(Shot(row, column - 1))
            else:
                self.remembered_shots.append(Shot(row, column - 1))
                self.remembered_shots.append(Shot(row, column + 1))

            self.shots.append(shot)  # Добавляем выстрел компьютера в список.

            # Возвращаем клетку, в который может быть танк.
            if row == 0:
                next_shot = Shot(1, column)
                self.direction = 'up'
            elif row == 9:
                next_shot = Shot(8, column)
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
                    else:
                        next_shot = self.saved_shot
                        self.saved_shot = (
                            Shot(row + 1, column) if self.direction == 'isup'
                            else Shot(row - 1, column) if self.direction == 'isdown'
                            else None
                        )

            return next_shot
        else:
            self.direction = None
            self.saved_shot = None


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

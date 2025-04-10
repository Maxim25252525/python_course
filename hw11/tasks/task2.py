"""
# Задание 2: Жилищный вопрос +1

Реализуйте класс 'Flat', описывающий квартиру. При создании экземпляра класс
должен принимать 3 аргумента:
- Количество комнат (целочисленный тип).
- Количество окон (целочисленный тип).
- Количество санузлов (целочисленный тип).

Экземпляр класса 'Flat' должен иметь следующие атрибуты:
- rooms - количество комнат.
- windows - количество окон.
- bathrooms - количество санузлов.
- laundry - прачечная (логический тип). По умол. False.

> Комнаты, окна и санузлы задаются сразу при постройке дома.
Есть в нём прачечная или нет - зависит от владельца. Поэтому при создании
нового объекта этот параметр не указывается, но может быть изменен в процессе
жизни объекта.

Если количество комнат меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество комнат должно быть больше 0'
Если количество окон меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество окон должно быть больше 0'
Если количество санузлов меньше 0 - вызвать исключение типа ValueError с
описанием: 'Количество санузлов должно быть больше или равно 0'

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает информацию о квартире в формате: 'Квартира состоит из
<количество комнат> комнат(ы). Количество окон в квартире - <количество окон>.
Санузлов - <количество санузлов>. В квартире <есть прачечная/нет прачечной>.'
Например: Квартира состоит из 3 комнат(ы). Количество окон в квартире - 4.
Санузлов - 1. В квартире есть прачечная.

Реализуйте класс 'Garage', описывающий гараж. При создании экземпляра класс
должен принимать 1 аргумент:
- Площадь гаража (вещественный тип). Измеряется в квадратных метрах.

Экземпляр класса 'Garage' должен иметь следующие атрибуты:
- square - Площадь гаража (вещественный тип). Измеряется в квадратных метрах.
- warm - Теплый гараж или нет (логический тип). По умол. False.

Если площадь гаража меньше или равна 0 - вызвать исключение типа ValueError с
описанием: 'Площадь гаража должна быть больше 0'

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает информацию о гараже в формате: 'Гараж <отапливаемый/
неотапливаемый> площадью <площадь гаража> м^2.'.
Например: Гараж отапливаемый площадью 10 м^2.

Создайте наследника класса 'Flat' и 'Garage' - класс 'Home', описывающий дом.
При создании экземпляра класс должен принимать 5 аргументов:
- Количество комнат (целочисленный тип).
- Количество окон (целочисленный тип).
- Количество санузлов (целочисленный тип).
- Площадь гаража (вещественный тип). Измеряется в квадратных метрах.
- Количество этажей (целочисленный тип).

> Базовые классы указываются в том же порядке, в котором они описаны выше.

Экземпляр класса 'Home' должен иметь следующие атрибуты, помимо базовых:
- floors - количество этажей.
- loft - чердак (логический тип). По умол. False.
- basement - подвал (логический тип). По умол. True.

> Чердак не передается в конструктор, так как после возведения дома его можно
достроить.
> Подвал не передается в контруктор, так как после возведения дома его можно
замуровать.

Если количество этажей меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество этажей должно быть больше 0'

Класс должен переопределять базовый метод:
- get_info - возвращает информацию о доме в формате: 'Дом имеет <количество
этажей> этажа/этажей. Состоит из <количество комнат> комнат(ы). Количество
окон в доме - <количество окон>. Санузлов - <количество санузлов>. В доме <есть
прачечная/нет прачечной>. Также в доме есть <отапливаемый/ не отапливаемый>
гараж площадью <площадь гаража> м^2. <Есть чердак/Нет чердака>. <Есть подвал/
Нет подвала>.'
Например: Дом имеет 2 этажа/этажей. Состоит из 6 комнат(ы). Количество окон в
доме - 8. Санузлов - 2. В доме есть прачечная. Также в доме есть отапливаемый
гараж площадью 15 м^2. Нет чердака. Есть подвал.

Под блоком if __name__ == '__main__':
1. Создайте экземпляр класса, передав необходимые аргументы.
2. Проверьте взаимодействие с атрибутами и методами класса.

Добавьте докстринги (описание классов и методов) и аннотации типов (указание
типов параметров и возвращаемых значений) для каждого метода и класса.
"""


class Flat:
    """
    Класс, описывающий квартиру.

    Args:
        rooms: Количество комнат.
        windows: Количество окон.
        bathrooms: Количество санузлов.

    Attributes:
        rooms: Количество комнат.
        windows: Количество окон.
        bathrooms: Количество санузлов.
        laundry: Есть прачечная или нет. По умолчанию False.
    """

    def __init__(self, rooms: int, windows: int, bathrooms: int):
        """
        Инициализация объекта класса Flat.

        Args:
            rooms: Количество комнат.
            windows: Количество окон.
            bathrooms: Количество санузлов.
        """

        if rooms < 1:
            raise ValueError("Количество комнат должно быть больше 0")
        elif windows < 1:
            raise ValueError("Количество окон должно быть больше 0")
        elif bathrooms < 0:
            raise ValueError(
                "Количество санузлов должно быть больше или равно 0"
            )

        self.rooms = rooms
        self.windows = windows
        self.bathrooms = bathrooms
        self.laundry = False

    def get_info(self) -> str:
        """
        Возвращает информацию о квартире.

        Returns:
            Возвращает количество комнат, количество окон, количество санузлов
            и наличие прачечной в квартире.
        """
        return (
            f"Квартира состоит из {self.rooms} комнат(ы). "
            f"Количество окон в квартире - {self.windows}. "
            f"Санузлов - {self.bathrooms}. "
            f"В квартире "
            f"{'есть прачечная' if self.laundry else 'нет прачечной'}."
        )


class Garage:
    """Класс, описывающий гараж.

    Args:
        square: Площадь гаража.

    Attributes:
        square: Площадь гаража.
        warm: Отапливаемый или нет. По умолчанию False.

    """

    def __init__(self, square: float):
        """
        Инициализация объекта класса Garage.

        Args:
            square: Площадь гаража.
        """
        if square <= 0:
            raise ValueError("Площадь гаража должна быть больше 0")

        self.square = square
        self.warm = False

    def get_info(self) -> str:
        """
        Возвращает информацию о гараже.

        Returns:
            Возвращает площадь гаража и наличие отопления в гараже.
        """
        return (
            f"Гараж {'отапливаемый' if self.warm else 'неотапливаемый'} "
            f"площадью {self.square} м^2."
        )


class Home(Flat, Garage):
    """Класс, описывающий дом.

    Args:
        rooms: Количество комнат.
        windows: Количество окон.
        bathrooms: Количество санузлов.
        square: Площадь гаража.
        floors: Количество этажей.

    Attributes:
        rooms: Количество комнат.
        windows: Количество окон.
        bathrooms: Количество санузлов.
        garage_square: Площадь гаража.
        floors: Количество этажей.
        loft: Есть чердак или нет. По умолчанию False.

    """

    def __init__(
        self,
        rooms: int,
        windows: int,
        bathrooms: int,
        square: float,
        floors: int,
    ):
        """
        Инициализация объекта класса Home.

        Args:
            rooms: Количество комнат.
            windows: Количество окон.
            bathrooms: Количество санузлов.
            square: Площадь гаража.
            floors: Количество этажей.
        """
        if floors < 1:
            raise ValueError("Количество этажей должно быть больше 0")

        Garage.__init__(self, square)
        Flat.__init__(self, rooms, windows, bathrooms)
        self.rooms = rooms
        self.windows = windows
        self.bathrooms = bathrooms
        self.garage_square = square
        self.floors = floors
        self.loft = False
        self.basement = True

    def get_info(self) -> str:
        """
        Возвращает информацию о доме.

        Returns:
            Возвращает информацию о доме, включая количество этажей,
            количество комнат, количество окон, количество санузлов,
            наличие прачечной, площадь гаража,
            наличие отопления в гараже, наличие чердака и наличие подвала.
        """
        return (
            f"Дом имеет {self.floors} этажа/этажей. "
            f"Состоит из {self.rooms} комнат(ы). "
            f"Количество окон в доме - {self.windows}. "
            f"Санузлов - {self.bathrooms}. "
            f"В доме {'есть прачечная' if self.laundry else 'нет прачечной'}. "
            f"Также в доме есть "
            f"{'отапливаемый' if self.warm else 'не отапливаемый'} гараж "
            f"площадью {self.garage_square} м^2. "
            f"{'Есть чердак' if self.loft else 'Нет чердака'}. "
            f"{'Есть подвал' if self.basement else 'Нет подвала'}."
        )


if __name__ == "__main__":
    my_home = Home(rooms=5, windows=8, bathrooms=3, square=100, floors=2)
    print(my_home.get_info())

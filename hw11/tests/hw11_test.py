import pytest

from hw11.tasks import task1, task2


class TestHw11Task1:

    @pytest.mark.parametrize(
        ("gemstone", "result_name", "result_carat"),
        [
            (
                task1.Gemstone("Драгоценность", 0.99),
                "Название: Драгоценность",
                "Карат: 0.99",
            ),
            (
                task1.Gemstone("Драгоценность", 1.0),
                "Название: Драгоценность",
                "Карат: 1.0",
            ),
        ],
    )
    def test_gemstone(self, gemstone, result_name, result_carat):
        assert gemstone.get_name() == result_name
        assert gemstone.get_carat() == result_carat

    @pytest.mark.parametrize(
        ("diamond", "result_name", "result_carat", "result_diameter"),
        [
            (
                task1.Diamond("Драгоценность", 0.55, 6.4),
                "Название: Драгоценность",
                "Карат: 0.55",
                "Диаметр: 6.4 мм",
            ),
            (
                task1.Diamond("Драгоценность", 2.0, 6.0),
                "Название: Драгоценность",
                "Карат: 2.0",
                "Диаметр: 6.0 мм",
            ),
        ],
    )
    def test_diamond(
        self, diamond, result_name, result_carat, result_diameter
    ):
        assert diamond.get_name() == result_name
        assert diamond.get_carat() == result_carat
        assert diamond.get_diameter() == result_diameter

    @pytest.mark.parametrize(
        (
            "brilliant",
            "result_name",
            "result_carat",
            "result_diameter",
            "result_cost",
        ),
        [
            (
                task1.Brilliant("Драгоценность", 1.143, 1.4, 150000.99),
                "Название: Драгоценность",
                "Карат: 1.143",
                "Диаметр: 1.4 мм",
                "Стоимость: 150000.99 руб.",
            ),
            (
                task1.Brilliant("Драгоценность", 0.95, 2.0, 154789.99),
                "Название: Драгоценность",
                "Карат: 0.95",
                "Диаметр: 2.0 мм",
                "Стоимость: 154789.99 руб.",
            ),
        ],
    )
    def test_brilliant(
        self,
        brilliant,
        result_name,
        result_carat,
        result_diameter,
        result_cost,
    ):
        assert brilliant.get_name() == result_name
        assert brilliant.get_carat() == result_carat
        assert brilliant.get_diameter() == result_diameter
        assert brilliant.get_cost() == result_cost


class TestHw11Task2:

    @pytest.mark.parametrize(
        ("flat", "laundry", "result"),
        [
            (
                task2.Flat(3, 4, 1),
                True,
                "Квартира состоит из 3 комнат(ы). "
                "Количество окон в квартире - 4. Санузлов - 1. "
                "В квартире есть прачечная.",
            ),
            (
                task2.Flat(1, 2, 0),
                False,
                "Квартира состоит из 1 комнат(ы). "
                "Количество окон в квартире - 2. Санузлов - 0. "
                "В квартире нет прачечной.",
            ),
        ],
    )
    def test_flat(self, flat, laundry, result):
        flat.laundry = laundry
        assert flat.get_info() == result

    @pytest.mark.parametrize(
        ("rooms", "windows", "bathrooms"),
        [
            (-100, 4, 1),
            (-1, 4, 1),
            (0, 4, 1),
        ],
    )
    def test_flat_raise_count_rooms(self, rooms, windows, bathrooms):
        with pytest.raises(ValueError) as ex:
            task2.Flat(rooms, windows, bathrooms)
        assert "Количество комнат должно быть больше 0" == str(ex.value)

    @pytest.mark.parametrize(
        ("rooms", "windows", "bathrooms"),
        [
            (1, -1000, 1),
            (2, -1, 1),
            (3, 0, 2),
        ],
    )
    def test_flat_raise_count_windows(self, rooms, windows, bathrooms):
        with pytest.raises(ValueError) as ex:
            task2.Flat(rooms, windows, bathrooms)
        assert "Количество окон должно быть больше 0" == str(ex.value)

    @pytest.mark.parametrize(
        ("rooms", "windows", "bathrooms"),
        [
            (1, 4, -101),
            (2, 4, -2),
            (3, 6, -1),
        ],
    )
    def test_flat_raise_count_bathrooms(self, rooms, windows, bathrooms):
        with pytest.raises(ValueError) as ex:
            task2.Flat(rooms, windows, bathrooms)
        assert "Количество санузлов должно быть больше или равно 0" == str(
            ex.value
        )

    @pytest.mark.parametrize(
        ("garage", "warm", "result"),
        [
            (
                task2.Garage(10.5),
                True,
                "Гараж отапливаемый площадью 10.5 м^2.",
            ),
            (
                task2.Garage(0.001),
                False,
                "Гараж неотапливаемый площадью 0.001 м^2.",
            ),
        ],
    )
    def test_garage(self, garage, warm, result):
        garage.warm = warm
        assert garage.get_info() == result

    @pytest.mark.parametrize(
        "square",
        [-1000, -100, -1, 0],
    )
    def test_garage_raise_square(self, square):
        with pytest.raises(ValueError) as ex:
            task2.Garage(square)
        assert "Площадь гаража должна быть больше 0" == str(ex.value)

    @pytest.mark.parametrize(
        ("home", "loft", "basement", "result"),
        [
            (
                task2.Home(6, 14, 2, 15, 2),
                False,
                True,
                "Дом имеет 2 этажа/этажей. Состоит из 6 комнат(ы). "
                "Количество окон в доме - 14. Санузлов - 2. "
                "В доме нет прачечной. Также в доме есть не "
                "отапливаемый гараж площадью 15 м^2. "
                "Нет чердака. Есть подвал.",
            ),
            (
                task2.Home(3, 4, 1, 10.1, 1),
                True,
                False,
                "Дом имеет 1 этажа/этажей. Состоит из 3 комнат(ы). "
                "Количество окон в доме - 4. Санузлов - 1. "
                "В доме нет прачечной. Также в доме есть не "
                "отапливаемый гараж площадью 10.1 м^2. "
                "Есть чердак. Нет подвала.",
            ),
            (
                task2.Home(9, 15, 3, 20.21, 3),
                True,
                True,
                "Дом имеет 3 этажа/этажей. Состоит из 9 комнат(ы). "
                "Количество окон в доме - 15. Санузлов - 3. "
                "В доме нет прачечной. Также в доме есть не "
                "отапливаемый гараж площадью 20.21 м^2. "
                "Есть чердак. Есть подвал.",
            ),
        ],
    )
    def test_home(self, home, loft, basement, result):
        home.loft = loft
        home.basement = basement
        assert home.get_info() == result

    @pytest.mark.parametrize(
        "floors",
        [-100, -1, 0],
    )
    def test_home_raise_floors(self, floors):
        with pytest.raises(ValueError) as ex:
            task2.Home(1, 2, 1, 10, floors)
        assert "Количество этажей должно быть больше 0" == str(ex.value)

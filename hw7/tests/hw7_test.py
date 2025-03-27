import pytest

from hw7.tasks import task1, task2, task3


class TestHw7Task1:

    @pytest.mark.parametrize(
        ("text", "result"),
        [
            ("I sit on bed", "Я сидеть на кровать"),
            ("I hear his cat", "Я слышать его ..."),
            ("I sIt On BEd", "Я сидеть на кровать"),
            ("I HEAR his CAT", "Я слышать его ..."),
            ("Eye is life", "Глаз это жизнь"),
            ("Eyes is life peoples", "... это жизнь ..."),
            (
                "Adult kids is nerves for their parent",
                "Взрослый ... это ... ... их ...",
            ),
        ],
    )
    def test_translate(self, text, result):
        assert task1.translate_text(text) == result


@pytest.fixture
def get_dictionary_contacts():
    return {
        "Билл Гейтс": "+79000375594",
        "Илон Маск": "+79024700417",
        "Уоррен Баффетт": "+79086098273",
        "Евгений Касперский": "+79302378514",
        "Александр Шулико": "+79023342723",
        "Билли Айлиш": "+79027539801",
    }


class TestHw7Task2:

    def test_create_dictionary_from_string(self, get_dictionary_contacts):
        assert task2.create_dictionary_from_string() == get_dictionary_contacts

    @pytest.mark.parametrize(
        ("name", "result"),
        [
            (
                "билл",
                {"Билл Гейтс": "+79000375594", "Билли Айлиш": "+79027539801"},
            ),
            (
                "Билл",
                {"Билл Гейтс": "+79000375594", "Билли Айлиш": "+79027539801"},
            ),
            (
                "БИлЛ",
                {"Билл Гейтс": "+79000375594", "Билли Айлиш": "+79027539801"},
            ),
            ("маск", {"Илон Маск": "+79024700417"}),
            (
                "ли",
                {
                    "Александр Шулико": "+79023342723",
                    "Билли Айлиш": "+79027539801",
                },
            ),
            ("такса", "Нет информации"),
        ],
    )
    def test_search_contact_in_dictionary_contacts(
        self, name, result, get_dictionary_contacts
    ):
        assert task2.search_contact(name, get_dictionary_contacts) == result

    def test_search_contact_in_empty_dict(self):
        assert task2.search_contact("Билл", {}) == "Нет информации"


class TestHw7Task3:

    @pytest.mark.parametrize(
        ("degrees", "result"),
        [
            (
                [
                    20,
                    20,
                    20,
                    20,
                    20.23,
                    20.23,
                    20.54,
                    20.546789,
                    20.71,
                    20.80,
                    21,
                    21,
                    21,
                    21,
                    21,
                ],
                {
                    "unique_degrees": {
                        20.71,
                        20.54,
                        20.546789,
                        20.0,
                        20.23,
                        20.8,
                        21.0,
                    },
                    "average_temperature": 20.537119266666664,
                },
            ),
            ([20], {"unique_degrees": {20.0}, "average_temperature": 20.0}),
            (
                [
                    -10,
                    -9,
                    -8.5,
                    0,
                    1,
                    1.21,
                    2.2,
                    2.2,
                    0,
                    0,
                    5,
                    4.98,
                    3.21,
                    -10,
                    10,
                    -2,
                ],
                {
                    "unique_degrees": {
                        0,
                        1,
                        1.21,
                        2.2,
                        4.98,
                        5,
                        3.21,
                        10,
                        -10,
                        -9,
                        -8.5,
                        -2,
                    },
                    "average_temperature": -0.60625,
                },
            ),
        ],
    )
    def test_create_weather_report(self, degrees, result):
        assert task3.create_weather_report(degrees) == result

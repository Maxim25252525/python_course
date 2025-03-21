import pytest

from hw6.tasks import task1, task2, task3, task4


@pytest.fixture
def get_list_even_numbers():
    return [3, 4, 5, 6, 7, 8, 1, 2]


@pytest.fixture
def get_list_odd_numbers():
    return [100, 200, 145, -100, 0, 10, -14]


class TestHw6Task1:

    def test_get_central_element_even(self, get_list_even_numbers):
        assert task1.get_central_element(get_list_even_numbers) == (6, 7)

    def test_get_central_element_odd(self, get_list_odd_numbers):
        assert task1.get_central_element(get_list_odd_numbers) == -100

    def test_get_latest_sorted_items_even(self, get_list_even_numbers):
        assert task1.get_latest_sorted_items(get_list_even_numbers) == (7, 8)

    def test_get_latest_sorted_items_odd(self, get_list_odd_numbers):
        assert task1.get_latest_sorted_items(get_list_odd_numbers) == (
            145,
            200,
        )

    def test_check_hundred_even(self, get_list_even_numbers):
        assert task1.check_hundred(get_list_even_numbers) == "NO"

    def test_check_hundred_odd(self, get_list_odd_numbers):
        assert task1.check_hundred(get_list_odd_numbers) == "YES"


class TestHw6Task2:

    @pytest.mark.parametrize(
        ("numbers", "result"),
        [
            ([1, 2, 3, 4, 25, 27, 35], (25, 27)),
            ([12, 12], (12, 12)),
            ([-1, -2, -12, -25, 0, 12, 22, 23, 29, 30], (12, 29)),
            ([12, 22, 30, 23], (12, 23)),
            ([23, 30, 22, 12], (23, 12)),
        ],
    )
    def test_check_hundred(self, numbers, result):
        assert task2.filter_numbers(numbers) == result


class TestHw6Task3:

    @pytest.mark.parametrize(
        ("text", "result"),
        [
            (
                "Сегодня мы пойдем в гости",
                "Сегоднясла мысла пойдемсла всла гостисла",
            ),
            (
                "А я учу предлоги",
                "Асла ясла учусла предлогисла",
            ),
        ],
    )
    def test_encrypt(self, text, result):
        assert task3.encrypt(text) == result

    @pytest.mark.parametrize(
        ("text", "result"),
        [
            (
                "Сегодня мы пойдем в гости!",
                "Сегоднясла мысла пойдемсла всла гостисла!",
            ),
            ("Привет! Как дела?", "Приветсла! Каксла деласла?"),
            (
                "А? я! учу, предлоги; такие, как: с, до, перед, под.",
                "Асла? ясла! учусла, предлогисла; такиесла, каксла: "
                "ссла, досла, передсла, подсла.",
            ),
        ],
    )
    def test_encrypt_with_punctuation(self, text, result):
        if task3.encrypt(text) != result:
            pytest.skip("Пунктуация не учтена")
        assert task3.encrypt(text) == result

    @pytest.mark.parametrize(
        ("text", "result"),
        [
            (
                "Сегоднясла мысла пойдемсла всла гостисла",
                "Сегодня мы пойдем в гости",
            ),
            (
                "Асла ясла учусла предлогисла",
                "А я учу предлоги",
            ),
        ],
    )
    def test_decrypt(self, text, result):
        assert task3.decrypt(text) == result

    @pytest.mark.parametrize(
        ("text", "result"),
        [
            (
                "Сегоднясла мысла пойдемсла всла гостисла!",
                "Сегодня мы пойдем в гости!",
            ),
            ("Приветсла! Каксла деласла?", "Привет! Как дела?"),
            (
                "Асла? ясла! учусла, предлогисла; такиесла, каксла: "
                "ссла, досла, передсла, подсла.",
                "А? я! учу, предлоги; такие, как: с, до, перед, под.",
            ),
        ],
    )
    def test_decrypt_with_punctuation(self, text, result):
        if task3.decrypt(text) != result:
            pytest.skip("Пунктуация не учтена")
        assert task3.decrypt(text) == result


class TestHw6Task4:

    @pytest.mark.parametrize(
        ("word", "text", "result"),
        [
            (
                "Лес",
                "Мой первый день в путешествии. Он начался на окраине леса."
                "Лес звал меня.",
                [(2, "Он начался на окраине леса"), (3, "Лес звал меня")],
            ),
            (
                "Отец",
                "Вот портфель. Пальто и шляпа. День у отца. Выходной. ОтЕц."
                "Что делать будем.",
                [(5, "ОтЕц")],
            ),
            (
                "ягодка",
                "Я программист,"
                "осознавший едва всю суть программистских контор."
                "Я миддл опять в мои двадцать два."
                "А в двадцать один был сеньор.",
                [],
            ),
            (
                "ОК",
                "Релиз горит, коллеги плачут."
                "Программа не готова в срок."
                "А мысль хаотично скачет."
                "Меж неработающих строк.",
                [
                    (2, "Программа не готова в срок"),
                    (4, "Меж неработающих строк"),
                ],
            ),
        ],
    )
    def test_encrypt(self, word, text, result):
        assert task4.search_word(word, text) == result

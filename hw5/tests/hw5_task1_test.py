#  Функции для тестирования
def is_tutor_in_string():
    string = "Сегодня Данил или Антон проверил мою работу"
    return "Данил" in string or "Антон" in string


def min_length_of_string():
    return len("ММММмаруСя") >= len("Маруся")


def is_string():
    return isinstance("Маруся", str)


# Тестирование
def test_is_tutor_in_string():
    assert is_tutor_in_string()


def test_min_length_of_string():
    assert min_length_of_string()


def test_is_string():
    assert is_string()

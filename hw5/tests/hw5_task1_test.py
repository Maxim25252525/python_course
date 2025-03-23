from hw5.tasks.task1 import get_answer


def test_get_answer_with_marusya():
    assert get_answer("frggrrgМАруСяfedd") == "Мяу..."


def test_get_answer_without_marusya():
    assert get_answer("feffegовва") == "..."


# строка содержит слово "Маруся",
# но 'a', 'p', 'y', 'с' в обоих регистрах или 'M' могут быть написаны не по-русски
def test_get_answer_with_marusya_in_english():
    assert get_answer("Мaруcя") == "..."
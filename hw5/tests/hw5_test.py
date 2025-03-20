import pytest

from hw5.tasks import task2


class TestHw5Task2:

    @pytest.mark.parametrize(
        ("a", "b", "result"),
        [(2, 4, 6), (2.5, 3.14, 5.64), (-1, 10, 9), (-1.4, 1.4, 0)],
    )
    def test_summarize(self, a, b, result):
        assert round(task2.summarize(a, b), 2) == result

    @pytest.mark.parametrize(
        ("a", "b", "result"),
        [(2, 4, 2), (2.5, 3.14, 0.64), (-1, 10, 11), (-1.4, 1.4, 2.8)],
    )
    def test_subtract(self, a, b, result):
        assert round(task2.subtract(a, b), 2) == result

    @pytest.mark.parametrize(
        ("a", "b", "result"),
        [
            (2, 4, 8),
            (2.5, 3.14, 7.85),
            (-1, 10, -10),
            (-1.4, 1.4, -1.96),
            (123.456, 0, 0),
        ],
    )
    def test_multiply(self, a, b, result):
        assert round(task2.multiply(a, b), 2) == result

    @pytest.mark.parametrize(
        ("a", "b", "result"),
        [
            (2, 4, 2),
            (2.5, 3.14, 1.256),
            (-1, 10, -10),
            (-1.4, 1.4, -1),
        ],
    )
    def test_divide(self, a, b, result):
        assert round(task2.divide(a, b), 3) == result

    def test_raise(self):
        with pytest.raises(ZeroDivisionError):
            task2.divide(10, 0)

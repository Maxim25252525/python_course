import pytest

from hw8.tasks import task1, task2, task3


class TestHw8Task1:

    def test_get_length(self):
        assert task1.get_length("Не баг,  а  фича! ") == 4


@pytest.fixture
def get_result_2_3():
    return {
        2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        3: [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],
    }


@pytest.fixture
def get_result_2_5_3():
    return {
        2: [1, 2, 4, 8],
        3: [1, 3, 9, 27],
        4: [1, 4, 16, 64],
        5: [1, 5, 25, 125],
    }


class TestHw8Task2:

    def test_get_degrees_2_3(self, get_result_2_3):
        assert task2.get_degrees(2, 3) == get_result_2_3

    def test_get_degrees_2_5_3(self, get_result_2_5_3):
        assert task2.get_degrees(2, 5, 3) == get_result_2_5_3

    def test_get_degrees_raise_parameter(self):
        with pytest.raises(ValueError) as ex:
            task2.get_degrees(10, 5)
        assert "Первый параметр больше второго" == str(ex.value)

    @pytest.mark.parametrize(
        ("start", "end", "degree"),
        [
            (2.5, 5, 10),
            (2, 5.5, 10),
            (2, 5, 10.1),
            ("2", 5, 10),
            (2, "5", 10),
            (2, 5, "10"),
            (2.5, "5", 10.123),
            ([], 5, 10),
            (2, [], 10),
            (2, 5, []),
        ],
    )
    def test_get_degrees_raise(self, start, end, degree):
        with pytest.raises(ValueError) as ex:
            task2.get_degrees(start, end, degree)
        assert "Параметр(ы) не являются натуральными числами" == str(ex.value)


class TestHw8Task3:

    def test_get_sum(self):
        assert (
            task3.get_sum(
                1,
                2,
                "3",
                2.5,
                "3,5",
                "1.5",
                [1, 2, 3],
                {1: 123, 2: 234},
                "abc 12",
                "12 abc",
            )
            == 13.5
        )

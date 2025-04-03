from hw8.tasks.task1 import get_length
from hw8.tasks.task2 import get_degrees
from hw8.tasks.task3 import get_sum
import pytest


@pytest.mark.parametrize(
    ("words", "result"),
    [
        ("hello", 1),
        ("hello world", 2),
        ("Hello world! How are you? ", 5),
        (" ", 0),
    ],
)
def test_get_length(words, result):
    assert get_length(words) == result


@pytest.mark.parametrize(
    ("start", "end", "degree", "result"),
    [
        (
            2,
            5,
            3,
            {
                2: [1, 2, 4, 8],
                3: [1, 3, 9, 27],
                4: [1, 4, 16, 64],
                5: [1, 5, 25, 125],
            },
        ),
        (
            2,
            3,
            10,
            {
                2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
                3: [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],
            },
        ),
        (
            1,
            9,
            2,
            {
                1: [1, 1, 1],
                2: [1, 2, 4],
                3: [1, 3, 9],
                4: [1, 4, 16],
                5: [1, 5, 25],
                6: [1, 6, 36],
                7: [1, 7, 49],
                8: [1, 8, 64],
                9: [1, 9, 81],
            },
        ),
        pytest.param(
            2, 5, -3, None, marks=pytest.mark.xfail(raises=ValueError)
        ),
        pytest.param(
            -100, -10, 3, None, marks=pytest.mark.xfail(raises=ValueError)
        ),
        pytest.param(
            1, 2, 3.14, None, marks=pytest.mark.xfail(raises=ValueError)
        ),
        pytest.param(
            10, 2, 3, None, marks=pytest.mark.xfail(raises=ValueError)
        ),
        pytest.param(
            -10, -2.5, -3.14, None, marks=pytest.mark.xfail(raises=ValueError)
        ),
    ],
)
def test_get_degrees(start, end, degree, result):
    assert get_degrees(start, end, degree) == result


@pytest.mark.parametrize(
    ("numbers", "result"),
    [
        (
            [
                1,
                2,
                "3",
                2.5,
                "3,5",
                "1.5",
                [1, 2, 3],
                {1: 123, 2: 234},
                "abc 12",
            ],
            13.5,
        ),
        ([], 0),
        ([1, "2,0", 3, "4,5", (1, 5), "0.000", 6.5], 17),
    ],
)
def test_get_sum(numbers, result):
    assert get_sum(*numbers) == result

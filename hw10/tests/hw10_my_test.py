import pytest
from hw10.tasks import task2 # noqa


@pytest.mark.parametrize(
    ("start", "end", "degree", "result"),
    [
        (
            1,
            3,
            "",
            {
                1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
                3: [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],
            },
        ),
        (
            1,
            2,
            "",
            {
                1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
            },
        ),
        (
            1,
            3,
            "a.degree = 2",
            {1: [1, 1, 1], 2: [1, 2, 4], 3: [1, 3, 9]},
        ),
    ],
)
def test_degree(start, end, degree, result):
    variables = {}
    exec(f'a = task2.Degree({start}, {end})\n'
         f'{degree}\n'
         f'a = a.get_degrees()', globals(), variables)
    assert variables['a'] == result

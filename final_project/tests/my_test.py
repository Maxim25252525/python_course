import pytest
from final_project import precode


@pytest.mark.parametrize(
    ("coordinate", "expression", "result"),
    [
        (
            ((0, 1), 0),
            [[(0, 1), 0], [(2, 3), 1], [(0, 1), 4], [(3, 4), 4]],
            False,
        ),
        (
            ((0, 1), 0),
            [[(0, 1), 0], [(1, 3), 2], [(0, 1), 4], [(3, 4), 4]],
            True,
        ),
        (
            ((2, 3), 3),
            [[(0, 1), 0], [(1, 2, 3), 3], [(0, 1), 4], [(3, 4), 4]],
            False,
        )
    ]
)
def test_check_tank_coordinate(coordinate, expression, result):
    assert precode.check_tank_coordinate(coordinate, expression) == result

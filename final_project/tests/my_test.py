import pytest
from final_project import precode
from final_project.precode import Tank


@pytest.mark.parametrize(
    ("coordinate", "expression", "result"),
    [
        (
            Tank((0, 1), 0),
            [Tank((0, 1), 0), Tank((3, 3), 1), Tank((0, 1), 4), Tank((3, 4), 4)],
            True,
        ),
        (
            Tank((0, 1), 0),
            [Tank((0, 1), 0), Tank((1, 3), 2), Tank((0, 1), 4), Tank((3, 4), 4)],
            True,
        ),
        (
            Tank((2, 3), 3),
            [Tank((0, 1), 0), Tank((1, 2), 3), Tank((0, 1), 4), Tank((3, 4), 4)],
            False,
        ),
(
            Tank((2, 3), 3),
            [Tank((0, 1), 0), Tank((0, 1), 0), Tank((0, 1), 4), Tank((3, 4), 4)],
            False,
        )
    ]
)
def test_check_tank_coordinate(coordinate, expression, result):
    assert precode.check_tank_coordinate(coordinate, expression) == result

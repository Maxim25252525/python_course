import pytest

from final_project.my_classes import Field, Tank, Shot
from final_project.my_functions import check_tank_coordinate, check_hit


@pytest.fixture
def make_tanks(player=True):
    if player:
        field = Field()
    else:
        field = Field(False)
    tanks = [
        Tank((0, 0), 0),
        Tank((2, 3), 2),
        Tank((4, 4), 4),
        Tank((6, 9), 6),
        Tank((6, 9), 0),
        Tank((6, 9), 9),
        Tank((0, 4), 9),
    ]
    field.tanks.extend(tanks)
    return field


@pytest.mark.parametrize(
    ("coordinate", "expression", "result"),
    [
        (
            Tank((0, 1), 0),
            [
                Tank((0, 1), 0),
                Tank((3, 3), 1),
                Tank((0, 1), 4),
                Tank((3, 4), 4),
            ],
            True,
        ),
        (
            Tank((0, 1), 0),
            [
                Tank((0, 1), 0),
                Tank((1, 3), 2),
                Tank((0, 1), 4),
                Tank((3, 4), 4),
            ],
            True,
        ),
        (
            Tank((2, 3), 3),
            [
                Tank((0, 1), 0),
                Tank((1, 2), 3),
                Tank((0, 1), 4),
                Tank((3, 4), 4),
            ],
            False,
        ),
        (
            Tank((2, 3), 3),
            [
                Tank((0, 1), 0),
                Tank((0, 1), 0),
                Tank((0, 1), 4),
                Tank((3, 4), 4),
            ],
            False,
        ),
    ],
)
def test_check_tank_coordinate(coordinate, expression, result):
    assert check_tank_coordinate(coordinate, expression) == result


@pytest.mark.parametrize(
    ("shot", "result"),
    [
        (Shot(0, 0), True),
        (Shot(0, 5), False),
        (Shot(4, 4), True),
        (Shot(8, 9), True),
        (Shot(6, 6), True),
        (Shot(9, 0), True),
        (Shot(3, 9), True),
        (Shot(5, 9), False),
    ],
)
def test_check_hit(make_tanks, shot, result):
    assert check_hit(shot, make_tanks, 'tank')[0] == result

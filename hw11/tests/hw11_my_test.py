import pytest
from hw11.tasks import task1


@pytest.mark.parametrize(('name', 'carat', 'result'), [
    ('Сапфир', 2.5, ['Название: Сапфир',
                     'Карат: 2.5'])
])
def test_gemstone(name, carat, result):
    my_brilliant = task1.Gemstone(name, carat)
    assert (my_brilliant.get_name(),
            my_brilliant.get_carat()) == (*result,)


@pytest.mark.parametrize(('name', 'carat', 'diameter', 'result'), [
    ('Сапфир', 2.5, 3.1, ['Название: Сапфир',
                          'Карат: 2.5',
                          'Диаметр: 3.1 мм'])
])
def test_diamond(name, carat, diameter, result):
    my_brilliant = task1.Diamond(name, carat, diameter)
    assert (my_brilliant.get_name(),
            my_brilliant.get_carat(),
            my_brilliant.get_diameter()) == (*result,)


@pytest.mark.parametrize(('name', 'carat', 'diameter', 'cost', 'result'), [
    ('Сапфир', 2.5, 3.1, 1253, ['Название: Сапфир',
                                'Карат: 2.5',
                                'Диаметр: 3.1 мм',
                                'Стоимость: 1253 руб.'])
])
def test_brilliant(name, carat, diameter, cost, result):
    my_brilliant = task1.Brilliant(name, carat, diameter, cost)
    assert (my_brilliant.get_name(),
            my_brilliant.get_carat(),
            my_brilliant.get_diameter(),
            my_brilliant.get_cost()) == (*result,)

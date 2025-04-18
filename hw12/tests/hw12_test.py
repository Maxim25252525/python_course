from datetime import date

import pytest

from hw12.tasks import task1


@pytest.fixture
def get_tasks():
    return (
        task1.Task("Позавтракать", "", date(2025, 9, 2), 2),
        task1.Task("Поспать", "Прям хорошо поспать", date(2025, 9, 10)),
        task1.Task("Погладить кошку", "  ", date(2025, 9, 1)),
    )


@pytest.fixture
def set_tasks_in_todolist(get_tasks):
    todo_list = task1.TodoList()
    for task in get_tasks:
        todo_list.add_task(task)
    return todo_list


class TestHw12Task1:

    @pytest.mark.parametrize(
        ("index", "result"),
        [
            (
                0,
                "--------------------\n"
                "Позавтракать - 2\n"
                "\n"
                "02.09.2025\n"
                "--------------------",
            ),
            (
                1,
                "--------------------\n"
                "Поспать - 1\n"
                "\n"
                "> Прям хорошо поспать\n"
                "\n"
                "10.09.2025\n"
                "--------------------",
            ),
            (
                2,
                "--------------------\n"
                "Погладить кошку - 1\n"
                "\n"
                "01.09.2025\n"
                "--------------------",
            ),
        ],
    )
    def test_get_info_task(self, index, result, get_tasks):
        assert get_tasks[index].get_info() == result

    def test_add_task_in_todolist(self, set_tasks_in_todolist, get_tasks):
        assert set_tasks_in_todolist.tasks == list(get_tasks)

    def test_search_task(self, set_tasks_in_todolist, get_tasks):
        for index in range(len(get_tasks)):
            try:
                assert (
                    set_tasks_in_todolist.search_task(get_tasks[index].id)
                    == index
                )
            except:  # noqa
                pytest.skip(
                    "Метод search_task не реализован или реализован с ошибками"
                )

    def test_get_all_tasks(self, set_tasks_in_todolist, get_tasks):
        tasks = set_tasks_in_todolist.get_all_tasks()
        assert tasks == set_tasks_in_todolist.tasks
        for index in range(len(tasks)):
            assert tasks[index].get_info() == get_tasks[index].get_info()

    def test_get_task(self, set_tasks_in_todolist, get_tasks):
        for index in range(len(get_tasks)):
            task = set_tasks_in_todolist.get_task(get_tasks[index].id)
            assert task == get_tasks[index]
            assert task.id == get_tasks[index].id
            assert task.name == get_tasks[index].name
            assert task.deadline == get_tasks[index].deadline
            assert task.priority == get_tasks[index].priority
            assert task.description == get_tasks[index].description

    def test_set_completed(self, set_tasks_in_todolist, get_tasks):
        for index in range(len(get_tasks)):
            set_tasks_in_todolist.set_completed(get_tasks[index].id)
            assert (
                len(set_tasks_in_todolist.get_all_tasks())
                == len(get_tasks) - index - 1
            )

    def test_get_sorted_tasks(self, set_tasks_in_todolist, get_tasks):
        assert set_tasks_in_todolist.get_sorted_tasks() == sorted(
            get_tasks, key=lambda obj: obj.deadline, reverse=False
        )
        assert set_tasks_in_todolist.get_sorted_tasks(reverse=True) == sorted(
            get_tasks, key=lambda obj: obj.deadline, reverse=True
        )
        assert set_tasks_in_todolist.get_sorted_tasks(key="name") == sorted(
            get_tasks, key=lambda obj: obj.name
        )
        assert set_tasks_in_todolist.get_sorted_tasks(
            key="name", reverse=True
        ) == sorted(get_tasks, key=lambda obj: obj.name, reverse=True)
        assert set_tasks_in_todolist.get_sorted_tasks(
            key="priority"
        ) == sorted(get_tasks, key=lambda obj: obj.priority)
        assert set_tasks_in_todolist.get_sorted_tasks(
            key="priority", reverse=True
        ) == sorted(get_tasks, key=lambda obj: obj.priority, reverse=True)

    def test_search_task_raise(self, set_tasks_in_todolist):
        with pytest.raises(ValueError) as ex:
            try:
                set_tasks_in_todolist.search_task("-1")
            except AttributeError:
                pytest.skip(
                    "Метод search_task не реализован или реализован с ошибками"
                )
        assert "Задача -1 не найдена" == str(ex.value)

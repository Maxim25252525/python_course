"""
# Задача 1: Список дел +1

Реализуйте класс 'Task', описывающий задачу. При создании экземпляра класс
должен принимать следующие аргументы:
- Имя задачи.
- Описание задачи.
- Срок исполнения задачи (дедлайн).
- Приоритет. По умолчанию 1.

Экземпляр класса 'Task' должен иметь следующие атрибуты:
- id - уникальный идентификатор задачи (строковый тип). Для генерации id
нужно использовать функцию uuid4 из модуля uuid.
- name - имя задачи.
- description - описание задачи.
- deadline - срок исполнения задачи (дедлайн) (тип date из модуля datetime).
- priority - приоритет (0 - низкий, 1 - средний, 2 - высокий).

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает информацию о задаче в формате:
- Если описание задачи не пусто:
```
--------------------
<Имя задачи> - <приоритет>

> <Описание задачи>

<дедлайн>
--------------------
```

Например:
```
--------------------
Позавтракать - 2

> На завтрак будет яичница с колбасками.

17.02.2025
--------------------
```
- Если описание задачи пусто, либо содержит только одни пробелы и переносы
строк (\n):
```
--------------------
<Имя задачи> - <приоритет>

<дедлайн>
--------------------
```

Например:
```
--------------------
Позавтракать - 2

17.02.2025
--------------------
```

Реализуйте класс TodoList, описывающий список дел.
При создании экземпляра класс не должен принимать аргументов.

Экземпляр класса TodoList должен иметь следующие атрибуты:
- tasks - изначально пустой список дел.

Класс должен иметь следующие методы экземпляра:
- add_task - добавляет задачу из класса Task в список задач.
- set_completed - Принимает на вход id задачи для удаления. Удаляет задачу из
списка только в том случае, если задача найдена по id.
Если задача не найдена, нужно вызвать исключение типа ValueError и изменить
текст ошибки на 'Задача <id> не найдена'.
Пример описания, если задача 123 не найдена: 'Задача 123 не найдена'.
- get_task - Принимает на вход id задачи. Возвращает задачу (объект) по id
только в том случае, если задача найдена по id. Если задача не найдена, нужно
вызвать исключение также, как в функции выше.
- get_all_tasks - возвращает список дел.
- get_sorted_tasks - принимает на вход параметры 'key' и 'reverse'.
Параметр 'key', равный по умолчанию 'deadline', может иметь следующие
значения:
    - name - сортировка по имени.
    - priority - сортировка по приоритету.
    - deadline - сортировка по дедлайнам.
Параметр 'reverse', равный по умолчанию 'False', может иметь следующие
значения:
    - False - сортировка по возрастанию.
    - True - сортировка по убыванию.
В данном методе при сортировке нужно использовать lambda-функции.

> flake8 может ругаться на lambda-функцию. Чтобы flake8 пропустил данную ошибку
можно написать на этой же строчке комментарий "noqa".
Например: key_sorted = lambda obj: obj.name  # noqa

> Методы set_completed и get_task выполняют поиск задачи по id. Для поиска
задачи можно использовать вспомогательный метод search_task. В данный метод
нужно будет также перенести вызов исключения, который был изначально в методах
set_completed и get_task.
Данный метод вы должны реализовать полностью сами.
За реализацию метода вы получаете +1 балл.

Под блоком if __name__ == '__main__':
1. Создайте экземпляр класса, передав необходимые аргументы.
2. Проверьте взаимодействие с атрибутами и методами класса.

Добавьте докстринги (описание классов и методов) и аннотации типов (указание
типов параметров и возвращаемых значений) для каждого метода и класса.
"""

from uuid import uuid4
from datetime import date


class Task:
    """Класс, описывающий задачу.

    Args:
        name: Имя задачи.
        description: Описание задачи.
        deadline: Срок исполнения задачи.
        priority: Приоритет задачи(по умолчанию 1).

    Attributes:
        id: Уникальный идентификатор задачи.
        name: Имя задачи.
        description: Описание задачи.
        deadline: Срок исполнения задачи.
        priority: Приоритет задачи(по умолчанию 1).

    """

    def __init__(
        self, name: str, description: str, deadline: date, priority: int = 1
    ):
        """
        Инициализация объекта класса Task.

        Args:
            name: Имя задачи.
            description: Описание задачи.
            deadline: Срок исполнения задачи.
            priority: Приоритет задачи(по умолчанию 1).
        """
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.deadline = deadline
        self.priority = priority

    def get_info(self) -> str:
        """
        Возвращает информацию о задаче в определенном формате.

        Returns:
            Информация о задаче в формате:
            --------------------
            <Имя задачи> - <приоритет>

            > <Описание задачи> (если есть)

            <дедлайн>
            --------------------
        """
        description = '> ' + self.description + '\n\n'
        return (
            f"--------------------\n"
            f"{self.name.capitalize()} - {self.priority}\n\n"
            f'{description if self.description.strip() else ""}'
            f'{self.deadline.strftime("%d.%m.%Y")}\n'
            f"--------------------"
        )


output_number = 1


def print_info(func):
    """Функция-декоратор."""

    def wrapper(*args, **kwargs):
        global output_number
        print(str(output_number) + "-й вывод:")
        for number, task in enumerate(func(*args, **kwargs)):
            print(f"\t {number + 1}-я задача:")
            print(*map(lambda x: "\t" + x + "\n", task.get_info().split("\n")))
        print()
        output_number += 1
        return func(*args, **kwargs)

    return wrapper


class TodoList:
    """Класс, описывающий список дел.

    Attributes:
        tasks: Список дел.
    """

    def __init__(self):
        """Инициализация объекта класса TodoList."""
        self.tasks = []

    def search_task(self, search_key: str) -> int:
        """
        Ищет задачу в списке дел.

        Args:
            search_key: Ключ по которому осуществляется поиск.

        Returns:
            Индекс задачи в списке дел.
        """
        for index, task in enumerate(self.tasks):
            if search_key == task.id:
                return index

        raise ValueError(f"Задача {search_key} не найдена")

    def add_task(self, task: Task):
        """Добавляет задачу в список дел."""
        self.tasks.append(task)

    def set_completed(self, task_id: str):
        """
        Удаляет задачу из списка дел по ее id.

        Args:
            task_id: Идентификатор задачи.
        """
        self.tasks.pop(self.search_task(task_id))

    def get_task(self, task_id: str) -> Task:
        """
        Возвращает задачу по ее id.

        Args:
            task_id: Идентификатор задачи.

        Returns:
            Объект класса Task с заданным идентификатором.
        """
        return self.tasks[self.search_task(task_id)]

    @print_info
    def get_all_tasks(self) -> list:
        """
        Возвращает все задачи из списка дел.

        Returns:
            Список всех задач из списка дел.
        """
        return self.tasks

    @print_info
    def get_sorted_tasks(
        self, key: str = "deadline", reverse: bool = False
    ) -> list:
        """
        Сортирует задачи из списка дел.

        Args:
            key: Ключ для сортировки задач.
            reverse: Порядок сортировки задач.

        Returns:
            Список отсортированных задач из списка дел.
        """
        return sorted(
            self.tasks, key=lambda task: getattr(task, key), reverse=reverse
        )


if __name__ == "__main__":
    task1 = Task("Посмотреть фильм", "       ", date(2025, 4, 12), 2)
    task2 = Task(
        "Приготовить ужин", "Блюдо должно быть вкусным", date(2025, 4, 12), 1
    )
    task3 = Task("Пойти в спортзал", "", date(2025, 4, 14), 0)

    todolist = TodoList()
    todolist.add_task(task1)
    todolist.add_task(task2)
    todolist.add_task(task3)
    todolist.get_sorted_tasks("priority", True)
    todolist.set_completed(task2.id)
    todolist.get_all_tasks()
    print(todolist.get_task(task3.id).id)

"""
# Задача 1: Класс "Человечек" +1

Реализуйте класс 'Human', описывающий человека. При создании экземпляра класс
должен принимать аргументы:
- Имя
- Фамилию
- Отчество
- Пол ('м' или 'ж')

Экземпляр класса 'Human' должен иметь следующие атрибуты:
- name - имя
- surname - фамилия
- patronymic - отчество
- age - возраст (по умол. 0 лет)
- gender - пол
- weight - вес (по умол. 3.3 кг)
- height - рост (по умол. 50 см)

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает строку с информацией о человеке: имя, фамилия,
отчество, возраст, пол, вес и рост в следующем формате (данные сформированы
случайным образом, у вас будут свои):
```
Фамилия: Иванов
Имя: Иван
Отчество: Иванович
Возраст: 50
Пол: м
Вес: 85.6 кг
Рост: 175 см
```

Под блоком if __name__ == '__main__':
1. Создайте экземпляр класса, передав необходимые аргументы.
2. Проверьте взаимодействие с атрибутами и методами класса.

Добавьте докстринги (описание классов и методов) и аннотации типов (указание
типов параметров и возвращаемых значений) для каждого метода и класса.
"""


class Human:

    """Класс, описывающий человека.

    Args:
        name: Имя.
        surname: Фамилия.
        patronymic: Отчество.
        gender: Пол.

    Attributes:
        name: Имя.
        surname: Фамилия.
        patronymic: Отчество.
        gender: Пол.
        age: Возраст.
        weight: Вес.
        height: Рост.

    """

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        gender: str
    ):
        """
        Инициализация объекта класса Human.

        Args:
            name: Имя.
            surname: Фамилия.
            patronymic: Отчество.
            gender: Пол('м' или 'ж').
        """
        self.name: str = name
        self.surname: str = surname
        self.patronymic: str = patronymic
        self.gender: str = gender
        self.age: int = 0
        self.weight: float = 3.3
        self.height: float = 50

    def get_info(self) -> str:
        """
        Выводит информацию о человеке.

        Returns:
            Ничего не возвращает.
        """
        return (
            f"Фамилия: {self.surname}\n"
            f"Имя: {self.name}\n"
            f"Отчество: {self.patronymic}\n"
            f"Возраст: {self.age}\n"
            f"Пол: {self.gender}\n"
            f"Вес: {self.weight} кг\n"
            f"Рост: {self.height} см"
        )


if __name__ == "__main__":
    maxim = Human("Максим", "Романчук", "Павлович", "м")
    maxim.age = 15
    print(maxim.get_info())

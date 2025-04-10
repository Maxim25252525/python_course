"""
# Задание 2: Жилищный вопрос +1

Реализуйте класс 'Flat', описывающий квартиру. При создании экземпляра класс
должен принимать 3 аргумента:
- Количество комнат (целочисленный тип).
- Количество окон (целочисленный тип).
- Количество санузлов (целочисленный тип).

Экземпляр класса 'Flat' должен иметь следующие атрибуты:
- rooms - количество комнат.
- windows - количество окон.
- bathrooms - количество санузлов.
- laundry - прачечная (логический тип). По умол. False.

> Комнаты, окна и санузлы задаются сразу при постройке дома.
Есть в нём прачечная или нет - зависит от владельца. Поэтому при создании
нового объекта этот параметр не указывается, но может быть изменен в процессе
жизни объекта.

Если количество комнат меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество комнат должно быть больше 0'
Если количество окон меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество окон должно быть больше 0'
Если количество санузлов меньше 0 - вызвать исключение типа ValueError с
описанием: 'Количество санузлов должно быть больше или равно 0'

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает информацию о квартире в формате: 'Квартира состоит из
<количество комнат> комнат(ы). Количество окон в квартире - <количество окон>.
Санузлов - <количество санузлов>. В квартире <есть прачечная/нет прачечной>.'
Например: Квартира состоит из 3 комнат(ы). Количество окон в квартире - 4.
Санузлов - 1. В квартире есть прачечная.

Реализуйте класс 'Garage', описывающий гараж. При создании экземпляра класс
должен принимать 1 аргумент:
- Площадь гаража (вещественный тип). Измеряется в квадратных метрах.

Экземпляр класса 'Garage' должен иметь следующие атрибуты:
- square - Площадь гаража (вещественный тип). Измеряется в квадратных метрах.
- warm - Теплый гараж или нет (логический тип). По умол. False.

Если площадь гаража меньше или равна 0 - вызвать исключение типа ValueError с
описанием: 'Площадь гаража должна быть больше 0'

Класс должен иметь следующие методы экземпляра:
- get_info - возвращает информацию о гараже в формате: 'Гараж <отапливаемый/
неотапливаемый> площадью <площадь гаража> м^2.'.
Например: Гараж отапливаемый площадью 10 м^2.

Создайте наследника класса 'Flat' и 'Garage' - класс 'Home', описывающий дом.
При создании экземпляра класс должен принимать 5 аргументов:
- Количество комнат (целочисленный тип).
- Количество окон (целочисленный тип).
- Количество санузлов (целочисленный тип).
- Площадь гаража (вещественный тип). Измеряется в квадратных метрах.
- Количество этажей (целочисленный тип).

> Базовые классы указываются в том же порядке, в котором они описаны выше.

Экземпляр класса 'Home' должен иметь следующие атрибуты, помимо базовых:
- floors - количество этажей.
- loft - чердак (логический тип). По умол. False.
- basement - подвал (логический тип). По умол. True.

> Чердак не передается в конструктор, так как после возведения дома его можно
достроить.
> Подвал не передается в контруктор, так как после возведения дома его можно
замуровать.

Если количество этажей меньше 1 - вызвать исключение типа ValueError с
описанием: 'Количество этажей должно быть больше 0'

Класс должен переопределять базовый метод:
- get_info - возвращает информацию о доме в формате: 'Дом имеет <количество
этажей> этажа/этажей. Состоит из <количество комнат> комнат(ы). Количество
окон в доме - <количество окон>. Санузлов - <количество санузлов>. В доме <есть
прачечная/нет прачечной>. Также в доме есть <отапливаемый/ не отапливаемый>
гараж площадью <площадь гаража> м^2. <Есть чердак/Нет чердака>. <Есть подвал/
Нет подвала>.'
Например: Дом имеет 2 этажа/этажей. Состоит из 6 комнат(ы). Количество окон в
доме - 8. Санузлов - 2. В доме есть прачечная. Также в доме есть отапливаемый
гараж площадью 15 м^2. Нет чердака. Есть подвал.

Под блоком if __name__ == '__main__':
1. Создайте экземпляр класса, передав необходимые аргументы.
2. Проверьте взаимодействие с атрибутами и методами класса.

Добавьте докстринги (описание классов и методов) и аннотации типов (указание
типов параметров и возвращаемых значений) для каждого метода и класса.
"""

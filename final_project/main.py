from final_project.my_functions import *

CELL_DESIGN = {"empty": "▢", "tank": "▣", "miss": "◼", "hit": "✘"}

coordinates_dict = {
    "а": 0,
    "б": 1,
    "в": 2,
    "г": 3,
    "д": 4,
    "е": 5,
    "ж": 6,
    "з": 7,
    "и": 8,
    "к": 9,
    0: "а",
    1: "б",
    2: "в",
    3: "г",
    4: "д",
    5: "е",
    6: "ж",
    7: "з",
    8: "и",
    9: "к",
}


if __name__ == "__main__":
    print(
        "Привет! Это игра танковый бой!",
        "Если вы хотите ознакомиться с правилами игры, напишите 'помощь'.",
        "Чтобы начать игру, вам нужно написать 'старт'.",
        sep="\n",
    )

    command = conv_cmd(input("> "))
    # command = 'старт'
    check_exit(command)
    while True:
        match command:
            case "помощь":
                print("Правила игры: ")
                command = conv_cmd(input("> "))
                check_exit(command)

            case "старт":
                # Начало программы, создаем поля для игрока и компьютера.
                # Создаём танки для компьютера.
                print("Игра началась!")
                user_field = Field()
                computer_field = Field()
                tanks = []
                create_tanks(tanks)
                computer_field.tanks = tanks
                print_fields(user_field, computer_field)

                # Создаем танки для игрока.
                command = conv_cmd(
                    input("Введите координаты ваших танков через пробел: ")
                )
                check_exit(command)
                tanks = command.split()
                tanks = converted_coords(
                    tanks
                )  # конвертируем координаты танков
                while not check_tanks_coordinates(tanks):
                    command = conv_cmd(
                        input("Введите координаты ваших танков через пробел: ")
                    )
                    check_exit(command)
                    tanks = command.split()
                    tanks = converted_coords(tanks)
                user_field.tanks = tanks

                # Алгоритм самой игры.

                # TODO:
                #  Глобально, нужно доделать логику самой игры.
                #  То есть добавить возможность производить выстрелы компьютеру
                #  И делать ходы по очереди, пока не закончится игра.
                #  Также нужно добавить всяческие проверки на корректность ввода координат,
                #  причем как танков, так и выстрелов.
                #
                # TODO:
                #  > Если понадобится делать проверку на наличие в клетки выстрела или танка
                #    можно использовать функцию "check_available_shot".
                #  > После каждого ввода пользователя нужно использовать "conv_cmd".
                #  > Также нужно использовать "check_exit", чтобы в случае чего завершать игру.
                #
                # TODO:
                #  Желательно вынести все функции в отдельный файл.
                #  Также нужно разобраться, когда стоит очищать терминал.
                #  Чтобы скрыть танки компьютера нужно добавить False в
                #  computer_field (находиться где-то в начале блока main, после приветствия).

                turn = 'user'  # Показывает, кто сейчас ходит.
                while computer_field.tanks and user_field.tanks:
                    if turn == 'user':
                        print()
                        print("Ваш ход!")
                        command = conv_cmd(
                            input(
                                "Введите координаты вашего выстрела или воспользуйтесь подсказкой: "
                            )
                        )
                        check_exit(command)
                        if command == "подсказка":
                            tip(computer_field)
                            command = conv_cmd(
                                input("Введите координаты вашего выстрела: ")
                            )
                            check_exit(command)

                        user_shot = Shot(
                            int(command[1:]) - 1, coordinates_dict[command[0]]
                        )
                        # Проверяем, попали в танк или нет.
                        if (
                            computer_field.data[user_shot.row][user_shot.column]
                            == "▣"
                        ):
                            user_shot.hit = True
                            computer_field.shots.append(user_shot)
                            print_fields(user_field, computer_field)
                            # Проверяем, уничтожен ли танк.
                            if check_destroyed_tank(computer_field, user_shot)[0]:
                                tank_id = 0
                                for i, tank in enumerate(computer_field.tanks):
                                    if (
                                        tank
                                        == check_destroyed_tank(
                                            computer_field, user_shot
                                        )[1]
                                    ):
                                        tank_id = i
                                        break
                                computer_field.tanks.pop(tank_id)
                                print("Вражеский танк уничтожен!")
                            else:
                                print("Вы попали!")
                        else:
                            computer_field.shots.append(user_shot)
                            print_fields(user_field, computer_field)
                            print("Вы промахнулись!")
                            turn = 'computer'  # Передаем ход компьютеру.
                    else:
                        print()
                        print("Ход компьютера!")
                        x = random.randint(0, 9)
                        y = random.randint(0, 9)
                        computer_shot = Shot(x, y)
                        # Проверяем, был ли выстрел ранее по этой клетке.
                        while check_hit(computer_shot, computer_field, 'shot')[0]:
                            x = random.randint(0, 9)
                            y = random.randint(0, 9)
                            computer_shot = Shot(x, y)
                        # Проверяем, попали в танк или нет.
                        if check_hit(computer_shot, user_field)[0]:
                            computer_shot.hit = True
                            user_field.shots.append(computer_shot)
                            print_fields(user_field, computer_field)
                            # Проверяем, уничтожен ли танк.
                            if check_destroyed_tank(user_field, computer_shot)[0]:
                                tank_id = 0
                                for i, tank in enumerate(computer_field.tanks):
                                    if (
                                        tank
                                        == check_destroyed_tank(
                                            user_field, computer_shot
                                        )[1]
                                    ):
                                        tank_id = i
                                        break
                                user_field.tanks.pop(tank_id)
                                print("Ваш танк уничтожен!")
                            else:
                                print("По вашему танку попали!")
                        else:
                            user_field.shots.append(computer_shot)
                            print_fields(user_field, computer_field)
                            print("Все танки остались целы!")
                            turn = 'user'  # Передаем ход пользователю.

                if not user_field.tanks:
                    print("Вы проиграли!")
                elif not computer_field.tanks:
                    print('Поздравляем! Все танки противника уничтожены!')
                    print("Вы выиграли!")
                    command = 'выход'

            case _:
                print("Такой команды нет! Попробуйте еще раз!")
                command = conv_cmd(input("> "))
                check_exit(command)

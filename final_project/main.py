from final_project.my_functions import *
from time import sleep


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
                sleep(0.5)
                user_field = Field()
                computer_field = Field()
                tanks = []
                create_tanks(tanks)
                computer_field.tanks = tanks
                print_fields(user_field, computer_field)

                # Создаем танки для игрока.
                sleep(0.5)
                command = conv_cmd(
                    input("Введите координаты ваших танков через пробел: ")
                )
                check_exit(command)
                tanks = command.split()
                while not check_input(tanks, 'tank'):
                    sleep(0.5)
                    command = conv_cmd(
                        input("Попробуйте снова: ")
                    )
                    check_exit(command)
                    tanks = command.split()

                tanks = converted_coords(tanks)
                user_field.tanks = tanks

                # TODO:
                #  Также нужно добавить всяческие проверки на корректность ввода координат,
                #  причем как танков, так и выстрелов.
                #  Также нужно разобраться, когда стоит очищать терминал.
                #  Сделать одинаковую размерность танков.
                #  Научить компьютер запоминать свои выстрелы.

                # Алгоритм самой игры.
                turn = 'user'  # Показывает, кто сейчас ходит.
                while computer_field.tanks and user_field.tanks:
                    # Алгоритм для игрока
                    if turn == 'user':
                        print()
                        print("Ваш ход!")
                        sleep(0.5)
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

                        while not check_input(command, 'shot', computer_field):
                            sleep(0.5)
                            command = conv_cmd(
                                input(
                                    "Попробуйте снова: "
                                )
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
                                sleep(0.5)
                                input("Вражеский танк уничтожен! ")
                            else:
                                sleep(0.5)
                                input("Вы попали! ")
                        else:
                            computer_field.shots.append(user_shot)
                            print_fields(user_field, computer_field)
                            sleep(0.5)
                            input("Вы промахнулись! ")
                            turn = 'computer'  # Передаем ход компьютеру.

                    # Алгоритм для компьютера
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
                        sleep(0.5)
                        print(f'Противник бьет по {coordinates_dict[y]}{x+1}:')
                        # Проверяем, попали в танк или нет.
                        if check_hit(computer_shot, user_field, 'tank')[0]:
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
                                sleep(0.5)
                                input("Ваш танк уничтожен! ")
                            else:
                                sleep(0.5)
                                input("По вашему танку попали! ")
                        else:
                            user_field.shots.append(computer_shot)
                            print_fields(user_field, computer_field)
                            sleep(0.5)
                            input("Все танки остались целы! ")
                            turn = 'user'  # Передаем ход пользователю.

                if not user_field.tanks:
                    print("Вы проиграли!")
                elif not computer_field.tanks:
                    print('Поздравляем! Все танки противника уничтожены!')
                    print("Вы выиграли!")
                    check_exit('выход')

            case _:
                print("Такой команды нет! Попробуйте еще раз!")
                command = conv_cmd(input("> "))
                check_exit(command)

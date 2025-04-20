from final_project.my_classes import User, Computer
from final_project.my_functions import *
from time import sleep


if __name__ == "__main__":
    print(
        "Привет! Это игра танковый бой!",
        "Если вы хотите ознакомиться с правилами игры, напишите 'правила'.",
        "Чтобы начать игру, вам нужно написать 'старт'.",
        sep="\n",
    )

    command = conv_cmd(input("> "))
    # command = 'старт'
    check_exit(command)
    while True:
        match command:
            case "правила":
                print("Правила игры:\n"
                      "Сначала вы должны разместить свои танки на поле. "
                      "Танки должны быть расположены по вертикали "
                      "в пределах от а1 до к10.\n"
                      "Ввод танков должен осуществляться через пробел.\n"
                      "Всего у вас должно быть 10 неповторяющихся танков.\n"
                      "- Танк из 5 клеток - 1\n"
                      "- Танк из 4 клеток - 1\n"
                      "- Танков из 3 клеток - 2\n"
                      "- Танков из 2 клеток - 3\n"
                      "- Танков из 1 клетки - 3\n"
                      "Затем начнется сама игра.\n"
                      "Ваша задача - уничтожить все танки компьютера. "
                      "Для того, чтобы сделать выстрел, "
                      "введите координаты клетки.\n"
                      "После этого по вам будет стрелять компьютер.\n"
                      "Вы будете ходить по очереди,"
                      " пока один из игроков не победит.\n"
                      "Также вы можете попросить подсказку. "
                      "Для этого напишите 'подсказка', вместо выстрела.\n"
                      "Не стоит забывать, что в любой момент "
                      "вы можете выйти из игры, написав 'выход'.\n"
                      "Напишите старт, чтобы начать.\n"
                      "Приятной игры!")
                command = conv_cmd(input("> "))
                check_exit(command)

            case "старт":
                # Начало программы, создаем поля для игрока и компьютера.
                # Создаём танки для компьютера.
                print("Игра началась!")
                sleep(0.5)
                user_field = User()
                computer_field = Computer(True)
                tanks = []
                create_tanks(tanks, computer_field.placement)
                computer_field.tanks = tanks
                print_fields(user_field, computer_field)

                # Создаем танки для игрока.
                # Танчики: а8а10 б3 б6 в1 в9в10 г5г7 д2д3 ж4ж7 з1з2 к3к7
                sleep(0.5)
                command = conv_cmd(
                    input("Введите координаты ваших танков через пробел: ")
                )
                check_exit(command)
                tanks = command.split()
                while not check_input(tanks, 'tank', user_field):
                    sleep(0.5)
                    command = conv_cmd(
                        input("Попробуйте снова: ")
                    )
                    check_exit(command)
                    tanks = command.split()

                tanks = converted_coords(tanks)
                user_field.tanks = tanks

                # TODO:
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

                        is_used = False
                        while not check_input(command, 'shot', computer_field):
                            sleep(0.5)
                            if command == "подсказка":
                                if not is_used:
                                    tip(computer_field)
                                    command = conv_cmd(
                                        input("Введите координаты вашего выстрела: ")
                                    )
                                    check_exit(command)
                                    is_used = True
                                else:
                                    print("Вы уже использовали подсказку!")
                                    command = input("Введите координаты вашего выстрела: ")
                                    check_exit(command)
                            else:
                                command = conv_cmd(input("Попробуйте снова: "))
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
                        while (
                                check_hit(computer_shot, user_field, 'tank')[0]
                        ):
                            computer_shot.hit = True
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

                                user_field.remember_shot(computer_shot, True)
                                user_field.tanks.pop(tank_id)
                                sleep(0.5)
                                input("Ваш танк уничтожен! ")
                            else:
                                sleep(0.5)
                                input("По вашему танку попали! ")
                                print()
                                print("Ход компьютера!")
                                computer_shot = user_field.remember_shot(computer_shot, False)
                                sleep(0.5)
                                print(f'Противник бьет по {coordinates_dict[y]}{x + 1}:')
                                print_fields(user_field, computer_field)
                        else:
                            user_field.shots.append(computer_shot)
                            if user_field.direction == 'up':
                                user_field.direction = 'isdown'
                            elif user_field.direction == 'down':
                                user_field.direction = 'isup'
                            print_fields(user_field, computer_field)
                            sleep(0.5)
                            input("Все танки остались целы! ")
                            turn = 'user'  # Передаем ход пользователю.

                if not user_field.tanks:
                    print('К сожалению, все ваши танки уничтожены!')
                    print("Вы проиграли!")
                elif not computer_field.tanks:
                    print('Поздравляем! Все танки противника уничтожены!')
                    print("Вы выиграли!")
                    check_exit('выход')

            case _:
                print("Такой команды нет! Попробуйте еще раз!")
                command = conv_cmd(input("> "))
                check_exit(command)

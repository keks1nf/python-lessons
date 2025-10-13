room = [
    ['*', '*', '*', '*', '*', ],
    ['*', '*', '*', '*', '*', ],
    ['*', '*', 'R', '*', '*', ],
    ['*', '*', '*', '*', '*', ],
    ['*', '*', '*', '*', '*', ]
]

robot_row = 2
robot_column = 2


def print_room(robot_room: list):
    for row in robot_room:
        print(' '.join(row))


def choice_is_correct(user_input: str) -> bool:  # 'up 1'
    split_result = user_input.split()

    if len(split_result) != 2:
        return False

    if split_result[0].lower() not in ('up', 'down', 'left', 'right'):
        return False

    if not split_result[1].isdigit():
        return False

    return True


def move(direction: str, distance: int):
    room[robot_row][robot_column] = '*'

    match direction.lower():
        case 'right':
            change_robot_column(distance)
        case 'left':
            change_robot_column(-distance)
        case 'up':
            change_robot_row(-distance)
        case 'down':
            change_robot_row(distance)

    room[robot_row][robot_column] = 'R'


def change_robot_row(distance: int):
    global robot_row

    robot_row += distance

    if robot_row > 4:
        robot_row = 4
    elif robot_row < 0:
        robot_row = 0


def change_robot_column(distance: int):
    global robot_column

    robot_column += distance

    robot_column = min(4, robot_column)
    robot_column = max(0, robot_column)


def main():
    while True:
        print_room(room)

        choice = input('Введіть команду (НАПРЯМ КІЛЬКІСТЬ): ')  # 'right 3'

        if choice == '0':
            break

        if not choice_is_correct(choice):
            print('Невірна команда!')
            continue

        choice = choice.split()
        dir, dis = choice[0], int(choice[1])

        move(dir, dis)


if __name__ == '__main__':
    main()

# * 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# =======================================================================================
import os


def check_4_win(fld: list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),  # кортеж выигрышных комбинаций
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for winrec in win_coord:                                 # сравниваем текущее поле с выигрышными комбинациями
        if fld[winrec[0]] == fld[winrec[1]] == fld[winrec[2]]:
            return fld[winrec[0]]
    return False


def print_field(game_field: list):
    clear = lambda: os.system('cls')
    clear()
    print('===============================================')
    for i in range(3):
        sep = '           '
        print(sep + str(game_field[0+i*3]) + sep +
              str(game_field[1+i*3]) + sep + str(game_field[2+i*3]))
        if i < 2:
            print()
    print('===============================================')


def update_field(field, value, player):
    res = list(field)
    # new_val = '\U0000274C' if player == 1 else '\U00002B55' #эмодзи как то криво отображаются в консоли - мне не понравилось :)
    new_val = 'X' if player == 1 else 'O'
    res[res.index(value)] = new_val
    return res


if __name__ == "__main__":
    field, player, turn = [x for x in range(1, 10)], 1, 1
    while turn < 10:
        repeat = True
        while repeat:
            print_field(field)
            try:
                turn_choice = int(input(f'Игрок {player}, Ваш ход: '))
            except KeyboardInterrupt:
                exit()
            except ValueError:
                turn_choice = -1
            repeat = field.count(turn_choice) == 0

        field = update_field(field, turn_choice, player)
        print_field(field)

        if check_4_win(field):
            print(10*'\U00002728')
            print(f'ИГРОК {player} ВЫИГРАЛ!!!')
            print(10*'\U00002728')
            exit()
        player = 2 if player == 1 else 1
        turn += 1
    print(10*'\U0001F4AA','\n','НИЧЬЯ','\n',10*'\U0001F4AA')
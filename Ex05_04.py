# ** 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
# =======================================================================================
from random import choice
import os
import msvcrt


def input_params():
    def clear(): return os.system('cls')
    clear()
    res = {}
    correct = False
    while not correct:
        game_mode = input(
            'Выберите режим игры: 0 - Игрок/Игрок, 1 - Игрок/Глупый бот, 2 - Игрок/Умный бот: ')
        if game_mode in ('0', '1', '2'):
            correct = True
            res['game_mode'] = int(game_mode)
    while True:
        try:
            sw_cou = int(input('Сколько конфет будем делить? '))
            if not sw_cou:
                sw_cou = 1
                print(
                    'Не жадничайте! Давайте разделим хотя бы одну конфетку!')
            break
        except ValueError:
            pass
    res['sw_cou'] = abs(sw_cou)
    while True:
        try:
            sw_max_on_turn_count = int(
                input('Ограничение количества конфет за ход: '))
            if not sw_max_on_turn_count:
                sw_max_on_turn_count = 1
                print(
                    'Не жадничайте! По одной конфетке брать можно!')
            break
        except ValueError:
            pass
    res['sw_max_on_turn_count'] = abs(sw_max_on_turn_count)
#    res = {'game_mode': 2, 'sw_cou': 234, 'sw_max_on_turn_count': 50}
    return res


def strategy(limit: int, cou: int):  # стратегия победы для умного бота
    #print (cou)
    if cou <= limit:
        res = cou
    else:
        # всегда оставляем число, кратное забираемому пределу +1 конфетку. Если невозможно (оно уже равно) - забираем максимально возможное число -1
        res = cou - ((cou // limit)*limit + 1)
        if res < 0:
            res = limit-1
    return res


def request(pl, gl_cou, max, bot1=False, bot2=False):
    req_string = f'Сколько конфет будем брать? (1..{max}) '
    while True:
        try:
            print(f'Число конфет на столе: {gl_cou}', end=". ")
            print('Ходит', pl, end=". ")
            if bot1:
                # Глупый бот - обычный рандом в диапазоне
                sw_count = choice(range(1, max + 1))
                print(req_string, sw_count)
            elif bot2:
                sw_count = strategy(max, gl_cou)
                print(req_string, sw_count)
            else:
                sw_count = int(input(req_string))
                if not sw_count:
                    sw_count = 1
                    print(
                        'Одну надо взять обязательно - они вкусные :) Берите-берите.. Взята одна конфетка..')
            if sw_count <= max:
                break
        except ValueError:
            pass
    return sw_count


def game(game_mode: int):
    print('Успешной игры!')
    print('Для выхода из игры нажмите Ctrl+C')
    print('Для начала нажмите любую клавишу....')
    msvcrt.getch()
    
    def clear(): return os.system('cls')
    clear()
    match game_mode:
        case 0:
            p1_name, p2_name = 'Игрок 1', 'Игрок 2'
        case 1:
            p1_name, p2_name = 'Игрок', 'Глупый бот'
        case 2:
            p1_name, p2_name = 'Игрок', 'Умный бот'

    player = choice((True, False))
    cur_sw_cou = params['sw_cou']
    first_turn = True
    while cur_sw_cou > 0:
        player_s = p1_name if player else p2_name
        if first_turn:
            print(f'По результатам жеребьёвки начинает {player_s}! Удачи!!!')
            print('===============================================')
            first_turn = False
        player_s = p1_name if player else p2_name
        turn_sw_cou = request(player_s, cur_sw_cou, params['sw_max_on_turn_count'], bot1=(
            game_mode == 1) and not player, bot2=(game_mode == 2) and not player)
        cur_sw_cou -= turn_sw_cou
        player = not player
    print('===============================================')        
    print(player_s, "победил!!!")
    print('Спасибо за игру!!!')
    print('===============================================')


if __name__ == "__main__":
    params = input_params()
    game(params['game_mode'])

import calc_controller as cc


def write_console(*params):
    print(' '.join(list(map(lambda x: str(x), params))))
    return


def get_real_value(num):
    while True:
        try:
            a = float(input(f'Введите {num}-е число: ').replace(',', '.'))
            break
        except ValueError:
            write_log(cc.t(), 'Ошибка ввода вещественного числа')
            write_console('Нужно ввести число. Попробуйте еще раз')
    return a


def get_complex_value(num):
    while True:
        try:
            a = int(input(f'Введите действительную часть {num}-го числа: '))
            b = int(input(f'Введите мнимую часть {num}-го числа: '))
            break
        except ValueError:
            write_log(cc.t(), 'Ошибка ввода целого числа')
            write_console('Нужно ввести целое число. Попробуйте еще раз')
    return (complex(a, b))


def input_number(num: int):
    write_console(f'Ввод {num}-го числа:')
    complex_num = True if input(
        'Число комплексное? (y/n): ') in ('y', 'Y') else False
    res = get_complex_value(num) if complex_num else get_real_value(num)
    return res


def menu(complex=True):
    res = -1
    complex_menu = {'1': 'Сумма', '2': 'Разность', '3': 'Произведение',
                    '4': 'Частное', '5': 'Степень', '0': 'Выход'}
    additional = {'6': 'Целочисленное деление', '7': 'Остаток от деления'}
    real_menu_keys = sorted(complex_menu | additional)[
        1:]+[sorted(complex_menu | additional)[0]]

    if complex:
        dic = complex_menu
        for key in dic:
            write_console(key, ' - ', dic[key])
    else:
        dic = complex_menu | additional
        for key in real_menu_keys:
            write_console(key, ' - ', dic[key])

    while res not in dic.keys():
        res = input('Выберите операцию: ')
    return res


def write_log(*params):
    with open("calc.log", 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), params)))+'\n')


if __name__ == '__main__':
    pass
from datetime import datetime as dt
from time import time

sep = ('**', '*', '//', '/',  '%', '+', '-')


def t():
    return dt.now().strftime('%D\t%H:%M:%S')


def summ(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 'Division by zero'
    else:
        return a / b


def pow(a, b):
    return a ** b


def whole_div(a, b):
    if b == 0:
        return 'Division by zero'
    else:
        return a // b


def tile_div(a, b):
    if b == 0:
        return 'Division by zero'
    else:
        return a % b


def calc(op, a, b):
    match op:
        case '+': f = summ
        case '-': f = sub
        case '*': f = mult
        case '/': f = div
        case '**': f = pow
        case '//': f = whole_div
        case '%': f = tile_div
    return f(a, b)


def prepare_string(string: str):
    global sep
    # for s in sep: #расстановка пробелов после знаков-разделителей, убирание двойных пробелов, выравнивание скобок (на будущее)
    #     string = string.replace(s, f' {s} ')
    # string = ' '.join(string.split())
    str_l = string.split()

    # подготовка строки к виду, пригодному для вычисления - прекращаем как только находим ошибку.
    valid_l = []
    digit_expected = True
    for i in range(len(str_l)):
        if digit_expected and str_l[i] not in ('(',')'):
            try:
                _ = float(str_l[i])
                valid_l.append(str_l[i])
                digit_expected = False
            except ValueError:
                break  # возвращаем только безошибочную часть
        else:
            if str_l[i] in sep:
                valid_l.append(str_l[i])
                if str_l[i] not in ('(',')'):
                    digit_expected = True                
            else:
                break
    if not valid_l:
        return ''
    if valid_l[-1] in sep and valid_l[-1] not in ('(',')'):
        valid_l = valid_l[:-1]
        print(valid_l)
    return ' '.join(valid_l)


def calc_string(string: str):  # вычисление по строке с соблюдением приоритетов операций
    if len(string) == 0:
        return '0'
# Приоритет операций:[**, унарный плюс, унарный минус, *, /, //, %], затем [+, -]
    global sep
    str_l = string.split()
    i = 0
    while i < len(str_l):
        if str_l[i] in sep[:-2]: #сначала вычисляем приоритетные операции
            str_l = calc_substr(str_l[i], str_l)
        i += 1
    i = 0
    while i < len(str_l):
        if str_l[i] in sep[-2:]:  #потом - сложение и вычитание
            str_l = calc_substr(str_l[i], str_l)
        i += 1
    if len(str_l) == 1:
        str_l = str_l[0]
    elif len(str_l) == 3:
        str_l = calc_substr(str_l[1], str_l)
    res = ''.join(str_l)
    if res[-2::] == '.0':
        res = res[:-2]
    return res


def calc_substr(s: str, str_l: list):  # атомарное математическое вычисление на основе трех элементов списка
    while s in str_l:
        sep_idx = str_l.index(s)
    # комплексные пока не работают - закладка на будущее
        a = float(str_l[sep_idx-1]) #if str_l[sep_idx-1].count('j') ==0 else complex(str_l[sep_idx-1])
        b = float(str_l[sep_idx+1]) #if str_l[sep_idx+1].count('j') ==0 else complex(str_l[sep_idx+1])
        op_res = calc(s, a, b)
        if op_res == 'Division by zero':
            return op_res
        str_l.pop(sep_idx-1)
        str_l.pop(sep_idx-1)
        str_l.pop(sep_idx-1)
        str_l.insert(sep_idx-1, str(op_res))
    return str_l


def write_log(*params):
    with open("calc.log", 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), params)))+'\n')


if __name__ == '__main__':
    pass
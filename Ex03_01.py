# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
# =======================================================================================

from random import choices


def calc_summ(in_list, mode='all'):
    sum = 0
    match mode:
        case 'all':  # все позиции
            for i in range(0, len(in_list)):
                sum += in_list[i]
        case 'odd':  # нечетные позиции
            for i in range(0, len(in_list), 2):
                sum += in_list[i]
        case 'even':  # четные позиции
            for i in range(1, len(in_list), 2):
                sum += in_list[i]
    return sum


# n = 4  #отладочная строка
while True:
    try:
        n = int(input('Введите длину списка: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")

my_list = choices(range(10), k=n)
print(
    f'Сгенерирован список: {my_list}\nСумма элементов на нечетных позициях = {calc_summ(my_list, "odd")}')

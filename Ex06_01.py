# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in : 9
# out:
#     [15, 16, 2, 3, 1, 7, 5, 4, 10]
#     [16, 3, 7, 10]
# in: 10
# out:
#     [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
#     [24, 15, 23, 25]
# =======================================================================================

from random import choices
range_len, list_len = 20, 10


def input_data():
    while True:
        try:
            list_len = int(input('Введите длину списка: '))
            range_len = int(
                input('Введите максимальное значение элемента списка: '))
            break
        except ValueError:
            print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")
    return [list_len, range_len]


def lists_gen(data: list):
    in_list = choices(range(data[1]), k=data[0])
    out_list = [in_list[i]
                for i in range(1, len(in_list)) if in_list[i] > in_list[i-1]]
    return [in_list, out_list]


def print_results(data: list):
    print('Исходный список: ', data[0])
    print('Выходной список: ', data[1])


if __name__ == "__main__":
    print_results(lists_gen(input_data()))

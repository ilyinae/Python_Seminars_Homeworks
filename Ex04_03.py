# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# in: 10
# out:  [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#       [6, 2, 3, 0, 9]
# in: 7
# out:  [4, 5, 3, 3, 4, 1, 2]
#       [5, 1, 2]
# in: -1
# out: 'Negative value of the number of numbers'
# =======================================================================================

from random import choices


def delete_repeated_items(lst: list):
    res = list(lst)  # Создаем копию входного списка
    for itm in lst:
        if lst.count(itm) > 1:
            while res.count(itm) != 0:
                res.pop(res.index(itm))
    return res


def delete_with_filter_function(lst: list):    #альтернативный вариант - с использованием функции filter()
    res = list(lst)  # Создаем копию входного списка
    for itm in lst:
        if lst.count(itm) > 1:
            res = list(filter(lambda x: x != itm, res))    
    return res

while True:
    try:
        list_length = int(input('Введите длину списка: '))
        if list_length < 0:
            print("Длина списка не может быть отрицательной")
            exit()
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")


in_list = choices(range(10), k=list_length)
w_list = delete_repeated_items(in_list)
f_list = delete_with_filter_function(in_list)

print('Исходный список:\t', in_list)
print('Новый список:\t\t', w_list)
print('Новый список(filter):\t', f_list)



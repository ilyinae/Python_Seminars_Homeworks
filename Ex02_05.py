# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# n = 9; maxvalue = 99 # отладочная строка

import random

def create_random_list(n, maxvalue):
    res = []
    for i in range(n):
        res.append(random.randint(1, maxvalue))
    return res    

def my_shuffle(in_list):
    tmp_lst = list(in_list)                        # создадим временный список, из которого будем постепенно удалять случайные элементы (создаем чтобы сохранить исходный список)
    res = []
    while len(tmp_lst) != 0:                                # пока временный список не пуст
        ran_idx = random.randint(0, len(tmp_lst) - 1)       # берем случайный индекс 
        res.append(tmp_lst[ran_idx])                        # копируем элемент по случайному индексу в выходной массив    
        tmp_lst.pop(ran_idx)                                # и удаляем его из временного списка
    return (res)    

while True:
    try:
        n = int(input('Введите длину списка: '))
        maxvalue = int(input('Максимальное значение в списке: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести целое число. Попробуйте еще раз...")
        
in_list = create_random_list(n, maxvalue)
print('Исходный список: \t', in_list)
print('Перемешанный список: \t', my_shuffle(in_list))
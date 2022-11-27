# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
# =======================================================================================
from random import uniform


def create_rand_float_list(n):
    res = []
    for i in range(n):
        res.append(round(uniform(0, 100), 2))
    return res


def create_tail_list(in_list):  # генерируем список из дробных частей
    res = []
    for i in range(0, len(in_list)):
        res.append(round(in_list[i] % 1, 2))
    return res


while True:
    try:
        n = int(input('Введите длину списка: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")


my_list = create_rand_float_list(n)
tail_list = create_tail_list(my_list)
tail_list.sort()
min = round(tail_list[0], 2)
max = round(tail_list[len(tail_list)-1], 2)
diff = round(max - min, 2)

print(f'Сгенерирован список: {my_list}')
print('Min:{0}\tMax:{1}\tDifference:{2}'.format(min, max, diff))

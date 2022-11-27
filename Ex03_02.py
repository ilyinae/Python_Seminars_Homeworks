# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
# =======================================================================================


from random import choices


def pairwise_product(in_list):
    res = []
    for i in range(len(in_list) // 2):  # идем до середины списка с двух концов
        res.append(in_list[i] * in_list[len(in_list)-1-i])
    if len(in_list) % 2:  # если число элементов нечетное - для "центрального" элемента пары не нашлось - добавляем его без произведения
        res.append(in_list[len(in_list) // 2])
    return res


# n = 11  # отладочная строка
while True:
    try:
        n = int(input('Введите длину списка: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")

my_list = choices(range(10), k=n)
print(
    f'Исходный список: {my_list}\nСписок попарных произведений: {pairwise_product(my_list)}')

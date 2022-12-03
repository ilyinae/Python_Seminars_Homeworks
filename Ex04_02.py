# Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.

# in: 54
# out: [2,3,3,3]
# in: 9990
# out: [2,3,3,3,5,37]
# in: 650
# out: [2,5,5,13]
# =======================================================================================

def is_simple(num: int):  # Возвращает True если число простое и False - если нет
    for i in range(2, num):
        if not num % i:
            return False
    return True


# Возвращает список минимальных простых делителей числа
def get_mindivider_list(num: int):
    res, i = [], 2  # начинаем с 2
    while num > 1:
        if is_simple(i):
            while not num % i:
                res.append(i)
                num = num // i
        i += 1
    if not res:
        res = 'Нет простых делителей'               # Для 0 и 1 список будет пустым
    return res


while True:
    try:
        user_n = int(input('Введите натуральное число: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")

if user_n < 0:  # инвертируем отрицательный ввод - список делителей будет один и тот же
    n = -user_n
else:
    n = user_n

print(
    f'Cписок минимальных простых делителей числа {user_n}:', get_mindivider_list(n))

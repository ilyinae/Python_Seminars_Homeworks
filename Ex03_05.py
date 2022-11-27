# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5
# =======================================================================================

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def nega_fib(n):
    # #способ 1
    # if n == -1:
    #     return 1
    # elif n == -2:
    #     return -1
    # else:
    #     return nega_fib(n+2) - nega_fib(n+1)

    # способ 2
    return (-1)**(1-n)*fib(-n)


while True:
    try:
        n = int(input('Введите длину списка: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")

my_list = []
for i in range(-n, n+1):
    if i < 0:
        my_list.append(nega_fib(i))
    else:
        my_list.append(fib(i))

print(f'Список чисел Фибоначчи в диапазоне -{n}..{n}:\n{my_list}')

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

#n = 6 # отладочная строка

def func(n):
    return ((1+1/n)**n)

while True:
    try:
        n = int(input('Введите целое число: '))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести целое число. Попробуйте еще раз...")

outlist = []
for i in range(1, n+1):
    outlist.append(round(func(i), 4))

print (f'Список: {outlist}')
print (f'Сумма элементов списка: {sum(outlist)}')
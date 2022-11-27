# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

#n = 4; p1 = 4; p2 = 2  #отладочная строка

while True:
    try:
        n = int(input('Enter the value of N: '))
        p1 = int(input('Position one: '))
        p2 = int(input('Position two: '))
        break
    except ValueError:
        print("You made a mistake. You need to enter an integer. Try again..")

outlist = []
for i in range(-n, n+1):
    outlist.append(i)
    
print (f'Список: {outlist}')
try:
    outstr = outlist[p1 - 1] * outlist[p2 - 1]
except:
    outstr = "There are no values for these indexes!"
finally:
    print(outstr)    
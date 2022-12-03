# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 10) многочлена и записать в файл многочлен степени k.
# Пример:
# in: 9
#     5
#     3
# out:
#     3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 +3 = 0
#     4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
#     4*x^2 - 4 = 0
# in: 0
#     -1
#     4
# out:
#     3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 +3 = 0
#     4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
#     4*x^2 - 4 = 0
#     4*x^5 + 1*x^4 - 3*x^3 + 1*x^1- 3 = 0    
# =======================================================================================
from random import choices


def polynom_item_gen(k:int, pow:int):       #формирование одного из членов многочлена
    k_str = ''                              #коэффициент
    if k == 0:
        return ''
    elif abs(k) == 1:
        k_str = ''
    else:
        if pow == 0:
            k_str = str(abs(k))
        else:
            k_str = str(abs(k))+'*'    
    pow_str = ''                            #степень    
    if pow > 1:
        pow_str = 'x^'+str(pow)
    elif pow == 1:
        pow_str = 'x'
    add_str = k_str+pow_str                 #суммируем
        
    if k < 0:                               #присваиваем знак
        add_str = '-'+add_str    
    else:
        add_str = '+'+add_str    
    return add_str    


def polynom_gen(k_list: list):          #формируем многочлен на основе списка коэффициентов
    poly_str = ''
    for i in range(0, len(k_list)):
        poly_str = polynom_item_gen(k_list[i], i) + poly_str
    res = poly_str.strip('+').replace('-', ' - ').replace('+',' + ') #наводим красоту в строке - расставляем пробелы, добавляем окончание
    if res[0:3] == ' - ':
        res = '-'+res[3:len(res)]         #убираем пробел у первого знака минус, если он есть  - стрипать нельзя - он значимый, в отличии от плюса
    if res[len(res)-3:len(res)] == ' - ': #убираем последний минус
        res = res[0:len(res)-3]        
    if res == '-' or res =='':    #если после всех обрезаний остался только знак минуса или ничего не осталось (все коэффициенты были = 0) - меняем его на 0  - финальный вид уравнения: 0 = 0
        res = '0'        
    res = res+ ' = 0'    # добавляем окончание полинома
    return (res)
    

while True:
    try:
        pow = int(input('Введите степень многочлена: '))
        if pow <= 0:
            print("Некорректная степень многочлена")
            exit()
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")


koef_list = choices(range(-10, 11), k=pow)
with open('Ex04_04_out_2.txt', 'a', encoding='utf-8') as F:
    F.writelines(polynom_gen(koef_list)+'\n')
    print("Многочлен записан в файл", F.name)    
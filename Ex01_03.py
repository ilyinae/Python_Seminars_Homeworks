# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


while True:
    try:
        x = float(input('Введите координату X:').replace(',','.')) #если вместо точки ввели запятую - заменим
        y = float(input('Введите координату Y:').replace(',','.'))
        break
    except ValueError:
        print("Видимо вы ошиблись. Нужно ввести число. Попробуйте еще раз...")

out_point =f'Точка ({x}, {y})' # шаблоны вывода информации
out_place= 'лежит'

if x == 0 and y == 0: 
   print(out_point, '- начало координат')
elif x == 0:
   print(out_point, out_place,'на оси Y')     
elif y == 0:
   print(out_point, out_place,'на оси X')        
elif x > 0 and y > 0:   
   print(out_point, out_place,'в I четверти')        
elif x < 0 and y > 0:   
   print(out_point, out_place,'во II четверти')        
elif x < 0 and y < 0:   
   print(out_point, out_place,'в III четверти')
else:
   print(out_point, out_place,'в IV четверти')
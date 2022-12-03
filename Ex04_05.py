# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Суммирование коэффициентов не выполнять - только сложение тел многочленов
# =======================================================================================

def generate_polynom_summ(b_lst: list, r_lst: list):
    # создаем копию основного списка чтобы не "портить" оригинал
    res = list(b_lst)
    # итерации - по наиболее короткому списку. Несовпадающие многочлены будут оставлены в исходном виде
    for i in range(len(r_lst)):
        first_poly = res[i].replace('\n', '').replace(' = 0', '')
        second_poly = r_lst[i].replace('\n', '').replace(' = 0', '')
        # вставляем начальные знаки плюс и минус, которые убирали на этапе формирования многочленов
        if second_poly[0] == '-':
            second_poly = ' - '+second_poly[1:len(second_poly)]
        else:
            second_poly = ' + '+second_poly
        res[i] = first_poly + second_poly+' = 0\n'
    return res


# константы - имена файлов
name_1, name_2, out_name = 'Ex04_04_out_1.txt', 'Ex04_04_out_2.txt', 'Ex04_05_out.txt'

try:
    with open(name_1, 'r', encoding='utf-8') as f1,\
            open(name_2, 'r', encoding='utf-8') as f2:
        lst1 = f1.readlines()
        lst2 = f2.readlines()
except IOError:
    print('Ошибка чтения файла')
    exit()


# Выбираем основной и референсный списки на основе длины файлов. За основу берем наиболее длинный
base_lst = lst1 if len(lst1) >= len(lst2) else lst2
ref_lst = lst2 if len(lst1) >= len(lst2) else lst1

out_lst = generate_polynom_summ(base_lst, ref_lst)

with open(out_name, 'a',  encoding='utf-8') as f3:
    f3.writelines(out_lst)
    print("Просуммированы многочлены из указанных файлов. Результат записан в файл", f3.name)
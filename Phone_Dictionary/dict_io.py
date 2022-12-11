
from random import choice


def read_init_values():  # чтение инициализирующих данных из файлов
    try:
        with open('names.txt', 'r', encoding='utf-8') as f1, open('descriptions.txt', 'r', encoding='utf-8') as f2:
            name_list, desc_list = f1.readlines(), f2.readlines()
            my_name_list = list(map(lambda x: choice(
                name_list).replace('\n', ''), name_list))
            my_desc_list = list(map(lambda x:  choice(
                desc_list).replace('\n', ''), desc_list))
    except IOError:
        print('Ошибка чтения файла')
    return (my_name_list, my_desc_list)


def phone_gen():  # генератор случайных телефонов
    from random import choice
    res = '+79'
    for i in range(9):
        res += str(choice(range(9)))
    return res


def menu():  # основное менб работы со словарем
    menu = {'1': 'Показать все записи', '2': 'Найти', '3': 'Добавить запись',
            '4': 'Редактировать запись', '5': 'Удалить запись', '6': 'Экспорт в xml', '7': 'Экспорт в csv', '0': 'Выход'}
    choice = -1
    print('='*20)
    for key, value in menu.items():
        print(key, ' - ', value)
    print('='*20)
    while choice not in menu.keys():
        choice = input('Выберите действие: ')
    return choice


def print_dict(book: dict):  # вывод словаря в консоль
    print('id|Фамилия|Имя|Отчество|Телефон|Комментарии')
    print('-------------------------------------------')
    for key, value in book.items():
        print(key, '|', '|'.join(value))


def write_log(*params):  # запись в лог
    with open("dict.log", 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), params)))+'\n')


def input_rec():
    name = input('Фамилия: ')
    s_name = input('Имя: ')
    f_name = input('Отчество: ')
    phone = input('Телефон: ')
    desc = input('Примечание: ')
    return (name, s_name, f_name, phone, desc)

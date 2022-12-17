
from random import choice
import service_controller as sc
import os


def clear():  # очистка консоли
    return os.system('cls')


def read_init_values():  # чтение инициализирующих данных из файлов
    try:
        with open('post_names.txt', 'r', encoding='utf-8') as f1, open('cust_names.txt', 'r', encoding='utf-8') as f2,\
                open('posts.txt', 'r', encoding='utf-8') as f3, open('autos.txt', 'r', encoding='utf-8') as f4,\
                open('work_types.txt', 'r', encoding='utf-8') as f5:
            tech_name_list, cust_name_list = f1.readlines(), f2.readlines()
            post_list, auto_list, work_list = f3.readlines(), f4.readlines(), f5.readlines()
            tech_name_list = list(
                map(lambda x: x.replace('\n', ''), tech_name_list))
            cust_name_list = list(
                map(lambda x: x.replace('\n', ''), cust_name_list))
            post_list = list(map(lambda x: x.replace('\n', ''), post_list))
            auto_list = list(map(lambda x: x.replace('\n', ''), auto_list))
            work_list = list(map(lambda x: x.replace('\n', ''), work_list))

    except IOError:
        print('Ошибка чтения файла')
    return (tech_name_list, cust_name_list, post_list, auto_list, work_list)


def phone_gen():  # генератор случайных телефонов
    from random import choice
    res = '+79'
    for i in range(9):
        res += str(choice(range(9)))
    return res


def main_menu():  # Главное меню - выбор справочника с которым будем работать
    clear()

    menu = {'1': 'Справочник сотрудников', '2': 'Справочник клиентов',
            '3': 'Справочник ремонтов', '0': 'Выход'}
    choice = -1
    print('Cправочники автосервиса'.upper())
    print('='*20)
    for key, value in menu.items():
        print(key, ' - ', value)
    print('='*20)
    while choice not in menu.keys():
        choice = input('Выберите действие: ')
    return choice


def sub_menu(branch):  # подменю в зависимости от ветки
    #    clear()
    match branch:
        case 1:
            title = 'Работа со справочником сотрудников'.upper()
            menu = {'1': 'Показать общий список сотрудников', '2': 'Найти сотрудника', '3': 'Добавить сотрудника',
                    '4': 'Изменить сотрудника', '5': 'Удалить сотрудника', '6': 'Экспорт в xml', '7': 'Экспорт в csv', '0': 'Назад'}
        case 2:
            title = 'Работа со справочником клиентов'.upper()
            menu = {'1': 'Показать общий список клиентов', '2': 'Найти клиента', '3': 'Добавить клиента',
                    '4': 'Изменить клиента', '5': 'Удалить клиента', '6': 'Экспорт в xml', '7': 'Экспорт в csv', '0': 'Назад'}
        case 3:
            title = 'Работа со справочником ремонтов'.upper()
            menu = {'1': 'Показать общий список ремонтов', '2': 'Найти ремонт', '3': 'Добавить ремонт', '4': 'Изменить ремонт',
                    '5': 'Удалить ремонт', '6': 'Вывести активные ремонты по клиенту', '7': 'Экспорт в xml', '8': 'Экспорт в csv', '0': 'Назад'}
    choice = -1
    print('\n'+'='*20)
    print(title)
    print('='*20)
    for key, value in menu.items():
        print(key, ' - ', value)
    print('='*20)
    while choice not in menu.keys():
        choice = input('Выберите действие: ')
    return (int(choice))


def print_dict(book: dict, dict_type='', client_id=''):  # вывод словаря в консоль
    match dict_type:
        case 'foreman':
            print('id|Фамилия|Имя|Отчество|Телефон|Должность|Зарплата')
        case 'customer':
            print('id|Фамилия|Имя|Отчество|Телефон|Автомобиль')
        case 'work':
            print('id|Клиент|Стоимость заказа|Вид работ|Мастер')
    print('-------------------------------------------')

    if dict_type == 'work':  # Джойн со справочниками техников и клиентов по ID - чтобы в списке отображались имена а не цифры
        if client_id == '':
            for key, value in book.items():
                cust_fio = sc.cust_dic[int(value[0])][0]+'.'+sc.cust_dic[int(
                    value[0])][1][0]+'.'+sc.cust_dic[int(value[0])][2][0]+'.'
                tech_fio = sc.tech_dic[int(value[0])][0]+'.'+sc.tech_dic[int(
                    value[0])][1][0]+'.'+sc.tech_dic[int(value[0])][2][0]+'.'
                print(key, '|', cust_fio, '|',
                      value[1], '|', value[2], '|', tech_fio)
        else:
            summ_price = 0
            for key, value in book.items():
                if int(value[0] == client_id):
                    summ_price += int(value[1])
                    cust_fio = sc.cust_dic[int(value[0])][0]+'.'+sc.cust_dic[int(
                        value[0])][1][0]+'.'+sc.cust_dic[int(value[0])][2][0]+'.'
                    tech_fio = sc.tech_dic[int(value[0])][0]+'.'+sc.tech_dic[int(
                        value[0])][1][0]+'.'+sc.tech_dic[int(value[0])][2][0]+'.'
                    print(key, '|', cust_fio, '|',
                          value[1], '|', value[2], '|', tech_fio)
            print(f'ИТОГО:       {summ_price}')
    else:
        for key, value in book.items():
            print(key, '|', '|'.join(value))


def write_log(*params):  # запись в лог
    with open("dict.log", 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), params)))+'\n')


def input_rec(dict_type: str):
    name = input('Фамилия: ')
    s_name = input('Имя: ')
    f_name = input('Отчество: ')
    phone = input('Телефон: ')
    post = cost = auto = ''
    match dict_type:
        case 'foreman':
            post = input('Должность: ')
            cost = input('Зарплата: ')
        case 'customer':
            auto = input('Марка автомобиля: ')
    return (name, s_name, f_name, phone, post, cost, auto)


def input_work():
    while True:
        try:
            cust_id = int(input('id Клиента: '))
            tech_id = int(input('id Мастера: '))
            _ = sc.cust_dic[cust_id]
            _ = sc.tech_dic[tech_id]
            price = int(input('Стоимость ремонта: '))
            break
        except ValueError:
            print("Нужно ввести целое число. Попробуйте еще раз...")
        except KeyError:
            print('Такого идентификатора нет в справочнике. Попробуйте еще раз...')
    w_type = input('Вид работ: ')
    return (cust_id, price, w_type, tech_id)


def print_client_works(cl_id):
    try:
        id = int(cl_id)
        print_dict(sc.work_dic, 'work', str(id))
        return True
    except ValueError:
        return False

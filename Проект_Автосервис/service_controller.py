import service_io as io
import service_processor as p
from random import choice, randint
from datetime import datetime as dt
from time import time

tech_dic = {}
cust_dic = {}
work_dic = {}


def t():  # текущее время
    return dt.now().strftime('%D\t%H:%M:%S')


# инициализация словарей  - читаем из файла входные данные, генерируем телефоны, добавляем случайные значения зарплат, стоимостей работ. Ключи в словарях - идентификаторы.
def init():
    io.write_log(t(), 'Начало работы')
    global tech_dic, cust_dict, work_dict
# читаем списки из файлов
    # => (tech_name_list, cust_name_list, post_list, auto_list, work_list)
    initial_data = io.read_init_values()
# Генерируем словарь технического персонала : {1:['Иванов','Иван','Иванович','+723424243234','ДОЛЖНОСТЬ', 'ЗАРПЛАТА']}
    for i in range(len(initial_data[0])):
        tech_dic[i+1] = [initial_data[0][i].split(' ')[0], initial_data[0][i].split(
            ' ')[1], initial_data[0][i].split(' ')[2], io.phone_gen(), choice(initial_data[2]), str(randint(10, 100)*1000)]
# Генерируем словарь клиентов : {1:['Иванов','Иван','Иванович','+723424243234','АВТОМОБИЛЬ',....]}
    for i in range(len(initial_data[1])):
        cust_dic[i+1] = [initial_data[1][i].split(' ')[0], initial_data[1][i].split(
            ' ')[1], initial_data[1][i].split(' ')[2], io.phone_gen(), choice(initial_data[3])]
# Генерируем словарь работ : {1:['ID_КЛИЕНТА','СТОИМОСТЬ ЗАКАЗА','ВИД РАБОТ','ID_МАСТЕРА']}
    for i in range(1, 101):
        work_dic[i] = [str(randint(1, len(cust_dic))), str(
            randint(10, 30)*1000), choice(initial_data[4]), str(randint(1, len(tech_dic)))]
# Пишем событие в лог-файл
    io.write_log(t(), 'Сгенерированы начальные справочники')
    return


def man():  # Обработка главного меню на основе выбора пользователя
    sel = io.main_menu()
    match int(sel):
        case 0:
            io.write_log(t(), 'Завершение работы')
            io.clear()
            exit()
        case _:
            sub_man(int(sel))


def sub_man(branch):  # Обработка выбора подменю - в зависимости от ветки и выбора пользователя
    sel = io.sub_menu(branch)
    match (int(branch), int(sel)):
        case (1, 0) | (2, 0) | (3, 0):
            man()
        case (1, 1):  # Сотрудники - Показать общий список
            io.print_dict(tech_dic, 'foreman')
            io.write_log(t(), 'Справочник сотрудников выведен в виде списка')
        case (1, 2):  # Сотрудники - найти сотрудника
            s = input('Введите строку для поиска ("back" - для отмены): ')
            if s == 'back':
                sub_man(branch)
            io.print_dict(p.search_items(tech_dic, s), 'foreman')
            io.write_log(
                t(), f'Осуществлен поиск сотрудника по строке "{s}". Результат выведен в виде списка.')
        case (1, 3):  # Сотрудники - Добавить сотрудника
            newrec = io.input_rec('foreman')[0:6]
            new_id = p.insert_row(newrec, 'foreman')
            outstr = f'Добавлена запись в справочник сотрудников id={new_id}: {newrec}'
            print(outstr)
            io.write_log(t(), outstr)
        case (1, 4):  # Сотрудники - Изменить сотрудника
            id_4_update = input(
                'Введите идентификатор для редактирования ("back"  - для отмены): ')
            if id_4_update == 'back':
                sub_man(branch)
            new_values = io.input_rec('foreman')[0:6]
            p.update_row(int(id_4_update), new_values, 'foreman')
            outstr = f'Изменена запись о сотруднике id={id_4_update}: {new_values}'
            print(outstr)
            io.write_log(t(), outstr)
        case (1, 5):  # Сотрудники - Удалить сотрудника
            id_4_del = input(
                'Введите идентификатор для удаления ("back"  - для возврата в главное меню): ')
            if id_4_del == 'back':
                sub_man(branch)
            if (p.delete_rows(int(id_4_del), 'foreman')):
                outstr = f'Удалена запись id={id_4_del}'
            else:
                outstr = f'Неудачная попытка удаления: id={id_4_del} не существует'
            print(outstr)
            io.write_log(t(), outstr)
        case (1, 6):  # Сотрудники - экспорт в xml
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.xml':
                filename += '.xml'
            p.xml_export(filename, 'foreman')
            outstr = f'Экспорт справочника сотрудников в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)
        case (1, 7):  # Сотрудники - экспорт в csv
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.csv':
                filename += '.csv'
            p.csv_export(filename, 'foreman')
            outstr = f'Экспорт справочника сотрудников в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)

        case (2, 1):  # Клиенты - Показать общий список
            io.print_dict(cust_dic, 'customer')
            io.write_log(t(), 'Справочник клиентов выведен в виде списка')
        case (2, 2):  # Клиенты - найти клиента
            s = input('Введите строку для поиска ("back" - для отмены): ')
            if s == 'back':
                sub_man(branch)
            io.print_dict(p.search_items(cust_dic, s), 'customer')
            io.write_log(
                t(), f'Осуществлен поиск клиента по строке "{s}". Результат выведен в виде списка.')
        case (2, 3):  # Клиенты - Добавить клиента
            nr = io.input_rec('customer')
            newrec = nr[:4]+tuple([nr[6]])
            new_id = p.insert_row(newrec, 'customer')
            outstr = f'Добавлена запись в справочник клиентов id={new_id}: {newrec}'
            print(outstr)
            io.write_log(t(), outstr)
        case (2, 4):  # Клиенты - Изменить клиента
            id_4_update = input(
                'Введите идентификатор для редактирования ("back"  - для отмены): ')
            if id_4_update == 'back':
                sub_man(branch)
            nr = io.input_rec('customer')
            new_values = nr[:4]+tuple([nr[6]])
            p.update_row(int(id_4_update), new_values, 'customer')
            outstr = f'Изменена запись о клиенте id={id_4_update}: {new_values}'
            print(outstr)
            io.write_log(t(), outstr)
        case (2, 5):  # Клиенты - Удалить клиента
            id_4_del = input(
                'Введите идентификатор для удаления ("back"  - для возврата в главное меню): ')
            if id_4_del == 'back':
                sub_man(branch)
            if (p.delete_rows(int(id_4_del), 'customer')):
                outstr = f'Удалена запись id={id_4_del}'
            else:
                outstr = f'Неудачная попытка удаления: id={id_4_del} не существует'
            print(outstr)
            io.write_log(t(), outstr)
        case (2, 6):  # Клиенты - экспорт в xml
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.xml':
                filename += '.xml'
            p.xml_export(filename, 'customer')
            outstr = f'Экспорт справочника клиентов в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)
        case (2, 7):  # Клиенты - экспорт в csv
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.csv':
                filename += '.csv'
            p.csv_export(filename, 'customer')
            outstr = f'Экспорт справочника клиентов в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)

        case (3, 1):  # Ремонты - Показать общий список
            io.print_dict(work_dic, 'work')
            io.write_log(t(), 'Справочник ремонтов выведен в виде списка')
        case (3, 2):  # Ремонты - найти ремонт
            s = input('Введите строку для поиска ("back" - для отмены): ')
            if s == 'back':
                sub_man(branch)
            io.print_dict(p.search_items(work_dic, s), 'work')
            io.write_log(
                t(), f'Осуществлен поиск ремонта по строке "{s}". Результат выведен в виде списка.')
        case (3, 3):  # Ремонты - Добавить ремонт
            newrec = io.input_work()
            new_id = p.insert_row(newrec, 'work')
            outstr = f'Добавлена запись в справочник ремонтов id={new_id}: {newrec}'
            print(outstr)
            io.write_log(t(), outstr)
        case (3, 4):  # Ремонты - Изменить ремонт
            id_4_update = input(
                'Введите идентификатор ремонта для редактирования ("back"  - для отмены): ')
            if id_4_update == 'back':
                sub_man(branch)
            newrec = io.input_work()
            if not p.update_row(int(id_4_update), newrec, 'work'):
                outstr = f'Ошибка изменения записи id={id_4_update}: не существует'
                print(outstr)
                io.write_log(t(), outstr)
            else:
                outstr = f'Изменена запись о ремонте id={id_4_update}: {newrec}'
                print(outstr)
                io.write_log(t(), outstr)
        case (3, 5):  # Ремонты - Удалить ремонт
            id_4_del = input(
                'Введите идентификатор для удаления ("back"  - для возврата в главное меню): ')
            if id_4_del == 'back':
                sub_man(branch)
            if (p.delete_rows(int(id_4_del), 'work')):
                outstr = f'Удалена запись id={id_4_del}'
            else:
                outstr = f'Неудачная попытка удаления: id={id_4_del} не существует'
            print(outstr)
            io.write_log(t(), outstr)
        case (3, 6):  # Вывод списка ремонтов по конкретному клиенту
            id_4_summ = input(
                'Введите идентификатор клиента ("back"  - для возврата в главное меню): ')
            if id_4_summ == 'back':
                sub_man(branch)
            io.print_client_works(id_4_summ)
            outstr = f'Вывод информации о ремонтах для клиента id={id_4_summ}'
            print(outstr)
            io.write_log(t(), outstr)
        case (3, 7):  # Ремонты - экспорт в xml
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.xml':
                filename += '.xml'
            p.xml_export(filename, 'work')
            outstr = f'Экспорт справочника работ в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)
        case (3, 8):  # Ремонты - экспорт в csv
            filename = input('Введите имя файла для экспорта: ')
            if filename[-4::] != '.csv':
                filename += '.csv'
            p.csv_export(filename, 'work')
            outstr = f'Экспорт справочника работ в файл{filename}'
            print(outstr)
            io.write_log(t(), outstr)

    sub_man(branch)  # зацикливание меню
    return

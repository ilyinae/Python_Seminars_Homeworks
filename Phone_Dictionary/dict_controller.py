import dict_io as io
import dict_processor as p
from random import choice
from datetime import datetime as dt
from time import time

phone_dictionary = {}


def t():  # текущее время
    return dt.now().strftime('%D\t%H:%M:%S')
# инициализация словаря  - читаем из файла имен, генерируем телефоны, добавляем случайное описание из файла описаний. Ключ словаря - идентификатор.


def init():
    global phone_dictionary
    personas = io.read_init_values()
    for i in range(len(personas[0])):
        phone_dictionary[i+1] = [personas[0][i].split(' ')[0], personas[0][i].split(
            ' ')[1], personas[0][i].split(' ')[2], io.phone_gen(), choice(personas[1])]
    io.write_log(
        t(), 'Сгенерирован телефонный справочник из {} строк'.format(len(personas[0])))
    return


def manager():  # вызов функций на основе выбранного раздела меню
    io.write_log(t(), 'Начало работы')
    choice = io.menu()
    match int(choice):
        case 1:
            io.print_dict(phone_dictionary)
            io.write_log(t(), 'Справочник выведен в виде списка')
        case 2:
            s = input(
                'Введите строку для поиска ("back" - для возврата в главное меню): ')
            if s == 'back':
                manager()
            io.print_dict(p.search_items(phone_dictionary, s))
            io.write_log(
                t(), f'Осуществлен поиск по строке "{s}". Результат выведен в виде списка.')
        case 3:
            newrec = io.input_rec()
            new_id = p.insert_row(newrec)
            io.write_log(t(), f'Добавлена запись id={new_id}: {newrec}')
        case 4:
            id_4_update = input(
                'Введите идентификатор для редактирования ("back"  - для возврата в главное меню): ')
            if id_4_update == 'back':
                manager()
            new_values = io.input_rec()
            p.update_row(id_4_update, new_values)
            print('Запись изменена...')
            io.write_log(
                t(), f'Изменена запись id={id_4_update}: {new_values}')
        case 5:
            id_4_del = input(
                'Введите идентификатор для удаления ("back"  - для возврата в главное меню): ')
            if id_4_del == 'back':
                manager()
            if (p.delete_rows(int(id_4_del))):
                print('Запись удалена...')
                io.write_log(t(), f'Удалена запись id={id_4_del}')
            else:
                io.write_log(
                    t(), f'Неудачная попытка удаления: id={id_4_del} не существует')
        case 6:
            filename = input('Введите имя файла для экспорта: ')
            p.xml_export(filename)
            print('Данные экспортированы в файл', filename)
            io.write_log(t(), f'Экспорт справочника в файл{filename}')

        case 7:
            filename = input('Введите имя файла для экспорта: ')
            p.csv_export(filename)
            print('Данные экспортированы в файл', filename)
            io.write_log(t(), f'Экспорт справочника в файл{filename}')
        case 0:
            io.write_log(t(), 'Завершение работы')
            exit()
    manager()
    return

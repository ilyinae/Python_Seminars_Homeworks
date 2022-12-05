# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1
# out
# The data is incorrect
# =======================================================================================
# Изменение постановки:
# Входной текст генерируется автоматически на основе длины списка, длины слова в списке и алфавита используемых символов, указанных в ini-файле.
# Список удаляемых слов также указан в ini-файле.
# [MAIN]
# BookLength = 20
# WordLength = 2
# Alphabet = аб
# DeletedWords = [аб, ба]
# =======================================================================================
from configparser import ConfigParser
from random import choice


def word_gen(word_len=3, alphabet='абвгдеёжзиклмнопрстуфхцчшщъыьэюя'):  # генератор слов
    res = ''
    for _ in range(word_len):
        res += choice(alphabet)
    return res


def book_gen(book_len=10,  word_len=3, alphabet='абвгдеёжзиклмнопрстуфхцчшщъыьэюя'):  # генератор списка слов
    res = []
    for _ in range(book_len):
        res.append(word_gen(word_len, alphabet))
    return res


def book_clear(book: list, deleted_words: list):  # удаляем в списке указанные слова
    return list(filter(lambda w: w not in deleted_words, book))


def readparams(ini_file_name: str):  # читаем параметры из ini-файла.
    p = ConfigParser()
    p.read(ini_file_name, encoding='utf-8')
    res = {section: dict(p.items(section)) for section in p.sections()}
    return res  # На выходе - словарь из словарей


if __name__ == "__main__":
    ini_file_name = 'Ex05_01.ini'

    ini_content = readparams(ini_file_name)
    in_params = ini_content['MAIN']  # сейчас нам нужна только эта секция

    # присвоение значений переменным из словаря
    book_len, word_len, alpha, del_str_list = (in_params['booklength'], in_params['wordlength'],
                                            in_params['alphabet'], in_params['deletedwords'])
    # создаем список случайных слов
    in_lst = book_gen(int(book_len), int(word_len), alpha)
    # удаляем из него перечисленные в параметрах слова
    cleared_lst = book_clear(in_lst, del_str_list)

    print('Исходный список: ', in_lst)
    print('Очищенный список: ', cleared_lst)

# ** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in 10 True
# out ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']

# in 10 False
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный',
# 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']
# #=======================================================================================
from random import choice


def joke_generator(nou, adv, adj):
    try:
        w1, w2, w3 = choice(tuple(nou)), choice(tuple(adv)), choice(tuple(adj))
    except IndexError:
        return -1
    return f'{w1} {w2} {w3}'


def joke_list_generator(list1, list2, list3, num, unique=False):
    res = []
    nou, adv, adj = set(list1), set(list2), set(list3)
    if not unique:
        for _ in range(num):
            res.append(joke_generator(nou, adv, adj))
        return res
    else:
        for _ in range(num):
            joke = joke_generator(nou, adv, adj)
            if joke == -1:
                return res
            res.append(joke)
            nou.discard(joke.split(' ')[0])
            adv.discard(joke.split(' ')[1])
            adj.discard(joke.split(' ')[2])
        return res


def input_data():
    while True:
        try:
            list_len = int(input('Введите длину списка шуток: '))
            un = int(input('Повторяем слова? (0 - нет, 1 - да): '))
            if un not in (0, 1):
                un = 1
            break
        except ValueError:
            print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")
    return [list_len, not un]


def read_lists():
    try:
        with open('Ex06_05_input.txt', 'r', encoding='utf-8') as f:
            lst = (f.readlines())
    except IOError:
        print('Ошибка чтения файла')
        exit()
    return list(map(lambda x: x.replace('\n', '').split(', '), lst))


if __name__ == "__main__":
    print(joke_list_generator(* read_lists()+input_data()))

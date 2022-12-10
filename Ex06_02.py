# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in : 100
# out: [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in: 424
# out: [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]
# =======================================================================================


def input_data():
    while True:
        try:
            n = int(input('Введите N: '))
            break
        except ValueError:
            print("Видимо вы ошиблись. Нужно ввести число. Попробуйте снова...")
    return n


def list_gen(list_limit: int):
    return [i for i in range(20, list_limit+1) if not i % 20 or not i % 21]


def print_results(data: list):
    print('Выходной список: ', data)


if __name__ == "__main__":
    print_results(list_gen(input_data()))
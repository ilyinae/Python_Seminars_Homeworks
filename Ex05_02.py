# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text: 'text_words.txt'
# Enter the file name to record: 'text_code_words.txt'
# Enter the name of the file to decode: 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a
# 11v2b2w2P3u2T1Y1y2W2Q
# 5a29v4s3D3d2F4g2O3i2a
# 11v2b2w2P3u2T1Y1y2W2Q
# =======================================================================================


def rle_encode(in_str: str):  # кодирование строки
    res = ''
    if len(in_str) == 0 or (in_str) == '\n':  # переносы строк не кодируем
        return in_str
    elif len(in_str) == 1:
        return '1' + in_str
    run_length = 0  # счетчик длины рана
    for i in range(len(in_str)):
        run_length += 1
        # если следующий шаг - конец строки или конец рана - заканчиваем ран
        if len(in_str) == i + 1 or in_str[i] != in_str[i + 1]:
            # переносы строк не кодируем
            res = res + str(run_length) + in_str[i] if in_str[i] != '\n' else res + in_str[i]
            run_length = 0
    return res


def rle_decode(in_str: str):  # раскодирование строки
    res = ''
    if len(in_str) == 0 or (in_str) == '\n':  # переносы строк пропускаем
        return in_str
    dec_length = 0  # счетчик длины числовой части
    num_str = ''    # строка для сбора числа
    for i in range(len(in_str)):
        if in_str[i].isdecimal():
            dec_length += 1
            num_str += in_str[i]
        else:
            if in_str[i] == '\n':
                res = res + in_str[i]
            else:
                res = res + (int(num_str)*in_str[i])
            dec_length = 0
            num_str = ''
    return res


def sl_rle_encode(string_list: list):  # кодирование списка строк
    return list(map(rle_encode, string_list))


def sl_rle_decode(string_list: list):  # pacкодирование списка строк
    return list(map(rle_decode, string_list))


def read_data(file_name: str):  # чтение списка строк из файла
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            res = f.readlines()
    except IOError:
        print('Ошибка чтения файла')
        exit()
    return res


def write_data(file_name: str, out_data: list, mode='a'):  # запись списка строк в файл
    with open(file_name, mode, encoding='utf-8') as f:
        f.writelines(out_data)


if __name__ == "__main__":
    in_file_name, enc_file_name, dec_file_name = 'Ex05_02_input.txt', 'Ex05_02_encoded.txt', 'Ex05_02_decoded.txt'

    write_data(enc_file_name, sl_rle_encode(read_data(in_file_name)), 'w')
    write_data(dec_file_name, sl_rle_decode(read_data(enc_file_name)), 'w')
    print('Закодированный файл - {}\nРаскодированный файл - {}'.format(enc_file_name, dec_file_name))
    

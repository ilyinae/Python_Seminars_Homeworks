import dict_controller as dc


# поиск в словаре по подстроке - если она содержится в ключе или списке - добавляем в результирующий список
def search_items(pd, searchstring: str):
    res = {}
    for key, value in pd.items():
        if f'{key}'.count(searchstring) != 0 or len(list(filter(lambda x: x.count(searchstring) != 0, value))) != 0:
            res[key] = value
    return res


def insert_row(row: tuple):
    new_id = sorted(dc.phone_dictionary.keys())[
        len(dc.phone_dictionary.keys())-1]+1
    dc.phone_dictionary[new_id] = list(row)
    return new_id


def delete_rows(key_4_del):
    res = False
    if key_4_del in dc.phone_dictionary.keys():
        res = True
        dc.phone_dictionary.pop(key_4_del)
    return res


def update_row(k, v):
    d = {}
    d[k] = list(v)
    dc.phone_dictionary.update(d)
    return


def xml_export(fn):
    xml = '<?xml version = "1.0" encoding = "UTF-8"?>\n'
    xml += '<ContactList>\n'
    for key in dc.phone_dictionary.keys():
        xml += f'\t<ContactInfo Id="{key}" '
        for i in range(len(dc.phone_dictionary[key])):
            match i:
                case 0:
                    xml += f'SecondName="{dc.phone_dictionary[key][i]}" '
                case 1:
                    xml += f'FirstName="{dc.phone_dictionary[key][i]}" '
                case 2:
                    xml += f'Patronymic="{dc.phone_dictionary[key][i]}" '
                case 3:
                    xml += f'Phone="{dc.phone_dictionary[key][i]}" '
                case 4:
                    xml += f'Comments="{dc.phone_dictionary[key][i]}"/>\n'
    xml += '</ContactList>\n'
    with open(fn, 'w', encoding='utf-8') as xmlf:
        xmlf.write(xml)
    return


def csv_export(fn):
    csv = 'id\tФамилия\tИмя\tОтчество\tТелефон\tКомментарии\n'
    for key, value in dc.phone_dictionary.items():
        csv += f'{key}\t'+'\t'.join(value)+'\n'
    with open(fn, 'w', encoding='utf-8') as csvf:
        csvf.write(csv)
    return

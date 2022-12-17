import service_controller as sc


# поиск в словаре по подстроке - если она содержится в ключе или списке - добавляем в результирующий список
def search_items(pd, searchstring: str):
    res = {}
    for key, value in pd.items():
        if f'{key}'.count(searchstring) != 0 or len(list(filter(lambda x: x.count(searchstring) != 0, value))) != 0:
            res[key] = value
    return res


def insert_row(row: tuple, dict_type: str):
    match dict_type:
        case 'foreman':
            new_id = sorted(sc.tech_dic.keys())[len(sc.tech_dic.keys())-1]+1
            sc.tech_dic[new_id] = list(row)
        case 'customer':
            new_id = sorted(sc.cust_dic.keys())[len(sc.cust_dic.keys())-1]+1
            sc.cust_dic[new_id] = list(row)
        case 'work':
            new_id = sorted(sc.work_dic.keys())[len(sc.work_dic.keys())-1]+1
            sc.work_dic[new_id] = list(row)
    return new_id


def delete_rows(key_4_del, dict_type: str):
    res = False
    match dict_type:
        case 'foreman': my_dic = sc.tech_dic
        case 'customer': my_dic = sc.cust_dic
        case 'work': my_dic = sc.work_dic
    if key_4_del in my_dic.keys():
        res = True
        my_dic.pop(key_4_del)
    return res


def update_row(k, v, dict_type: str):
    try:
        match dict_type:
            case 'foreman': sc.tech_dic[k] = list(v)
            case 'customer': sc.cust_dic[k] = list(v)
            case 'work': sc.work_dic[k] = list(v)
        return True
    except KeyError:
        return False


def xml_export(fn, dict_type: str):
    xml = '<?xml version = "1.0" encoding = "UTF-8"?>\n'
    match dict_type:
        case 'foreman':
            xml += '<ForemanList>\n'
            for key in sc.tech_dic.keys():
                xml += f'\t<ForemanInfo Id="{key}" '
                for i in range(len(sc.tech_dic[key])):
                    match i:
                        case 0:
                            xml += f'SecondName="{sc.tech_dic[key][i]}" '
                        case 1:
                            xml += f'FirstName="{sc.tech_dic[key][i]}" '
                        case 2:
                            xml += f'Patronymic="{sc.tech_dic[key][i]}" '
                        case 3:
                            xml += f'Phone="{sc.tech_dic[key][i]}" '
                        case 4:
                            xml += f'Post="{sc.tech_dic[key][i]}" '
                        case 5:
                            xml += f'Cost="{sc.tech_dic[key][i]}"/>\n'
            xml += '</ForemanList>\n'
        case 'customer':
            xml += '<CustomerList>\n'
            for key in sc.cust_dic.keys():
                xml += f'\t<CustomerInfo Id="{key}" '
                for i in range(len(sc.cust_dic[key])):
                    match i:
                        case 0:
                            xml += f'SecondName="{sc.cust_dic[key][i]}" '
                        case 1:
                            xml += f'FirstName="{sc.cust_dic[key][i]}" '
                        case 2:
                            xml += f'Patronymic="{sc.cust_dic[key][i]}" '
                        case 3:
                            xml += f'Phone="{sc.cust_dic[key][i]}" '
                        case 4:
                            xml += f'Auto="{sc.cust_dic[key][i]}"/>\n'
            xml += '</CustomerList>\n'
        case 'work':
            xml += '<WorkList>\n'
            for key in sc.work_dic.keys():
                xml += f'\t<WorkInfo Id="{key}" '
                for i in range(len(sc.work_dic[key])):
                    match i:
                        case 0:
                            xml += f'Customer_id="{sc.work_dic[key][i]}" '
                        case 1:
                            xml += f'Price="{sc.work_dic[key][i]}" '
                        case 2:
                            xml += f'WorkType="{sc.work_dic[key][i]}" '
                        case 3:
                            xml += f'Foreman_id="{sc.work_dic[key][i]}"/>\n '
            xml += '</WorkList>\n'
    with open(fn, 'w', encoding='utf-8') as xmlf:
        xmlf.write(xml)
    return


def csv_export(fn, dict_type: str):
    match dict_type:
        case 'foreman':
            csv = 'id\tФамилия\tИмя\tОтчество\tТелефон\tДолжность\tОклад\n'
            my_dic = sc.tech_dic
        case 'customer':
            csv = 'id\tФамилия\tИмя\tОтчество\tТелефон\tМарка_автомобиля\n'
            my_dic = sc.cust_dic
        case 'work':
            csv = 'id\tID Клиента\tСтоимость_работ\tВид_работ\tID_Мастера\n'
            my_dic = sc.work_dic

    for key, value in my_dic.items():
        csv += f'{key}\t'+'\t'.join(value)+'\n'
    with open(fn, 'w', encoding='utf-8') as csvf:
        csvf.write(csv)
    return

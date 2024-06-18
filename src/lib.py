
headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']

def import_from_txt(filename): 
    phone_book = []
    if filename == '':
        return phone_book    
    try:
        with open(filename,'r',encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(headers, line.rstrip().split(',')))
                phone_book.append(record)
    except IOError:
        pass
    return phone_book


def export_to_txt(filename , phone_book, mode = 'w'):
    if filename == '':
        return    
    with open(filename,mode,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


def find_by_lastname(phone_book,last_name):
    '''3. Найти абонента по фамилии''' 
    return list(filter(lambda record: record["Фамилия"] == last_name, phone_book))

def find_by_number(phone_book,number):
    '''4. Найти абонента по номеру телефона'''
    return list(filter(lambda record: record["Телефон"] == number, phone_book))

def find_by_row_number(phone_book,row_num):
    '''Найти запись по номеру строки'''
    result = []
    result.append(phone_book[row_num-1])
    return result


def add_user(phone_book,user_data):
    '''5. Добавить абонента в справочник'''
    if user_data == '': 
        return False
    user_data = user_data.rstrip().split(',')
    if len(user_data) != len(headers):
        return False
    record = dict(zip(headers, user_data))
    phone_book.append(record)    
    return True


def change_number(phone_book,last_name,new_number):
    '''6. Изменить данные абонента в справочнике'''
    def change(record):
        if record["Фамилия"] == last_name:
            record["Телефон"] = new_number
        return record
    phone_book = list(map(change, phone_book))
    return phone_book


def delete_by_lastname(phone_book,lastname):
    '''7. Удалить абонента из справочника'''
    result = False
    tmp_list = find_by_lastname(phone_book,lastname)
    for record in tmp_list:
        phone_book.remove(record)
        result = True
    return result


if __name__ == '__main__':
    pass
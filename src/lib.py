def import_from_txt(filename): 
    phone_book = []
    if filename == '':
        return phone_book
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    try:
        with open(filename,'r',encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(fields, line.rstrip().split(',')))
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
    return phone_book


def find_by_number(phone_book,number):
    '''4. Найти абонента по номеру телефона'''
    return phone_book


def add_user(phone_book,user_data):
    '''5. Добавить абонента в справочник'''
    return True


def change_number(phone_book,last_name,new_number):
    '''6. Изменить данные абонента в справочнике'''
    return phone_book


def delete_by_lastname(phone_book,lastname):
    '''7. Удалить абонента из справочника'''
    return True


if __name__ == '__main__':
    pass
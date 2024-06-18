def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Загрузить справочник из текстового формата\n",          
          "2. Отобразить весь справочник\n",
          "3. Найти абонента по фамилии\n",
          "4. Найти абонента по номеру телефона\n",
          "5. Добавить абонента в справочник\n",
          "6. Изменить данные абонента в справочнике\n",
          "7. Удалить абонента из справочника\n",
          "8. Сохранить справочник в текстовом формате\n",
          "0. Закончить работу\n")
    try:
        choice = int(input())
    except:
        choice = 0
    return choice


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


def export_to_txt(filename , phone_book):
    if filename == '':
        return    
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


def print_result(phone_book):
    '''2. Отобразить весь справочник'''
    col_size = 20
    head = ''
    div_line = ''
    for i in range(len(phone_book)):
        s=''
        for h,v in phone_book[i].items():
            if i == 0:
                head = head + h.ljust(col_size) + '|'
                div_line = div_line + '-' * col_size + '+'
            s = s + v.ljust(col_size) + '|'
        if i == 0: 
            print(f'{head[:-1]}')
            print(f'{div_line[:-1]}')
        print(f'{s[:-1]}')
        

def find_by_lastname(phone_book,last_name):
    '''3. Найти абонента по фамилии'''
    pass


def find_by_number(phone_book,number):
    '''4. Найти абонента по номеру телефона'''
    pass


def add_user(phone_book,user_data):
    '''5. Добавить абонента в справочник'''
    pass


def change_number(phone_book,last_name,new_number):
    '''6. Изменить данные абонента в справочнике'''
    pass


def delete_by_lastname(phone_book,lastname):
    '''7. Удалить абонента из справочника'''
    pass


if __name__ == '__main__':
    pass
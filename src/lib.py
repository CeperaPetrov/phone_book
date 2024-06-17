
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента в справочнике\n"
          "6. Удалить абонента из справочника\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))
           phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    '''1. Отобразить весь справочник'''
    pass

def find_by_lastname(phone_book,last_name):
    '''2. Найти абонента по фамилии'''
    pass

def find_by_number(phone_book,number):
    '''3. Найти абонента по номеру телефона'''
    pass

def add_user(phone_book,user_data):
    '''4. Добавить абонента в справочник'''
    pass

def change_number(phone_book,last_name,new_number):
    '''5. Изменить данные абонента в справочнике'''
    pass

def delete_by_lastname(phone_book,lastname):
    '''6. Удалить абонента из справочника'''
    pass

if __name__ == '__main__':
    pass
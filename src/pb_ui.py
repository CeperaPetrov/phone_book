from lib import *

def show_menu():
    '''Меню справочника'''
    print("\nВыберите необходимое действие:\n",
          "1. Загрузить данные справочника из текстового формата\n",          
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

def print_result(phone_book):
    '''Вывод в терминал данных справочника'''
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

def main():
    filename = ''
    phone_book= []
    choice=show_menu()    

    while (choice):
        #----------------------------------------------------------------------
        if choice == 1:
            filename=input('filename ')
            phone_book=import_from_txt(filename)
        #----------------------------------------------------------------------
        elif choice == 2:
            print_result(phone_book)
        #----------------------------------------------------------------------
        elif choice == 3:
            last_name=input('lastname ')
            print_result(find_by_lastname(phone_book,last_name))
        #----------------------------------------------------------------------
        elif choice == 4:
            number=input('number ')
            print_result(find_by_number(phone_book,number))
        #----------------------------------------------------------------------
        elif choice == 5:
            user_data=input('new data ')
            if add_user(phone_book,user_data):
                print(f"данные абонента {user_data} добавлены в телефонный справочник\n")
            else:
                print(f"Не удалось добавить абонента {user_data} в телефонный справочник\n")                
        #----------------------------------------------------------------------
        elif choice == 6:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print_result(change_number(phone_book,last_name,new_number))	    	
        #----------------------------------------------------------------------
        elif choice == 7:
            lastname=input('lastname ')
            if delete_by_lastname(phone_book,lastname):
                print(f"данные абонента {lastname} удалены из телефонного справочника\n")
            else:
                print(f"Не удалось удалть абонента {lastname} из телефонного справочника\n")
        #----------------------------------------------------------------------
        elif choice == 8:
            #lastname=input('lastname ')
            export_to_txt(filename, phone_book)
        #----------------------------------------------------------------------
        choice=show_menu()


if __name__ == '__main__':
    main()
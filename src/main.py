from lib import *

def main():
    filename = 'phonebook.txt'
    choice=show_menu()
    phone_book=read_txt(filename)

    while (choice != 8):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice == 3:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice == 4:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            # write_txt(filename,phone_book)     1               
        elif choice == 5:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))	    	
        elif choice == 6:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice == 7:
            lastname=input('lastname ')
            write_txt(filename, phone_book)

        choice=show_menu()

if __name__ == '__main__':
    main()
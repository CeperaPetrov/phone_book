from lib import *

def main():
    filename = ''
    phone_book= []
    choice=show_menu()    

    while (choice):
        if choice == 1:
            filename=input('filename ')
            phone_book=import_from_txt(filename)
        elif choice == 2:
            print_result(phone_book)
        elif choice == 3:
            last_name=input('lastname ')
            print_result(find_by_lastname(phone_book,last_name))
        elif choice == 4:
            number=input('number ')
            print_result(find_by_number(phone_book,number))
        elif choice == 5:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            # write_txt(filename,phone_book)     1               
        elif choice == 6:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print_result(change_number(phone_book,last_name,new_number))	    	
        elif choice == 7:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice == 8:
            lastname=input('lastname ')
            export_to_txt(filename, phone_book)

        choice=show_menu()

if __name__ == '__main__':
    main()
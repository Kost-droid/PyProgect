
# # Цикл виду не труе
# две строки между функциями
# функция маин
# не более 40 строк в функци
# функции без ссылок на глобалные переменые (с параметрами)


def menu ():
    print ('\n1. List_print \n2. Search \n3. Add \n4. Del \n5. Exit  \n********')


def list_print (phone_dict):
    [print (x) for x in phone_dict.items()]


def search (phone_dict):
    print (phone_dict.get(input('Input name ')))


def refresh(phone_dict, name_item = None):
    if not name_item is None:
        phone_dict[name_item] = input('Input new phone ')


def add_item (phone_dict):
    name_item = input('Input new name ')
    if name_item in phone_dict:
        print('Name exist, refresh ? ')
        user_answer = input("y/n ")
        if user_answer == 'y':
            refresh (phone_dict, name_item)
        else:
            return
    else:
        new_phone = input('Input new phone ')
        phone_dict[name_item]=new_phone


def del_item (phone_dict):
    name_item = input('Input dell name ')
    del phone_dict[name_item]

def main ():

    phone_dict = {'Anna' : '+79059700582', 'Bob' : '+79059700583', 'Jon' : '+79059700584'}

    exit_program = True

    while exit_program:
        menu()
        user_command = input('Input command ')
        if user_command == '1':
            list_print (phone_dict)
        elif user_command == '2':
            search(phone_dict)
        elif user_command == '3':
            add_item(phone_dict)
        elif user_command == '4':
            del_item (phone_dict)
        elif user_command == '5':
            exit_program = False
    else:
        print ('By !!')


main ()


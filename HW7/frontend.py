import os.path

def main_menu():
    print('''Main menu. Aviable actions:\n
        1 - Show contacts
        2 - Create new contact
        3 - Import contacts from file
        4 - Close programm''')

def show_contacts(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print("{:3} {:15} {:15} {:11} {:20} {}".format(*line.split(";")))

def new_contact_input():
    f_name = input("Insert contact's first name: ")
    l_name = input("Insert contact's last name: ")
    birthday = input("Insert contact's birthday: ")
    occupation = input("Insert contact's occupation: ")
    phone_num = input("Insert contact's phone number: ")
    print("New contact seccessfully created!")
    return f_name, l_name, birthday, occupation, phone_num

def import_file_input():
    file_name = input("Insert file name to import: ")
    if os.path.isfile(file_name):
        show_contacts(file_name)
        if input("Import file to contacts? Y/N").capitalize() == 'Y':
            print("File seccessfully imported.")
            return file_name
        else:
            print("Import aborted by user.")
            return ''
    else:
        print("File wasn't founded. Try again.")
        return file_name

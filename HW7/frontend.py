columns = ['ID', 'First name', 'Last name',
           'Birthday', 'Occupation', 'Phone number']


def main_menu():
    print('''Main menu. Aviable actions:\n
    1 - Show contacts
    2 - Create new contact
    3 - Import contacts from file
    4 - Close programm''')


def show_contacts(file_name):
    print("List of contacts", end="\n\n")
    print("{:3} {:15} {:15} {:11} {:20} {}".format(*columns))
    with open(file_name, 'r') as file:
        for line in file:
            print("{:3} {:15} {:15} {:11} {:20} {}".format(
                *line.split(";")), end='')
    print()


def show_new(data):
    print("{:3} {:15} {:15} {:11} {:20} {}".format(*columns), end="\n\n")
    print("{:3} {:15} {:15} {:11} {:20} {}".format(*data))


def new_contact_input():
    f_name = input("Insert contact's first name: ")
    l_name = input("Insert contact's last name: ")
    birthday = input("Insert contact's birthday: ")
    occupation = input("Insert contact's occupation: ")
    phone_num = input("Insert contact's phone number: ")
    print()
    return f_name, l_name, birthday, occupation, phone_num


def import_file_input():
    return input("Insert file name to import: ")


def new_contact_status(status):
    if status == 1:
        print("New contact seccessfully created!", end="\n\n")
    else:
        print("Creating new contact aborted by user", end="\n\n")


def import_status(status):
    if status == 1:
        print("File seccessfully imported!", end="\n\n")
    elif status == 2:
        print("Import aborted by user.", end="\n\n")
    else:
        print("File wasn't founded. Try again.", end="\n\n")

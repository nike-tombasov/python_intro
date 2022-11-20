import os.path
import backend
import frontend

def run():
    while True:
        frontend.main_menu()
        action = input('Choose action to do: ')

        match action:
            case '1':
                frontend.show_contacts('database.csv')
            case '2':
                backend.new_contact_save(frontend.new_contact_input())
            case '3':
                file_name = frontend.import_file_input()
                if os.path.isfile(file_name):
                    backend.import_data(file_name)
            case '4':
                exit("Programm closed.")
            # case '5':

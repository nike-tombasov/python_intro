import os.path
import sys
import backend
import frontend

def run():
    while True:
        frontend.main_menu()
        action = input('*Choose action to do: ')
        print()

        match action:
            case '1': # Show base in console
                frontend.show_contacts('database.csv')
            
            case '2': # New contact init
                status = 0
                new_contact = frontend.new_contact_input()
                
                if new_contact[5]: # for multiphone contact
                    backend.pre_new_multiphone_contact(new_contact)
                    frontend.show_contacts('temp.csv', 1)
                    if input("*Save this contact? Y/N ").capitalize() == 'Y':
                        backend.new_multiphone_save()
                        status = 1
                        frontend.new_contact_status(status)
                    else:
                        frontend.new_contact_status(status)
                else: # for simple contact
                    new_contact[4] = new_contact[4][0]
                    new_contact = backend.pre_new_line(new_contact)
                    frontend.show_new(new_contact)
                    if input("*Save this contact? Y/N ").capitalize() == 'Y':
                        backend.new_contact_save(new_contact)
                        status = 1
                        frontend.new_contact_status(status)
                    else:
                        frontend.new_contact_status(status)
            
            case '3': # Importing file to database
                status = 0
                file_name = frontend.import_file_input()
                if os.path.isfile(file_name):
                    frontend.show_contacts(file_name)    
                    if input("*Import file to contacts? Y/N ").capitalize() == 'Y':
                        backend.import_data(file_name)
                        status = 1
                        frontend.import_status(status)
                    else:
                        status = 2
                        frontend.import_status(status)
                else:
                    frontend.import_status(status)

            case '4': # Exit
                sys.exit("Programm closed.")
            # case '5':

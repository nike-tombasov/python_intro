# Contacts database

## Target

Make contact database, that can export data from base or import from given file, can show imporing data and show data from base. 

* File format - csv, xml or json
* Data fields:
1) id
2) first name
3) last name
4) birthday
5) occupation
6) phone numbers

## Moduls and methods

* main (**main.py**) - starting system

* user interface (**ui.py**)

    1) main menu controlling


* backend (**backend.py**)

    1) inserting new contact to database manualy (*new_contact_save*)
    2) exporting database to file ???
    3) imporing from file to database (*import_data*)
    4) helpers (get_next_id)

* frontend (**frontend.py**)

    1. show main menu: (*main_menu*)
        1) Show contacts 
        2) Create new contact
        3) Import contacts from file
        4) Close programm
    2. creating new contact (*new_contact_input*)
    3. send current database to console (*show_contacts*)
    4. importing fil (*import_file_input*)
    5. show importing database (*import_file_input*+*show_contacts*)
 



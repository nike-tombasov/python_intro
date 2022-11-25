# Contacts database

## Target

Make contact database, that can export data from base or import from given file, can show importing data and show data from base. 

* File format - **csv**, xml or json
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

    1) user main menu controlling
    2) user acceptions to rewrite database
    3) accses to moduls


* backend (**backend.py**)

    1) preparing inputed new contact for print and save (*pre_new_line*, *pre_new_multiphone_contact*)
    2) saving new contact to database (*new_contact_save*, *new_multiphone_save*)
    3) imporing from file to database (*import_data*)
    4) helpers (get_next_id)

* frontend (**frontend.py**)

    1. show main menu: (*main_menu*)
        1) Show contacts 
        2) Create new contact
        3) Import contacts from file
        4) Close programm
    2. creating data with new contact manualy and sending to console (*new_contact_input* + *show_new*/*show_contacts*)
    3. sending current database to console (*show_contacts*)
    4. importing file input (*import_file_input*)
    5. show importing database (*import_file_input* + *show_contacts*)
 



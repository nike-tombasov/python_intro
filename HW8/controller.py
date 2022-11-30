import os
import ui
import frontend
import sqlite3

def run():
    
    while True:
        if not os.path.exists('school.db'):
            ui.no_db()
        conn = sqlite3.connect('school.db')
        cur = conn.cursor()

        frontend.main_menu()
        action = input('*Choose action to do: ')
        print()

        match action:
            case '1': # Show database
                ui.display_db(cur)

            case '2': # New record
                ui.new_record(cur, conn)    

            case '3': # Editing records                   
                ui.record_editor(cur, conn)

            case '4': # Deleting record
                ui.deleting(cur, conn)

            case '5': # Searching
                ui.searcher(cur)

            case '6': # Erase database
                if input("*You really want to erase this database? Y/N ").capitalize() == 'Y':
                    if input("*Are you so sure you want to erase this database? Y/N ").capitalize() == 'Y':
                        if input("*Are you so so sure? You'll lost all data. Y/N ").capitalize() == 'Y':
                            print()
                            print("So be it", end="\n\n")
                            conn.close()
                            os.remove('school.db')
                            print('Database seccessfully erased.', end="\n\n")
            case '7': # Exit
                conn.close()
                print("Programm closed.")
                break

            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")

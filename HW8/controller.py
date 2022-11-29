# import os.path
# import sys
# import backend
import ui
import frontend
import sqlite3

def run():
    while True:
        conn = sqlite3.connect('school.db')
        cur = conn.cursor()

        frontend.main_menu()
        action = input('*Choose action to do: ')
        print()

        match action:
            case '1': # Show database
                ui.display_db(cur, conn)

            case '2': # New record
                ui.new_record(cur, conn)    

            case '3': # Editing records
                pass

            case '4': # Exit
                conn.close()
                print("Programm closed.")
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")

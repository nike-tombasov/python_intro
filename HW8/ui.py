import frontend
import backend
import dbinit
import sys

def no_db():
    print("Database doesn't found!", end="\n\n")
    if input("*Initialize default version of database? Y/N ").capitalize() == 'Y':
        dbinit.initialize_db()
        print()
        print("Database seccessfully initialized!", end="\n\n")
    else:
        sys.exit("Programm closed.")


def show_grades(cur):
    cur.execute('''SELECT grade_name, start_year, graduation_year 
                FROM grades''')
    frontend.dipslay_sheet(cur.fetchall(), 1)    


def save_query_csv(query):
    if input("*Save sheet to CSV file? Y/N ").capitalize() == 'Y':
        file_name = input("*Enter file name: ")
        if backend.save_file_csv(query, file_name):
            print("File seccessfully saved!", end="\n\n")


def display_db(cur):
    while True:
        frontend.display_menu()
        action = input('*Choose action to do: ')
        if action.isdigit():
            action = int(action)
        print()
        
        match action:
            case 1: # Grades list
                cur.execute('''SELECT grade_name, start_year, graduation_year 
                            FROM grades''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action)
                save_query_csv(query)
            case 2: # Pupils list
                cur.execute('''SELECT pupil_id, first_name, last_name, 
                            birthday, grade_name, graduation_year
                            FROM pupils LEFT JOIN grades 
                            ON grades.grade_id = pupils.grade_id''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action)
                save_query_csv(query)
            case 3: # Grades with pupils list
                cur.execute('''SELECT grade_name, start_year, graduation_year, 
                            first_name, last_name, birthday
                            FROM grades INNER JOIN pupils 
                            ON grades.grade_id = pupils.grade_id''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action)
                save_query_csv(query)
            case 4: # Pupils by grade
                show_grades(cur)
                
                grade = input('*Insert grade name from list above: ').upper()

                cur.execute(f'''SELECT grade_name, start_year, graduation_year, 
                            first_name, last_name, birthday
                            FROM grades LEFT JOIN pupils 
                            ON grades.grade_id = pupils.grade_id
                            WHERE grade_name="{grade}"''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action, grade)
                save_query_csv(query)
            case 5: # Full database
                cur.execute('''SELECT grade_name, start_year, graduation_year, 
                            first_name, last_name, birthday
                            FROM grades LEFT JOIN pupils 
                            ON grades.grade_id = pupils.grade_id''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action)
                save_query_csv(query)
            case 6: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")


def new_record(cur, conn):
    while True:
        frontend.new_record_menu()
        status = 0
        action = input('*Choose table for new record: ')
        if action.isdigit():
            action = int(action)        
        print()

        match action:
            case 1: # Add to grades
                grade = input('*Insert new grade name: ')
                start = int(input('*Insert start year: '))
                graduat = int(input('*Insert graduation year: '))
                frontend.new_record_preview([grade, start, graduat], action)
                
                if input("*Save this grade? Y/N ").capitalize() == 'Y':
                    backend.new_record(cur, action, [backend.get_next_id(cur, action), grade, start, graduat])
                    conn.commit()
                    status = 1
                    frontend.new_record_status(status, action)
                else:
                    frontend.new_record_status(status, action)
            
            case 2: # Add to pupils
                first = input('*Insert first name: ').title()
                last = input('*Insert last name: ').title()
                birth = input('*Insert date of birth: ')

                show_grades(cur)

                grade = input('*Insert grade name from list above: ').capitalize()
                cur.execute(f'SELECT grade_id FROM grades where grade_name="{grade}"')
                grade_id = cur.fetchone()[0]
                new = [backend.get_next_id(cur, action), first, last, birth, grade_id]
                frontend.new_record_preview(new, action)
                
                if input("*Save this pupil? Y/N ").capitalize() == 'Y':
                    backend.new_record(cur, action, new)
                    conn.commit()
                    status = 1
                    frontend.new_record_status(status, action)
                else:
                    frontend.new_record_status(status, action)
            
            case 3: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")

def record_editor(cur, conn):
    while True:
        frontend.editor_menu()
        status = 0
        action = input('*Choose table for new record: ')
        if action.isdigit():
            action = int(action)        
        print()

        match action:
            case 1: # Edit grades
                show_grades(cur)

                grade = input('*Insert grade name from list above: ').upper()                
                cur.execute(f'SELECT grade_id FROM grades where grade_name="{grade}"')
                grade_id = cur.fetchone()[0]
                
                

                pass
            case 2: # Edit pupils
                pass
            case 3: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")





# match action:
#     case '1':
#         pass
#     case '2':
#         pass
#     case '3':
#         pass
#     case '4':
#         pass
#     case '5':
#         break
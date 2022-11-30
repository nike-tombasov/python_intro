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
                frontend.display_grades_sheet(cur)
                
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
                frontend.display_grades_sheet(cur)
                grade = input('*Insert new grade name: ')
                start = int(input('*Insert start year: '))
                graduat = int(input('*Insert graduation year: '))
                frontend.new_record_preview([grade, start, graduat], action)
                
                if input("*Save this grade? Y/N ").capitalize() == 'Y':
                    backend.new_record(cur, action, [backend.get_next_id(cur, action), grade, start, graduat])
                    conn.commit()
                    status = 1
                frontend.new_record_status(status, action)
            
            case 2: # Add to pupils
                first = input('*Insert first name: ').title()
                last = input('*Insert last name: ').title()
                birth = input('*Insert date of birth: ')

                frontend.display_grades_sheet(cur)

                grade = input('*Insert grade name from list above: ').upper()
                grade_id = backend.get_grade_id(cur, grade)
                new_pupil = [backend.get_next_id(cur, action), first, last, birth, grade_id]
                frontend.new_record_preview(new_pupil, action)
                
                if input("*Save this pupil? Y/N ").capitalize() == 'Y':
                    backend.new_record(cur, action, new_pupil)
                    conn.commit()
                    status = 1
                frontend.new_record_status(status, action)
            
            case 3: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")


def record_editor(cur, conn):
    while True:
        frontend.editor_menu()
        action = input('*Choose table where edit record: ')
        print()

        match action:
            case '1': # Edit grades
                grade_editor(cur, conn)
            case '2': # Edit pupils
                pupil_editor(cur, conn)
            case '3': # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")


def grade_editor(cur, conn):
    while True:
        frontend.display_grades_sheet(cur)
        grade = input('*Insert grade name from list above: ').upper()
        grade_id = backend.get_grade_id(cur, grade)
        new_grade = backend.get_grade_line(cur, grade_id)
        
        frontend.grade_editor_menu()
        status = 0
        action = input('*Choose which field to edit: ')
        if action.isdigit():
            action = int(action)
        print()

        match action:
            case 1: # Edit grade name
                new_grade[0] = input('*Insert new grades name: ').upper()
            case 2: # Edit grade start
                new_grade[1] = int(input('*Insert new grades start year: '))
            case 3: # Edit grade graduate
                new_grade[2] = int(input('*Insert new grades graduation year: '))
            case 4: # Edit all
                new_grade[0] = input('*Insert new grades name: ').upper()
                new_grade[1] = int(input('*Insert new grades start year: '))
                new_grade[2] = int(input('*Insert new grades graduation year: '))
            case 5: # Return to main editor
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")
                continue
        
        frontend.new_record_preview(new_grade, 1)
        if input("*Save this grade edition? Y/N ").capitalize() == 'Y':
            backend.edit_grade_record(cur, grade_id, action, new_grade)
            conn.commit()
            status = 1
        frontend.edition_record_status(status, 1)
        break


def pupil_editor(cur, conn):
    while True:
        frontend.pupil_preeditor()
        match input('*Choose action to do: '):
            case '1': 
                searcher(cur)
                continue
            case '2':
                pass
            case '3':
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")
                continue
        
        id_edit = input('*Insert pupils ID for editioning: ')
        print()
        if id_edit.isdigit(): # Check ID in DB
            id_edit = int(id_edit)
            cur.execute(f'SELECT * FROM pupils WHERE pupil_id = {id_edit}').rowcount
        if len(cur.fetchall()) == 0:
            print(f'No such pupil with ID {id_edit} found. Try again or use search.')
            continue

        cur.execute(f'''SELECT pupil_id, first_name, last_name, 
            birthday, grade_name, graduation_year
            FROM pupils LEFT JOIN grades 
            ON grades.grade_id = pupils.grade_id
            WHERE pupil_id = {id_edit}''')
        frontend.dipslay_sheet(cur.fetchall(), 2)

        new_pupil = backend.get_pupil_line(cur, id_edit)

        frontend.pupil_editor_menu()
        status = 0
        action = input('*Choose which field to edit: ')
        if action.isdigit():
            action = int(action)
        print()

        match action:
            case 1: # Edit first name
                new_pupil[1] = input('*Insert new first name: ').title()
            case 2: # Edit last name
                new_pupil[2] = input('*Insert new last name: ').title()
            case 3: # Edit birthday
                new_pupil[3] = input('*Insert new date of birth: ')
            case 4: # Edit grade
                frontend.display_grades_sheet(cur)
                new_grade = input('*Insert new grade: ').upper()
                new_pupil[4] = new_grade
            case 5: # Edit all
                new_pupil[1] = input('*Insert new first name: ').title()
                new_pupil[2] = input('*Insert new last name: ').title()
                new_pupil[3] = input('*Insert new date of birth: ')
                frontend.display_grades_sheet(cur)
                new_grade = input('*Insert new grade: ').upper()
                new_pupil[4] = new_grade
            case 6: # Return to main editor
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")
                continue
        
        frontend.new_record_preview(new_pupil, 2)
        if not new_grade.isdigit():
            new_pupil[4] = backend.get_grade_id(cur, new_grade)
        if input("*Save this pupils edition? Y/N ").capitalize() == 'Y':
            backend.edit_pupil_record(cur, id_edit, action, new_pupil)
            conn.commit()
            status = 1
        frontend.edition_record_status(status, 2)
        break


def searcher(cur):
    while True:
        frontend.search_menu()
        action = input('*Choose action to do: ')
        if action.isdigit():
            action = int(action)
        print()

        match action:
            case 1:
                searching = input("*Enter first name to search: ").title()
            case 2:
                searching = input("*Enter last name to search: ").title()
            case 3:
                searching = input("*Enter birthday to search (MM/DD/YYYY): ")
            case 4:
                print('Please. Use display list of pupils by grade in Show database menu')
                break
            case 5: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")
                continue
        
        columns = ('first_name', 'last_name', 'birthday')
        cur.execute(f'''SELECT pupil_id, first_name, last_name, 
                    birthday, grade_name, graduation_year
                    FROM pupils LEFT JOIN grades 
                    ON grades.grade_id = pupils.grade_id
                    WHERE {columns[action - 1]} = "{searching}"''')
        query = cur.fetchall()
        frontend.dipslay_sheet(query, 2)
        save_query_csv(query)


def deleting(cur, conn):
    while True:
        frontend.deleting_menu()
        action = input('*Choose table where delete record: ')
        if action.isdigit():
            action = int(action)
        status = 0
        print()

        match action:
            case 1: # Edit grades
                frontend.display_grades_sheet(cur)
                grade = input('*Insert grade name from list above: ').upper()
                grade_id = backend.get_grade_id(cur, grade)
                cur.execute(f'''SELECT grade_name, start_year, graduation_year, 
                            first_name, last_name, birthday
                            FROM grades LEFT JOIN pupils 
                            ON grades.grade_id = pupils.grade_id
                            WHERE grade_name="{grade}"''')
                frontend.dipslay_sheet(cur.fetchall(), 4, grade)

                if input("*Delete this grade? Y/N ").capitalize() == 'Y':
                    if input("*Are you so sure you want to delete this grade forever? Y/N ").capitalize() == 'Y':
                        cur.execute(f'''DELETE FROM grades WHERE grade_id = {grade_id}''')
                        conn.commit()
                        status = 1
                frontend.delete_record_status(status, action)
            case 2: # Edit pupils
                delet_pupil(cur, conn)
            case 3: # Return to main
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")


def delet_pupil(cur, conn):
    while True:
        status = 0
        frontend.pupil_preeditor()
        match input('*Choose action to do: '):
            case '1': 
                searcher(cur)
                continue
            case '2':
                pass
            case '3':
                break
            case _: # Exception
                print("Wrong input. Try again!", end="\n\n")
                continue
        
        id_del = input('*Insert pupils ID for deleting: ')
        print()
        if id_del.isdigit(): # Check ID in DB
            id_del = int(id_del)
            cur.execute(f'SELECT * FROM pupils WHERE pupil_id = {id_del}').rowcount
        if len(cur.fetchall()) == 0:
            print(f'No such pupil with ID {id_del} found. Try again or use search.')
            continue
        
        cur.execute(f'''SELECT pupil_id, first_name, last_name, 
            birthday, grade_name, graduation_year
            FROM pupils LEFT JOIN grades 
            ON grades.grade_id = pupils.grade_id
            WHERE pupil_id = {id_del}''')
        frontend.dipslay_sheet(cur.fetchall(), 2)

        if input("*Delete this pupil? Y/N ").capitalize() == 'Y':
            if input("*Are you so sure you want to delete this pupil forever? Y/N ").capitalize() == 'Y':
                cur.execute(f'''DELETE FROM pupils WHERE pupil_id = {id_del}''')
                conn.commit()
                status = 1
        frontend.delete_record_status(status, 2)

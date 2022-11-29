import frontend
import backend

def save_query_csv(query):
    if input("*Save sheet to CSV file? Y/N ").capitalize() == 'Y':
        file_name = input("*Enter file name: ")
        if backend.save_file_csv(query, file_name):
            print("File seccessfully saved!")


def display_db(cur, conn):
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
            case 4: # Full database
                cur.execute('''SELECT grade_name, start_year, graduation_year, 
                            first_name, last_name, birthday
                            FROM grades LEFT JOIN pupils 
                            ON grades.grade_id = pupils.grade_id''')
                query = cur.fetchall()
                frontend.dipslay_sheet(query, action)
                save_query_csv(query)
            case 5: # Return to main
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
                grade = input('Insert new grade name: ')
                start = int(input('Insert start year: '))
                graduat = int(input('Insert graduation year: '))
                frontend.new_record_preview([grade, start, graduat], action)
                
                if input("*Save this grade? Y/N ").capitalize() == 'Y':
                    backend.new_record(cur, action, [backend.get_next_id(cur, action), grade, start, graduat])
                    conn.commit()
                    status = 1
                    frontend.new_record_status(status, action)
                else:
                    frontend.new_record_status(status, action)
            
            case 2: # Add to pupils
                first = input('Insert first name: ').title()
                last = input('Insert last name: ').title()
                birth = input('Insert date of birth: ')

                cur.execute('''SELECT grade_name, start_year, graduation_year 
                            FROM grades''')
                frontend.dipslay_sheet(cur.fetchall(), 1)

                grade = input('Insert grade name from list above: ').capitalize()
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









        # match action:
        #     case '1': # Pupils list
        #         pass
        #     case '2': # Grades list
        #         pass
        #     case '3': # Grades with pupils list
        #         pass
        #     case '4': # Full database
        #         pass
        #     case '5': # Return to main
        #         break
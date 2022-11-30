grades_head = ('Grade', 'Start year', 'Graduation year')
pupils_head = ('ID', 'First Name', 'Last Name', 'Birthday', 'Grade')
mixed_head = ('Grade', 'Start year', 'Graduation year', 'First Name', 'Last Name', 'Birthday')

# Menues
def main_menu():
    print('''Main menu. Aviable actions:\n
    1 - Show database
    2 - Add new record
    3 - Edit record
    4 - Delete record
    5 - Search pupil
    6 - Erase database
    7 - Close programm''')


def display_menu():
    print('''Show database. Aviable actions:\n
    1 - Display list of grades
    2 - Display list of pupils
    3 - Display list of grades with pupils
    4 - Display list of pupils by grade
    5 - Display full database list of grades and pupils
    6 - Return to main menu''')


def new_record_menu():
    print('''Add new record. Aviable tables:\n
    1 - Add to grades
    2 - Add to pupils
    3 - Return to main menu''')


def editor_menu():
    print('''Edit record. Aviable actions:\n
    1 - Edit grades records
    2 - Edit pupils records
    3 - Return to main menu''')


def grade_editor_menu():
    print('''Edit grades records. Aviable actions:\n
    1 - Edit grade name
    2 - Edit grade start year
    3 - Edit grade graduation year
    4 - Edit whole record
    5 - Return to main record editor''')


def pupil_preeditor():
    print('''To continue you need to know pupil's ID. Aviable actions:\n
    1 - Search pupil
    2 - Proceed
    3 - Return to main record editor''')    


def pupil_editor_menu():
    print('''Edit pupils records. Aviable actions:\n
    1 - Edit pupils first name
    2 - Edit pupils last name
    3 - Edit pupils birthday
    4 - Edit pupils grade
    5 - Edit whole record
    6 - Return to main record editor''')


def search_menu():
    print('''Search pupil. Aviable actions:\n
    1 - Search by first name
    2 - Search by last name
    3 - Search by birthday
    4 - Search by grade
    5 - Return''')    


def deleting_menu():
    print('''Delete record. Aviable actions:\n
    1 - Delete grades records
    2 - Delete pupils records
    3 - Return to main menu''')


# Console printing
def dipslay_sheet(query, layout, grade=''):
    match layout:
        case 1: # Grades sheet
            print("List of grades", end="\n\n")
            print("{:6} {:<12} {:<12}".format(*grades_head))
            for line in query:
                print("{:6} {:<12} {:<12}".format(*tuple(map(str,line))))
        case 2: # Pupils sheet
            print("List of pupils", end="\n\n")
            print("{:>4} {:15} {:15} {:11} {:10}".format(*pupils_head))
            for line in query:
                print("{:>4} {:15} {:15} {:11} {:10}".format(*tuple(map(str,line))))
        case 3: # Grades with pupils sheet
            print("List of grades with pupils", end="\n\n")
            print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*mixed_head))
            for line in query:
                print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*tuple(map(str,line))))
        case 4: # Pupils by grade sheet
            print(f"List of pupils in {grade}", end="\n\n")
            print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*mixed_head))
            for line in query:
                print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*tuple(map(str,line))))
        case 5: # Full database sheet
            print("List of grades with pupils", end="\n\n")
            print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*(mixed_head)))
            for line in query:
                print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*tuple(map(str,line))))


def new_record_preview(new_line, layout):
    match layout:
        case 1: # Grades sheet
            print("New grade", end="\n\n")
            print("{:6} {:<12} {:<12}".format(*grades_head))
            print("{:6} {:<12} {:<12}".format(*tuple(map(str,new_line))))
        case 2: # Pupils sheet
            print("New pupil", end="\n\n")
            print("{:>4} {:15} {:15} {:11} {:10}".format(*pupils_head))
            print("{:>4} {:15} {:15} {:11} {:10}".format(*tuple(map(str,new_line))))


def display_grades_sheet(cur):
    cur.execute('''SELECT grade_name, start_year, graduation_year 
                FROM grades''')
    dipslay_sheet(cur.fetchall(), 1)

# Statuses
def new_record_status(status, layout):
    if status == 1:
        print()        
        if layout == 1:
            print("New grade seccessfully created!", end="\n\n")
        elif layout == 2:
            print("New pupil seccessfully created!", end="\n\n")
    else:
        print()
        print("Creating new record aborted by user", end="\n\n")


def edition_record_status(status, layout):
    if status == 1:
        print()        
        if layout == 1:
            print("Grade record seccessfully edited!", end="\n\n")
        elif layout == 2:
            print("Pupil record seccessfully edited!", end="\n\n")
    else:
        print()
        print("Record edition aborted by user", end="\n\n")


def delete_record_status(status, layout):
    if status == 1:
        print()        
        if layout == 1:
            print("Grade record seccessfully deleted!", end="\n\n")
        elif layout == 2:
            print("Pupil record seccessfully deleted!", end="\n\n")
    else:
        print()
        print("Record deleting aborted by user", end="\n\n")
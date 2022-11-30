grades_head = ('Grade', 'Start year', 'Graduation year')
pupils_head = ('ID', 'First Name', 'Last Name', 'Birthday', 'Grade')
mixed_head = ('Grade', 'Start year', 'Graduation year', 'First Name', 'Last Name', 'Birthday')

def main_menu():
    print('''Main menu. Aviable actions:\n
    1 - Show database
    2 - Add new record
    3 - Edit record
    4 - Close programm''')

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



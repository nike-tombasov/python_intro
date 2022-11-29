# import pandas as pd
# import numpy as np


def main_menu():
    print('''Main menu. Aviable actions:\n
    1 - Show database
    2 - Make new record
    3 - Edit record
    4 - Close programm''')

def display_menu():
    print('''Show database. Aviable actions:\n
    1 - Display list of grades
    2 - Display list of pupils
    3 - Display list of grades with pupils
    4 - Display full database list of grades and pupils
    5 - Return to main menu''')


def new_record_menu():
    print('''Add new record. Aviable tables:\n
    1 - Add to grades
    2 - Add to pupils
    3 - Return to main menu''')


def dipslay_sheet(query, layout):
    if layout == 1: # Grades sheet
        print("List of grades", end="\n\n")
        print("{:6} {:<12} {:<12}".format(*('Grade', 'Start year', 'Graduation year')))
        for line in query:
            print("{:6} {:<12} {:<12}".format(*tuple(map(str,line))))
    elif layout == 2: # Pupils sheet
        print("List of pupils", end="\n\n")
        print("{:>4} {:15} {:15} {:11} {:10}".format(*('ID', 'First Name', 'Last Name', 'Birthday', 'Grade')))
        for line in query:
            print("{:>4} {:15} {:15} {:11} {:10}".format(*tuple(map(str,line))))
    elif layout == 3: # Grades with pupils sheet
        print("List of grades with pupils", end="\n\n")
        print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*('Grade', 'Start year', 'Graduation year', 'First Name', 'Last Name', 'Birthday')))
        for line in query:
            print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*tuple(map(str,line))))
    elif layout == 4: # Full database sheet
        print("List of grades with pupils", end="\n\n")
        print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*('Grade', 'Start year', 'Graduation year', 'First Name', 'Last Name', 'Birthday')))
        for line in query:
            print("{:6} {:<12} {:<16} {:15} {:15} {:11}".format(*tuple(map(str,line))))


def new_record_preview(new_line, layout):
    if layout == 1: # Grades sheet
        print("New grade", end="\n\n")
        print("{:6} {:<12} {:<12}".format(*('Grade', 'Start year', 'Graduation year')))
        print("{:6} {:<12} {:<12}".format(*tuple(map(str,new_line))))
    elif layout == 2: # Pupils sheet
        print("New pupil", end="\n\n")
        print("{:>4} {:15} {:15} {:11} {:10}".format(*('ID', 'First Name', 'Last Name', 'Birthday', 'Grade')))
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



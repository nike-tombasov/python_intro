def new_contact_save(data):
    with open('database.csv', 'a') as file:
        file.write(f'''{get_next_id()};{data[0].title()};{data[1].title()};{data[2].title()};{data[3].title()};{data[4].title()}\n''')


def import_data(import_file):
    with open(import_file, 'r') as file:
        lst = file.read().split('\n')
    for i in lst:
        if i != '':
            new_contact_save(i.split(";")[1:6])

def get_next_id():
    with open('database.csv', 'r') as file:
        temp = file.read().rsplit('\n', 2)
        last_record = temp[-2].split(';')
        return int(last_record[0]) + 1

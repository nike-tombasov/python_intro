def new_contact_save(new_line):
    with open('database.csv', 'a') as file:
        file.write(';'.join(new_line) + '\n')
    return new_line

def pre_new_line(data):
    new_line = [str(get_next_id()), data[0].title(), data[1].title(), data[2], data[3], data[4]]
    return new_line

def import_data(import_file):
    with open(import_file, 'r') as file:
        lst = file.read().split('\n')
    for i in lst:
        if i != '':
            new_contact_save(pre_new_line(i.split(";")[1:6]))


def get_next_id():
    with open('database.csv', 'r') as file:
        temp = file.read().rsplit('\n', 2)
        last_record = temp[-2].split(';')
        return int(last_record[0]) + 1

#import controller

def save_file_csv(query, file_name):
    with open(f'{file_name}.csv', 'w') as file:
        for i in query:
            file.write(';'.join(tuple(map(str,i))) + '\n')
    return True

def new_record(cur, table, values):
    if table == 1:
        cur.execute('INSERT INTO grades VALUES(?, ?, ?, ?);', values)
    elif table == 2:
        cur.execute('INSERT INTO pupils VALUES(?, ?, ?, ?, ?);', values)


# def new_prerecord(cur, table, *args):
#     next_id = get_next_id(cur, table)
#     values = [next_id, *args]
#     return values

def get_next_id(cur, table):
    if table == 1:
       cur.execute('SELECT grade_id FROM grades')
    elif table == 2:
        cur.execute('SELECT pupil_id FROM pupils')
    return cur.fetchall()[-1][0] + 1
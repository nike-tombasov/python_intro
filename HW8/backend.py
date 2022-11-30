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


def get_grade_id(cur, grade):
    cur.execute(f'SELECT grade_id FROM grades where grade_name="{grade}"')
    return cur.fetchone()[0]


def get_grade_line(cur, grade_id):
    cur.execute(f'''SELECT grade_name, start_year, graduation_year
                FROM grades WHERE grade_id = {grade_id}''')
    return list(cur.fetchone())


def get_pupil_line(cur, pupil_id):
    cur.execute(f'''SELECT pupil_id, first_name, last_name, birthday, grade_id
                FROM pupils WHERE pupil_id = {pupil_id}''')
    return list(cur.fetchone())


def edit_grade_record(cur, grade_id, action, new_grade):
    columns = ['grade_name', 'start_year', 'graduation_year']
    if action == 4:
        cur.execute(f'''UPDATE grades SET 
                    {columns[0]} = "{new_grade[0]}",
                    {columns[1]} = "{new_grade[1]}",
                    {columns[2]} = "{new_grade[2]}"
                    WHERE grade_id = {grade_id}''')
    else:
        cur.execute(f'''UPDATE grades SET {columns[action - 1]} = "{new_grade[action - 1]}"
                    WHERE grade_id = {grade_id}''')


def edit_pupil_record(cur, pupil_id, action, new_pupil):
    columns = ['pupil_id', 'first_name', 'last_name', 'birthday', 'grade_id']
    if action == 5:
        cur.execute(f'''UPDATE pupils SET 
                    {columns[1]} = "{new_pupil[1]}",
                    {columns[2]} = "{new_pupil[2]}",
                    {columns[3]} = "{new_pupil[3]}",
                    {columns[4]} = "{new_pupil[4]}"
                    WHERE pupil_id = {pupil_id}''')
    else:
        cur.execute(f'''UPDATE pupils SET {columns[action]} = "{new_pupil[action]}"
                    WHERE pupil_id = {pupil_id}''')


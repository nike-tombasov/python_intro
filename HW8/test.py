import  sqlite3


conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute('''SELECT grade_name, start_year, graduation_year 
            FROM grades''')
a = cur.fetchall()
print(a)

grade = input('*Insert grade name from list above: ').upper()

cur.execute(f'SELECT grade_id FROM grades where grade_name="{grade}"')
grade_id = cur.fetchone()[0]
print(grade)
print(grade_id)


cur.execute(f'''UPDATE''')
conn.commit()


cur.execute('''SELECT grade_name, start_year, graduation_year 
            FROM grades''')
a = cur.fetchall()
print(a)
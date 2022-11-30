import  sqlite3

def initialize_db():
    conn = sqlite3.connect('school.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS pupils(
        pupil_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birthday TEXT,
        grade_id TEXT);
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS grades(
        grade_id INT PRIMARY KEY,
        grade_name TEXT,
        start_year INT,
        graduation_year INT);
    ''')

    # cur.execute('''CREATE TABLE IF NOT EXISTS parents(
    #     parent_id INT PRIMARY KEY,
    #     first_name TEXT,
    #     last_name TEXT,
    #     birthday TEXT,
    #     parent_role_id INT,
    #     phone_number_id INT);
    # ''')
    # cur.execute('''CREATE TABLE IF NOT EXISTS phone_numbers(
    #     phone_number_id INT PRIMARY KEY,
    #     phone_number_1 TEXT,
    #     phone_number_2 TEXT,
    #     phone_number_3 TEXT,
    #     phone_number_4 TEXT,
    #     phone_number_5 TEXT);
    # ''')
    # cur.execute('''CREATE TABLE IF NOT EXISTS phone_numbers(
    #     parent_role_id INT PRIMARY KEY,
    #     role_type TEXT);
    # ''')

    conn.commit()

    pupils_insert = "INSERT INTO pupils VALUES(?, ?, ?, ?, ?);"
    grades_insert = "INSERT INTO grades VALUES(?, ?, ?, ?);"

    pupils_main = [
        ('0001', 'Tom', 'Ridle', '12/24/1985', '01'),
        ('0002', 'Michael', 'Jonhson', '05/06/1992', '02'),
        ('0003', 'Frank', 'Codd', '01/18/1986', '12'),
        ('0004', 'Mike', 'Torry', '02/11/1999', '01'),
        ('0005', 'Fred', 'De Zack', '', '01')
    ]

    grades_main = [
        ('01', '1A', '2020', '2031'),
        ('02', '1B', '2020', '2031'),
        ('03', '1C', '2020', '2031'),
        ('04', '2A', '2019', '2030'),
        ('05', '2B', '2019', '2030'),
        ('06', '2C', '2019', '2030'),
        ('07', '3A', '2018', '2029'),
        ('08', '3B', '2018', '2029'),
        ('09', '3C', '2018', '2029'),
        ('10', '4A', '2017', '2028'),
        ('11', '4B', '2017', '2028'),
        ('12', '4C', '2017', '2028'),
        ('13', '5A', '2016', '2027'),
        ('14', '5B', '2016', '2027'),
        ('15', '5C', '2016', '2027'),
    ]

    cur.executemany(pupils_insert, pupils_main)
    cur.executemany(grades_insert, grades_main)

    conn.commit()

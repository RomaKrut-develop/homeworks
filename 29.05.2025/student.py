import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
--begin-sql
CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,    
        name TEXT,
        age INTEGER,
        major TEXT
)
--end-sql
''')

cursor.execute('''
--begin-sql
CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,    
        student_id INTEGER, FOREIGN KEY REFERENCES,
        students id,
        grade INTEGER
)
--end-sql
''')

def add_student(name, age, major):
    try:
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)',
                       (name, age, major))
        conn.commit()
    except sqlite3.IntegrityError:
        print('Lol, exists')

def give_grade(student_id, students, grade):
    try:
        cursor.execute('SELECT FROM students(name, age, major) VALUES (?, ?, ?)',
                       (name, age, major))
        conn.commit()
    except sqlite3.IntegrityError:
        print('Lol, exists')
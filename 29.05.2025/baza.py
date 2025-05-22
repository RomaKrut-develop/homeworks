import sqlite3

def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        grade INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
    ''')
    
    # 3. Добавление данных
    # Вставка студентов
    students_data = [
        ('John Smith', 20, 'IT'),
        ('Bill Gates', 21, 'Math'),
        ('Paul Allen', 19, 'Phycics'),
        ('Kristopher Alexander', 22, 'IT'),
        ('Pavel Durov', 20, 'Math')
    ]
    
    cursor.executemany('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', students_data)
    
    # Вставка оценок
    grades_data = [
        (1, 'Programming', 5),
        (1, 'Data base', 4),
        (2, 'Math analyze', 5),
        (2, 'Math', 5),
        (3, 'Mechanics', 4),
        (3, 'Dynamics', 3),
        (4, 'Programming', 5),
        (4, 'Algorythms', 4),
        (5, 'Possibility', 5),
        (5, 'Disckrets Mathics', 4)
    ]
    
    cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades_data)
    
    # Сохранение изменений
    conn.commit()
    
    print("All students and middle grade:")
    cursor.execute('''
    SELECT s.name, s.major, AVG(g.grade) as avg_grade
    FROM students s
    LEFT JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ''')
    for row in cursor.fetchall():
        print(f"Student: {row[0]}, Job: {row[1]}, middle grade: {row[2]:.2f}")
    
    print("\nStudents with middle grade bigger than 4:")
    cursor.execute('''
    SELECT s.name, s.major, AVG(g.grade) as avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    HAVING avg_grade > 4
    ''')
    for row in cursor.fetchall():
        print(f"Student: {row[0]}, Job: {row[1]}, Middle grade: {row[2]:.2f}")
    
    print("\nAmounts of students by job:")
    cursor.execute('''
    SELECT major, COUNT(*) as count
    FROM students
    GROUP BY major
    ''')
    for row in cursor.fetchall():
        print(f"Job: {row[0]}, students: {row[1]}")
    
    conn.close()

if __name__ == "__main__":
    create_database()
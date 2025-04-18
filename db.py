import sqlite3
def create_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        roll_number TEXT NOT NULL,
        exam_roll TEXT NOT NULL,
        registration_number TEXT NOT NULL,
        batch TEXT NOT NULL,
        session TEXT NOT NULL,
        blood_group TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
create_db()

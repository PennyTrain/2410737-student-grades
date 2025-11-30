import sqlite3
import atexit

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()
atexit.register(conn.close)

def query(selected): 
    query = f"SELECT {selected} FROM student"
    c.execute(query)
    results = c.fetchall()
    data = [row[0] for row in results]
    values = remove_duplicates(data)
    return values

def remove_duplicates(values):
    """Return a list with duplicates removed (order not guaranteed)."""
    return list(set(values))

ages = query('age')
grades = query('grade')
attendance = query('attendance')



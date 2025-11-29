import sqlite3
import atexit

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

atexit.register(conn.close)

def avg_grade():
    c.execute("SELECT AVG(grade) FROM student")
    result = c.fetchone()
    average = result[0]
    return average

def avg_attendance():
    c.execute("SELECT AVG(attendance) FROM student")
    result = c.fetchone()
    average = result[0]
    return average

print(avg_grade())
print(avg_attendance())
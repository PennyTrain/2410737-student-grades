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

def _count_by_condition(condition):
    c.execute(f"SELECT COUNT(*) FROM student WHERE {condition};")
    return c.fetchone()[0]

def num_passed():
    return _count_by_condition("grade >= 40")

def num_failed():
    return _count_by_condition("grade < 40")

def num_grades():
    """Return a dictionary of grade counts."""
    c.execute("""
        SELECT
            SUM(CASE WHEN grade >= 70 THEN 1 ELSE 0 END) AS A_count,
            SUM(CASE WHEN grade >= 60 AND grade < 70 THEN 1 ELSE 0 END) AS B_count,
            SUM(CASE WHEN grade >= 50 AND grade < 60 THEN 1 ELSE 0 END) AS C_count
        FROM student;
    """)
    row = c.fetchone() or (0, 0, 0)
    A_count, B_count, C_count = row
    return {"A": A_count, "B": B_count, "C": C_count}

print(avg_grade())
print(avg_attendance())
print(num_grades())
print(num_passed())
print(num_failed())
import sqlite3
import atexit

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

atexit.register(conn.close)

def avg_grade():
    return get_avg('grade')

def avg_attendance():
    return get_avg('attendance')

def get_avg(condition):   
    try:
        c.execute(f"SELECT AVG({condition}) FROM student")
        result = c.fetchone()
        if result and result[0] is not None:
            average = result[0]
            return average
        else:
            return ("No attendance found in the database")
    except Exception as e:
        return (f"Error fetching average attendance: {e}")

def _count_by_condition(condition):
    c.execute(f"SELECT COUNT(*) FROM student WHERE {condition};")
    return c.fetchone()[0]

def num_passed():
    return _count_by_condition("grade >= 40")

def num_failed():
    return _count_by_condition("grade < 40") #move to constants, no number hard codes

def num_grades():
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

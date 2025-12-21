import sqlite3
import atexit

conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()

atexit.register(conn.close)

grade_condition = 40

def avg_grade():
    return get_avg('grade')

def avg_attendance():
    return get_avg('attendance')

def get_avg(condition):   
    # condition = to any database column that could be averaged. so only integers
    # or floats!
    try:
        c.execute(f"SELECT AVG({condition}) FROM student")
        result = c.fetchone()
        if result and result[0] is not None:
            average = result[0]
            return round(average, 2)
        else:
            return ("No attendance found in the database")
    except Exception as e:
        return (f"Error fetching average attendance: {e}")

def count_by_condition(condition):
    c.execute(f"SELECT COUNT(*) FROM student WHERE {condition};")
    return c.fetchone()[0]

def num_passed():
    return count_by_condition(f"grade >= {grade_condition}")

def num_failed():
    return count_by_condition(f"grade < {grade_condition}")

def num_grades():
    c.execute("""
        SELECT
            SUM(CASE WHEN grade >= 70 THEN 1 ELSE 0 END) AS A,
            SUM(CASE WHEN grade >= 60 AND grade < 70 THEN 1 ELSE 0 END) AS B,
            SUM(CASE WHEN grade >= 50 AND grade < 60 THEN 1 ELSE 0 END) AS C
        FROM student;
    """)
    row = c.fetchone() or (0, 0, 0)

    grades = {"A": row[0], "B": row[1], "C": row[2]}
    return (
        f"Grade A: {grades['A']}\n"
        f"Grade B: {grades['B']}\n"
        f"Grade C: {grades['C']}"
    )

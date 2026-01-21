import sqlite3
from database import c

grade_condition = 40


def avg_grade():
    return get_avg('grade')


def avg_attendance():
    return get_avg('attendance')


def get_avg(condition):
    # condition = to any numeric database column
    # that could be averaged. so only integers
    # or floats!
    if c is None:
        return "Database not connected"

    try:
        c.execute(f"SELECT AVG({condition}) FROM student")
        result = c.fetchone()

        if result and result[0] is not None:
            return round(result[0], 2)
        else:
            return f"No {condition} data found in the database"

    except Exception as e:
        return f"Error fetching average {condition}: {e}"


def count_by_condition(condition):
    if c is None:
        return "Database not connected"
    try:
        c.execute(f"SELECT COUNT(*) FROM student WHERE {condition}")
        result = c.fetchone()

        if result:
            return result[0]
        else:
            return 0

    except Exception as e:
        return f"Error getting data from database: {e}"


def num_passed():
    return count_by_condition(f"grade >= {grade_condition}")


def num_failed():
    return count_by_condition(f"grade < {grade_condition}")


def num_grades():
    if c is None:
        return "Database not connected"

    try:
        c.execute("""
    SELECT
        SUM(
            CASE
                WHEN grade >= 70 THEN 1
                ELSE 0
            END
        ) AS A,
        SUM(
            CASE
                WHEN grade >= 60
                     AND grade < 70 THEN 1
                ELSE 0
            END
        ) AS B,
        SUM(
            CASE
                WHEN grade >= 50
                     AND grade < 60 THEN 1
                ELSE 0
            END
        ) AS C
    FROM student
""")

        row = c.fetchone()

        if row:
            grades = {
                "A": row[0] or 0,
                "B": row[1] or 0,
                "C": row[2] or 0
            }

            return (
                f"\nGrade A: {grades['A']}\n"
                f"Grade B: {grades['B']}\n"
                f"Grade C: {grades['C']}"
            )
        else:
            return "No grade data found"

    except sqlite3.Error as e:
        return f"SQL error while counting grades: {e}"

    except Exception as e:
        return f"Unexpected error: {e}"

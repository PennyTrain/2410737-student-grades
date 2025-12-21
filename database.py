# https://docs.python.org/3/library/csv.html
import csv
import sqlite3

def create_database():
    conn = sqlite3.connect('student-data/student_grades.db')
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student';")
    table_exists = c.fetchone()
# https://www.geeksforgeeks.org/python/how-to-import-a-csv-file-into-a-sqlite-database-table-using-python/
# https://www.geeksforgeeks.org/sqlite/import-a-csv-file-into-an-sqlite-table/
# how I am doing this ^^ I learnt from here
# """"""/'''''' = docstring, to do multiple things on multiple lines
# datatype = text/integrer/boolean/float there are more

    if not table_exists:
        create_table = '''CREATE TABLE student \
                        ( \
                            student_id           INTEGER PRIMARY KEY AUTOINCREMENT, \
                            first_name           TEXT    NOT NULL, \
                            last_name            TEXT    NOT NUll, \
                            age                  INTEGER NOT NULL, \
                            email                TEXT    NOT NULL UNIQUE, \
                            country              TEXT    NOT NULL, \
                            attendance           FLOAT   NOT NULL, \
                            assignment_completed BOOLEAN NOT NULL DEFAULT 0, \
                            grade                FLOAT   NOT NULL \
                        ); \
                    '''
        c.execute(create_table)

# this was to keep track and ensure the database was not duplicated everytime the code was ran
#     print("table created")
# else:
#     print("table here")

# SQLite does not have a dedicated BOOLEAN data type. Instead, it treats BOOLEAN as an alias for INTEGER.
# I kept it as an integer as I want to be able to easily do numeric comparisons. Instead of making it TEXT NOT NULL, 
# I figured this is best
# Also used email address as the unique identifier to avoid duplicating data

    with open('student-data/student_grades.csv') as file:
        contents = csv.reader(file)
        next(contents)
        cleaned_data = []
        for row in contents:
            cleaned_data.append(row[1:])

# ignoring it if it already exists
    insert_info = "INSERT OR IGNORE INTO student(first_name, last_name, age, email, country, attendance, assignment_completed, grade) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"

# cleaning the data is taking out the booleans and replacing all the 
# true values with 1, and false values with 0
    c.executemany(insert_info, cleaned_data)

    select_all = "SELECT * FROM student"
    rows = c.execute(select_all).fetchall()

# This was to check it was working and print the database to terminal
# for r in rows:
#     print(r)

    conn.commit()
    conn.close()


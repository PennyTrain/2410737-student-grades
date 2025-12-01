import sqlite3
import pandas as pd
import os

# Connect to SQLite database
conn = sqlite3.connect(r"./student-data/student_grades.db")

# Load CSV data into Pandas DataFrame
stud_data = pd.read_csv('student-data/student_grades.csv')
# Write the data to a sqlite table
stud_data.to_sql('student', conn, if_exists='replace', index=False)

# Create a cursor object
cur = conn.cursor()
# Fetch and display result
for row in cur.execute('SELECT * FROM student'):
    print(row)
# Close connection to SQLite database
conn.close()

# I did find this way to do it, but only after I figured out the other way
# and I worked so hard on the above that I want to keep it

# 🐼 Approach 1: Pandas + to_sql

# Pros:
# It’s fast, simple, and only takes a few lines of code.
# Pandas guesses the schema for me.
# It fits naturally into analysis workflows where I clean or transform data first.
# Cons:
# I lose control over the exact schema — types, constraints, and keys.
# No automatic UNIQUE or NOT NULL rules.
# It can be slower for huge datasets.
# It adds a Pandas dependency.

# 📜 Approach 2: Raw CSV + sqlite3

# Pros:
# I define the schema exactly how I want, including constraints and keys.
# I can preprocess values however I need.
# It’s better for production because it enforces data integrity.
# No external libraries required.
# Cons:
# It’s more verbose and takes longer to write.
# I have to maintain the schema manually.
# It’s easier to introduce errors.
# ⚖️ When I use each

# I reach for Pandas when I want quick prototyping or simple workflows.
# I use raw sqlite3 when I need a strict, well-defined schema or I’m building something production-ready.

# this clears the terminal to make it ready for new content
# https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

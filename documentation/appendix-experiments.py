import sqlite3
import pandas as pd

# # Connect to SQLite database
# conn = sqlite3.connect(r"./student-data/student_grades.db")

# # Load CSV data into Pandas DataFrame
# stud_data = pd.read_csv('student-data/student_grades.csv')
# # Write the data to a sqlite table
# stud_data.to_sql('student', conn, if_exists='replace', index=False)

# # Create a cursor object
# cur = conn.cursor()
# # Fetch and display result
# for row in cur.execute('SELECT * FROM student'):
#     print(row)
# # Close connection to SQLite database
# conn.close()


# AND IN CLASS TEACHING
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    '''
)

conn.commit()

cursor.execute(
    '''
    INSERT INTO students(name, age, email)
    VALUES (?,?,?)
    ''',
    ("slaa", 20, "slaa@omg.com")
)

conn.commit()
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









# WEB SCRAPING

import requests
from bs4 import BeautifulSoup

# path_to_scrape = requests.get("https://quotes.toscrape.com/")

# soup = BeautifulSoup(path_to_scrape.text, "html.parser")

# # for link in soup.find_all("a"):
# #     print(link.get("href"), "-", link.text)

# quotes = soup.find_all("span", attrs={"class": "text"})
# authors = soup.find_all("small", attrs={"class": "author"})
# # print(authors, quotes)

# for quotes, authors in zip(quotes, authors):
#     print(quotes.text + " - " + authors.text)


path_to_scrape = requests.get("https://rholden-bs-dev.chi.ac.uk/scraping/demoscrapingpage.php")

soup = BeautifulSoup(path_to_scrape.text, "html.parser")

# for link in soup.find_all("a"):
#     print(link.get("href"), "-", link.text)

money = soup.find_all("p", attrs={"class": "price"})
print(money)
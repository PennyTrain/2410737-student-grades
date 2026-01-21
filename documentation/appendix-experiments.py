###############################################################################
# APPENDIX: EXPERIMENTAL CODE & EXPLORATION
# Purpose: Demonstrates experimentation with databases, web scraping,
#          testing, logging, and debugging concepts used during analysis.
# All code in this appendix is COMMENTED OUT by design.
###############################################################################


###############################################################################
# SECTION 1: SQLITE + PANDAS (CSV → DATABASE)
###############################################################################

# import sqlite3
# import pandas as pd

# # Connect to SQLite database (creates file if it doesn't exist)
# conn = sqlite3.connect(r"./student-data/student_grades.db")

# # Load CSV data into a Pandas DataFrame
# stud_data = pd.read_csv('student-data/student_grades.csv')

# # Write DataFrame to SQLite table
# stud_data.to_sql(
#     'student',
#     conn,
#     if_exists='replace',
#     index=False
# )

# # Create cursor to query the database
# cur = conn.cursor()

# # Fetch and display all rows from the table
# for row in cur.execute('SELECT * FROM student'):
#     print(row)

# # Close the database connection
# conn.close()



###############################################################################
# SECTION 2: SQLITE (IN-CLASS TEACHING EXAMPLE)
###############################################################################

# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()

# # Create table with explicit schema and constraints
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         email TEXT UNIQUE NOT NULL
#     );
#     '''
# )

# conn.commit()

# # Insert a sample student record
# cursor.execute(
#     '''
#     INSERT INTO students(name, age, email)
#     VALUES (?, ?, ?)
#     ''',
#     ("slaa", 20, "slaa@omg.com")
# )

# conn.commit()
# conn.close()



###############################################################################
# SECTION 3: COMPARISON OF DATABASE APPROACHES
###############################################################################

# I discovered this alternative approach after completing the first method.
# I chose to keep both to demonstrate learning progression.

# 🐼 Approach 1: Pandas + to_sql
#
# Pros:
# - Fast and concise
# - Automatically infers schema
# - Ideal for exploratory data analysis
#
# Cons:
# - Less control over schema constraints
# - No automatic UNIQUE or NOT NULL enforcement
# - Slower with very large datasets
# - Requires Pandas dependency


# 📜 Approach 2: Raw CSV + sqlite3
#
# Pros:
# - Full control over schema and constraints
# - Better for production-level systems
# - No external libraries required
#
# Cons:
# - More verbose
# - Schema must be maintained manually
# - Higher chance of human error


# ⚖️ Usage Decision
#
# - Pandas is used for rapid prototyping and analysis.
# - Raw sqlite3 is used for strict schemas and production-ready systems.



###############################################################################
# SECTION 4: WEB SCRAPING EXPERIMENTS
###############################################################################

# import requests
# from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Example 1: Quotes to Scrape (commented exploration)
# ---------------------------------------------------------------------------

# response = requests.get("https://quotes.toscrape.com/")
# soup = BeautifulSoup(response.text, "html.parser")

# quotes = soup.find_all("span", class_="text")
# authors = soup.find_all("small", class_="author")

# for quote, author in zip(quotes, authors):
#     print(f"{quote.text} - {author.text}")


# ---------------------------------------------------------------------------
# Example 2: Demo Scraping Page
# ---------------------------------------------------------------------------

# response = requests.get(
#     "https://rholden-bs-dev.chi.ac.uk/scraping/demoscrapingpage.php"
# )

# soup = BeautifulSoup(response.text, "html.parser")

# prices = soup.find_all("p", class_="price")

# for price in prices:
#     print(price.text)



###############################################################################
# SECTION 5: LOGGING (DEBUGGING & TEST SUPPORT)
###############################################################################

# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     filename='log.txt',
#     filemode='w',
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# logging.debug("Debug message")
# logging.info("Informational message")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical failure message")

# Although I explored Python’s logging module earlier, I deliberately
# chose NOT to use logging in this appendix or final implementation.

# Reason:
# logging code in a final codebase, as this can reduce readability and
# maintainability.

# Instead, logging was used during development and debugging phases
# and removed once the program logic was verified.

# This reflects a real-world development workflow:
# - Logging is useful during testing and debugging
# - Clean code should not retain unnecessary commented-out logging



###############################################################################
# SECTION 6: DEBUGGING & UNIT-TEST STYLE LOGIC
###############################################################################

# The following code was used to practice debugging logic.
# It calculates an average score and assigns grades.

# def calculate_average(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total / len(numbers)


# def categorize_score(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "F"


# def process_scores(scores):
#     average = calculate_average(scores)
#     results = []

#     for score in scores:
#         grade = categorize_score(score)
#         results.append((score, grade))

#     return average, results


# if __name__ == "__main__":
#     scores = [95, 82, 67, 58, 76]

#     avg, graded_scores = process_scores(scores)

#     print(f"Average score: {avg}")
#     for score, grade in graded_scores:
#         print(f"Score: {score}, Grade: {grade}")

###############################################################################
# END OF APPENDIX
###############################################################################

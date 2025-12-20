import unittest
import sys
# Programs that import and use 'os' stand a better chance of being
# portable between different platforms. Of course, they must then
# only use functions that are defined by all platforms (e.g., unlink
# and opendir), and leave all pathname manipulation to os.path
import os
import sqlite3

#https://python-basics-tutorial.readthedocs.io/en/24.3.0/test/sqlite.html
conn = sqlite3.connect("student-data/student_grades.db")
c = conn.cursor()
# python can now see the parent folder (where corecalc lives)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import database

class TestCreateDB(unittest.TestCase):
        def test_db_exists(self):
                # assert, so true table exists, and if not 
                # true it testcase will fail
                # Here I only test the path, i do not 
                # test the contents of the database
                assert os.path.exists("database.py")

        def test_table_exists(self):
                # this created table again
                # here I test that it has columns with names, and 
                # if it does not i create one therefore causing a fail
                with self.assertRaises(sqlite3.OperationalError): 
                        database.c.execute("'''CREATE TABLE student \
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
                   '''")
                           
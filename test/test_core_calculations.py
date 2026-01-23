import unittest
from database import c
import sqlite3
import core_calculations


class TestSQLQueries(unittest.TestCase):
    def test_select_all_from_database(self):
        c.execute("""
                SELECT student_id, first_name, last_name, age, email,
                        country, attendance, assignment_completed, grade
                FROM student
                ORDER BY student_id
                LIMIT 5;
                """)
        result = c.fetchall()

        expected = [
                    (
                        1,
                        'Rebeca',
                        'Maryon',
                        20,
                        'rmaryon0@networkadvertising.org',
                        'Slovenia',
                        65.24,
                        'true',
                        96.93
                        ),
                    (
                        2,
                        'Gerry',
                        'Madsen',
                        24,
                        'gmadsen1@msn.com',
                        'Poland',
                        60.43,
                        'true',
                        90.39
                        ),
                    (
                        3,
                        'Wanids',
                        'Uridge',
                        25,
                        'wuridge2@nature.com',
                        'France',
                        81.96,
                        'true',
                        90.57
                        ),
                    (
                        4,
                        'Bailie',
                        'Huffy',
                        25,
                        'bhuffy3@irs.gov',
                        'France',
                        21.67,
                        'true',
                        99.41
                        ),
                    (
                        5,
                        'Renata',
                        'Broadnicke',
                        18,
                        'rbroadnicke4@princeton.edu',
                        'Indonesia',
                        1.42,
                        'false',
                        39.72),
                ]

        self.assertEqual(result, expected)


    def test_num_passed(self):
        # create an in-memory test database
        conn = sqlite3.connect(":memory:")
        c = conn.cursor()

        # create a table that matches your real schema
        c.execute("CREATE TABLE student (grade REAL)")
        c.execute("INSERT INTO student (grade) VALUES (25), (50), (70)")

        # inject the test cursor into your module
        core_calculations.c = c

        # run the function as-is
        assert core_calculations.num_passed() == 2



    def test_num_failed(self):
        conn = sqlite3.connect(":memory:")
        c = conn.cursor()
        c.execute("CREATE TABLE student (grade REAL)")
        c.execute("INSERT INTO student (grade) VALUES (25), (50), (70)")

        core_calculations.c = c  # inject cursor

        assert core_calculations.num_failed() == 1

        
    def test_avg_grade(self):
        conn = sqlite3.connect(":memory:")
        c = conn.cursor()
        c.execute("CREATE TABLE student (grade REAL, attendance REAL)")
        c.execute("INSERT INTO student (grade, attendance) VALUES (40, 80), (60, 90)")

        core_calculations.c = c

        assert core_calculations.avg_grade() == 50.0



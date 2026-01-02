import unittest
import sys
import os
import sqlite3
from database import c

# python can now see the parent folder (where corecalc lives)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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

import database
import visuals
import unittest
import sys


def main():
    database.create_database()
    suite = unittest.defaultTestLoader.discover("test")
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if not result.wasSuccessful():
        print("Tests failed now the app will not launch.")
        sys.exit(1)
    try:
        visuals.app()
    finally:
        database.close_connection()
        print("connection closed")


if __name__ == "__main__":
    main()

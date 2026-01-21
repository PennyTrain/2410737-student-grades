import database
import visuals
import unittest
import sys


def main():
    database.create_database()
    suite = unittest.defaultTestLoader.discover("test")
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if not result.wasSuccessful():
        # app cannot run, open tkinter window with error
        sys.exit(1)
    try:
        visuals.app()
    finally:
        database.close_connection()


if __name__ == "__main__":
    main()

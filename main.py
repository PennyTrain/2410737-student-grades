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
    visuals.app()


if __name__ == "__main__":
    main()
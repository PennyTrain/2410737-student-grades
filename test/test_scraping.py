import unittest
from scraping import web_scraped


class TestWebScraped(unittest.TestCase):

    def test_web_scraped_returns_contact_info(self):
        result = web_scraped()
        # Check that something is returned
        self.assertIsNotNone(result)
        # Check expected content exists
        self.assertIn("CONTACT US", result)


if __name__ == "__main__":
    unittest.main()

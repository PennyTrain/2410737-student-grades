import unittest
from weatherapi import get_weather

class TestGetWeather(unittest.TestCase):

    def test_get_weather_returns_data(self):
        result = get_weather()

        self.assertIsNotNone(result)
        self.assertIn("Weather:", result)
        self.assertIn("Temperature:", result)
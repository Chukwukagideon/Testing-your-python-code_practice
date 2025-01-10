import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
    """Test for city_functions.py"""
    def test_city_country(self):
        """Do names like Santiago, Chile? """
        formatted_name = get_city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

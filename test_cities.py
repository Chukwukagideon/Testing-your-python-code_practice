import unittest
from city_functions import get_city_country


class CitiesTestCase(unittest.TestCase):
    """Test for city_functions.py"""
    def test_city_country(self):
        """Do names like Santiago, Chile work? """
        formatted_name = get_city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_population(self):
        """Will parameters like Santiago, Chile and population-500000 work?"""
        formatted_name = get_city_country("santiago", "chile", "population-500000")
        self.assertEqual(formatted_name, "Santiago, Chile - Population-500000.")

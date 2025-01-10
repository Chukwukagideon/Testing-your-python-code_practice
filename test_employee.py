import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the employee class"""

    def setUp(self):
        self.my_employee = Employee("John", "Doe", 40000)
        self.my_employee.give_raise()

    def test_give_default_raise(self):
        """Test if the default raise amount works"""
        self.assertEqual(self.my_employee.annual_salary, 45000)


if __name__ == "__main__":
    unittest.main()

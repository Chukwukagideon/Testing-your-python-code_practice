import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the employee class"""

    def setUp(self):
        self.my_employee = Employee("John", "Doe", 40000)
        self.my_employee.give_raise()

        self.my_employee2 = Employee("John", "Doe", 40000)
        self.my_employee2.give_raise(6000)

    def test_give_default_raise(self):
        """Test if the default raise amount works"""
        self.assertEqual(self.my_employee.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Test if giving a custom raise works"""
        self.assertEqual(self.my_employee2.annual_salary, 46000)


if __name__ == "__main__":
    unittest.main()

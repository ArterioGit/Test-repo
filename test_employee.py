import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee("Alessandro", "Bigucci")
        emp_2 = Employee("Emanuela", "Bellone")

        self.assertEqual(emp_1.email, "Alessandro.Bigucci@gmail.com")
        self.assertEqual(emp_2.email, "Emanuela.Bellone@gmail.com")


if __name__ == "__main__":
    unittest.main()

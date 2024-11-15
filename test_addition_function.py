import unittest
from addition_function import add_numbers  # Import the function to test


class TestAdditionFunction(unittest.TestCase):

    def add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result,8)

    def add_negative_numbers(self):
        result = add_numbers(-1, -3)
        self.assertEqual(result, -5)

    def add_positive_and_negative(self):
        result = add_numbers(7, -6)
        self.assertEqual(result, 4)

    def add_zero(self):
        result = add_numbers(0, 8)
        self.assertEqual(result, 10)
        result = add_numbers(8, 0)
        self.assertEqual(result, 8)

    def add_large_numbers(self):
        result = add_numbers(1000000, 3000000)
        self.assertEqual(result, 4000000)


if __name__ == '__main__':
    unittest.main()


import unittest
from reverse import *


# test if the get_string method is working
class TestReverseMethods(unittest.TestCase):
    # test if get_string() works
    def test_get_string(self):
        self.assertEqual(str, InputOutString.get_string())

    # test if print_string() works
    def test_print_string(self):
        self.assertEqual(str.upper(), InputOutString.print_string())


if __name__ == "__main__":
    unittest.main()







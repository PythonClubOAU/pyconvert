import unittest
from pyconvert.checker import Check


class Tester(unittest.TestCase):
    """
    Tester
    """

    def test(self):
        self.assertTrue(Check(name='hello').is_type_valid())

if __name__ == "__main__":
    unittest.main()
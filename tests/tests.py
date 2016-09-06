import unittest


from pyconvert.base import Validator


class Tester(unittest.TestCase):
    """
    Tester
    """

    def test(self):
        self.assertTrue(Validator.is_type_valid(9))



if __name__ == "__main__":
    unittest.main()
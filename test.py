import unittest

from main import check_for_sum

class Test(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_for_sum([1, 3, -1, 5, -4], 2))

    def test_simple_2(self):
        self.assertFalse(check_for_sum([1, 3, -1, 5, -4], 3))

    def test_simple_3(self):
        self.assertFalse(check_for_sum([1], 3))

    def test_simple_4(self):
        self.assertFalse(check_for_sum([], 3))

    def test_simple_5(self):
        self.assertTrue(check_for_sum([10, 2, 3, 3424, 3, 456, -1, 23, -324, 23, 22, -12, 2], 22))

    def test_simple_6(self):
        self.assertTrue(check_for_sum([3, 3, 3, 3, 3, 3, 3, 3, 3], 6))

    def test_simple_7(self):
        self.assertTrue(check_for_sum([3, 3, 3, 3, 3, 3, 3, 3, -4], -1))

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from more_fun_with_collections import assign_average

class TestSet(unittest.TestCase):
    def test_for_key_A(self):
        self.assertEquals(assign_average.switch_average('A'), 5)

    def test_for_key_B(self):
        self.assertEquals(assign_average.switch_average('B'), 10)

    def test_for_key_C(self):
        self.assertEquals(assign_average.switch_average('C'), 15)

    def test_for_key_D(self):
        self.assertEquals(assign_average.switch_average('D'), 20)

    def test_for_key_E(self):
        self.assertEquals(assign_average.switch_average('E'), 25)

    def test_for_no_key(self):
        self.assertRaises(assign_average.switch_average(), ValueError)


if __name__ == '__main__':
    unittest.main()

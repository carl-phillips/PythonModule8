import unittest
from unittest.mock import patch
from more_fun_with_collections import dict_membership

class TestSet(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dict_membership.in_dict({'A':5, 'B':10}))

    def test_in_dict_false(self):
        self.assertFalse(dict_membership.in_dict({}))


if __name__ == '__main__':
    unittest.main()

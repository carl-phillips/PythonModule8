import unittest
from unittest.mock import patch
import datetime
from more_fun_with_collections import half_birthday

class TestSet(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2019, 4, 19)
        my_half_birthday = datetime.datetime(2019, 10, 18, 12)
        self.assertEquals(half_birthday.half_birthday(birthday), my_half_birthday)


if __name__ == '__main__':
    unittest.main()

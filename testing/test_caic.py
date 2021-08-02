# unittest +HTMLTestrunner
import sys

print(sys.path)
import unittest
from python.caic import Calc


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(11, 2)
        self.assertEqual(13, result)
        print(result)


if __name__ == '__main__':
    unittest.main()

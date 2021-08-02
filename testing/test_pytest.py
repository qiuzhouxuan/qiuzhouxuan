import pytest

from python.caic import Calc


class TestCalc:
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result


if __name__ == '__main__':
    pytest.main()

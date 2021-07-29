import pytest


def testa():
    print("testaaa")


class TestDemo():
    def test01(self):
        print("开始执行 test01 方法")
        x = "this"
        assert "h" in x

    def test02(self):
        print(print("开始执行 test02 方法"))
        x = "hello"
        assert "e" in x

    def test03(self):
        print(print("开始执行 test03 方法"))
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main("-v -x TestDemo")
    pytest.main(["-v", "-x", "TestDemo"])
    pytest.main(["-vs", "-rerun=2", "--html=邱邱.html", "--capture=sys"])

import pytest


# 指定执行某一接口,将需要该接口执行的函数名放到下一个函数的传参中

def test_login():
    print('登录方法')


def test_case1(test_login):
    print("01需要登录")


def test_case2():
    print("02不需要登录")


def test_case3(test_login):
    print("03需要登录")


if __name__ == '__main__':
    pytest.main()

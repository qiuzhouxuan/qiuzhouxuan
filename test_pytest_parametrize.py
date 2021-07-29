import pytest


@pytest.mark.parametrize("test_input,expect", [("3+5", 8), ("2+5", 7), ("7+5", 12)])
# 参数化  前两个变量，后面是对应的数据；
# 3+5->test_input    8->expected
def test_eva(test_input, expect):
    # eval ：将字符串str当成有效表达式来求值，并返回结果
    assert eval(test_input) == expect


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x:{x},y:{y}")


# 方法名作为参数
test_user_data = ["Tome", "Jerry"]


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登陆。登录用户：{user}")
    return user


# indirect = True,可以把传过来的参数当函数执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试硬了中login的返回值：{a}")
    assert a != ""

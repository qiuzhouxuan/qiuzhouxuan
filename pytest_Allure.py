# 完美测试报告ALLURE执行命令,执行PY文件生成文件指定到文件目录：
# pytest pytest_Allure.py --alluredir=./allure
# 生成报告（使用刚刚生成的文件生成测试报告：直接出现网页跳转html，本地作为监控）
# allure serve ./allure
# 生成测试报告文件到指定目录：allure generate ./pytest-demo2 -o ./fca/ --clean
# 打开指定目录下生成的allure报告（需要指定IP和端口进行监听）：allure open -h 127.0.0.1 -p 8883 ./fca

import pytest


def test_success():
    assert True


def test_failure():
    assert False


def test_skip():
    pytest.skip("for a reason!")


def test_broken():
    raise Exception("oops")

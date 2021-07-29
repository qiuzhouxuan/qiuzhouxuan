# 测试用例分等级执行
# 执行命令
# pytest -s -v 文件名 --allure-severities normal,critical
# Blocker:中断缺陷
# Critical:临界缺陷（功能点缺失）
# Normal:普通缺陷（数值计算错误）
# Minor:次要缺陷（界面错误与UI不符）
# Trivial：轻微缺陷（必输项无提示）
import allure


def test_with_serverity_lable():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_trivial_severity_1():
    pass


@allure.severity(allure.severity_level.BLOCKER)
def test_with_trivial_severity_2():
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_with_trivial_severity_3():
    pass


@allure.severity(allure.severity_level.MINOR)
def test_with_trivial_severity_4():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity_5():
    pass

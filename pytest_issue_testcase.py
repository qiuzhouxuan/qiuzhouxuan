# 给测试场景添加链接
import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一个测试")
    pass


TEST_LINK = "http://www.baidu.com"


@allure.testcase(TEST_LINK, "链接2")
def test_with_testcase_link():
    print("这是一条测试用例链接，链接为上方变量")
    pass


# 140为BUG编号
# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue("140", "这是一个issure")
def test_with_issue_link():
    pass

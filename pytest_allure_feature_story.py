import allure


# @allure.feature；为报告区分测试模块名
# @allure.story：为报告设置测试场景名
# allure.step：为报告设置测试步骤名
# 指定执行相应的模块名（针对多模块接口自动化测试）pytest pytest_allure_feature_story.py --allure-features "登录模块"
# 指定执行相应的模块名下的的测试场景名称pytest pytest_allure_feature_story.py --allure--stories"登录成功"


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录;  测试用例 ， 登录成功")
        pass

    @allure.story("登录失败")
    def test_login_a(self):
        print("这是登录;  测试用例 ， 登录成功")
        pass

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("这用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("请输入用户名")
        with allure.step("点击密码"):
            print("请输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert "1" == 1
            print("登录失败")

    @allure.story("登陆失败")
    def test_login_faile_a(self):
        print("这是登录测试用例，登录失败")

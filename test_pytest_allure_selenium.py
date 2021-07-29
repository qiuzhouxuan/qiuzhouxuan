import time

import allure
import pytest
from selenium import webdriver


@allure.testcase("http://www.githup.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", ["allure", "pytest", "阳逻"])
def test_step_demo(test_data1):
    with allure.step("打开浏览器页面"):
        driver = webdriver.Chrome(executable_path=r"C:\Python382\chromedriver.exe")
        driver.get("http://www.baidu.com")

    with allure.step(f"输入关键搜索词:{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./fca/888.png")
        allure.attach.file("./fca/888.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()

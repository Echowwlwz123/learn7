# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 16:27
# @Author  : WANGWEILI
# @FileName: test_baidudemo.py
# @Software: PyCharm
import time

import allure
import pytest
from selenium import webdriver


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unitest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome("D:/王伟莉测试开发学习/测试人项目实践/learn7/PYTEST_DEMO/test_baidudemo.py")
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词:{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()

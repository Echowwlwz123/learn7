# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 22:14
# @Author  : WANGWEILI
# @FileName: test_wait.py
# @Software: PyCharm
from selenium import webdriver


class TestWait:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("霍格沃兹测试学院")

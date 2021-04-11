# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 10:11
# @Author  : WANGWEILI
# @FileName: test_file.py
# @Software: PyCharm
from time import sleep

from selenium_js.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/span[1]").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[5]/div/div/form/div/div[2]/div[2]/input").send_keys(r"D:\photo\123.jpg")
        sleep(3)

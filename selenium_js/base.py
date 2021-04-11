# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 21:38
# @Author  : WANGWEILI
# @FileName: base.py
# @Software: PyCharm
import os
from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

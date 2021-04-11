# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 21:38
# @Author  : WANGWEILI
# @FileName: base.py
# @Software: PyCharm
import os
from selenium import webdriver


class Base():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

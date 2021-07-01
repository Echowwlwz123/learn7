# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 20:16
# @Author  : WANGWEILI
# @FileName: fmain.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login import Login
from page.register import Register


class Fmain(BasePage):

    def goto_login(self):
        self.steps("../page/fmain.yaml")
        return Login(self._driver)

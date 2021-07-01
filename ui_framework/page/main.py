# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 20:42
# @Author  : WANGWEILI
# @FileName: main.py
# @Software: PyCharm
from page.base_page import BasePage
from ui_framework.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)

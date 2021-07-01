# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 20:45
# @Author  : WANGWEILI
# @FileName: market.py
# @Software: PyCharm
from page.base_page import BasePage
from ui_framework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)

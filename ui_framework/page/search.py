# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 20:48
# @Author  : WANGWEILI
# @FileName: search.py
# @Software: PyCharm
from page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page/search.yaml")

# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 20:53
# @Author  : WANGWEILI
# @FileName: test_search.py
# @Software: PyCharm
from ui_framework.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")

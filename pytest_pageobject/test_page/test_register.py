# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 20:46
# @Author  : WANGWEILI
# @FileName: test_register.py
# @Software: PyCharm
from page.fmain import Fmain


class TestRegister:
    def setup(self):
        self.main = Fmain()

    def test_register_rfirst(self):
        assert self.main.goto_register().register()

    def test_register_lfirst(self):
        self.main.goto_login().scan()

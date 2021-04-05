# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 8:27
# @Author  : WANGWEILI
# @FileName: test_hook.py
# @Software: PyCharm
import pytest


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_name(name):
    print(f"{name}")


def test_login():
    print("login")


def test_login_failure():
    print("login_failure")
    assert False


def test_search():
    print("search")

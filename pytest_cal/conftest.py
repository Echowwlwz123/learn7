# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 20:50
# @Author  : WANGWEILI
# @FileName: conftest.py
# @Software: PyCharm
import pytest
from python_practice.caculator import Caculator


@pytest.fixture(scope='module')
def tcal():
    print("开始计算")
    cal = Caculator()
    yield cal
    print("计算结束")

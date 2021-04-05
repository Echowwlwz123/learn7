# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 16:24
# @Author  : WANGWEILI
# @FileName: test_encode.py
# @Software: PyCharm
import pytest
from pytest_encode import logger


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_mm(name):
    logger.info("测试案例ENCODING")
    print(name)

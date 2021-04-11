# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 13:07
# @Author  : WANGWEILI
# @FileName: test_selenium.py
# @Software: PyCharm
from pytest_encode import logger
from selenium import webdriver


def test_selenium():
    logger.info("网站测试")
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")

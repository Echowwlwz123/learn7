# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 19:51
# @Author  : WANGWEILI
# @FileName: base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    # 复用浏览器
    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            # 使用浏览器复用模式（目的是可以在已经打开的页面上面测试已经登录的情况的案例）

            chrome_arg = Options()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=chrome_arg)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

        # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
        self._driver.implicitly_wait(5)

    def teardown(self):
        self._driver.quit()

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 19:51
# @Author  : WANGWEILI
# @FileName: base_page.py
# @Software: PyCharm
# 复用浏览器需要注意：
"""
1.需要退出当前所欲偶的谷歌浏览器（特别注意）
2.找到chrome的启动路径
3.配置环境变量
4.启动命令：windows:chrome --remote-debugging-port=9222
启动命令：mac: Google\Chrome --remote-debugging-port=9222
5.访问http://localhost:9222/
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from page.fmain import Fmain


class BasePage:
    _base_url = "https://work.weixin.qq.com/"

    # 复用浏览器
    def start(self, driver: WebDriver = None):
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
        return self

    def teardown(self):
        self._driver.quit()

    def main(self):
        return Fmain(self._driver)

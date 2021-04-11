# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 12:56
# @Author  : WANGWEILI
# @FileName: test_touchactions.py
# @Software: PyCharm
from time import sleep

import pytest
from selenium.webdriver import TouchActions

from pytest_selenium.base import Base


class TestTouchAction(Base):
    def test_touchaction_scrollbottom(self):
        """
        打开浏览器
        打开百度
        向搜索框中输入‘selenium测试’
        通过TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭浏览器
        :return:
        """
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el, 0, 10000).perform()
        sleep(3)

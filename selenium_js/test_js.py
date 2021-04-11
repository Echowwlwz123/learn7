# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 19:50
# @Author  : WANGWEILI
# @FileName: test_js.py
# @Software: PyCharm
from time import sleep

from selenium_js.base import Base
import pytest


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        sleep(3)
        element = self.driver.execute_script("return document.getElementById('su')")  # 找到搜索手柄
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 滑动到底部
        self.driver.find_element_by_xpath("//*[@id='page']//a[10]").click()  # 点击下一页
        sleep(3)
        #
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")  # 这个日期只能往后改不能往前改
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

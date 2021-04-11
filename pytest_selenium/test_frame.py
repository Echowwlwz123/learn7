# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 13:25
# @Author  : WANGWEILI
# @FileName: test_frame.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver import ActionChains

from pytest_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        ele = self.driver.find_element_by_id("draggable")
        elef = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele, elef).perform()
        sleep(3)

        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
        sleep(3)

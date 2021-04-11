# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 7:05
# @Author  : WANGWEILI
# @FileName: test_actionchains.py
# @Software: PyCharm
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_dblclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.click(element_dblclick)
        action.context_click(element_rightclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_move(self):
        # 将光标移动到某个位置上
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("新闻")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        # 点击HOLD一个元素，拖拽到一个位置
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        # 点击拖拽可以使用下面3种方法
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        # 使用TAB跳转到下一个输入框
        action.send_keys(Keys.TAB).pause(1)
        action.send_keys("jerry").pause(1).perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_actionchains.py'])

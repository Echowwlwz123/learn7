# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 10:50
# @Author  : WANGWEILI
# @FileName: test_alert.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver import ActionChains

from selenium_js.base import Base


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作创右侧页面，将元素1拖拽到元素2
        这时候会有一个alert弹框，点击弹框中的确定
        然后再按点击运行
        关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        print("点击alert确认")
        self.driver.switch_to_alert().accept()  # 点击弹出的alert弹出窗的确认
        self.driver.switch_to_default_content()  # 回到默认的frame下面
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

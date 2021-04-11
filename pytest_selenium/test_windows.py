# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 12:32
# @Author  : WANGWEILI
# @FileName: test_windows.py
# @Software: PyCharm
from time import sleep

from pytest_selenium.base import Base


class TestWindows(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_link_text("立即注册").click()
        windows = self.driver.window_handles

        # 收集的窗口中最后一个窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("12345")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("echo318961@")
        self.driver.find_element_by_id("TANGRAM__PSP_4__verifyCodeSend").click()
        self.driver.find_element_by_id("TANGRAM__PSP_4__verifyCode").send_keys("123")

        # 收集的窗口中第一个窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("uuuuuu")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("11111")
        sleep(5)

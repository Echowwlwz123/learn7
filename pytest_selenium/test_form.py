# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 22:58
# @Author  : WANGWEILI
# @FileName: test_form.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from pytest_selenium.base import Base


class TestForm(Base):
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("1091931840@qq.com")
        self.driver.find_element_by_id("user_password").send_keys("echo318961@")
        self.driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()
        self.driver.find_element_by_xpath('//*[id="new_user"]/div[4]/input')
        sleep(5)

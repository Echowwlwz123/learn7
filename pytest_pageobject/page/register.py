# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 19:50
# @Author  : WANGWEILI
# @FileName: register.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("izhan科技")
        self.find(By.ID, "manager_name").send_keys("echowwlwz")
        self.find(By.ID, "corp_industry").click()
        self.find(By.XPATH,
                  "/html/body/div/div/div/main/div/div/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr/td[1]/div[1]").click()
        self.find(By.XPATH,
                  "/html/body/div/div/div/main/div/div/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[1]/div[1]").click()
        self.find(By.ID, "corp_scale_btn").click()
        self.find(By.CSS_SELECTOR, ".ww_dropdownMenu_itemLink_text").click()
        self.find(By.ID, "register_tel").send_keys("123456")
        return True

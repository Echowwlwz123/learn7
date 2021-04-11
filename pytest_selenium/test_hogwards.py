# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 22:30
# @Author  : WANGWEILI
# @FileName: test_hogwards.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        # def wait(x):
        #     return len(self.driver.find_element(By.XPATH,'//*[@class="nav-item"]'))>=1
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="nav-item"]')))
        self.driver.find_element_by_css_selector(".topic-29255 .title > a").click()

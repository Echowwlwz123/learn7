# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:56
# @Author  : WANGWEILI
# @FileName: test_appium.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['noReset'] = True
        caps['browserName'] = 'Browser'
        # caps['chromedriverExecutable']='C:/Users/echowwlwz/AppData/Local/Programs/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()

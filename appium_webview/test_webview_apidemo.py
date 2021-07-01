# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:56
# @Author  : WANGWEILI
# @FileName: test_appium.py
# @Software: PyCharm
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '8.0'
        caps['appPackage'] = 'com.example.android.apis'
        caps['appActivity'] = 'com.example.android.apis.view.WebView1'
        caps['deviceName'] = 'emulator-5554'
        caps['noReset'] = True
        # caps['browserName']='Browser'
        # caps['chromedriverExecutable']='C:/Users/echowwlwz/AppData/Local/Programs/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}"))'
                                                        '.instance(0));').click()
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.ID, 'Hello World!-1').click()
        print(self.driver.page_source)

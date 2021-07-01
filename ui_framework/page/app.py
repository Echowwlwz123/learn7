# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 8:23
# @Author  : WANGWEILI
# @FileName: app.py
# @Software: PyCharm
from appium import webdriver

from page.base_page import BasePage
from ui_framework.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = 'com.xueqiu.android.common.MainActivity'
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['noReset'] = True
            caps['dontStopAppOnReset'] = True
            caps['skipDeviceInitialization'] = True
            caps['unicodeKeyBoard'] = True
            caps['resetKeyBoard'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def main(self):
        return Main(self._driver)

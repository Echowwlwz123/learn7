# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:56
# @Author  : WANGWEILI
# @FileName: test_appium.py
# @Software: PyCharm
from appium import webdriver

caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '6.0'
caps['deviceName'] = 'emulator-5554'
caps['appPackage'] = 'com.xueqiu.android'
caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
caps['noReset'] = True
caps['dontStopAppOnReset'] = True
caps['skipDeviceInitialization'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
driver.back()
driver.back()
driver.quit()

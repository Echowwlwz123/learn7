# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 14:06
# @Author  : WANGWEILI
# @FileName: test_dwappium.py
# @Software: PyCharm
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        caps['noReset'] = True
        # caps['dontStopAppOnReset'] = True
        caps['skipDeviceInitialization'] = True
        caps['unicodeKeyBoard'] = True
        caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):

        self.driver.quit()

    def test_search(self):
        print('搜索测试案例')
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框里面输入阿里巴巴
        4.在搜索结果里面选择阿里巴巴，然后进行点击
        5.获取这只香港阿里巴巴的股价，并判断这只股价的家隔>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attribute(self):
        """
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入：alibaba
        判断阿里巴巴是否可见
        如果可见，打印搜索成功点击，如果不可见，打印搜索失败
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # print(alibaba_element.get_attribute("displayed"))
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

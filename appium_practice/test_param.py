# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 20:52
# @Author  : WANGWEILI
# @FileName: test_param.py
# @Software: PyCharm
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestParam:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        caps['noReset'] = True
        caps['dontStopAppOnReset'] = True
        caps['skipDeviceInitialization'] = True
        caps['unicodeKeyBoard'] = True
        caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()

        # self.driver.quit()

    @pytest.mark.parametrize('searchkey, type, expect_price',
                             [('alibaba', 'BABA', 220), ('xiaomi', '01810', 20)])
    def test_search(self, searchkey, type, expect_price):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入搜索词 阿里巴巴，小米
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        current_price_elemet = self.driver.find_element(MobileBy.XPATH,
                                                        f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(current_price_elemet.text)
        print(f"当前股价是：{current_price}")
        print(f"期望股价是：{expect_price}")
        # expect_price =210
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))

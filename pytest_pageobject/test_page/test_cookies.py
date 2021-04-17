# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 12:57
# @Author  : WANGWEILI
# @FileName: test_cookies.py
# @Software: PyCharm
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from page.base_page import BasePage


class TestCookies():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_cookies(self):
        # 获取当前cookies
        # cookies = self._driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850159973427'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850159973427'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324972443261'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2619018'},
            {'domain': '.qq.com', 'expiry': 1681448653, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.40839872.1618375157'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2249096216, 'httpOnly': False,
             'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1618375155'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649911155, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1618375155'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649911154.526475, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2249096216, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
             'secure': True, 'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'yjSqUSsbdnoa5XBFjtyPABRrf7V8a4G9z57FZUF3OOpAsHYnDxPXTIC2iU7Z2JhT'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618406690.526441, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': True, 'value': '21qsp9r'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'ntyGJ02XC3qzbcjbXdcjesPD_YCFMCSW3VgpUwSGeKehASmg0wKkS4VPNQ6KxM-u4T7oZcAUI-yf24BWrmobN8ebmdthHZvkDRFB-Vl5EVjf34bBAkfb6_G9okHKoymdjkHAiQJTzZkOlhppEvvORTSRwbV-D31wGc0rCiI8tlu_-Y7URDU3kFL6VOfotv0tcnyh75Fhrwge7i6l1_ILJp67UwSGfG0MdwSqVDV418Yz5AeIBEVKUi0yz9_voHrOom_M89hUn_CDWl3OGuKvrw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2249096216, 'httpOnly': True, 'name': 'wwrtx.refid',
             'path': '/', 'secure': True, 'value': '23669720162353133'},
            {'domain': '.qq.com', 'expiry': 1618463053, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.541557003.1618375157'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1620968657.228284, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    # 实现 cookie 数据的持久化存储
    # def test_shelve(self):
    # #     """
    # #      # shelve python 内置的模块，相当于小型的数据库
    # #      # 带有登录信息的cookie
    # #     """
    #     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618375155'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649911155, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618375155'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '23669720162353133'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618406690.526441, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '21qsp9r'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649911154.526475, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1620967156.551737, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'en'}]
    #     db =shelve.open('./mydbs/cookies')
    #     db['cookie'] = cookies
    #     db.close()

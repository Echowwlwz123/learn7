# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 19:50
# @Author  : WANGWEILI
# @FileName: login.py
# @Software: PyCharm
import shelve
from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.register import Register


class Login(BasePage):
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)

    def scan(self):
        # 获取当前cookies
        # cookies = self._driver.get_cookies()
        # print(cookies)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1618375155'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649911155, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618375155'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '23669720162353133'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618406690.526441, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '21qsp9r'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649911154.526475, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1620967156.551737, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en'}]
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
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

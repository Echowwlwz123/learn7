# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 18:03
# @Author  : WANGWEILI
# @FileName: test_allure_link.py
# @Software: PyCharm
import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'https://blog.csdn.net/iKaChu/article/details/105714494'


@allure.testcase(TEST_CASE_LINK, "登录用例")
def test_with_testcase_link():
    print("这是一条加了链接的测试")
    pass


# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass

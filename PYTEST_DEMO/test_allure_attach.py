# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 15:51
# @Author  : WANGWEILI
# @FileName: test_allure_attach.py
# @Software: PyCharm
import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段HTML的BODY</body>", "HTML测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("D:/王伟莉测试开发学习/测试人项目实践/learn7/PYTEST_DEMO/resource/微信图片_20210401125306.jpg", "图片测试块",
                       attachment_type=allure.attachment_type.JPG)


def test_attach_gif():
    allure.attach.file("D:/王伟莉测试开发学习/测试人项目实践/learn7/PYTEST_DEMO/resource/77c4831103f95a72448ae630e9453615.gif", "动图测试块",
                       attachment_type=allure.attachment_type.GIF)

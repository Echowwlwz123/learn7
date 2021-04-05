# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 14:28
# @Author  : WANGWEILI
# @FileName: __init__.py.py
# @Software: PyCharm
import logging
from typing import List

import pytest

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='w'
                    )
logger = logging.getLogger(__name__)


def pytest_collection_modifyitems(session, config, items: List):
    for item in items:
        # item.name 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    # 执行顺序翻转
    items.reverse()

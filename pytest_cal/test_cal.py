# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 18:09
# @Author  : WANGWEILI
# @FileName: test_cal.py
# @Software: PyCharm
import pytest
import yaml

from python_practice.caculator import Caculator


def get_data(datav):
    with open(r"D:\王伟莉测试开发学习\测试人项目实践\learn7\pytest_cal\datas.yaml") as f:
        datas = yaml.safe_load(f)[datav]
        test_datas = datas['datas']
        print(test_datas)
        myid = datas['myid']
        print(myid)
    return test_datas, myid


class TestCal:
    def setup_class(self):
        print("开始计算")
        self.cal = Caculator()

    def teardown_class(self):
        print("计算结束")

    # 加法测试
    add_datas = get_data('add')

    @pytest.mark.parametrize("a,b,expact", add_datas[0], ids=add_datas[1])
    def test_add(self, a, b, expact):
        result = self.cal.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 减法测试
    subtr_datas = get_data('subtr')

    @pytest.mark.parametrize("a,b,expact", subtr_datas[0], ids=subtr_datas[1])
    def test_subt(self, a, b, expact):
        result = self.cal.subtr(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 乘法测试
    multi_datas = get_data('multi')

    @pytest.mark.parametrize("a,b,expact", multi_datas[0], ids=multi_datas[1])
    def test_multi(self, a, b, expact):
        result = self.cal.multi(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 除法测试
    divi_datas = get_data('divi')

    @pytest.mark.parametrize("a,b,expact", divi_datas[0], ids=divi_datas[1])
    def test_divi(self, a, b, expact):
        result = self.cal.divi(a, b)
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.cal.divi(a, b)
        else:
            if isinstance(result, float):
                result = round(result, 2)
            assert result == expact

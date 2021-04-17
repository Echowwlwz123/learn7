# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 18:09
# @Author  : WANGWEILI
# @FileName: test_cal.py
# @Software: PyCharm
import allure
import pytest
import yaml


def get_data():
    with open(r"D:\王伟莉测试开发学习\测试人项目实践\learn7\pytest_cal\datas.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


@allure.title("计算器测试")
class TestCal:
    # 加法测试
    @allure.story("加法测试案例")
    @pytest.mark.parametrize("a,b,expact", get_data()['add']['datas'], ids=get_data()['add']['myid'])
    def test_add(self, a, b, expact, tcal):
        result = tcal.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 减法测试
    @allure.story("减法测试案例")
    @pytest.mark.parametrize("a,b,expact", get_data()['subtr']['datas'], ids=get_data()['subtr']['myid'])
    def test_subt(self, a, b, expact, tcal):
        result = tcal.subtr(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 乘法测试
    @allure.story("乘法测试案例")
    @pytest.mark.parametrize("a,b,expact", get_data()['multi']['datas'], ids=get_data()['multi']['myid'])
    def test_multi(self, a, b, expact, tcal):
        result = tcal.multi(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expact

    # 除法测试
    @allure.story("除法测试案例")
    @pytest.mark.parametrize("a,b,expact", get_data()['divi']['datas'], ids=get_data()['divi']['myid'])
    def test_divi(self, a, b, expact, tcal):
        result = tcal.divi(a, b)
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.cal.divi(a, b)
        else:
            if isinstance(result, float):
                result = round(result, 2)
            assert result == expact

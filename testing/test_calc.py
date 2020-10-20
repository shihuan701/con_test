import pytest
import os
from utils.get_datas import GetData


'''
1、补全计算器（加减乘除）的测试用例
2、使用数据的数据驱动，节省代码编写量
3、创建 Fixture 方法实现，测试开始前打印【开始计算】，测试结束后打印【计算结束】
4、将 Fixture 方法存放在conftest.py ，设置scope=module
'''


class TestCalc():

    yaml_src = os.path.join(GetData().get_basesrc(),'datas/calc.yml')
    get_yaml = GetData().get_datas(yaml_src)
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['add']['datas'],
                             ids=get_yaml['add']['ids'])
    def test_add(self,init_calc,a, b,excepted):
        result = init_calc.add(a, b)
        assert result == excepted

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['div']['datas'],
                             ids=get_yaml['div']['ids'])
    def test_div(self, init_calc, a, b, excepted):
        result = init_calc.div(a, b)
        assert result == excepted

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['div_zero']['datas'],
                             ids=get_yaml['div_zero']['ids'])
    def test_div_zero(self, init_calc, a, b, excepted):
        with pytest.raises(ZeroDivisionError):
            init_calc.div(a, b)

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['div_float']['datas'],
                             ids=get_yaml['div_float']['ids'])
    def test_div_float(self, init_calc, a, b, excepted):
        c = init_calc.div(a, b)
        assert round(c,2) == excepted


    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['sub']['datas'],
                             ids=get_yaml['sub']['ids'])
    def test_sub(self, init_calc, a, b, excepted):
        assert excepted == init_calc.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['mul']['datas'],
                             ids=get_yaml['mul']['ids'])
    def test_mul(self, init_calc, a, b, excepted):
        assert excepted == init_calc.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,excepted', get_yaml['mul_float']['datas'],
                             ids=get_yaml['mul_float']['ids'])
    def test_mul_float(self, init_calc, a, b, excepted):
        assert excepted == round(init_calc.mul(a, b),2)

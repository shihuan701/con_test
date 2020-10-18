import sys

print('-----------', sys.path.append('..'))
import pytest
from pythoncode.calc import Calculator



class TestCalc:
    def setup_class(cls):
        print('类级别 setup_class')

    def teardown_class(cls):
        print('类级别 teardown_class')

    def setup(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,result', [(1, 1, 2), (100, 200, 300), (-1.0, -1.1, -2.1)],
                             ids=['int', 'bignum', 'floatnum'])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)


    @pytest.mark.parametrize('a,b,result', [(3, 1, 3.00), (-3, -1, 3.00),(-3, 1, -3.00),(6.2, 4, 1.55),(0, 200, 0), (7, 0, '除数不能为0')],
                             ids=['均为为正整数', '均为为负数','其中有一个为负数','为小数','被除数为0', '除数为0'])
    def test_div(self,a, b, result):
        assert result == self.calc.div(a, b)

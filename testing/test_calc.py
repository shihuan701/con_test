
import sys

import pytest
from pythoncode.calc import Calculator

def setup_module():
    print('模块级别 setup')

def teardown_module():
    print('模块级别 teardown_module')

print('-----------',sys.path.append('..'))


def setup_function():
    print('方法级别 function')

def teardown_function():
    print('方法级别 teardown_function')

class TestCalc:
    def setup_class(cls):
        print('类级别 setup_class')

    def teardown_class(cls):
        print('类级别 teardown_class')

    def setup_method(self):
        self.calc = Calculator()
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result',[(1,1,2),(100,200,300),(-1.0,-1.1,-2.1)],ids=['int','bignum','floatnum'])
    def test_add(self,a,b,result):
        assert result == self.calc.add(a, b)



    @pytest.mark.div
    def test_add3(self):
        calc = Calculator()
        assert 5 == calc.add(1, 4)

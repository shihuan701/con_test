import pytest
from pythoncode.calc import Calculator
from typing import List
'''
作业3【选做】：

1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
'''


@pytest.fixture(scope='module')
def init_calc():
    calc = Calculator()
    print('开始计算')
    yield calc
    print('结束计算')

# 解决用例名称为中文的问题
def pytest_collection_modifyitems(
        session:'Session',config:'Config',items:List['Item']
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# 注册命令
def pytest_addoption(parser):
    mygroup = parser.getgroup('hogwarts')
    mygroup.addoption('--env',action="store",
                      default='test',
                      dest='env',
                      choices=['dev','st','test'],
                      help='set your env')

# @pytest.fixture(scope='session')
# def cmdoption(request):
#     print('默认:',request.config.getoption('--env'))
#     return request.config.getoption('--env',default='test')



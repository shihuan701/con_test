import pytest

@pytest.fixture(scope='modele')
# scope 指定范围内共享，作用范围有：
# function: 函数或方法级别都会被调用
# class : 类级别调用一次
# module:模块级别调用一次
# session:多个文件调用一次，可以跨文件调用，每个.py文件就是module
def login():
    print('登录成功')
    session = '6a8dyhug97787662481'
    yield session
    print('teardown')

@pytest.fixture()
def getUser():
    print('登录后操作')
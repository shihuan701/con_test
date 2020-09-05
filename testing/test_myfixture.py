import pytest


class TestMyFixture:

    def test_case1(self,login,getUser):
        print(login)
        print(getUser)
        print('需要登陆')

    def test_case2(self):
        print('不需要要登录')
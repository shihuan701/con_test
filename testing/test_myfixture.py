import pytest


class TestMyFixture:

    def test_case1(self,login,getUser,request):
        print(login)
        print(getUser)
        print('需要登陆')

    @pytest.mark.parametrize('login',[(1,2),(3,4)])
    def test_case2(self,login):
        print('login参数化',login)
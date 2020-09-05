from pythoncode.calc import Calculator


def test_add():
    calc = Calculator()
    assert 2 == calc.add(1,1)
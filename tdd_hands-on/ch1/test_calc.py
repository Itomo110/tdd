from .calc import add, sub


def test_add():
    assert add(2,3) ==5


def test_add1():
    assert add(10,90) == 100

def test_sub():
    assert sub(110,10) == 100
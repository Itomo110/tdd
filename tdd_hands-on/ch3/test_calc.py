import pytest

from .calc import add,mul

@pytest.mark.parametrize('x,y,expected',[
(2,3,5),
('Hello','World','Hello World'),
])
def test_add(x,y,expected):
    assert add(x,y) == expected

@pytest.mark.parametrize('x,y,expected',[
(2,3,6),
('Hello',2,'HelloHello'),
('Hello',0,""),
('Hello',1.5,""),
])
def test_mul(x,y,expected):
    assert mul(x,y) == expected

@pytest.mark.parametrize('x,y',[
('Hello',2),
(3,'Hello')
])
def test_add_raises(x,y):
    with pytest.raises(ValueError):
        add(x,y)
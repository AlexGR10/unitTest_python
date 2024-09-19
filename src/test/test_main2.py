import pytest 
from src.main2 import sum, sub, div

def test_sum():
    assert sum(1, 2) == 3
    

def test_sub():
    assert sub(5, 3) == 2

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (20, 4, 5),
    (30, 0, ValueError), 
])
def test_div(x, y, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            div(x, y)
    else:
        assert div(x, y) == expected
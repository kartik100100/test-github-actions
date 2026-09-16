from src.math_operations import add, subtraction

def test_add():
    assert add(3,4)==7
    assert add(-1,4)==3
    assert add(-1,1)==0


def test_sub():
    assert subtraction(6,4)==2
    assert subtraction(5,5)==0
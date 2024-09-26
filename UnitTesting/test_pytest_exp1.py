import pytest_exp1
import pytest

#@pytest.mark.x
def test_add():
    assert pytest_exp1.add(5,20) == 25

def test_mult():
    assert pytest_exp1.mult(4,5) == 20

def sub():
    assert pytest_exp1.sub(20,5) == 15

def test_hello():
    assert pytest_exp1.hello() == 'Working fine'
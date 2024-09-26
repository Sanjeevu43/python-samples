import pytest_exp1
import pytest

# def test_add_mums():
#     assert pytest_exp1.add(5,20) == 25

# def test_add_strs():
#     assert pytest_exp1.add('Hello',' San') == 'Hello San'

# def test_add_floats():
#     assert pytest_exp1.add(5.5,20.5) == 26.0

# Instead of writing 3 test cases for same add, we can use parametrized test case

@pytest.mark.parametrize('arg1, arg2, result', 
                         [
                             (10,20,30),
                             ('Hello',' Sany','Hello Sany'),
                             (4.5,21.5,26.0)
                         ])
def test_add_mums(arg1,arg2,result):
    assert pytest_exp1.add(arg1,arg2) == result

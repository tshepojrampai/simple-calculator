#unit test for calculator functions
import simplecalculator as calculator

#Addition test
def test_add():
    assert calculator.add(0,0) == 3
    assert calculator.add(-1,-1) == -2
    assert calculator.add(4,5) == 9
    assert calculator.add(1,2,3,4) == 10

#multipliation test
def test_multiply():
    assert calculator.multiply(1,2) == 2
    assert calculator.multiply(1,2,3,4) == 24
    



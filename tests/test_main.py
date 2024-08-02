from main import isGreaterThan, sum, login
import pytest

def testSum():
    assert sum(2,5) == 7

def testIsGreaterThan():
    assert isGreaterThan(12,8) == True

@pytest.mark.parametrize(
    "inputA, inputB, expected",
    [
        (5,2,7),
        (7,1,8),
        (2,7,9),
        (1,1,2)
    ]
)
def testSumParams(inputA, inputB, expected):
    assert sum(inputA, inputB) == expected

def testLogin():
    loginPassed = login("juan123", "1234567")
    assert loginPassed

def testLoginFaild():
    loginPassed = login("juan12", "1234567")
    assert not loginPassed
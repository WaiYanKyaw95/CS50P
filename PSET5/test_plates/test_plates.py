from plates import is_valid

def test_startWithZero():
    assert is_valid('0AA22') == False
    assert is_valid('AA023') == False

def test_startWithTwoLetters():
    assert is_valid('AA222') == True
    assert is_valid('BB232') == True
    assert is_valid('A235') == False

def test_minAndMax():
    assert is_valid('A') == False
    assert is_valid('AAA2232') == False

def test_numInMiddle():
    assert is_valid('AA22AA') == False
    assert is_valid('AA2234') == True

def test_notAlphaDigit():
    assert is_valid('AA.23') == False
    assert is_valid('A2345!') == False

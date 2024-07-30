from bank import value

# ensure that greeting with hello return 0
def test_hello():
    assert value("hello") == 0
    assert value("Hello, Wai Yan") == 0

# ensure that greeting with word starting with h return 20
def test_h():
    assert value("Hi") == 20
    assert value("Hi, Norman") == 20

# test whether greeting with words other than hello or start with h, otherwise return 100
def test_other():
    assert value("What's up?") == 100
    assert value("Wee hee") == 100

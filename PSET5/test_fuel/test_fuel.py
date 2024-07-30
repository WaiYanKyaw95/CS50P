import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("2/3") == 67

def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_nonInteger():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_largeDividend():
    with pytest.raises(ValueError):
        convert("3/2")

def test_gaugeEmpty():
    assert gauge(1) == "E"

def test_gaugeFull():
    assert gauge(99) == "F"

def test_gaugePercent():
    assert gauge(35) == "35%"


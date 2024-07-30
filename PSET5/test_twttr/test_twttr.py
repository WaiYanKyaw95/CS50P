from twttr import shorten

def test_small_letter():
    assert shorten("This is CS50!") == "Ths s CS50!"
    assert shorten("Twitter") == "Twttr"

def test_capital_letter():
    assert shorten("NO MATTER") == "N MTTR"
    assert shorten("THERE IS NO SUCH PLACE") == "THR S N SCH PLC"

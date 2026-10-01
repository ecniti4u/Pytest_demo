import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_creditcard():
    msg = "Hello"
    assert msg == "Hi", "Testpy failed bcz stings do not match"

def test_secondprogram():
    a = 4
    b = 6
    assert a+2 == 6, "addition do not match "



def test_fixturedemo(setup):
    print("i will execute steps in fixturedemo method")

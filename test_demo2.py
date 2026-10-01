import pytest

@pytest.mark.smoke
def test_firstprogram():
    print("Hello")

@pytest.mark.xfail
def test_greetcreditcard():
    print("good")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

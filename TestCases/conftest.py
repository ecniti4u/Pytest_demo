import pytest


@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i will be executing last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return["Rahul", "Shetty", "rahulshetty.com"]


@pytest.fixture(params=[("chrome","rahul","shetty"),("firefox","shetty"), ("IE","ss")])
def crossBrowser(request):
    return request.param


nithi


asdvgbhjmkdfghjkldcvbnm,.git



from lib.greet import *

def test_greet():
    result = greet("Som")
    assert result == "Hello, Som!"
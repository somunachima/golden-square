from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."

def test_multiple_counter():
    counter = Counter()
    counter.add(3)
    counter.add(8)
    assert counter.report() == "Counted to 11 so far."

def test_multiple_minus_counter():
    counter = Counter()
    counter.add(-2)
    counter.add(5)
    assert counter.report() == "Counted to 3 so far."
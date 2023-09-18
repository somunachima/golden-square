from lib.check_codeword import *

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_with_similar_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_with_wrong_codeword():
    result = check_codeword("wrong")
    assert result == "WRONG!"

def test_with_similar_first_codeword():
    result = check_codeword("heat")
    assert result == "WRONG!"

def test_with_similar_last_codeword():
    result = check_codeword("nose")
    assert result == "WRONG!"
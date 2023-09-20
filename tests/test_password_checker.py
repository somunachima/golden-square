import pytest
from lib.password_checker import PasswordChecker

def test_incorrect_password_checker():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("abc123")
    assert str(e.value) == "Invalid password, must be 8+ characters"

def test_empty_password_checker():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("")
    assert str(e.value) == "Invalid password, must be 8+ characters"

def test_correct_password_checker():
    password_checker = PasswordChecker()
    assert password_checker.check("somunachima") == True

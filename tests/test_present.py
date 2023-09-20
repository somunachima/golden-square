import pytest
from lib.present import Present

def test_no_errors():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

def test_unwrap_no_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped"

def test_already_wrap_error():
    present = Present()
    present.wrap("hello")
    with pytest.raises(Exception) as e:
        present.wrap("bye")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped"

def test_prevent_overwrite_if_already_wrap_error():
    present = Present()
    present.wrap("hello")
    with pytest.raises(Exception) as e:
        present.wrap("bye")
    assert present.unwrap() == "hello"

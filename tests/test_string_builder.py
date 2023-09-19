from lib.string_builder import StringBuilder

def test_empty_string_builder():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_size_string_builder():
    string_builder = StringBuilder()
    string_builder.add("and call")
    result = string_builder.size()
    assert result == 8

def test_output_string_builder():
    string_builder = StringBuilder()
    string_builder.add("and call")
    result = string_builder.output()
    assert result == "and call"

def test_multiple_string_builder():
    string_builder = StringBuilder()
    string_builder.add("som cook ")
    string_builder.add("and call")
    assert string_builder.output() == "som cook and call"

def test_multiple_string_builder():
    string_builder = StringBuilder()
    string_builder.add("som cook ")
    string_builder.add("and call")
    assert string_builder.size() == 17
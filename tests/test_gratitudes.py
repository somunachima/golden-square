from lib.gratitudes import Gratitudes

def test_empty_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_adding_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("friends")
    assert gratitudes.format() == "Be grateful for: family, friends"
"""Test file to practice the structure of pytest"""

# simple test
def test_add_two():
    x = 1
    y = 2
    assert x + y == 3


# example of how dictionaries are tested - important for APIs because APIs work with Json and python always treats Json as dictionaries
def test_dict_contains():
    x = {"a": 1, "b": 2}
    expected = {"a": 1}
    assert expected.items() <= x.items()  # .items() looks into the contents of the dictionary

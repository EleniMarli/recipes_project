from main.app import give_list_with_1st_as_float

def test_function():
    result = give_list_with_1st_as_float("1 unit(s) egg(s)")
    assert result == [1.0, 'unit(s)', 'egg(s)']
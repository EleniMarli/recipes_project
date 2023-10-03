from main.ingredient_module import Ingredient

def test_ingredient_can_be_created_from_string():
    result = Ingredient.from_str_to_ingredient("1 unit(s) egg(s)")
    assert isinstance(result, Ingredient)
    assert [result.amount, result.metric_unit, result.name] == [1.0, 'unit(s)', 'egg(s)']

def not_recognised_by_pytest():
    return True

def test_recognised_by_pytest():
    assert not_recognised_by_pytest() == True
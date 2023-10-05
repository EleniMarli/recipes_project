from main.ingredient_module import Ingredient

def test_ingredient_can_be_created_from_string():
    # when
    result = Ingredient.from_str_to_ingredient("egg(s), 1 unit(s)")

    # then
    assert isinstance(result, Ingredient)
    assert result.as_list() == [1.0, 'unit(s)', 'egg(s)']
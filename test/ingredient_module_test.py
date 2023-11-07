import pytest
from main.ingredient_module import Ingredient



def test_ingredient_can_be_created_from_string():
    # when
    result = Ingredient.from_str_to_ingredient("egg(s), 1 unit(s)")

    # then
    assert isinstance(result, Ingredient) # whether result is object of class Ingredient
    assert result.as_list() == [1.0, 'unit(s)', 'egg(s)']



@pytest.mark.parametrize("amount, unit, name", 
                         [(300.00, 'gr', 'flour'),
                          (15.27, 'tons', 'salt'),
                          (400.456, 'ml', 'red wine')])
def test_Ingredient_can_be_converted_to_list(amount, unit, name):
    # given
    ingr = Ingredient(amount, unit, name)
    
    # when
    result_list = ingr.as_list()

    # then
    assert result_list == [amount, unit, name]



@pytest.mark.parametrize("amount, unit, name, expected",
                         [(300, 'gr', 'flour', 'flour, 300 gr'),
                          (15.27, 'tons', 'salt', 'salt, 15.27 tons'),
                          (400.456, 'ml', 'red wine', 'red wine, 400.456 ml')])
def test_Ingredient_can_be_converted_to_str(amount, unit, name, expected):
    # given
    ingr = Ingredient(amount, unit, name)
    
    # when
    result_str = ingr.as_str()

    # then
    assert result_str == expected
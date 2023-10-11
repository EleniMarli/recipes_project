from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.ingredient_module import Ingredient
from test.paths_config_for_tests import result_full_path, shopping_list_full_path

def test_shopping_list_can_be_created_from_list_of_recipes():
    # given
    recipe1 = Recipe ('recipe1', [Ingredient(3.0, 'unit(s)', 'egg(s)')])
    
    # when
    result = Shopping_list.from_list_of_recipes([recipe1])
    
    # then
    assert isinstance (result, Shopping_list)
    ingr = result.list_of_all_ingredients[0]
    assert isinstance (ingr,Ingredient)
    assert ingr.as_list() == [3.0, 'unit(s)', 'egg(s)']

def test_combine_repetitions():
    # given
    shop_list1 = Shopping_list([ 
        Ingredient(3.0, 'unit(s)', 'egg(s)'),
        Ingredient(250.0, 'gr', 'flour'),
        Ingredient(1.0, 'unit(s)', 'egg(s)') 
        ])
    
    # when
    Shopping_list.combine_repetitions(shop_list1)

    # then
    assert isinstance (shop_list1, Shopping_list)
    list1 = list (map (lambda ingr : ingr.as_list(), shop_list1.list_of_all_ingredients))
    assert list1 == [ [4.0, 'unit(s)', 'egg(s)'], [250.0, 'gr', 'flour'] ]

def test_export_to_text_file_from_path ():
    # given
    shop_list1 = Shopping_list([ 
        Ingredient(3.0, 'unit(s)', 'egg(s)'),
        Ingredient(250.0, 'gr', 'flour'),
        Ingredient(1.0, 'unit(s)', 'egg(s)') 
        ])
    
    # when
    shop_list1.export_to_text_file(result_full_path)
    
    # then
    with open(shopping_list_full_path) as file:
        shopping_list = file.read()
        first_line = shopping_list.split('\n')[0]
        assert first_line == "Your shopping list:"
        assert "flour" in shopping_list
        assert "egg(s)" in shopping_list
import os
from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.ingredient_module import Ingredient
from test.paths_config_for_tests import result_full_path, temporary_shopping_list_full_path, permanent_result_folder_full_path



def test_shopping_list_can_be_created_from_list_of_recipes():
    # given
    recipe1 = Recipe('recipe1.txt', 'Cook this', 2.0, [Ingredient(3.0, 'unit(s)', 'egg(s)')])
    recipe2 = Recipe('recipe2.txt', 'Bake this', 3.0, [Ingredient(200.0, 'gr', 'sugar')])
    list_of_recipes = [recipe1, recipe2]
    
    # when
    result = Shopping_list.from_list_of_recipes(list_of_recipes)
    
    # then
    assert isinstance (result, Shopping_list)
    for ingr in result.list_of_all_ingredients:
        assert isinstance (ingr,Ingredient)
    ingr1 = result.list_of_all_ingredients[0]
    ingr2 = result.list_of_all_ingredients[1]
    assert ingr1.as_list() == [3.0, 'unit(s)', 'egg(s)']
    assert ingr2.as_list() == [200.0, 'gr', 'sugar']



def test_combine_repetitions():
    # given
    shop_list1 = Shopping_list([ 
        Ingredient(3.0, 'unit(s)', 'egg(s)'),
        Ingredient(250.0, 'gr', 'flour'),
        Ingredient(1.0, 'unit(s)', 'egg(s)') 
        ])
    
    # when
    shop_list1.combine_repetitions()

    # then
    assert isinstance (shop_list1, Shopping_list)
    assert shop_list1.list_of_all_ingredients[0].as_list() == [4.0, 'unit(s)', 'egg(s)']
    assert shop_list1.list_of_all_ingredients[1].as_list() == [250.0, 'gr', 'flour']



def test_export_to_temporary_txt_file_from_path ():
    # given
    shop_list1 = Shopping_list([ 
        Ingredient(3.0, 'unit(s)', 'egg(s)'),
        Ingredient(250.0, 'gr', 'flour'),
        Ingredient(1.0, 'unit(s)', 'egg(s)') 
        ])
    
    # when
    shop_list1.export_to_temporary_text_file(result_full_path)

    # then
    with open(temporary_shopping_list_full_path) as file:
        shopping_list = file.read()
        assert shopping_list.split('\n')[0] == "Your shopping list:"
        assert shopping_list.split('\n')[1] == "egg(s), 3.0 unit(s)"
        assert shopping_list.split('\n')[2] == "flour, 250.0 gr"
        assert shopping_list.split('\n')[3] == "egg(s), 1.0 unit(s)"


def test_export_to_permanent_text_file():
    # setup
    filename = "permanent_shopping_list"
    path = os.path.join(permanent_result_folder_full_path, filename + ".txt")
    if os.path.isfile(path):
        os.remove(path)
    
    # given
    shopping_list = Shopping_list([ 
        Ingredient(3.0, 'unit(s)', 'egg(s)'),
        Ingredient(250.0, 'gr', 'flour'),
        Ingredient(1.0, 'unit(s)', 'egg(s)') 
        ])
    
    # when
    shopping_list.export_to_permanent_text_file(permanent_result_folder_full_path, filename)

    # then  permanent_result_folder_full_path 
    with open(path) as file:
        shopping_list = file.read()
        assert shopping_list.split('\n')[0] == "Your shopping list:"
        assert shopping_list.split('\n')[1] == "egg(s), 3.0 unit(s)"
        assert shopping_list.split('\n')[2] == "flour, 250.0 gr"
        assert shopping_list.split('\n')[3] == "egg(s), 1.0 unit(s)"
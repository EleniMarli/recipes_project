import os

from main.recipe_module import Recipe
from main.ingredient_module import Ingredient
from test.paths_config_for_tests import recipes_full_path



def test_list_of_Ingr_can_be_created_from_list_of_ingr_str ():
    #given
    list_of_ingr_str = ['egg(s), 4 unit(s)', 'flour, 400 gr']

    #when
    result = Recipe.create_list_of_ingredients(list_of_ingr_str)

    #then
    assert isinstance (result, list)
    assert result[0].as_str() == 'egg(s), 4.0 unit(s)'
    assert result[1].as_str() == 'flour, 400.0 gr'
    for ingr in result:
        assert isinstance (ingr,Ingredient)
   


def test_recipe_can_be_created_from_file():
    # given
    filename  = 'recipe1.txt'
    
    # when
    result = Recipe.from_file(recipes_full_path, filename)
    
    # then
    assert isinstance (result, Recipe)
    assert result.name == 'recipe1.txt'
    assert result.instructions[0] == 'Cook spaghetti according to package instructions.'
    assert result.portions == 4.0
    assert isinstance (result.list_of_ingredients, list)
    for ingr in result.list_of_ingredients:
        assert isinstance (ingr,Ingredient)
    assert result.list_of_ingredients[0].as_list() == [400.0, 'gr', 'spaghetti']
    assert result.list_of_ingredients[1].as_list() == [150.0, 'gr', 'guanciale or pancetta']



def test_portions_adjustment ():
    # given
    recipe = Recipe ('recipe.txt', 'Cook this', 1.0, [Ingredient(3.0, 'unit(s)', 'egg(s)')])

    # when
    result = recipe.adjust_portions(6)

    # then 
    assert isinstance (result, Recipe)
    assert result.portions == 6.0
    assert result.list_of_ingredients[0].amount == 18.0



# for this test i had to add the path as argument in the OG function!!!!
def test_export_to_file():
    # given
    recipe3 = Recipe ('recipe3.txt', 'Cook this', 1.0, [Ingredient(3.0, 'unit(s)', 'egg(s)')])

    # when
    recipe3.export_to_file(recipes_full_path)

    # then
    with open (os.path.join(recipes_full_path, recipe3.name)) as file:
        recipe3_str = file.read()
        assert recipe3_str.split('\n')[1] == 'Cook this'
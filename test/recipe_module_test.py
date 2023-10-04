from main.recipe_module import Recipe
from main.ingredient_module import Ingredient

def test_recipe_can_be_created_from_file_name():
    # when
    result = Recipe.from_file('C:/VSCode/recipes_project/test/text/recipes', 'recipe1.txt')
    
    # then
    assert isinstance (result, Recipe)
    for ingr in result.list_of_ingredients:
        assert isinstance (ingr,Ingredient)
    first_ingr = result.list_of_ingredients[0]
    assert first_ingr.as_list() == [1.0, 'unit(s)', 'egg(s)']
import os

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list

def execute_app():
    text_folder_path = 'C:/VSCode/recipes_project/main/text'
    recipes_path = text_folder_path + '/recipes'
    result_path = text_folder_path + '/result'

    all_filenames_as_list_of_str = os.listdir(recipes_path) # list of str: list of all files names in the folder

    recipe_objects_list = [] # I will end up with a list of all the Recipe objects
    for file_name in all_filenames_as_list_of_str:
        recipe_objects_list += [Recipe.from_file(recipes_path, file_name)]

    shopping_list = Shopping_list.from_list_of_recipes(recipe_objects_list)

    shopping_list.combine_repetitions()

    shopping_list.export_to_text_file(result_path)

    print("Application has run successfully, the shopping list can be found in the ./main/text/result directory")
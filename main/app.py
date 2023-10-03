from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import os

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list

text_folder_path = 'C:/VSCode/recipes_project/main/text'
recipes_path = text_folder_path + '/recipes'
result_path = text_folder_path + '/result'

all_filenames_as_list_of_str = os.listdir(recipes_path) # list of str: list of all files names in the folder

recipe_objects_list = [] # I will end up with a list of all the Recipe objects
for file_name in all_filenames_as_list_of_str:
    recipe_objects_list += [Recipe.from_file(file_name)]

shopping_list = Shopping_list.from_list_of_recipes(recipe_objects_list)

shopping_list.filter_out_repetitions()

shopping_list.export_to_text_file(result_path)

# convert metric units?
# kg,kilo,kilos,kilogram, kilograms --> gr
# recognise gram --> gr
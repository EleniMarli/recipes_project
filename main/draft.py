import os
folder_path = 'C:/VSCode/recipes_project/main/text/recipes'

from ingredient_module import Ingredient
from recipe_module import Recipe
from shopping_list_module import Shopping_list

all_filenames_as_list_of_str = os.listdir(folder_path) # list of str: list of all files names in the folder

recipes_cl_list = [] # we will end up with a list of all the Recipe objects

list_of_ingr_cl_for_all_files = []  # we will end up with  a list of lists of ingredients

for file_name in all_filenames_as_list_of_str:
    list_of_ingr_cl_for_single_file = []
    with open(f"C:/VSCode/recipes_project/main/text/recipes/{file_name}") as file:
        file_lines = file.read()
        file_list_of_str = file_lines.split('\n')  #list of strings
        for str_Ingr in file_list_of_str:
            object_Ingr = Ingredient.from_str_to_ingredient(str_Ingr) # i made Ingredient objects here
            list_of_ingr_cl_for_single_file += [object_Ingr]
        recipes_cl_list += [Recipe(f"{file_name}", list_of_ingr_cl_for_single_file)]

separated_list_of_ingr_cl_for_all_files = []
for recipe in recipes_cl_list:
    separated_list_of_ingr_cl_for_all_files += [recipe.list_of_ingredients]

print()

unified_list_of_ingr_cl_for_all_files = []
for sublist in separated_list_of_ingr_cl_for_all_files:
    for item in sublist:
        unified_list_of_ingr_cl_for_all_files.append(item)

# we end up with a unified list of ingredients

sl_before_filtering = Shopping_list (unified_list_of_ingr_cl_for_all_files)

print()

# here we need to filter for repetition of ingr within the sl_before_filtering

# evens = list(filter(lambda x: x%2 == 0, [1,2,3,4]))
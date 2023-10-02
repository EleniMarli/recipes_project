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

separated_list_of_ingr_cl_for_all_files = []  # [[ingra1,ingra2,ing3], [ingrb1,ingrb2,ingrb3], [ingrc1,ingrc2]]
for recipe in recipes_cl_list:
    separated_list_of_ingr_cl_for_all_files += [recipe.list_of_ingredients]

unified_list_of_ingr_cl_for_all_files = []  #!!!!!!!!!!!  [ingra1,ingra2,ing3,ingrb1,ingrb2,ingrb3, ingrc1,ingrc2]
for sublist in separated_list_of_ingr_cl_for_all_files:
    for item in sublist:
        unified_list_of_ingr_cl_for_all_files.append(item)

# we end up with a unified list of ingredients

sl_before_filtering = Shopping_list (unified_list_of_ingr_cl_for_all_files)   # object of class Shopping list


# here we need to filter for repetition of ingr within the unified_list_of_ingr_cl_for_all_files

names_list_pre_filter = list (map (lambda x : x.name , sl_before_filtering.list_of_all_ingredients ))   # [eggs,flour,salt,eggs,flour] -->just STRINGS

set_unique_names = set(names_list_pre_filter) # in a set each element appears only once {eggs,flour,salt} --> just STRINGS???   {eggs, flour, salt}


list_sublists = []

for unique_name in set_unique_names:
    extra = list (filter ( lambda ingr: ingr.name == unique_name , sl_before_filtering.list_of_all_ingredients ))
    list_sublists.append(extra)   # with append and not concatenation, i make sublists of ingr within the empty_list!



sl_final = []  # here i make the final shopping list, consisting of Ingredient objects

for sub in list_sublists:
    sum = 0
    for ingr in sub:
        sum += ingr.amount
    object = Ingredient (sum, ingr.metric_unit, ingr.name)
    sl_final += [object]


# # write result in the shopping list text file

shopping_list = open("C:/VSCode/recipes_project/main/text/result/myshoppinglist.txt", "w")
# This "w" command creates a new file, but unlike the "x", it overwrites any existing file found with the same file name.

#HOW TO WRITE SOMETHING IN THE NEW TEXT FILE:
shopping_list.write("Your shopping list:")
for ingr in sl_final:
    shopping_list.write(f"\n{ingr.amount} {ingr.metric_unit} {ingr.name} ")
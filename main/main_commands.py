import os

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list

import subprocess

def choose_files (all_filenames_as_list_of_str_local):
 
    while True:
        print("\nThe following are the available recipes:")

        dictionary = {}
        counter = 1
        for file_name in all_filenames_as_list_of_str_local:
            dictionary[counter] = file_name
            print(f"{counter} : {file_name}" )
            counter += 1

        print("\nPlease choose the recipes to be considered by typing the corresponding digit. Separate the digits using one space." )

        user_input_local = input()

        list_of_int = list (map (lambda x: int(x), user_input_local.split(' ')))

        called_filenames_list_local = []
        for integr in list_of_int:
            called_filenames_list_local += [dictionary.get(integr)]

        if None in called_filenames_list_local:
            print(f"\nOne or more digits you have inserted do not correspond to a recipe. Try again.")
        else:
            break

    print("\nThe selected recipes are the following:")
    print(*called_filenames_list_local, sep='\n')

    return called_filenames_list_local

def from_filenames_to_shopping_list (called_filenames_list_local, recipes_path_local, result_path_local):
    recipe_objects_list = [] # I will end up with a list of all the Recipe objects
    for file_name in called_filenames_list_local:
        recipe_objects_list += [Recipe.from_file(recipes_path_local, file_name)]

    shopping_list = Shopping_list.from_list_of_recipes(recipe_objects_list)

    shopping_list.combine_repetitions()

    shopping_list.export_to_text_file(result_path_local)

    print("\nApplication has run successfully, the shopping list can be found in the ./main/text/result directory")



def execute_app():
    text_folder_path = 'C:/VSCode/recipes_project/main/text'
    recipes_path = text_folder_path + '/recipes'
    result_path = text_folder_path + '/result'

    all_filenames_as_list_of_str = os.listdir(recipes_path) # list of str: list of all files names in the folder

    flag = True

    while flag == True:
        called_filenames_list = choose_files(all_filenames_as_list_of_str)

        print("\nAre you sure? (yes/no/help)")

        user_input = input()
        if user_input == 'yes':
            from_filenames_to_shopping_list (called_filenames_list, recipes_path, result_path)
            flag = False


        elif user_input == 'no':
            flag = True


        elif user_input == 'help':
            subprocess.run(['notepad.exe', 'C:/VSCode/recipes_project/README.md'], check=True)
            print('\nHopefully that was helpful.')


        else:
            print (f"The command {user_input} is not valid. Try again.")
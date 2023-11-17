import os
import subprocess

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.paths_config import recipes_full_path, result_full_path, readme_full_path, permanent_result_folder_full_path
from main.txt_files_config import add_front_dot_to_filenames

def choose_files (all_recipe_names_as_list_of_str):
 
    while True:

        while True:
            print("\nThe following are the available recipes:")

            dictionary = {}
            counter = 1
            for recipe_name in all_recipe_names_as_list_of_str:
                dictionary[counter] = recipe_name
                print(f'{counter} :' + f' {recipe_name}')
                counter += 1

            print("\nPlease choose the recipes to be considered by typing the corresponding digit. Separate the digits using one space." )

            user_input_local = input()

            user_input_no_spaces = user_input_local.replace(" ", "")

            # control if input is numeric (also False if a minus is included, therefore checks if input is positive as well)
            if user_input_no_spaces.isdigit() == False:
                print('Please type one or more valid digits and separate them using one space." )')
                continue
            else:
                break
          
        list_of_int = list (map (lambda x: int(x), user_input_local.split(' ')))

        called_filenames_list_local = []
        for integr in list_of_int:
            called_filenames_list_local += [dictionary.get(integr)]

        # control if input is a valid digit
        if None in called_filenames_list_local:
            print(f"\nOne or more digits you have inserted do not correspond to a recipe. Try again.")
        else:
            break

    print("\nThe selected recipes are the following:")
    print(*add_front_dot_to_filenames(called_filenames_list_local), sep='\n')

    return called_filenames_list_local


def from_recipe_names_to_shopping_list_object (called_recipe_names_list, result_path):
    recipe_objects_list = []
    for recipe_name in called_recipe_names_list:
        recipe_objects_list += [Recipe.retrieve_from_database(recipe_name)]

    shopping_list = Shopping_list.from_list_of_recipes(recipe_objects_list).combine_repetitions()
    # HERE I AM NOT CREATING A SHOPPING LIST OBJECT, NEITHER A TEMPORARY TXT FILE, JUST PRINTING SHOPPING LIST IN TERMINAL
    shopping_list.print_object()
    print("\nApplication has run successfully.")

    return shopping_list


def execute_app ():

    all_recipe_names_as_list_of_str = Recipe.get_all_recipe_names_from_db()
    flag = True

    while flag == True:
        called_recipe_names_list = choose_files(all_recipe_names_as_list_of_str)

        print("\nAre you sure? (yes/no/help)")

        user_input1 = input()   #1
        if user_input1 == 'yes':
            shopping_list_object = from_recipe_names_to_shopping_list_object (called_recipe_names_list, result_full_path)

            while True:
                print ('\nIf you run the application again, your current shopping list will be overwritten. Do you want to save it? (yes/no)')

                user_input2 = input()  #2

                if user_input2 == 'yes':
                    while True:
                        print('\nHow do you want to name it?')
                        shopping_list_name = input()  #3
                        # HERE FOR NOW I KEPT THE TXT FILES (ONLY FOR PERMANENT SHOPPING LIST)
                        current_permanent_shopping_list_full_path = os.path.join(permanent_result_folder_full_path, shopping_list_name + '.txt')

                        if os.path.exists(current_permanent_shopping_list_full_path) == True or Shopping_list.check_database_for(shopping_list_name) != []:
                            print(f'File with name {shopping_list_name} already exists. Try an other name.')
                        else:
                            shopping_list_object.export_to_permanent_txt_file(permanent_result_folder_full_path, shopping_list_name)
                            
                            shopping_list_object = Shopping_list(shopping_list_name, shopping_list_object.list_of_all_ingredients)
                            shopping_list_object.insert_to_database()

                            print('\nYour saved shopping list can be found in ./main/text/result/permanent directory')
                            flag = False
                            break
                    break
                        
                
                elif user_input2 == 'no':
                    flag = False
                    break
                
                else:
                    print(f"The command {user_input2} is not valid. Try again.")


        elif user_input1 == 'no':
            flag = True


        elif user_input1 == 'help':
            subprocess.run(['notepad.exe', readme_full_path], check=True)
            print('\nHopefully that was helpful.')


        else:
            print (f"The command {user_input1} is not valid. Try again.")
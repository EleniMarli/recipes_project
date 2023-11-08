import os
import subprocess

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.paths_config import recipes_full_path, result_full_path, readme_full_path, permanent_result_folder_full_path
from main.txt_files_config import remove_txt_from_filenames, add_front_dot_to_filenames



def choose_files (all_filenames_as_list_of_str_local):
 
    while True:

        while True:
            print("\nThe following are the available recipes:")

            dictionary = {}
            counter = 1
            for file_name in all_filenames_as_list_of_str_local:
                dictionary[counter] = file_name
                print(f'{counter} :' + f' {file_name.replace(".txt","")}' )
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
    remove_txt_from_filenames(called_filenames_list_local)
    print(*add_front_dot_to_filenames(remove_txt_from_filenames(called_filenames_list_local)), sep='\n')

    return called_filenames_list_local



def from_filenames_to_temporary_shopping_list (called_filenames_list_local, recipes_path_local, result_path_local):
    recipe_objects_list = [] # I will end up with a list of all the Recipe objects
    for file_name in called_filenames_list_local:
        recipe_objects_list += [Recipe.from_file(recipes_path_local, file_name)]

    shopping_list = Shopping_list.from_list_of_recipes(recipe_objects_list)

    shopping_list.combine_repetitions()

    shopping_list.export_to_temporary_text_file(result_path_local)

    print("\nApplication has run successfully, the shopping list can be found in the ./main/text/result directory")

    return shopping_list



def execute_app():

    all_filenames_as_list_of_str = os.listdir(recipes_full_path) # list of str: list of all files names in the folder

    flag = True

    while flag == True:
        called_filenames_list = choose_files(all_filenames_as_list_of_str)

        print("\nAre you sure? (yes/no/help)")

        user_input1 = input()   #1
        if user_input1 == 'yes':
            list_for_use = from_filenames_to_temporary_shopping_list (called_filenames_list, recipes_full_path, result_full_path)

            while True:
                print ('\nIf you run the application again, your current shopping list will be overwritten. Do you want to save it? (yes/no)')

                user_input2 = input()  #2

                if user_input2 == 'yes':
                    while True:
                        print('\nHow do you want to name this shopping list?')
                        filename = input()  #3
                        current_permanent_shopping_list_full_path = os.path.join(permanent_result_folder_full_path, filename + '.txt')
                        if os.path.exists(current_permanent_shopping_list_full_path) == True:
                            print(f'File with name {filename} already exists. Try an other name.')
                        else:
                            list_for_use.export_to_permanent_text_file(permanent_result_folder_full_path, filename)
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
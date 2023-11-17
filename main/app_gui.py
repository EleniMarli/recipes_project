from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg

from datetime import datetime

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.paths_config import help_text_full_path


sg.theme('DarkGreen7')


def help_window ():
    with open(help_text_full_path, 'r') as file:

        layout = [  [sg.Text('Help:', font = ('default', 11, 'bold'))],
                    [sg.Multiline(default_text=file.read(), disabled=True, size=(70,13))],
                    [sg.Button('Back')]]

        window = sg.Window('Recipes project',layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Back':
                break
        window.close()


def add_recipe_window():
    
    layout = [  [sg.Text('Add new recipe:', font = ('default', 11, 'bold'))],
                [sg.Text('Name:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
                [sg.Text('Portions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE2-')],
                [sg.Text('Instructions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,10), key='-MULTILINE3-')],
                [sg.Text('Ingredients:', font = ('default', 10))],
                [sg.Multiline('(keep this format: flour, 500 gr)', font = ('default', 10, 'italic'), size=(45,10), key='-MULTILINE4-')],
                [sg.Button('Save'), sg.Button('Help'), sg.Button('Close')]]


    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Save':
            name_of_file = values['-MULTILINE1-']
            portions = float(values['-MULTILINE2-'])
            instructions = values['-MULTILINE3-']
            ingredients_list = values['-MULTILINE4-'].split('\n')

            list_of_ingr_objects = Recipe.create_list_of_ingredients(ingredients_list)

            recipe = Recipe (name_of_file, instructions, portions, list_of_ingr_objects)

            recipe.insert_to_database()
            break

        if event == 'Help':
            help_window()
        
    window.close()


def edit_recipe_window(selected_recipe):

    recipe_object = Recipe.retrieve_from_database(selected_recipe)
    ingredients = recipe_object.get_ingredients_as_str()

    layout = [  [sg.Text('Edit recipe:', font = ('default', 11, 'bold'))],
                [sg.Text('Name:', font = ('default', 10))],
                [sg.Multiline(recipe_object.name, font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
                [sg.Text('Portions:', font = ('default', 10))],
                [sg.Multiline(recipe_object.portions, font = ('default', 10), size=(45,2), key='-MULTILINE2-')],
                [sg.Text('Instructions:', font = ('default', 10))],
                [sg.Multiline(recipe_object.instructions, font = ('default', 10), size=(45,10), key='-MULTILINE3-')],
                [sg.Text('Ingredients:', font = ('default', 10))],
                [sg.Multiline(ingredients, font = ('default', 10), size=(45,10), key='-MULTILINE4-')],
                [sg.Button('Save'), sg.Button('Help'), sg.Button('Close')]]

    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()

        if event == 'Save':
            new_name = values['-MULTILINE1-']
            new_portions = float(values['-MULTILINE2-'])
            new_instructions = values['-MULTILINE3-']
            new_ingredients_list = values['-MULTILINE4-'].split('\n')

            list_of_ingr_objects = Recipe.create_list_of_ingredients(new_ingredients_list)

            updated_recipe_object = Recipe (new_name, new_instructions, new_portions, list_of_ingr_objects)

            Recipe.delete_from_database(recipe_object.name)
            updated_recipe_object.insert_to_database()
            break
        
    window.close()


def delete_recipe_window(selected_recipe):
    layout = [ [sg.Text(f'Are you sure you want to delete {selected_recipe}?', font = ('default', 10))],
                        [sg.Button('Yes'), sg.Button('No')]]
            
    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'No':
            break

        if event == 'Yes':
            Recipe.delete_from_database(selected_recipe)
            break

    window.close()


def manage_recipes_window ():
    all_recipe_names_as_list_of_str = Recipe.get_all_recipe_names_from_db()

    layout = [  [sg.Text('Manage recipes:', font = ('default', 11, 'bold'))],
                [sg.Text('Choose a recipe and edit or delete it:', font = ('default', 10))],
                [sg.Listbox(values = all_recipe_names_as_list_of_str, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, key='-LISTBOX-'), sg.Button ('Delete'), sg.Button ('Edit')],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (20, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (20, 10)))]]
    
    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()

        if event == 'Delete':
            selected_recipe = values['-LISTBOX-'][0]
            delete_recipe_window(selected_recipe)
            all_new_recipe_names_as_list_of_str = Recipe.get_all_recipe_names_from_db()
            window['-LISTBOX-'].update(all_new_recipe_names_as_list_of_str)

        if event == "Edit":
            selected_recipe = values['-LISTBOX-'][0]
            edit_recipe_window(selected_recipe)

    window.close()


def my_recipes_window():

    layout = [  [sg.Text('My recipes:', font = ('default', 11, 'bold'), pad=((10, 0), (10, 10)))],
                [sg.Button('Add new recipe', size=(20, 2), pad=((16, 0), (10, 10)))],
                [sg.Button('Manage my recipes', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (20, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (20, 10)))]]

    window = sg.Window('Recipes project', layout, size=(220, 240))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()            

        if event == 'Add new recipe':
            add_recipe_window()

        if event == 'Manage my recipes':
            manage_recipes_window()
        
    window.close()


def save_shopping_list_window(shopping_list):

    timestamp = datetime.now().strftime(r"%d-%m-%Y (%H:%M)")

    layout = [  [sg.Text('Save shopping list:', font = ('default', 11, 'bold'))],
               [sg.Text('Name:', font = ('default', 10))],
               [sg.Multiline(timestamp, font = ('default', 10, 'italic'), size=(45,2), key='-MULTILINE1-')],
               [sg.Text('Your shopping list:', font = ('default', 10))],
               [sg.Multiline(shopping_list, font = ('default', 10, 'normal'), size=(45,20), key = '-MULTILINE2-')],
               [sg.Button('Save'), sg.Button('Help'), sg.Button('Close')]]
    
    window = sg.Window('Recipes project', layout)
    
    saved_was_clicked = False

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()

        if event == 'Save':
            name_of_shopping_list = values['-MULTILINE1-']
            ingredients_list = values['-MULTILINE2-'].split('\n')

            list_of_ingr_objects = Shopping_list.create_list_of_ingredients(ingredients_list)
            shopping_list_to_save = Shopping_list (name_of_shopping_list, list_of_ingr_objects)

            shopping_list_to_save.insert_to_database()
            saved_was_clicked = True
            break

    window.close()
    return saved_was_clicked


def make_shopping_list_window ():
    all_recipe_names_as_list_of_str = Recipe.get_all_recipe_names_from_db()

    chosen = []

    layout = [  [sg.Text('Create shopping list:', font = ('default', 11, 'bold'))],
                [sg.Text('Choose a recipe and type portions number:', font = ('default', 10))],
                [sg.Listbox(values = all_recipe_names_as_list_of_str, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, key='-LISTBOX1-'), sg.Text('Portions:'), sg.InputText('', size=(2, 1), key='-EDIT-'), sg.Button ('Add')], #!!
                [sg.Text('Chosen recipes:', font = ('default', 10))],
                [sg.Listbox(values = chosen, size=(30, 6), key='-LISTBOX2-' ), sg.Button ('Generate'), sg.Button ('Empty')],
                [sg.Text('Your shopping list:', font = ('default', 10))],
                [sg.Multiline('If you are happy with the chosen recipes and portions click Generate.', font = ('default', 10, 'italic'), size=(45,20), key = '-MULTILINE-'), sg.Button ('Save')],
                [sg.Button('Help'), sg.Button('Close')]]

    window = sg.Window('Recipes project - create shopping list', layout)

    flag = False

    while flag == False:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            flag = True

        if event == 'Help':
            help_window()    

        if event == 'Add':
            selected_recipe = values['-LISTBOX1-'][0]
            portions = values['-EDIT-']
            chosen += [f'(x{portions}) {selected_recipe}']

            window['-LISTBOX2-'].update(chosen)

        if event == 'Empty':
            chosen = []

            window['-LISTBOX2-'].update(chosen)
        
        if event == 'Generate':
            recipes = []

            for choice in chosen:
                split_choice = choice.split(' ')
                recipe_name = ' '.join(split_choice[1::])
                portions = float(split_choice[0][2:-1:])

                recipes += [Recipe.retrieve_from_database(recipe_name).adjust_portions(portions)]

            shopping_list_object = Shopping_list.from_list_of_recipes(recipes).combine_repetitions()

            shopping_list = shopping_list_object.get_ingredients_as_str()

            window['-MULTILINE-'].update(shopping_list, font = ('default', 10, 'normal'))

        if event == 'Save':
            shopping_list_for_saving = values['-MULTILINE-']
            flag = save_shopping_list_window(shopping_list_for_saving)

    window.close()


def edit_shopping_list_window(selected_shopping_list):

    shopping_list_object = Shopping_list.retrieve_from_database(selected_shopping_list)
    ingredients = shopping_list_object.get_ingredients_as_str()

    layout = [  [sg.Text('Edit shopping list:', font = ('default', 11, 'bold'))],
                [sg.Text('Name:', font = ('default', 10))],
                [sg.Multiline(shopping_list_object.name, font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
                [sg.Text('Ingredients:', font = ('default', 10))],
                [sg.Multiline(ingredients, font = ('default', 10), size=(45,10), key='-MULTILINE2-')],
                [sg.Button('Save'), sg.Button('Help'), sg.Button('Close')]]

    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()

        if event == 'Save':
            new_name = values['-MULTILINE1-']
            new_ingredients_list = values['-MULTILINE2-'].split('\n')

            list_of_ingr_objects = Shopping_list.create_list_of_ingredients(new_ingredients_list)

            updated_shopping_list_object = Shopping_list (new_name, list_of_ingr_objects)

            Shopping_list.delete_from_database(shopping_list_object.name)
            updated_shopping_list_object.insert_to_database()
            break
        
    window.close()


def delete_shopping_list_window(selected_shopping_list):
    layout = [ [sg.Text(f'Are you sure you want to delete {selected_shopping_list}?', font = ('default', 10))],
                        [sg.Button('Yes'), sg.Button('No')]]
            
    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'No':
            break

        if event == 'Yes':
            Shopping_list.delete_from_database(selected_shopping_list)
            break
            
    window.close()


def manage_shopping_lists_window ():
    all_shopping_list_names_as_list_of_str = Shopping_list.get_all_shopping_list_names_from_db()

    layout = [  [sg.Text('Manage shopping lists:', font = ('default', 11, 'bold'))],
                [sg.Text('Choose a shopping list and edit or delete it:', font = ('default', 10))],
                [sg.Listbox(values = all_shopping_list_names_as_list_of_str, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, key='-LISTBOX-'), sg.Button ('Delete'), sg.Button ('Edit')],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (20, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (20, 10)))]]

    
    window = sg.Window('Recipes project', layout)

    while True:

        event,values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()

        if event == 'Delete':
            selected_shopping_list = values['-LISTBOX-'][0]
            delete_shopping_list_window(selected_shopping_list)
            all_new_shopping_list_names_as_list_of_str = Shopping_list.get_all_shopping_list_names_from_db()
            window['-LISTBOX-'].update(all_new_shopping_list_names_as_list_of_str)

        if event == "Edit":
            selected_shopping_list = values['-LISTBOX-'][0]
            edit_shopping_list_window(selected_shopping_list)

    window.close()


def my_shopping_lists_window():

    layout = [  [sg.Text('My recipes:', font = ('default', 11, 'bold'), pad=((10, 0), (10, 10)))],
                [sg.Button('Create shopping list', size=(20, 2), pad=((16, 0), (10, 10)))],
                [sg.Button('Manage my shopping lists', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (20, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (20, 10)))]]

    window = sg.Window('Recipes project', layout, size=(220, 240))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()            

        if event == 'Create shopping list':
            make_shopping_list_window()

        if event == 'Manage my shopping lists':
            manage_shopping_lists_window()
        
    window.close()


def main_menu_window():
    layout = [  [sg.Text('Main menu:', font = ('default', 11, 'bold'), pad=((10, 0), (10, 0)))],
                [sg.Text('Welcome to Recipes project ❤️', font = ('default', 10), pad=((10, 0), (10, 10)))],
                [sg.Button('My recipes', size=(20, 2), pad=((16, 0), (10, 10)))],
                [sg.Button('My shopping lists', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (20, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (20, 10)))]]

    window = sg.Window('Recipes project', layout, size=(220, 270))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Help':
            help_window()            

        if event == 'My recipes':
            my_recipes_window()

        if event == 'My shopping lists':
            my_shopping_lists_window()
        
    window.close()


# START

main_menu_window()
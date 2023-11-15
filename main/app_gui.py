from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg
import os

from main.recipe_module import Recipe
from main.shopping_list_module import Shopping_list
from main.main_commands import from_filenames_to_temporary_shopping_list
from main.txt_files_config import remove_txt_from_filenames, add_txt_to_filenames
from main.paths_config import recipes_full_path, result_full_path, help_text_full_path


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
    

    layout2 = [  [sg.Text('Add new recipe:', font = ('default', 11, 'bold'))],
                [sg.Text('Name:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
                [sg.Text('Portions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE2-')],
                [sg.Text('Instructions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,10), key='-MULTILINE3-')],
                [sg.Text('Ingredients:', font = ('default', 10))],
                [sg.Multiline('(i.e. flour, 500 gr)', font = ('default', 10), size=(45,10), key='-MULTILINE4-')],
                [sg.Button('Add'), sg.Button('Help'), sg.Button('Close')]]


    window2 = sg.Window('Recipes project', layout2)

    while True:

        event2,values2 = window2.read()

        if event2 == sg.WIN_CLOSED or event2 == 'Close':
            break

        if event2 == 'Add':
            name_of_file = values2['-MULTILINE1-'] + '.txt'
            portions = float(values2['-MULTILINE2-'])
            instructions = values2['-MULTILINE3-']
            ingredients_list = values2['-MULTILINE4-'].split('\n')

            list_of_ingr_objects = Recipe.create_list_of_ingredients(ingredients_list)

            recipe = Recipe (name_of_file, instructions, portions, list_of_ingr_objects)

            recipe.insert_to_database()
            break

        if event2 == 'Help':
            help_window()
        
    window2.close()

# CONTINUE HERE
def save_shopping_list_window():
    layout4 = [  [sg.Text('Save shopping list:', font = ('default', 11, 'bold'))],
               [sg.Text('Name:', font = ('default', 10))],
               [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
               [sg.Text('Your shopping list:', font = ('default', 10))],
               [sg.Multiline(font = ('default', 10), size=(45,20), key = '-MULTILINE-')],
               [sg.Button('Save'), sg.Button('Help'), sg.Button('Close')]]
    
    window4 = sg.Window('Recipes project', layout4)

    while True:

        event4,values4 = window4.read()

        if event4 == sg.WIN_CLOSED or event4 == 'Close':
            break

        if event4 == 'Help':
            help_window()


def make_shopping_list_window ():
    all_recipe_names_as_list_of_str = Recipe.get_all_recipe_names_from_db()

    filenames = remove_txt_from_filenames(all_recipe_names_as_list_of_str)  ###################### HERE

    chosen = []

    layout3 = [  [sg.Text('Create shopping list:', font = ('default', 11, 'bold'))],
                [sg.Text('Choose a recipe and type portions number:', font = ('default', 10))],
                [sg.Listbox(values = filenames, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, key='-LISTBOX1-'), sg.Text('Portions:'), sg.InputText('', size=(2, 1), key='-EDIT-'), sg.Button ('Add')], #!!
                [sg.Text('Chosen recipes:', font = ('default', 10))],
                [sg.Listbox(values = chosen, size=(30, 6), key='-LISTBOX2-' ), sg.Button ('Generate'), sg.Button ('Empty')],
                [sg.Text('Your shopping list:', font = ('default', 10))],
                [sg.Multiline('Select recipes and click OK', font = ('default', 10, 'italic'), size=(45,20), key = '-MULTILINE-'), sg.Button ('Save')],
                [sg.Button('Help'), sg.Button('Close')]]

    window3 = sg.Window('Recipes project - create shopping list', layout3)

    while True:

        event3, values3 = window3.read()

        if event3 == sg.WIN_CLOSED or event3 == 'Close':
            break

        if event3 == 'Help':
            help_window()    

        if event3 == 'Add':
            selected_recipe = values3['-LISTBOX1-'][0]
            portions = values3['-EDIT-']
            chosen += [f'(x{portions}) {selected_recipe}']

            window3['-LISTBOX2-'].update(chosen)

        if event3 == 'Empty':
            chosen = []

            window3['-LISTBOX2-'].update(chosen)
        
        if event3 == 'Generate':
            recipes = []

            for choice in chosen:
                split_choice = choice.split(' ')
                recipe_name = ' '.join(split_choice[1::]) + '.txt'
                portions = float(split_choice[0][2:-1:])

                recipes += [Recipe.retrieve_from_database(recipe_name).adjust_portions(portions)]

            shopping_list_object = Shopping_list.from_list_of_recipes(recipes).combine_repetitions()

            shopping_list = shopping_list_object.to_str()

            window3['-MULTILINE-'].update(shopping_list, font = ('default', 10, 'normal'))

        if event3 == 'Save':
            save_shopping_list_window()
        
    window3.close()


def main_menu_window():

    layout1 = [  [sg.Text('Main menu:', font = ('default', 11, 'bold'), pad=((10, 0), (10, 0)))],
                [sg.Text('Welcome to Recipes project ❤️', font = ('default', 10), pad=((10, 0), (10, 10)))],
                [sg.Button('Add new recipe', size=(20, 2), pad=((16, 0), (10, 10)))],
                [sg.Button('Create shopping list', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Manage recipes', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Manage shopping lists', size=(20, 2), pad=((16, 0), (0, 10)))],
                [sg.Button('Help', size=(5, 1), pad=((16, 0), (0, 10))), sg.Button('Close', size=(5, 1), pad=((9, 0), (0, 10)))]]


    window1 = sg.Window('Recipes project', layout1, size=(220, 340))

    while True:
        event1, values1 = window1.read()

        if event1 == sg.WIN_CLOSED or event1 == 'Close':
            break

        if event1 == 'Help':
            help_window()            

        if event1 == 'Add new recipe':
            add_recipe_window()

        if event1 == 'Create shopping list':
            make_shopping_list_window ()
        
    window1.close()

# START

main_menu_window()
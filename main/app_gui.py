from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg
import os
import random

from recipe_module import Recipe
from main.main_commands import from_filenames_to_temporary_shopping_list
from main.txt_files_config import remove_txt_from_filenames, add_txt_to_filenames
from main.paths_config import recipes_full_path, result_full_path, help_text_full_path


# playing with the themes:
themes = sg.list_of_look_and_feel_values()
chosen_theme = random.choice(themes)
print('The theme today is ' + chosen_theme)

sg.theme(chosen_theme)  # (previously 'DarkAmber')
# sg.theme('DarkAmber')   # Add a touch of color


def help_window ():
    with open(help_text_full_path, 'r') as file:

        layout = [  [sg.Text('Help:', font = ('default', 11, 'bold'))],
                    [sg.Multiline(default_text=file.read(), disabled=True, size=(70,10))],
                    [sg.Button('Back')]]

        window = sg.Window('Recipes project',layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Back':
                break
        window.close()


def add_recipe_window():
    

    layout2 = [  [sg.Text('Add new recipe:', font = ('default', 11, 'bold'))],
                [sg.Text('Title:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE1-')],
                [sg.Text('Portions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,2), key='-MULTILINE2-')],
                [sg.Text('Instructions:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,10), key='-MULTILINE3-')],
                [sg.Text('Ingredients:', font = ('default', 10))],
                [sg.Multiline(font = ('default', 10), size=(45,10), key='-MULTILINE4-')],
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
            
            recipe.export_to_file()
            break

        if event2 == 'Help':
            help_window()
        
    window2.close()


def make_shoping_list_window ():
    all_filenames_as_list_of_str = os.listdir(recipes_full_path)
    filenames = remove_txt_from_filenames(all_filenames_as_list_of_str)

    layout3 = [  [sg.Text('Create shopping list:', font = ('default', 11, 'bold'))],
                [sg.Text('Choose recipes:', font = ('default', 10))],
                [sg.Listbox(values = filenames, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_MULTIPLE ), sg.Button ('OK')], #!!
                [sg.Text('Your shopping list:', font = ('default', 10))],
                [sg.Multiline('Select some recipes and click OK', font = ('default', 10, 'italic'), size=(45,20))],
                [sg.Button('Help'), sg.Button('Close')]]
    
    window3 = sg.Window('Recipes project - create shopping list', layout3)

    while True:
        event3, values3 = window3.read()

        if event3 == sg.WIN_CLOSED or event3 == 'Close':
            break

        selected_filenames =  values3[0]

        selected_filenames_txt = add_txt_to_filenames(selected_filenames)

        from_filenames_to_temporary_shopping_list (selected_filenames_txt, recipes_full_path, result_full_path)

        if event3 == 'Help':
            help_window()            

        with open (os.path.join(result_full_path, "temporary", "myshoppinglist.txt")) as file: 
            file.readline()
            shopping_list = file.read()

        window3[1].update(shopping_list, font = ('default', 10, 'normal'))
        
    window3.close()



# START

layout1 = [  [sg.Text('Welcome to Recipes Project:\nan easy way to manage recipes and shopping lists', font = ('default', 11, 'bold'))],
            [sg.Button('Add new recipe')], 
            [sg.Button('Create shopping list')],
            [sg.Button('Help'), sg.Button('Close')]]


window1 = sg.Window('Recipes project - main menu', layout1)

while True:
    event1, values1 = window1.read()

    if event1 == sg.WIN_CLOSED or event1 == 'Close':
        break

    if event1 == 'Help':
        help_window()            

    if event1 == 'Add new recipe':
        add_recipe_window()

    if event1 == 'Create shopping list':
        make_shoping_list_window ()
    
window1.close()
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg
import os
from main.main_commands import from_filenames_to_shopping_list

import random

text_folder_path = 'C:/VSCode/recipes_project/main/text'
recipes_path = text_folder_path + '/recipes'
result_path = text_folder_path + '/result'
all_filenames_as_list_of_str = os.listdir(recipes_path)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Choose recipes:')],
            [sg.Listbox( values= all_filenames_as_list_of_str, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_MULTIPLE )],
            [sg.Button('OK')],
            [sg.Text('Your shopping list:')],
            [sg.Multiline('(Select some recipes and click OK)', auto_refresh = True, size=(45,20))],
            [sg.Button('Close')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break

    selected_filenames =  values[0]

    from_filenames_to_shopping_list (selected_filenames, recipes_path, result_path)

    with open(f"C:/VSCode/recipes_project/main/text/result/myshoppinglist.txt") as file:
        file.readline()
        shopping_list = file.read()

    window[1].update(shopping_list)
    
window.close()

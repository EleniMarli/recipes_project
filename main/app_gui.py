from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg
import os
from main.main_commands import from_filenames_to_shopping_list

import random

from main.paths_config import recipes_full_path, result_full_path

all_filenames_as_list_of_str = os.listdir(recipes_full_path)

themes = sg.list_of_look_and_feel_values()
chosen_theme = random.choice(themes)
print('The theme today is ' + chosen_theme)

sg.theme(chosen_theme)  # (previously 'DarkAmber')
# sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Choose recipes:', font = ('default', 11, 'bold'))],
            [sg.Listbox( values= all_filenames_as_list_of_str, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_MULTIPLE )],
            [sg.Button('OK')],
            [sg.Text('Your shopping list:', font = ('default', 11, 'bold'))],
            [sg.Multiline('Select some recipes and click OK', font = ('default', 10, 'italic'), size=(45,20))],
            [sg.Button('Close')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break

    selected_filenames =  values[0]

    from_filenames_to_shopping_list (selected_filenames, recipes_full_path, result_full_path)

    with open (os.path.join(result_full_path, "myshoppinglist.txt")) as file:  #?????
        file.readline()
        shopping_list = file.read()

    window[1].update(shopping_list, font = ('default', 10, 'normal'))
    
window.close()

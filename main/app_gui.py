from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import PySimpleGUI as sg
import os
from main.main_commands import from_filenames_to_shopping_list

import random

from main.paths_config import recipes_full_path, result_full_path, help_text_full_path

all_filenames_as_list_of_str = os.listdir(recipes_full_path)
filenames = []
for name in all_filenames_as_list_of_str:
    first = name.split('.')[0]
    filenames += [first]

# playing with the themes:
themes = sg.list_of_look_and_feel_values()
chosen_theme = random.choice(themes)
print('The theme today is ' + chosen_theme)

sg.theme(chosen_theme)  # (previously 'DarkAmber')
# sg.theme('DarkAmber')   # Add a touch of color



layout1 = [  [sg.Text('Choose recipes:', font = ('default', 11, 'bold'))],
            [sg.Listbox(values = filenames, size=(30, 6), select_mode = sg.LISTBOX_SELECT_MODE_MULTIPLE ), sg.Button ('OK')], #!!
            [sg.Text('Your shopping list:', font = ('default', 11, 'bold'))],
            [sg.Multiline('Select some recipes and click OK', font = ('default', 10, 'italic'), size=(45,20))],
            [sg.Button('Help'), sg.Button('Close')]]



def help_window ():
    with open(help_text_full_path, 'r') as file:

        layout2 = [  [sg.Text('Help')],
                    [sg.Multiline(default_text=file.read(), disabled=True, size=(70,10))],
                    [sg.Button('Back')]]

        window2 = sg.Window('Help',layout2)
        while True:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED or event2 == 'Back':
                break
        window2.close()



# Create the main Window
window1 = sg.Window('Recipes project', layout1)

while True:
    event1, values1 = window1.read()

    if event1 == sg.WIN_CLOSED or event1 == 'Close':
        break

    selected_filenames =  values1[0]

    selected_filenames_txt = []
    for name in selected_filenames:
        first = name + '.txt'
        selected_filenames_txt += [first]

    from_filenames_to_shopping_list (selected_filenames_txt, recipes_full_path, result_full_path)

    if event1 == 'Help':
        help_window()            

    with open (os.path.join(result_full_path, "myshoppinglist.txt")) as file: 
        file.readline()
        shopping_list = file.read()

    window1[1].update(shopping_list, font = ('default', 10, 'normal'))
    
window1.close()
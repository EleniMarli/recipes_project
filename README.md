# A way to create your shopping list
## How does it work?

## Execute using the graphical user interface (currently recommended)
* Install the necessary dependencies by writing on the command line:

        pip install PySimpleGUI

* If your Python distribution does not include Tkinter, you might have to install it, i.e. for Linux: 

        sudo apt install python3-tk -y

* Execute on the command line:
        
        python -u main/app_gui.py

* Each ingredient in the 'Add new recipe', 'Edit recipe', 'Create shopping list' & 'Save shopping list' windows should occupy one line. Currently the format you should use for each ingredient is:

        <name of ingredient>, <amount> <metric unit>

        i.e. egg(s), 1 unit(s)

* Use the same metric unit(s) for ingredients with the same name:

        flour, 100 gr
        flour, 350 gr

## Execute on command line (can't add new recipes from here yet)
* Execute on the command line:
        
        python -u main/app.py
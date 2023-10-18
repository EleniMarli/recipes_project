# A way to create your shopping list
## How does it work?
* Save each recipe as a ```*.txt``` file in the ```main/text/recipes``` directory.

* In the ```main/text/recipe_example``` read the ```recipe_example.txt``` file to understand the format you have to follow.

* Each ingredient in your ```*.txt``` file(s) should occupy one line. Currently the format you should use for each ingredient is:

        <name of ingredient>, <amount> <metric unit>

        i.e. egg(s), 1 unit(s)

* Use the same metric unit(s) for ingredients with the same name:

        flour, 100 gr
        flour, 350 gr

## Execute only on command line
* Execute on the command line:
        
        python -u main/app.py


* Now you have your shopping list in the ```main/text/result``` directory.

## Execute using the graphical user interface
* Install the necessary dependencies by writing on the command line:

        pip install PySimpleGUI

* If your Python distribution does not include Tkinter, you might have to install it, i.e. for Linux: 

        sudo apt install python3-tk -y

* Execute on the command line:
        
        python -u main/app_gui.py

* Now you have your shopping list in the ```main/text/result``` directory and it appears also on the graphical user interface after clicking ```OK```.
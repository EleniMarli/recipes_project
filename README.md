# A way to create your shopping list
## How does it work?
* Save each list of ingredients for a recipe as a ```*.txt``` file in the ```main/text/recipes``` directory.

* Each ingredient in your ```*.txt``` file(s) should occupy one line. Currently the format you should use for each ingredient is:

        <name of ingredient>, <amount> <metric unit>

        i.e. egg(s), 1 unit(s)

* Use the same metric unit(s) for ingredients with the same name:

        flour, 100 gr
        flour, 350 gr

## Execution only on command line
* Execute on the command line:
        
        python -u main/app.py


* Now you have your shopping list in the ```main/text/result``` directory.

## Execute using the graphical user interface
* Execute on the command line:
        
        python -u main/app_gui.py

* Now you have your shopping list in the ```main/text/result``` directory and it appears also on the graphical user interface after clicking ```OK```.
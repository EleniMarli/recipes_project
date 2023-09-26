from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
# print(sys.path)

# i have a collection of text files, each of them is a list of ingredients for a recipe.
# my program collects the ingredients in a "shopping" list 
# it compares for the same ingredients and adds them up 

# recipe1 content:    1 egg(s)                  recipe2 content:    3 egg(s)
#                     250 gr flour                                  50 gr flour
#                     50 gr sugar                                   150 gr sugar
#__________________________________________________________________________________________
# HOW TO ACCESS PRE-EXISTING TEXT FILES:
# file1 = open("C:/VSCode/recipes_project/main/text/recipe1.txt")  #reference correct path: directory and name of file
# file.close()        important to close file at the end
#.read(): reads text file as STRING          .read(4) --> 1 eg

#better: (closes file automatically)
with open("C:/VSCode/recipes_project/main/text/recipe1.txt","r") as file: # "r" --> reads text file as STRING
    file1 = file.read()
    print(file1)
    
#___________________________________________________________________________________________

# HOW TO CREATE AN EMPTY TEXT FILE:
# shopping_list = open("C:/VSCode/recipes_project/main/text/myshoppinglist.txt", "x")   
# creating a text file with the command function "x", if file with this name exists --> Error

shopping_list = open("C:/VSCode/recipes_project/main/text/myshoppinglist.txt", "w")
# This "w" command creates a new file, but unlike the "x", it overwrites any existing file found with the same file name.
#___________________________________________________________________________________________

#HOW TO WRITE SOMETHING IN THE NEW TEXT FILE:
shopping_list.write("Your shopping list:")
#______________________________:_____________________________________________________________

# Function that takes str and returns list with 1st element as float:

def give_list_with_1st_as_float (str_local):
    list_local = str_local.split(' ') #split string into list, identifying space as separator
    list_local[0] = float(list_local[0])
    return list_local

test_str = "1 unit(s) egg(s)"
test_list = give_list_with_1st_as_float(test_str)

print(test_list)

#___________________________________________________________________________________________

from main.ingredient_module import Ingredient  # importing the class Ingredients from the Ingredient.py file

# let's make an Ingredients object:
ingr_obj = Ingredient (test_list[0], test_list[1], test_list[2])

print(ingr_obj.ammount)
print(ingr_obj.metric_unit)
print(ingr_obj.name)

shopping_list.write(f"\n{ingr_obj.ammount} {ingr_obj.metric_unit} of {ingr_obj.name}")
#____________________________________________________________________________________________

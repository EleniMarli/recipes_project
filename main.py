# i have a collection of text files, each of them is a list of ingredients for a recipe.
# my program collects the ingredients in a "shopping" list 
# it compares for the same ingredients and adds them up 

# recipe1 content:    1 egg(s)                  recipe2 content:    3 egg(s)
#                     250 gr flour                                  50 gr flour
#                     50 gr sugar                                   150 gr sugar
#__________________________________________________________________________________________
# HOW TO ACCESS PRE-EXISTING TEXT FILES:
file1 = open("C:/VSCode/recipes_project/Text/recipe1.txt")  # reference correct path: directory and name of file
file2 = open("C:/VSCode/recipes_project/Text/recipe2.txt")

#.read(): reads text file as STRING

ingredients1 = file1.read()  # here i have a STRING containing the ingredients

print(ingredients1)  #if .read(4) --> 1 eg

# file.close() important to close file at the end

#better:
# with open("demo.txt") as file: --> this way file closes automatically at the end
#    print(file.read())
#___________________________________________________________________________________________

# HOW TO CREATE AN EMPTY TEXT FILE:
# shopping_list = open("C:/VSCode/recipes_project/Text/myshoppinglist.txt", "x")   
# creating a text file with the command function "x", if file with this name exists --> Error

shopping_list = open("C:/VSCode/recipes_project/Text/myshoppinglist.txt", "w")
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

#___________________________________________________________________________________________

from Ingredient import Ingredient  # importing the class Ingredients from the Class_Ingredients.py file

# let's make an Ingredients object:
ingr_obj = Ingredient (test_list[0], test_list[1], test_list[2])

print(ingr_obj.ammount)
print(ingr_obj.metric_unit)
print(ingr_obj.name)

shopping_list.write(f"\n{ingr_obj.ammount} {ingr_obj.metric_unit} of {ingr_obj.name}")
#____________________________________________________________________________________________
# function to create an ingredient: reads file and makes ingredient
#def make_ingredient ():
    
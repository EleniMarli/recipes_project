with open("C:/VSCode/recipes_project/main/text/recipes/recipe1.txt") as file: # "r" --> reads text file

    file1 = file.read()  # --> STRING, looks exactly like file reads
    print(file1)

    list_of_strings = file1.split('\n') # splits with new line as separator --> ['1 unit(s) egg(s)', '250 gr flour']
    print(list_of_strings)

    from ingredient_module import Ingredient #^

    list_of_ingredientscl = []
    for str_ingr in list_of_strings:
        list_of_ingredientscl += [Ingredient.from_str_to_ingredient (str_ingr)]  # here I create a list consisting of abstract objects of the Ingredient class, each of them having 3 properties

    from recipe_module import Recipe #^

    recipe_object = Recipe("recipe1", list_of_ingredientscl) #made 1 recipe object with the Ingr of recipe1
    
    print(recipe_object)

    recipe_object.print_object()
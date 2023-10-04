# A list of objects of the Ingredient class, each text file will create 1 object in the Recipe class

from main.ingredient_module import Ingredient

class Recipe:
    def __init__ (self, name_local : str, list_local : list):   # these are just comments
        self.name = name_local
        self.list_of_ingredients = list_local

    @staticmethod
    def from_file (path_local, file_name_local):
        list_of_ingr_objects_for_single_file = []
        with open(path_local + '/' + file_name_local) as file:
            file_lines = file.read()
            file_list_of_str = file_lines.split('\n')  #list of strings
            for str_Ingr in file_list_of_str:
                object_Ingr = Ingredient.from_str_to_ingredient(str_Ingr) # I make Ingredient objects here
                list_of_ingr_objects_for_single_file += [object_Ingr]
            return Recipe(f"{file_name_local}", list_of_ingr_objects_for_single_file)

    def print_object (self):
        print(f"Recipe {self.name} consisting of following ingredients:")
        for ingr in self.list_of_ingredients:
            ingr.print_object()
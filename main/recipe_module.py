class Recipe:   # a collection of objects of the Ingredient class, each text file will create 1 Recipe object
    def __init__ (self, name_local : str, list_local : list):   # these are just comments
        self.name = name_local
        self.list_of_ingredients = list_local

    def print_object (self):
        print(f"Recipe {self.name} consisting of following ingredients:")
        for ingr in self.list_of_ingredients:
            ingr.print_object()
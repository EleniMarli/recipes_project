# A list of objects of the Ingredient class

class Shopping_list:
    def __init__ (self, list_local : list):
        self.list_of_all_ingredients = list_local

    def print_object (self):
        print(f"Shopping list consisting of following ingredients:")
        for ingr in self.list_of_all_ingredients:
            ingr.print_object()
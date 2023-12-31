import os

from main.ingredient_module import Ingredient
from main.databases.db_utils_module import DB_utils

class Recipe:
    def __init__ (self, name_local : str, instructions_local : str, portions_local : float, list_local : list):
        self.name = name_local  # i.e. "Carbonara.txt"
        self.instructions = instructions_local
        self.portions = portions_local
        self.list_of_ingredients = list_local

    @staticmethod
    def create_list_of_ingredients (list_of_ingr_str): # argument = ['egg(s), 4 unit(s)', 'flour, 400 gr']
        list_of_ingr_objects_for_single_file = []
        for str_Ingr in list_of_ingr_str:
            object_Ingr = Ingredient.from_str_to_ingredient(str_Ingr) # I make Ingredient objects here
            list_of_ingr_objects_for_single_file += [object_Ingr]
        return list_of_ingr_objects_for_single_file

    def adjust_portions (self, new_portions):
        proportion = new_portions/self.portions
        self.portions = new_portions
        for ingr in self.list_of_ingredients:
            ingr.amount = round(ingr.amount*proportion,2)
        return Recipe(self.name, self.instructions, self.portions, self.list_of_ingredients)
    
    def get_ingredients_as_str (self):
        result_list = []
        for ingr in self.list_of_ingredients:
            result_list += [ingr.as_str()]
        return '\n'.join(result_list)    # 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier


    # def export_to_txt_file(self, recipes_full_path):
    #     with open (os.path.join(recipes_full_path, self.name), "w") as recipe_file:
    #         recipe_file.write(f"Instructions:\n{self.instructions}\n\nPortions:\n{self.portions}\n\nIngredients:\n{self.__get_ingredients_as_str()}")

    # @staticmethod
    # def from_txt_file (path_local, file_name_local):
    #     # list_of_ingr_objects_for_single_file = []
    #     with open(os.path.join(path_local, file_name_local)) as file:
    #         file_lines = file.read()
    #         file_list_of_str = file_lines.split('\n')

    #         index_Instructions = file_list_of_str.index('Instructions:')
    #         index_Portions = file_list_of_str.index('Portions:')
    #         index_portions_num = index_Portions + 1
    #         index_Ingredients = file_list_of_str.index('Ingredients:')

    #         instructions = file_list_of_str[index_Instructions+1 : index_Portions-1]  # currently a list of strings
    #         portions = float(file_list_of_str[index_portions_num])

    #         index_of_first_ingr = index_Ingredients + 1
    #         list_only_ingredients = file_list_of_str[index_of_first_ingr:]
            
    #         return Recipe(file_name_local, instructions, portions, Recipe.create_list_of_ingredients (list_only_ingredients))


    def insert_to_database (self):
        query = f"""
        INSERT INTO recipes (name, instructions, portions, str_with_all_ingredients) 
        VALUES ('{self.name}', '{self.instructions}', '{self.portions}', '{self.get_ingredients_as_str()}')
        """
        # name = i.e. 'Carbonara.txt'
        # list_of_ingredients column in this form: 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier
        DB_utils.insert_to_recipes_database(query)

    @staticmethod
    def delete_from_database (recipe_name):
        query = f"""
        DELETE FROM recipes 
        WHERE name='{recipe_name}'
        """
        DB_utils.delete_from_recipes_database(query)

    @staticmethod
    def retrieve_from_database (recipe_name):  # recipe_name = i.e. 'Carbonara.txt'
        query = f"""
        SELECT name, instructions, portions, str_with_all_ingredients 
        FROM recipes 
        WHERE name='{recipe_name}'
        """
        name, instructions, portions, ingr = DB_utils.retrieve_from_recipes_database(query)[0]  # ('Carbonara.txt', 'Cook this.', 4.0, 'egg(s), 3.0 unit(s)\nflour, 400.0 gr')
        return Recipe (name, instructions, float(portions), Recipe.create_list_of_ingredients(ingr.split('\n')))

    def check_database_for (recipe_name):
        query = f"""
        SELECT name 
        FROM recipes 
        WHERE name='{recipe_name}'
        """
        result = DB_utils.retrieve_from_recipes_database(query)
        return result   # if it doesnt exist == [], else returns sth
    
    @staticmethod
    def get_all_recipe_names_from_db ():
        results = DB_utils.retrieve_from_recipes_database("SELECT name FROM recipes")
        return [result[0] for result in results]
    

    def print_object (self):
        print(f"Recipe {self.name} consisting of following ingredients:")
        for ingr in self.list_of_ingredients:
            ingr.print_object()


import sqlite3
from main.databases.database_config import access_recipes_database_and_return_con_n_cur

import os
from main.ingredient_module import Ingredient

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



    @staticmethod
    def from_file (path_local, file_name_local):
        # list_of_ingr_objects_for_single_file = []
        with open(os.path.join(path_local, file_name_local)) as file:
            file_lines = file.read()
            file_list_of_str = file_lines.split('\n')

            index_Instructions = file_list_of_str.index('Instructions:')
            index_Portions = file_list_of_str.index('Portions:')
            index_portions_num = index_Portions + 1
            index_Ingredients = file_list_of_str.index('Ingredients:')

            instructions = file_list_of_str[index_Instructions+1 : index_Portions-1]  # currently a list of strings
            portions = float(file_list_of_str[index_portions_num])

            index_of_first_ingr = index_Ingredients + 1
            list_only_ingredients = file_list_of_str[index_of_first_ingr:]
            
            return Recipe(file_name_local, instructions, portions, Recipe.create_list_of_ingredients (list_only_ingredients))


    def adjust_portions (self, new_portions):
        proportion = new_portions/self.portions
        self.portions = new_portions
        for ingr in self.list_of_ingredients:
            ingr.amount = round(ingr.amount*proportion,2)
        return Recipe(self.name, self.instructions, self.portions, self.list_of_ingredients)
    

    def __get_ingredients_as_str (self): # private method
        result_list = []
        for ingr in self.list_of_ingredients:
            result_list += [ingr.as_str()]
        return '\n'.join(result_list)    # 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier


    def export_to_file(self, recipes_full_path):
        with open (os.path.join(recipes_full_path, self.name), "w") as recipe_file:
            recipe_file.write(f"Instructions:\n{self.instructions}\n\nPortions:\n{self.portions}\n\nIngredients:\n{self.__get_ingredients_as_str()}")


    def insert_to_database (self):
        con, cur = access_recipes_database_and_return_con_n_cur()
        data = (self.name, self.instructions, self.portions, self.__get_ingredients_as_str()) # name = i.e. 'Carbonara.txt'
        cur.execute(f"INSERT INTO recipes (name, instructions, portions, str_with_all_ingredients) VALUES (?, ?, ?, ?)", data)
        con.commit()
        con.close()
        # list_of_ingredients column in this form: 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier

    @staticmethod
    def retrieve_from_database (recipe_name):  # recipe_name = i.e. 'Carbonara.txt'
        con, cur = access_recipes_database_and_return_con_n_cur()
        cur.execute(f"SELECT name, instructions, portions, str_with_all_ingredients FROM recipes WHERE name='{recipe_name}'")
        name, instructions, portions, ingr = cur.fetchone()  # ('Carbonara.txt', 'Cook this.', 4.0, 'egg(s), 3.0 unit(s)\nflour, 400.0 gr')
        con.commit()
        con.close()
        return Recipe (name, instructions, portions, Recipe.create_list_of_ingredients(ingr.split('\n')))


    def print_object (self):
        print(f"Recipe {self.name} consisting of following ingredients:")
        for ingr in self.list_of_ingredients:
            ingr.print_object()


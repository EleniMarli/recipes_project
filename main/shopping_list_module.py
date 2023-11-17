# A list of objects of the Ingredient class

import os

from main.ingredient_module import Ingredient
from main.databases.db_utils_module import DB_utils

class Shopping_list:

    def __init__ (self, name_local : str, list_local : list):  # for 2 arguments
        self.name = name_local
        self.list_of_all_ingredients = list_local

    def __init__ (self, list_local : list):  # for 1 argument
        self.name = ''
        self.list_of_all_ingredients = list_local


    @staticmethod
    def from_list_of_recipes (list_of_recipes_local):
        separated_list_of_ingr_objects_for_all_files = []  # [[ingra1,ingra2,ing3], [ingrb1,ingrb2,ingrb3], [ingrc1,ingrc2]]
        for recipe in list_of_recipes_local:
            separated_list_of_ingr_objects_for_all_files += [recipe.list_of_ingredients]

        unified_list_of_ingr_objects_for_all_files = []  # [ingra1,ingra2,ing3,ingrb1,ingrb2,ingrb3, ingrc1,ingrc2]
        for sublist in separated_list_of_ingr_objects_for_all_files:
            for item in sublist:
                unified_list_of_ingr_objects_for_all_files.append(item)

        return Shopping_list (unified_list_of_ingr_objects_for_all_files)


    def combine_repetitions (self):
        names_list_pre_filter = list (map (lambda x : x.name , self.list_of_all_ingredients ))   # [eggs,flour,salt,eggs,flour]
        alphabetical_list_unique_names = sorted(list(set(names_list_pre_filter)))

        list_of_sublists = []
        for unique_name in alphabetical_list_unique_names:
            extra = list (filter ( lambda ingr: ingr.name == unique_name , self.list_of_all_ingredients ))
            list_of_sublists.append(extra)   # with append and not concatenation, i make sublists of ingr within the empty_list!

        sl_without_repetitions = []  # here i make the final shopping list, consisting of Ingredient objects
        for sub in list_of_sublists:  # this works, only if I have the same metric units 
            sum = 0
            for ingr in sub:
                sum += ingr.amount
            object = Ingredient (sum, ingr.metric_unit, ingr.name)
            sl_without_repetitions += [object]

        self.list_of_all_ingredients = sl_without_repetitions

        return self


    def to_str(self):
        list1 = []
        for ingr in self.list_of_all_ingredients:
            list1 += [ingr.as_str()]
        return '\n'.join(list1)


    # def export_to_temporary_txt_file (self, result_path_local):
    #     shop_list = open(os.path.join(result_path_local, 'temporary', "myshoppinglist.txt"), "w") # "w" command creates a new file, but unlike the "x", it overwrites any existing file found with the same file name.
    #     shop_list.write("Your shopping list:\n")
    #     shop_list.write(self.get_ingredients_as_str())

    # HERE FOR NOW I KEPT THE TXT FILES (PERMANENT SHOPPING LIST)
    def export_to_permanent_txt_file (self, permanent_result_folder_full_path, filename_local):
        shop_list = open(os.path.join(permanent_result_folder_full_path, filename_local + '.txt'), "x")
        shop_list.write("Your shopping list:\n")
        shop_list.write(self.get_ingredients_as_str())


    def insert_to_database (self):
        query = f"""
        INSERT INTO shopping_lists (name, str_with_all_ingredients) 
        VALUES ('{self.name}', '{self.get_ingredients_as_str()}')
        """
        DB_utils.insert_to_shopping_lists_database(query)

    @staticmethod
    def delete_from_database (shopping_list_name):
        query = f"""
        DELETE FROM shopping_lists 
        WHERE name='{shopping_list_name}'
        """
        DB_utils.delete_from_shopping_lists_database(query)

    @staticmethod
    def retrieve_from_database (shopping_list_name):
        query = f"""
        SELECT name, str_with_all_ingredients 
        FROM shopping_lists 
        WHERE name='{shopping_list_name}'
        """
        name, ingr = DB_utils.retrieve_from_shopping_lists_database(query)[0]  # ('Carbonara.txt', 'Cook this.', 4.0, 'egg(s), 3.0 unit(s)\nflour, 400.0 gr')
        return Shopping_list (name, Shopping_list.create_list_of_ingredients(ingr.split('\n')))
    
    def check_database_for (shopping_list_name):
        query = f"""
        SELECT name 
        FROM shopping_lists 
        WHERE name='{shopping_list_name}'
        """
        result = DB_utils.retrieve_from_shopping_lists_database(query)
        return result   # if it doesnt exist == [], else returns sth
    
    @staticmethod
    def get_all_shopping_list_names_from_db ():
        results = DB_utils.retrieve_from_shopping_lists_database("SELECT name FROM shopping_lists")
        return [result[0] for result in results]

    def print_object (self):
        print(f"Shopping list consisting of following ingredients:")
        for ingr in self.list_of_all_ingredients:
            ingr.print_object()       
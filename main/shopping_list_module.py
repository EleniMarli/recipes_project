# A list of objects of the Ingredient class

import os

from main.ingredient_module import Ingredient
from main.databases.database_config import access_shopping_lists_database_and_return_con_n_cur

class Shopping_list:

    # CONTINUE HERE!!!!!!!!!!!!!!!!!!!!!!

    def __init__ (self, name_local : str, list_local : list):
        self.name = name_local
        self.list_of_all_ingredients = list_local

    def __init__ (self, list_local : list):
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


    def export_to_temporary_text_file (self, result_path_local):
        shop_list = open(os.path.join(result_path_local, 'temporary', "myshoppinglist.txt"), "w") # "w" command creates a new file, but unlike the "x", it overwrites any existing file found with the same file name.
        shop_list.write("Your shopping list:")
        for ingr in self.list_of_all_ingredients:
            shop_list.write(f"\n{ingr.as_str()}")


    def save_to_database (self, given_name):
        con, cur = access_shopping_lists_database_and_return_con_n_cur()
        data = (f'{given_name}' , f'{self.list_of_all_ingredients}')  # name = i.e. 'Carbonara.txt'
        cur.executemany("INSERT INTO shopping_lists VALUES(?, ?)", data)
        con.commit()
        con.close()
        # list_of_ingredients column in this form: 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier


    def export_to_permanent_text_file (self, permanent_result_folder_full_path, filename_local):
        shop_list = open(os.path.join(permanent_result_folder_full_path, filename_local + '.txt'), "x")
        shop_list.write("Your shopping list:")
        for ingr in self.list_of_all_ingredients:
            shop_list.write(f"\n{ingr.as_str()}")



    def print_object (self):
        print(f"Shopping list consisting of following ingredients:")
        for ingr in self.list_of_all_ingredients:
            ingr.print_object()       
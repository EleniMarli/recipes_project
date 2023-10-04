# A list of objects of the Ingredient class

from main.ingredient_module import Ingredient


class Shopping_list:
    def __init__ (self, list_local : list):
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

    def export_to_text_file (self, path_local):
        shop_list = open(path_local + "/myshoppinglist.txt", "w") # "w" command creates a new file, but unlike the "x", it overwrites any existing file found with the same file name.
        shop_list.write("Your shopping list:")
        for ingr in self.list_of_all_ingredients:
            shop_list.write(f"\n{ingr.amount} {ingr.metric_unit} {ingr.name} ")


    def print_object (self):
        print(f"Shopping list consisting of following ingredients:")
        for ingr in self.list_of_all_ingredients:
            ingr.print_object()
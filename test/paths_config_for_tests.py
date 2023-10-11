import os

absolute_path_test = os.path.dirname(__file__)
recipes_full_path = os.path.join(absolute_path_test, "text", "recipes")
result_full_path = os.path.join(absolute_path_test, "text", "result")
shopping_list_full_path = os.path.join(result_full_path, "myshoppinglist.txt")
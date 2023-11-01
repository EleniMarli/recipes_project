import os

absolute_path_test = os.path.dirname(__file__)

recipes_full_path = os.path.join(absolute_path_test, "text", "recipes")
result_full_path = os.path.join(absolute_path_test, "text", "result")

temporary_shopping_list_full_path = os.path.join(result_full_path, 'temporary', 'myshoppinglist.txt')

permanent_result_folder_full_path = os.path.join(result_full_path, 'permanent')
temporary_result_folder_full_path = os.path.join(result_full_path, 'temporary')

os.makedirs(result_full_path, exist_ok=True)
os.makedirs(temporary_result_folder_full_path, exist_ok=True)
os.makedirs(permanent_result_folder_full_path, exist_ok=True)
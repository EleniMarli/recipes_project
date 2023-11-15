import os

absolute_path_main = os.path.dirname(__file__)

recipes_database_path = os.path.join(absolute_path_main, 'databases', 'recipes_database.db')
shopping_lists_database_path = os.path.join(absolute_path_main, 'databases', 'shopping_lists_database.db')

recipes_full_path = os.path.join(absolute_path_main, 'text', 'recipes')
result_full_path = os.path.join(absolute_path_main, 'text', 'result')
readme_full_path = os.path.join(absolute_path_main, '..', 'README.md')

help_text_full_path = os.path.join(absolute_path_main, 'text', 'help_text', 'help_text.txt')

temporary_shopping_list_full_path = os.path.join(result_full_path, 'temporary', 'myshoppinglist.txt')

permanent_result_folder_full_path = os.path.join(result_full_path, 'permanent')
temporary_result_folder_full_path = os.path.join(result_full_path, 'temporary')

os.makedirs(result_full_path, exist_ok=True)
os.makedirs(temporary_result_folder_full_path, exist_ok=True)
os.makedirs(permanent_result_folder_full_path, exist_ok=True)
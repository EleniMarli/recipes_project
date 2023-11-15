from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[2]))

import sqlite3

from main.paths_config import recipes_database_path, shopping_lists_database_path


def access_recipes_database_and_return_con_n_cur():
    con = sqlite3.connect(f'{recipes_database_path}')
    cur = con.cursor()
    return con, cur


def access_shopping_lists_database_and_return_con_n_cur():
    con = sqlite3.connect(f'{shopping_lists_database_path}')
    cur = con.cursor()
    return con, cur
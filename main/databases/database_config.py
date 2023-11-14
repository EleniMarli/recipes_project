import sqlite3

def access_recipes_database_and_return_con_n_cur():
    con = sqlite3.connect('C:/VSCode/recipes_project/main/databases/recipes_database.db')
    cur = con.cursor()
    return con, cur


def access_shopping_lists_database_and_return_con_n_cur():
    con = sqlite3.connect('C:/VSCode/recipes_project/main/databases/shopping_lists_database.db')
    cur = con.cursor()
    return con, cur
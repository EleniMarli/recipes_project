import sqlite3

from main.paths_config import recipes_database_path, shopping_lists_database_path


class DB_utils:  # utility class

    @staticmethod
    def __access_database_and_return_con_n_cur (db_path):
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        return con, cur

    @staticmethod
    def access_recipes_database_and_return_con_n_cur ():
        return __class__.__access_database_and_return_con_n_cur(recipes_database_path)

    @staticmethod
    def access_shopping_lists_database_and_return_con_n_cur ():
        return __class__.__access_database_and_return_con_n_cur(shopping_lists_database_path)

    @staticmethod
    def __retrieve_from_database (db_path, sql_query) -> list:
        con, cur = __class__.__access_database_and_return_con_n_cur(db_path)
        cur.execute(sql_query)
        data = cur.fetchall()
        con.close()
        return data
    
    @staticmethod
    def retrieve_from_recipes_database (sql_query) -> list:
        return __class__.__retrieve_from_database(recipes_database_path, sql_query)
    
    @staticmethod
    def retrieve_from_shopping_lists_database (sql_query) -> list:
        return __class__.__retrieve_from_database(shopping_lists_database_path, sql_query)

    @staticmethod
    def __insert_to_database (db_path, sql_query):
        con, cur = __class__.__access_database_and_return_con_n_cur(db_path)
        cur.execute(sql_query)
        con.commit()
        con.close()

    @staticmethod
    def insert_to_recipes_database (sql_query) -> list:
        __class__.__insert_to_database(recipes_database_path, sql_query)

    @staticmethod
    def insert_to_shopping_lists_database (sql_query) -> list:
        __class__.__insert_to_database(shopping_lists_database_path, sql_query)  
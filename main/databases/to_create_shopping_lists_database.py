from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[2]))

import sqlite3
import os

from main.paths_config import shopping_lists_database_path

# Name of the database file
con = sqlite3.connect(f'{shopping_lists_database_path}')

# Tool that allows interaction with the database by creating a cursor
cur = con.cursor()

# Create table named "recipes" with COLUMNS for name, instr, portions and ingr
cur.execute("CREATE TABLE shopping_lists (name, str_with_all_ingredients)")

# list_of_ingredients column in this form: 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier

# Commit the transaction
con.commit()  

# Close the connection
con.close()
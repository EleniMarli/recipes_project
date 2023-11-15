from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[2]))

import sqlite3

from main.paths_config import recipes_database_path

# Name of the database file
con = sqlite3.connect(recipes_database_path)

# Tool that allows interaction with the database by creating a cursor
cur = con.cursor()

# Create table named "recipes" with COLUMNS for name, instr, portions and ingr
cur.execute("CREATE TABLE recipes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, instructions TEXT, portions, str_with_all_ingredients TEXT)")
cur.execute("CREATE INDEX idx_name ON recipes(name)")

# list_of_ingredients column in this form: 'flour, 300.0 gr\neggs, 4.0 unit(s)' --> \n can be used to split easier

# Commit the transaction
con.commit()  

# Close the connection
con.close()
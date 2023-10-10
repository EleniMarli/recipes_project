from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import main_commands
import subprocess

print ("Hi! Please read the README file for instructions on how to use this app.")

print ("Do you want to execute the app? (yes/no/help)")

while True:
    user_input = input()
    if user_input == 'yes':
        main_commands.execute_app()
        break
    elif user_input == 'no':
        break
    elif user_input == 'help':
       subprocess.run(['notepad.exe', 'C:/VSCode/recipes_project/README.md'], check=True)
       print('\nHopefully that was helpful. Do you want to execute the app? (yes/no/help)')
    else:
        print (f"The command {user_input} is not valid. Try again.")
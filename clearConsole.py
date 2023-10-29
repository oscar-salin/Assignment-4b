# clearConsole.py
# Function for clearing the screen
# Oscar Salin

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
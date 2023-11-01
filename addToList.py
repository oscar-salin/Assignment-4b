# addToList.py
# Adds a weather object from input from the user to the weather list
# Oscar Salin
from clearConsole import *

def addedList(oldList):
    # cls()
    key = input("Please give a location/city: ").capitalize()
    while True:
        value = input("Please give a temperature (int): ")
        try:
            int(value)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    new_obj = {key: value}
    cls()
    print(f"Added city: {key} with temperature: {value}")
    oldList.append(new_obj)
    return oldList


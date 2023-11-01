# addToList.py
# Adds a weather object from input from the user to the weather list
# Oscar Salin
from clearConsole import *
from mainProgram import updateWeather

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
    print(new_obj)
    new_list = oldList.append(new_obj)
    return oldList


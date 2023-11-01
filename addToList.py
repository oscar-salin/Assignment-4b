# addToList.py
# Adds a weather object from input from the user to the weather list
# Oscar Salin
from clearConsole import cls

def added_list(old_list):
    """Adds a object to the list"""
    # cls()
    key = input("Please give a location/city: ").capitalize()
    while True:
        value = input("Please give a temperature (int): ")
        try:
            value = int(value)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    new_obj = {key: value}
    cls()
    print(f"Added city: {key} with temperature: {value}")
    old_list.append(new_obj)
    return old_list

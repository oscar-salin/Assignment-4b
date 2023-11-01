# removeFromList.py
# removes an element form the list
# Oscar Salin
from clearConsole import *

def removedList(oldList):
    cls()
    key_to_remove = input("Please give a location/city to remove: ").capitalize()
    begin_len = len(oldList)
    for obj in oldList:
        if list(obj.keys())[0] == key_to_remove:
            oldList.remove(obj)
            print(f"Removed {key_to_remove} from the list.")

    new_len = len(oldList)
    if begin_len == new_len:
        print(f"Could not find {key_to_remove} in the list")
    
    return oldList
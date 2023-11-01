# removeFromList.py
# removes an element form the list
# Oscar Salin
from clearConsole import cls

def removed_list(old_list):
    """removes a spesified object"""
    cls()
    key_to_remove = input("Please give a location/city to remove: ").capitalize()
    begin_len = len(old_list)
    for obj in old_list:
        if list(obj.keys())[0] == key_to_remove:
            old_list.remove(obj)
            print(f"Removed {key_to_remove} from the list.")

    new_len = len(old_list)
    if begin_len == new_len:
        print(f"Could not find {key_to_remove} in the list")

    return old_list

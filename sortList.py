# sortList.py
# Sorts the list based on parameters
# Oscar Salin
from clearConsole import cls

def sort_list(old_list):
    """Sorts list based on user input"""
    cls()
    def get_values(d):
        return list(d.values())[0]

    print("Sort list in ascending or descending order?")
    direction = input("Please input asc/desc:")
    cls()
    if direction == "asc":
        sorted_list = sorted(old_list, key=get_values)
        print("sorted list in ascending order")
    elif direction == "desc":
        sorted_list = sorted(old_list, key=get_values, reverse=True)
        print("sorted list in descending order")
    else:
        sorted_list = old_list
        print("Invalid input. List not sorted")


    return sorted_list
# searchList.py
# Searches the list for a specific key
# Oscar Salin
from clearConsole import *

def searchList(weather):
    cls()
    while True:
        search_key = input("Search for a city or 'q' to go back: ").capitalize()
        found = False
        if search_key.lower() == 'q':
            break
        for obj in weather:
            if search_key in obj:
                name, temp = list(obj.items())[0]
                found = True
        cls()
        if found:
            print(f"The temperature in {name} is {temp}")
        else:
            print(f"{search_key} was not found")


    cls()


if __name__ == "__main__":
    input("Please execute mainProgram.py instead of this one :)")

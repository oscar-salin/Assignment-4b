# listWeather.py
# Function for printing all weather objects
# Oscar Salin
from clearConsole import cls

def list_weather(weather):
    """Prints all objects in the list"""
    cls()
    for i in weather:
        name, temp = list(i.items())[0]
        print(f"{name}: {temp}")
    input("\n'q' to go back: ")
    cls()

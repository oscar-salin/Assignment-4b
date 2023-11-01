# listWeather.py
# Function for printing all weather objects
# Oscar Salin
from clearConsole import *

def list_weather(weather):
    cls()
    for i in weather:
        name, temp = list(i.items())[0]
        print(f"{name}: {temp}")
    input("\n'q' to go back: ")
    cls()
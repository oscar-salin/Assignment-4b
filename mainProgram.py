import random
from listWeather import *
from clearConsole import *
from searchList import *
from addToList import *
from removeFromList import *

weather = []

def genData():
    """
    Generate weather data
    """
    finnish_cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Lahti", "Kuopio", "Pori", "Kouvola", "Joensuu", "Lappeenranta", "Hämeenlinna", "Vaasa", "Seinäjoki", "Rovaniemi", "Mikkeli", "Kotka", "Salonkylä", "Porvoo", "Lohja", "Hyvinkää", "Nurmijärvi", "Järvenpää", "Rauma", "Kirkkonummi", "Tuusula", "Kerava", "Hanko", "Sodankylä"]

    for i in range(len(finnish_cities)):
        city = random.choice(finnish_cities)
        finnish_cities.remove(city)
        temperature = random.randint(-15, 30) 
        weather.append({city: temperature})

    print(weather)


def print_options():
    print("\n")
    print("Quit program: q")
    print("List all cities: 1")
    print("Search based on city: 2")
    print("Add a city & temperature: 3")
    print("Remove a city & temperature: 4")

def updateWeather(newWeather):
    global weather
    weather = newWeather

def main():
    cls()
    while True:

        print_options()
        user_input = input("\nInput: ")

        match user_input:
            case "q":
                break
            case "1":
                list_weather(weather)
            case "2":
                searchList(weather)
            case "3":
                updateWeather(addedList(weather))
            case "4":
                updateWeather(removedList(weather))
            case _:
                cls()
                print("Please input a correct option or 'q' to quit")            

if __name__ == "__main__":
    genData()
    main()

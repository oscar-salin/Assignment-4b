import random
from listWeather import *
from clearConsole import *
from searchList import *

"""
Generate weather data
"""
finnish_cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Lahti", "Kuopio", "Pori", "Kouvola", "Joensuu", "Lappeenranta", "Hämeenlinna", "Vaasa", "Seinäjoki", "Rovaniemi", "Mikkeli", "Kotka", "Salonkylä", "Porvoo", "Lohja", "Hyvinkää", "Nurmijärvi", "Järvenpää", "Rauma", "Kirkkonummi", "Tuusula", "Kerava", "Hanko", "Sodankylä"]
weather = []

for i in range(len(finnish_cities)):
    city = random.choice(finnish_cities)
    finnish_cities.remove(city)
    temperature = random.randint(-15, 30) 
    weather.append({city: temperature})

# print(weather)


def print_options():
    print("\n")
    print("Quit program: q")
    print("List all cities: 1")
    print("Search based on city: 2")


def main():
    cls()
    while True:

        print_options()
        user_input = input("\nInput: ")

        if user_input.lower() == "q":
            break
        if user_input == "1":
            list_weather(weather)
        elif user_input == "2":
            searchList(weather)

        else:
            cls()
            print("Please input a correct option or 'q' to quit")

if __name__ == "__main__":
    main()

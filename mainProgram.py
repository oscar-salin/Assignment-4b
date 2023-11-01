"""mainProgram.py"""
import random
from listWeather import list_weather
from clearConsole import cls
from searchList import search_list
from addToList import added_list
from removeFromList import removed_list
from sortList import sort_list

weather = []

def gen_data():
    """
    Generate weather data
    """

    finnish_cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku",
                        "Jyväskylä", "Lahti", "Kuopio", "Pori", "Kouvola",
                        "Joensuu", "Lappeenranta", "Hämeenlinna", "Vaasa", "Seinäjoki",
                        "Rovaniemi", "Mikkeli", "Kotka", "Salonkylä", "Porvoo", "Lohja", 
                        "Hyvinkää", "Nurmijärvi","Järvenpää", "Rauma", "Kirkkonummi", 
                        "Tuusula", "Kerava", "Hanko", "Sodankylä"]

    for _ in range(len(finnish_cities)):
        city = random.choice(finnish_cities)
        finnish_cities.remove(city)
        temperature = random.randint(-15, 30)
        weather.append({city: temperature})

    print(weather)


def print_options():
    """
    prints all options
    """
    print()
    print("Quit program: q")
    print("List all cities: 1")
    print("Search based on city: 2")
    print("Add a city & temperature: 3")
    print("Remove a city & temperature: 4")
    print("Sort the list: 5")

def update_weather(new_weather):
    """
    modifies global weather variable
    """
    # pylint: disable=locally-disabled, global-statement
    global weather
    weather = new_weather

def main():
    """Main loop"""
    cls()
    while True:

        print_options()
        user_input = input("\nInput: ")

        match user_input:
            case "q":
                break
            case "Q":
                break
            case "1":
                list_weather(weather)
            case "2":
                search_list(weather)
            case "3":
                update_weather(added_list(weather))
            case "4":
                update_weather(removed_list(weather))
            case "5":
                update_weather(sort_list(weather))
            case _:
                cls()
                print("Please input a correct option or 'q' to quit\n")            

if __name__ == "__main__":
    gen_data()
    main()

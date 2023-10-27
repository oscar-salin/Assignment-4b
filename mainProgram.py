import random


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
    print("List all cities: 1")
    print("Search based on city: 2")

def main():
    while True:
        print_options()
        try:
            user_input = input("Input: ")
            if user_input.lower() == "q":
                break
            user_input = int(user_input)

            if user_input == 1:
                print("Here is the weather data:", weather)
            if user_input == 2:
                raise ValueError()
        except ValueError:
            print("Please use a valid option or 'q' to quit")

if __name__ == "__main__":
    main()

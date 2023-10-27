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
    weather.append({str(city): temperature})

print(weather)


def main():
    while True:
        try:
            user_input = float(input("Please enter 1: "))
            print("Here is the weather data:", weather)
        except ValueError:
            user_input = input("Invalid input. Please enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break

if __name__ == "__main__":
    main()

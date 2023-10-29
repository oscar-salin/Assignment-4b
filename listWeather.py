# listWeather.py
# Function for printing all weather objects
# Oscar Salin

def list_weather(weather):
    for i in weather:
        name, temp = list(i.items())[0]
        print(f"{name}: {temp}")
    input("q to close: ")
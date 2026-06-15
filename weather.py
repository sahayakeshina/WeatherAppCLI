import requests

API_KEY = "cbafe4e44f379d7052d777da0edb443d*"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        print("\n Weather Report")
        print("----------------------")
        print("City:", city)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
    else:
        print("* City not found")

while True:
    city = input("\nEnter city name (or type 'exit'): ")

    if city.lower() == "exit":
        print(" Goodbye")
        break

    get_weather(city)
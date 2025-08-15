import requests
from datetime import datetime

# Replace with your actual API key and city
API_KEY = 'your_openweathermap_api_key'
CITY = 'London'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f"{datetime.now().strftime('%Y-%m-%d')}: Weather in {CITY}: {weather}, Temperature: {temp}°C")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data.')}")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == '__main__':
    get_weather()
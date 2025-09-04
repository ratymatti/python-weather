import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_API_KEY") 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a city from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

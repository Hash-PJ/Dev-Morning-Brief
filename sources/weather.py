from sources.base import BaseSource
import os


class WeatherSource(BaseSource):
    URL = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city):
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            print("Error: WEATHER_API_KEY missing from .env!")
            return None

        params = {"q": city, "appid": api_key, "units": "metric"}

        data = self.get(self.URL, params=params)
        if data is None:
            return None

        weather = {
            "city": f'{data.get("name", "Unknown")}, {data.get("sys", {}).get("country", "?")}',
            "temperature": f'{data.get("main", {}).get("temp", "N/A")} °C',
            "feels like": f'{data.get("main", {}).get("feels_like", "N/A")} °C',
            "description": data.get("weather", [{}])[0].get("description", "N/A"),
            "humidity": f'{data.get("main", {}).get("humidity", "N/A")} %'
        }
        return weather

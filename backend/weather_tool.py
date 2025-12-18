import requests
import os

def get_weather(city: str) -> str:
    try:
        api_key = os.getenv("WEATHER_API_KEY")

        if not city or city.strip() == "":
            return "Please provide a valid city name."

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        response = requests.get(url, timeout=5)
        data = response.json()

        # 🚨 City not found
        if data.get("cod") == "404":
            return f"Sorry, I couldn't find weather information for '{city}'."

        # 🚨 API error
        if response.status_code != 200:
            return "Weather service is temporarily unavailable. Please try again later."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"The temperature in {city} is {temp}°C with {desc}."

    except requests.exceptions.Timeout:
        return "Weather service timed out. Please try again."

    except Exception:
        return "An unexpected error occurred while fetching weather."

import tabulate
from services.weather.schemas import SWeather


def weather_print(weather: SWeather) -> str:
    data = [
        ["city", f"{weather.city}"],
        ["time", f"{weather.time}"],
        ["temperature", f"{weather.temperature}°C"],
        ["condition", f"{weather.condition}"],
        ["wind_speed", f"{weather.wind_speed}km/h"],
        ["humidity", f"{weather.humidity}%"],
        ["cloud", f"{weather.cloud}%"],
    ]
    weather_display = tabulate.tabulate(data)
    return weather_display

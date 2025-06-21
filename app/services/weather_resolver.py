import httpx
from settings import settings

from .schemas import SWeather


class WeatherResolverError(Exception):
    """any exception related with resolve user weather"""


class WeatherResolverAPIError(WeatherResolverError):
    """any exception related with weather API"""


class WeatherResolverParseError(WeatherResolverError):
    """any exception related with parse response"""


class WeatherResolverService:
    @classmethod
    def get_weather(cls, user_city: str) -> SWeather:
        response = cls.__get_response(user_city)
        cls.__validate_response(response)
        return cls.__extract_weather_from_response(response)

    @staticmethod
    def __get_response(user_city: str) -> httpx.Response:
        return httpx.get(settings.CHECK_WEATHER_URL + user_city)

    @staticmethod
    def __validate_response(response: httpx.Response):
        if not response.is_success:
            raise WeatherResolverAPIError

    @staticmethod
    def __extract_weather_from_response(response: httpx.Response) -> SWeather:
        weather_data = response.json()
        city = weather_data["location"]["name"]
        time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        wind_speed = weather_data["current"]["wind_kph"]
        humidity = weather_data["current"]["humidity"]
        cloud = weather_data["current"]["cloud"]

        return SWeather(
            city=city,
            time=time,
            temperature=temperature,
            condition=condition,
            wind_speed=wind_speed,
            humidity=humidity,
            cloud=cloud,
        )

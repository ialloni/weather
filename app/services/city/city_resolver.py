import httpx
from settings import settings

from .exceptions import CityResolverAPIError, CityResolverParseError


class CityResolverService:
    @classmethod
    def get_city(cls, user_ip: str) -> str:
        response = cls.__get_response(user_ip)
        cls.__validate_response(response)
        return cls.__get_city_from_response(response)

    @staticmethod
    def __get_response(user_ip: str) -> httpx.Response:
        return httpx.get(
            settings.CHECK_CITY_URL + user_ip + "?token=" + settings.CITY_API_KEY
        )

    @staticmethod
    def __validate_response(response: httpx.Response) -> None:
        if not response.is_success:
            raise CityResolverAPIError

    @staticmethod
    def __get_city_from_response(response: httpx.Response) -> str:
        city_data = response.json()
        city = city_data["city"]
        if city is None:
            raise CityResolverParseError
        return city

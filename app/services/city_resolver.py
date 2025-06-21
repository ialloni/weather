import json
import re

import httpx
from settings import settings


class CityResolverError(Exception):
    """any exceptions related with user city"""


class CityResolverAPIError(CityResolverError):
    """any exceptions related with API"""


class CityResolverParseError(CityResolverError):
    """any exceptions related with handling response"""


class CityResolverService:
    @classmethod
    def get_city(cls, user_ip) -> str:
        response = cls.__get_response(user_ip)
        cls.__validate_response(response)
        return cls.__get_city_from_response(response)

    @staticmethod
    def __get_response(user_ip: str) -> httpx.Response:
        return httpx.get(settings.CHECK_CITY_URL + user_ip)

    @staticmethod
    def __validate_response(response: httpx.Response) -> None:
        if not response.is_success:
            raise CityResolverAPIError

    @staticmethod
    def __get_city_from_response(response: httpx.Response) -> str:
        json_data = response.content.decode()
        data = json.loads(json_data)
        if data.get("city") is None:
            raise CityResolverParseError
        return data.get("city")

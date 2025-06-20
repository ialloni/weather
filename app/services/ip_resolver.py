import re

import httpx
from settings import settings


class IpResolverAPIError(Exception):
    """any error related connect to API"""


class IpResolverValidateError(Exception):
    """any error related to API"""


class IpResolverResponseError(Exception):
    """any error in handling the response"""


class IpResolverService:
    @classmethod
    def get_ip(cls) -> str:
        response = cls.__get_response()
        cls.__validate_response(response)
        return cls.__extract_ip_from_response(response)

    @staticmethod
    def __get_response() -> httpx.Response:
        return httpx.get(settings.CHECK_IP_URL)

    @staticmethod
    def __validate_response(res: httpx.Response) -> None:
        if not res.is_success:
            raise IpResolverAPIError

    @staticmethod
    def __extract_ip_from_response(res: httpx.Response) -> str:
        ip_groups = re.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(res.text)
        if ip_groups is None:
            raise IpResolverValidateError
        return ip_groups.group(1)

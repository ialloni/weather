class CityResolverError(Exception):
    """any exceptions related with user city"""


class CityResolverAPIError(CityResolverError):
    """any exceptions related with API"""


class CityResolverParseError(CityResolverError):
    """any exceptions related with handling response"""

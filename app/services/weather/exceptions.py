class WeatherResolverError(Exception):
    """any exception related with resolve user weather"""


class WeatherResolverAPIError(WeatherResolverError):
    """any exception related with weather API"""

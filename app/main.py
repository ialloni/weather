from services.city_resolver import (
    CityResolverAPIError,
    CityResolverParseError,
    CityResolverService,
)
from services.ip_resolver import (
    IpResolverAPIError,
    IpResolverParseError,
    IpResolverService,
)
from services.weather_resolver import (
    WeatherResolverAPIError,
    WeatherResolverParseError,
    WeatherResolverService,
)


def main():
    try:
        user_ip = IpResolverService.get_ip()
        user_city = CityResolverService.get_city(user_ip)
        user_weather = WeatherResolverService.get_weather(user_city)
        print(user_weather)
    except IpResolverAPIError:
        print("exception while connect to API for resolve your IP ")
        exit(1)
    except IpResolverParseError:
        print("exception while extract IP from API response")
        exit(1)
    except CityResolverAPIError:
        print("exception while connect to API for resolve your city")
        exit(1)
    except CityResolverParseError:
        print("exception while extract city from API response")
        exit(1)


if __name__ == "__main__":
    main()

from services import city, ip, weather


def main():
    try:
        user_ip = ip.ip_resolver.IpResolverService.get_ip()
        user_city = city.city_resolver.CityResolverService.get_city(user_ip)
        user_weather = weather.weather_resolver.WeatherResolverService.get_weather(
            user_city
        )
        print(user_weather)
    except ip.exceptions.IpResolverAPIError:
        print("exception while connect to API for resolve your IP ")
        exit(1)
    except ip.exceptions.IpResolverParseError:
        print("exception while extract IP from API response")
        exit(1)
    except city.exceptions.CityResolverAPIError:
        print("exception while connect to API for resolve your city")
        exit(1)
    except city.exceptions.CityResolverParseError:
        print("exception while extract city from API response")
        exit(1)
    except weather.exceptions.WeatherResolverAPIError:
        print("exception while connect to API for resolve weather")
        exit(1)


if __name__ == "__main__":
    main()

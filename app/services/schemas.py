import datetime

from pydantic import BaseModel


class SWeather(BaseModel):
    city: str
    time: datetime.datetime
    temperature: float
    condition: str
    wind_speed: float
    humidity: int
    cloud: int

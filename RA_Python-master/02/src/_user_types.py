from enum import Enum
from dataclasses import dataclass


class DefaultColor(Enum):
    Red = (255, 0, 0),
    Green = (0, 255, 0),
    Blue = (0, 0, 255),
    Black = (255, 255, 255),
    White = (0, 0, 0),


color = DefaultColor.Red
print(color)
print(color.name, color.value)


@dataclass
class Location:
    latitude: float
    longitude: float
    label: str


location = Location(56.484640, 84.947649, 'Tomsk')
print(location)

assert location.latitude == 56.484640
assert location.longitude == 84.947649
assert location.label == 'Tomsk'

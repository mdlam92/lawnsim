"""The lawn area dataclass representations."""
from dataclasses import dataclass

from location import Location


@dataclass
class LawnRectangle:
    location: Location
    width: float
    height: float

"""The lawn representation"""
from dataclasses import dataclass

from hose import Hose
from lawn_area import LawnRectangle
from spigot import Spigot
from sprinkler import Sprinkler


@dataclass
class Lawn:
    rectangles: list[LawnRectangle]
    spigots: list[Spigot]
    hoses: list[Hose]
    sprinklers: list[Sprinkler]

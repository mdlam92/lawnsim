"""The spicket dataclass representations."""
from dataclasses import dataclass

from location import Location
from water_sink import WaterSink
from water_source import WaterSource


@dataclass
class Spigot(WaterSource):
    location: Location
    sink: WaterSink = None

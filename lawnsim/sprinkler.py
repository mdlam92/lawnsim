"""The sprinkler representations."""
from dataclasses import dataclass

from hose import Hose
from location import Location
from water_source import WaterSource
from water_sink import WaterSink


@dataclass
class Sprinkler(
    WaterSink, WaterSource
):  # Sprinkler is sink, but can also be a source if it has an outlet hose
    location: Location
    spray_arc: float
    spray_direction: float
    spray_radius: float
    sink: WaterSink = None
    source: WaterSource = None
    water_flow_rate: float = 40.0

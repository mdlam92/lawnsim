"""The hose datacalss representations."""
from dataclasses import dataclass

from water_sink import WaterSink
from water_source import WaterSource


@dataclass
class Hose(WaterSource, WaterSink):
    length: float
    sink: WaterSink = None
    source: WaterSource = None

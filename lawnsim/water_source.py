"""The abstract water source representations."""
from abc import ABC

from water_sink import WaterSink


class WaterSource(ABC):
    """The abstract water source representations."""

    def __init__(self):
        self.sink = None

    def connect(self, sink: WaterSink):
        self.sink = sink
        sink.source = self

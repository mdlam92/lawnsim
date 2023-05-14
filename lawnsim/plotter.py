"""Plotter."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D

from hose import Hose
from lawn import Lawn
from lawn_area import LawnRectangle
from location import Location
from spigot import Spigot
from sprinkler import Sprinkler


lavender_rectangle = LawnRectangle(
    location=Location(x=0.0, y=0.0), width=13.5, height=15.0
)
middle_rectangle = LawnRectangle(
    location=Location(x=13.5, y=5.0),
    width=10.5,
    height=10,
)
trench_rectangle = LawnRectangle(
    location=Location(x=24.0, y=0.0),
    width=5.0,
    height=15.0,
)

rectangles = [lavender_rectangle, middle_rectangle, trench_rectangle]

walkway_spigot = Spigot(location=Location(29.0, -20.0))
side_spigot = Spigot(location=Location(3.0, 0))

hydrangea_hose = Hose(
    length=25.0,
)
tulip_hose = Hose(
    length=25.0,
)
hydrangea_sprinkler = Sprinkler(
    location=Location(x=29.0, y=8.0),
    spray_arc=190.0,
    spray_direction=180,
    spray_radius=8.5,
)

tulip_sprinkler = Sprinkler(
    location=Location(x=15.0, y=15.0),
    spray_arc=190.0,
    spray_direction=270,
    spray_radius=10.0,
)
walkway_spigot.connect(sink=hydrangea_hose)
hydrangea_hose.connect(sink=hydrangea_sprinkler)
hydrangea_sprinkler.connect(sink=tulip_hose)
tulip_hose.connect(sink=tulip_sprinkler)


little_lavender_hose = Hose(
    length=10.0,
)
corner_sprinkler = Sprinkler(
    location=Location(x=0.0, y=0.0),
    spray_arc=90.0,
    spray_direction=45,
    spray_radius=14.5,
)
side_spigot.connect(sink=little_lavender_hose)
little_lavender_hose.connect(sink=corner_sprinkler)
lavender_hose = Hose(
    length=25.0,
)
lavender_sprinkler = Sprinkler(
    location=Location(x=0.0, y=15.0),
    spray_arc=90,
    spray_direction=315,
    spray_radius=14.0,
)
corner_sprinkler.connect(sink=lavender_hose)
lavender_hose.connect(sink=lavender_sprinkler)


spigots = [walkway_spigot, side_spigot]
hoses = [hydrangea_hose, tulip_hose, little_lavender_hose, lavender_hose]
sprinklers = [
    hydrangea_sprinkler,
    tulip_sprinkler,
    corner_sprinkler,
    lavender_sprinkler,
]

lawn = Lawn(
    rectangles=rectangles,
    spigots=spigots,
    hoses=hoses,
    sprinklers=sprinklers,
)


class LawnSimulator:
    def __init__(self, lawn):
        self.lawn = lawn

    def plot(self):
        fig, ax = plt.subplots()

        # Plot lawn rectangles
        for rectangle in self.lawn.rectangles:
            lawn_patch = patches.Rectangle(
                (rectangle.location.x, rectangle.location.y),
                rectangle.width,
                rectangle.height,
                fill=True,
                color="green",
            )
            ax.add_patch(lawn_patch)

        # Plot hoses
        for hose in self.lawn.hoses:
            ax.plot(
                [hose.source.location.x, hose.sink.location.x],
                [hose.source.location.y, hose.sink.location.y],
                color="black",
            )

        # Plot spigots
        for spigot in self.lawn.spigots:
            ax.plot(spigot.location.x, spigot.location.y, "bo")

        # Plot sprinklers and their spray arcs
        for sprinkler in self.lawn.sprinklers:
            ax.plot(sprinkler.location.x, sprinkler.location.y, "ro")
            sprinkler_patch = patches.Wedge(
                (sprinkler.location.x, sprinkler.location.y),
                sprinkler.spray_radius,
                sprinkler.spray_direction - sprinkler.spray_arc / 2,
                # theta1 (start angle)
                sprinkler.spray_direction + sprinkler.spray_arc / 2,
                # theta2 (end angle)
                fill=False,
                color="blue",
            )
            ax.add_patch(sprinkler_patch)

        # Set the aspect of the plot to match the real-world aspect
        ax.set_aspect("equal")

        # Show the plot
        plt.show()


if __name__ == "__main__":
    lawn_simulator = LawnSimulator(lawn=lawn)
    lawn_simulator.plot()

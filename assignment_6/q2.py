from task.geometric_object import GeometricObject
import math
from abc import ABC, abstractmethod

class GeometricObject(ABC):

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return self.color

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled
        return self.filled

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Cone(GeometricObject):
    def __init__(self, radius, vertical_height, slant_height, color, filled):
        self.radius = radius
        self.vertical_height = vertical_height
        self.slant_height = slant_height
        self.color = color
        self.filled = filled

    def area(self):
        area = (math.pi * (self.radius **2)) + (math.pi * self.radius * self.slant_height)
        return round(area, 2)

    def volume(self):
        volume = (1/3) * math.pi * (self.radius ** 2) * self.vertical_height
        return round(volume, 2)

class Cylinder(GeometricObject):
    def __init__(self, radius, height, color, filled):
        self.radius = radius
        self.height = height
        self.color = color
        self.filled = filled

    def area(self):
        area = (2 * math.pi * (self.radius ** 2)) + (2 * math.pi * self.radius * self.height)
        return round(area, 2)

    def volume(self):
        volume = math.pi * (self.radius ** 2) * self.height
        return round(volume, 2)

class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        self.side_length = side_length
        self.color = color
        self.filled = filled

    def area(self):
        area = 6 * (self.side_length ** 2)
        return round(area, 2)

    def volume(self):
        volume = self.side_length ** 3
        return round(volume, 2)

import math


class MagicClass:
    def __init__(self, radius):
        self._MagicClass__Radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__Radius = radius

    def area(self):
        return ((self._MagicClass__Radius ** 2) * math.pi)

    def circumference(self):
        return (2 * math.pi * self._MagicClass__radius)

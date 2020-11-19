import math


class SodaCan:
    def setHeight(self, height):
        self.height = height

    def setRadius(self, radius):
        self.radius = radius

    def getSurfaceArea(self):
        A = (2 * math.pi * self.radius * self.height) + 2 * math.pi * self.radius**2
        return A

    def getVolume(self):
        V = math.pi * self.radius ** 2 * self.height
        return V

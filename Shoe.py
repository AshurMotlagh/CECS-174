class Shoes:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def getType(self):
        return "shoes"

    def describe(self):
        return self.color + self.getType() + ':' + "size" + self.size


class Boots(Shoes):
    def __init__(self, color, size,  height):
        super().__init__(color, size) # calling
        self.height = height

    def getType(self):
        return "boots"

    def describe(self):
        return super().describe() + self.height


class Sneakers(Boots):
    def __init__(self, lace_color, color, size, height):
        super().__init__(height, color, size)
        self.lace_color = lace_color

    def getType(self):
        return "sneakers"

    def describe(self):
        return super().describe() + self.lace_color

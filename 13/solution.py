class ThresholdEqual():

    def __init__(self, value):
        self.x = value
        self.threshold = 2

    def __eq__(self, other):
        return abs(self.x - other.x) <= self.threshold

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

    def __mod__(self, other):
        return self.x % other.x

    def __pow__(self, power, modulo=None):
        return self.x ** power.x

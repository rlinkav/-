import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

p= Point(3, 4)
print(p.distance_to_zero())




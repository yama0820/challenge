import math

class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius * self.radius * math.pi

circle = Circle(2)
print(circle.area())

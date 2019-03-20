class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height /2

tr1 = Triangle(2,4)
print(tr1.area())
